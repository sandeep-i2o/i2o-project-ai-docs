---
ticket_type: story
local_key: MPO-R9-ST-006
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Request Audit Flow with Duplicate and Retry Semantics

## Story
**As a** Brand Protection client,
**I want** to request an audit report for selected brands and marketplace,
**so that** I can receive a scoped report in the promised SLA window.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Audit request is a high-intent action that should stay frictionless even on transient mail failures.
- **Technical (Bob-Builder):** Similar to pilot path but with duplicate-allowed semantics and `[DUPLICATE]` email subject handling.

## Acceptance Criteria
1. `POST /marketplace-overview/request-audit` validates marketplace using `org_market_mapping.enabled=false` and accepts duplicate requests.
2. Duplicate requests succeed and mark outbound email subject with `[DUPLICATE]` prefix while returning confirmation message.
3. Transport/5xx email failures return `202 Accepted` and persist outbox rows for scheduled retry.

## Tasks
- [ ] Implement audit request service path with duplicate-detection annotation and duplicate subject formatting (AC: 1, 2).
- [ ] Implement frontend request-audit modal/CTA states and response message handling for success + accepted retry states (AC: 2, 3).
- [ ] Add tests for standard success, duplicate success, and queued-retry semantics (AC: 2, 3).

## Dev Notes
Unlike pilot flow, audit flow allows duplicate requests by design. Keep marketplace validation source aligned with pilot (`org_market_mapping.enabled=false`).

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 6.3, 8.5, 12.1.1, 12.3)
- `projects/marketplace-overview/release_9/docs/requirements/prd.md` (US006)

### Testing Standards
- **Frameworks**: JUnit/Mockito/REST Assured, Jasmine/Karma, Playwright.
- **Requirements**: Assert duplicate audit behavior is non-blocking and outbox retry persists on transient email failures.

## Story Draft Validation
Against checklist templates:
- `checklist/story-draft-checklist.md`
- `templates/story-draft-checklist.md` (fallback for missing `.aiccelerate` path)

### Goal and Context Clarity
- [x] Story purpose clear
- [x] Epic relationship evident
- [x] Dependencies identified

### Technical Implementation
- [x] Key files identified
- [x] Technologies specified
- [x] APIs described

### Self-Containment
- [x] Core information included
- [x] Assumptions explicit
- [x] Terms explained

**Validation Result**: READY
