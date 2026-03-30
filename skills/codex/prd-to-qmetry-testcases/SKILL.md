---
name: prd-to-qmetry-testcases
description: Generate comprehensive non-executable UAT QMetry test cases from PRD user stories in i2o-project-ai-docs, run user review, and push approved cases into a project-specific QMetry folder.
---

# PRD To QMetry Testcases

## Goal
Generate high-quality, comprehensive manual (non-executable) UAT test cases from PRD user stories and push them to QMetry only after explicit user approval.

## Inputs
Collect and confirm these inputs before execution:
- `module` (required): expected branch name such as `price_monitoring`, `growth_accelerator`, `brand_protection`
- `project_id` (required): requirement/project identifier used in generation prompt and as QMetry folder name
- `project_name` (required): project directory under `projects/`
- `release_version` (required): release folder name (no default)
- `instructions` (optional): additional QA instructions from input prompt (`--instructions`)

QMetry target project id is static and must always be `10537`.

## Preflight
1. Verify required tools: `git`, `python3`, and Markdown parsing capability.
2. Verify QMetry credentials from repository-local file `.jira/credentials.json`:
   - Required fields:
     - `apiKey`
     - `basicAuthBase64` (base64 token only, without `Basic ` prefix)
   - Required fixed field:
     - `project_id` must be `10537`
   - Optional field:
     - `base_url` (default `https://qtmcloud.qmetry.com`; use `https://syd-qtmcloud.qmetry.com` for AU)
3. If `.jira/credentials.json` is missing or incomplete, ask the user once for `apiKey` and `basicAuthBase64`, then create/update `.jira/credentials.json` and reuse it in future runs.
4. Validate credentials with a safe GET call before push:
   ```bash
   curl --request GET \
     --url https://qtmcloud.qmetry.com/rest/api/latest/projects/10537/priorities \
     --header 'apikey: <apiKey>' \
     --header 'authorization: Basic <base64encoded_string>' \
     --header 'content-type: application/json'
   ```
5. Ask concise clarification questions when requirements are ambiguous.
6. Do not push anything to QMetry before explicit user confirmation.

Use [scripts/prd_preflight.py](scripts/prd_preflight.py) for deterministic repository/branch/PRD checks.

## Credentials File Contract
Store credentials at `.jira/credentials.json` (repository root):

```json
{
  "project_id": 10537,
  "apiKey": "<qmetry_api_key>",
  "basicAuthBase64": "<jira_email_colon_api_token_base64>",
  "base_url": "https://qtmcloud.qmetry.com"
}
```

Rules:
- Create `.jira/` if it does not exist.
- Reuse existing credentials on subsequent runs.
- Never print secrets in logs or reports.
- Do not commit `.jira/credentials.json`.

## Workflow

### 1) Clone Docs Repository
1. Clone repository when absent:
   ```bash
   git clone https://github.com/sandeep-i2o/i2o-project-ai-docs/
   ```
2. Reuse existing local clone when present.

### 2) Resolve Branch from Module
1. Treat `module` as branch name.
2. Check whether branch exists in origin.
3. If branch does not exist, stop and ask user for the correct branch name.
4. Checkout resolved branch.

### 3) Locate PRD
Read this path exactly:
`projects/{project_name}/{release_version}/docs/requirements/prd.md`

If file is missing, stop and report the exact missing path.

### 4) Generate Test Cases from PRD
1. Parse all user stories in `prd.md`.
2. If no user stories exist, stop with an error: `User stories are not present in the document.`
3. Read edge cases and corner cases from PRD and include coverage.
4. Consult product guides from `knowledge/kb_pdfs/` for domain-specific behavior and terminology.
5. Read additional QA instructions from input prompt (`--instructions`) and apply them.
6. Generate only manual/non-executable test cases compatible with QMetry import/API using this fixed generation prompt:
   ```text
   Generate all possible comprehensive UAT test cases covering all scenarios for the requirement: {project_id}
   
   PRD Content:
   Read from - prd.md
   Additional QA Instructions: read from --instructions in input prompt
   
   For each test case, provide ALL of the following fields:
   
   SYSTEM FIELDS:
   - id: A unique identifier like "TC-001", "TC-002", etc.
   - summary: A clear, concise test case title
   - description: A detailed paragraph explaining the test case intent and coverage
   - precondition: Prerequisites that must be met before executing the test (use \\n for multiple points)
   - stepDetails: Detailed step-by-step instructions to execute the test
   - testData: Specific test data to be used (usernames, values, inputs)
   - expectedResult: Clear expected outcomes for each step
   - priority: One of "Blocker", "High", "Medium", "Low"
   
   CUSTOM FIELDS:
   - testCaseType: One of "Feature", "Regression", "Sanity"
   - testLayer: One of "UI", "API", "SQL_Query"
   - automation: One of "Completed", "In-progress", "Manual-Could not be done", "Yet to start"
   - sanityType: One of "DailySanity-Load", "WeeklySanity-Load", "Application - Sanity"
   
   CRITICAL STEP-TO-RESULT MAPPING RULES:
   1. stepDetails and expectedResult MUST have EXACTLY the same number of points (e.g., 6 steps = 6 results)
   2. Each expected result MUST directly correspond to its matching step number:
      - Step 1 action → Expected Result 1 (outcome of Step 1 ONLY)
      - Step 2 action → Expected Result 2 (outcome of Step 2 ONLY)
      - Step 3 action → Expected Result 3 (outcome of Step 3 ONLY)
   3. Each expected result describes what happens IMMEDIATELY after completing THAT specific step
   4. Do NOT combine multiple outcomes into one result
   5. Do NOT write expected results that belong to a different step
   
   CORRECT EXAMPLE:
   stepDetails: "1. Open login page\\n2. Enter username 'testuser'\\n3. Enter password\\n4. Click Login"
   expectedResult: "1. Login page is displayed with username and password fields\\n2. Username 'testuser' appears in the field\\n3. Password is masked with dots\\n4. User is redirected to dashboard"
   
   INCORRECT EXAMPLE (DO NOT DO THIS):
   stepDetails: "1. Open login page\\n2. Enter username\\n3. Enter password\\n4. Click Login"
   expectedResult: "1. User logs in successfully\\n2. Dashboard is shown\\n3. Welcome message appears"
   WHY WRONG: Only 3 results for 4 steps, and results don't match their corresponding steps
   
   IMPORTANT RULES:
   - Every field must have a meaningful value - NO null, empty, or placeholder values
   - description must be a detailed paragraph (not just a copy of summary)
   - precondition MUST have each prerequisite on a NEW LINE. Format: "1. First condition\\n2. Second condition\\n3. Third condition"
   - stepDetails MUST have each step on a NEW LINE. Format: "1. First step\\n2. Second step\\n3. Third step"
   - expectedResult MUST have each result on a NEW LINE. Format: "1. First result\\n2. Second result\\n3. Third result"
   - testData should include realistic example data
   - Use \\n (newline character) to separate each numbered point in precondition, stepDetails and expectedResult, DO NOT use actual line breaks in the text. This is crucial for correct parsing later.
   
   BEFORE RETURNING, VERIFY:
   - Count steps and results - they MUST be equal
   - Read step 1, then result 1 - result 1 should be the DIRECT outcome of step 1
   - Repeat for all steps
   ```
7. Save generated cases to JSON for push step, e.g.:
   `artifacts/qmetry_testcases_{module}_{release_version}.json`

Use QMetry structure from [references/qmetry-testcase-format.md](references/qmetry-testcase-format.md).

### 5) Review Gate (Mandatory)
1. Present generated test cases to the user in a reviewable table/list.
2. Also show the target QMetry folder as `{project_id}/{release_version}`.
3. Ask for explicit approval of both the test cases and the folder path, and request edits.
3. Apply requested edits and re-present when needed.
4. Update the JSON artifact so it exactly matches the approved version.

### 6) Push Gate (Mandatory)
1. Push to QMetry only after explicit confirmation such as `Approved`, `Proceed`, or equivalent clear consent.
2. If approval is not explicit, do not push.
3. In QMetry project `10537`, create folder `{project_id}` if it does not already exist.
4. Under `{project_id}`, create subfolder `{release_version}` if it does not already exist.
5. Push approved test cases into the `{project_id}/{release_version}` folder.
5. Run API push script with fixed project id `10537`:
   ```bash
   python3 scripts/qmetry_push_testcases.py \
     --input artifacts/qmetry_testcases_{module}_{release_version}.json \
     --project-id 10537 \
     --module {project_id}/{release_version} \
     --release {release_version}
   ```
6. Ensure script runtime uses `apiKey` and `basicAuthBase64` from `.jira/credentials.json`.
7. Use `--dry-run` first when requested to validate payload without creating test cases.

### 7) Report Push Result
After push, report:
1. Created test case keys/IDs.
2. Any warnings (for example, unmapped labels).
3. Concise coverage summary by user story and priority.

## QMetry API Contract
- Base path: `/rest/api/latest`
- Create endpoint: `POST /rest/api/latest/testcases`
- Fixed project id: `10537`
- Required headers:
  - `authorization: Basic <basicAuthBase64>`
  - `apikey: <apiKey>`
- Script lookups used for safe mapping:
  - `GET /rest/api/latest/projects/10537/priorities`
  - `GET /rest/api/latest/projects/10537/testcase-statuses`
  - `GET /rest/api/latest/projects/10537/labels`

## QMetry Compatibility Rules
- Set case type to manual/non-executable (`isAutomated=false`).
- Keep each test case atomic with clear preconditions, steps, and expected results.
- Map each test case to at least one user story identifier or title.
- Include priority and module labels where available.
- Include release version metadata (label and/or description metadata).

## Output Contract
Produce both:
1. Human-review markdown table/list.
2. QMetry push JSON artifact (input for `scripts/qmetry_push_testcases.py`).

## Failure Conditions
Stop and report clearly when any condition is met:
- branch missing for provided module
- `prd.md` missing at required path
- user stories absent in PRD
- `.jira/credentials.json` missing/unreadable and user did not provide required credentials
- QMetry API rejects payload/auth

## Guardrails
- Do not invent user stories.
- Do not skip edge cases documented in PRD.
- Do not push unreviewed test cases.
- Never expose `apiKey` or `basicAuthBase64` in output.
- Keep communication concise and ask questions when ambiguity blocks accurate test design.
