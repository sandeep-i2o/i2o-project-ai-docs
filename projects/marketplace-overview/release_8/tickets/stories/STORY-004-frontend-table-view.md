---
id: STORY-004
title: "[MO] Frontend: Table View — AG Grid Enterprise with KPI Columns"
project: marketplace_overview
release: release_8
module: frontendapplication-i2oretail
type: Story
priority: High
epic: EPIC-001
status: Draft
estimate: 2 days
created: 2026-03-04
updated: 2026-03-20
depends_on:
  - STORY-001
  - STORY-002
---

# STORY-004 — Frontend: Table View — AG Grid Enterprise with KPI Columns

## Context

The Table View is the alternative layout on the Marketplace Overview page, activated via the Card/Table toggle in the Filter Bar. It uses **AG Grid Enterprise 21.1.1** (licensed and configured in `frontendapplication-i2oretail`) to display all four marketplaces as rows with all 10 KPI columns plus a Status column. Data is loaded via `POST /report/getGridCardData` with `componentId: 'bp_marketplace_overview_table'`, `pageSize: 10`, `sort: 'marketplace ASC'`.

## Module: `frontendapplication-i2oretail`

### Files to Create

```
src/app/modules/marketplace-overview/components/marketplace-table/
├── marketplace-table.component.ts
├── marketplace-table.component.html
└── marketplace-table.component.scss
```

### Column Specification (AG Grid Enterprise)

| Column | Data Source | Format | Notes |
|--------|-------------|--------|-------|
| Marketplace | `marketplace` | Logo + name | Custom cell renderer |
| Lost Sales | `lost_sales` | Currency (USD) | — |
| Total Closed Listings | `total_closed_listings` | Count | — |
| Reseller Removed | `reseller_removed` | Count | — |
| Buybox Win % | `buybox_win_pct` | Percentage | `null` → `--` |
| Total Brand Violation | `total_brand_violation` | Count | `null` → `--` (Walmart) |
| Violations Closed | `violations_closed` | Count | `null` → `--` (Walmart) |
| Notification in Queue | `notification_in_queue` | Count | — |
| C&D Pending | `cnd_pending` | Count | — |
| Total C&D Sent | `total_cnd_sent` | Count | — |
| Test Purchase | `test_purchase` | Count | — |
| Status | `status` | ACTIVATED badge / Initiate Trial button | Custom cell renderer |

### Behaviour

- **Default sort:** `marketplace ASC` (alphabetical — sent in API request, not client-side).
- **Default page size:** `10` (passed in API request).
- `null` values must render as `--` in all KPI cells.
- **AG Grid Enterprise** features: Enable `rowModelType: 'clientSide'`, `pagination: true`, and `paginationPageSize: 10`.
- Filter state triggers a fresh `POST /report/getGridCardData` call when toggled to table view.

### API Call Contract

```json
{
  "componentId": "bp_marketplace_overview_table",
  "filters": { "marketplace": [...], "brands": [...], "region": "US", "start_date": "...", "end_date": "..." },
  "page": 0,
  "pageSize": 10,
  "sort": "marketplace ASC"
}
```

## User Stories Covered

- **US004** (AC 41–44): Table view renders all 4 marketplaces with correct KPI columns; Walmart BV columns show `--`; page size defaults to 10; default sort is marketplace ASC

## Acceptance Criteria

1. Table view renders when `viewMode === 'table'` is set in state.
2. All 12 columns (Marketplace, 10 KPIs, Status) are visible and formatted correctly.
3. Default row sort is `marketplace ASC` (alphabetical).
4. Default page size is `10`.
5. Walmart rows show `--` in Brand Violation columns (`total_brand_violation`, `violations_closed`).
6. Any `null` KPI value renders as `--`.
7. Filter changes trigger a fresh `getGridCardData` API call.
8. AG Grid Enterprise virtual scroll and pagination configured correctly.
9. **Playwright** tests verify table rendering and `null` handling.
10. Unit tests cover column definition and `null` rendering (≥ 70% component coverage).

## Definition of Done Checklist

- [ ] `MarketplaceTableComponent` created with **AG Grid Enterprise** column definitions
- [ ] `null` → `--` value formatter applied to all KPI columns
- [ ] API call includes `pageSize: 10` and `sort: 'marketplace ASC'`
- [ ] Status column renders ACTIVATED badge or Initiate Trial button
- [ ] Filter state change triggers fresh API call on table view
- [ ] AG Grid pagination and virtual scroll configured
- [ ] Unit tests written achieving ≥ 70% component coverage
- [ ] **Playwright** E2E test passed for table view

## Architecture References

- Section 8.1 — `POST /report/getGridCardData` request shape and defaults
- Section 9.3 — Component tree (MarketplaceTableComponent)
- Section 10.2 — N/A KPI handling (`null` → `--`)
- SUMMARY-frontendapplication-i2oretail.md — AG Grid Enterprise standards
