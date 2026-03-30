---
name: generate-update-architecture
description: Generate or update fullstack architecture.md from PRD and project knowledge, including technology decisions, module mapping, and checklist validation. Use when a user asks to create a new architecture document, revise an existing one, or maintain architecture decisions with ADR records.
---

# Generate or Update Fullstack Architecture

## Overview

Generate a new architecture document when none exists, or update an existing `architecture.md` when requirements change. Follow the structure in `./references/arc42-architecture-tmpl.yaml` when available.

Prefer existing projects and tech choices from knowledge summaries. Do not introduce a new stack or new project unless requirements force it.

## Required Inputs

Collect and read these inputs before drafting:

- PRD: `i2o-feature-ai-docs/features/{project_dir}/docs/requirements/prd.md`
- Frontend summary (optional but preferred): `i2o-feature-ai-docs/knowledge/projects/SUMMARY-frontend.md`
- Project summaries: all `i2o-feature-ai-docs/knowledge/projects/SUMMARY-*.md`
- Knowledge base references: `i2o-feature-ai-docs/knowledge/kb_pdfs`
- BigQuery schemas: `i2o-feature-ai-docs/knowledge/bigquery_schemas`
- PostgreSQL schemas: `i2o-feature-ai-docs/knowledge/pg_schema`
- KPI/UI query references: `i2o-project-ai-docs/knowledge/ui_data_queries`
- Architect checklist: `./checklist/architect-checklist.md`

If any mandatory path is missing, stop and ask for the correct path.

## Output Paths

Use these default paths unless the user provides different locations:

- Architecture doc: `i2o-feature-ai-docs/features/{project_dir}/docs/design/architecture.md`
- ADR directory: `i2o-feature-ai-docs/features/{project_dir}/docs/design/ADR/`
- Progress checkpoints: `i2o-feature-ai-docs/features/{project_dir}/progress.md`

## Mode Detection

1. Check whether `architecture.md` already exists.
2. If missing, run **Generate Mode**.
3. If present, run **Update Mode** and preserve stable sections while revising impacted sections.

## Progress Tracking

Create or amend `progress.md` at the project root and maintain checkpoints:

1. Context loaded
2. Project/module selection done
3. Architecture draft/update complete
4. User review complete
5. Checklist run complete
6. Gaps remediated
7. Final architecture delivered

## Generate Mode Workflow

1. Gather architectural drivers from PRD:
   - Functional requirements, NFRs, constraints, assumptions, UI/UX needs, epic/story breakdown.
2. Select projects/modules from `SUMMARY-*.md` and record in `Solution Strategy & Project Modules`.
3. Define high-level architecture:
   - Repository/package structure
   - Frontend/backend/integration patterns
4. Define definitive technology stack with versions:
   - Frontend, backend, data, DevOps, and testing.
5. Design data architecture:
   - Conceptual entities, relationships, shared TypeScript interfaces, concrete schemas, indexes, migration strategy.
6. Define API specification based on chosen style (REST/OpenAPI, GraphQL schema, or tRPC routers).
7. Design components:
   - System boundaries, frontend structure/state/routing/service layer, backend structure/data access/auth/middleware.
8. Define UI/UX architecture:
   - User flows, navigation, responsive breakpoints, core screen wireframes/states/accessibility.
9. Define integrations and workflows:
   - External APIs, auth/rate limits, fallback behavior, sequence diagrams for critical paths.
10. Define deployment and operations:
    - Monorepo structure, local setup, environment strategy, CI/CD, deployment architecture.
11. Define quality attributes and standards:
    - Security, performance, testing strategy, coding standards, observability/alerts.

## Update Mode Workflow

1. Diff current PRD/knowledge inputs against the existing `architecture.md`.
2. Update only impacted sections while retaining valid prior decisions.
3. Keep all changed choices explicit:
   - What changed
   - Why it changed
   - Impact on modules, APIs, data, operations, and tests
4. Reconcile `Solution Strategy & Project Modules` with latest `SUMMARY-*.md` analysis.
5. Ensure backward compatibility or migration notes are added for breaking changes.

## ADR Requirements (Mandatory on Update)

Whenever `architecture.md` is updated:

1. Create `docs/design/ADR/` if it does not exist.
2. Create a new ADR file named `adr-<dd-MM-yyyy>.MD`.
3. If a same-day file already exists, create `adr-<dd-MM-yyyy>-02.MD`, `-03`, etc.
4. Follow the MADR template structure from:
   - `https://github.com/adr/madr/blob/develop/template/adr-template.md`
5. Use the local baseline template at `references/adr-template.md` and fill all sections.
6. Link the ADR from the updated `architecture.md` change notes section.

## Checklist Validation (Mandatory)

After drafting/updating:

1. Share full architecture draft with the user before checklist execution.
2. After user confirmation, run architect checklist from `./checklist/architect-checklist.md`.
3. Mark each item PASS/FAIL with concrete evidence.
4. Revise architecture for all FAIL items.
5. Re-run until all critical items pass or accepted deviations are justified.
6. Include checklist results, remaining actions, and implementation readiness confidence in final output.

## Collaboration Rules

1. Present each major section for user review before finalization.
2. Ask targeted questions only for ambiguous requirements.
3. Provide recommendation + rationale when multiple options exist.
4. Require explicit confirmation for critical technology choices.
5. Mark assumptions clearly and keep them traceable.

## Final Deliverables

Always deliver:

1. Updated or newly generated `architecture.md`.
2. New ADR file for updates (`adr-<dd-MM-yyyy>.MD` format).
3. Updated `progress.md` with completed checkpoints.
4. Checklist results and remediation summary embedded in architecture output.
