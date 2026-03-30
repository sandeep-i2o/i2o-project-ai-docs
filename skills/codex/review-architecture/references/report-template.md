# Architecture Review Template

Use this structure for `architecture-review.md`.

## 1. Review Metadata

- Project: `{project_name}`
- Reviewer: `AI Agent`
- Date: `YYYY-MM-DD`
- Source docs:
  - `architecture.md`
  - `prd.md`
  - `pid.md`

## 2. Executive Verdict

- Overall status: `Approved | Conditionally Approved | Rejected`
- Feasibility summary: 2-4 sentences
- Highest-risk area: 1 sentence

## 3. Severity Summary

- `P0` count:
- `P1` count:
- `P2` count:
- `P3` count:

## 4. Findings (Ordered by Severity)

For each finding include:

- ID: `AR-###`
- Severity: `P0|P1|P2|P3`
- Area: `Architecture Domain`
- Gap: clear statement of what is missing/inconsistent
- Evidence:
  - PRD/PID requirement reference
  - Architecture reference
- Impact: delivery/quality/business impact
- Recommendation: specific remediation
- Status: `Open | In Progress | Resolved | Accepted Risk`

## 5. PRD/PID Coverage Matrix

Columns:

- Requirement ID/Topic
- Source (`PRD` or `PID`)
- Architecture Coverage (`Full | Partial | Missing | Conflicting`)
- Notes

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks
- Integration/dependency risks
- Non-functional readiness risks
- Rollout/migration/operations risks

## 7. Open Questions and Assumptions

List only unresolved items that materially affect approval.

## 8. Approval Log

- Current approval status:
- Approval date:
- Approved by:
- Approval conditions (if any):
