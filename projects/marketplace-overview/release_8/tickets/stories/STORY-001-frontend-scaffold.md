---
id: STORY-001
title: "[MO] Frontend: Module Scaffold, Models, API Service & State Service"
project: marketplace_overview
release: release_8
module: frontendapplication-i2oretail
type: Story
priority: High
epic: EPIC-001
status: Draft
estimate: 3 days
created: 2026-03-04
updated: 2026-03-20
---

# STORY-001 — Frontend: Module Scaffold, Models, API Service & State Service

## Context

This story lays the foundation for the Marketplace Overview Angular feature inside `frontendapplication-i2oretail`. All subsequent frontend stories (STORY-002 through STORY-005) depend on this scaffold. The module is lazy-loaded and follows the established Angular module pattern with wiring via **CoreModule** per March 2026 standards.

## Module: `frontendapplication-i2oretail`

### Files to Create

```
src/app/modules/marketplace-overview/
├── marketplace-overview.module.ts
├── marketplace-overview-routing.module.ts
├── marketplace-overview.constants.ts
├── models/
│   ├── marketplace-kpi.model.ts
│   ├── marketplace-filter.model.ts
│   └── marketplace-activation.model.ts
└── services/
    ├── marketplace-overview-api.service.ts
    └── marketplace-overview-state.service.ts
```

### Route Registration

Add to `app-routing.module.ts` (lazy-loading):
```typescript
{
  path: 'brand-protector/benefits/marketplace-overview',
  loadChildren: () => import('./modules/marketplace-overview/marketplace-overview.module')
    .then(m => m.MarketplaceOverviewModule),
  canActivate: [KeycloakAuthGuard, RoleBasedAuthGuard],
  data: { roles: ['brand-protector'] }
}
```

### Key Models (`marketplace-kpi.model.ts`)

```typescript
export type ViewMode = 'card' | 'table';
export type MarketplaceName = 'AMAZON' | 'WALMART' | 'EBAY' | 'TARGET';
export type MarketplaceStatus = 'ACTIVATED' | 'TRIAL';

export interface MarketplaceFilter {
  brands: string[];
  region: string;
  weekStart: string;
  weekEnd: string;
  viewMode: ViewMode;
}
```

### `MarketplaceOverviewApiService`

- `getConfig(): Observable<MarketplaceConfigResponse>` — calls `GET /marketplace-overview/config`
- `getCardData(filters): Observable<any>` — calls `POST /widget/getCardData` with `componentId: 'bp_marketplace_overview_card'`
- `getGridData(filters): Observable<any>` — calls `POST /report/getGridCardData` with `componentId: 'bp_marketplace_overview_table'`
- `initiateTrial(brand, marketplace): Observable<any>` — calls `POST /marketplace-overview/initiate-trial`

### `MarketplaceOverviewStateService`

- BehaviorSubjects: `filter$`, `data$`, `loading$`, `error$`
- `setFilter(partial: Partial<MarketplaceFilter>): void`
- `loadData(): void` — triggers API call, updates `data$`
- Default filter: `brands: [], region: '', weekStart: getLastMonday(), weekEnd: getLastSunday(), viewMode: 'card'`

## User Stories Covered

- **US001** (AC 1–9): Route is gated behind `brand-protector` Keycloak role; **Marketplace Overview tab must be inserted into the Benefits top navigation and must be hidden for non-BP users**.
- **US002** (AC 17–21): Default filter values set correctly; state persists across view toggle.

## Acceptance Criteria

1. `marketplace-overview` module exists and is lazy-loaded at `/brand-protector/benefits/marketplace-overview`.
2. Route is protected by `RoleBasedAuthGuard` with `roles: ['brand-protector']`.
3. `MarketplaceOverviewApiService` has all 4 methods implemented with correct endpoint URLs and payload shapes.
4. `MarketplaceOverviewStateService` exposes `filter$`, `data$`, `loading$` observables.
5. Default filter includes `getLastMonday()` and `getLastSunday()` week range, `viewMode: 'card'`.
6. Unit tests cover `MarketplaceOverviewApiService` with `HttpClientTestingModule` (≥ 80% coverage).
7. Unit tests cover `MarketplaceOverviewStateService` state transitions (≥ 80% coverage).
8. **[Remediates F-H-001]** A "Marketplace Overview" entry is inserted into the Benefits top-navigation menu; the entry is visible only for users with the `brand-protector` role.
9. **[Remediates F-H-001]** The Benefits top-nav "Marketplace Overview" entry is NOT rendered for users without the `brand-protector` role; **Playwright** test evidence is provided showing tab presence/absence.

## Definition of Done Checklist

- [ ] Module scaffold created and lazy-loaded
- [ ] Route registered in `app-routing.module.ts` with role guard
- [ ] Feature-scoped `marketplace-overview.constants.ts` created
- [ ] All 3 model files created with interfaces matching architecture Section 7.3
- [ ] API service created with all 4 methods, correct endpoint URLs and header handling
- [ ] State service created with BehaviorSubject pattern and default filter
- [ ] Unit tests written achieving ≥ 80% coverage on both services
- [ ] No lint errors; build passes locally
- [ ] **[F-H-001]** "Marketplace Overview" tab added to Benefits top-navigation component
- [ ] **[F-H-001]** Tab is conditionally rendered using role guard / `*ngIf` for `brand-protector` role only
- [ ] **[F-H-001]** **Playwright** test evidence attached to PR showing tab visibility for BP user and tab absence for non-BP user

## Architecture References

- Section 5.1 — Angular module file structure
- Section 7.3 — TypeScript interfaces
- Section 9.1 — Routing
- Section 9.2 — State management pattern
- Section 8.1, 8.2 — API endpoint contracts
- SUMMARY-frontendapplication-i2oretail.md — March 2026 baselines
