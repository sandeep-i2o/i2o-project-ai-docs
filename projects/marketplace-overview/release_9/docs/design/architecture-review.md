# Architecture Review - Marketplace Overview (release_9)

## 1. Review Metadata

- Project: `marketplace-overview`
- Reviewer: `AI Agent`
- Review version: `v9`
- Date: `2026-04-06`
- Source docs:
  - `projects/marketplace-overview/release_9/docs/design/architecture.md` (`v1.8`)
  - `projects/marketplace-overview/release_9/docs/requirements/prd.md` (`v1.0`)
  - `knowledge/pg_schema/app_db_schema.csv` (schema validation for `org_market_mapping.enabled`)
  - `PID`: Not applicable for release_9 (Product direction recorded on 2026-04-06)
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026.MD`
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026-02.MD`
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026-03.MD`
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026-04.MD`

## 2. Executive Verdict

- Overall status: `Conditionally Approved`
- Feasibility summary: No material source-document delta was found since review v8. Product decisions remain explicit for release_9: placeholder-only unsubscribed metrics, published PPT URL as WBR artifact, retry execution via `i2o-scheduler`, and PID not applicable. P1 blockers AR-010 and AR-011 remain resolved; requirement/contract mismatches (AR-013, AR-015) remain accepted risks pending PRD text alignment. One quality gap remains open for KPI reliability (`mo_wbr_download_completed`).
- Highest-risk area: PRD-to-architecture documentation drift for US002/US004 until PRD revision captures the approved release_9 decisions.

## 3. Severity Summary

- `P0` count: `1`
- `P1` count: `3`
- `P2` count: `1`
- `P3` count: `0`

## 4. Findings (Ordered by Severity)

### AR-013
- Severity: `P0`
- Area: Functional Coverage / Requirement Compliance
- Gap: Architecture `v1.8` keeps canonical/backend sourcing for unsubscribed marketplace metrics out of release_9 and mandates UI placeholders (`##`) with no API/backend logic.
- Evidence:
  - PRD B5 (In Scope) requires top unsubscribed marketplace cards with pain ranking.
  - PRD US002 requires ranked cards by reseller count, metric fields (`Total Products`, `Total Listings`, `Total Resellers`), and pain-badge calculation.
  - Architecture v1.8 confirms Product decision for release_9 placeholder-only behavior (`Change Notes v1.8`, `Section 8.2`, `Section 9.4`).
- Impact: Core P0 user story behavior is not implementable as specified; release intent ("unmonitored marketplace risk view") is not met.
- Recommendation: Update PRD B5/US002/US003 text to reflect approved release_9 placeholder scope and move canonical metrics delivery to follow-up release scope.
- Status: `Accepted Risk`

### AR-014
- Severity: `P1`
- Area: Functional Consistency / Validation Logic
- Gap: The previous review found the validation source undefined. Architecture `v1.8` defines an authoritative source for "known unsubscribed marketplace."
- Evidence:
  - Architecture Section 8.4 defines validation query using `org_market_mapping` with `COALESCE(enabled,false)=false`.
  - Architecture Section 11.4 applies the same source to both `start-pilot` and `request-audit`.
  - Schema reference `knowledge/pg_schema/app_db_schema.csv` contains `org_market_mapping.enabled` as boolean.
- Impact: Validation logic is now deterministic and auditable.
- Recommendation: Keep integration tests to verify marketplace/region matching against `enabled=false` rows.
- Status: `Resolved`

### AR-015
- Severity: `P1`
- Area: API Contract / Requirement Alignment
- Gap: WBR artifact contract diverges from PRD: PRD specifies zip download of brand-level PDFs; architecture now specifies published URL from `sw.gcs_location` and sample `.pptx`.
- Evidence:
  - PRD US004 flow and acceptance criteria explicitly call for zip download containing brand-level PDFs.
  - Architecture v1.8 confirms Product decision: canonical WBR artifact is published `PPT url` from `sw.gcs_location` (Change Notes v1.8, Section 8.3).
- Impact: Implementation built to architecture may fail PRD acceptance and user expectation.
- Recommendation: Update PRD US004 and glossary language from zip/PDF bundle to published PPT URL contract for release_9.
- Status: `Accepted Risk`

### AR-010
- Severity: `P1`
- Area: Resilience / Operations
- Gap: Retry executor ownership was previously unspecified.
- Evidence:
  - Architecture Section 7.2 defines `marketplace_email_outbox`.
  - Architecture Section 10.3 now includes scheduler config (`email_retry_scheduler_cron`).
  - Architecture Section 12.1.1 assigns retry execution to `i2o-scheduler` job `MarketplaceOverviewEmailRetryJob`.
- Impact: Retry ownership and execution path are now implementation-ready.
- Recommendation: Add integration test coverage for scheduler retry state transitions (`PENDING/RETRYING/SENT/FAILED`).
- Status: `Resolved`

### AR-011
- Severity: `P1`
- Area: Governance / Delivery Readiness
- Gap: PID disposition was previously unresolved.
- Evidence:
  - Architecture Section 1.5 now records PID as not applicable for release_9.
  - Architecture Section 10.5 marks PID disposition dependency as `Closed`.
- Impact: Governance blocker removed for release_9 architecture approval.
- Recommendation: None.
- Status: `Resolved`

### AR-012
- Severity: `P2`
- Area: Observability / KPI Measurement
- Gap: `mo_wbr_download_completed` remains weakly measurable because WBR uses direct URL navigation outside reliable app callback control.
- Evidence:
  - Architecture Section 12.5 defines completion event.
  - Architecture Section 6.4 shows browser navigates directly to published download URL.
- Impact: Completion metric is likely under-reported or inconsistent.
- Recommendation: Use `mo_wbr_download_initiated` as primary KPI or move completion measurement to server-side access logs.
- Status: `Open`

## 5. PRD/PID Coverage Matrix

| Requirement ID/Topic | Source | Architecture Coverage | Notes |
|---|---|---|---|
| US001 Active subscriptions + enforcement popup + link gating | PRD | Full | Sections 6.1, 8.1, 9.3 remain aligned. |
| US002 Unsubscribed marketplace ranking + pain levels | PRD | Conflicting | Product accepted release_9 placeholder-only behavior; PRD update is still required (AR-013 accepted risk). |
| US003 Brand and enforcement filtering | PRD | Partial | Enforcement filtering is defined; unsubscribed metric behavior follows approved placeholder scope in release_9 (AR-013 accepted risk). |
| US004 WBR download | PRD | Partial | Architecture follows approved published-PPT contract; PRD still states zip/PDF bundle (AR-015 accepted risk). |
| US005 Start Free Pilot | PRD | Full | Core flow and validation source are now explicitly defined via `org_market_mapping.enabled = false` (AR-014 resolved). |
| US006 Request Audit Report | PRD | Full | Flow, duplicate handling, and retry semantics are specified. |
| US007 Audit sample download | PRD | Full | One-click guard + download URL flow is defined. |
| US009 Navigation links | PRD | Full | `ui_config`-based gating is explicit. |
| Success metrics / observability | PRD | Partial | KPI plan exists; WBR completion event remains weak (AR-012). |
| PID baseline | PID | Full | Product disposition recorded: PID not applicable for release_9 (AR-011 resolved). |

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks:
  - No open implementation blocker remains after decisions captured in architecture v1.8.
- Integration and dependency risks:
  - PRD text is still misaligned with approved release_9 behavior for US002/US004 until PRD is revised.
- Non-functional readiness risks:
  - WBR completion KPI remains difficult to measure reliably.
- Rollout and operations risks:
  - Remaining release gates are operational dependencies (bucket readiness, contract validation, support-email path smoke test).

## 7. Open Questions and Assumptions

None. Open questions from v7 were resolved on 2026-04-06:
1. US002 scope: placeholder-only unsubscribed metrics for release_9.
2. WBR artifact: published PPT URL is canonical for release_9.
3. Retry execution: scheduled job in `i2o-scheduler`.
4. PID: not applicable for release_9.

## 8. Approval Log

- Current approval status: `Conditionally Approved`
- Approval date: `2026-04-06`
- Approved by: `Product/Tech Direction (recorded in review resolution inputs)`
- Approval conditions:
  - Update PRD to reflect approved release_9 decisions for US002/US003 and US004 (AR-013/AR-015 accepted risks).
  - Revisit AR-012 before KPI sign-off.
