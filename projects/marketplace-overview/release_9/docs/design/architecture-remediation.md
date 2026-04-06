# Architecture Remediation Report - Marketplace Overview (release_9)

- Project: `marketplace-overview`
- Release: `release_9`
- Remediation Date: `2026-04-06`
- Source Review: `projects/marketplace-overview/release_9/docs/design/architecture-review.md` (`v4`)
- Updated Architecture: `projects/marketplace-overview/release_9/docs/design/architecture.md` (`v1.5`)

## 1. Summary by Severity

| Severity | Findings | Resolved | Open | Deferred | Cannot Resolve |
|---|---:|---:|---:|---:|---:|
| P1 | 3 | 1 | 1 | 1 | 0 |
| P2 | 1 | 0 | 1 | 0 | 0 |
| P3 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **4** | **1** | **2** | **1** | **0** |

## 2. Finding-to-Change Matrix

| Finding ID | Severity | Status (Before) | Affected Area | Recommendation | `architecture.md` Target Section | Planned Change | Acceptance Check | Status (After) | Evidence (Updated Section/Quote) | Owner | Notes / Blockers |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AR-009 | P1 | Open | Data Contract / API Specification | Define the WBR metadata source and lookup path explicitly | 6.4, 8.1, 8.3, 1.4 | Add canonical `schedule_wbr_details` lookup, period derivation, and `sw.gcs_location` JSON parsing for `wbrInfo.latestDate` and download target | Section includes the exact SQL join path, `latestPeriod` derivation, and JSON parsing rule | Resolved | Section 6.4 now resolves WBR metadata via `schedule_wbr_details`; Section 8.1 includes the query; Section 8.3 reuses the same lookup path | Backend Lead | None |
| AR-010 | P1 | Open | Resilience / Operations | Name the retry executor explicitly | 7.2, 10.3, 12.1.1 | Add a scheduled worker or poller in `i2o-reseller` that drains `marketplace_email_outbox` for `PENDING` / `RETRYING` rows | Section names the executor, polling cadence, and retry-state transition rules | Open | No retry executor is defined yet | Backend Lead + Platform Team | Implementation decision still pending |
| AR-011 | P1 | Open | Governance / Delivery Readiness | Provide PID path or explicit not-applicable sign-off | 1.5, 10.5, 17 | Record PID disposition in the architecture approval log | Section contains the PID path or a product sign-off that PID is not applicable | Deferred | PID remains not found; approval is still blocked on Product Owner disposition | Product Owner | External decision required |
| AR-012 | P2 | Open | Observability / KPI Measurement | Treat WBR completion as approximate or switch to server-side tracking | 6.4, 12.5 | Either document `mo_wbr_download_completed` as best-effort or replace it with server-side GCS access-log confirmation | Section defines a reliable completion signal or removes the inaccurate metric | Open | Current WBR flow still uses direct published URL navigation, so browser-side completion remains weak | Product Analytics + Backend Lead | Lowers metric fidelity, but does not block basic flow approval |

## 3. Unresolved / Deferred Items

| Finding ID | Severity | Disposition | Owner | Blocking Decision | Target Date |
|---|---|---|---|---|---|
| AR-010 | P1 | Open | Backend Lead + Platform Team | Confirm the retry executor that polls `marketplace_email_outbox` and drains retryable failures | 2026-04-08 |
| AR-011 | P1 | Deferred | Product Owner | Provide PID path in repo or approve explicit statement: "PID not applicable for release_9" | 2026-04-10 |
| AR-012 | P2 | Open | Product Analytics + Backend Lead | Decide whether WBR completion is approximate or needs server-side confirmation | 2026-04-11 |

## 4. Validation Notes for Resolved Findings

- AR-009 is resolved by the new canonical WBR query in Section 8.1 and the matching runtime flow in Section 6.4.
- The backend now derives `latestPeriod` as the most recent Sunday date and uses `sw.gcs_location` JSON as the download source, so the config API has a deterministic WBR lookup path.

## 5. Approval Readiness

Architecture is **not approval-ready** yet.

Remaining blockers:
1. AR-010 still lacks a concrete retry executor.
2. AR-011 still lacks PID disposition from Product Owner.

Non-blocking but still open:
1. AR-012 should be resolved before KPI sign-off because WBR completion tracking is still approximate.
