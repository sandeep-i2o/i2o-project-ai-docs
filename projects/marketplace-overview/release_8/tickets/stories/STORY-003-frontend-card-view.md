---
id: STORY-003
title: "[MO] Frontend: Marketplace Card View — Card List & Card Component"
project: marketplace_overview
release: release_8
module: frontendapplication-i2oretail
type: Story
priority: High
epic: EPIC-001
status: Draft
estimate: 3 days
created: 2026-03-04
depends_on:
  - STORY-001
  - STORY-002
---

# STORY-003 — Frontend: Marketplace Card View

## Context

The Card View is the default view on the Marketplace Overview page. It displays one `MarketplaceCardComponent` per marketplace (Amazon, Walmart, eBay, Target). Each card contains 3 KPI groups (Analytics, Brand Violations, Enforcement Centre) for activated marketplaces, or a limited 3-KPI trial view (Listings, Resellers, WoW Change %) for trial marketplaces. Data is loaded via `POST /widget/getCardData` using `componentId: 'bp_marketplace_overview_card'`.

## Module: `frontendapplication-i2oretail`

### Files to Create

```
src/app/modules/marketplace-overview/components/
├── marketplace-overview-page/
│   ├── marketplace-overview-page.component.ts
│   ├── marketplace-overview-page.component.html
│   └── marketplace-overview-page.component.scss
├── marketplace-card-list/
│   ├── marketplace-card-list.component.ts
│   ├── marketplace-card-list.component.html
│   └── marketplace-card-list.component.scss
└── marketplace-card/
    ├── marketplace-card.component.ts
    ├── marketplace-card.component.html
    └── marketplace-card.component.scss
```

### `MarketplaceCardComponent` Specification

**Inputs:**
- `card: MarketplaceCard` — including `marketplace`, `logoUrl`, `countryFlag`, `status`, `kpiGroups`, `trialKpis`, `dataStalenessFlag`

**UI Rendering Rules:**

| Status | Displayed content |
|--------|-------------------|
| `ACTIVATED` | Marketplace logo + name, "Activated" green badge, 3 KPI groups (Analytics, Brand Violations, Enforcement Centre) |
| `TRIAL` | Marketplace logo + name, trial KPIs only (Listings, Resellers, WoW Change %), "Initiate Trial" button (STORY-005) |

**KPI rendering rules:**
- `null` value → display `--` (not 0)
- `0` value → display `0`
- Currency format for `lost_sales` only
- Percentage format for `buybox_win_pct` and `wow_change_pct`

**Stale data:**
- If `dataStalenessFlag === true`, show a warning banner: "Data is from [week range]. Latest aggregation incomplete."

**Page component:**
- On init: call `configService.getConfig()` → populate filters → call `stateService.loadData()`
- Subscribe to `data$`, `loading$` from state service
- Show loading skeleton while `loading$ === true`
- Pass `cards` array to `<app-marketplace-card-list>`

## User Stories Covered

- **US003** (AC 29–34): Amazon card shows 3 KPI sections; eBay/Target show trial cards with Initiate Trial button; Walmart BV KPIs display `--` (null)

## Acceptance Criteria

1. Card view renders one card per marketplace in the response (Amazon, Walmart, eBay, Target).
2. Activated marketplace cards show 3 KPI groups: Analytics (4 KPIs), Brand Violations (2 KPIs), Enforcement Centre (4 KPIs).
3. Trial marketplace cards (eBay, Target) show only: No. of Listings, No. of Resellers, WoW Change %.
4. `null` KPI values render as `--`; `0` values render as `0`.
5. Walmart's Brand Violation KPIs (`total_brand_violation`, `violations_closed`) show `--` (returned as `null` from API).
6. Stale data banner appears when `dataStalenessFlag === true` on any card.
7. Loading skeleton is shown while `loading$ === true`.
8. Unit tests cover card rendering for ACTIVATED and TRIAL states (≥ 70% coverage).

## Definition of Done Checklist

- [ ] `MarketplaceOverviewPageComponent` created; loads config on init, renders card or table view based on `viewMode`
- [ ] `MarketplaceCardListComponent` created; passes cards array to child
- [ ] `MarketplaceCardComponent` created; renders ACTIVATED and TRIAL states correctly
- [ ] `null` → `--` rendering confirmed in template
- [ ] Stale data banner implemented
- [ ] Loading skeleton matches existing app pattern
- [ ] Unit tests written achieving ≥ 70% component coverage

## Architecture References

- Section 7.3 — TypeScript interfaces (`MarketplaceCard`, `KpiGroup`, `KpiItem`)
- Section 9.3 — Component tree
- Section 8.1 — `POST /widget/getCardData` request shape
- Section 6.1 — Card view data load sequence
- Section 10.2 — Stale data handling (frontend banner)
