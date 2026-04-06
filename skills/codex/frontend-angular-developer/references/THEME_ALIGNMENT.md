# Marketplace Overview — i2o Theme Alignment

## 1. Why the module looks off-theme

The marketplace overview screens were built with **standalone SCSS and hardcoded hex values** (e.g. `#ffffff`, `#e0e0e0`, `#333`, `#f7f9fa`) in:

| Area | File(s) | Current approach |
|------|---------|------------------|
| Filter bar | `filter-bar.component.scss` | White bar, generic borders, local `::ng-deep` on PrimeNG |
| Cards | `marketplace-card.component.scss` | Generic shadows; activated/trial greens/oranges not tied to `$extras` |
| Page shell | `marketplace-overview-page.component.scss` | Background `#f7f9fa` |
| KPI groups | `kpi-group.component.scss` | `#444`, `#eee` |
| Table | `marketplace-table.component.scss` + template | **AG Grid** uses `ag-theme-alpine` with local overrides |

Elsewhere in i2o, themed screens **do not** rely on raw hex for layout/surface colors. They use:

1. **`$extras` map** in `src/styles.scss` — semantic tokens (e.g. `layout-background`, `border-color`, `header-background-color`, `text-high-emphasis`, `greyscale-*`, `chart-heading`, `ag-grid-primary`, `ag-grid-header`).
2. **Per-component theme mixins** — `*.component.theme.scss` files that declare `@mixin component-name-theme($theme)` and read colors via `map-get($theme, extra-colors)`.
3. **Central registration** — `src/app/styles/component-themes.scss` imports each theme file and includes every mixin inside `@mixin component-themes($theme)`, which is invoked from `styles.scss` as `@include component-themes($app-theme)`.

**Marketplace overview has no theme mixin and is not registered in `component-themes.scss`.** It therefore never receives `$app-theme`, cannot follow global theme switches, and drifts visually from dashboard, filters, and marketplace forms that *are* on the pipeline.

---

## 2. Target architecture

```
styles.scss ($extras + $app-theme)
        ↓
component-themes.scss (@include component-themes($app-theme))
        ↓
marketplace-overview-theme($theme)   ← to be added
        ↓
Scoped under .marketplace-overview-container (or similar)
```

All new color usage should flow from **`map-get($extra-colors, <key>)`** (or Material palette roles) inside the mixin, not from literals in component SCSS.

---

## 3. Recommended implementation phases

### Phase 1 — Register and scope

1. **Scope:** Use the existing root wrapper (e.g. `.marketplace-overview-container`) so theme rules are prefixed and do not leak globally.
2. **Create** `marketplace-overview.component.theme.scss` (or split into `filter-bar`, `marketplace-card`, `marketplace-table` theme partials if preferred) containing:
   - `@use '@angular/material' as mat;` if you need palette helpers.
   - `@mixin marketplace-overview-theme($theme) { ... }`
   - Inside the mixin:
     - `$extra-colors: map-get($theme, extra-colors);`
     - Replace each previous hex with the closest existing `$extras` key (see section 5).
3. **Register:**  
   - `@import` the new file in `src/app/styles/component-themes.scss`.  
   - Add `@include marketplace-overview-theme($theme);` inside `@mixin component-themes($theme)`.

### Phase 2 — PrimeNG (filter bar)

- Controls: `p-multiselect`, `p-dropdown`, `p-calendar`, `p-selectbutton`.
- Align borders, focus rings, and fills to **either** PrimeNG’s theme variables **or** `$extra-colors` (e.g. `btn-border-color`, `white-color`, `ag-grid-accent` for active states).
- **Reference pattern:** `src/app/modules/common/app-filters/app-filters.component.theme.scss`.

### Phase 3 — AG Grid

- Today: `ag-theme-alpine` + `.marketplace-grid` overrides — visually neutral vs i2o grids.
- **Option A — Override Alpine:** Use `$extra-colors` for header background, header text, accent, and borders to match `ag-grid-header` / `ag-grid-primary`.
- **Option B — Shared grid theme:** Reuse the same theme class or SCSS partial as `app-data-grid` / full-edit-grid if those are the canonical report grids.
- Loading and no-rows overlays should use theme-friendly colors, not one-off grays.

### Phase 4 — Cards and KPIs

- Activated/trial badges: map to existing tokens if any (success/warn), or **add once** to `$extras` and consume from the mixin only.
- Typography: align with `$custom-typography` and existing card themes (`dashboard-card`, `synopsis-card`) for font size/weight consistency.

---

## 4. Checklist

| Step | Action |
|------|--------|
| 1 | Audit all marketplace-overview `*.scss` for hex/rgb; list each and target `$extras` key or new key. |
| 2 | Implement `marketplace-overview-theme($theme)` and register in `component-themes.scss`. |
| 3 | PrimeNG: move filter bar colors into mixin / variables; reduce raw `::ng-deep` literals. |
| 4 | AG Grid: theme header/accent to match i2o grids; document chosen option (A or B). |
| 5 | Regression test if the app swaps stylesheets (`AppThemeService` / alternate theme links). |

---

## 5. Reference locations

| Item | Location |
|------|----------|
| `$extras` map | `src/styles.scss` (starts ~line 88) |
| Theme registration | `src/app/styles/component-themes.scss` |
| Global theme apply | `src/styles.scss` — `@include component-themes($app-theme);` |
| Filter theme example | `src/app/modules/common/app-filters/app-filters.component.theme.scss` |
| Dashboard/chart example | `src/app/modules/dashboard/dashboard.component.theme.scss` |
| Data grid theme | `src/app/modules/common/data-grid/app-data-grid.component.theme.scss` |
| Marketplace form themes | `component-themes.scss` imports under `modules/marketplace/...` |

---

## 6. Optional: mapping cheatsheet

Use this as a starting point when replacing literals (confirm with design if a key is ambiguous):

| Current literal (examples) | Candidate `$extras` key |
|----------------------------|-------------------------|
| `#ffffff` / white surfaces | `white-color` |
| `#e0e0e0`, `#ebebeb` borders | `border-color`, `greyscale-200` |
| `#333`, `#444` body text | `text-high-emphasis`, `charcoal-grey`, `h3-regular-color` |
| Page background `#f7f9fa` | `layout-background`, `greyscale-100` |
| AG Grid header / accent | `ag-grid-header`, `ag-grid-primary`, `ag-grid-accent` |

---

## Document control

| | |
|--|--|
| **Owner** | Frontend / platform theme |
| **Update when** | New `$extras` keys added, AG Grid theme strategy changes, or PrimeNG preset changes |

*End of document.*
