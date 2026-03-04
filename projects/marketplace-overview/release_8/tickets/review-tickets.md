# Ticket Review Report

## 1. Review Scope
- Project: `marketplace-overview`
- Release: `release_8`
- Review date: `2026-03-04`
- Reviewer: `Codex via review-generated-epics`

### Inputs Reviewed
- PRD: `projects/marketplace-overview/release_8/docs/requirements/prd.md`
- Architecture:
  - `projects/marketplace-overview/release_8/docs/design/architecture.md`
  - `projects/marketplace-overview/release_8/docs/design/architecture-review.md`
  - `projects/marketplace-overview/release_8/docs/design/architecture-remediation.md`
- Tickets folder (fallback used): `projects/marketplace-overview/release_8/tickets`

## 2. Readiness Verdict
`Ready with Conditions`

The ticket set is mostly structured and traceable, with clear Epic->Story breakdown and generally testable acceptance criteria. However, there are high-impact gaps that should be fixed before implementation starts at scale: US001 tab-placement coverage is incomplete in story-level AC, performance/availability NFRs are not represented as executable backlog work, and the componentId GO/NO-GO gate is not consistently wired in dependencies/ownership.

## 3. Executive Summary
- Total Epics reviewed: `4`
- Total Stories reviewed: `11`
- Total findings: `6`
- Critical/High/Medium/Low: `0/3/2/1`
- Ambiguities: `4`

## 4. Traceability Matrix
| Requirement ID | Requirement Summary | Ticket Coverage | Coverage Status | Notes |
|---|---|---|---|---|
| PRD-RQ-001 | US001: Add Marketplace Overview tab under Benefits; BP-gated visibility | EPIC-001, STORY-001 | Partial | Route + guard are covered; explicit top-nav tab insertion/visibility behavior is not called out in STORY-001 AC. |
| PRD-RQ-002 | US002: Brand/Region/Week filters + Card/Table toggle with state retention | EPIC-001, STORY-001, STORY-002 | Full | Controls, defaults, and toggle persistence are explicit. |
| PRD-RQ-003 | US003: Card view activated vs trial cards + KPI grouping + null/zero handling | EPIC-001, STORY-003, STORY-005 | Full | KPI sections, trial state, stale banner, and null rendering are testable. |
| PRD-RQ-004 | US004: Table parity with card data, `--` for N/A, default sort/page size | EPIC-001, STORY-004 | Full | `pageSize: 10`, `sort: marketplace ASC`, `null -> --` included. |
| PRD-RQ-005 | US005: Initiate Trial flow with brand disambiguation | EPIC-001, EPIC-002, STORY-005, STORY-008 | Full | Frontend disambiguation and backend email + rate limit are covered. |
| PRD-RQ-006 | US006: Weekly refresh, default last complete week, stale indicator on failure | EPIC-003, STORY-002, STORY-003, STORY-009, STORY-010 | Full | Calendar default + scheduler + staleness handling are covered. |
| ARC-RQ-001 | Reuse `getCardData`/`getGridCardData`; no new data-fetch endpoint | EPIC-001, EPIC-002, EPIC-004, STORY-001, STORY-004, STORY-011 | Full | Reuse strategy is consistent across epics/stories. |
| ARC-RQ-002 | Implement only `GET /marketplace-overview/config` and `POST /marketplace-overview/initiate-trial` | EPIC-002, STORY-007, STORY-008 | Full | Endpoint scope is consistent with architecture. |
| ARC-RQ-003 | Tenant isolation: `org_id` token-derived, query-scoped, cross-tenant test evidence | EPIC-002, STORY-007, STORY-008, STORY-009, STORY-010 | Partial | Token extraction and schema coverage exist; cross-tenant validation is only epic-level, not clearly owned at story level. |
| ARC-RQ-004 | componentId registration is a hard GO/NO-GO gate before frontend integration | EPIC-004, STORY-011, EPIC-001, EPIC-002 | Partial | Gate is documented, but dependency/ownership is split and not explicitly wired at story dependency level. |
| NFR-001 | Performance target: dashboard load P95 < 3s | EPIC-001, EPIC-002, EPIC-003 | None | No story defines perf test method, threshold checks, or owning team/task. |
| NFR-002 | Availability target: 99.5% read-path uptime + operational verification | EPIC-003, STORY-009, STORY-010 | Partial | Retry/audit are covered; measurable SLO validation/monitoring acceptance is not represented in backlog AC. |
| NFR-003 | Security hardening: role guard, email injection prevention, rate limiting | EPIC-001, EPIC-002, STORY-001, STORY-007, STORY-008 | Full | Security controls are explicit and testable. |
| NFR-004 | Test strategy includes US001-US006 E2E scenarios | EPIC-001 | Partial | E2E is listed at epic level but no executable story/ticket owns implementation. |

## 5. Findings by Severity

### Critical
No critical findings.

### High
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| F-H-001 | Coverage Gap | PRD-RQ-001 | STORY-001 | PRD US001 requires tab placement under Benefits top navigation; STORY-001 AC focuses on route/guard and does not explicitly require top-nav insertion/visibility behavior. | Update STORY-001 AC + DoD to include “Benefits top navigation includes Marketplace Overview tab” and “hidden for non-BP users,” with UI integration test evidence. |
| F-H-002 | Non-Functional Gap | NFR-001, NFR-002 | EPIC-001, EPIC-002, EPIC-003 (all story sets) | Architecture defines P95<3s and 99.5% availability, but no story has measurable SLO validation tasks or pass/fail AC. | Add one dedicated NFR story (or split FE/BE stories) with load-test plan, target thresholds, instrumentation, and release gate AC for P95 and uptime. |
| F-H-003 | Sequencing/Dependency Gap | ARC-RQ-004 | EPIC-001, EPIC-002, EPIC-004, STORY-011 | GO/NO-GO gate exists, but ownership is duplicated (EPIC-002 and EPIC-004) and frontend stories do not explicitly depend on STORY-011 for integration readiness. | Make EPIC-004/STORY-011 the single owner of componentId registration; add explicit dependency tags (integration phases of STORY-003/004/005 blocked by STORY-011). |

### Medium
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| F-M-001 | Non-Functional Gap | ARC-RQ-003 | EPIC-002, STORY-007, STORY-008 | Cross-tenant isolation testing is required by architecture but only appears at epic level; no story AC clearly requires this specific integration test. | Add explicit AC to STORY-007 (or new backend test story): org_A data must not be returned for org_B token scope; include negative test proof in CI artifacts. |
| F-M-002 | Ticket Quality Gap | NFR-004 | EPIC-001 | E2E coverage is required but lacks a concrete story owner and deliverables; this creates risk that E2E is deferred. | Add a frontend QA story for US001-US006 E2E automation/manual suite with environment, data setup, and exit criteria. |

### Low
| Finding ID | Type | Requirement Ref | Ticket Ref | Why this matters | Recommendation |
|---|---|---|---|---|---|
| F-L-001 | Duplication/Overlap Gap | ARC-RQ-004 | EPIC-002, EPIC-004 | Component registration appears in both EPIC-002 scope and EPIC-004 scope, which can create duplicate execution or assumption drift. | Remove component registration from EPIC-002 scope text and retain cross-reference to EPIC-004 only. |

## 6. Ambiguities
| Ambiguity ID | Location | Ambiguous Statement | Risk | Clarify By (Question) |
|---|---|---|---|---|
| A-001 | `architecture.md` Section 7.3 vs 10.1 | Activation table is `org_market_mapping` in one section, but dependency table still mentions `org_marketplace_config`. | Backend implementation may point to wrong source/table contract. | Which exact data source contract is authoritative for activation status in implementation and tests? |
| A-002 | STORY-008 “Rate Limit Implementation” | Allows either PostgreSQL table or in-memory cache for 1-hour limit. | In-memory option can break consistency across multiple app instances. | Is distributed/persistent rate limiting mandatory for production, or is single-instance behavior acceptable? |
| A-003 | STORY-009 DDL + STORY-010 lifecycle | `created_at`/`updated_at` fields exist, but write/update policy is not explicitly required in AC. | Inconsistent metadata population reduces operability and auditability. | Should AC enforce timestamp population policy for INSERT/UPDATE in scheduler writes? |
| A-004 | EPIC/STORY dependency language | “Integration blocked by componentId gate” is clear in prose, but formal `depends_on` is not modeled across affected frontend integration stories. | Teams may start integration steps prematurely. | Should dependency metadata be extended to model “build-ready” vs “integration-ready” dependencies explicitly? |

## 7. Recommended Ticket Updates
1. `STORY-001`: Add AC for explicit Benefits top-nav tab placement + non-BP visibility behavior (US001 full coverage).
2. `EPIC-001` + `STORY-003/004/005`: Add explicit integration dependency on `STORY-011` (or add integration subtask blocked by STORY-011).
3. `EPIC-002`: Remove/relocate componentId registration ownership to `EPIC-004` only; keep reference link.
4. `STORY-007`: Add cross-tenant isolation integration AC and test evidence requirement.
5. Add a new NFR story: performance + availability validation (`P95 < 3s`, read-path availability evidence, monitoring hooks).
6. Add a new QA/E2E story: implement/execute US001-US006 test suite with concrete exit criteria.
7. `STORY-008`: Lock rate-limit storage strategy to production-safe persistent/distributed approach.
8. `STORY-009`/`STORY-010`: Add AC for `created_at`/`updated_at` population and verification.

## 8. Open Questions
1. Is US001 considered complete with route-only access, or must a visible Benefits top-nav tab be explicitly delivered in this release?
2. Who is the single accountable owner for the componentId gate execution: EPIC-004 only, or shared with EPIC-002?
3. Which mechanism is approved for production rate limiting (persistent DB, distributed cache, or other)?
4. Where should performance/availability validation live in the backlog (frontend, backend, or shared platform story)?

## 9. Assumptions
1. `architecture-remediation.md` is treated as authoritative over older conflicting architecture statements where wording diverges.
2. Tickets reviewed are intended to be implementation-ready artifacts, not only documentation placeholders.
3. Scope assessment is based on current files under `projects/marketplace-overview/release_8/tickets` only (no external Jira items included).
