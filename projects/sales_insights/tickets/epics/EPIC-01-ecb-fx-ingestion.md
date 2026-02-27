# Epic: EPIC-01 — Automated ECB FX Rate Ingestion Pipeline

**Epic ID:** GA-SI-EPIC-01  
**Priority:** P0 — Critical  
**Target Release:** Q2 2026 (Week 3 — Alpha)  
**Status:** Draft  
**Epic Type:** Backend / Infrastructure

---

## Business Value (Charlie-Conductor)

Panasonic EMEA regional managers currently spend 4–6 hours per week manually looking up and applying exchange rates. This epic eliminates that entirely by establishing an **automated, trusted, and auditable FX rate data store** — the foundational layer that all multi-currency reporting depends on.

**Business Outcome:** 90% reduction in manual FX effort; single authoritative FX source for all EMEA sales calculations.

---

## Two-Agent Analysis

- **Strategic (Charlie-Conductor):** Foundational capability — without accurate FX rates, multi-currency reporting is impossible. Constitutes the highest-risk dependency for the entire Sales Insights release. Must be stable before any dashboard work begins.
- **Technical (Bob-Builder):** Feasible within 2 weeks. ECB XML feed is well-documented; the `i2o-scheduler` CRON infrastructure handles retry/alert patterns already. Risk: ECB XML schema changes; mitigated by schema validation on every fetch.

---

## Success Metrics

- ECB CRON runs successfully at 16:30 CET daily ≥ 99% of business days
- Fallback to last-known rate activates within 30s of ECB failure
- Zero duplicate `(date, currency_code)` rows in `fx_rates` table
- Admin alert email fires within 60s of 3rd retry failure

---

## Technical Foundation (Bob-Builder)

- **Repository:** `i2o-retail/i2o-scheduler` (extended)
- **New class:** `EcbIngestionTask` implementing the `RunnableTask` interface
- **Trigger:** Cloud Scheduler `POST /scheduler/execute {taskId: "ecb-fx-ingestion"}` @ 16:30 CET
- **DB table:** `fx_rates` (TimescaleDB hypertable on Cloud SQL PostgreSQL 14+)
- **Retry:** Exponential backoff ×3 (2s, 4s, 8s) via Spring Retry
- **Alert:** SendGrid via existing `EmailService`
- **DB migration:** Flyway script in `sales-insights-api/src/main/resources/db/migration/V1__fx_rates.sql`

---

## Architecture Components

From `architecture.md` (Section 5.3 — Level 3: EcbIngestionTask Detail):

```
EcbIngestionTask.execute():
  a. HTTP GET https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml (timeout 10s)
  b. Validate XML schema (content-type, root element, min currencies)
  c. Sanity-check: >20% rate change flags for review
  d. Parse currency/rate pairs
  e. UPSERT into fx_rates WHERE (date, currency_code) ON CONFLICT DO UPDATE
  f. Retry ×3 with exponential backoff on failure
  g. After 3 failures: SendGrid admin alert + write fallback flag
```

**DB Schema:**
```sql
CREATE TABLE fx_rates (
  date          DATE        NOT NULL,
  currency_code VARCHAR(3)  NOT NULL,
  rate_to_eur   DECIMAL(18,6) NOT NULL,
  ingested_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  is_fallback   BOOLEAN     DEFAULT FALSE,
  PRIMARY KEY (date, currency_code)
);
SELECT create_hypertable('fx_rates', 'date');
CREATE INDEX ON fx_rates (date DESC, currency_code);
```

---

## Dependencies

- **External:** ECB XML feed availability (`https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`)
- **Technical (Bob):** TimescaleDB extension enabled on Cloud SQL instance; `sales-insights-api` Flyway migration run
- **Coordination (Charlie):** Infrastructure team enables TimescaleDB; Cloud Scheduler CRON configured pointing to `i2o-scheduler`

---

## Implementation Readiness

- **Ready:** Spring Retry dependency in `i2o-scheduler`; SendGrid `EmailService` in place; Cloud Scheduler infrastructure exists
- **POC Needed:** Confirm TimescaleDB availability on shared Cloud SQL instance (low risk — supported from PG 14+)

---

## Stories Breakdown

- [ ] **GA-SI-01-S01** — DB Migration: `fx_rates` TimescaleDB Hypertable — 0.5 day
- [ ] **GA-SI-01-S02** — EcbIngestionTask Implementation (fetch, validate, UPSERT) — 1.5 days
- [ ] **GA-SI-01-S03** — Retry Logic & Admin Alert Integration — 1 day
- [ ] **GA-SI-01-S04** — Cloud Scheduler CRON Configuration & Smoke Test — 0.5 day

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial epic generation from architecture | AI Agent |
