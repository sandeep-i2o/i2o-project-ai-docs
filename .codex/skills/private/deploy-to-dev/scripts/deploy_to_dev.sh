#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: deploy_to_dev.sh [--jenkins-url URL] [--jenkins-user USER] [--jenkins-token TOKEN]

Deploy current git branch to Jenkins dev job and wait for completion.

Behavior:
- Reads/writes one-time config at <repo>/.jenkins/config.json
- Uses current git branch as JENKINS_BRANCH
- Extracts job from Jenkins job URL
- Prints concise failure summary (no full stacktrace)
USAGE
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 2
  fi
}

trim() {
  local v="$1"
  v="${v#${v%%[![:space:]]*}}"
  v="${v%${v##*[![:space:]]}}"
  printf '%s' "$v"
}

extract_base_and_job_path() {
  local url="$1"
  url="$(trim "$url")"
  url="${url%%\?*}"
  url="${url%/}"

  if [[ ! "$url" =~ ^https?:// ]]; then
    echo "Invalid JENKINS_URL. Expected full URL like https://jenkins.example.com/job/my-job" >&2
    return 1
  fi

  local base
  base="$(printf '%s' "$url" | sed -E 's#^(https?://[^/]+).*$#\1#')"

  local path
  path="${url#"$base"}"

  if [[ "$path" != *"/job/"* ]]; then
    echo "JENKINS_URL must include a job path, e.g. /job/my-job" >&2
    return 1
  fi

  path="${path%/buildWithParameters}"
  path="${path%/build}"
  path="${path%/}"

  if [[ -z "$path" || "$path" == "/" ]]; then
    echo "Unable to derive Jenkins job path from JENKINS_URL" >&2
    return 1
  fi

  local job_name
  job_name="$(printf '%s' "$path" | awk -F'/job/' '{print $NF}' | sed 's#/$##')"

  if [[ -z "$job_name" ]]; then
    echo "Unable to derive JOB_NAME from JENKINS_URL" >&2
    return 1
  fi

  printf '%s\n%s\n%s\n' "$base" "$path" "$job_name"
}

print_relevant_failure() {
  local build_url="$1"
  local user="$2"
  local token="$3"

  local console
  console="$(curl -sS -u "$user:$token" "${build_url}consoleText" || true)"

  if [[ -z "$console" ]]; then
    echo "Relevant error: Jenkins console log unavailable. Check ${build_url}consoleText"
    return
  fi

  local filtered
  filtered="$(
    printf '%s\n' "$console" | tr -d '\r' | awk '
      BEGIN { count=0 }
      /^[[:space:]]+at / { next }
      /^[[:space:]]*\.\.\./ { next }
      /ERROR|FAIL|FATAL|Exception|Caused by:/ {
        if (length($0) > 350) {
          print substr($0, 1, 350) "..."
        } else {
          print $0
        }
        count++
        if (count >= 8) exit
      }
    '
  )"

  if [[ -n "$filtered" ]]; then
    echo "Relevant error message(s):"
    printf '%s\n' "$filtered"
  else
    local tail_lines
    tail_lines="$(printf '%s\n' "$console" | tr -d '\r' | tail -n 10)"
    echo "Relevant error message (tail excerpt):"
    printf '%s\n' "$tail_lines"
  fi
}

main() {
  require_cmd curl
  require_cmd jq
  require_cmd git

  local input_url=""
  local input_user=""
  local input_token=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --jenkins-url)
        input_url="${2:-}"
        shift 2
        ;;
      --jenkins-user)
        input_user="${2:-}"
        shift 2
        ;;
      --jenkins-token)
        input_token="${2:-}"
        shift 2
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        echo "Unknown argument: $1" >&2
        usage
        exit 2
        ;;
    esac
  done

  local repo_root
  if ! repo_root="$(git rev-parse --show-toplevel 2>/dev/null)"; then
    echo "Run this command inside a git repository." >&2
    exit 2
  fi

  local config_dir="$repo_root/.jenkins"
  local config_file="$config_dir/config.json"

  local jenkins_url=""
  local jenkins_user=""
  local jenkins_token=""

  if [[ -f "$config_file" ]]; then
    jenkins_url="$(jq -r '.JENKINS_URL // empty' "$config_file")"
    jenkins_user="$(jq -r '.JENKINS_USER // empty' "$config_file")"
    jenkins_token="$(jq -r '.JENKINS_API_TOKEN // empty' "$config_file")"
  fi

  [[ -n "$input_url" ]] && jenkins_url="$input_url"
  [[ -n "$input_user" ]] && jenkins_user="$input_user"
  [[ -n "$input_token" ]] && jenkins_token="$input_token"

  if [[ -z "$jenkins_url" ]]; then
    read -r -p "Enter JENKINS_URL (job URL): " jenkins_url
  fi
  if [[ -z "$jenkins_user" ]]; then
    read -r -p "Enter JENKINS_USER: " jenkins_user
  fi
  if [[ -z "$jenkins_token" ]]; then
    read -r -s -p "Enter JENKINS_API_TOKEN: " jenkins_token
    echo
  fi

  mkdir -p "$config_dir"
  jq -n \
    --arg url "$jenkins_url" \
    --arg user "$jenkins_user" \
    --arg token "$jenkins_token" \
    '{JENKINS_URL:$url,JENKINS_USER:$user,JENKINS_API_TOKEN:$token}' > "$config_file"
  chmod 600 "$config_file" || true

  local parsed
  parsed="$(extract_base_and_job_path "$jenkins_url")"

  local JENKINS_URL JOB_PATH JOB_NAME
  JENKINS_URL="$(printf '%s' "$parsed" | sed -n '1p')"
  JOB_PATH="$(printf '%s' "$parsed" | sed -n '2p')"
  JOB_NAME="$(printf '%s' "$parsed" | sed -n '3p')"

  local USER TOKEN
  USER="$jenkins_user"
  TOKEN="$jenkins_token"

  local JENKINS_BRANCH
  JENKINS_BRANCH="$(git -C "$repo_root" rev-parse --abbrev-ref HEAD)"

  echo "JENKINS_URL(base): $JENKINS_URL"
  echo "JOB_NAME: $JOB_NAME"
  echo "JENKINS_BRANCH: $JENKINS_BRANCH"

  local encoded_branch
  encoded_branch="$(jq -rn --arg v "$JENKINS_BRANCH" '$v|@uri')"

  local headers_file body_file
  headers_file="$(mktemp)"
  body_file="$(mktemp)"

  local trigger_url status queue_url
  trigger_url="${JENKINS_URL}${JOB_PATH}/buildWithParameters?JENKINS_BRANCH=${encoded_branch}&BRANCH=${encoded_branch}&branch=${encoded_branch}&GIT_BRANCH=${encoded_branch}&BRANCH_NAME=${encoded_branch}"

  curl -sS -D "$headers_file" -o "$body_file" -X POST -u "$USER:$TOKEN" "$trigger_url" || true
  status="$(awk 'toupper($1) ~ /^HTTP\// {code=$2} END{print code}' "$headers_file")"
  queue_url="$(awk 'tolower($1)=="location:" {loc=$2} END{print loc}' "$headers_file" | tr -d '\r')"

  # Falling back to /build can trigger Jenkins default branch. Only do it when
  # parameterized trigger is clearly unavailable.
  if [[ -z "$queue_url" && ( "$status" == "404" || "$status" == "405" ) ]]; then
    echo "buildWithParameters unavailable (HTTP $status), falling back to /build (branch parameter cannot be guaranteed)."
    trigger_url="${JENKINS_URL}${JOB_PATH}/build"
    : > "$headers_file"
    : > "$body_file"
    curl -sS -D "$headers_file" -o "$body_file" -X POST -u "$USER:$TOKEN" "$trigger_url" || true
    status="$(awk 'toupper($1) ~ /^HTTP\// {code=$2} END{print code}' "$headers_file")"
    queue_url="$(awk 'tolower($1)=="location:" {loc=$2} END{print loc}' "$headers_file" | tr -d '\r')"
  fi

  if [[ "$status" != "201" || -z "$queue_url" ]]; then
    local response_excerpt
    response_excerpt="$(tr -d '\r' < "$body_file" | head -n 20)"
    echo "Failed to trigger Jenkins build (HTTP $status)."
    if [[ -n "$response_excerpt" ]]; then
      echo "Relevant error message:"
      echo "$response_excerpt"
    fi
    rm -f "$headers_file" "$body_file"
    exit 1
  fi

  if [[ "$queue_url" != http* ]]; then
    queue_url="${JENKINS_URL}${queue_url}"
  fi

  echo "Queued at: $queue_url"

  local BUILD_URL=""
  while true; do
    BUILD_URL="$(curl -sS -u "$USER:$TOKEN" "${queue_url}api/json" | jq -r '.executable.url // "null"')"
    [[ "$BUILD_URL" != "null" ]] && break
    sleep 2
  done

  echo "Build started: $BUILD_URL"

  while true; do
    local BUILDING
    BUILDING="$(curl -sS -u "$USER:$TOKEN" "${BUILD_URL}api/json" | jq -r '.building')"
    [[ "$BUILDING" == "false" ]] && break
    sleep 5
  done

  local RESULT
  RESULT="$(curl -sS -u "$USER:$TOKEN" "${BUILD_URL}api/json" | jq -r '.result // "UNKNOWN"')"
  echo "Build Result: $RESULT"

  rm -f "$headers_file" "$body_file"

  if [[ "$RESULT" != "SUCCESS" ]]; then
    print_relevant_failure "$BUILD_URL" "$USER" "$TOKEN"
    exit 1
  fi

  echo "Build is successful"
}

main "$@"
