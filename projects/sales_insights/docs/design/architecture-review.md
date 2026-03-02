## 1. Review Metadata

- Project: `sales_insights`
- Reviewer: `Codex`
- Date: `2026-03-01`
- Source docs:
  - `projects/sales_insights/docs/design/architecture.md`
  - `projects/sales_insights/docs/requirements/prd.md`
  - `pid.md` not provided for this review cycle

## 2. Executive Verdict

- Overall status: `Rejected`
- Feasibility summary: The architecture direction is mostly coherent (scheduler extension, dedicated API service, Angular module, materialized-view performance strategy), but it is not implementation-safe for approval in its current form. A launch-blocking gap exists around historical FX data readiness for LY calculations, and multiple high-risk requirement mismatches remain unresolved (currency fallback behavior, large-export handling, upstream data-contract readiness, and scope/constraint inconsistency). Without resolving these items, acceptance criteria for US002/US003 and launch reliability are at high risk.
- Highest-risk area: Day-1 data correctness for LY and multi-currency analytics due to missing historical FX/backfill strategy.

## 3. Severity Summary

- `P0` count: 1
- `P1` count: 5
- `P2` count: 3
- `P3` count: 1

## 4. Findings (Ordered by Severity)

### AR-001
- Severity: `P0`
- Area: `Data Model / FX Ingestion`
- Gap: Historical FX backfill strategy is missing, but LY comparisons are required at launch.
- Evidence:
  - PRD reference: `B5 In Scope` requires historical exchange-rate ingestion; US002 requires LY metrics and AC2 validation against previous-year week (`prd.md`:57, 154-155, 180).
  - Architecture reference: Only daily pull from `eurofxref-daily.xml` and daily CRON ingestion are defined; no bootstrap/backfill path is described (`architecture.md`:96, 262, 299-320).
- Impact: LY values and back-dated conversions cannot be trusted at go-live; US002 acceptance criteria are not realistically satisfiable.
- Recommendation: Add an explicit historical FX bootstrap design (source endpoint, date range, idempotent replay, reconciliation checks, and cutoff policy) before implementation approval.
- Status: `Open`

### AR-002
- Severity: `P1`
- Area: `External Dependencies / Data Contracts`
- Gap: Marketplace feed contract and operational ownership are underspecified.
- Evidence:
  - PRD reference: Known blocker is access/stability of regional feeds; release show-stopper calls schema normalization risk (`prd.md`:21, 264).
  - Architecture reference: `CsvIngestionTask` assumes GCS files and schema normalization, but no producer SLA, schema version contract, quarantine/replay policy, or ownership model is defined (`architecture.md`:97, 205, 322-341, 531-532).
- Impact: High probability of ingestion failures, silent data drift, and rework during UAT.
- Recommendation: Define feed contracts (schema/versioning), ownership RACI, late/partial file handling, reconciliation reports, and replay procedures.
- Status: `Open`

### AR-003
- Severity: `P1`
- Area: `Requirements Consistency / API Behavior`
- Gap: Unsupported-currency behavior is conflicting between PRD and architecture.
- Evidence:
  - PRD reference: US002 business rule says return error `Currency Not Supported`, but corner-case handling says fallback to EUR with notification (`prd.md`:159, 167).
  - Architecture reference: API behavior fixed to HTTP 422 `Currency Not Supported` (`architecture.md`:462).
- Impact: Product acceptance ambiguity; FE/API behavior can fail UAT depending on which PRD statement QA enforces.
- Recommendation: Product and engineering must choose one behavior, update PRD + AC, and align API contract and UX copy.
- Status: `Open`

### AR-004
- Severity: `P1`
- Area: `Export Architecture / Scalability`
- Gap: Large CSV export fallback path is not architected.
- Evidence:
  - PRD reference: For large exports, expected behavior allows paginated export or server-side async/email workflow (`prd.md`:234).
  - Architecture reference: Runtime defines synchronous streamed CSV only; no async export pipeline/storage/notification path (`architecture.md`:343-356, 518).
- Impact: Exports for large filtered datasets are likely to timeout or degrade API responsiveness.
- Recommendation: Add async export design (job queue, object storage, notification callback/email, retention policy).
- Status: `Open`

### AR-005
- Severity: `P1`
- Area: `Architecture Governance / Scope Definition`
- Gap: Constraint and solution strategy are internally inconsistent on service topology.
- Evidence:
  - Architecture constraint says existing services must be reused and lists extension model (`architecture.md`:57).
  - Strategy and ADR-002 introduce a new `sales-insights-api` service/repo (`architecture.md`:115, 139, 473-476).
- Impact: Confused implementation scope, approval friction with platform/security review, and planning churn.
- Recommendation: Reconcile constraints text with intended topology and explicitly separate “new service” from “new infrastructure” to remove ambiguity.
- Status: `Open`

### AR-006
- Severity: `P1`
- Area: `Program Governance / Completeness`
- Gap: PID artifact is missing for this review, so delivery feasibility cannot be fully validated.
- Evidence:
  - Review input requirement includes PID coverage for dependency/governance checks.
  - No `pid.md` (or equivalent) exists in the project docs; review proceeded on architecture + PRD only.
- Impact: Approval lacks evidence for staffing assumptions, dependency commitments, budget/timeline realism, and decision ownership.
- Recommendation: Provide PID and rerun the review for final approval.
- Status: `Open`

### AR-007
- Severity: `P2`
- Area: `Observability / Success Measurement`
- Gap: Success-metric instrumentation is incomplete for PRD goals.
- Evidence:
  - PRD reference: Success metrics include reporting turnaround `<5s`, adoption `100%`, and dashboard latency `<200ms P95` (`prd.md`:49-51).
  - Architecture reference: Monitoring lists API latency/freshness/ingestion but not adoption telemetry or explicit report-turnaround measurement definition (`architecture.md`:437-439).
- Impact: Launch success cannot be objectively demonstrated against PRD commitments.
- Recommendation: Define telemetry events and owners for adoption, report-generation timing, and end-to-end page-load RUM.
- Status: `Open`

### AR-008
- Severity: `P2`
- Area: `Data Readiness / Rollout`
- Gap: Initial sales-history backfill and cutover plan are not defined.
- Evidence:
  - PRD reference: Unified dashboard and LY comparison imply immediate historical context (`prd.md`:154-155, 180).
  - Architecture reference: CSV ingestion scenario is daily forward ingestion (`date=today`) with no explicit bootstrap/cutover/reconciliation sequence (`architecture.md`:333, 568-584).
- Impact: Day-1 dashboard can launch with partial history, undermining trust and comparison accuracy.
- Recommendation: Add rollout plan with historical load window, reconciliation checks, and go-live data readiness gates.
- Status: `Open`

### AR-009
- Severity: `P3`
- Area: `Quality / Technical Debt`
- Gap: Frontend test strategy references deprecated tooling and is not aligned to modern stack.
- Evidence:
  - Architecture next steps call out E2E testing with Protractor (`architecture.md`:583).
- Impact: Lower maintainability and avoidable test pipeline fragility.
- Recommendation: Replace with supported E2E framework and update quality gate definitions.
- Status: `Open`

## 5. PRD/PID Coverage Matrix

| Requirement ID/Topic | Source | Architecture Coverage | Notes |
|---|---|---|---|
| Daily ECB ingestion at 16:30 CET | PRD US001 | Full | Covered by `EcbIngestionTask` + Cloud Scheduler flow. |
| Retry/fallback for ECB outages | PRD US001 | Full | Retry x3 + last-known-rate + alert are documented. |
| XML validation + duplicate UPSERT + outlier check | PRD US001 | Full | Explicit in ingestion algorithm and runtime scenario. |
| Historical FX availability for LY/use-at-launch | PRD B5, US002 | Missing | No historical bootstrap strategy; daily feed only. |
| Multi-region filtering + currency conversion | PRD US002 | Full | Controller/service/DAO pipeline and conversion pattern defined. |
| 200ms response target | PRD US002, B4 | Partial | API-level target is defined; end-to-end page-load proof plan is weak. |
| Daily/Weekly/Monthly/Quarterly granularity | PRD B5 | Partial | Granularity is modeled, but materialized-view design is described mainly as daily pre-aggregation. |
| Unsupported currency behavior | PRD US002 | Conflicting | PRD itself conflicts; architecture picks HTTP 422 path. |
| Unauthorized region access filtering | PRD US002 | Full | Region-level RBAC via JWT claims is defined. |
| Stale data indicator (>24h delayed feed) | PRD US002 | Full | API stale flag and FE stale badge are defined. |
| Rapid filter interactions (debounce/cancel) | PRD US002 | Full | RxJS debounce + `switchMap` cancel is defined. |
| Dashboard chart + AG Grid virtualization (10k+) | PRD US003 | Full | ECharts + AG Grid Enterprise + virtualization covered. |
| Large export fallback (async/email or paging) | PRD US003 | Partial | Only synchronous stream path is defined; async fallback missing. |
| Session expiry with saved filter state | PRD US003 | Partial | Auth flow is covered, but explicit filter-state persistence on expiry is not described. |
| PID-driven delivery dependencies and governance | PID | Missing | PID file not available; governance traceability incomplete. |

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks:
  - Historical FX and sales backfill are not designed, yet LY accuracy is a launch requirement.
  - Export strategy lacks a robust large-dataset path.
- Integration/dependency risks:
  - Upstream regional feed contract, ownership, and SLA details are missing.
  - Constraint/solution inconsistency can stall platform/security approvals.
- Non-functional readiness risks:
  - Success metrics are not fully instrumented (especially adoption and end-to-end reporting turnaround).
  - Latency guarantees are stronger at API-level than at user-experience level.
- Rollout/migration/operations risks:
  - No explicit cutover and data-readiness gates for day-1 launch quality.
  - Without PID, key delivery assumptions (dependencies, schedule confidence, escalation path) are unverified.

## 7. Open Questions and Assumptions

- `Assumption:` Team will provide a PID in the next review cycle; final approval is blocked until then.
- `Question:` What is the authoritative source and date range for historical FX backfill (ECB historical XML/API variant), and who owns reconciliation sign-off?
- `Question:` Which unsupported-currency behavior is correct for MVP: fallback-to-EUR or hard error?
- `Question:` For large exports, should the MVP include asynchronous export + notification, or should PRD acceptance criteria be narrowed?
- `Question:` What is the agreed historical sales backfill window needed before UAT (e.g., 12 months minimum for LY)?

## 8. Approval Log

- Current approval status: `Rejected`
- Approval date: `2026-03-01`
- Approved by: `N/A`
- Approval conditions (if any):
  - Resolve `AR-001` (P0) and all open `P1` findings.
  - Provide PID and rerun architecture review for final approval.
