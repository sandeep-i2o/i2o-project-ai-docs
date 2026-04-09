---
ticket_type: story
local_key: MPO-R9-ST-002
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: Unsubscribed Marketplace Metrics Cards and CTA State

## Story
**As a** Brand Protection client,
**I want** to see unsubscribed marketplace cards with clear CTA actions,
**so that** I can evaluate risk from actual marketplace metrics and initiate pilot/audit actions.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Maintains conversion flow visibility in release_9.
- **Technical (Bob-Builder):** `/marketplace-overview/config` must include `unsubscribedMarketplaces[]` from `marketplace_unsubscribed_metrics`, with UI fallback only when data is missing.

## Acceptance Criteria
1. `GET /marketplace-overview/config` returns `unsubscribedMarketplaces[]` sourced from `marketplace_unsubscribed_metrics`, including `totalProducts`, `totalListings`, `totalResellers`, `trialInitiated`, `auditRequested`, `auditStatus`, `auditType`, `auditRequestedTime`, and `auditReportGcsLink`.
2. Unsubscribed cards render backend values for totals and derived `painLevel` (`LOW`/`MEDIUM`/`HIGH`) using reseller thresholds (`0-50`, `51-200`, `201+`).
3. If a metric field is missing/null for a card, UI renders `##` and `Data pending` only for that field/card (no global placeholder mode).
4. `Start free pilot` and `Request Audit Report` CTAs remain available per card, with CTA state hydrated from backend flags (`trialInitiated`, `auditRequested`) plus existing pilot-request guard behavior.
5. No separate unsubscribed-metrics endpoint is introduced; data is delivered through `/marketplace-overview/config`.

## Tasks
- [ ] Implement backend query + DTO mapping from `marketplace_unsubscribed_metrics` into `MarketplaceOverviewConfigResponse.unsubscribedMarketplaces[]` (AC: 1, 5).
- [ ] Update frontend unsubscribed-card model/state rendering for numeric metrics, pain-level mapping, and per-field fallback (`##`) (AC: 2, 3).
- [ ] Hydrate CTA state from backend flags while preserving pilot duplicate/disabled behavior (AC: 4).
- [ ] Add integration + UI regression tests for table-backed rendering, fallback behavior, and CTA visibility/state transitions (AC: 1, 2, 3, 4, 5).

## Dev Notes
Architecture v1.12 supersedes placeholder-only behavior. Unsubscribed metrics are now sourced from `marketplace_unsubscribed_metrics` and returned in `/marketplace-overview/config` as part of page bootstrap.

Key table contract columns for this story:
- `org_id`, `marketplace_id`, `total_products`, `total_listings`, `total_resellers`
- `audit_requested`, `trial_initiated`
- `temp1`, `temp2`
- `audit_status`, `audit_type`, `audit_requested_time`, `audit_report_gcs_link`

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 4.1, 6.1, 7.2, 7.4, 8.1, 8.2, 9.4, 10.5)
- `projects/marketplace-overview/release_9/docs/design/ADR/adr-09-04-2026.MD`

### Testing Standards
- **Frameworks**: JUnit + REST Assured, Jasmine/Karma, Playwright.
- **Requirements**: Validate `/config` returns unsubscribed metrics contract fields, UI pain-level mapping, and per-card/field fallback (`##`) only for missing values.

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
