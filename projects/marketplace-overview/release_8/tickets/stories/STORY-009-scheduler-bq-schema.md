---
id: STORY-009
title: "[MO] Scheduler: PostgreSQL Schema Setup — Sink Table & Audit Log DDL"
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

# STORY-009 — Scheduler: PostgreSQL Schema Setup

## Context

Before the weekly aggregation task (STORY-010) can run, the PostgreSQL sink table and audit log table must be created in all environments (DEV, QA, PROD). This story covers the DDL scripts and their execution. The `marketplace_kpi_weekly_snapshot` table is the destination for all weekly pre-aggregated KPI data. `org_id` is the mandatory key column to enforce tenant isolation.

## Module: `i2o-scheduler`

### DDL: `marketplace_kpi_weekly_snapshot`

```sql
CREATE TABLE IF NOT EXISTS marketplace_kpi_weekly_snapshot (
  id                    BIGSERIAL PRIMARY KEY,
  -- Tenant isolation key (mandatory — all queries must filter by this column)
  org_id                BIGINT NOT NULL,
  week_start            DATE NOT NULL,
  week_end              DATE NOT NULL,
  marketplace           VARCHAR(32) NOT NULL,   -- AMAZON | WALMART | EBAY | TARGET
  brand                 VARCHAR(255) NOT NULL,
  region                VARCHAR(32) NOT NULL,   -- US | UK | DE | etc.
  -- Analytics KPIs
  lost_sales            NUMERIC(18,2),
  total_closed_listings BIGINT,
  reseller_removed      BIGINT,
  buybox_win_pct        NUMERIC(7,2),
  -- Brand Violation KPIs (nullable for Walmart)
  total_brand_violation BIGINT,
  violations_closed     BIGINT,
  -- Enforcement Centre KPIs
  notification_in_queue BIGINT,
  cnd_pending           BIGINT,
  total_cnd_sent        BIGINT,
  test_purchase         BIGINT,
  -- Trial Marketplace KPIs (eBay, Target)
  no_of_listings        BIGINT,
  no_of_resellers       BIGINT,
  wow_change_pct        NUMERIC(7,2),
  -- Metadata
  data_staleness_flag   BOOLEAN NOT NULL DEFAULT FALSE,
  created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  CONSTRAINT uq_marketplace_kpi_snapshot
    UNIQUE (org_id, week_start, marketplace, brand, region)
);

CREATE INDEX IF NOT EXISTS idx_marketplace_kpi_snapshot_lookup
  ON marketplace_kpi_weekly_snapshot (org_id, brand, region, week_start DESC);
```

### DDL: `marketplace_scheduler_audit_log`

```sql
```sql
CREATE TABLE IF NOT EXISTS marketplace_scheduler_audit_log (
  id            BIGSERIAL PRIMARY KEY,
  job_id        VARCHAR(64) NOT NULL,
  org_id        BIGINT NOT NULL,
  week_start    DATE NOT NULL,
  status        VARCHAR(32) NOT NULL,   -- SUCCESS | FAILED | RETRYING
  attempt       INTEGER,
  error_message TEXT,
  started_at    TIMESTAMPTZ DEFAULT NOW(),
  completed_at  TIMESTAMPTZ
);
```
```

### Deployment Checklist

- [ ] Execute DDL on DEV PostgreSQL instance
- [ ] Verify table exists and schema matches above
- [ ] Execute DDL on QA PostgreSQL instance
- [ ] Execute DDL on PROD PostgreSQL instance

## Acceptance Criteria

1. `marketplace_kpi_weekly_snapshot` table exists in all target PostgreSQL environments with correct schema.
2. Table has primary key and lookup index on `(org_id, brand, region, week_start)`.
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
