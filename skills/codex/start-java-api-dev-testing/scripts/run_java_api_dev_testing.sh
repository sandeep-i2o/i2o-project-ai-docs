#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_PATH="${1:-.config/api_curl_tests/config.yaml}"
APP_LOG="${2:-target/start-java-api-dev-testing.log}"
APP_PID=""

log() {
  printf '[start-java-api-dev-testing] %s\n' "$*"
}

fail() {
  printf '[start-java-api-dev-testing] ERROR: %s\n' "$*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail "Missing command: $1"
}

cleanup() {
  if [[ -n "${APP_PID}" ]] && kill -0 "${APP_PID}" >/dev/null 2>&1; then
    kill "${APP_PID}" >/dev/null 2>&1 || true
    wait "${APP_PID}" >/dev/null 2>&1 || true
    log "Stopped service process ${APP_PID}."
  fi
}

trap cleanup EXIT

require_cmd mvn
require_cmd java
require_cmd curl
require_cmd jq
require_cmd ruby
require_cmd python3

[[ -f pom.xml ]] || fail "Run this script from a Maven project root containing pom.xml"

mapfile -t changed_controllers < <(git diff --name-only -- src/main/java 2>/dev/null | grep 'Controller\.java$' || true)

discover_cmd=(python3 "$SCRIPT_DIR/discover_controller_endpoints.py" --root "$PWD" --format json)
if [[ ${#changed_controllers[@]} -gt 0 ]]; then
  for file in "${changed_controllers[@]}"; do
    discover_cmd+=(--file "$file")
  done
fi

endpoints_json="$(${discover_cmd[@]})"

if [[ "$endpoints_json" == "[]" ]] && [[ ${#changed_controllers[@]} -gt 0 ]]; then
  endpoints_json="$(python3 "$SCRIPT_DIR/discover_controller_endpoints.py" --root "$PWD" --format json)"
fi

endpoint_count="$(jq 'length' <<<"$endpoints_json")"
log "Discovered ${endpoint_count} endpoint(s)."

table_cmd=(python3 "$SCRIPT_DIR/discover_controller_endpoints.py" --root "$PWD" --format table)
if [[ ${#changed_controllers[@]} -gt 0 ]]; then
  for file in "${changed_controllers[@]}"; do
    table_cmd+=(--file "$file")
  done
fi
"${table_cmd[@]}" || true

if [[ ! -f "$CONFIG_PATH" ]]; then
  mkdir -p "$(dirname "$CONFIG_PATH")"
  printf '%s' "$endpoints_json" | ruby -rjson -ryaml -e '
endpoints = JSON.parse(STDIN.read)
config = {
  "app" => {
    "base_url" => "http://localhost:8080",
    "startup_wait_seconds" => 120,
    "ready_path" => "",
    "ready_expected_status" => 200
  },
  "tests" => endpoints.map do |ep|
    payload = %w[POST PUT PATCH DELETE].include?(ep["method"]) ? "{}" : ""
    {
      "name" => "#{ep["method"]} #{ep["path"]}",
      "enabled" => false,
      "method" => ep["method"],
      "endpoint" => ep["path"],
      "expected_status" => 200,
      "headers" => {"Content-Type" => "application/json"},
      "payload" => payload
    }
  end
}
puts config.to_yaml(line_width: -1)
' > "$CONFIG_PATH"
  log "Created $CONFIG_PATH from discovered endpoints."
  log "Edit payloads and set enabled: true for ticket-relevant tests, then rerun."
fi

config_json="$(ruby -ryaml -rjson -e '
config = YAML.safe_load(File.read(ARGV[0]), aliases: true) || {}
puts JSON.generate(config)
' "$CONFIG_PATH")"

base_url="$(jq -r '.app.base_url // "http://localhost:8080"' <<<"$config_json")"
startup_wait_seconds="$(jq -r '.app.startup_wait_seconds // 120' <<<"$config_json")"
ready_path="$(jq -r '.app.ready_path // ""' <<<"$config_json")"
ready_expected_status="$(jq -r '(.app.ready_expected_status // 200) | tostring' <<<"$config_json")"

log "Building application with Maven."
mvn clean package -DskipTests=true

war_file="$(ls -1 target/*.war 2>/dev/null | head -n 1 || true)"
[[ -n "$war_file" ]] || fail "No WAR file found under target/*.war after build"

mkdir -p "$(dirname "$APP_LOG")"
log "Starting service: java -jar ${war_file}"
java -jar "$war_file" > "$APP_LOG" 2>&1 &
APP_PID="$!"
log "Service PID ${APP_PID}; log file: ${APP_LOG}"

start_deadline=$((SECONDS + startup_wait_seconds))

if [[ -n "$ready_path" ]]; then
  ready_url="${base_url%/}/${ready_path#/}"
  ready_body="$(mktemp)"
  while true; do
    if ! kill -0 "$APP_PID" >/dev/null 2>&1; then
      tail -n 120 "$APP_LOG" || true
      rm -f "$ready_body"
      fail "Service exited before readiness check passed"
    fi

    status="$(curl -sS -o "$ready_body" -w '%{http_code}' "$ready_url" || true)"
    if [[ "$status" == "$ready_expected_status" ]]; then
      break
    fi

    if (( SECONDS >= start_deadline )); then
      tail -n 120 "$APP_LOG" || true
      rm -f "$ready_body"
      fail "Readiness check failed for ${ready_url}; expected HTTP ${ready_expected_status}, got ${status:-N/A}"
    fi
    sleep 2
  done
  rm -f "$ready_body"
  log "Readiness check passed: ${ready_url}"
else
  while true; do
    if ! kill -0 "$APP_PID" >/dev/null 2>&1; then
      tail -n 120 "$APP_LOG" || true
      fail "Service exited before startup confirmation"
    fi

    if grep -Eq 'Started .* in .* seconds' "$APP_LOG"; then
      break
    fi

    if (( SECONDS >= start_deadline )); then
      tail -n 120 "$APP_LOG" || true
      fail "Service did not become ready within ${startup_wait_seconds}s"
    fi
    sleep 2
  done
  log "Startup confirmation found in application logs."
fi

enabled_tests_json="$(jq -c '.tests // [] | map(select((.enabled // false) == true))' <<<"$config_json")"
enabled_count="$(jq 'length' <<<"$enabled_tests_json")"

if [[ "$enabled_count" == "0" ]]; then
  log "No enabled tests found in ${CONFIG_PATH}."
  log "Set enabled: true for ticket-relevant endpoints and rerun."
  exit 0
fi

pass_count=0
fail_count=0

while IFS= read -r test; do
  test_name="$(jq -r '.name // "unnamed-test"' <<<"$test")"
  method="$(jq -r '(.method // "GET") | ascii_upcase' <<<"$test")"
  endpoint="$(jq -r '.endpoint // ""' <<<"$test")"
  expected_status="$(jq -r '(.expected_status // 200) | tostring' <<<"$test")"
  payload="$(jq -r '.payload // ""' <<<"$test")"

  [[ -n "$endpoint" ]] || fail "Test '${test_name}' is missing endpoint"
  [[ "$endpoint" == /* ]] || endpoint="/$endpoint"

  url="${base_url%/}${endpoint}"
  response_file="$(mktemp)"

  curl_cmd=(curl -sS -o "$response_file" -w '%{http_code}' -X "$method")
  while IFS= read -r header; do
    curl_cmd+=(-H "$header")
  done < <(jq -r '.headers // {} | to_entries[]? | "\(.key): \(.value)"' <<<"$test")

  if [[ -n "$payload" ]] && [[ "$payload" != "null" ]]; then
    curl_cmd+=(--data-raw "$payload")
  fi

  status="$("${curl_cmd[@]}" "$url" || true)"

  if [[ "$status" == "$expected_status" ]]; then
    log "PASS ${test_name} -> HTTP ${status}"
    pass_count=$((pass_count + 1))
  else
    log "FAIL ${test_name} -> expected ${expected_status}, got ${status:-N/A}"
    cat "$response_file" || true
    fail_count=$((fail_count + 1))
  fi

  rm -f "$response_file"
done < <(jq -c '.[]' <<<"$enabled_tests_json")

log "Test summary: ${pass_count} passed, ${fail_count} failed."

if (( fail_count > 0 )); then
  exit 1
fi
