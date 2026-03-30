# QMetry Manual Test Case Format

Use this structure for non-executable (manual) test cases.

## Required Fields
- `Title`: concise and behavior-focused
- `Objective`: what scenario is being validated
- `Preconditions`: system/user/data prerequisites
- `Steps`: numbered manual actions
- `Expected Result`: observable outcome per step or final state
- `Priority`: `High`, `Medium`, or `Low` (or a valid project priority name)
- `Module`: input module (or mapped component)
- `Release`: release version (default `7.5` unless provided)
- `Requirement Mapping`: user story ID/title
- `Type`: `Manual`
- `Automation Status`: `Not Automated`

## Recommended Additions
- `Test Data`
- `Environment`
- `Labels` (module, release, story)
- `Negative/Edge` marker

## Authoring Rules
- Keep one validation intent per case.
- Write deterministic step verbs: `Navigate`, `Enter`, `Select`, `Submit`, `Verify`.
- Use explicit expected outcomes; avoid vague checks.
- Add boundary and failure-path cases when PRD indicates corner cases.

## Markdown Review Template

| ID | Title | User Story | Priority | Preconditions | Steps | Expected Result | Tags |
|---|---|---|---|---|---|---|---|
| TC-001 | [title] | [story id/title] | High | [preconditions] | 1. ... 2. ... | [result] | module, release |

## QMetry Push JSON Template

This JSON is the direct input for `scripts/qmetry_push_testcases.py`.

```json
[
  {
    "title": "Login succeeds with valid credentials",
    "objective": "Verify user can sign in with a valid username/password",
    "preconditions": "Active user exists and login page is reachable",
    "steps": [
      {
        "step": "Navigate to the login page",
        "expected_result": "Login page is displayed"
      },
      {
        "step": "Enter valid username and password and click Sign In",
        "test_data": "username: qa_user, password: ********",
        "expected_result": "User is redirected to dashboard"
      }
    ],
    "expected_result": "Authenticated dashboard is shown",
    "priority": "High",
    "status": "To Do",
    "labels": ["price_monitoring", "7.5"],
    "requirement_mapping": "US-LOGIN-01",
    "type": "Manual",
    "automation_status": "Not Automated"
  }
]
```

## JSON Field Notes for Push Script
- `title` or `summary`: required
- `steps`: required for best quality; accepts string list or object list
- Step object keys accepted:
  - `stepDetails` or `step`
  - `testData` or `test_data`
  - `expectedResult` or `expected_result`
- `priority` and `status` can be names (resolved through QMetry lookup APIs) or numeric IDs
- `labels` can be names or numeric IDs
- `requirement_mapping`, `module`, and `release` are preserved in description metadata

## CSV Header Template

```csv
Title,Objective,Preconditions,Steps,Expected Result,Priority,Module,Release,Requirement Mapping,Type,Automation Status,Labels
```

For multi-step fields in CSV, use newline separators supported by your QMetry importer.
