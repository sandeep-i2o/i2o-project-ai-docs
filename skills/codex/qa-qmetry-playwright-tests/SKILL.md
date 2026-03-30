---
name: qa-qmetry-playwright-tests
description: Read QMetry test cases from a user-provided QMetry link, convert them into executable frontend Playwright tests, capture and persist execution environment credentials in .config/credentials.json, enforce an explicit user approval gate before execution, and generate execution reports under i2o-ai-project-docs/{project_id}/{release_id}/tests/qmetery-test-reports. Use when asked to create or run Playwright UI tests from QMetry test cases with project/release-scoped reporting and login-first test flow.
---

# QA QMetry Playwright Tests

## Goal
Generate frontend Playwright tests from QMetry test cases, persist reusable test environment credentials, require explicit approval before running tests, execute approved tests, and publish a markdown report in the required project/release docs folder.

## Required Inputs
Collect these inputs before generation:
- `project_id` (required)
- `release_id` (required)
- `qmetry_link` (required, ask if not provided)
- `test_url` (default: `https://qa.i2oretail.com`)
- `test_username` (default: `agency.user@i2oretail.com`)
- `test_password` (default: `I2oretail@123`)

## QMetry URL Handling (Aligned With `prd-to-qmetry-testcases`)
Treat `qmetry_link` as tenant-aware input, not raw text.

1. Reuse repository-local `.jira/credentials.json` as the source of QMetry tenant config.
2. Required fields in `.jira/credentials.json`:
   - `project_id` (must be `10537`)
   - `apiKey`
   - `basicAuthBase64` (base64 token only, without `Basic ` prefix)
3. Optional field:
   - `base_url` (default `https://qtmcloud.qmetry.com`; use `https://syd-qtmcloud.qmetry.com` for AU)
4. Normalize incoming `qmetry_link` before use:
   - accept plain URL or markdown link format (`[label](url)`)
   - trim wrappers/spaces and resolve to a single canonical URL
   - require `https` scheme
   - host must match `base_url` host from `.jira/credentials.json`
5. Project validation:
   - if URL contains project id/key context, it must resolve to QMetry project `10537`
   - if tenant or project context cannot be determined from URL, stop and ask for clarification
6. Use the normalized URL for all downstream steps and reporting (never use unvalidated raw text).

## Preflight
1. Ask for `project_id` and `release_id`.
2. Ask for `qmetry_link` when missing.
3. Validate `.jira/credentials.json` using the same contract as `prd-to-qmetry-testcases`:
   - required: `project_id=10537`, `apiKey`, `basicAuthBase64`
   - optional: `base_url` (`https://qtmcloud.qmetry.com` default)
4. Normalize and validate `qmetry_link` against the tenant `base_url` and project `10537` rules above.
5. Resolve and store execution environment credentials in repo-local `.config/credentials.json` using:
   ```bash
   python3 ./scripts/resolve_test_credentials.py \
     --repo-root <absolute_repo_root> \
     --test-url <test_url_or_default> \
     --test-username <test_username_or_default> \
     --test-password <test_password_or_default>
   ```
6. Reuse `.config/credentials.json` on later runs instead of re-asking unless user wants to override values.
7. Validate the report directory exists and stop if missing:
   - `i2o-ai-project-docs/{project_id}/{release_id}/tests/qmetery-test-reports`
8. Run report-path validation with normalized QMetry URL:
   ```bash
   python3 ./scripts/prepare_qmetry_playwright_report.py \
     --docs-root <absolute_path_to_i2o-ai-project-docs> \
     --project-id <project_id> \
     --release-id <release_id> \
     --qmetry-link <normalized_qmetry_link> \
     --credentials-file <absolute_repo_root>/.config/credentials.json \
     --dry-run
   ```

## Workflow

### 1) Read QMetry Cases
1. Use the normalized/validated `qmetry_link` (not raw input).
2. Extract test case IDs, titles, preconditions, steps, and expected results.
3. Prefer QMetry API-backed retrieval using `.jira/credentials.json` (`base_url`, `apiKey`, `basicAuthBase64`) instead of brittle UI scraping.
4. If the link is accessible but does not provide resolvable case identifiers, ask the user for explicit case IDs or a case-list link with IDs.
5. Stop and ask for clarification if the link is inaccessible or missing case details.

### 2) Build Login-First Base Flow (Mandatory)
1. Load `test_url`, `test_username`, and `test_password` from `.config/credentials.json`.
2. Treat login as the first action for every generated test case.
3. Ensure each generated test starts by:
   - navigating to `test_url`
   - authenticating with stored credentials on the login page
4. Implement a shared login helper/fixture and call it before case-specific steps.

### 3) Generate Frontend Playwright Tests
1. Map each QMetry case into deterministic Playwright UI scenarios.
2. Write tests into the repository frontend Playwright tests area.
3. Prefer existing project convention; fallback path is `tests/e2e/playwright/`.
4. Name tests to preserve traceability to original QMetry case IDs.
5. Keep test files free of hardcoded credentials; load credentials through shared fixture/config.

### 4) Mandatory Approval Gate
1. Present generated test cases before execution.
2. Include at minimum:
   - QMetry case ID/title
   - generated test file path
   - scenario purpose
3. Ask for explicit approval.
4. Do not execute any test without explicit approval.

### 5) Execute Approved Tests
1. Run only approved tests using project-native Playwright command.
2. Prefer command producing JSON output, for example:
   ```bash
   npx playwright test <approved_specs> --reporter=json > artifacts/playwright-results.json
   ```
3. Capture artifact paths needed for reporting.

### 6) Generate Report
1. Build report in:
   - `i2o-ai-project-docs/{project_id}/{release_id}/tests/qmetery-test-reports/`
2. Use script:
   ```bash
   python3 ./scripts/prepare_qmetry_playwright_report.py \
     --docs-root <absolute_path_to_i2o-ai-project-docs> \
     --project-id <project_id> \
     --release-id <release_id> \
     --qmetry-link <normalized_qmetry_link> \
     --results-json artifacts/playwright-results.json \
     --credentials-file <absolute_repo_root>/.config/credentials.json \
     --test-file <generated_test_file> \
     --artifact artifacts/playwright-results.json
   ```
3. If the target report directory does not exist, stop and report the missing path.

## Output Contract
Return:
1. Generated test file list.
2. Approval decision used for execution.
3. Execution summary (total/passed/failed/skipped).
4. Credentials file used (`.config/credentials.json`).
5. Final report path.

## Guardrails
- Never skip the approval gate.
- Never execute tests before explicit user approval.
- Never skip login as the first base step.
- Never create report folders automatically when required folder is missing.
- Never invent QMetry test cases.
- Never use unvalidated QMetry URLs across different tenants/domains.
- Do not print raw passwords, `apiKey`, or `basicAuthBase64` in logs or reports.

## Failure Conditions
Stop and report clearly when:
- `project_id` or `release_id` is missing.
- `qmetry_link` is missing and user does not provide it.
- `.jira/credentials.json` is missing/unreadable or required fields are absent.
- QMetry URL tenant/project validation fails (host mismatch, unsupported URL format, or non-`10537` project context).
- QMetry link is inaccessible.
- `.config/credentials.json` cannot be created or read.
- `i2o-ai-project-docs/{project_id}/{release_id}/tests/qmetery-test-reports` is missing.
- Playwright execution fails to produce requested artifacts.
