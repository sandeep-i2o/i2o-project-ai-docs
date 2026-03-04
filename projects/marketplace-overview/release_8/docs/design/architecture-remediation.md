# Architecture Review Remediation Report — Marketplace Overview

**Project:** BP-MO-001 | **Release:** release_8
**Source Review:** `architecture-review.md` (Reviewer: Codex, 2026-03-04)
**Remediation Date:** 2026-03-04
**Remediator:** Antigravity

---

## 1. Summary by Severity

| Severity | Count | Resolved | Partially Resolved | Deferred | Cannot Resolve |
|----------|-------|----------|--------------------|----------|----------------|
| P0 | 1 | 1 | 0 | 0 | 0 |
| P1 | 3 | 3 | 0 | 0 | 0 |
| P2 | 2 | 2 | 0 | 0 | 0 |
| P3 | 1 | 1 | 0 | 0 | 0 |
| **Total** | **7** | **7** | **0** | **0** | **0** |

**Overall status:** All findings resolved. Architecture is **conditionally approval-ready** — one go/no-go gate remains (component ID registration, Open Item #2) that must be cleared before frontend integration begins.

---

## 2. Finding-to-Change Matrix

### AR-001 · P0 · Security / Multi-tenant Data Isolation

| Field | Detail |
|-------|--------|
| **Gap** | `org_id` absent from sink schema and runtime query path despite security claim |
| **Sections modified** | §7.2, §6.1, §6.3, §12, §14.2, §15 |
| **Changes made** | Added `org_id STRING NOT NULL` as the first column in `marketplace_kpi_weekly_snapshot` schema with `CLUSTER BY org_id, marketplace, brand_id`. Updated runtime diagrams (§6.1, §6.3) to show `WHERE org_id=?` in all BQ queries and `org_id` in the scheduler INSERT. §12 Security section now specifies `org_id` is extracted from the Keycloak token and never accepted from the client payload. §14.2 adds a mandatory cross-tenant isolation integration test. §15 checklist row 4 updated with concrete evidence pointers. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §7.2 — `org_id STRING NOT NULL` present with clustering comment. §6.1 — BQ WHERE clause contains `org_id=?`. §12 — isolation mechanism explicitly described. §14.2 — cross-tenant test defined. |

---

### AR-002 · P1 · API Contract

| Field | Detail |
|-------|--------|
| **Gap** | Architecture simultaneously claimed reuse of `getCardData`/`getGridCardData` and defined a new `GET /marketplace-overview/data` endpoint — contradictory |
| **Decision (confirmed 2026-03-04)** | Strictly reuse existing endpoints. No `GET /marketplace-overview/data` will be created. |
| **Sections modified** | §2, §4.1, §6.1, §8.1, §15 |
| **Changes made** | §2 Constraints updated to include "(decision confirmed 2026-03-04)". §4.1 Key Decisions table updated to note confirmation; added explicit Multi-brand Trial Enforcement row. §6.1 runtime diagram fully replaced — `GET /marketplace-overview/data` removed; now shows three-step flow: config load → `POST /widget/getCardData` (card) → `POST /report/getGridCardData` (table). §15 added checklist row 6 for API contract clarity. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §6.1 — No `GET /marketplace-overview/data` in any diagram. §8.1 header note states "no new data-fetch endpoint will be introduced". |

---

### AR-003 · P1 · Trial Workflow Correctness

| Field | Detail |
|-------|--------|
| **Gap** | Multi-brand disambiguation only documented as frontend behavior; backend contract did not enforce it |
| **Decision (confirmed 2026-03-04)** | Frontend-only enforcement accepted. Backend trusts single `brandId` from payload. `brandName` derived server-side. |
| **Sections modified** | §4.1, §8.2, §10.2, §12, §15 |
| **Changes made** | §4.1 — new "Multi-brand Trial Enforcement" decision row added with explicit confirmation note. §8.2 initiate-trial endpoint: removed `brandName` from request payload (now derived server-side from `i2o-master-data` using `brandId`); added frontend pre-condition block specifying brand-selection dialog behavior when `brandIds.length > 1`. §10.2 error handling — multi-brand row updated to state "Frontend-only enforcement (confirmed 2026-03-04)". §12 Security — email injection prevention updated: "`brandName` derived server-side from `i2o-master-data` using `brandId`; user-supplied strings never interpolated". |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §8.2 — request payload contains only `brandId` and `marketplace`. §12 — email injection via `brandName` is architecturally prevented. §10.2 — enforcement ownership is explicit. |

---

### AR-004 · P1 · Delivery Readiness

| Field | Detail |
|-------|--------|
| **Gap** | "Implementation-ready" confidence score (9.5/10) contradicted by an unresolved high-risk open dependency; teams could start on a false readiness signal |
| **Sections modified** | §15 (footer), §16 |
| **Changes made** | §15 footer: confidence score reduced from 9.5/10 → 8/10 with explicit rationale that Open Item #2 is a hard gate. §16 Open Items table restructured with `Due`, `Gate?` columns; row 2 (componentId registration) now marked "🚦 GO/NO-GO GATE — Frontend integration testing is blocked until this is done" with deployment steps (DEV → QA → PROD) and a Week 1 due date. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §15 footer — confidence score is 8/10 with gate explanation. §16 — row 2 has GATE flag, owner, due date, and deployment sequence. |

---

### AR-005 · P2 · Reliability / Operations

| Field | Detail |
|-------|--------|
| **Gap** | Stale-data behavior defined but no alerting, retry policy, audit log, or on-call runbook |
| **Sections modified** | §6.3, §10.2, new §17 |
| **Changes made** | §6.3 scheduler diagram: added `INSERT INTO marketplace_scheduler_audit_log` step after each successful run. §10.2: stale data row adds PagerDuty alert threshold (>24h); new "Scheduler job failure" row added with 3-retry/30-min-backoff policy and reference to §17. New §17 Operational Runbook: detection indicators (audit log + staleness flag), PagerDuty trigger rule, escalation steps, manual re-trigger command, backfill procedure with verification query, and `marketplace_scheduler_audit_log` schema. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §6.3 — audit log INSERT present. §10.2 — alert threshold stated. §17 — full runbook with backfill command and verification step. |

---

### AR-006 · P2 · Functional Acceptance Alignment (US004)

| Field | Detail |
|-------|--------|
| **Gap** | API example had `pageSize: 50` and no default sort; PRD US004 requires `pageSize: 10` and alphabetical sort |
| **Sections modified** | §8.1 |
| **Changes made** | `getGridCardData` example payload updated: `"pageSize": 50` → `"pageSize": 10`, added `"sort": "marketplace ASC"`. Expanded the filters object to be fully explicit. Added a business-rule note quoting the PRD US004 requirements for pageSize and sort defaults. §15 added checklist row 17 confirming the fix. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §8.1 `getGridCardData` body — `"pageSize": 10`, `"sort": "marketplace ASC"`. Business rule note cites PRD US004. |

---

### AR-007 · P3 · Data Semantics / KPI Definition

| Field | Detail |
|-------|--------|
| **Gap** | Source tables listed but no deterministic aggregation formulas, null/zero policies, or applies-to marketplace scope per KPI |
| **Sections modified** | New §18 (Appendix A — KPI Mapping) |
| **Changes made** | Added §18 with a 13-row KPI mapping table covering: KPI label, snapshot column, source table, aggregation formula (SUM/COUNT/ratio), unit, null/zero policy, and marketplace applicability. Covers all Analytics, Brand Violation, Enforcement Centre, and Trial KPIs. WoW formula uses self-join on snapshot table. Walmart Brand Violation NULL policy explicitly documented. |
| **Resolution status** | ✅ **Resolved** |
| **Validation evidence** | §18 — 13 KPIs with complete column, formula, unit, null policy, and applicability. |

---

## 3. Open Questions — Resolved

| Question | Resolution |
|----------|-----------|
| Will data retrieval use existing `getCardData/getGridCardData` or new `GET /marketplace-overview/data`? | **Confirmed:** Reuse existing endpoints only. No new data-fetch endpoint. (AR-002) |
| Is `brand_id` globally tenant-safe, or must `org_id` be added to the snapshot? | **Confirmed:** `org_id` must be added. Added to sink schema and all query paths. (AR-001) |
| Should backend reject Initiate Trial requests when multiple brands are selected, or is frontend-only enforcement acceptable? | **Confirmed:** Frontend-only enforcement. Backend trusts single `brandId` from payload. (AR-003) |
| Is `org_marketplace_config` already in i2o-master-data or does it need migration? | **Confirmed:** Table name is `org_market_mapping`. No migration needed. All references updated. |

---

## 4. Remaining Risks and Blockers

| # | Risk | Owner | Gate? |
|---|------|-------|-------|
| 1 | **componentId registration** — `bp_marketplace_overview_card` and `bp_marketplace_overview_table` must be registered in `i2oretail.component` before frontend integration. | Engineering Lead | 🚦 **Hard gate** — Week 1 |
| 2 | **`bp_wbr_detail` column name confirmation** — exact column names for EC KPIs (queue, cnd_pending, total_cnd_sent, test_purchase) needed for aggregation task implementation. | Data Team | Soft dependency — Week 1 |
| 3 | **Trial marketplace BQ data** — eBay/Target data availability in source tables for trial KPIs (Listings, Resellers, WoW) is unconfirmed. | Data Team | Soft dependency — Week 2 |

---

## 5. Decisions Required from Stakeholders

None outstanding. All four open questions from the review have been answered and incorporated.

---

## 6. Architecture Approval Readiness

| Condition | Status |
|-----------|--------|
| AR-001 (P0) resolved | ✅ Yes |
| AR-002 (P1) resolved | ✅ Yes |
| AR-003 (P1) resolved | ✅ Yes |
| AR-004 (P1) resolved | ✅ Yes |
| No unresolved P0/P1 findings | ✅ Yes |
| Hard delivery gate documented with owner | ✅ Yes (Open Item #2 — componentId registration, Week 1) |

**Recommendation:** Architecture is **conditionally approved** for implementation start. Engineering may begin backend (`i2o-reseller`, `i2o-scheduler`) and test infrastructure work immediately. Frontend integration is **gated** on componentId registration completion (Open Item #2).

---

*Remediation completed: 2026-03-04 | Release: release_8*
