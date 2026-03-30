---
name: architecture-review-remediation
description: Incorporate architecture-review findings into architecture.md by repairing gaps, inconsistencies, and missing decisions with requirement traceability and explicit resolution status. Use when a user asks to update, fix, remediate, or rewrite architecture documentation after running review-architecture or after receiving a severity-ranked architecture review report.
---

# Architecture Review Remediation

## Overview

Repair architecture documentation based on architecture-review findings. Prioritize closure of P0/P1 risks with concrete, implementation-ready architecture decisions and explicit evidence.

## Required Input

- `project_name`

## Required Files

Read these files before editing:

- `projects/{project_name}/{release_version}/docs/design/architecture-review.md`
- `projects/{project_name}/{release_version}/docs/design/architecture.md`

Also read when available for requirement validation:

- `projects/{project_name}/{release_version}/docs/design/prd.md`
- `../i2o-project-docs/projects/{project_name}/{release_version}/docs/design/prd.md`

If `architecture-review.md` is missing, stop and ask the user to run `review-architecture` first or provide the correct path.

## Workflow

1. Parse findings and resolution state.
   - Extract finding ID, severity, status, area, evidence, and recommendation.
   - Build a remediation queue sorted by severity/status: open P0/P1 first, then P2, then P3.

2. Build a finding-to-change plan.
   - For each finding in queue, define:
   - Exact `architecture.md` section to update or create
   - Concrete text changes needed
   - Acceptance check that proves closure
   - Use `references/finding-resolution-matrix.md` to keep mapping explicit.

3. Repair architecture documentation.
   - Update `architecture.md` with implementable decisions, not generic intent.
   - Add missing details where needed:
   - Component boundaries and responsibilities
   - Data contracts and integration touchpoints
   - Security controls and failure handling
   - Reliability, observability, and operations runbook expectations
   - Rollout, migration, rollback, and dependency constraints
   - Preserve valid content. Replace only incorrect, conflicting, or incomplete sections.

4. Re-validate against review evidence.
   - Re-check each finding against updated architecture text.
   - Mark disposition:
   - `Resolved`: recommendation is satisfied with direct architecture evidence
   - `Partially Resolved`: progress exists but key gap remains
   - `Deferred`: intentionally postponed with justification and owner
   - `Cannot Resolve`: blocked by external dependency or decision

5. Produce remediation artifact.
   - Write `projects/{project_name}/{release_version}/docs/design/architecture-remediation.md`.
   - Include:
   - Summary by severity
   - Finding-to-change matrix
   - Unresolved/deferred items with owners and blocking decisions
   - Validation notes for resolved items

## Editing Standards

- Prioritize technical feasibility and delivery safety over stylistic edits.
- Do not mark high-severity findings resolved without direct evidence in `architecture.md`.
- Keep language concrete and implementation-ready.
- Distinguish confirmed facts from assumptions.
- Preserve architecture structure unless reorganization is required to fix traceability.

## Output Requirements

Always produce:

- Updated `architecture.md` with concrete repairs.
- New or updated `architecture-remediation.md` with full finding traceability.

Always report to the user:

- Resolved finding IDs
- Remaining risks and blockers
- Decisions required from user or stakeholders

If critical blockers remain unresolved, state explicitly that architecture is not approval-ready.

## References

- `references/finding-resolution-matrix.md`
