---
id: STORY-008
title: "[MO] Backend: POST /marketplace-overview/initiate-trial Endpoint + Rate Limit"
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

# STORY-008 — Backend: POST /marketplace-overview/initiate-trial + Rate Limit

## Context

This story implements the Initiate Trial endpoint in `i2o-reseller`. When a user clicks "Initiate Trial" for a trial marketplace (eBay/Target), this endpoint receives a `{ brandId, marketplace }` payload, looks up the brand name server-side from `i2o-master-data`, and calls `i2o-email-service` to send an email to the support team. Server-side rate limiting (1 request per marketplace per brand per hour) prevents spam.

## Module: `i2o-reseller`

### Files to Implement

- `MarketplaceOverviewController.java` — add `POST /marketplace-overview/initiate-trial`
- `MarketplaceTrialEmailService.java` — implement email call + rate limit check

### Service Logic

**`MarketplaceTrialEmailService.initiateTrial(String brandId, MarketplaceEnum marketplace, String orgId)`:**

1. **Rate limit check:** Query PostgreSQL rate limit table (or in-memory store): if a request for `(orgId, brandId, marketplace)` was made within the last 1 hour, return 429 Too Many Requests.
2. **Brand name lookup:** Call `i2o-master-data` to get `brandName` from `brandId` — NEVER use user-supplied brand name strings in the email.
3. **Email construction:**
   ```
   to: ["support@i2oretail.com"]
   subject: "Initiate L1 report for {Brand Name}"
   body: "Hey Team, can you run L1 audit for {Brand Name} on {Marketplace}"
   template: "plain_text"
   ```
4. **Call `i2o-email-service`:** `POST {email-service-url}/send` with above payload.
5. **If email service unreachable:** Return 503 with `{ "message": "Email service unavailable. Please try again." }`.
6. **On success:** Record request timestamp in rate limit store; return 200.

### Controller Method

```java
@PostMapping("/initiate-trial")
@PreAuthorize("hasRole('brand-protector')")
public ResponseEntity<Map<String, Object>> initiateTrial(@Valid @RequestBody InitiateTrialRequest request) {
    String orgId = tokenUtil.extractOrgId();
    emailService.initiateTrial(request.getBrandId(), request.getMarketplace(), orgId);
    return ResponseEntity.ok(Map.of("success", true, "message", "Trial request sent successfully."));
}
```

### Rate Limit Implementation

- **[Remediates A-002]** Rate limit MUST be enforced via a **persistent data store** (PostgreSQL table `marketplace_trial_rate_limit` or equivalent). An in-memory Guava/ConcurrentHashMap cache is NOT acceptable for production because it does not survive restarts and fails in multi-instance deployments.
- Key: `(orgId, brandId, marketplace)`.
- Rate limit record: insert a row on first request; reject subsequent requests within 1 hour of `requested_at` timestamp; expire records older than 1 hour.
- On rate limit exceeded: HTTP 429 with `{ "error": "Trial request already sent. Please wait before sending again." }`.

## Acceptance Criteria

1. `POST /marketplace-overview/initiate-trial` with valid `brandId` and `marketplace` sends email and returns 200.
2. `brandName` used in email subject/body is derived server-side from `i2o-master-data` — not from the request payload.
3. If the same `(orgId, brandId, marketplace)` combination triggers a second request within 1 hour, API returns HTTP 429.
4. If `i2o-email-service` is unreachable, API returns HTTP 503 with appropriate message.
5. Invalid `brandId` (not found in `i2o-master-data`) returns HTTP 404.
6. Missing or blank `marketplace` / `brandId` returns HTTP 400 (validation error).
7. JUnit 5 unit tests cover rate limit, email call, and error handling (≥ 80% coverage).
8. Integration test verifies 200, 429, and 503 responses.

## Definition of Done Checklist

- [ ] Endpoint implemented in controller with `@Valid` and role guard
- [ ] `MarketplaceTrialEmailService` implemented with brand name lookup, rate limit, and email dispatch
- [ ] Email payload uses server-derived `brandName`, not client-supplied string
- [ ] Rate limit enforced (1/hour/org/brand/marketplace)
- [ ] 503 error response on email service unreachable
- [ ] `marketplace.email-service.url` and `marketplace.trial.support-email` properties set in `application-{env}.properties`
- [ ] Unit tests written (≥ 80% coverage)
- [ ] JavaDocs added to all public methods

## Architecture References

- Section 5.2 — `MarketplaceTrialEmailService` in sub-package structure
- Section 6.2 — Initiate Trial email flow diagram
- Section 8.2 — `POST /marketplace-overview/initiate-trial` API spec
- Section 8.3 — Email payload to `i2o-email-service`
- Section 12 — Email injection prevention (brandName derived server-side)
- Section 12 — Rate limiting (1 request per marketplace per brand per hour)
- Section 10.2 — Email service unreachable error handling
