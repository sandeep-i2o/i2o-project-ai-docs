# QMetry Manual Test Case Format

Use this structure for non-executable (manual) test cases.

## Required Fields
- `Title`: concise and behavior-focused
- `Objective`: what scenario is being validated
- `Preconditions`: system/user/data prerequisites
- `Steps`: numbered manual actions
- `Expected Result`: observable outcome per step or final state
- `Priority`: `High`, `Medium`, or `Low`
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

## CSV Header Template

```csv
Title,Objective,Preconditions,Steps,Expected Result,Priority,Module,Release,Requirement Mapping,Type,Automation Status,Labels
```

For multi-step fields in CSV, use newline separators supported by your QMetry importer.
