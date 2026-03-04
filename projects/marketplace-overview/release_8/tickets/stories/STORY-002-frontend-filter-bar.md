---
id: STORY-002
title: "[MO] Frontend: Filter Bar Component"
project: marketplace_overview
release: release_8
module: frontendapplication-i2oretail
type: Story
priority: High
epic: EPIC-001
status: Draft
estimate: 2 days
created: 2026-03-04
depends_on:
  - STORY-001
---

# STORY-002 — Frontend: Filter Bar Component

## Context

The Filter Bar is the primary navigation control on the Marketplace Overview page. It contains Brand multi-select, Region dropdown, Calendar (week mode), and a Card/Table view toggle. Filter changes update `MarketplaceOverviewStateService` which triggers a fresh API call. Filter state must persist when toggling between card and table view.

## Module: `frontendapplication-i2oretail`

### Files to Create/Modify

```
src/app/modules/marketplace-overview/components/filter-bar/
├── filter-bar.component.ts
├── filter-bar.component.html
└── filter-bar.component.scss
```

Also modify:
- `marketplace-overview-page/marketplace-overview-page.component.html` — include `<app-filter-bar>`

### Component Specification

**Inputs:**
- `brands: { id: string; name: string }[]` — from config API response
- `regions: string[]` — from config API response
- `currentFilter: MarketplaceFilter` — from state service

**Outputs:**
- `filterChange: EventEmitter<Partial<MarketplaceFilter>>` — emits on any filter change

**UI Controls:**

| Control | Type | Notes |
|---------|------|-------|
| Brand | PrimeNG MultiSelect | Allows selecting multiple brands; single-brand disambiguation for Initiate Trial handled by STORY-005 |
| Region | PrimeNG Dropdown | Region list from config |
| Calendar | PrimeNG Calendar (week mode) | Selects week range (Mon–Sun); defaults to last complete week |
| View Toggle | Toggle button (Card / Table) | Emits `viewMode` update; does NOT reset other filter values |

**Week selector rules:**
- Defaults to last complete Monday–Sunday week on page load.
- User can select any historical week from calendar picker.
- Week start must be a Monday; week end must be the same week's Sunday.

## User Stories Covered

- **US002** (AC 17–21): Filter bar renders correctly; filter state persists across Card ↔ Table toggle
- **US006** (AC 59–62): Calendar defaults to last complete week

## Acceptance Criteria

1. Filter bar renders with Brand multi-select, Region dropdown, Calendar, and View toggle controls.
2. Brand options are populated from `GET /marketplace-overview/config` response.
3. Region options are populated from `GET /marketplace-overview/config` response.
4. Calendar defaults to the last complete week (Monday–Sunday) on page load.
5. Any filter change emits `filterChange` and triggers a fresh data API call via the state service.
6. Toggling Card ↔ Table view preserves all other filter values (brand, region, week).
7. Unit tests cover filter initialization and `filterChange` emission (≥ 70% component coverage).

## Definition of Done Checklist

- [ ] `FilterBarComponent` created with all 4 controls
- [ ] Brand/Region populated from config API via inputs
- [ ] Calendar week selector defaults to `getLastMonday()` / `getLastSunday()`
- [ ] `filterChange` event emitter wired to state service in parent component
- [ ] View toggle does not reset brand/region/week selection
- [ ] Unit tests written
- [ ] Matches existing filter bar styling conventions of the application

## Architecture References

- Section 9.2 — State management pattern (BehaviorSubject filter update)
- Section 9.3 — Component interaction diagram (FilterBarComponent)
- Section 9.4 — Default filter state
- Section 6.1 — Step 1: Config load sequence
