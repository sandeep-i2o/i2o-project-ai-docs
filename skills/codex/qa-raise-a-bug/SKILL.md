---
name: qa-raise-a-bug
description: Create Jira Bug issues from QMetry test case results by reading pass/fail status comments and drafting Jira bugs with the project_id prefix in the summary (e.g., [MARKETPLACE_OVERVIEW] ...). Use when asked to raise/triage bugs from QMetry test cases, extract failure reasons from QMetry comments, and file Jira Bugs only after explicit user review.
---

# QA Raise A Bug

## Goal
Raise Jira Bug issues from QMetry test cases by reading the latest pass/fail comments, extracting failure details, and creating Jira bugs with a strict user review gate.

## Required Inputs
Collect these inputs before starting:
- `project_id` (required, used in Jira summary prefix like `[PROJECT_ID] ...`)
- `qmetry_link` (required unless user provides explicit QMetry case IDs)
- `jira_project_key` (required, Jira project key for issue creation)
- `environment` (optional, e.g., QA/Stage URL)
- `component` (optional)
- `priority` (optional)
- `labels` (optional list)

## QMetry URL Handling (Aligned With Existing QMetry Skills)
Treat `qmetry_link` as tenant-aware input, not raw text.

1. Reuse repository-local `.jira/credentials.json` as the source of QMetry tenant config when available.
2. Required fields in `.jira/credentials.json` for QMetry:
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

## Jira Auth
Prefer Atlassian CLI (`acli`) if available:
- Verify auth with `acli whoami`.

If `acli` is unavailable or fails, fall back to Jira REST API with credentials gathered from the user (or a repo-local `.jira/credentials.json` if it includes Jira fields). Required Jira fields for REST fallback:
- `jira_base_url` (e.g., `https://your-domain.atlassian.net`)
- `jira_email`
- `jira_api_token`

## Workflow

### 1) Read QMetry Test Cases
1. Use the normalized `qmetry_link` or explicit case IDs supplied by the user.
2. Retrieve test case details via QMetry API when possible (avoid UI scraping).
3. Capture for each case:
   - Case ID
   - Title
   - Preconditions
   - Steps
   - Expected Results
   - Latest comments (including author + timestamp)

### 2) Determine Pass/Fail From Comments
1. Identify the most recent status comment for each case.
2. Treat comment format `{STATUS} - {REASON}` as the source of truth, where `{STATUS}` is `PASSED` or `FAILED`.
3. If no status comment exists, stop and ask the user whether to proceed.
4. If latest status is `PASSED`, do not raise a bug; report it as skipped.
5. If latest status is `FAILED`, proceed to bug draft using the failure reason as the primary issue summary signal.

### 3) Draft Jira Bug Content
For each failed case, draft a Jira Bug with the following rules:
1. Summary must start with `[PROJECT_ID]`.
2. Use the failure reason from the latest QMetry comment as the main issue summary when available.
3. If failure reason is missing, fall back to the QMetry case title.
4. Description must include:
   - QMetry case ID + title
   - QMetry link
   - Latest status comment (verbatim)
   - Preconditions
   - Steps to reproduce (from case steps)
   - Expected result (from case)
   - Actual result (derived from failure reason)
   - Environment (if provided)
   - Evidence/attachments references if available

### 4) Mandatory Review Gate
1. Present each drafted Jira Bug (summary + description + fields).
2. Ask for explicit approval before creating any Jira issue.
3. Do not create or update Jira issues without clear approval.

### 5) Create Jira Bug
Use `acli` if possible:
```bash
acli jira workitem create \
  --project "${JIRA_PROJECT_KEY}" \
  --type "Bug" \
  --summary "${SUMMARY}" \
  --description "${DESCRIPTION}" \
  --priority "${PRIORITY}" \
  --labels "${LABELS}" \
  --components "${COMPONENTS}"
```

Fallback to Jira REST if `acli` is unavailable. Use Jira REST API to create the issue with the same fields and attach labels/components when provided.

### 6) Return Results
Provide:
- Created Jira keys (or confirmation that nothing was created)
- Skipped cases (PASSED)
- Drafts reviewed and approved
- Any errors with details

## Output Contract
Return:
1. QMetry cases evaluated (IDs + status).
2. Drafted Jira bug summaries.
3. Approval decision used for creation.
4. Created Jira bug keys (if any).
5. Skipped case list with reason.

## Guardrails
- Never create Jira bugs without explicit user approval.
- Never create a bug from a `PASSED` status comment.
- Never invent QMetry test cases or comments.
- Never use unvalidated QMetry URLs across different tenants/domains.
- Do not print or log secrets (`apiKey`, `basicAuthBase64`, Jira tokens).

## Failure Conditions
Stop and report clearly when:
- `project_id` is missing.
- `jira_project_key` is missing.
- `qmetry_link` or case IDs are missing and user does not provide them.
- QMetry URL tenant/project validation fails.
- QMetry link is inaccessible or case details cannot be retrieved.
- No status comment exists for a case and user does not allow manual status input.
- Jira auth fails for both `acli` and REST fallback.
