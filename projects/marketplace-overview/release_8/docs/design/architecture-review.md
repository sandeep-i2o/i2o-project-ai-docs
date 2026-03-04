# Marketplace Overview Architecture Review

## 1. Review Metadata

- Project: `marketplace-overview`
- Release: `release_8`
- Reviewer: `Codex`
- Date: `2026-03-04`
- Source docs:
  - `projects/marketplace-overview/release_8/docs/design/architecture.md`
  - `projects/marketplace-overview/release_8/docs/requirements/prd.md`
  - `pid.md` not reviewed (explicitly skipped per user instruction)

## 2. Executive Verdict

- Overall status: `Rejected`
- Feasibility summary: The architecture is close to implementable, but it contains one security/data-isolation blocker and multiple high-risk contract inconsistencies. As written, teams can implement incompatible APIs and still fail acceptance criteria around table behavior and trial email handling.
- Highest-risk area: Tenant isolation is internally inconsistent (declared `org_id` filtering without `org_id` in the snapshot schema/query contract).

## 3. Severity Summary

- `P0` count: `1`
- `P1` count: `3`
- `P2` count: `2`
- `P3` count: `1`

## 4. Findings (Ordered by Severity)

### AR-001
- Severity: `P0`
- Area: `Security / Multi-tenant Data Isolation`
- Gap: The document promises tenant isolation via `org_id`, but the proposed sink schema and runtime query path do not carry `org_id`.
- Evidence:
  - Architecture security claim: all BQ queries filtered by `org_id` (`architecture.md:616`).
  - Runtime query filters only `brand_id`, `region`, `week_start` (`architecture.md:203-205`).
  - Proposed sink table omits `org_id` column (`architecture.md:282-309`).
- Impact: Data leakage risk across tenants, compliance exposure, and inability to prove isolation controls.
- Recommendation: Add `org_id` as mandatory key column in `marketplace_kpi_weekly_snapshot`, enforce it in scheduler writes and all read queries, and add integration tests for cross-tenant isolation.
- Status: `Open`

### AR-002
- Severity: `P1`
- Area: `API Contract`
- Gap: Data API strategy is contradictory.
- Evidence:
  - Architecture states no new data-fetch endpoint; reuse `getCardData/getGridCardData` (`architecture.md:37`, `architecture.md:89-90`, `architecture.md:176`).
  - Runtime view still defines `GET /marketplace-overview/data` returning cards+table (`architecture.md:197-208`).
- Impact: Frontend/backend implementation drift, integration churn, and schedule slippage.
- Recommendation: Choose one contract, remove the conflicting flow, and freeze request/response schemas.
- Status: `Open`

### AR-003
- Severity: `P1`
- Area: `Trial Workflow Correctness`
- Gap: Multi-brand Initiate Trial rule is only enforced in frontend behavior, not backend contract.
- Evidence:
  - PRD requires explicit brand disambiguation when multiple brands are selected (`prd.md:612-614`) and calls out this rule in business logic (`prd.md:570-572`).
  - Architecture only states “frontend prompts user” (`architecture.md:573`) and endpoint accepts direct `brandId/brandName` payload (`architecture.md:434-440`) with no backend ambiguity check.
- Impact: Wrong-brand trial emails can be triggered by buggy clients or non-UI callers.
- Recommendation: Server-side enforce single-brand context, derive `brandName` from authoritative data, reject ambiguous requests (`400`), and make endpoint idempotent.
- Status: `Open`

### AR-004
- Severity: `P1`
- Area: `Delivery Readiness`
- Gap: “Implementation-ready” verdict conflicts with explicitly unresolved hard dependency.
- Evidence:
  - Architecture claims implementation readiness and high confidence (`architecture.md:684`).
  - Open item says component registration is high risk and required before frontend integration (`architecture.md:693`).
  - PRD timeline is tight with dependency sequencing (`prd.md:722-733`).
- Impact: Teams can start build on a false readiness signal and get blocked late during integration.
- Recommendation: Convert unresolved dependencies into explicit go/no-go gates with owners, due dates, and migration steps by environment.
- Status: `Open`

### AR-005
- Severity: `P2`
- Area: `Reliability / Operations`
- Gap: Stale-data behavior exists, but operational detection/alerting and failure recovery are not specified.
- Evidence:
  - PRD requires stale indicator when weekly aggregation fails (`prd.md:695-697`) and highlights delayed pipeline behavior (`prd.md:669-670`).
  - Architecture only defines response behavior (`dataStalenessFlag`) (`architecture.md:569`) without monitoring/retry/runbook details.
- Impact: Prolonged stale KPI exposure without alerting; correctness objective degraded.
- Recommendation: Add scheduler run audit table, alert thresholds, retry/backoff policy, and on-call runbook.
- Status: `Open`

### AR-006
- Severity: `P2`
- Area: `Functional Acceptance Alignment (US004)`
- Gap: Table defaults in architecture do not match PRD business rules.
- Evidence:
  - PRD requires default alphabetical sort and 10 rows/page (`prd.md:482-487`).
  - API example sets `pageSize: 50` and no default sort contract (`architecture.md:401-407`).
- Impact: AC failures and avoidable UX/test rework.
- Recommendation: Set default sort `marketplace ASC` and default page size `10` in API/UI contracts.
- Status: `Open`

### AR-007
- Severity: `P3`
- Area: `Data Semantics / KPI Definition`
- Gap: Source tables are listed, but metric-level transformation rules (formula, precedence, null/zero policy per KPI) are not formalized.
- Evidence:
  - PRD expects cross-module KPI correctness and aggregation (`prd.md:339-341`).
  - Architecture lists sources but not deterministic KPI mapping formulas (`architecture.md:269-277`).
- Impact: KPI drift between card/table and between teams over time.
- Recommendation: Add a KPI mapping appendix with exact formulas, units, and null/zero handling.
- Status: `Open`

## 5. PRD/PID Coverage Matrix

| Requirement ID/Topic | Source | Architecture Coverage | Notes |
|---|---|---|---|
| US001: Tab visibility + BP gating + default state | PRD | Full | Route, guard, and default filter are described (`architecture.md:473-479`, `architecture.md:533-539`). |
| US002: Brand/region/date filters + view toggle retention | PRD | Full | Filter bar + state pattern sufficiently covers behavior (`architecture.md:508-513`, `architecture.md:489-500`). |
| US003: Card view activation states + KPI grouping | PRD | Partial | Structure is present; trial KPI data readiness still unresolved (`architecture.md:356-364`, `architecture.md:696`). |
| US004: Table parity, N/A handling, pagination/sort defaults | PRD | Partial | N/A handling covered; default sort/page-size misaligned (AR-006). |
| US005: Initiate Trial email + multi-brand handling | PRD | Partial | Endpoint exists; backend enforcement for multi-brand ambiguity is missing (AR-003). |
| US006: Weekly refresh + stale indicator | PRD | Partial | Refresh/stale flag defined; missing operational controls (AR-005). |
| Security: Tenant isolation | Architecture quality goal / PRD context | Conflicting | Claimed via `org_id`, but schema/query path omits it (AR-001). |
| Performance: P95 < 3s | Architecture | Partial | Target stated, but no load model/SLO validation plan. |
| Availability: 99.5% | Architecture | Partial | Objective stated; no concrete monitoring/error-budget design. |
| PID coverage | PID | Missing (intentionally skipped) | Excluded per user instruction for this review cycle. |

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks:
  - Multi-tenant isolation contract is not implementable as documented (P0).
  - API contract ambiguity can produce incompatible implementations (P1).
- Integration/dependency risks:
  - Component/query configuration dependency is unresolved but required before UI integration.
  - Master-data schema existence/migration for `org_marketplace_config` is still an assumption.
- Non-functional readiness risks:
  - Reliability/observability design is under-specified for stale-data and scheduler failures.
  - Performance/availability goals are declarative without explicit verification criteria.
- Rollout/migration/operations risks:
  - No explicit cutover/backfill/runbook sequence tied to release gates.

## 7. Open Questions and Assumptions

- Decision needed: Will data retrieval strictly use existing `getCardData/getGridCardData`, or will a new `GET /marketplace-overview/data` endpoint be introduced?
- Decision needed: Is `brand_id` globally tenant-safe, or must `org_id` be added to the snapshot primary access pattern?
- Decision needed: Should backend reject Initiate Trial requests when multiple brands are selected, or is frontend-only enforcement acceptable?
- Assumption currently made in architecture: `org_marketplace_config` either exists or can be added without release risk.

## 8. Approval Log

- Current approval status: `Not Approved`
- Approval date: `N/A`
- Approved by: `N/A`
- Approval conditions:
  - Resolve AR-001 (P0) before any approval.
  - Resolve AR-002, AR-003, AR-004 (P1) before conditional approval.

