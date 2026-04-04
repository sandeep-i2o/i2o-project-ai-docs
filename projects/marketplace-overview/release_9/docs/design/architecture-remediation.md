# Architecture Remediation Report - Marketplace Overview (release_9)

- Project: `marketplace-overview`
- Release: `release_9`
- Remediation Date: `2026-04-04`
- Source Review: `projects/marketplace-overview/release_9/docs/design/architecture-review.md`
- Updated Architecture: `projects/marketplace-overview/release_9/docs/design/architecture.md`

## 1. Summary by Severity

| Severity | Findings | Resolved | Partially Resolved | Deferred | Cannot Resolve |
|---|---:|---:|---:|---:|---:|
| P0 | 1 | 1 | 0 | 0 | 0 |
| P1 | 3 | 2 | 0 | 1 | 0 |
| P2 | 4 | 4 | 0 | 0 | 0 |
| P3 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **8** | **7** | **0** | **1** | **0** |

## 2. Finding-to-Change Matrix

| Finding ID | Severity | Status (Before) | Affected Area | Recommendation | `architecture.md` Target Section | Planned Change | Acceptance Check | Status (After) | Evidence (Updated Section/Quote) | Owner | Notes/Blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AR-001 | P0 | Open | Functional Coverage - Filtering | Align canonical brand filter behavior across all cards | 4.1, 6.1, 7.2, 7.4, 8.2, 9.4 | Make unsubscribed data brand-aware end-to-end: brand-level cache schema, brand-filter query contract, aggregation by selected brands | Section defines API contract + data model + runtime behavior where same brand filter affects both columns | Resolved | 9.4: "Both columns update... unsubscribed cards recompute totals only for selected brands"; 8.2 includes `appliedBrandIds`; 7.2 cache now includes `brand_id` | Backend Lead | None |
| AR-002 | P1 | Open | Requirement Clarity / Failure Handling | Resolve contradictory pilot/audit email failure behavior with error-class decision table | 8.4, 8.5, 12.1, 12.1.1 | Add authoritative failure matrix by class (validation/auth vs sync transport/5xx vs async delivery) + explicit 202 queued response contract + retry outbox design | Section includes failure class, API behavior, UI behavior, and retry ownership | Resolved | 12.1.1 decision table and 8.4/8.5 `202 Accepted` (`deliveryState: "QUEUED_RETRY"`) | Backend Lead + Platform Team | None |
| AR-003 | P1 | Open | Dependency & Integration Readiness | Add explicit go/no-go checklist with owner, due date, fallback; gate promotion | 10.5, 17 | Create dependency checklist with owner/due date/go-no-go/fallback and explicit promotion block rule | Checklist includes owner, date, fallback, and promotion gate criteria | Resolved | 10.5 table includes owner/due date/fallback and "Promotion rule... deployment to production is rejected" | Engineering Manager | Dependency items remain operationally open, but architecture control model is now defined |
| AR-004 | P1 | Open | Review Scope Completeness | Provide PID path or explicit not-applicable decision | 1.5, 10.5, 17 | Record current PID absence and add mandatory Product Owner disposition gate | Section clearly identifies PID state, owner, and decision required before approval | Deferred | 1.5 PID row: "Not found... Pending product decision"; 10.5 includes PID go/no-go row | Product Owner | Blocking external decision: PID file path or explicit "not applicable" sign-off is still pending |
| AR-005 | P2 | Open | Functional Edge-Case Coverage | Define deterministic alphabetical tie-break for equal reseller counts | 6.1, 8.2, 9.2 | Add deterministic ordering contract (`total_resellers DESC, marketplace_name ASC`) in runtime + API + UI hierarchy notes | Section explicitly states tie-break sort rule | Resolved | 8.2: "ORDER BY total_resellers DESC, marketplace_name ASC"; 9.2 includes same tiebreak behavior | Backend Lead | None |
| AR-006 | P2 | Open | UI Interaction Contract | Align audit sample rapid-click behavior with debounce/guard | 8.6, 12.2 | Replace "no duplicate prevention" with one-click guard behavior and timing | Section specifies duplicate prevention behavior and guard lifecycle | Resolved | 12.2: "Audit Sample download | One-click guard..." and 8.6 frontend guard note | Frontend Lead | None |
| AR-007 | P2 | Open | Business Observability | Add analytics event schema, dashboard ownership, and review cadence | 12.4, 12.5, 17 | Add KPI event contract (names/dimensions), ownership, cadence, and launch gate | Section defines event names, required dimensions, dashboard owner, cadence | Resolved | 12.5 event table (`mo_screen_viewed`, `mo_pilot_requested`, etc.) + owner/cadence + release gate | Product Analytics | None |
| AR-008 | P2 | Open | Decision Traceability | Remove broken ADR references or provide ADR evidence | 15 | Replace broken file links with inline ADR records including rationale/consequence | Section contains auditable ADR records without broken links | Resolved | 15 now has inline ADR table (ADR-001 to ADR-004) and no `ADR/...` file references | Tech Lead | None |

## 3. Unresolved / Deferred Items

| Finding ID | Severity | Disposition | Owner | Blocking Decision | Target Date |
|---|---|---|---|---|---|
| AR-004 | P1 | Deferred | Product Owner | Provide PID path in repo or approve explicit statement: "PID not applicable for release_9" | 2026-04-10 |

## 4. Validation Notes for Resolved Findings

- AR-001 validated by consistent contract across runtime (6.1), data schema (7.2/7.4), API (8.2), and UI filter behavior (9.4).
- AR-002 validated by class-based failure table (12.1.1) and explicit API examples for queued-retry responses in 8.4/8.5.
- AR-003 validated by dependency gate table with owners/due dates/fallbacks and CI/CD promotion blocking rule in 10.5.
- AR-005 validated by explicit deterministic ordering contract in API spec and mirrored UI hierarchy expectation.
- AR-006 validated by replacing the prior non-guard behavior with one-click guard policy.
- AR-007 validated by event schema and dashboard ownership/cadence mapped to PRD success metrics.
- AR-008 validated by replacing broken ADR links with inline ADR records.

## 5. Approval Readiness

Architecture is **not approval-ready** yet because one P1 finding (AR-004) remains deferred pending Product Owner decision on PID applicability/path.

Required stakeholder decision:
1. Product Owner must confirm one of:
   - PID path for `release_9`, or
   - signed statement that PID is not applicable for this release.
