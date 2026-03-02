#!/usr/bin/env bash
set -euo pipefail

usage() { echo "Usage: $0 -u <pr_url> -t <ticket_id> -p <project_name> -b <branch> -C <critical> -W <warnings> -S <suggestions> -A <align> -M <summary>"; exit 2; }

PR_URL=""; TICKET=""; PROJECT=""; BRANCH=""
CRIT="0"; WARN="0"; SUGG="0"; ALIGN=""; SUMMARY=""

while getopts ":u:t:p:b:C:W:S:A:M:" opt; do
  case $opt in
    u) PR_URL="$OPTARG" ;;
    t) TICKET="$OPTARG" ;;
    p) PROJECT="$OPTARG" ;;
    b) BRANCH="$OPTARG" ;;
    C) CRIT="$OPTARG" ;;
    W) WARN="$OPTARG" ;;
    S) SUGG="$OPTARG" ;;
    A) ALIGN="$OPTARG" ;;
    M) SUMMARY="$OPTARG" ;;
    *) usage ;;
  esac
done
[[ -z "$PR_URL" || -z "$TICKET" || -z "$PROJECT" || -z "$BRANCH" || -z "$ALIGN" || -z "$SUMMARY" ]] && usage

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "Skipping PR comment — GITHUB_TOKEN not set."
  exit 0
fi

owner=$(printf "%s" "$PR_URL" | awk -F/ '{print $(NF-3)}')
repo=$(printf "%s" "$PR_URL" | awk -F/ '{print $(NF-2)}')
pr_number=$(printf "%s" "$PR_URL" | awk -F/ '{print $NF}')

body="## 🤖 AI Code Review — \`$TICKET\`

**Architecture Alignment:** $ALIGN
> $SUMMARY

| 🔴 Critical | 🟡 Warnings | 💡 Suggestions |
|---|---|---|
| $CRIT | $WARN | $SUGG |

📄 Full report: \`projects/$PROJECT/docs/review/audit-feature-$TICKET.md\`"

api="https://api.github.com/repos/$owner/$repo/issues/$pr_number/comments"

if command -v jq >/dev/null 2>&1; then
  payload=$(jq -n --arg body "$body" '{body: $body}')
  curl -s -X POST -H "Authorization: Bearer '"$GITHUB_TOKEN"'" -H "Content-Type: application/json" -d "$payload" "$api" >/dev/null
else
  esc=$(printf "%s" "$body" | python - <<'PY'
import json,sys
print(json.dumps({"body": sys.stdin.read()}))
PY
)
  curl -s -X POST -H "Authorization: Bearer $GITHUB_TOKEN" -H "Content-Type: application/json" -d "$esc" "$api" >/dev/null
fi

echo "PR comment posted."
