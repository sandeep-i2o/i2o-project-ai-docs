---
name: start-java-api-dev-testing
description: Build and run a Java API service from the current branch, discover controller endpoints, and execute curl API checks using a repo-local `.config/api_curl_tests/config.yaml` payload file. Use when validating backend ticket changes in Maven/Spring services with `mvn clean package -DskipTests=true`, `java -jar target/*.war`, and endpoint-focused curl tests.
---

# Start Java API Dev Testing

## Goal
Build the current branch, start the WAR locally, discover controller endpoints, and run configurable curl tests for ticket-relevant APIs.

## Command Interface
Run:

```bash
./scripts/run_java_api_dev_testing.sh
```

Optional config path:

```bash
./scripts/run_java_api_dev_testing.sh .config/api_curl_tests/config.yaml
```

## Required Workflow
1. Identify changed backend files for the ticket using `git diff --name-only -- src/main/java`.
2. Run the script to discover endpoints, build the app, start the WAR, and execute enabled curl tests.
3. Let the script create `.config/api_curl_tests/config.yaml` if missing, then edit payloads and `enabled` flags for ticket-relevant endpoints.
4. Watch runtime output and inspect `target/start-java-api-dev-testing.log` for failures.
5. Ask for user approval before applying any code fix when build/start/test errors require source changes.
6. Re-run until relevant endpoints pass.

## Behavior
- Build command: `mvn clean package -DskipTests=true`
- Start command: `java -jar target/*.war`
- Endpoint discovery source: `src/main/java/**/*Controller.java`
- Curl test source: `.config/api_curl_tests/config.yaml`

## Resources
- Run script: `scripts/run_java_api_dev_testing.sh`
- Endpoint parser: `scripts/discover_controller_endpoints.py`
- Config reference: `references/config-schema.md`
- Config template asset: `assets/config.template.yaml`
