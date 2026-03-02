#!/usr/bin/env bash
set -euo pipefail

usage() { echo "Usage: $0 -p <project_name> -b <branch> [-r <docs_repo_url>] [-d <docs_repo_dir>] [-c <code_repo_dir>]"; exit 2; }

PROJECT_NAME=""
BRANCH=""
DOCS_REPO_URL="${DOCS_REPO_URL:-git@github.com:sandeep-i2o/i2o-project-ai-docs.git}"
DOCS_REPO_DIR="${DOCS_REPO_DIR:-$HOME/temp/i2o-project-ai-docs}"
CODE_REPO_DIR="${CODE_REPO_DIR:-$(pwd)}"

while getopts ":p:b:r:d:c:" opt; do
  case $opt in
    p) PROJECT_NAME="$OPTARG" ;;
    b) BRANCH="$OPTARG" ;;
    r) DOCS_REPO_URL="$OPTARG" ;;
    d) DOCS_REPO_DIR="$OPTARG" ;;
    c) CODE_REPO_DIR="$OPTARG" ;;
    *) usage ;;
  esac
done
[[ -z "$PROJECT_NAME" || -z "$BRANCH" ]] && usage

mkdir -p "$(dirname "$DOCS_REPO_DIR")"
if [[ ! -d "$DOCS_REPO_DIR/.git" ]]; then
  git clone "$DOCS_REPO_URL" "$DOCS_REPO_DIR"
else
  git -C "$DOCS_REPO_DIR" fetch --all
fi

if [[ ! -d "$CODE_REPO_DIR/.git" ]]; then
  echo "Code repo directory is not a git repository: $CODE_REPO_DIR"
  exit 2
fi

git -C "$CODE_REPO_DIR" fetch --all

if ! git -C "$CODE_REPO_DIR" show-ref --verify --quiet "refs/remotes/origin/$BRANCH"; then
  echo "Branch $BRANCH not found in remote."
  exit 3
fi

git -C "$CODE_REPO_DIR" checkout "$BRANCH"
git -C "$CODE_REPO_DIR" pull origin "$BRANCH"

BASE=""
for cand in main master develop; do
  if git -C "$CODE_REPO_DIR" show-ref --verify --quiet "refs/remotes/origin/$cand"; then
    BASE="$cand"; break
  fi
done
if [[ -z "$BASE" ]]; then
  echo "No base branch found (main/master/develop)."
  exit 4
fi

OUT="/tmp/review-code-skill/$PROJECT_NAME/$BRANCH"
mkdir -p "$OUT"

git -C "$CODE_REPO_DIR" -c core.pager=cat diff "origin/$BASE...$BRANCH" > "$OUT/diff.txt" || true
git -C "$CODE_REPO_DIR" diff --name-only "origin/$BASE...$BRANCH" > "$OUT/changed_files.txt" || true

if [[ ! -s "$OUT/diff.txt" ]]; then
  echo "No changes found between origin/$BASE and $BRANCH. Nothing to review."
  exit 5
fi

awk -F. 'NF>1 {print tolower($NF)}' "$OUT/changed_files.txt" | sort -u > "$OUT/changed_exts.txt" || true

ARCH="$DOCS_REPO_DIR/projects/$PROJECT_NAME/docs/design/architecture.md"
PRD="$DOCS_REPO_DIR/projects/$PROJECT_NAME/docs/requirements/prd.md"

if [[ ! -f "$ARCH" ]]; then
  echo "Missing architecture.md for project $PROJECT_NAME. Cannot proceed."
  exit 6
fi
if [[ ! -f "$PRD" ]]; then
  echo "Missing prd.md for project $PROJECT_NAME. Cannot proceed."
  exit 7
fi

cp "$ARCH" "$OUT/architecture.md"
cp "$PRD" "$OUT/prd.md"

printf "OK\nCODE_REPO_DIR=%s\nDOCS_REPO_DIR=%s\nBASE=%s\nOUT=%s\n" "$CODE_REPO_DIR" "$DOCS_REPO_DIR" "$BASE" "$OUT"
