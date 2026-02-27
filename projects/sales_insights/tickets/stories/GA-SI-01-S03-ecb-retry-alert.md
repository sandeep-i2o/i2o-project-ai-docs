# Story GA-SI-01-S03: EcbIngestionTask — Retry Logic & Admin Alert Integration

**Epic:** GA-SI-EPIC-01 — Automated ECB FX Rate Ingestion Pipeline  
**Story ID:** GA-SI-01-S03  
**Priority:** P0  
**Estimate:** 1 day  
**Status:** Draft

---

## Story

**As a** system administrator,  
**I want** the ECB ingestion task to automatically retry on failure and send an admin alert email after 3 consecutive failures,  
**so that** the team is immediately notified of data pipeline issues and the system gracefully falls back to the last known FX rates.

---

## Acceptance Criteria

1. `EcbIngestionTask` retries up to 3 times with exponential backoff: 2s, 4s, 8s delays between attempts
2. After 3 failed attempts, the task sets `is_fallback = TRUE` on the most recent `fx_rates` entries for today's date (or writes a flag entry indicating fallback mode)
3. A SendGrid admin alert email is sent after 3 failures with: subject `"[ALERT] ECB FX Ingestion Failed"`, body containing timestamp, error message, and last successful ingestion date
4. The dashboard API (`sales-insights-api`) reads `is_fallback` status and returns `"Rates as of [last_date]"` in the response if fallback is active
5. On the next successful run, `is_fallback` is reset to `FALSE`
6. Unit tests: retry trigger (mock first 2 calls fail, 3rd succeeds), alert trigger (mock all 3 fail), fallback flag set correctly

---

## Tasks / Subtasks

- [ ] Add Spring Retry to `EcbIngestionTask` (AC: 1)
  - [ ] Annotate fetch method with `@Retryable(maxAttempts = 3, backoff = @Backoff(delay = 2000, multiplier = 2))`
  - [ ] Add `@EnableRetry` to scheduler config class
  - [ ] Confirm `spring-retry` dependency in `i2o-scheduler/pom.xml` (already present — verify)
- [ ] Add `@Recover` method for post-all-retries failure handling (AC: 2, 3)
  - [ ] Set fallback flag: insert/update `fx_rates` row with `is_fallback = TRUE` for today's date
  - [ ] Call `EmailService.sendAdminAlert()` with failure details
- [ ] Implement `sendAdminAlert()` addition to `EmailService` (AC: 3)
  - [ ] Subject: `"[ALERT] ECB FX Ingestion Failed - {date}"`
  - [ ] Body: timestamp, caught exception message, last successful `ingestion_date` from `fx_rates`
  - [ ] Recipient: admin email from application properties `scheduler.alert.admin-email`
- [ ] Add `is_fallback` field handling in `FxRatesRepository` (AC: 2, 5)
  - [ ] Query: `findLatestFallbackStatus()` — returns current fallback state
  - [ ] On success: `UPDATE fx_rates SET is_fallback = FALSE WHERE date = :today`
- [ ] Unit tests for retry and recovery (AC: 6)
  - [ ] Mock `OkHttpClient` to throw `IOException` on first 2 calls, succeed on 3rd
  - [ ] Verify `@Recover` not called when 3rd attempt succeeds
  - [ ] Mock all 3 calls failing → verify `EmailService.sendAdminAlert()` called once

---

## Dev Notes

**Repository:** `i2o-retail/i2o-scheduler`  
**Prerequisite stories:** GA-SI-01-S01 (table), GA-SI-01-S02 (base task)

**Spring Retry annotation pattern:**
```java
@Retryable(
    retryFor = {IOException.class, HttpException.class},
    maxAttempts = 3,
    backoff = @Backoff(delay = 2000, multiplier = 2.0)
)
private void fetchAndIngestEcbRates() { ... }

@Recover
public void handleIngestionFailure(Exception ex) {
    log.error("[ECB] All retries failed: {}", ex.getMessage());
    fxRatesRepository.setFallbackFlag(LocalDate.now());
    emailService.sendAdminAlert(
        "[ALERT] ECB FX Ingestion Failed",
        buildAlertBody(ex)
    );
}
```

**EmailService** already exists in `i2o-scheduler` (`com.corecompete.i2o.scheduler.service.EmailService`). Add an overloaded `sendAlert(String subject, String body)` method using the existing SendGrid template.

**Application properties addition:**
```properties
scheduler.ecb.admin-alert-email=devteam@company.com
scheduler.ecb.fallback-on-failure=true
```

**`is_fallback` dashboard contract:** `sales-insights-api`'s `/currencies` endpoint should return:
```json
{
  "currencies": ["EUR", "GBP", "USD"],
  "fxRatesDate": "2026-02-25",
  "isFallback": true,
  "message": "Rates as of 2026-02-25 (ECB feed unavailable)"
}
```

### Testing

- **Location:** `i2o-scheduler/src/test/java/.../task/EcbIngestionTaskRetryTest.java`
- **Framework:** JUnit 5 + Mockito + `@SpringBootTest` with Spring Retry context loaded
- **Key assertions:** `verify(emailService, times(1)).sendAdminAlert(...)` after 3 failures; `verify(fxRatesRepository, times(1)).setFallbackFlag(...)` 

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2026-02-26 | 1.0 | Initial story generation | AI Agent |

---

## Dev Agent Record
*(Populated during implementation)*

### Agent Model Used
_TBD_

### Debug Log References
_None yet_

### Completion Notes List
_None yet_

### File List
_None yet_

---

## QA Results
*(Populated by QA Agent)*
