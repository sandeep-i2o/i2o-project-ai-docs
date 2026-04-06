---
name: frontend-angular-developer
description: Implement or modify Angular frontend code in the i2o-retail repository using repo-specific standards from SUMMARY.md, strict Observable-first TypeScript practices, required Storybook/testing coverage, and mandatory theme alignment through $extras tokens, component theme mixins, and component-themes registration. Use for any new frontend feature, refactor, bug fix, or UI styling change.
---

# Frontend Angular Developer Skill (i2o-retail)

Use this skill for any code change under `src/app` in this repository.

## Read Context First

- Read `SUMMARY.md` to align with repo structure, scripts, and framework versions.
- Read `./references/frontend-angular-coding-guidelines.skill.md` for coding constraints.
- Read `./references/THEME_ALIGNMENT.md` for theme architecture and token usage.
- Read neighboring files in the target module before writing new code.
- If either external guideline file is missing, continue using `SUMMARY.md` and local patterns, then report the limitation.

## Keep Compatibility

- Target Angular `15.2.x` and TypeScript `4.9.x` compatible patterns.
- Follow existing library usage patterns for Angular Material, PrimeNG, AG Grid, ECharts, and FusionCharts.
- Reuse existing auth, routing, and shared-service patterns instead of introducing parallel abstractions.

## Place Code in the Correct Layer

- Add feature code inside `src/app/modules/<feature>/`.
- Add reusable cross-feature UI/utilities inside `src/app/modules/common/`.
- Keep components focused on view orchestration.
- Move data-access and business logic into services.
- Preserve module conventions:
  - `<feature>.module.ts`
  - `<feature>-routing.module.ts` for routed modules
  - `components/`, `services/`, `models/` as needed

## Enforce Size and Structure Limits

- Keep component TypeScript files under `300` lines.
- Keep component templates under `200` lines.
- Keep methods under `30` lines.
- Keep service files under `400` lines.
- Split large files into focused child components or services.

## Follow Naming and Type Rules

- Use `kebab-case` file names and `PascalCase` classes.
- Use suffixes consistently: `*.service.ts`, `*.guard.ts`, `*.pipe.ts`, `*.interceptor.ts`.
- Name Observables with `$` suffix.
- Prefix booleans with `is`, `has`, `can`, or `should`.
- Use explicit interfaces, enums, and union types.
- Avoid `any`; use it only at unavoidable boundaries and document why.

## Use Observable-Only Reactive Patterns

- Use RxJS Observables end-to-end in components and services.
- Return Observables from service methods.
- Compose streams with operators such as `switchMap`, `map`, `combineLatest`, `forkJoin`, `catchError`, `finalize`, and `shareReplay`.
- Prefer template subscriptions via `async` pipe.
- Use `takeUntil(this.destroy$)` for imperative subscriptions and complete `destroy$` in `ngOnDestroy`.
- Do not introduce `Promise`, `async/await`, or `.toPromise()` in application code.

## Apply Component and Template Best Practices

- Use a single-responsibility component design.
- Keep member order consistent:
  1. Public properties
  2. Private properties
  3. Constructor
  4. Lifecycle hooks
  5. Public methods
  6. Private methods
- Use safe navigation (`?.`) on nullable chains.
- Add `trackBy` for non-trivial `*ngFor` lists.
- Prefer `ChangeDetectionStrategy.OnPush` when inputs and flow support it.
- Extract repeated or complex template blocks into child components.

## Enforce Theme Alignment for Every UI Change

- Avoid hardcoded color literals (`#hex`, `rgb`, `rgba`) in feature/component style files.
- Use semantic tokens from `$extras` through theme mixins.
- Read colors inside mixins with:

```scss
$extra-colors: map-get($theme, extra-colors);
color: map-get($extra-colors, text-high-emphasis);
```

- Create or update `*.component.theme.scss` files with `@mixin <component>-theme($theme)`.
- Scope rules under a stable feature root selector to avoid leakage.
- Register each new mixin in `src/app/styles/component-themes.scss`:
  - Add `@import` for the theme file.
  - Add `@include <component>-theme($theme);` inside `@mixin component-themes($theme)`.
- Reuse existing `$extras` keys in `src/styles.scss` before adding new ones.
- Add new tokens only when no semantic key fits, then consume only via mixins.
- Align PrimeNG controls with tokenized borders/focus/active states.
- Align AG Grid surfaces, headers, accents, and borders with i2o grid theme tokens and shared patterns.

## Implement Storybook and Testing Standards

- Add a `.stories.ts` file for each new component.
- Provide at least three stories: default, variant, and edge case.
- Add interactive controls for `@Input()` values.
- Reuse realistic typed mock data.
- Add or update `.spec.ts` tests for behavior, observable success paths, and observable error handling.

## Validate Before Finalizing

- Run `npm run lint`.
- Run `npm test` for affected scope.
- Run `npm run build`.
- Run `npm run build_prod` when production build impact is relevant.
- Run color-literal audit on touched style files:

```bash
rg -n "(#[0-9a-fA-F]{3,8}|rgb\(|rgba\()" src/app
```

- Keep color literals only in centralized token/theme definition locations where intentionally required.

## Definition of Done

- Follow module placement and naming conventions.
- Keep code within size limits or split it.
- Keep all async flows Observable-based.
- Keep UI styles tokenized through theme mixins.
- Register new mixins in `component-themes.scss`.
- Update Storybook and unit tests for affected components.
- Pass lint, tests, and build checks for changed scope.

## Report Back After Each Task

- List changed files and purpose.
- List theme tokens reused or added.
- Confirm mixin registration updates.
- Report validation commands and results.
- Call out intentional deviations and rationale.
