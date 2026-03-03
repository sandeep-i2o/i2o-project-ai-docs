---
name: architecture-review-remediation
description: Incorporate architecture-review findings into architecture.md by repairing gaps, inconsistencies, and missing decisions with requirement traceability and explicit resolution status. Use when a user asks to update, fix, remediate, or rewrite architecture documentation after running review-architecture or after receiving a severity-ranked architecture review report.
---

# Architecture Review Remediation

## Overview

Apply architecture-review output to repair architecture documentation, not just summarize findings. Prioritize P0 and P1 issues first, then close P2/P3 items where feasible while preserving clear traceability from finding to document change.

## Required Input

- `project_name`

## Required Files

Read these files before editing:

- `i2o-project-ai-docs/projects/{project_name}/{release_version}/docs/design/architecture-review.md`
- `i2o-project-ai-docs/projects/{project_name}/{release_version}/docs/design/architecture.md`

Also read when available for requirement validation:

- `i2o-project-ai-docs/projects/{project_name}/{release_version}/docs/design/prd.md`

If `architecture-review.md` is missing, stop and ask the user to run `review-architecture` first or provide the correct path.

## Workflow

1. Parse findings and resolution state
- Extract each finding ID, severity, status, affected area, evidence, and recommendation.
- Build a remediation queue sorted by severity and status: Open P0/P1 first, then P2, then P3.

2. Build a finding-to-change plan
- For every queued finding, define:
  - exact `architecture.md` section to update or create
  - concrete text changes needed
  - acceptance check proving the gap is resolved
- Use `references/finding-resolution-matrix.md` to keep mapping explicit.

3. Repair architecture documentation
- Update `architecture.md` with implementable decisions, not generic intent.
- Add missing architecture details where needed:
  - component responsibilities and boundaries
  - data contracts and integration touchpoints
  - security controls and failure handling
  - reliability, observability, and operations runbook expectations
  - rollout, migration, rollback, and dependency constraints
- Keep existing valid content. Replace only incorrect, conflicting, or incomplete sections.

4. Re-validate against review evidence
- Re-check each finding against updated architecture text.
- Mark finding result as:
  - `Resolved`: architecture text now satisfies recommendation with evidence
  - `Partially Resolved`: progress exists but key gaps remain
  - `Deferred`: intentionally postponed with justification and owner
  - `Cannot Resolve`: blocked by external decision/dependency

5. Produce remediation artifact
- Write `i2o-project-ai-docs/projects/{project_name}/{release_version}/docs/design/architecture-remediation.md`.
- Include:
  - summary by severity
  - finding-to-change matrix
  - unresolved/deferred items with owners and blocking decisions
  - validation notes for resolved items

## Editing Standards

- Prioritize technical feasibility and delivery safety over stylistic edits.
- Do not mark high-severity findings resolved without direct evidence in `architecture.md`.
- Keep language concrete and implementation-ready.
- Distinguish confirmed facts from assumptions.
- Preserve architecture structure unless reorganization is required to fix traceability.

## Output Requirements

Always provide:

- Updated `architecture.md` with concrete repairs.
- New or updated `architecture-remediation.md` with full finding traceability.
- A concise completion summary to the user:
  - resolved finding IDs
  - remaining risks and blockers
  - decisions required from user/stakeholders

If critical blockers remain unresolved, explicitly state that architecture is not approval-ready.

## References

- Use `references/finding-resolution-matrix.md` for consistent finding-to-fix mapping.
