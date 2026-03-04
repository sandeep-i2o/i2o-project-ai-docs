---
id: EPIC-002
title: "[MO] Backend — i2o-reseller Marketplace Overview Sub-Package"
project: marketplace_overview
release: release_8
module: i2o-reseller
type: Epic
priority: High
status: Draft
created: 2026-03-04
stories:
  - STORY-006
  - STORY-007
  - STORY-008
---

# EPIC-002 — Backend: i2o-reseller Marketplace Overview Sub-Package

## Business Value (Charlie-Conductor)

The backend provides two new lightweight endpoints (`GET /marketplace-overview/config` and `POST /marketplace-overview/initiate-trial`) that enable the Marketplace Overview dashboard and the trial request email flow respectively. All KPI data retrieval reuses the existing `getCardData`/`getGridCardData` generic query engine — no new data-fetch endpoints are introduced. This keeps the architecture minimal and reuses the existing BQ-backed query framework while delivering the config and email capabilities required by the PRD.

## Technical Feasibility (Bob-Builder)

- **Stack:** Spring Boot 3.x, existing `i2o-reseller` Controller/Service/DTO pattern, existing Keycloak Bearer interceptor.
- **New additions:** 1 controller, 2 services, 2 DTOs, 1 enum — all within a new `marketplaceoverview` sub-package.
- **BQ isolation:** `org_id` is extracted from the Keycloak token server-side and injected as a mandatory `WHERE` clause into every BigQuery query — never trusted from the client.
- **Effort estimate:** Medium (1–2 sprints for all stories).
- **Dependency:** `org_market_mapping` table in `i2o-master-data` exists (confirmed); no schema changes needed.

## Scope

This epic covers all changes inside `i2o-reseller`:

| Area | Deliverable |
|------|-------------|
| Sub-package scaffold | `com.corecompete.i2o.marketplaceoverview` package structure |
| Config endpoint | `GET /marketplace-overview/config` — brands, regions, week defaults, activation status |
| Trial endpoint | `POST /marketplace-overview/initiate-trial` — calls i2o-email-service |
| `MarketplaceEnum` | `AMAZON`, `WALMART`, `EBAY`, `TARGET` enum |
| DTOs | `MarketplaceConfigResponse.java`, `InitiateTrialRequest.java` |
| Email service integration | `MarketplaceTrialEmailService` — REST call to `i2o-email-service` |
| Security | `org_id` from Keycloak token; `brandName` derived server-side; rate limiting (1/hour/marketplace/brand) |
| Config registration | Register `bp_marketplace_overview_card` and `bp_marketplace_overview_table` componentIds in `i2oretail.component` PostgreSQL table |
| Unit tests | JUnit 5 + Mockito ≥ 80% service coverage |
| Integration tests | `@SpringBootTest` for `MarketplaceOverviewController` with mock BQ + mock PostgreSQL; cross-tenant isolation test |

## Dependencies

- `i2o-master-data` must expose `org_market_mapping` read access (already exists).
- `i2o-email-service` REST endpoint must be reachable in DEV/QA/PROD.
- Support team email address (Open Item #3 — 🟡 Medium risk; fallback: placeholder value).
- componentId registration is a prerequisite for EPIC-001 integration testing.

## Story Breakdown

| Story | Title |
|-------|-------|
| STORY-006 | Sub-package scaffold + MarketplaceEnum + DTOs |
| STORY-007 | Config endpoint — `GET /marketplace-overview/config` |
| STORY-008 | Trial endpoint — `POST /marketplace-overview/initiate-trial` + email integration + rate limit |

## Acceptance Criteria (Epic-level)

1. `GET /marketplace-overview/config` returns brands, regions, week defaults, and activation status per marketplace for the authenticated org.
2. `POST /marketplace-overview/initiate-trial` triggers an email to `support@i2oretail.com` with the correct brand and marketplace.
3. `org_id` is never accepted from the client payload — always extracted from the Keycloak Bearer token.
4. `brandName` is derived server-side from `i2o-master-data` using `brandId` — preventing email injection.
5. Rate limit of 1 trial request per marketplace per brand per hour is enforced server-side.
6. Unit tests pass with ≥ 80% service coverage.
7. Cross-tenant isolation integration test passes (org_A data not visible to org_B queries).

## Architecture References

- Section 4.1 — Key decisions (config endpoint rationale, trial endpoint, frontend-only multi-brand enforcement)
- Section 5.2 — Backend sub-package structure
- Section 8.2 — New endpoint API specification
- Section 8.3 — Email payload to i2o-email-service
- Section 12 — Security architecture (org_id isolation, email injection prevention, rate limiting)
- Section 14.2 — Integration tests incl. cross-tenant isolation
