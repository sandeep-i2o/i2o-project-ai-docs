---
id: STORY-009
title: "[MO] Scheduler: BigQuery Schema Setup — Sink Table & Audit Log DDL"
project: marketplace_overview
release: release_8
module: i2o-scheduler
type: Story
priority: High
epic: EPIC-003
status: Draft
estimate: 1 day
created: 2026-03-04
---

# STORY-009 — Scheduler: BigQuery Schema Setup

## Context

Before the weekly aggregation task (STORY-010) can run, the BigQuery sink table and audit log table must be created in all environments (DEV, QA, PROD). This story covers the DDL scripts and their execution. The `marketplace_kpi_weekly_snapshot` table is the destination for all weekly pre-aggregated KPI data. `org_id` is the mandatory first clustering column to enforce tenant isolation.

## Module: `i2o-scheduler`

### DDL: `marketplace_kpi_weekly_snapshot`

```sql
CREATE TABLE `{project}.CC_I2O_DATA_MART.marketplace_kpi_weekly_snapshot` (
  -- Tenant isolation key (all queries MUST filter by this column)
  org_id                STRING NOT NULL,
  week_start            DATE NOT NULL,
  week_end              DATE NOT NULL,
  marketplace           STRING NOT NULL,     -- AMAZON | WALMART | EBAY | TARGET
  brand_id              STRING NOT NULL,
  region                STRING NOT NULL,
  -- Analytics KPIs
  lost_sales            NUMERIC,
  total_closed_listings INT64,
  reseller_removed      INT64,
  buybox_win_pct        FLOAT64,
  -- Brand Violation KPIs (NULL for Walmart)
  total_brand_violation INT64,
  violations_closed     INT64,
  -- Enforcement Centre KPIs
  notification_in_queue INT64,
  cnd_pending           INT64,
  total_cnd_sent        INT64,
  test_purchase         INT64,
  -- Trial Marketplace KPIs (eBay, Target)
  no_of_listings        INT64,
  no_of_resellers       INT64,
  wow_change_pct        FLOAT64,
  -- Metadata
  data_staleness_flag   BOOL DEFAULT FALSE,
  created_at            TIMESTAMP,
  updated_at            TIMESTAMP
)
PARTITION BY week_start
CLUSTER BY org_id, marketplace, brand_id;
```

### DDL: `marketplace_scheduler_audit_log`

```sql
CREATE TABLE `{project}.CC_I2O_DATA_MART.marketplace_scheduler_audit_log` (
  job_id        STRING NOT NULL,
  org_id        STRING NOT NULL,
  week_start    DATE NOT NULL,
  status        STRING NOT NULL,   -- SUCCESS | FAILED | RETRYING
  attempt       INT64,
  error_message STRING,
  started_at    TIMESTAMP,
  completed_at  TIMESTAMP
);
```

### Deployment Checklist

- [ ] Execute DDL on DEV BigQuery project
- [ ] Verify table exists and schema matches above
- [ ] Execute DDL on QA BigQuery project
- [ ] Execute DDL on PROD BigQuery project

## Acceptance Criteria

1. `marketplace_kpi_weekly_snapshot` table exists in all target BQ environments with correct schema.
2. Table is partitioned by `week_start` and clustered by `(org_id, marketplace, brand_id)`.
3. `org_id` is `NOT NULL` (mandatory for tenant isolation).
4. `data_staleness_flag` defaults to `FALSE`.
5. `marketplace_scheduler_audit_log` table exists in all environments with correct schema.

## Definition of Done Checklist

- [ ] DDL scripts committed to repository (as migration scripts or documented in runbook)
- [ ] Tables created in DEV
- [ ] Tables created in QA
- [ ] Tables created in PROD
- [ ] Schema verified against architecture Section 7.2

## Architecture References

- Section 7.2 — `marketplace_kpi_weekly_snapshot` schema and tenant isolation rationale
- Section 17 — Scheduler audit log schema
