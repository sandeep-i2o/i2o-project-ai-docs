---
id: STORY-005
title: "[MO] Frontend: Initiate Trial Button + Multi-Brand Disambiguation Dialog"
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
  - STORY-003
  - STORY-004
---

# STORY-005 — Frontend: Initiate Trial Button & Multi-Brand Dialog

## Context

Trial marketplaces (eBay, Target) display an "Initiate Trial" button both in Card View (STORY-003) and Table View (STORY-004). Clicking the button triggers `POST /marketplace-overview/initiate-trial`. The **frontend enforces multi-brand disambiguation**: if more than one brand is selected in the filter, the button opens a brand-selection dialog before firing the API call. This is a confirmed frontend-only enforcement decision (architecture Section 4.1, Section 8.2, confirmed 2026-03-04).

## Module: `frontendapplication-i2oretail`

### Files to Create

```
src/app/modules/marketplace-overview/components/initiate-trial-dialog/
├── initiate-trial-dialog.component.ts
├── initiate-trial-dialog.component.html
└── initiate-trial-dialog.component.scss
```

### Button & Dialog Behaviour

**Single brand in filter (`filterState.brandIds.length === 1`):**
1. User clicks "Initiate Trial" on a trial marketplace card/row.
2. Show a confirmation dialog: "Send trial request for [Brand Name] on [Marketplace]? [Confirm / Cancel]"
3. On Confirm: call `POST /marketplace-overview/initiate-trial` with `{ brandId, marketplace }`.
4. On success: show success toast "Trial request sent."
5. On error (503): show error toast "Failed to send — please try again."

**Multiple brands in filter (`filterState.brandIds.length > 1`):**
1. User clicks "Initiate Trial" on a trial marketplace card/row.
2. Show brand-selection dialog: "Please select one brand to initiate trial for [Marketplace]: [Brand dropdown] [Confirm / Cancel]"
3. On Confirm with selected brand: call `POST /marketplace-overview/initiate-trial` with `{ brandId: selectedBrand, marketplace }`.
4. On success: show success toast.
5. On error: show error toast.

**Note:** The backend does NOT perform multi-brand validation — it trusts the single `brandId` sent in the payload. Multi-brand enforcement is purely a frontend responsibility.

### Component Specification

**Inputs:**
- `marketplace: MarketplaceName` — the trial marketplace being activated
- `brands: { id: string; name: string }[]` — list of currently selected brands

**Outputs:**
- `trialConfirmed: EventEmitter<{ brandId: string; marketplace: MarketplaceName }>` — emitted after user selects brand and confirms

## User Stories Covered

- **US005** (AC 50–53): Initiate Trial button triggers confirmation; multi-brand selection prompts brand disambiguation dialog before API call

## Acceptance Criteria

1. "Initiate Trial" button appears on all `TRIAL` status marketplace cards and table rows.
2. Clicking "Initiate Trial" when a single brand is selected shows a confirmation dialog with brand and marketplace name.
3. Clicking "Initiate Trial" when multiple brands are selected shows a brand-selection dropdown dialog.
4. API call `POST /marketplace-overview/initiate-trial` is only fired after user confirmation, with a single `brandId`.
5. On API success: success toast is displayed.
6. On API error (503): error toast "Failed to send — please try again." is displayed.
7. Unit tests cover both single-brand and multi-brand dialog flows (≥ 70% component coverage).

## Definition of Done Checklist

- [ ] `InitiateTrialDialogComponent` created with single-brand and multi-brand modes
- [ ] Dialog opens correctly from both card and table view "Initiate Trial" buttons
- [ ] `POST /marketplace-overview/initiate-trial` called via `MarketplaceOverviewApiService`
- [ ] Success toast displayed on 200 response
- [ ] Error toast displayed on 503 or network error
- [ ] API call is never fired without a single confirmed `brandId`
- [ ] Unit tests written achieving ≥ 70% component coverage

## Architecture References

- Section 4.1 — Multi-brand trial enforcement decision (frontend-only, confirmed 2026-03-04)
- Section 6.2 — Initiate Trial runtime flow
- Section 8.2 — `POST /marketplace-overview/initiate-trial` request/response contract
- Section 10.2 — Email service unreachable error handling (503 → toast)
