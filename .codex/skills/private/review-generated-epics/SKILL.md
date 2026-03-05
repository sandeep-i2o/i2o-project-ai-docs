---
name: review-generated-epics
description: Review generated Epics/Stories against PRD and architecture artifacts, then produce a gap-and-ambiguity audit report. Use when tickets exist under i2o-project-ai-docs/projects/{project_id}/{release_id}/docs/tickets (or nearby tickets folders) and Codex must validate requirement coverage, architectural alignment, sequencing, and clarity before implementation or Jira publishing.
---

# Review Generated Epics

Review ticket quality before execution. Produce a traceable audit between requirements, architecture, and generated epics/stories, and write `review-tickets.md` with concrete findings.

## Inputs

Collect these inputs first:
- `project_id`
- `release_id`
- Optional scope filter: only epics, only stories, or full set

Resolve primary paths:
- PRD: `projects/{project_id}/{release_id}/docs/requirements/prd.md`
- Architecture (preferred order):  
`projects/{project_id}/{release_id}/docs/design/architecture.md`  
`projects/{project_id}/{release_id}/docs/design/architecture-review.md`  
`projects/{project_id}/{release_id}/docs/design/architecture-remediation.md`
- Tickets (preferred): `projects/{project_id}/{release_id}/docs/tickets`

If `docs/tickets` does not exist, fall back to:
- `projects/{project_id}/{release_id}/tickets`
- `features/{project_id}/tickets`

Stop and report missing critical inputs if neither PRD nor architecture is available.

## Workflow

### 1) Build a requirement baseline

Extract from PRD:
- Functional requirements and user journeys
- Non-functional requirements (performance, security, observability, reliability)
- Constraints, assumptions, and explicit out-of-scope items

Extract from architecture:
- Service/component boundaries
- Data flow, storage, integration points
- Operational and deployment constraints

Assign short IDs during review if the docs do not provide IDs:
- `PRD-RQ-###`, `ARC-RQ-###`, `NFR-###`

### 2) Parse generated epics and stories

For each ticket, capture:
- Ticket ID/title
- Parent-child relationship (Epic -> Story)
- Scope summary
- Acceptance criteria quality
- Dependencies and sequencing clues

Flag malformed tickets immediately:
- Missing acceptance criteria
- No testability signal
- Vague or contradictory scope

### 3) Run alignment checks

Use `references/gap-taxonomy.md` and evaluate:
- Coverage gaps: requirement exists but no ticket covers it
- Architecture drift: ticket asks for behavior that violates architecture direction
- Sequencing risk: prerequisites missing or ordered incorrectly
- NFR omission: quality attributes absent in implementation tickets
- Duplication/overlap: multiple tickets claim same deliverable
- Ambiguity: terms, ownership, or completion criteria unclear

### 4) Score findings

Assign severity per finding:
- `Critical`: blocks delivery or introduces high implementation risk
- `High`: likely rework or significant scope/quality risk
- `Medium`: clarity/coverage issue with moderate impact
- `Low`: improvement opportunity

Every finding must include evidence:
- Source requirement reference
- Ticket reference
- Short rationale (1-3 lines)

### 5) Write report

Create or overwrite:
- `projects/{project_id}/{release_id}/docs/tickets/review-tickets.md`

If tickets came from fallback location, write the report alongside that tickets folder.

Use `assets/review-tickets-template.md` as the base structure.

## Output Contract

The `review-tickets.md` report must contain:
- Scope and input files reviewed
- Executive summary with readiness verdict (`Ready`, `Ready with Conditions`, `Not Ready`)
- Traceability matrix (requirements vs ticket coverage)
- Gaps by severity (Critical -> Low)
- Ambiguities list (separate from gaps)
- Recommended ticket updates (exact Epic/Story references)
- Open questions and assumptions
- Update `progress.md` with the readiness verdict and findings under projects/docs/{project_id}/{release_id}/docs/progress.md

## Quality Rules

Enforce these rules while reviewing:
- Prefer evidence over interpretation; cite exact file/section names.
- Do not invent requirements absent from PRD/architecture.
- Treat ambiguity as a first-class finding, not a minor note.
- Keep recommendations actionable: who/what/where should change.
- Keep the review concise; avoid restating full ticket text.

## Reference Files

Load only as needed:
- `references/gap-taxonomy.md`: detailed definitions and detection heuristics
- `assets/review-tickets-template.md`: markdown template for final report
