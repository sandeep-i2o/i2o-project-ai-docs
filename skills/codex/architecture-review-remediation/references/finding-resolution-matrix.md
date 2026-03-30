# Finding Resolution Matrix

Use this matrix to keep each architecture-review finding traceable from evidence to concrete architecture changes.

## Required Columns

| Finding ID | Severity | Status (Before) | Affected Area | Recommendation | `architecture.md` Target Section | Planned Change | Acceptance Check | Status (After) | Evidence (Updated Section/Quote) | Owner | Notes/Blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Status Rules

- `Resolved`: Updated architecture text directly satisfies the recommendation with clear evidence.
- `Partially Resolved`: Update exists but one or more mandatory acceptance checks fail.
- `Deferred`: Work is intentionally postponed with rationale, owner, and dependency.
- `Cannot Resolve`: Blocked by an external decision or missing dependency outside architecture scope.

## Severity Handling

- Handle all open `P0` and `P1` findings first.
- Address `P2` and `P3` findings after high-severity closure unless explicitly scoped otherwise by the user.

## Acceptance Check Guidance

Use objective checks. Prefer statements such as:

- "Section defines component owner, API contract, and failure path."
- "Section includes rollback trigger, rollback steps, and blast radius."
- "Section specifies security control with enforcement point and audit signal."
- "Section defines SLO/SLI threshold and alert owner."

Avoid subjective checks such as "looks clearer" or "seems complete."
