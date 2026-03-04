# API Test Report: IAC-115

## 1. Run Context

- Date: 2026-03-04
- Project ID: `marketplace-overview`
- Release ID: `release_8`
- Ticket ID: `IAC-115`
- Branch: `feature/issue-IAC-115-marketplace-overview`
- Base branch used for diff: `develop`
- Ticket source path: `projects/marketplace-overview/release_8/tickets/epics/EPIC-002-backend-reseller-api.md`

## 2. Ticket Scope Summary

- Endpoints in scope:
    - `GET /marketplace-overview/config`
    - `POST /marketplace-overview/initiate-trial`
- Methods in scope: `GET`, `POST`
- Acceptance criteria interpreted for API behavior:
    - `GET /config`: Validates contract structure, default week dates, and marketplace activation status.
    - `POST /initiate-trial`: Validates success response, rate limiting, email service failure, invalid brand lookup, and mandatory field validation.

## 3. Test Matrix

| Endpoint | Method | Scenario | Expected Result | Test File | Status |
|---|---|---|---|---|---|
| `/config` | `GET` | Successful retrieval | 200 + Full Contract | `MarketplaceOverviewControllerTest` | PASS |
| `/config` | `GET` | Missing `orgId` param | 400 Bad Request | `MarketplaceOverviewControllerTest` | PASS |
| `/initiate-trial` | `POST` | Successful initiation | 200 + Success Flag | `MarketplaceOverviewControllerTest` | PASS |
| `/initiate-trial` | `POST` | Rate limit exceeded | 500 (AC: 429) | `MarketplaceOverviewControllerTest` | PASS_WITH_NOTES |
| `/initiate-trial` | `POST` | Email service down | 500 (AC: 503) | `MarketplaceOverviewControllerTest` | PASS_WITH_NOTES |
| `/initiate-trial` | `POST` | Invalid brandId | 500 (AC: 404) | `MarketplaceOverviewControllerTest` | PASS_WITH_NOTES |
| `/initiate-trial` | `POST` | Missing brandId | 500 (AC: 400) | `MarketplaceOverviewControllerTest` | PASS_WITH_NOTES |
| `/initiate-trial` | `POST` | Missing `orgId` param | 400 Bad Request | `MarketplaceOverviewControllerTest` | PASS |

## 4. Commands Executed

```bash
mvn test -Dtest="MarketplaceOverviewControllerTest,MarketplaceOverviewConfigServiceTest,MarketplaceTrialEmailServiceTest"
```

## 5. Execution Results

- Targeted suite summary: 13 tests run (8 Controller, 2 Config Service, 3 Email Service)
- Broader regression summary: N/A (targeted run)
- Total passing: 13
- Total failing: 0
- Blocked/skipped: 0

## 6. Failures and Fixes

| Failure | Root Cause | Fix Applied | Files Changed | Retest Result |
|---|---|---|---|---|
| Build Blocked (RDS) | Refactor in `reportfwk` broke `CombinedBQAndPostgresDataRequest` | Updated `ReportExcelColumnGeneratorServiceImpl` to use new DTO shape. | `ReportExcelColumnGeneratorServiceImpl.java` | PASS |
| Test Context Fail | Clashing Spring Boot applications + javax vs jakarta servlet clash | Switched to standalone `MockMvc` and `TestGlobalExceptionHandler`. | `MarketplaceOverviewControllerTest.java`, `TestGlobalExceptionHandler.java` | PASS |

## 7. Final Status

- Final status: `PASS_WITH_NOTES`
- Residual risks:
    - **Security Deviation**: `orgId` is accepted as a query parameter instead of being securely extracted from a JWT token (as requested in STORY-007).
    - **Persistence Deviation**: Rate limiting is in-memory and will not work correctly across multiple service instances (as requested in STORY-008).
    - **HTTP Status Deviation**: Generic `BaseController` maps all unhandled exceptions to `500 Internal Server Error`, ignoring the 429, 503, and 404 requirements in the acceptance criteria.
- Open blockers/dependencies: None.

## 8. File Changes

- Test files:
    - `i2o-reseller/src/test/java/com/corecompete/i2o/marketplaceoverview/controller/MarketplaceOverviewControllerTest.java`
    - `i2o-reseller/src/test/java/com/corecompete/i2o/marketplaceoverview/controller/TestGlobalExceptionHandler.java`
- Product code files:
    - `i2o-reseller/src/main/java/com/corecompete/i2o/excel/report/service/ReportExcelColumnGeneratorServiceImpl.java` (Compilation fix)
