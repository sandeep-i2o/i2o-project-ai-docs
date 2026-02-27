# Story GA-SI-03-S05: `TrendChartComponent` — ECharts Multi-Line Regional Sales Chart

**Epic:** GA-SI-EPIC-03 — EMEA Sales Command Center Dashboard (Angular UI)  
**Story ID:** GA-SI-03-S05  
**Priority:** P0  
**Estimate:** 1.5 days  
**Status:** Draft

---

## Story

**As an** Executive VP,  
**I want** a multi-line trend chart showing revenue over time for each selected EMEA region,  
**so that** I can instantly identify regional sales patterns and compare performance across markets.

---

## Acceptance Criteria

1. `TrendChartComponent` renders an ECharts multi-line area chart using `ngx-echarts`
2. One series line per selected region; each region has a distinct, accessible colour (high-contrast, colour-blind friendly palette of 5 colours for DE/FR/IT/ES/UK)
3. X-axis shows time periods (labels adapt to granularity: dates for DAILY, "W08" for WEEKLY, "Mar" for MONTHLY, "Q1" for QUARTERLY)
4. Y-axis shows revenue in the selected display currency (label shows currency code)
5. Hovering a data point shows tooltip with: region name, period, revenue (formatted with 2 decimal places), units
6. Chart re-renders within 200ms when filters change (driven by `aggregatedData$` from `SalesInsightsStateService`)
7. Loading state: skeleton placeholder (grey pulsing box) shown while data is fetching
8. Error state: "Unable to load chart" message with a retry button if `error$` emits
9. If a region has `stale: true`, a warning icon appears in the chart legend next to that region's name
10. Chart is responsive: scales to container width; minimum chart height 300px

---

## Tasks / Subtasks

- [ ] Install / confirm `ngx-echarts` is available in `frontendapplication-i2oretail` (AC: 1)
  - [ ] Check `package.json` for `ngx-echarts` and `echarts`; if missing, `npm install ngx-echarts echarts`
  - [ ] Import `NgxEchartsModule` in `SalesInsightsModule`
- [ ] Create `trend-chart.component.ts/html/scss` (AC: 1–10)
  - [ ] `@Input() chartData: ChartDataPoint[]`
  - [ ] `@Input() loading: boolean`
  - [ ] `@Input() error: string | null`
  - [ ] `@Input() staleRegions: Record<string, boolean>`
  - [ ] `@Input() currency: string`
  - [ ] Build ECharts `EChartsCoreOption` from `chartData` input
- [ ] Implement ECharts option builder (AC: 2, 3, 4, 5)
  - [ ] Group `chartData` by region → one `series` per region
  - [ ] Apply colour palette array: `['#2563EB', '#DC2626', '#16A34A', '#D97706', '#7C3AED']`
  - [ ] X-axis `data`: extract unique `period` values (sorted)
  - [ ] Y-axis `name`: display currency code
  - [ ] Tooltip: `trigger: 'axis'`, custom formatter showing region + revenue + units
- [ ] Loading skeleton HTML (AC: 7)
  - [ ] `<div *ngIf="loading" class="skeleton-chart">` — pulsing CSS animation
- [ ] Error state HTML (AC: 8)
  - [ ] `<div *ngIf="error">Unable to load chart. <button (click)="retry()">Retry</button></div>`
- [ ] Stale region legend marker (AC: 9)
  - [ ] Custom legend formatter: append `⚠️` if `staleRegions[regionName] === true`
- [ ] Wire input changes to ECharts `mergeOption` for re-render (AC: 6)
- [ ] Write unit test: verify ECharts option has correct number of `series` for given `chartData` (AC: 2)

---

## Dev Notes

**Repository:** `i2o-retail/frontendapplication-i2oretail`  
**Path:** `src/app/modules/sales-insights/components/trend-chart/`  
**Prerequisite stories:** GA-SI-03-S01 (module scaffold), GA-SI-03-S02 (state service)

**ECharts option structure:**
```typescript
buildChartOption(data: ChartDataPoint[], currency: string): EChartsCoreOption {
  const regions = [...new Set(data.map(d => d.region))];
  const periods = [...new Set(data.map(d => d.period))].sort();
  const colors = ['#2563EB', '#DC2626', '#16A34A', '#D97706', '#7C3AED'];

  return {
    color: colors,
    tooltip: {
      trigger: 'axis',
      formatter: (params: any[]) => params.map(p =>
        `${p.seriesName}: ${currency} ${p.data.toFixed(2)}`
      ).join('<br/>')
    },
    legend: {
      data: regions,
      formatter: (name: string) =>
        this.staleRegions[name] ? `${name} ⚠️` : name
    },
    xAxis: { type: 'category', data: periods },
    yAxis: { type: 'value', name: currency },
    series: regions.map((region, i) => ({
      name: region,
      type: 'line',
      areaStyle: { opacity: 0.1 },
      data: periods.map(p => {
        const point = data.find(d => d.region === region && d.period === p);
        return point?.revenue ?? 0;
      })
    }))
  };
}
```

**ngx-echarts template:**
```html
<div *ngIf="loading" class="skeleton-chart"></div>
<div *ngIf="error" class="chart-error">
  Unable to load chart. <button (click)="retry.emit()">Retry</button>
</div>
<div *ngIf="!loading && !error" echarts [options]="chartOption" 
     [merge]="chartOption" class="trend-chart"></div>
```

**SCSS — skeleton animation:**
```scss
.skeleton-chart {
  height: 300px;
  background: linear-gradient(90deg, #e2e8f0 25%, #f8fafc 50%, #e2e8f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

**Design reference:** `docs/requirements/images/Graph.png` — shows the chart style expected; and `docs/requirements/images/Multi Region Screen.png` for overall layout context.

### Testing

- **Location:** `src/app/modules/sales-insights/components/trend-chart/trend-chart.component.spec.ts`
- **Framework:** Jasmine/Karma + Angular `TestBed`
- **Key test:** Given `chartData` with DE and UK series → `buildChartOption()` returns 2 series with correct names
- **Stale test:** Given `staleRegions = {UK: true}` → UK legend item includes `⚠️`
- **Empty state test:** Given empty `chartData` → chart renders with 0 series (no error)

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
