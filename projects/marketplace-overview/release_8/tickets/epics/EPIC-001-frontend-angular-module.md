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
updated: 2026-03-20
stories:
  - STORY-001
  - STORY-002
  - STORY-003
  - STORY-004
  - STORY-005
---

# EPIC-001 — Frontend: Marketplace Overview Angular Module

## Business Value (Charlie-Conductor)

The Marketplace Overview dashboard consolidates KPI data from Analytics, Brand Violations, and Enforcement Centre across four marketplaces (Amazon, Walmart, eBay, Target) into a single-screen experience for Brand Protector users. By aligning with the latest **i2o-retail** frontend architecture (March 2026), we ensure long-term maintainability, high-performance data rendering via AG Grid Enterprise, and robust E2E coverage using Playwright. This feature remains gated behind the `brand-protector` Keycloak role and reuses the established lazy-loaded Angular module pattern.

## Technical Feasibility (Bob-Builder)

- **Stack:** Angular **15.2.10**, TypeScript **4.9.5**, Angular Material **15.2.9**, PrimeNG **15.0.0** — fully aligned with `frontendapplication-i2oretail` March 2026 baselines.
- **Data Grid:** Upgraded to **AG Grid Enterprise 21.1.1** to support advanced cell rendering and performance-optimised virtual scrolling.
- **Testing:** Unit tests via Jasmine/Karma; E2E automation via **Playwright (^1.58.x)** alongside legacy Protractor support.
- **Effort estimate:** Medium-Large (3–4 sprints for all stories).
- **Hard dependency:** `bp_marketplace_overview_card` and `bp_marketplace_overview_table` componentId entries must be registered in `i2oretail.component` PostgreSQL table before frontend integration testing begins.
- **Wiring Policy:** All feature-reusable UI must be declared/imported via **CoreModule** (`src/app/modules/core/core.module.ts`) per project standards; no standalone `common.module.ts`.

## Scope

This epic covers the implementation of the `marketplace-overview` module in `frontendapplication-i2oretail`:

| Area | Deliverable |
|------|-------------|
| Module scaffold | Lazy-loaded `marketplace-overview` module + routing |
| State management | `MarketplaceOverviewStateService` (RxJS BehaviorSubject) |
| API service | `MarketplaceOverviewApiService` (HTTP calls to i2o-reseller) |
| Filter Bar | Multi-brand select, Region dropdown, Calendar (week mode), View toggle |
| Card View | `MarketplaceCardListComponent` + `MarketplaceCardComponent` |
| Table View | `MarketplaceTableComponent` (**AG Grid Enterprise 21.1.1**, 10 KPI columns) |
| Initiate Trial | `InitiateTrialDialogComponent` + brand-selection dialog |
| Constants | Feature-scoped `marketplace-overview.constants.ts` for feature literals |
| Unit tests | Jasmine/Karma ≥ 80% service coverage, ≥ 70% component coverage |
| E2E tests | **Playwright** scenarios for US001–US006 (Section 14.3 of architecture) |

## Dependencies

- **EPIC-002** (i2o-reseller backend) must be deployed to DEV before Step 2 integration.
- **componentId registration** (recorded in PostgreSQL) is a hard gate before integration testing.
- **EPIC-003** (scheduler) must complete weekly run for real KPI data availability.

## Story Breakdown

| Story | Title | US Covered |
|-------|-------|-----------|
| STORY-001 | Module scaffold, routing, models, API service, state service | US001, US002 |
| STORY-002 | Filter Bar component | US002, US006 |
| STORY-003 | Card View — MarketplaceCard + KPI groups | US003 |
| STORY-004 | Table View — AG Grid Enterprise with all KPI columns | US004 |
| STORY-005 | Initiate Trial button + dialog (multi-brand enforcement) | US005 |

## Acceptance Criteria (Epic-level)

1. The Marketplace Overview page renders at `/brand-protector/benefits/marketplace-overview`.
2. The page is accessible only to users with the `brand-protector` Keycloak role.
3. Card view and Table view display the correct KPIs for all four marketplaces.
4. Filter state (brand, region, week, view mode) persists across Card ↔ Table toggle.
5. Trial marketplaces (eBay, Target) display `Initiate Trial` button with correct behaviour.
6. All unit tests pass; coverage targets met (services ≥ 80%, components ≥ 70%).
7. E2E test scenarios US001–US006 pass using **Playwright** in the DEV environment.

## Architecture References

- Section 5.1 — Frontend Angular module structure
- Section 9 — Frontend architecture (routing, state management, component tree)
- Section 8.1 — Reused API contracts (`getCardData`, `getGridCardData`)
- Section 14 — Testing strategy (updated to Playwright)
- SUMMARY-frontendapplication-i2oretail.md — March 2026 baselines
