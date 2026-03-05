---
name: generate-api-tests-from-ticket
description: Generate API test cases for new branch code from a ticket definition, execute the tests, and produce a test report with evidence. Use when inputs include project_id, release_id, and an Atlassian ticket_id and Codex must (1) derive in-scope endpoints from the ticket, (2) implement API tests in the existing repo test framework, and (3) run a fix-and-retest loop until tests pass or blockers are documented.
---

# Generate API Tests From Ticket

Generate endpoint-level API tests directly from ticket scope, execute them against the current branch, remediate failures in code, and produce a traceable report.

## Inputs

Collect these inputs first:
- `project_id`
- `release_id`
- `ticket_id` (Atlassian issue key, for example `ABC-123`)

Optional but helpful:
- Base branch for comparison (`main`, `develop`, or release branch)
- Test command override when the repo has multiple API test runners

## Resolve Ticket Scope

Resolve ticket details in this order:
1. Local docs:
   - `projects/{project_id}/{release_id}/docs/tickets`
   - `projects/{project_id}/{release_id}/tickets`
   - `features/{project_id}/tickets`
2. If local docs do not contain the ticket, read the ticket from Atlassian (for example via `acli`) when available.

Capture only in-scope API details:
- Endpoint path(s)
- HTTP method(s)
- Request schema and required fields
- Expected status codes and response contracts
- Auth/role constraints
- Explicit edge cases in acceptance criteria

Stop and report if no API endpoint can be identified from the ticket.

## Resolve Code and Test Baseline

Identify the branch delta before writing tests:
1. Detect candidate base branch and compute diff.
2. Locate changed API files (routes/controllers/handlers/openapi specs).
3. Map changed files back to ticket endpoints.
4. Locate existing API test framework and conventions in the repo.

Preserve current test style:
- Reuse existing fixtures, factories, auth helpers, and test bootstrap.
- Add tests to existing suite folders unless the repo convention requires a new file.

## Create API Test Cases

Design tests for every ticket endpoint and method using `references/api-test-design-checklist.md`.

Minimum coverage per endpoint:
- Success path (`2xx`) with contract assertions
- Validation error (`4xx`) for malformed/missing input
- Auth/authz behavior (unauthenticated and unauthorized when applicable)
- Not found or business-rule rejection path when relevant

Prefer deterministic tests:
- Control seed/test data.
- Mock unstable external dependencies only when required by current suite patterns.
- Avoid fragile time-dependent assertions without fixed clocks.

## Execute and Remediate Loop

Run tests in a strict loop:
1. Execute targeted API test suite for the ticket.
2. If failing, classify root cause:
   - Product code defect
   - Test issue (incorrect expectation/setup)
   - Environment/setup issue
3. Fix product code first when acceptance criteria indicate incorrect behavior.
4. Re-run targeted tests after each fix.
5. Repeat until all targeted tests pass or a hard blocker is found.

Loop guardrails:
- Maximum 3 remediation iterations unless user asks for deeper debugging.
- If blocked, document exact blocker and stop (do not fabricate passing results).

After targeted tests pass, run the nearest broader regression scope used by the repo for API stability.

## Generate Report

Create report from `assets/api-test-report-template.md`.

Preferred output path:
- `projects/{project_id}/{release_id}/docs/qa/api-test-report-{ticket_id}.md`

Fallback output path (if above path is unavailable):
- `reports/api-tests/{ticket_id}.md`

The report must include:
- Inputs and resolved ticket source
- Endpoint-by-endpoint test matrix
- Commands executed
- Pass/fail summary
- Failures encountered and fixes applied
- Final status (`PASS`, `PASS_WITH_NOTES`, or `BLOCKED`)
- Files changed (tests and product code)

## Output Contract

At completion, always provide:
- Implemented or updated API test files
- Any code fixes applied during remediation
- Final report file path
- Residual risks and follow-up recommendations (if any)

## Quality Rules

- Keep test scope strictly tied to the ticket.
- Prefer minimal, surgical code fixes over broad refactors during remediation.
- Do not change unrelated behavior while fixing failing tests.
- Cite exact evidence (commands, failures, commit-local file paths) in the report.

## Reference Files

Load only as needed:
- `references/api-test-design-checklist.md`: scenario checklist for endpoint coverage
- `assets/api-test-report-template.md`: report scaffold with required sections
