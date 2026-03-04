---
epic_key: GA-SI-002
project: sales_insights
labels: [architecture, frontend, api]
components: [sales-insights-api, frontendapp]
---

# Epic: Beta (MVP Dashboard) - Unified Aggregation & UI

## Business Value (Charlie-Conductor)
This Epic binds disparate regional sales data into a unified, high-performance UI. Regional managers will gain immediate insights by querying "Sales across FR, DE in GBP" dynamically. Replacing slow manual workflows involves building the `sales-insights-api` to process business logic instantly, while extending the robust `frontendapplication-i2oretail` SPA to render interactive trend-charts and tabular datasets.

## Technical Execution & Bounds (Bob-Builder)
- **Domain:** `sales-insights-api` and `frontendapplication-i2oretail`.
- **Stack:** Java 17, Angular 15, RxJS, ECharts, AG Grid Enterprise.
- **Constraints:** ECharts required for graphics. AG Grid for 10k+ row DOM virtualization.
- **Performance Spec:** Real-time AggregationService (<200ms loads) hits the `mv_daily_aggregates` view, rather than raw row queries. Background threads configured explicitly for async CSV exports over SendGrid (`@Async`). Playwright replaces existing E2E (deprecation).
- **Security:** KeycloakBearerInterceptor auth propagation required.

## Included Stories
- **GA-SI-002-S01**: SalesInsightsController & AggregationService / FxConversion
- **GA-SI-002-S02**: Large CSV Export Background Async Thread 
- **GA-SI-002-S03**: Angular Dashboard Module Bootstrap (Routing, Base Components)
- **GA-SI-002-S04**: SalesInsightsStateService / API wiring & Debouncing (RxJS)
- **GA-SI-002-S05**: ECharts Implementation & KPI Cards
- **GA-SI-002-S06**: AG Grid Enterprise Setup (Export & Paging)
- **GA-SI-002-S07**: Playwright E2E Dash Validation

## Go-Live Readiness
- 100% adoption metrics tracking active.
- End-to-end report UI latency validated sub 5-seconds. 
- UI responds smoothly under 10k row scenarios.
