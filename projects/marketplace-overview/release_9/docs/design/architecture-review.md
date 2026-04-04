# Architecture Review - Marketplace Overview (release_9)

## 1. Review Metadata

- Project: `marketplace-overview`
- Reviewer: `AI Agent`
- Date: `2026-04-03`
- Source docs:
  - `projects/marketplace-overview/release_9/docs/design/architecture.md`
  - `projects/marketplace-overview/release_9/docs/requirements/prd.md`
  - `PID`: Not found under `projects/marketplace-overview/release_9/docs`

## 2. Executive Verdict

- Overall status: `Rejected`
- Feasibility summary: The architecture is structurally strong and covers most module-level implementation concerns, but it contains one direct conflict with a P0 PRD requirement and multiple unresolved delivery risks tied to external dependencies and ambiguous failure semantics. Because P0/P1 items remain open, this design should not be approved for implementation as-is.
- Highest-risk area: Brand filter behavior for unsubscribed marketplaces conflicts with US003 acceptance intent and can fail P0 scope.

## 3. Severity Summary

- `P0` count: `1`
- `P1` count: `3`
- `P2` count: `4`
- `P3` count: `0`

## 4. Findings (Ordered by Severity)

### AR-001
- Severity: `P0`
- Area: `Functional Coverage - Filtering`
- Gap: Architecture states the brand filter does not affect unsubscribed marketplace cards, but PRD US003 requires filtered behavior across all cards.
- Evidence:
  - PRD: US003 corner case says both columns reflect selected brand (`requirements/prd.md:299`), and AC says "Only Denon-related data shown across all cards" (`requirements/prd.md:317`)
  - Architecture: Filter behavior says "unsubscribed cards unchanged" (`design/architecture.md:1080`)
- Impact: Critical requirement miss for P0 story; likely QA failure and rework across API, cache keying, and UI behavior.
- Recommendation: Decide canonical behavior and update architecture/API contracts accordingly. If PRD intent stands, make unsubscribed endpoint/filter semantics brand-aware and define cache strategy for brand-filtered responses.
- Status: `Open`

### AR-002
- Severity: `P1`
- Area: `Requirement Clarity / Failure Handling`
- Gap: Pilot and audit email failure behavior is contradictory in PRD and not reconciled with a final authoritative rule.
- Evidence:
  - PRD includes both "show error + allow retry" (`requirements/prd.md:434`, `requirements/prd.md:498`, FAQ `requirements/prd.md:761`) and "show success + queue retry silently" (`requirements/prd.md:439`, `requirements/prd.md:503`)
  - Architecture chooses one behavior ("return error to user ... allow retry") (`design/architecture.md:1209`) without explicit resolution note against contradictory PRD rows
- Impact: Inconsistent UX, test ambiguity, and potential production behavior drift between frontend and backend.
- Recommendation: Resolve failure-mode decision table by error class (sync 4xx/5xx, transport timeout, async delivery failure). Record final behavior in PRD and architecture.
- Status: `Open`

### AR-003
- Severity: `P1`
- Area: `Dependency & Integration Readiness`
- Gap: External dependencies that directly gate MVP flows remain open without owners/dates in the architecture approval gate.
- Evidence:
  - PRD show stoppers: GCP bucket URLs + subscription config API availability + email trigger readiness (`requirements/prd.md:690-700`)
  - Architecture risks/open items list same dependencies (`design/architecture.md:1321`, `design/architecture.md:1324`, `design/architecture.md:1360`)
- Impact: High schedule risk to April release; core stories US002/US004/US005/US006/US007 can slip or ship with partial behavior.
- Recommendation: Add explicit go/no-go checklist with owner, due date, and fallback per dependency; gate environment promotion on checklist completion.
- Status: `Open`

### AR-004
- Severity: `P1`
- Area: `Review Scope Completeness`
- Gap: PID document is missing, so PRD/PID-to-architecture traceability is incomplete.
- Evidence:
  - Skill requires PRD/PID-based audit and coverage matrix
  - No PID file found in `projects/marketplace-overview/release_9/docs` during repository scan
- Impact: Review cannot verify non-PRD business constraints/assumptions from PID; approval confidence is reduced.
- Recommendation: Provide PID path (or explicitly confirm PID is not applicable for this release) and rerun gap analysis for final approval.
- Status: `Open`

### AR-005
- Severity: `P2`
- Area: `Functional Edge-Case Coverage`
- Gap: PRD requires deterministic alphabetical tiebreak when reseller counts are equal; architecture/API do not define this ordering rule.
- Evidence:
  - PRD US002 corner case: alphabetical tiebreak (`requirements/prd.md:249`)
  - Architecture API covers ranking and pain logic but no equal-count ordering rule (`design/architecture.md:815-875`, `design/architecture.md:1058-1063`)
- Impact: Non-deterministic ordering across loads can cause flaky tests and confusing UI.
- Recommendation: Add explicit sort contract: `ORDER BY total_resellers DESC, marketplace_name ASC`.
- Status: `Open`

### AR-006
- Severity: `P2`
- Area: `UI Interaction Contract`
- Gap: PRD requires audit sample click debouncing; architecture states no duplicate prevention is needed.
- Evidence:
  - PRD US007 corner case: open/download only once with debounce (`requirements/prd.md:569`)
  - Architecture debouncing table: "Audit Sample download - no duplicate prevention needed" (`design/architecture.md:1219`)
- Impact: Potential duplicate downloads and mismatch against PRD acceptance expectations.
- Recommendation: Align on expected behavior; if PRD stands, add frontend click guard/debounce and test case.
- Status: `Open`

### AR-007
- Severity: `P2`
- Area: `Business Observability`
- Gap: PRD success metrics are defined, but architecture does not specify event schema/dashboard ownership to measure them end-to-end.
- Evidence:
  - PRD metrics: pilot requests, audit requests, WBR download rate, DAU (`requirements/prd.md:65-75`)
  - Architecture observability is technical (latency/errors/cache) with no explicit product KPI instrumentation plan (`design/architecture.md:1233-1240`)
- Impact: Release can ship without reliable KPI proof, weakening product validation in Q2/Q3 goals.
- Recommendation: Add analytics event contract and reporting plan (event names, dimensions: org/brand/marketplace/user, dashboard owner, review cadence).
- Status: `Open`

### AR-008
- Severity: `P2`
- Area: `Decision Traceability`
- Gap: Architecture references ADR files that are not present in the ADR folder.
- Evidence:
  - Architecture ADR references (`design/architecture.md:1334-1336`)
  - `projects/marketplace-overview/release_9/docs/design/ADR` folder has no files
- Impact: Key decisions are not auditable; future changes may re-open settled choices.
- Recommendation: Add referenced ADR documents or remove broken links and inline final decisions with rationale.
- Status: `Open`

## 5. PRD/PID Coverage Matrix

| Requirement ID/Topic | Source | Architecture Coverage | Notes |
|---|---|---|---|
| US001 Active subscription cards + enforcement popup + link gating | PRD | Full | Covered in sections 6.1, 7.1, 8.1, 9.2, 9.3 |
| US002 Unsubscribed marketplace ranking + pain levels | PRD | Partial | Pain thresholds covered; equal-reseller alphabetical tiebreak missing |
| US003 Brand/enforcement filtering across screen | PRD | Conflicting | Brand filter behavior conflicts on unsubscribed side (AR-001) |
| US004 WBR download + not-available handling | PRD | Partial | Core flow covered; partial zip "note in filename" rule not defined |
| US005 Start free pilot (capture fields, dedupe, tooltip) | PRD | Partial | Core flow and dedupe covered; failure semantics ambiguous (AR-002) |
| US006 Request audit report + duplicate handling | PRD | Partial | Duplicate handling covered; failure semantics ambiguous (AR-002) |
| US007 Audit sample download | PRD | Partial | Core endpoint covered; rapid-click debounce conflicts (AR-006) |
| US009 Navigation to Analytics/Enforcement/Violations | PRD | Full | Route mapping and subscription-based gating documented |
| Show stoppers and dependency deadlines | PRD | Partial | Risks listed but no explicit go/no-go control model (AR-003) |
| Success metrics instrumentation | PRD | Partial | Technical metrics present; product KPI implementation plan missing (AR-007) |
| Security/tenant isolation | PRD | Full | org_id isolation, auth, rate limiting, validation are documented |
| PID baseline coverage | PID | Missing | PID document not provided/found (AR-004) |

## 6. Feasibility and Delivery Risk Assessment

- Technical feasibility risks:
  - Brand filter behavior conflict for P0 story introduces likely redesign at API/data contract level.
  - ADR references unresolved in repository reduce decision stability.
- Integration/dependency risks:
  - GCP bucket path confirmation and schema finalization remain open.
  - Subscription config/API readiness and email trigger configuration are still external dependencies.
- Non-functional readiness risks:
  - Product KPI instrumentation is not concretely defined despite PRD success metrics.
  - Edge-case behavior contracts (ordering, debounce) are not fully aligned.
- Rollout/migration/operations risks:
  - Migration DDL exists, but go-live readiness gates are not explicit.
  - Current architecture is not approval-ready until P0/P1 items are resolved and re-reviewed.

## 7. Open Questions and Assumptions

1. Should brand filters apply to unsubscribed marketplace cards, or should PRD US003 be revised to subscription-side-only behavior?
2. For pilot/audit email failures, what is the canonical UX per failure type: immediate error+retry, or optimistic success with async retry?
3. Where is the PID document for `marketplace-overview/release_9`, or can Product explicitly mark PID as not applicable?
4. Who owns each external dependency (GCP bucket URLs/schema, subscription config API shape, support email readiness) and what are approval cutoff dates?
5. Should audit sample download enforce debounce/one-click behavior, or should PRD US007 corner case be updated?

## 8. Approval Log

- Current approval status: `Not Approved`
- Approval date: `N/A`
- Approved by: `N/A`
- Approval conditions (if any):
  - Resolve AR-001 (P0)
  - Resolve AR-002/AR-003/AR-004 (P1)
  - Confirm acceptance or remediation plan for open P2 findings
