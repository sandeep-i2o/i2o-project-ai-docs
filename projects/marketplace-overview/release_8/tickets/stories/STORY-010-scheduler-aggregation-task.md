---
id: STORY-010
title: "[MO] Scheduler: MarketplaceOverviewWeeklyAggregationTask Implementation"
project: marketplace_overview
release: release_8
module: i2o-scheduler
type: Story
priority: High
epic: EPIC-003
status: Draft
estimate: 3 days
created: 2026-03-04
depends_on:
  - STORY-009
---

# STORY-010 — Scheduler: WeeklyAggregationTask Implementation

## Context

This story implements `MarketplaceOverviewWeeklyAggregationTask` in `i2o-scheduler`. The task runs every Monday at 06:00 UTC, reads from five confirmed BQ source tables in `CC_I2O_DATA_MART`, aggregates KPIs per `(org_id, marketplace, brand_id, region, week_start)`, and writes to the PostgreSQL `marketplace_kpi_weekly_snapshot` table. The task includes retry logic (3 retries, 30-min backoff), audit logging in PostgreSQL, and staleness flag management.

## Module: `i2o-scheduler`

### Files to Create

```
com.corecompete.i2o.scheduler.task/
└── MarketplaceOverviewWeeklyAggregationTask.java
```

### Key Aggregation Logic (per architecture Section 18 — KPI Mapping Appendix)

| KPI | Source Table | Formula |
|-----|-------------|---------|
| `lost_sales` | `viz_lost_sales` | `SUM(lost_sales)` WHERE `reporting_range='weekly'` |
| `total_closed_listings` | `listings_progress_by_week` | `SUM(List_Count_Closed)` |
| `reseller_removed` | `reseller_progress_by_week` | `SUM(closed_reseller_count)` |
| `buybox_win_pct` | `reseller_progress_by_week` | `SUM(buy_box_winning_reseller_count_closed) / NULLIF(SUM(closed_reseller_count), 0) * 100` |
| `total_brand_violation` | `viz_reseller_filtered_detail` | `COUNT(DISTINCT reseller_id)` where BV applies; NULL for Walmart |
| `violations_closed` | `viz_reseller_filtered_detail` | `COUNT(DISTINCT reseller_id)` where `enforcement_status='CLOSED'`; NULL for Walmart |
| `notification_in_queue` | `bp_wbr_detail` | `SUM(queue)` |
| `cnd_pending` | `bp_wbr_detail` | `SUM(cnd_pending)` |
| `total_cnd_sent` | `bp_wbr_detail` | `SUM(total_cnd_sent)` |
| `test_purchase` | `bp_wbr_detail` | `SUM(test_purchase)` |
| `no_of_listings` | `viz_lost_sales` | `COUNT(DISTINCT listing_id)` — trial marketplaces only |
| `no_of_resellers` | `reseller_progress_by_week` | `COUNT(DISTINCT reseller_id)` — trial marketplaces only |
| `wow_change_pct` | `marketplace_kpi_weekly_snapshot` (self-join in PostgreSQL) | `(current.lost_sales - prev.lost_sales) / NULLIF(prev.lost_sales, 0) * 100` |

### Task Lifecycle

1. Log task start to PostgreSQL `marketplace_scheduler_audit_log` (`status='RETRYING'`).
2. Execute BQ aggregation queries for each source table.
3. Merge results into the PostgreSQL `marketplace_kpi_weekly_snapshot` (UPSERT by `(org_id, week_start, marketplace, brand_id, region)` unique constraint).
4. Set `data_staleness_flag = FALSE` for rows written this run.
5. Update audit log `status='SUCCESS'`, `completed_at`.

**On failure:**
- Retry up to 3 times with 30-minute backoff.
- After 3 failures: update audit log `status='FAILED'`, `error_message`, trigger PagerDuty alert.
- Set `data_staleness_flag = TRUE` for the failed week's rows.

**Cron configuration (in `application-{env}.properties`):**
```properties
scheduler.marketplace-overview.cron=0 6 * * MON
```

**Manual trigger support:**
- `POST /admin/scheduler/run?task=MarketplaceOverviewWeeklyAggregationTask`
- `POST /admin/scheduler/run?task=MarketplaceOverviewWeeklyAggregationTask&weekStart=2026-02-24` (backfill)

### `org_id` Handling

- The task must iterate over all active org/marketplace combinations from `org_market_mapping`.
- Each PostgreSQL INSERT row must include the correct `org_id`.
- All BigQuery SELECT queries must be scoped with `WHERE org_id = ?` for the current org.

## Acceptance Criteria

1. Task is registered with cron `0 6 * * MON` and runs at Monday 06:00 UTC.
2. Task reads from all 5 BQ source tables using the formulas in Section 18.
3. Task writes aggregated rows to the PostgreSQL `marketplace_kpi_weekly_snapshot` with correct `org_id` per tenant.
4. `data_staleness_flag = FALSE` is set on successful writes.
5. On failure: retry 3× with 30-minute backoff; after all retries, sets `status='FAILED'` in audit log and triggers PagerDuty alert.
6. `data_staleness_flag = TRUE` is set for rows where aggregation failed.
7. Manual trigger via `/admin/scheduler/run?task=...` works, with optional `weekStart` override for backfill.
8. JUnit 5 unit tests cover task logic, retry, and audit logging (≥ 70% task coverage).

## Definition of Done Checklist

- [ ] `MarketplaceOverviewWeeklyAggregationTask` class created
- [ ] Cron expression configured in properties file
- [ ] All 13 KPI aggregation queries implemented per Section 18 formulas
- [ ] `org_id` correctly scoped in all BQ operations
- [ ] Retry logic (3×, 30-min backoff) implemented
- [ ] Audit log write on start, retry, success, and failure
- [ ] Staleness flag managed on success and failure
- [ ] Manual trigger + weekStart backfill supported
- [ ] Unit tests written (≥ 70% coverage)
- [ ] JavaDocs added to all public methods

## Architecture References

- Section 5.3 — Scheduler task structure
- Section 6.3 — Weekly aggregation runtime view
- Section 7.2 — Sink table schema
- Section 10.2 — Scheduler failure and staleness handling
- Section 17 — Operational runbook (detection, escalation, backfill, verification)
- Section 18 — KPI mapping appendix (all aggregation formulas)
