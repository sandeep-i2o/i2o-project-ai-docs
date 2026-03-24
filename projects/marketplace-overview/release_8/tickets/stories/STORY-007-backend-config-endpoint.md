---
id: STORY-007
title: "[MO] Backend: GET /marketplace-overview/config Endpoint"
project: marketplace_overview
release: release_8
module: i2o-reseller
type: Story
priority: High
epic: EPIC-002
status: Draft
estimate: 2 days
created: 2026-03-04
depends_on:
  - STORY-006
---

# STORY-007 — Backend: GET /marketplace-overview/config Endpoint

## Context

This story implements `GET /marketplace-overview/config` in `i2o-reseller`. The endpoint returns the filter metadata that the Angular frontend needs on page load: brand list, region list, current week defaults, and activation status per marketplace. Data is sourced from `i2o-master-data` (PostgreSQL `org_market_mapping` table). Brand and region metadata is cached in Spring in-memory cache (TTL 5 min) to avoid repeated database trips.

## Module: `i2o-reseller`

### Files to Implement

- `MarketplaceOverviewController.java` — add `GET /marketplace-overview/config` method
- `MarketplaceOverviewConfigService.java` — implement business logic
- `application-{env}.properties` — add new properties if needed

### Service Logic

**`MarketplaceOverviewConfigService.getConfig(String orgId)`:**

1. Extract `orgId` from Keycloak Bearer token (via `SecurityContextHolder` / existing token util) — NEVER from request params.
2. Query `i2o-master-data` (HTTP REST call or shared DB view): `SELECT org_id, marketplace, is_activated, activated_at, regions_enabled FROM org_market_mapping WHERE org_id = ?`
3. Derive `brands` and `regions` from master data — cache result with Spring `@Cacheable` (TTL 5 min, cache name `marketplace-config`).
4. Compute `defaultWeekStart` = last Monday, `defaultWeekEnd` = last Sunday.
5. Return `MarketplaceConfigResponse`.

### Controller Method

```java
@GetMapping("/config")
@PreAuthorize("hasRole('brand-protector')")
public ResponseEntity<MarketplaceConfigResponse> getConfig() {
    String orgId = tokenUtil.extractOrgId();
    return ResponseEntity.ok(configService.getConfig(orgId));
}
```

### Response Contract

```json
{
  "brands": ["Nike", "Adidas", "Puma"],
  "regions": ["US", "UK"],
  "defaultWeekStart": "2026-02-24",
  "defaultWeekEnd": "2026-03-02",
  "marketplaceConfig": [
    { "marketplace": "AMAZON", "status": "ACTIVATED" },
    { "marketplace": "WALMART", "status": "ACTIVATED" },
    { "marketplace": "EBAY",   "status": "TRIAL" },
    { "marketplace": "TARGET", "status": "TRIAL" }
  ]
}
```

## Acceptance Criteria

1. `GET /marketplace-overview/config` returns HTTP 200 with correct response structure.
2. `orgId` is extracted from the Keycloak Bearer token — not from request parameters or body.
3. `marketplaceConfig` reflects the actual activation status from `org_market_mapping` for the authenticated org.
4. `defaultWeekStart` is always the previous Monday; `defaultWeekEnd` is the previous Sunday.
5. Brand and region metadata is cached (Spring `@Cacheable`, TTL 5 min).
6. Unauthorized request (no valid token) returns HTTP 401.
7. Request from a user without `brand-protector` role returns HTTP 403.
8. JUnit 5 unit tests cover service logic with mocked master-data dependency (≥ 80% coverage).
9. `@SpringBootTest` integration test verifies correct response shape.
10. **[Remediates F-M-001]** Cross-tenant isolation integration test passes: a request authenticated with `org_A`'s token must NOT return any data rows belonging to `org_B`. Test evidence (CI artifact: test report or log excerpt) must be attached to the PR.

## Definition of Done Checklist

- [ ] Endpoint implemented in `MarketplaceOverviewController`
- [ ] `MarketplaceOverviewConfigService.getConfig(orgId)` implemented
- [ ] `orgId` always extracted from token (not from request)
- [ ] Spring `@Cacheable` applied with TTL 5 min on brand/region metadata
- [ ] Auth guard `@PreAuthorize("hasRole('brand-protector')")` applied
- [ ] Unit tests written (≥ 80% coverage)
- [ ] Integration test written
- [ ] **[F-M-001]** Cross-tenant isolation integration test written and passing; CI test-report artifact attached to PR
- [ ] JavaDocs added to all public methods

## Architecture References

- Section 5.2 — Controller/Service/DTO structure
- Section 6.1 — Step 1: Config load sequence diagram
- Section 8.2 — `GET /marketplace-overview/config` API spec
- Section 12 — Security (org_id from token, role-based access)
- Section 13 — Cache TTL for filter metadata
