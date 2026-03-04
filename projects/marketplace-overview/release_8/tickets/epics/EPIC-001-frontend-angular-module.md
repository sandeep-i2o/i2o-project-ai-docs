---
id: EPIC-001
title: "[MO] Frontend — Marketplace Overview Angular Module"
project: marketplace_overview
release: release_8
module: frontendapplication-i2oretail
type: Epic
priority: High
status: Draft
created: 2026-03-04
stories:
  - STORY-001
  - STORY-002
  - STORY-003
  - STORY-004
  - STORY-005
---

# EPIC-001 — Frontend: Marketplace Overview Angular Module

## Business Value (Charlie-Conductor)

The Marketplace Overview dashboard consolidates KPI data from Analytics, Brand Violations, and Enforcement Centre across four marketplaces (Amazon, Walmart, eBay, Target) into a single-screen experience for Brand Protector users. This eliminates context-switching between sub-modules and reduces reporting time for Account Managers. The feature is gated behind the existing `brand-protector` Keycloak role and reuses the established lazy-loaded Angular module pattern — minimising delivery risk.

## Technical Feasibility (Bob-Builder)

- **Stack:** Angular 15, PrimeNG (dropdowns, calendar), AG Grid Community (table view), RxJS BehaviorSubject pattern — all pre-existing in `frontendapplication-i2oretail`.
- **No new library dependencies** required.
- **Effort estimate:** Medium-Large (3–4 sprints for all stories).
- **Hard dependency:** `bp_marketplace_overview_card` and `bp_marketplace_overview_table` componentId entries must be registered in `i2oretail.component` PostgreSQL table **before** frontend integration testing begins (Open Item #2 — 🔴 GO/NO-GO GATE).
- **Data retrieval:** Frontend reuses `POST /widget/getCardData` and `POST /report/getGridCardData` — no new data-fetch endpoints.

## Scope

This epic covers everything inside `frontendapplication-i2oretail`:

| Area | Deliverable |
|------|-------------|
| Module scaffold | Lazy-loaded `marketplace-overview` Angular module + routing |
| State management | `MarketplaceOverviewStateService` (RxJS BehaviorSubject) |
| API service | `MarketplaceOverviewApiService` (HTTP calls to i2o-reseller) |
| Filter Bar | Brand multi-select, Region dropdown, Calendar (week mode), View toggle |
| Card View | `MarketplaceCardListComponent` + `MarketplaceCardComponent` with KPI groups |
| Table View | `MarketplaceTableComponent` (AG Grid, 10 KPI columns, marketplace ASC sort, pageSize 10) |
| Initiate Trial | `InitiateTrialDialogComponent` + brand-selection dialog for multi-brand case |
| Data models | `marketplace-kpi.model.ts`, `marketplace-filter.model.ts`, `marketplace-activation.model.ts` |
| Unit tests | Jasmine/Karma ≥ 80% service coverage, ≥ 70% component coverage |
| E2E scenarios | US001–US006 test scenarios (Section 14.3 of architecture) |

## Dependencies

- **EPIC-002** (i2o-reseller backend) must be deployed to DEV before Step 2 integration.
- componentId registration (Open Item #2) is a hard gate before integration testing.
- EPIC-003 (scheduler) must complete weekly run before real KPI data is available.

## Story Breakdown

| Story | Title | US Covered |
|-------|-------|-----------|
| STORY-001 | Module scaffold, routing, models, API service, state service | US001, US002 |
| STORY-002 | Filter Bar component | US002, US006 |
| STORY-003 | Card View — MarketplaceCard + KPI groups | US003 |
| STORY-004 | Table View — AG Grid with all KPI columns | US004 |
| STORY-005 | Initiate Trial button + dialog (multi-brand enforcement) | US005 |

## Acceptance Criteria (Epic-level)

1. The Marketplace Overview page renders at `/brand-protector/benefits/marketplace-overview`.
2. The page is accessible only to users with the `brand-protector` Keycloak role.
3. Card view and Table view display the correct KPIs for all four marketplaces.
4. Filter state (brand, region, week, view mode) persists across Card ↔ Table toggle.
5. Trial marketplaces (eBay, Target) display `Initiate Trial` button with correct behaviour.
6. All unit tests pass; coverage targets met (services ≥ 80%, components ≥ 70%).
7. E2E test scenarios US001–US006 pass in DEV environment.

## Architecture References

- Section 5.1 — Frontend Angular module structure
- Section 9 — Frontend architecture (routing, state management, component tree)
- Section 8.1 — Reused API contracts (`getCardData`, `getGridCardData`)
- Section 14 — Testing strategy
