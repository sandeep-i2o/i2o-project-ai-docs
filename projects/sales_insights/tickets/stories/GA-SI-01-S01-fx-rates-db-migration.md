# Story GA-SI-01-S01: DB Migration — `fx_rates` TimescaleDB Hypertable

**Epic:** GA-SI-EPIC-01 — Automated ECB FX Rate Ingestion Pipeline  
**Story ID:** GA-SI-01-S01  
**Priority:** P0  
**Estimate:** 0.5 day  
**Status:** Draft

---

## Story

**As a** system,  
**I want** a `fx_rates` database table created as a TimescaleDB hypertable in the Cloud SQL PostgreSQL instance,  
**so that** the ECB ingestion task has a performant, time-partitioned store for historical exchange rate data.

---

## Acceptance Criteria

1. Flyway migration script `V1__fx_rates.sql` is created in `sales-insights-api/src/main/resources/db/migration/`
2. `fx_rates` table has columns: `date DATE`, `currency_code VARCHAR(3)`, `rate_to_eur DECIMAL(18,6)`, `ingested_at TIMESTAMPTZ`, `is_fallback BOOLEAN`
3. Primary key is composite `(date, currency_code)` — enforces uniqueness (UPSERT safety)
4. TimescaleDB hypertable created via `SELECT create_hypertable('fx_rates', 'date')`
5. Compound index `CREATE INDEX ON fx_rates (date DESC, currency_code)` is present
6. Migration runs successfully on `dev` Cloud SQL instance without errors
7. Flyway version table records successful migration

---

## Tasks / Subtasks

- [ ] Create Flyway migration script (AC: 1, 2, 3, 4, 5)
  - [ ] `V1__fx_rates.sql` — CREATE TABLE with correct types and constraints
  - [ ] Add TimescaleDB `create_hypertable` call
  - [ ] Add compound index
- [ ] Verify TimescaleDB extension is enabled on target Cloud SQL instance (AC: 6)
  - [ ] Run `SELECT * FROM pg_extension WHERE extname = 'timescaledb';` to confirm
  - [ ] If not enabled: coordinate with infra team to enable extension
- [ ] Run `./mvnw flyway:migrate` against `dev` profile and confirm success (AC: 6, 7)
- [ ] Write integration test confirming table exists and hypertable metadata is correct (AC: 4)

---

## Dev Notes

**Target Repository:** `i2o-retail/sales-insights-api` (new project — see Story GA-SI-02-S01 for project bootstrap)

**Migration file path:**
```
sales-insights-api/
└── src/main/resources/db/migration/
    └── V1__fx_rates.sql
```

**Full SQL for V1__fx_rates.sql:**
```sql
-- V1: Create fx_rates hypertable for ECB exchange rate storage
CREATE TABLE IF NOT EXISTS fx_rates (
    date          DATE            NOT NULL,
    currency_code VARCHAR(3)      NOT NULL,
    rate_to_eur   DECIMAL(18, 6)  NOT NULL,
    ingested_at   TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
    is_fallback   BOOLEAN         NOT NULL DEFAULT FALSE,
    CONSTRAINT pk_fx_rates PRIMARY KEY (date, currency_code)
);

-- Convert to TimescaleDB hypertable (partitioned monthly by date)
SELECT create_hypertable('fx_rates', 'date',
    chunk_time_interval => INTERVAL '1 month',
    if_not_exists => TRUE
);

-- Performance index for date-range + currency lookups
CREATE INDEX IF NOT EXISTS idx_fx_rates_date_currency
    ON fx_rates (date DESC, currency_code);
```

**Flyway config** (in `application-{env}.properties`):
```properties
spring.flyway.enabled=true
spring.flyway.locations=classpath:db/migration
spring.flyway.baseline-on-migrate=true
```

**TimescaleDB note:** Cloud SQL PostgreSQL 14+ supports the TimescaleDB extension. Confirm with `SHOW server_version;` and `SELECT * FROM pg_available_extensions WHERE name = 'timescaledb';` before running migration.

### Testing

- **Location:** `sales-insights-api/src/test/java/.../migration/FxRatesMigrationTest.java`
- **Framework:** Spring Boot Test + Testcontainers (PostgreSQL + TimescaleDB image)
- **Pattern:** `@SpringBootTest` + `@Testcontainers` with `TimescaleDBContainer`
- **Test:** Assert `fx_rates` table exists, primary key constraint tested via duplicate insert (expect constraint violation), hypertable metadata confirmed via `SELECT * FROM timescaledb_information.hypertables`

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial story generation | AI Agent |

---

## Dev Agent Record

*(Populated during implementation)*

### Agent Model Used
_TBD_

### Debug Log References
_None yet_

### Completion Notes List
_None yet_

### File List
_None yet_

---

## QA Results

*(Populated by QA Agent)*
