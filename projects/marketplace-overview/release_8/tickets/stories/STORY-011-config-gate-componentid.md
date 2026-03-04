---
id: STORY-011
title: "[MO] Config Gate: Register bp_marketplace_overview_card & _table componentIds in PostgreSQL"
project: marketplace_overview
release: release_8
module: i2o-reseller (PostgreSQL config)
type: Story
priority: Critical
epic: EPIC-004
status: Draft
estimate: 1–2 days
created: 2026-03-04
---

# STORY-011 — Config Gate: componentId Registration (🔴 GO/NO-GO GATE)

## Context

> **⚠️ This is the GO/NO-GO gate for all frontend integration testing (Open Item #2 in architecture Section 16).** 
> The `getCardData` and `getGridCardData` generic APIs work by looking up the `componentId` in the `i2oretail.component` PostgreSQL table to determine which BigQuery `query_id` to execute. Until `bp_marketplace_overview_card` and `bp_marketplace_overview_table` are registered, the frontend cannot complete integration tests.

This story must be completed and deployed to DEV before EPIC-001 integration testing begins.

## Module: `i2o-reseller` (PostgreSQL configuration tables)

### What Needs to Be Done

1. **Identify the correct `query_id` values** — from `query_described.csv` (or equivalent config) for:
   - Marketplace Overview card-view KPI queries
   - Marketplace Overview table-view KPI queries

2. **Register `bp_marketplace_overview_card`** in `i2oretail.component`:
   ```sql
   INSERT INTO i2oretail.component (component_id, query_id, description, active)
   VALUES ('bp_marketplace_overview_card', '<card_query_id>', 'BP Marketplace Overview - Card View', true);
   ```

3. **Register `bp_marketplace_overview_table`** in `i2oretail.component`:
   ```sql
   INSERT INTO i2oretail.component (component_id, query_id, description, active)
   VALUES ('bp_marketplace_overview_table', '<table_query_id>', 'BP Marketplace Overview - Table View', true);
   ```

4. **Register query_id entries** (if not already present) in the `query_described` config referencing the `marketplace_kpi_weekly_snapshot` BQ table.

5. **Deploy to DEV → QA → PROD** in sequence.

### Deployment Sequence

| Environment | Action | Verification |
|-------------|--------|--------------|
| DEV | Execute DML inserts | `POST /widget/getCardData` with `componentId: "bp_marketplace_overview_card"` returns data |
| QA | Execute DML inserts | Same verification in QA |
| PROD | Execute DML inserts | Same verification in PROD |

## Acceptance Criteria

1. `bp_marketplace_overview_card` is registered in `i2oretail.component` and linked to the correct `query_id`.
2. `bp_marketplace_overview_table` is registered in `i2oretail.component` and linked to the correct `query_id`.
3. `POST /widget/getCardData` with `componentId: "bp_marketplace_overview_card"` returns data (not 404 or empty) in DEV.
4. `POST /report/getGridCardData` with `componentId: "bp_marketplace_overview_table"` returns data in DEV.
5. Config is deployed and verified in QA.
6. Frontend integration testing is unblocked.

## Definition of Done Checklist

- [ ] `query_id` values confirmed with Engineering Lead (prerequisite — may require data team input)
- [ ] DML scripts written and reviewed
- [ ] Executed in DEV — `getCardData` / `getGridCardData` returns data
- [ ] Executed in QA — verified
- [ ] Executed in PROD
- [ ] EPIC-001 integration testing unblocked (confirmed by frontend lead)

## Architecture References

- Section 4.1 — Decision to reuse `getCardData`/`getGridCardData` with BP-specific `query_id`
- Section 8.1 — API request payloads showing `componentId` usage
- Section 16, Open Item #2 — GO/NO-GO gate description
