# Story GA-SI-03-S02: `SalesInsightsApiService` & `SalesInsightsStateService` (Angular RxJS)

**Epic:** GA-SI-EPIC-03 — EMEA Sales Command Center Dashboard (Angular UI)  
**Story ID:** GA-SI-03-S02  
**Priority:** P0  
**Estimate:** 1 day  
**Status:** Draft

---

## Story

**As a** developer working on the Sales Insights Angular module,  
**I want** a typed API service and a RxJS-based state service,  
**so that** all dashboard components share a consistent data layer with centralized loading/error states and automatic request cancellation on filter change.

---

## Acceptance Criteria

1. `SalesInsightsApiService` has methods for all 4 API endpoints: `getAggregatedData()`, `getSupportedCurrencies()`, `getStaleStatus()`, `exportCsv()`
2. `SalesInsightsApiService` uses `HttpClient` (Angular) following the `RestApiService` pattern already in `src/app/services/rest-api.service.ts`
3. Auth token is auto-attached to all requests via existing `KeycloakBearerInterceptor` — no manual token handling needed
4. `SalesInsightsStateService` exposes: `filters$: BehaviorSubject<SalesQuery>`, `aggregatedData$: Observable<SalesAggregationResponse>`, `loading$: BehaviorSubject<boolean>`, `error$: BehaviorSubject<string | null>`
5. State service uses `switchMap` to auto-cancel previous in-flight API calls when filters change
6. `filters$` changes are debounced 300ms via `debounceTime(300)` before triggering API call
7. `SalesInsightsApiService` is provided in `SalesInsightsModule` (not root)
8. TypeScript interfaces defined in `models/sales-insights.model.ts` matching backend DTO structure
9. Unit tests: verify `switchMap` cancellation (spy confirms only 1 API call resolves), verify loading state transitions

---

## Tasks / Subtasks

- [ ] Create `models/sales-insights.model.ts` with TypeScript interfaces (AC: 8)
  - [ ] `SalesQuery`, `SalesAggregationResponse`, `KpiSummary`, `ChartDataPoint`, `GridRow`
  - [ ] `Granularity` enum: `DAILY | WEEKLY | MONTHLY | QUARTERLY`
- [ ] Create `SalesInsightsApiService` (AC: 1, 2, 3, 7)
  - [ ] `getAggregatedData(query: SalesQuery): Observable<SalesAggregationResponse>`
    - `GET /api/v1/sales-insights/aggregate` with HttpParams
  - [ ] `getSupportedCurrencies(): Observable<string[]>`
    - `GET /api/v1/sales-insights/currencies`
  - [ ] `getStaleStatus(): Observable<Record<string, boolean>>`
    - `GET /api/v1/sales-insights/stale-status`
  - [ ] `exportCsv(query: SalesQuery): void`
    - `GET /api/v1/sales-insights/export` with `responseType: 'blob'`; trigger browser download
- [ ] Create `SalesInsightsStateService` (AC: 4, 5, 6)
  - [ ] `filters$ = new BehaviorSubject<SalesQuery>(defaultFilters)`
  - [ ] `aggregatedData$ = this.filters$.pipe(debounceTime(300), switchMap(q => this.apiService.getAggregatedData(q)), tap(...loading states...))`
  - [ ] `updateFilters(partial: Partial<SalesQuery>)` method
- [ ] Register both services in `sales-insights.module.ts` providers (AC: 7)
- [ ] Unit tests using `HttpClientTestingModule` (AC: 9)

---

## Dev Notes

**Repository:** `i2o-retail/frontendapplication-i2oretail`  
**Path:** `src/app/modules/sales-insights/services/`  
**Prerequisite story:** GA-SI-03-S01 (module scaffold must exist)

**Pattern reference:** Look at `src/app/services/rest-api.service.ts` for how HTTP calls are structured in this app. Mirror the same HTTP client injection pattern.

**API base URL** from environment: `environment.apiBaseUrl + '/api/v1/sales-insights'`

**TypeScript models:**
```typescript
// models/sales-insights.model.ts
export type Granularity = 'DAILY' | 'WEEKLY' | 'MONTHLY' | 'QUARTERLY';

export interface SalesQuery {
  regions: string[];       // e.g. ['DE', 'FR']
  currency: string;        // e.g. 'EUR'
  granularity: Granularity;
  startDate: string;       // ISO date string YYYY-MM-DD
  endDate: string;
}

export interface KpiSummary {
  orderedRevenue: number;
  orderedUnits: number;
  asp: number;
  lyRevenue: number;
  lyRevenueDelta: number;  // percentage change
  displayCurrency: string;
}

export interface ChartDataPoint {
  period: string;    // e.g. '2026-W08'
  region: string;
  revenue: number;
}

export interface GridRow {
  sku: string;
  productName: string;
  region: string;
  localRevenue: number;
  convertedRevenue: number;
  units: number;
  asp: number;
}

export interface SalesAggregationResponse {
  totals: KpiSummary;
  byRegion: Array<{ region: string; kpi: KpiSummary }>;
  chartData: ChartDataPoint[];
  tableData: GridRow[];
  staleRegions: Record<string, boolean>;
  displayCurrency: string;
  fxRatesDate: string;
  isFallback: boolean;
}
```

**State service RxJS pattern:**
```typescript
// Key pattern for 300ms debounce + auto-cancel on filter change
aggregatedData$ = this.filters$.pipe(
  debounceTime(300),
  tap(() => { this.loading$.next(true); this.error$.next(null); }),
  switchMap(query => this.apiService.getAggregatedData(query).pipe(
    catchError(err => {
      this.error$.next(err.message);
      return EMPTY;
    })
  )),
  tap(() => this.loading$.next(false))
);
```

**CSV download trigger:**
```typescript
exportCsv(query: SalesQuery): void {
  this.http.get('/api/v1/sales-insights/export', {
    params: this.toHttpParams(query), responseType: 'blob'
  }).subscribe(blob => {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'sales-export.csv'; a.click();
    URL.revokeObjectURL(url);
  });
}
```

### Testing

- **Location:** `src/app/modules/sales-insights/services/sales-insights-api.service.spec.ts`
- **Framework:** Jasmine/Karma (existing in `frontendapplication-i2oretail`)
- **Mock:** `HttpClientTestingModule` + `HttpTestingController`
- **Key test:** Verify `switchMap` cancellation — emit two filter values rapidly; confirm only one HTTP GET resolves

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
