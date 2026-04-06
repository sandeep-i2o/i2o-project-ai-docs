---
ticket_type: story
local_key: MPO-R9-ST-002
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Unsubscribed Placeholder Cards and CTA Shell

## Story
**As a** Brand Protection client,
**I want** to see unsubscribed marketplace cards with clear CTA actions,
**so that** I can initiate pilot/audit actions even while metrics are deferred.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Maintains conversion flow visibility in release_9.
- **Technical (Bob-Builder):** FE-only metrics (`##`) with no backend retrieval path as per approved release decision.

## Acceptance Criteria
1. Unsubscribed cards render with placeholder metrics (`##`) and "Data pending" semantics in the right column.
2. No backend endpoint for unsubscribed metrics is called or required in release_9.
3. `Start free pilot` and `Request Audit Report` CTAs remain available per card.

## Tasks
- [ ] Implement unsubscribed card rendering constants/models for placeholder values (AC: 1).
- [ ] Ensure frontend state layer does not call any unsubscribed-metrics API (AC: 2).
- [ ] Add regression test to assert placeholder-only behavior and CTA visibility (AC: 1, 3).

## Dev Notes
This story intentionally preserves accepted-risk scope. PRD text still references ranked metric cards, but release_9 architecture and review disposition approve placeholder-only behavior.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 4.1, 7.4, 8.2, 9.4)
- `projects/marketplace-overview/release_9/docs/design/architecture-review.md` (AR-013 accepted risk)

### Testing Standards
- **Frameworks**: Jasmine/Karma, Playwright.
- **Requirements**: Assert no network call to unsubscribed-metrics endpoint and verify UI placeholders on card metrics.

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

