# Epic: EPIC-02 — Sales Insights API — Multi-Region Aggregation Service

**Epic ID:** GA-SI-EPIC-02  
**Priority:** P0 — Critical  
**Target Release:** Q2 2026 (Week 5 — Beta)  
**Status:** Draft  
**Epic Type:** Backend / Full-Stack  
**Depends on:** EPIC-01 (FX rates must be available)

---

## Business Value (Charlie-Conductor)

This epic delivers the core computation engine that transforms raw regional sales data into unified, multi-currency aggregated KPIs. It enables the dashboard to show consistent, accurate EMEA revenue figures regardless of which currencies the regional marketplaces natively report in.

**Business Outcome:** Eliminates 100% of manual Excel merging; provides a Single Source of Truth for EMEA sales with <200ms P95 query latency.

---

## Two-Agent Analysis

- **Strategic (Charlie-Conductor):** Central capability — blocks EPIC-03 (Dashboard). Establishes the data contract that all consumers (frontend, future export jobs) depend on. Design the API contract carefully to avoid breaking changes.
- **Technical (Bob-Builder):** New microservice `sales-insights-api` using Java 17 / Spring Boot 3.1.x (same stack as `i2o-scheduler`). Key complexity: LY 364-day offset calculation and multi-currency FX conversion formula. Materialized view is the primary performance lever.

---

## Success Metrics

- Aggregation API P95 latency < 200ms for a 5-region, 1-year date range query
- All FX conversions produce results matching manual calculation (±0.01%)
- LY metrics use 364-day (52-week) offset — verified by data validation tests
- `mv_daily_aggregates` refresh completes in < 5 minutes nightly
- CSV export endpoint streams 100k rows without timeout

---

## Technical Foundation (Bob-Builder)

- **New Repository:** `i2o-retail/sales-insights-api` (Spring Boot 3.1.7, Java 17, Maven)
- **DB tables:** `sales_data`, `mv_daily_aggregates` (materialized view)
- **Ingestion:** `CsvIngestionTask` in `i2o-scheduler` reads GCS CSVs and bulk-inserts into `sales_data`
- **API style:** REST (OpenAPI 3.0 documented)
- **Auth:** Spring Security + JWT (Keycloak realm, existing `i2o` realm)
- **DB migration:** Flyway scripts V2 (`sales_data`) + V3 (`mv_daily_aggregates`)

**FX Conversion Formula:**
```
converted = local_value
    ÷ fx_rates.rate_to_eur(local_currency)   -- normalize to EUR
    × fx_rates.rate_to_eur(target_currency)⁻¹ -- convert to target
```

**LY Offset:** `date - INTERVAL '364 days'` (52 × 7 = same weekday alignment).

---

## Architecture Components

From `architecture.md` (Sections 4, 5.1, 5.2, 8.4, 8.5):

**DB Schemas:**
```sql
-- sales_data
CREATE TABLE sales_data (
  id              BIGSERIAL PRIMARY KEY,
  date            DATE        NOT NULL,
  region          VARCHAR(5)  NOT NULL,  -- DE, FR, IT, ES, UK
  sku             VARCHAR(50) NOT NULL,
  product_name    VARCHAR(255),
  local_revenue   DECIMAL(18,2) NOT NULL,
  units           INTEGER     NOT NULL,
  currency_code   VARCHAR(3)  NOT NULL,
  ingestion_date  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX ON sales_data (date, region, sku);

-- mv_daily_aggregates (materialized view)
CREATE MATERIALIZED VIEW mv_daily_aggregates AS
  SELECT date, region, currency_code,
         SUM(local_revenue) AS total_revenue,
         SUM(units) AS total_units,
         COUNT(DISTINCT sku) AS sku_count
  FROM sales_data
  GROUP BY date, region, currency_code
WITH DATA;
CREATE UNIQUE INDEX ON mv_daily_aggregates (date, region, currency_code);
```

**REST API Endpoints:**
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/sales-insights/aggregate` | Multi-region aggregated KPIs + chart data |
| GET | `/api/v1/sales-insights/currencies` | Supported currencies list |
| GET | `/api/v1/sales-insights/stale-status` | Staleness per region |
| GET | `/api/v1/sales-insights/export` | Streamed CSV download |

**Project Structure:**
```
sales-insights-api/src/main/java/com/corecompete/i2o/salesinsights/
├── config/        # Spring Security JWT, CORS, Swagger
├── controller/    # SalesInsightsController
├── dto/           # SalesQueryRequest, SalesAggregationResponse, KpiSummaryResponse, FxRateResponse
├── model/         # SalesData (JPA entity), FxRate (JPA entity)
├── repository/    # SalesDataRepository, FxRatesRepository (Spring Data JPA)
├── service/       # AggregationService, FxConversionService
└── exception/     # GlobalExceptionHandler (RFC 7807 Problem Detail)
```

---

## Dependencies

- **Blocks:** EPIC-03 (Dashboard cannot function without this API)
- **Depends on:** EPIC-01 — `fx_rates` table must be populated
- **External:** GCS bucket `marketplace-csvs` must receive regional CSV drops from upstream pipelines
- **Technical (Bob):** Cloud Run deployment config; Cloud SQL socket factory setup in `sales-insights-api`
- **Coordination (Charlie):** Finalize API contract with frontend team before EPIC-03 story development begins (Week 4)

---

## Implementation Readiness

- **Ready:** Java 17 / Spring Boot 3.1.x stack proven in `i2o-scheduler`; Cloud SQL socket factory pattern established
- **POC Needed:** Validate materialized view refresh time against realistic dataset size (estimate: 500k rows; 5 regions × 2 years daily data)

---

## Stories Breakdown

- [ ] **GA-SI-02-S01** — New `sales-insights-api` Project Bootstrap & Cloud SQL Config — 1 day
- [ ] **GA-SI-02-S02** — DB Migration: `sales_data` Table + Indexes — 0.5 day
- [ ] **GA-SI-02-S03** — DB Migration: `mv_daily_aggregates` Materialized View — 0.5 day
- [ ] **GA-SI-02-S04** — `CsvIngestionTask` in `i2o-scheduler` (GCS read + bulk insert) — 2 days
- [ ] **GA-SI-02-S05** — `FxConversionService` Implementation & Unit Tests — 1 day
- [ ] **GA-SI-02-S06** — `AggregationService` with LY 364-day offset logic — 1.5 days
- [ ] **GA-SI-02-S07** — REST API Controller, DTOs, Keycloak JWT Filter & OpenAPI docs — 1.5 days
- [ ] **GA-SI-02-S08** — CSV Export Endpoint (streaming response) — 1 day

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial epic generation from architecture | AI Agent |
