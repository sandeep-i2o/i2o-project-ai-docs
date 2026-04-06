# Architecture Review - Marketplace Overview (release_9)

## 1. Review Metadata

- Project: `marketplace-overview`
- Reviewer: `AI Agent`
- Review version: `v4`
- Date: `2026-04-06`
- Source docs:
  - `projects/marketplace-overview/release_9/docs/design/architecture.md` (`v1.5`)
  - `projects/marketplace-overview/release_9/docs/requirements/prd.md` (`v1.0`)
  - `PID`: Not found; disposition pending Product Owner sign-off
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026.MD`
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026-02.MD`
  - `projects/marketplace-overview/release_9/docs/design/ADR/adr-06-04-2026-03.MD`

## 2. Executive Verdict

- Overall status: `Rejected`
- Feasibility summary: The architecture covers the core Marketplace Overview flows and now resolves the earlier brand-filter, ordering, duplicate-download, email-failure, and WBR metadata contradictions. The remaining gaps are the retry queue execution mechanism and PID governance. Those items still block approval.
- Highest-risk area: Operational readiness and governance, because the system cannot be implemented or approved cleanly without an outbox retry executor and PID disposition.

## 3. Severity Summary

- `P0` count: `0`
- `P1` count: `2`
- `P2` count: `1`
- `P3` count: `0`

## 4. Findings (Ordered by Severity)

### AR-009
- Severity: `P1`
- Area: Data Contract / API Specification
- Gap: `GET /marketplace-overview/config` now has a defined WBR metadata source, but the review is keeping this entry for traceability because it was the highest-risk missing contract in the prior revision.
- Evidence:
  - Architecture Section 6.4 now resolves WBR metadata from `i2oretail.schedule_wbr_details` via `schedule_master`, `organization`, `schedule_details`, and `report`.
  - Architecture Section 8.1 includes the WBR metadata query and states that `latestPeriod` is the last completed Sunday in `YYYY-MM-DD` form.
  - Architecture Section 8.3 reuses the same lookup path and parses `sw.gcs_location` JSON to extract the published GCS URL.
- Impact: The config card can now be rendered deterministically from a single backend lookup path without guessing at table vs. GCS resolution.
- Recommendation: No further action required for the WBR metadata contract.
- Status: `Resolved`

### AR-010
- Severity: `P1`
- Area: Resilience / Operations
- Gap: `marketplace_email_outbox` and backoff settings are defined, but the architecture does not say what component actually executes retries.
- Evidence:
  - Architecture Section 7.2 defines `marketplace_email_outbox`.
  - Architecture Section 10.3 defines retry backoff config.
  - Architecture Section 12.1.1 says transport/5xx failures queue retries, but no scheduler, worker, or poller is specified.
- Impact: Accepted pilot and audit requests can remain stuck in retry state forever if the retry executor is omitted or implemented inconsistently.
- Recommendation: Name the retry executor explicitly, for example a scheduled worker in `i2o-reseller` that polls `marketplace_email_outbox` where `status IN ('PENDING','RETRYING')` and `next_retry_at <= NOW()`.
- Status: `Open`

### AR-011
- Severity: `P1`
- Area: Governance / Delivery Readiness
- Gap: PID disposition is still unresolved. The architecture says implementation approval is blocked until Product Owner either provides the PID path or explicitly signs off that PID is not applicable.
- Evidence:
  - Architecture Section 1.5 marks PID as not found.
  - Architecture Section 10.5 includes PID disposition as a Go/No-Go dependency with `Open` status.
  - Architecture Section 17 repeats the PID disposition as an implementation readiness prerequisite.
- Impact: This is a formal approval blocker, not just a documentation nit. The architecture is not approval-complete until the governance decision is recorded.
- Recommendation: Product Owner must record PID disposition before implementation starts.
- Status: `Open`

### AR-012
- Severity: `P2`
- Area: Observability / KPI Measurement
- Gap: The architecture defines `mo_wbr_download_completed`, but the WBR flow uses a direct published GCS URL. There is no reliable browser-side callback mechanism for completion after the navigation leaves the app.
- Evidence:
  - Architecture Section 12.5 defines `mo_wbr_download_completed`.
  - Architecture Section 6.4 shows the browser navigates directly to the published WBR URL.
- Impact: The completion event is likely to underfire or never fire, which makes the WBR download success metric unreliable.
- Recommendation: Treat `mo_wbr_download_initiated` as the primary metric, or switch completion tracking to server-side GCS access logs if completion must be measured.
- Status: `Open`

## 5. PRD/PID Coverage Matrix

| Requirement ID/Topic | Source | Architecture Coverage | Notes |
|---|---|---|---|
| US001 Active subscriptions + enforcement popup + link gating | PRD | Full | Core card flow, popup, and gating are covered in Sections 6.1, 7.1, 8.1, 9.3. |
| US002 Unsubscribed marketplace ranking + pain levels | PRD | Full | Pain thresholds, ordering contract, cache strategy, and error handling are covered. |
| US003 Brand and enforcement filtering | PRD | Full | Brand filter behavior is defined; enforcement filter scope is present in Section 9.4. |
| US004 WBR download | PRD | Full | Download flow and config-card WBR metadata resolution are now defined through the schedule-table lookup path (AR-009 resolved). |
| US005 Start Free Pilot | PRD | Full | Duplicate prevention, failure semantics, and retry behavior are documented. |
| US006 Request Audit Report | PRD | Full | Duplicate audit behavior and retry semantics are documented. |
| US007 Audit sample download | PRD | Full | One-click guard and signed URL download are covered. |
| US009 Navigation links | PRD | Full | `ui_config` screen gates and route mapping are explicit. |
| Success metrics / observability | PRD | Partial | KPI plan exists, but WBR completion tracking is not reliable as written (AR-012). |
| PID baseline | PID | Missing | PID file not provided; disposition still pending (AR-011). |

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks:
  - The retry queue has no specified executor, so the failure recovery path is incomplete even though the table and backoff settings exist.
- Integration and dependency risks:
  - GCP bucket paths, legacy mapping contract, `ui_config` screen-enablement contract, and email trigger validation remain release gates in Section 10.5.
  - PID is still open and blocks formal approval.
- Non-functional readiness risks:
  - Direct published-URL downloads make `mo_wbr_download_completed` hard to measure reliably.
- Rollout and operations risks:
  - The deployment checklist is good, but production promotion is still gated on several open items. Until those are closed, the architecture is not deployment-ready.

## 7. Open Questions and Assumptions

1. What process executes `marketplace_email_outbox` retries?
2. Will Product Owner provide PID disposition or explicitly mark PID as not applicable?
3. Is `mo_wbr_download_completed` expected to be approximate, or should it be replaced with a server-side metric?

## 8. Approval Log

- Current approval status: `Rejected`
- Approval date: `N/A`
- Approved by: `N/A`
- Approval conditions:
  - Resolve AR-010 before implementation starts.
  - Resolve AR-011 before architecture approval.
  - Revisit AR-012 before KPI sign-off.
