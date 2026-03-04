# Architecture Remediation Report

**Date:** 2026-03-03
**Project:** sales_insights
**Version:** 1.1.0

## Executive Summary
This document confirms the remediation actions taken in response to the `architecture-review.md` dated 2026-03-01. Structural gaps, conflicting constraints, and missing failure states have been addressed directly within `architecture.md`. 

The architecture is now considered **Conditionally Approved**, pending the submission of `pid.md` (AR-006).

### Severity Resolution Summary
* **P0 Findings:** 1 of 1 Resolved
* **P1 Findings:** 4 of 5 Resolved (1 Blocked by missing PID)
* **P2 Findings:** 2 of 2 Resolved
* **P3 Findings:** 1 of 1 Resolved

---

## Finding-to-Fix Matrix

### AR-001 (P0): Historical FX Bootstrap Missing
* **Status:** `Resolved`
* **Changes Made:** Added Section `6.3.1 Scenario: Historical FX & Sales Data Bootstrap`. Defined `EcbHistoricalBootstrapTask` for 12-month bulk payloads. Added localized 12-month backfill to `qa`/`uat` environment configuration. Included explicit Go-Live gate in the Rollout section validating 100% correlation.

### AR-002 (P1): Feed Contract and Ownership Underspecified
* **Status:** `Resolved`
* **Changes Made:** Updated `6.3 Scenario: CSV Sales Data Ingestion & Bootstrap` with a Data Contracts & Constraints section. Officially pegged CSV format to `knowledge/bigquery_schemas/sales_data_schema.md`. Assigned extractor ownership to Data Platform. Added `/api/admin/replay-ingestion` endpoint for idempotent replay.

### AR-003 (P1): Currency Fallback PRD Conflict
* **Status:** `Resolved`
* **Changes Made:** Updated Section `8.5 Currency Conversion Pattern`. Removed HTTP 422 behavior. Implemented the PRD corner-case fallback. The API now returns `{"fallback": true, "fallback_currency": "EUR"}`. 

### AR-004 (P1): Large CSV Export Fallback Missing
* **Status:** `Resolved`
* **Changes Made:** Rewrote sequence diagram `6.4 Scenario: CSV Export`. Removed the synchronous file stream. Replaced with an `@Async` background process that chunks data to a temporary Google Cloud Storage bucket and triggers a SendGrid email with a signed download URL. 

### AR-005 (P1): Scope Constraints Inconsistencies
* **Status:** `Resolved`
* **Changes Made:** Corrected Section 2 (Constraints). Rather than strictly mandating "no new APIs", the text now accurately states the intention: establishing a decoupled bounded context via `sales-insights-api` on the Java 17 / Spring Boot 3.x stack, dropping the legacy boundary conflict.

### AR-006 (P1): PID Missing
* **Status:** `Cannot Resolve (Blocked)`
* **Validation Notes:** The Project Initiation Document (PID) was not present in the workspace. The architecture review requires it for final delivery governance checks.
* **Owner:** Sandeep (PM) requires to generate the PID using `/generate-pid`.

### AR-007 (P2): Success Metric Instrumentation Incomplete
* **Status:** `Resolved`
* **Changes Made:** Expanded Section `8.3 Logging & Observability`. Appended `Custom PRD Telemetry` block defining explicit extraction of `report_generation_duration_ms` (for the <5s load constraint) and `unique_weekly_users` (for the 100% adoption metrics).

### AR-008 (P2): Initial Backfill and Cutover Not Defined
* **Status:** `Resolved`
* **Changes Made:** Added Section `7.3 Data Readiness & Rollout Sequence`. Specified exactly how Flyway schema initialization precedes 13 months of historical data ingestion. Declared a strict data-readiness QA gate ensuring zero missing days prior to accepting live user traffic.

### AR-009 (P3): Deprecated Frontend Tests (Protractor)
* **Status:** `Resolved`
* **Changes Made:** Updated Section `12. Next Steps > Sprint 2 > Step 8`. Swapped references from Protractor to `Playwright`, bringing the E2E architecture in-line with modern standard support.

---

## Open Risks and Blockers

1. **AR-006 is blocking final approval:** The implementation strategy is technically validated and feasible, but program governance is pending until `pid.md` is compiled. Once compiled, a brief re-validation of AR-006 will move the architecture to full "Approved" status.
