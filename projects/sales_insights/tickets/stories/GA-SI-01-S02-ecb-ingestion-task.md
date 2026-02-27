# Story GA-SI-01-S02: EcbIngestionTask — Fetch, Validate & UPSERT ECB Exchange Rates

**Epic:** GA-SI-EPIC-01 — Automated ECB FX Rate Ingestion Pipeline  
**Story ID:** GA-SI-01-S02  
**Priority:** P0  
**Estimate:** 1.5 days  
**Status:** Draft

---

## Story

**As a** system,  
**I want** a scheduled task that fetches ECB daily XML exchange rates, validates the payload, and UPSERTs them into the `fx_rates` table,  
**so that** the FX rate store is always up-to-date with trusted, deduplicated ECB data.

---

## Acceptance Criteria

1. `EcbIngestionTask` implements `RunnableTask` interface in `i2o-scheduler` (same pattern as existing tasks e.g. `DataScrapingTask`)
2. Task fetches ECB XML from `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml` with a 10-second HTTP timeout
3. XML schema validation: checks content-type, root element `gesmes:Envelope`, and that ≥10 currencies are present
4. Sanity check: if any currency rate changes by >20% vs. the previous day's rate, the rate is flagged (`is_fallback = false`) and logged as WARNING (but still stored)
5. All valid currency/rate pairs UPSERTed: `INSERT INTO fx_rates ... ON CONFLICT (date, currency_code) DO UPDATE SET rate_to_eur = EXCLUDED.rate_to_eur`
6. Task is registered in the scheduler task registry and can be triggered via `POST /scheduler/execute {taskId: "ecb-fx-ingestion"}`
7. Unit tests cover: successful parse, XML validation failure, rate spike detection, UPSERT idempotency

---

## Tasks / Subtasks

- [ ] Create `EcbIngestionTask.java` in `i2o-scheduler` (AC: 1, 6)
  - [ ] Implement `RunnableTask` interface
  - [ ] Register task with `taskId = "ecb-fx-ingestion"` in task registry bean
- [ ] Implement ECB HTTP fetch with OkHttp (already in `i2o-scheduler` deps) (AC: 2)
  - [ ] 10s timeout on both connect and read
  - [ ] Validate `Content-Type` header is `application/xml` or `text/xml`
- [ ] Implement XML parsing and validation with standard Java DOM/SAX parser (AC: 3)
  - [ ] Assert root element = `gesmes:Envelope`
  - [ ] Assert at least 10 `Cube` currency entries exist
- [ ] Implement rate sanity check: query `fx_rates` for yesterday's rate and compare (AC: 4)
  - [ ] If |new_rate - old_rate| / old_rate > 0.20 → log WARNING
- [ ] Implement UPSERT via Spring Data JPA (AC: 5)
  - [ ] Use `@Query` with native SQL: `INSERT ... ON CONFLICT DO UPDATE`
  - [ ] Wrap all inserts in a single transaction
- [ ] Write unit tests with mocked OkHttp and mocked repository (AC: 7)
  - [ ] Test: normal XML → n rows upserted
  - [ ] Test: malformed XML → exception thrown, no DB write
  - [ ] Test: rate spike → WARNING logged, row still saved
  - [ ] Test: duplicate date → single clean row (UPSERT)

---

## Dev Notes

**Repository:** `i2o-retail/i2o-scheduler`  
**Package:** `com.corecompete.i2o.scheduler.task`  
**Key existing classes to follow:**
- `DataScrapingTask.java` — same pattern for `RunnableTask` implementation
- `GenericSchedulerTask.java` — shows task registration mechanism
- `SchedulerTaskService.java` — where tasks are looked up by `taskId`
- `EmailService.java` — used in S03 for alerts (not this story)

**ECB XML structure:**
```xml
<gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01"
                 xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
  <gesmes:subject>Reference rates</gesmes:subject>
  <Cube>
    <Cube time="2026-02-26">
      <Cube currency="USD" rate="1.0812"/>
      <Cube currency="GBP" rate="0.8342"/>
      <!-- ... more currencies ... -->
    </Cube>
  </Cube>
</gesmes:Envelope>
```

**Parse strategy:** Use `DocumentBuilderFactory` (standard Java). XPath: `//Cube[@currency]` to collect all `(currency, rate)` pairs. The `time` attribute of the parent `Cube` gives the date.

**FxRatesRepository — UPSERT native query:**
```java
@Modifying
@Transactional
@Query(value = """
    INSERT INTO fx_rates (date, currency_code, rate_to_eur, ingested_at, is_fallback)
    VALUES (:date, :currencyCode, :rateToEur, NOW(), false)
    ON CONFLICT (date, currency_code)
    DO UPDATE SET rate_to_eur = EXCLUDED.rate_to_eur,
                  ingested_at = NOW()
    """, nativeQuery = true)
void upsert(@Param("date") LocalDate date,
            @Param("currencyCode") String currencyCode,
            @Param("rateToEur") BigDecimal rateToEur);
```

**Dependencies already in `i2o-scheduler` pom.xml:** `okhttp3`, Spring Data JPA, Lombok, Spring Retry.

**Prerequisite:** Story GA-SI-01-S01 (table must exist).

### Testing

- **Location:** `i2o-scheduler/src/test/java/.../task/EcbIngestionTaskTest.java`
- **Framework:** JUnit 5 + Mockito (same as existing `i2o-scheduler` tests — see `src/test/`)
- **Mock:** `OkHttpClient` via Mockito; `FxRatesRepository` via `@MockBean`
- **Test XML fixtures:** Store 2–3 sample ECB XML files in `src/test/resources/ecb/`
- **Coverage target:** ≥80% line coverage on `EcbIngestionTask`

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
