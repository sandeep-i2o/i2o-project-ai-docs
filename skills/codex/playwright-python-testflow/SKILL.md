---
name: playwright-python-testflow
description: Generate executable Playwright Python (pytest) test cases from current branch code changes, PRD requirements, and ticket user stories; present test cases for user approval; execute only approved tests with Playwright video capture; generate an execution report; and update i2o-project-ai-docs/{project}/{release}/progress.md. Use when asked to create and run branch-aware automated test coverage with an explicit review gate, video evidence, and progress tracking.
---

# Playwright Python Testflow

## Goal
Generate reliable Playwright Python executable tests from implementation deltas and requirements, enforce user approval before execution, capture testcase video evidence, and publish traceable QA outcomes.

## Required Inputs
Collect these inputs before execution:
- `project` (required): project folder under `i2o-project-ai-docs`, for example `reseller`.
- `release` (required): release folder, for example `7.6`.
- `ticket_id` (required): Jira or tracker key, for example `I2O-1234`.
- `ticket_description` (required): concise requirement/problem statement from the ticket.
- `user_stories` (required): story list from ticket or linked requirement.
- `base_ref` (optional): diff base branch, default `origin/main`.
- `app_endpoint` (required on first run): application base URL for Playwright execution.
- `login_username` (required on first run): username for login page authentication.
- `login_password` (required on first run): password for login page authentication.

## Preflight
1. Verify tools: `git`, `python3`, `pytest`.
2. Verify Playwright stack is available in the target repo:
   - `playwright` Python package
   - `pytest-playwright` (if using pytest fixtures)
   - Playwright video capture support (`pytest --help` includes `--video` and `--output` options)
3. Resolve docs repository path:
   - Preferred: existing local clone containing `projects/{project}/{release}`
   - Example local clone: `/Users/sandeepofficial/temp/i2o-project-ai-docs`
4. Locate PRD at:
   - `i2o-project-ai-docs/projects/{project}/{release}/docs/requirements/prd.md`
5. Initialize app login config in repo-local `.app_playwright_config/app_login.json`:
   - If file exists, load `app_endpoint`, `login_username`, and `login_password` from it and do not ask the user again.
   - If file does not exist, collect these three values once and persist them for subsequent invocations.
   - Never print raw password values in console output, reports, generated test logs, or artifact names.
6. Stop and ask for clarification if ticket description or user stories are missing.

## Workflow

### 1) Resolve App Login Bootstrap
1. Ensure `.app_playwright_config/app_login.json` is loaded before test generation.
2. Build generated tests with a shared login bootstrap:
   - Navigate to `app_endpoint` first.
   - Detect whether the login page is present.
   - If login page is present, perform login as the first basic step using `login_username` and `login_password`.
3. Keep login handling reusable via a helper/fixture to avoid duplication across test files.

### 2) Build Context From Code and Requirements
1. Detect current branch with `git branch --show-current`.
2. Compute changed files versus `base_ref` using `git diff --name-only {base_ref}...HEAD`.
3. Read only relevant changed files and impacted flows.
4. Read PRD user stories and acceptance criteria from:
   - `projects/{project}/{release}/docs/requirements/prd.md`
5. Combine these sources to derive a traceability matrix:
   - `story -> acceptance criteria -> impacted code -> proposed test case`

### 3) Generate Executable Playwright Python Tests
1. Create test files under project test location (example: `tests/e2e/playwright/`).
2. Use Python Playwright patterns compatible with the project test runner.
3. Keep tests deterministic:
   - Avoid hard waits where event/state waits are possible.
   - Reuse existing fixtures and environment configuration.
4. Ensure each test starts from the shared login bootstrap so authentication runs first when a login page is encountered.
5. Name tests and docstrings to include story/ticket traceability.
6. Produce a review table before running any test.

Use test case format from [references/testcase-review-format.md](references/testcase-review-format.md).

### 4) Review Gate (Mandatory)
1. Present generated test cases to the user.
2. Include at minimum:
   - test id/name
   - mapped user story
   - scenario purpose
   - file path
   - execution tags/markers
3. Ask for explicit approval to execute.
4. If edits are requested, apply changes and re-present updated cases.
5. Do not execute tests before explicit approval.

### 5) Execute Approved Tests (with Video Capture)
1. Run only after explicit approval.
2. Execute with machine-readable output and video recording:
   ```bash
   pytest tests/e2e/playwright \
     --video=on \
     --output artifacts/playwright-results \
     --junitxml artifacts/playwright-junit.xml
   ```
3. If the repository uses a different test command, use project-native command while still producing:
   - JUnit XML output
   - Playwright video artifacts in a deterministic folder (recommended `artifacts/playwright-results`)
4. Capture failing test names and failure reasons for report generation.
5. Build a video inventory after execution:
   ```bash
   find artifacts/playwright-results -type f -name "*.webm" | sort > artifacts/playwright-videos.txt
   ```
6. If no videos are produced, report it explicitly as an execution issue.

### 6) Generate Execution Report
1. Generate markdown report using:
   ```bash
   python3 scripts/render_pytest_report.py \
     --junit-xml artifacts/playwright-junit.xml \
     --output-md artifacts/playwright-execution-report.md \
     --ticket-id <ticket_id> \
     --project <project> \
     --release <release> \
     --branch <branch_name> \
     --prd-path <absolute_prd_path>
   ```
2. Include generated test files in the report using repeated `--test-file` flags.
3. Append a `## Video Artifacts` section to the markdown report with:
   - video root directory
   - total `.webm` count
   - list of video file paths (or link to `artifacts/playwright-videos.txt`)
4. Ensure report includes:
   - execution context
   - pass/fail/skip/error counts
   - failing test details
   - artifact paths (JUnit XML, report markdown, video inventory, video directory)

Use report layout from [references/report-format.md](references/report-format.md).

### 7) Update Progress Tracking
1. Update:
   - `i2o-project-ai-docs/projects/{project}/{release}/progress.md`
2. Use helper script:
   ```bash
   python3 scripts/update_progress_md.py \
     --progress-file <path_to_progress_md> \
     --ticket-id <ticket_id> \
     --project <project> \
     --release <release> \
     --branch <branch_name> \
     --prd-path <absolute_prd_path> \
     --report-file artifacts/playwright-execution-report.md \
     --tests-generated <count> \
     --tests-passed <count> \
     --tests-failed <count> \
     --tests-skipped <count> \
     --tests-errors <count>
   ```
3. Append a dated QA automation entry; do not overwrite existing history.
4. Include video artifact references in the progress checkpoint summary when available.

### 8) Final Response Contract
Report back with:
1. Generated test file list.
2. Approval status and what was approved.
3. Execution summary counts.
4. Report artifact location.
5. Video artifact locations (video root + inventory file + count).
6. Updated `progress.md` path and appended entry timestamp.

## Guardrails
- Do not invent user stories not present in ticket/PRD context.
- Do not execute tests before explicit user approval.
- Do not modify unrelated test suites.
- Keep test data and credentials out of committed source.
- Never expose plaintext `login_password` in generated artifacts or reports.
- Prefer small, reviewable test increments over bulk unverified generation.

## Failure Conditions
Stop and report clearly when:
- PRD file is missing at required path.
- ticket description or user stories are unavailable.
- required app login config is missing and cannot be collected.
- Playwright/pytest dependencies are missing and cannot be installed.
- test command cannot produce execution artifacts.
- video capture is enabled but video files cannot be produced or located.
- progress file path is missing or non-writable.
