---
ticket_type: story
local_key: MPO-R9-ST-003
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Filter Bar Brand and Enforcement Behavior

## Story
**As a** Brand Protection client,
**I want** brand and enforcement account filters to update page content predictably,
**so that** I can focus on relevant marketplaces and send correctly scoped requests.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Filtering is required to make the page operational for multi-brand clients.
- **Technical (Bob-Builder):** Implemented in frontend state service with deterministic defaults and debounced updates.

## Acceptance Criteria
1. Default filter state is: all brands selected, all enforcement accounts selected, region set to US.
2. Selecting/deselecting brands updates active subscriptions and CTA brand-context payload behavior.
3. Clearing all brands displays explicit empty-state prompt across both columns.

## Tasks
- [ ] Implement filter state model/BehaviorSubject defaults and update handlers (AC: 1, 2).
- [ ] Connect filter outputs to active cards and CTA context binding (AC: 2).
- [ ] Add debounce and empty-state handling tests for all-brands-cleared path (AC: 3).

## Dev Notes
Unsubscribed metrics are table-backed in release_9 (`marketplace_unsubscribed_metrics`) and returned via `/marketplace-overview/config`. Brand filter still drives pilot/audit payload context, while metric values remain backend-provided with per-field fallback only for missing data.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 5.2, 8.1, 8.2, 9.4, 12.2)
- `projects/marketplace-overview/release_9/docs/requirements/prd.md` (US003)

### Testing Standards
- **Frameworks**: Jasmine/Karma + Playwright.
- **Requirements**: Validate defaults, single-brand and all-clear scenarios, and enforcement account narrowing.

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
