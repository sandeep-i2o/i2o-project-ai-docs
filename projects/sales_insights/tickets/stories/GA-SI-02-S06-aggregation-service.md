# Story GA-SI-02-S06: `AggregationService` — Multi-Region KPIs with LY Offset Logic

**Epic:** GA-SI-EPIC-02 — Sales Insights API — Multi-Region Aggregation Service  
**Story ID:** GA-SI-02-S06  
**Priority:** P0  
**Estimate:** 1.5 days  
**Status:** Draft

---

## Story

**As a** Regional Sales Manager,  
**I want** the API to aggregate sales data across multiple EMEA regions for a selected time period and convert totals to my chosen currency,  
**so that** I can compare multi-region performance without manual calculation.

---

## Acceptance Criteria

1. `AggregationService.aggregate(SalesQueryRequest request)` returns `SalesAggregationResponse` with KPI totals and time-series chart data
2. Request supports: `regions` (list), `currency` (3-letter ISO), `granularity` (DAILY/WEEKLY/MONTHLY/QUARTERLY), `startDate`, `endDate`
3. **Ordered Revenue** = `SUM(local_revenue × fx_conversion_factor)` per region per period — using `FxConversionService`
4. **ASP** = Total Ordered Revenue ÷ Total Units (computed in-memory, not in DB)
5. **LY Revenue** = Revenue from same period exactly 364 days (52 weeks) prior — `startDate - 364`, `endDate - 364`
6. If a region has no data for the selected period, it returns `0` values (not an error)
7. If the data for a region is stale (last `ingestion_date` > 24h ago), the response marks that region with `"stale": true`
8. Aggregation queries hit `mv_daily_aggregates` materialized view (not raw `sales_data`) for the main query
9. Integration test: a mix of DE (EUR) and UK (GBP) data → verify EUR total matches expected after conversion

---

## Tasks / Subtasks

- [ ] Create `SalesQueryRequest.java` DTO (AC: 2)
  - [ ] Fields: `List<String> regions`, `String currency`, `Granularity granularity` (enum), `LocalDate startDate`, `LocalDate endDate`
  - [ ] Bean validation: `@NotEmpty regions`, `@NotNull currency`, valid date range
- [ ] Create `SalesAggregationResponse.java` DTO (AC: 1, 3, 4, 5)
  - [ ] Fields: `List<KpiSummary> kpis`, `List<ChartDataPoint> chartData`, `List<GridRow> tableData`, `Map<String, Boolean> staleRegions`
- [ ] Implement `AggregationService.aggregate()` (AC: 1–8)
  - [ ] Query `mv_daily_aggregates` for current period (per region, per day)
  - [ ] Apply `FxConversionService.convert()` for each region's local currency → target currency
  - [ ] Group by `granularity` (DAILY: as-is; WEEKLY: ISO week; MONTHLY: YYYY-MM; QUARTERLY: Q1-Q4)
  - [ ] Calculate ASP in-memory: `totalRevenue / totalUnits`
  - [ ] LY query: same query with `startDate - 364` and `endDate - 364`
  - [ ] Stale detection: `SELECT MAX(ingestion_date) FROM sales_data WHERE region = :r` → compare to `NOW() - 24h`
- [ ] Add `MvDailyAggregatesRepository` (Spring Data JPA or `@Query`) (AC: 8)
  - [ ] Query: `SELECT date, region, currency_code, SUM(total_revenue), SUM(total_units) FROM mv_daily_aggregates WHERE region IN :regions AND date BETWEEN :start AND :end GROUP BY date, region, currency_code`
- [ ] Write integration test with test data (AC: 9)

---

## Dev Notes

**Repository:** `i2o-retail/sales-insights-api`  
**Prerequisite stories:** GA-SI-02-S01 (bootstrap), GA-SI-02-S03 (mv_daily_aggregates), GA-SI-02-S05 (FxConversionService)

**Granularity grouping logic (Java):**
```java
// WEEKLY: ISO week key = year + "W" + weekOfYear
// MONTHLY: YYYY-MM
// QUARTERLY: YYYY-Q + quarter
String periodKey = switch (granularity) {
    case DAILY -> date.toString();
    case WEEKLY -> date.getYear() + "W" + date.get(IsoFields.WEEK_OF_WEEK_BASED_YEAR);
    case MONTHLY -> date.format(DateTimeFormatter.ofPattern("yyyy-MM"));
    case QUARTERLY -> date.getYear() + "-Q" + ((date.getMonthValue() - 1) / 3 + 1);
};
```

**LY offset (from architecture.md ADR-006):**
```java
// 364 days = exactly 52 weeks → same weekday alignment
LocalDate lyStart = request.getStartDate().minusDays(364);
LocalDate lyEnd = request.getEndDate().minusDays(364);
```

**Region stale check query:**
```java
@Query("SELECT MAX(s.ingestionDate) FROM SalesData s WHERE s.region = :region")
Optional<Instant> findLatestIngestionDate(@Param("region") String region);
```

**Response structure:**
```java
public class SalesAggregationResponse {
    private KpiSummary totals;              // Grand total across all selected regions
    private List<RegionKpi> byRegion;       // Per-region breakdown
    private List<ChartDataPoint> chartData; // [{period, region, revenue}] for trend chart
    private List<GridRow> tableData;        // [{sku, productName, region, revenue, units, asp}]
    private Map<String, Boolean> staleRegions; // {"UK": true, "DE": false}
    private String displayCurrency;
    private String fxRatesDate;
    private boolean isFallback;
}
```

### Testing

- **Location:** `src/test/java/.../service/AggregationServiceIntegrationTest.java`
- **Framework:** `@SpringBootTest` + Testcontainers PostgreSQL
- **Test data:** Insert 30 days of DE (EUR) and UK (GBP) test rows into `sales_data`; run `REFRESH MATERIALIZED VIEW`; then call `aggregate()` and assert EUR total
- **LY test:** Insert same data at `date - 364`; verify LY fields populated correctly

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
