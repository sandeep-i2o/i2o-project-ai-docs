# Ticket Review Report

## 1. Review Scope
- Project: `marketplace-overview` (input normalized from `marketplace_overview`)
- Release: `release_9`
- Review date: `2026-04-06`
- Reviewer: `AI Agent via review-generated-epics`

### Inputs Reviewed
- PRD: `projects/marketplace-overview/release_9/docs/requirements/prd.md`
- Architecture:
  - `projects/marketplace-overview/release_9/docs/design/architecture.md`
  - `projects/marketplace-overview/release_9/docs/design/architecture-review.md`
  - `projects/marketplace-overview/release_9/docs/design/architecture-remediation.md`
- Tickets folder: `projects/marketplace-overview/release_9/tickets` (fallback path; `docs/tickets` not present)

## 2. Readiness Verdict
`Ready with Conditions`

Ticket set is structurally strong (clear epic-story hierarchy, testable acceptance criteria, architecture citations) and covers the release_9 implementation shape. Readiness is conditional on addressing one architecture contract mismatch, one sequencing dependency risk, and several medium-level coverage/NFR clarifications before Jira publishing or sprint commitment.

## 3. Executive Summary
- Total Epics reviewed: `1`
- Total Stories reviewed: `8`
- Total findings: `6`
- Critical/High/Medium/Low: `0/2/3/1`
- Ambiguities: `3`

## 4. Traceability Matrix
| Requirement ID | Requirement Summary | Ticket Coverage | Coverage Status | Notes |
|---|---|---|---|---|
| PRD-RQ-001 | US001 active subscription cards + enforcement popup + active-only rendering | MPO-R9-ST-001 | Partial | Core rendering and popup are covered; explicit no-active-subscription empty-state AC is missing. |
| PRD-RQ-002 | US002 top unsubscribed marketplaces with ranking/pain badges from GCP data | MPO-R9-ST-002 | Partial | Story intentionally uses release_9 placeholder model (`##`) per architecture accepted risk; PRD still defines ranking logic. |
| PRD-RQ-003 | US003 filter by brand + enforcement account, defaults, debounce, empty state | MPO-R9-ST-003 | Full | Default state, filtering behavior, and empty-state handling are covered. |
| PRD-RQ-004 | US004 WBR access and unavailable/error handling | MPO-R9-ST-004 | Partial | Behavior coverage is good, but endpoint naming drifts from architecture API contract. |
| PRD-RQ-005 | US005 start free pilot with validation, persistence, duplicate prevention | MPO-R9-ST-005 | Full | Includes validation source (`org_market_mapping.enabled=false`) and retry semantics. |
| PRD-RQ-006 | US006 request audit with duplicate-allowed behavior | MPO-R9-ST-006 | Full | Duplicate handling and queued-retry semantics are explicit. |
| PRD-RQ-007 | US007 audit sample banner + sample download | MPO-R9-ST-007 | Full | CTA/banner and signed URL behavior are covered. |
| PRD-RQ-008 | US009 navigation links by enabled modules + back-navigation UX | MPO-R9-ST-001 | Partial | Link gating is covered; explicit “back returns with filter state intact” AC is not included. |
| ARC-RQ-001 | Active subscription source is legacy `org_market_mapping` path; brands/accounts from master tables | MPO-R9-ST-001 | Full | Story aligns to architecture v1.8 data source split. |
| ARC-RQ-002 | Screen enablement via `ui_config` keys (`BrandProtector*`) | MPO-R9-ST-001 | Full | AC directly references module-gated rendering by `ui_config`. |
| ARC-RQ-003 | WBR canonical source: `schedule_wbr_details` + published `PPT url` from `gcs_location` JSON | MPO-R9-ST-004 | Full | Canonical source stated; endpoint path naming mismatch remains. |
| ARC-RQ-004 | Unsubscribed metrics are UI placeholders only in release_9 (no backend API) | MPO-R9-ST-002 | Full | Story explicitly enforces no backend endpoint usage. |
| ARC-RQ-005 | Retry executor ownership in `i2o-scheduler` for outbox failures | MPO-R9-ST-008, MPO-R9-ST-005, MPO-R9-ST-006 | Partial | Job logic story exists, but sequencing/dependency with pilot/audit delivery stories is not explicit. |
| NFR-001 | Performance: page load <3s P95 | None explicit | None | No story contains measurable performance AC or instrumentation validation for the target. |
| NFR-002 | Security: org isolation, auth claims, rate limiting on action endpoints | MPO-R9-ST-001, ST-005, ST-006 | Partial | Token/validation appears, but explicit rate-limit/security AC is absent in stories. |
| NFR-003 | Reliability: optimistic 202 + outbox retry lifecycle | MPO-R9-ST-005, ST-006, ST-008 | Full | Core failure class and retry behavior are represented. |
| NFR-004 | Observability/KPI instrumentation incl. WBR signals | MPO-R9-ST-004, ST-008 | Partial | Initiated event and retry metrics covered; completion signal reliability remains unresolved (AR-012). |

## 5. Findings by Severity

### Critical
No critical findings.

### High
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| FND-001 | Architecture Misalignment | ARC-RQ-003 (`architecture.md` Section 8.3) | `MPO-R9-ST-004` | Story AC uses `GET /marketplace-overview/wbr-report`, while architecture contract defines `GET /marketplace-overview/wbr/download`. This can cause implementation divergence and incorrect QA test targets. | Update ST-004 AC/API references to `GET /marketplace-overview/wbr/download` (or update architecture if API was intentionally renamed), then keep one canonical endpoint name across docs. |
| FND-002 | Sequencing/Dependency Gap | PRD-RQ-001, PRD-RQ-008; ARC dependency gate (`architecture.md` Section 10.5) | `MPO-R9-ST-001` | ST-001 combines US001 and US009 link-gating while `ui_config` contract sign-off is still open in architecture dependency table. This can block core page delivery if nav contract slips. | Split US009 into a dedicated story or add explicit dependency gating in ST-001 (deliver core card rendering first, enable nav links behind contract/feature toggle). |

### Medium
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| FND-003 | Coverage Gap (Known, accepted-risk) | PRD-RQ-002 (US002) vs architecture accepted-risk AR-013 | `MPO-R9-ST-002`, Epic summary | PRD still defines pain ranking/badges/data freshness behavior; story correctly implements release_9 placeholders. Without explicit PRD-alignment note in delivery checklist, QA may test against outdated PRD behaviors. | Add a release condition note in Epic + ST-002: “US002 ranking logic deferred; placeholder-only behavior is the test oracle for release_9 pending PRD update.” |
| FND-004 | Ticket Quality Gap | PRD-RQ-001 (US001 corner/AC), PRD-RQ-008 (US009 corner/AC) | `MPO-R9-ST-001` | Story AC omits two explicit user-visible outcomes: no-active-subscriptions empty state and back-navigation with filter-state retention. Both are testable requirements in PRD and UI behavior sections. | Add AC entries for no-subscription empty state and back-navigation filter preservation (or create a small follow-up story if scope is intentionally deferred). |
| FND-005 | Non-Functional Gap | NFR-001, NFR-002 (`architecture.md` Sections 11, 13.2) | `MPO-R9-ST-001`, `ST-005`, `ST-006` | Security/rate-limit/performance targets are present in architecture but not translated into measurable story ACs. This increases risk of “done but not production-ready.” | Add measurable NFR ACs: org-scope query enforcement checks, action endpoint rate-limit checks, and page-load P95 validation in E2E/perf tests. |

### Low
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| FND-006 | Ticket Quality Gap | PRD release priorities (US004 P1, US007 P2) | `MPO-R9-ST-004` (P0), `MPO-R9-ST-007` (P1) | Priority labels are slightly higher than PRD release priorities, which may reorder sprint focus unintentionally. | Realign story priorities to PRD, or explicitly document why priorities were elevated for release risk management. |

## 6. Ambiguities
| Ambiguity ID | Location | Ambiguous Statement | Risk | Clarify By (Question) |
|---|---|---|---|---|
| AMB-001 | PRD US004 vs architecture v1.8 + ST-004 | PRD says zip of PDFs; architecture/story say published PPT URL. | QA/or implementation may validate against wrong artifact format. | For release_9 sign-off, should the official test oracle be architecture v1.8 (published PPT URL) until PRD revision lands? |
| AMB-002 | ST-005/ST-006 with ST-008 sequencing | Pilot/audit return `202` and queue retries, but dependency on retry job readiness is implied, not explicit. | Requests may queue indefinitely in early environments if scheduler is not active. | Should ST-005/ST-006 definition of done require ST-008 minimum deployable retry capability in the same milestone? |
| AMB-003 | NFR ownership across stories | NFR targets exist in architecture but are not assigned to specific stories. | NFR work may be postponed and missed before release cut. | Which story (or dedicated NFR hardening story) owns page-load P95 and rate-limit verification evidence? |

## 7. Recommended Ticket Updates
1. `MPO-R9-ST-004`: Normalize endpoint name to `GET /marketplace-overview/wbr/download` to match architecture Section 8.3.
2. `MPO-R9-ST-001`: Add explicit ACs for no-active-subscription empty state and back-navigation filter-state retention.
3. `MPO-R9-ST-001` and/or new `MPO-R9-ST-009`: decouple US009 navigation gating from core US001 if `ui_config` contract closure is delayed.
4. `MPO-R9-ST-002`: Add explicit note that US002 ranking/pain logic is deferred and excluded from release_9 QA acceptance.
5. `MPO-R9-ST-005` and `MPO-R9-ST-006`: add measurable security/rate-limit ACs and explicit dependency on retry readiness.
6. Epic `MPO-R9-EP-001`: include a small NFR checklist row (performance/security/observability) as release gate criteria.

## 8. Open Questions
1. Should release_9 test cases and PO sign-off use architecture v1.8 as source-of-truth when PRD language conflicts (US002/US004)?
2. Is there intent to create a separate post-release story for canonical unsubscribed metrics source integration, or keep it only as a dependency note?
3. Should navigation gating (US009) remain bundled with active-subscription story execution, or be independently planned to protect week 1–2 delivery?

## 9. Assumptions
1. Architecture v1.8 and architecture-review v9 are authoritative for release_9 implementation decisions.
2. Tickets in `release_9/tickets` are the working source since `release_9/docs/tickets` does not exist.
3. Accepted risks AR-013 and AR-015 are intentionally carried for release_9 until PRD text alignment is completed.
