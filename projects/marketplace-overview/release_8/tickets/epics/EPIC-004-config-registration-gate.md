---
id: EPIC-004
title: "[MO] Config Registration & Integration Readiness Gate"
project: marketplace_overview
release: release_8
module: i2o-reseller (PostgreSQL config)
type: Epic
priority: High
status: Draft
created: 2026-03-04
stories:
  - STORY-011
---

# EPIC-004 — Config Registration & Integration Readiness Gate

## Business Value (Charlie-Conductor)

Before the frontend can call the existing `getCardData`/`getGridCardData` endpoints with Marketplace Overview-specific component IDs, those component IDs (`bp_marketplace_overview_card`, `bp_marketplace_overview_table`) must be registered in the `i2oretail.component` PostgreSQL configuration table and linked to the correct `query_id` rows. This is the **critical GO/NO-GO gate** (Open Item #2) identified in the architecture review. Completing this epic unblocks all frontend integration testing.

## Technical Feasibility (Bob-Builder)

- **Scope:** Data migration / config DML — no code changes.
- **Effort estimate:** Small (1–2 days).
- **Risk:** 🔴 High — frontend integration testing is blocked until this is complete. Must be deployed to DEV → QA → PROD in sequence.
- **Dependency:** Requires `query_id` values from BQ query catalog (`query_described.csv`-equivalent config). Engineering Lead action.

## Scope

| Area | Deliverable |
|------|-------------|
| componentId registration | DML script: INSERT `bp_marketplace_overview_card` and `bp_marketplace_overview_table` into `i2oretail.component` |
| query_id wiring | Link each componentId to the correct BQ `query_id` in the `ui_config` / `query_described` config |
| DEV deployment | Deploy and verify in DEV environment |
| QA deployment | Deploy and verify in QA environment |
| PROD deployment | Deploy to PROD after QA sign-off |

## Story Breakdown

| Story | Title |
|-------|-------|
| STORY-011 | Register `bp_marketplace_overview_card` and `bp_marketplace_overview_table` componentIds in PostgreSQL config (GO/NO-GO gate) |

## Acceptance Criteria (Epic-level)

1. `bp_marketplace_overview_card` componentId exists in `i2oretail.component` and references the correct `query_id` for card-view KPI queries.
2. `bp_marketplace_overview_table` componentId exists in `i2oretail.component` and references the correct `query_id` for table-view KPI queries.
3. `POST /widget/getCardData` with `componentId: "bp_marketplace_overview_card"` returns data in DEV.
4. `POST /report/getGridCardData` with `componentId: "bp_marketplace_overview_table"` returns data in DEV.
5. Config is deployed to QA and verified before frontend integration testing begins.

## Architecture References

- Section 4.1 — Decision: reuse `getCardData`/`getGridCardData` with BP-specific `query_id`
- Section 8.1 — API request payload examples for both APIs
- Section 16, Open Item #2 — GO/NO-GO GATE description
