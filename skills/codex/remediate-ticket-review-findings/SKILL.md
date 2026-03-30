---
name: remediate-ticket-review-findings
description: Remediate review findings produced by ticket-review workflows (for example `review-tickets.md` from review-generated-epics), then update Epic/Story markdown files under i2o-project-ai-docs/projects/{project_id}/{release_id}/tickets/** (or docs/tickets fallback), generate a remediation completion summary report, and update progress tracking in projects/progress.md (with release-level fallback).
---

# Remediate Ticket Review Findings

Remediate ticket-review findings into concrete Epic/Story updates and track closure status. Maintain traceability from each finding to each ticket change.

## Inputs

Collect first:
- `project_id`
- `release_id`
- Optional scope filter: `critical-only`, `high+`, or `all`

Resolve files in this order:
- Review report:
  - `projects/{project_id}/{release_id}/tickets/review-tickets.md`
  - `projects/{project_id}/{release_id}/docs/tickets/review-tickets.md`
- Ticket roots:
  - `projects/{project_id}/{release_id}/tickets`
- Progress trackers:
  - `projects/{project_id}/{release_id}/progress.md` (fallback/release tracker)

Stop and report if review report or ticket root is missing.

## Workflow

### 1) Parse remediation scope from review report

Read:
- Section `5. Findings by Severity`
- Section `6. Ambiguities`
- Section `7. Recommended Ticket Updates`

Capture for each finding:
- Finding ID (`F-*` or `A-*`)
- Severity/type
- Source requirement refs
- Target ticket refs
- Recommended fix

Use `references/finding-action-map.md` for mapping rules.

### 2) Build remediation plan

For each finding, decide action:
- Update existing Epic/Story markdown in place
- Add missing dependency statements
- Add/clarify acceptance criteria
- Add/clarify DoD checklist items
- Create new Story only when no existing Story can own the requirement cleanly

When creating a new story:
- Use next numeric ID in `tickets/stories` (`STORY-###`)
- Add story into parent Epic frontmatter `stories:` list
- Keep status as `Draft` unless source tickets use another status convention

### 3) Apply ticket changes

Edit only required files under:
- `tickets/epics/*.md`
- `tickets/stories/*.md`

Apply minimal diffs:
- Preserve frontmatter keys and current ordering
- Keep original intent and module ownership
- Add explicit traceability in prose, for example `Remediates F-H-002`

Required remediation coverage:
- Every `Critical` and `High` finding must map to at least one ticket update
- Medium/Low findings and ambiguities must be marked as `Resolved` or `Deferred` with rationale

### 4) Validate remediation quality

Before finalizing, confirm:
- No broken Epic->Story linkage
- No duplicate ownership across epics for the same gate/deliverable
- AC statements are testable and measurable
- Dependencies are explicit where sequencing gates exist
- Newly added NFR work includes measurable thresholds and evidence expectations

### 5) Write remediation completion report

Create or overwrite:
- `{tickets_root}/review-remediation-summary.md`

Use `assets/review-remediation-summary-template.md`.

The summary must include:
- Scope and input files
- Totals: findings addressed/resolved/deferred
- Finding-by-finding disposition table
- Exact ticket files changed
- New tickets created (if any)
- Remaining open risks/questions

### 6) Update progress trackers

Update progress in this order:
1. update `projects/{project_id}/{release_id}/progress.md`

Add a dated checkpoint entry containing:
- Remediation run scope
- Count of findings resolved/deferred
- Link/path to `review-remediation-summary.md`
- Remaining blockers/gates

## Output Contract

Deliverables after execution:
- Updated Epic/Story files under selected ticket root
- `review-remediation-summary.md` alongside tickets
- Progress entry update in global and/or release progress tracker

Always report:
- Files changed
- Findings resolved vs deferred
- Any missing inputs or unresolved blockers

## Quality Rules

- Prefer direct evidence from `review-tickets.md`; do not invent new findings.
- Keep edits surgical; avoid reformatting entire ticket files.
- Maintain ID stability (`EPIC-*`, `STORY-*`, `F-*`, `A-*`).
- Preserve architecture and PRD alignment while remediating.
- If recommendation conflicts with architecture docs, mark as deferred and explain.

## Reference Files

Load only as needed:
- `references/finding-action-map.md`: mapping of finding categories to remediation actions
- `assets/review-remediation-summary-template.md`: completion summary template
