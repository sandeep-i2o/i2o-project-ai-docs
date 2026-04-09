---
ticket_type: story
local_key: MPO-R9-ST-005
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Start Free Pilot Flow

## Story
**As a** Brand Protection client,
**I want** to request a free pilot from unsubscribed marketplace cards,
**so that** I can start onboarding in marketplaces not currently covered.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Converts unmonitored-marketplace intent directly into a support workflow.
- **Technical (Bob-Builder):** Requires strict validation using `marketplace_unsubscribed_metrics`, idempotent pilot tracking, and email dispatch with retry-safe behavior.

## Acceptance Criteria
1. `POST /marketplace-overview/start-pilot` validates marketplace against org-scoped unsubscribed set from `marketplace_unsubscribed_metrics` and requires at least one selected brand.
2. Successful request persists `marketplace_pilot_requests` and disables pilot CTA with `Free pilot requested` tooltip on reload.
3. Successful request updates `marketplace_unsubscribed_metrics.trial_initiated=true` for target org+marketplace.
4. Transport/5xx email failures return `202 Accepted` and queue outbox retry; duplicate pilot request returns `409`.

## Tasks
- [ ] Implement validation + persistence path for pilot requests and duplicate constraint handling (AC: 1, 2, 4).
- [ ] Update unsubscribed metrics state (`trial_initiated=true`) after accepted pilot request (AC: 3).
- [ ] Integrate frontend modal/CTA state transitions, disabled-button behavior, and response messaging (AC: 2, 3).
- [ ] Add tests for 200/202/409 outcomes, required-brand validation, metrics-table state updates, and button disabled-state hydration (AC: 1, 2, 3, 4).

## Dev Notes
Authoritative unsubscribed marketplace validation source is `marketplace_unsubscribed_metrics` for release_9 v1.12. Keep user-level duplicate suppression in `marketplace_pilot_requests`, and persist org-market state using `trial_initiated`.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 6.2, 7.2, 8.4, 11.4, 12.1.1, 12.3)
- `projects/marketplace-overview/release_9/docs/design/architecture-review.md` (AR-014 resolved)

### Testing Standards
- **Frameworks**: JUnit + Testcontainers, REST Assured, Jasmine/Karma, Playwright.
- **Requirements**: Cover validation matrix (marketplace, brands, identity claims), optimistic-acceptance retry path, and duplicate prevention.

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
