---
epic_key: GA-SI-001
project: sales_insights
labels: [architecture, backend, ingestion]
components: [i2o-scheduler, Cloud SQL]
---

# Epic: Alpha (Core Pipeline) - Ingestion & FX Storage

## Business Value (Charlie-Conductor)
To deliver the foundational data model for the Unified EMEA Sales Dashboard, this Epic establishes the continuous ingestion plumbing. It automatically processes daily European Central Bank (ECB) FX rates and regional sales CSVs. By completing this, we eliminate the need for regional managers to lookup historical FX metrics and standardize the raw data format required for cross-region analytics.

## Technical Execution & Bounds (Bob-Builder)
- **Domain:** `i2o-scheduler` and `Cloud SQL`.
- **Stack:** Java 17, Spring Boot 3.x, PostgreSQL (Cloud SQL), TimescaleDB, Flyway.
- **Constraints:** Must use existing infrastructure; extending `i2o-scheduler` avoids spinning up net-new Cloud Run instances for CRON tasks. TimescaleDB is needed for `fx_rates` hypertable partitioning.
- **Dependencies:** Platform team must prepare GCS extractor pipeline dropping CSVs daily. Keycloak validation logic ported implicitly if expanding to API layers.
- **Risks:** ECB XML schema drift. Migration conflicts on `i2o-admin-db`. TimescaleDB extension compatibility.

## Included Stories
- **GA-SI-001-S01**: Database Schema & Flyway Migrations (fx_rates, sales_data, mv_daily_aggregates)
- **GA-SI-001-S02**: EcbIngestionTask & Historical Bootstrap
- **GA-SI-001-S03**: CsvIngestionTask & GCS Integration

## Go-Live Readiness
- Go-Live Gate: Zero missing days in `fx_rates`.
- Localized 12-month backfill tested in QA/UAT environments.
