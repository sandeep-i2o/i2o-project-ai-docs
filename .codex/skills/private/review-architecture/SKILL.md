---
name: review-architecture
description: Perform a critical architecture audit against PRD and PID documents, focused on technical feasibility, design gaps, delivery risks, and requirement coverage. Use when a user asks for brutally honest architecture review, PRD-to-architecture gap analysis, or approval-ready architecture assessment for a project in i2o-project-docs.
---

# Review Architecture

## Overview

Run a strict, evidence-based review of architecture quality and feasibility against product intent. Surface hard blockers, weak assumptions, missing decisions, and inconsistencies early.

## Required Input

- `project_name`

## Required Files

Read these files first:

- `i2o-project-docs/projects/{project_name}/docs/design/architecture.md`
- `i2o-project-docs/projects/{project_name}/docs/design/prd.md`

If any file is missing, stop and ask the user for the correct path before continuing.

## Review Standards

- Be direct and explicit. Avoid softening critical risks.
- Ground every finding in evidence from PRD, PID, or architecture text.
- Distinguish facts, assumptions, and inferences.
- Prioritize feasibility, implementation risk, and requirement traceability.
- Do not approve while open P0/P1 issues remain unresolved.

## Workflow

1. Load and parse all three documents.
2. Extract requirement intents from PRD and PID into a coverage checklist.
3. Evaluate architecture for:
   - Functional coverage completeness
   - Non-functional coverage (security, scale, reliability, observability, operations)
   - Technical feasibility and implementation realism
   - Dependency and integration assumptions
   - Migration, rollout, and failure-handling readiness
4. Identify and classify gaps:
   - `P0`: Blocker; cannot proceed safely
   - `P1`: High risk; likely to cause failure/rework
   - `P2`: Important quality gap; should be fixed soon
   - `P3`: Improvement suggestion
5. Draft the review using `references/report-template.md`.
6. Share findings with the user and request resolution decisions for open items.
7. Revise the report based on user feedback and repeat review-feedback cycles until explicit user approval.
8. Write the final approved report to:
   - `i2o-feature-docs/features/{project_name}/docs/design/architecture-review.md`

## Approval Loop

Repeat until approved:

1. Present unresolved findings and required decisions.
2. Ask targeted questions only for ambiguous or disputed items.
3. Update severities/status after user clarifications.
4. Regenerate the report with a clear approval state.

Approval is complete only after the user explicitly confirms approval.

## Output Requirements

Always generate `architecture-review.md` with:

- Executive verdict
- Severity-ranked findings with evidence
- PRD/PID-to-architecture coverage matrix
- Feasibility verdict and delivery risks
- Open questions or assumptions
- Final approval status and date

Use concise, technical language. Prefer actionable recommendations over generic commentary.
