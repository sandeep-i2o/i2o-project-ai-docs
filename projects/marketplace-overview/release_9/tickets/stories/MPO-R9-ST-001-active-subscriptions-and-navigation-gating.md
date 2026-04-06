---
ticket_type: story
local_key: MPO-R9-ST-001
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Active Subscriptions and Navigation Gating

## Story
**As a** Brand Protection client,
**I want** to view only my active marketplace subscriptions with correct module-gated links,
**so that** I can verify coverage and navigate to enabled screens confidently.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** This is the entry-value slice for the page and unblocks all downstream actions.
- **Technical (Bob-Builder):** Straightforward implementation via `/marketplace-overview/config` using `org_market_mapping`, `brand_master`, `account/account_brand`, and `ui_config` resolution.

## Acceptance Criteria
1. Active cards render only for org-scoped active marketplace+region mappings with correct brand and enforcement counts.
2. Enforcement popup shows only account names and linked brands; zero-account state renders explicit empty message.
3. `View analytics`, `View enforcement`, and `Brand Violations` links render only when enabled via `ui_config` property mapping.

## Tasks
- [ ] Implement/verify backend config aggregation and DTO mapping for active subscriptions and enabled modules (AC: 1, 3).
- [ ] Implement frontend active card/popup rendering and module-gated links (AC: 1, 2, 3).
- [ ] Add unit/integration tests for `ui_config` mapping and empty-state handling (AC: 2, 3).

## Dev Notes
Use the release_9 contract where active subscriptions come from `org_market_mapping` and navigation gating comes from `ui_config`. Preserve `org_id` token scope on every query.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 6.1, 7.1, 8.1, 9.2, 9.3)
- `projects/marketplace-overview/release_9/docs/requirements/prd.md` (US001, US009)

### Testing Standards
- **Frameworks**: Jasmine/Karma (frontend), JUnit + Mockito + Testcontainers (backend), Playwright for E2E.
- **Requirements**: Validate link-visibility permutations from `BrandProtector*` keys and enforcement popup edge states.

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

