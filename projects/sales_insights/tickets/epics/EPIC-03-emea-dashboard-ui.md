# Epic: EPIC-03 — EMEA Sales Command Center Dashboard (Angular UI)

**Epic ID:** GA-SI-EPIC-03  
**Priority:** P0 — Critical  
**Target Release:** Q2 2026 (Week 8 — Beta UAT)  
**Status:** Draft  
**Epic Type:** Frontend / UI  
**Depends on:** EPIC-02 (API must be available before UI integration)

---

## Business Value (Charlie-Conductor)

This epic delivers the user-facing "Command Center" — the unified EMEA sales dashboard that replaces fragmented Excel reports. It directly delivers value to Regional Sales Managers, Executive VPs, and Data Analysts by showing real-time multi-currency KPIs, trend charts, and SKU-level data in a single interactive view.

**Business Outcome:** 100% adoption by Regional Managers (90-day target); reporting turnaround reduced from 2–3 days to <5 seconds; Executive VP gets instant pan-EMEA visibility.

---

## Two-Agent Analysis

- **Strategic (Charlie-Conductor):** Highest business visibility epic — this is the user-facing interface. Adoption depends entirely on it being intuitive and fast. Must match UI screens in PRD (Multi Region Screen, View By Table, Currency Filter, Graph).
- **Technical (Bob-Builder):** New Angular lazy-loaded module inside `frontendapplication-i2oretail` following the existing `modules/sales-analysis/` pattern. Uses ECharts (already in app), AG Grid Enterprise (already licensed), PrimeNG dropdowns, Keycloak Angular auth (already wired via `KeycloakBearerInterceptor`).

---

## Success Metrics

- Dashboard chart + cards update in < 200ms after filter change (Performance profiling)
- AG Grid handles 10,000 SKU rows smoothly (>30 fps scroll)
- CSV export generates file for filtered data (exported file check)
- All 5 regions (DE, FR, IT, ES, UK) render correctly with correct currency conversion
- Stale data warning visible for regions with data >24h old
- Keycloak-protected: unauthorized regions not visible in filter list

---

## Technical Foundation (Bob-Builder)

- **Repository:** `i2o-retail/frontendapplication-i2oretail` (Angular 15, TypeScript 4.9.5)
- **Path:** `src/app/modules/sales-insights/` (new lazy-loaded module)
- **Pattern:** Follow `modules/sales-analysis/` and `modules/dashboard/` for conventions
- **Charts:** ECharts 6.0 (`ngx-echarts` wrapper) — multi-line area chart for trend
- **Data Grid:** AG Grid Enterprise 21.1.1 — virtual row rendering, column search, CSV export
- **UI Components:** PrimeNG 15 (multi-select dropdowns, buttons, cards); Angular Material 15 (layout)
- **State:** RxJS BehaviorSubject via `SalesInsightsStateService`
- **HTTP:** `SalesInsightsApiService` using existing `RestApiService` / `rest-api.service.ts` pattern
- **Auth:** Existing `KeycloakBearerInterceptor` auto-attaches JWT; `RoleBasedAuthGuard` protects `/sales-insights` route
- **Route:** Lazy-loaded `{ path: 'sales-insights', loadChildren: () => import('./modules/sales-insights/sales-insights.module').then(m => m.SalesInsightsModule) }`

---

## Architecture Components

From `architecture.md` (Sections 5.2, 6.1, 6.4, PRD Section C):

**Module Structure:**
```
src/app/modules/sales-insights/
├── sales-insights.module.ts
├── sales-insights-routing.module.ts
├── components/
│   ├── sales-filter-bar/     # PrimeNG p-multiSelect for regions; p-dropdown for currency, granularity
│   ├── kpi-card-group/       # Revenue (converted), Units, ASP cards
│   ├── trend-chart/          # ECharts multi-line: one series per region
│   ├── sales-data-grid/      # AG Grid Enterprise: search, sort, export
│   └── stale-data-badge/     # Yellow dot + tooltip for >24h stale regions
├── services/
│   ├── sales-insights-api.service.ts     # GET /api/v1/sales-insights/*
│   └── sales-insights-state.service.ts  # BehaviorSubjects: filters$, data$, loading$
└── models/
    └── sales-insights.model.ts           # SalesQuery, KpiSummary, ChartData, GridRow
```

**API Consumed:**
- `GET /api/v1/sales-insights/aggregate?regions=DE,FR&currency=EUR&granularity=WEEKLY`
- `GET /api/v1/sales-insights/currencies`
- `GET /api/v1/sales-insights/stale-status`
- `GET /api/v1/sales-insights/export?regions=...&currency=...&format=csv`

**UI Screens (from PRD Section C, Story #3):**
1. **Main Dashboard:** Context filter bar (top sticky) → KPI cards (Revenue, Units, ASP) → Trend chart (multi-line regional comparison)
2. **Detailed Table:** SKU-level AG Grid with column search + CSV export button
3. **Filter Interactions:** Multi-select region picker; currency dropdown; granularity selector (Daily/Weekly/Monthly/Quarterly)

---

## Dependencies

- **Depends on:** EPIC-02 — API endpoints must be available for integration
- **External:** API contract finalized and documented (OpenAPI spec from `sales-insights-api`)
- **Coordination (Charlie):** UI screens from PRD images used as design reference; align with UX on ECharts color palette for 5 regions (accessible, high-contrast)

---

## Implementation Readiness

- **Ready:** Angular module pattern established; ECharts, AG Grid Enterprise, Keycloak Angular, PrimeNG all already installed and configured in `frontendapplication-i2oretail`
- **Design Reference:** PRD images at `docs/requirements/images/` (Multi Region Screen.png, View By Table.png, Currency Filter.png, Region Filter.png, Graph.png)

---

## Stories Breakdown

- [ ] **GA-SI-03-S01** — Angular Module Scaffold: `sales-insights.module.ts`, routing, lazy route registration — 0.5 day
- [ ] **GA-SI-03-S02** — `SalesInsightsApiService` & `SalesInsightsStateService` (RxJS) — 1 day
- [ ] **GA-SI-03-S03** — `SalesFilterBarComponent`: Region, Currency, Granularity selectors — 1 day
- [ ] **GA-SI-03-S04** — `KpiCardGroupComponent`: Revenue, Units, ASP cards with currency label — 0.5 day
- [ ] **GA-SI-03-S05** — `TrendChartComponent`: ECharts multi-line area chart with tooltip — 1.5 days
- [ ] **GA-SI-03-S06** — `SalesDataGridComponent`: AG Grid Enterprise with search + CSV export — 1.5 days
- [ ] **GA-SI-03-S07** — `StaleDataBadgeComponent` + error states (loading skeletons, empty state, error overlay) — 0.5 day
- [ ] **GA-SI-03-S08** — Route guard, nav link, E2E integration test (Protractor) — 1 day

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial epic generation from architecture | AI Agent |
