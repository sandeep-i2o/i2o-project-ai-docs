---
id: EPIC-003
title: "[MO] Scheduler — Weekly KPI Aggregation Task"
project: marketplace_overview
release: release_8
module: i2o-scheduler
type: Epic
priority: High
status: Draft
created: 2026-03-04
stories:
  - STORY-009
  - STORY-010
---

# EPIC-003 — Scheduler: Weekly KPI Aggregation Task

## Business Value (Charlie-Conductor)

Weekly KPI data delivery is the heartbeat of the Marketplace Overview feature. The `MarketplaceOverviewWeeklyAggregationTask` runs every Monday at 06:00 UTC, reads from five BigQuery source tables in `CC_I2O_DATA_MART`, and writes a consolidated snapshot into the PostgreSQL `marketplace_kpi_weekly_snapshot` table. Without this, the dashboard has no data. The weekly refresh pattern aligns with the existing scheduler architecture, eliminating the need for any new infrastructure.

## Technical Feasibility (Bob-Builder)

- **Stack:** Spring Boot 3.x task within `i2o-scheduler`, BigQuery Java client, existing cron framework.
- **Data sources:** Five confirmed BQ tables from `query_described.csv` — `viz_lost_sales`, `reseller_progress_by_week`, `listings_progress_by_week`, `viz_reseller_filtered_detail`, `bp_wbr_detail`.
- **Sink:** New PostgreSQL table `marketplace_kpi_weekly_snapshot` (indexed by `org_id, week_start, marketplace, brand_id`).
- **Retry policy:** 3 retries with 30-minute backoff; failure → PagerDuty alert via audit log monitoring.
- **Effort estimate:** Medium (1–2 sprints for all stories).
- **Risk:** Open Item #5 (eBay/Target BQ data availability for trial KPIs) and Open Item #6 (`bp_wbr_detail` column name confirmation) are 🟡 Medium risks.

## Scope

This epic covers all changes inside `i2o-scheduler`:

| Area | Deliverable |
|------|-------------|
| PostgreSQL sink DDL | `CREATE TABLE marketplace_kpi_weekly_snapshot` (org_id, week_start, marketplace, brand_id, region, 13 KPI cols) |
| Audit log DDL | `CREATE TABLE marketplace_scheduler_audit_log` in PostgreSQL |
| Aggregation task | `MarketplaceOverviewWeeklyAggregationTask.java` — reads 5 source tables, writes snapshot |
| Cron configuration | `scheduler.marketplace-overview.cron=0 6 * * MON` in `application-{env}.properties` |
| Staleness flag | Set `data_staleness_flag=true` when aggregation fails; reset on success |
| Manual trigger | Support `weekStart` override via `/admin/scheduler/run?task=...&weekStart=...` for backfill |
| Unit tests | JUnit 5 + Mockito ≥ 70% task coverage |
| Operational runbook | Section 17 of architecture doc: detection, escalation, backfill, verification steps |

## Dependencies

- PostgreSQL schema must be created in DEV before task testing.
- Open Item #5: eBay/Target BQ data for trial KPIs (Listings, Resellers, WoW) — needed for trial marketplace KPIs.
- Open Item #6: `bp_wbr_detail` column name confirmation — needed for Enforcement Centre KPIs.
- `i2o-master-data` `org_market_mapping` — used to determine which org/marketplace combos to aggregate.

## Story Breakdown

| Story | Title |
|-------|-------|
| STORY-009 | PostgreSQL schema setup — sink table + audit log DDL |
| STORY-010 | `MarketplaceOverviewWeeklyAggregationTask` — aggregation logic + cron + retry + audit |

## Acceptance Criteria (Epic-level)

1. `marketplace_kpi_weekly_snapshot` table is created in PostgreSQL with correct schema (`org_id` NOT NULL and indexed).
2. Task runs on Monday 06:00 UTC cron and writes all 13 KPI columns per `(org_id, marketplace, brand_id, region, week_start)`.
3. On failure, task retries up to 3 times (30-minute backoff) then writes `status='FAILED'` to audit log and triggers PagerDuty alert.
4. `data_staleness_flag` is set to `true` on failure and reset to `false` on successful next run.
5. Backfill can be triggered via `/admin/scheduler/run?task=MarketplaceOverviewWeeklyAggregationTask&weekStart={date}`.
6. Unit tests pass with ≥ 70% task coverage.

## Architecture References

- Section 5.3 — Scheduler new weekly task structure
- Section 6.3 — Weekly KPI aggregation runtime view
- Section 7.2 — BigQuery sink table schema
- Section 18 — KPI mapping appendix (aggregation formulas per KPI)
- Section 17 — Operational runbook (scheduler failure handling)
