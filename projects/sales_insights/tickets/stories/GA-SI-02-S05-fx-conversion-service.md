# Story GA-SI-02-S05: `FxConversionService` — Multi-Currency Conversion Logic

**Epic:** GA-SI-EPIC-02 — Sales Insights API — Multi-Region Aggregation Service  
**Story ID:** GA-SI-02-S05  
**Priority:** P0  
**Estimate:** 1 day  
**Status:** Draft

---

## Story

**As a** system,  
**I want** a `FxConversionService` that converts sales revenue between any two supported currencies using historical `fx_rates` data,  
**so that** the aggregation API can return values in the user's chosen display currency accurately.

---

## Acceptance Criteria

1. `FxConversionService.convert(BigDecimal localValue, String fromCurrency, String toCurrency, LocalDate date)` returns the correctly converted value
2. If `fromCurrency == toCurrency`, the original `localValue` is returned (passthrough, no DB query)
3. If either currency is not found in `fx_rates` for the given date, throw `CurrencyNotSupportedException` (HTTP 422)
4. EUR is treated as the base: `converted = localValue ÷ rate_to_eur(from) × rate_to_eur(to)⁻¹`
5. Special case: `fromCurrency == "EUR"` → skip the divide step (rate_to_eur = 1.0)
6. `getSupportedCurrencies(LocalDate date)` returns a list of all currency codes available for that date
7. Unit tests verify: EUR passthrough, EUR→GBP, USD→GBP, unknown currency throws exception, edge case rate=0 throws `IllegalStateException`

---

## Tasks / Subtasks

- [ ] Create `FxConversionService.java` in `service/` package (AC: 1–6)
  - [ ] Inject `FxRatesRepository`
  - [ ] Implement `convert()` with formula: `value ÷ rate(from) × 1/rate(to)` all from `fx_rates`
  - [ ] Passthrough for `fromCurrency == toCurrency` (AC: 2)
  - [ ] Throw `CurrencyNotSupportedException` on missing rate (AC: 3)
  - [ ] Handle EUR base case (no lookup needed for EUR→EUR or EUR→X, AC: 5)
  - [ ] Implement `getSupportedCurrencies()` (AC: 6)
- [ ] Create `CurrencyNotSupportedException.java` (AC: 3)
  - [ ] Handled by `GlobalExceptionHandler` → HTTP 422 with body `{"error": "Currency Not Supported", "currency": "XYZ"}`
- [ ] Add to `FxRatesRepository` (AC: 1, 3, 6)
  - [ ] `Optional<FxRate> findByDateAndCurrencyCode(LocalDate date, String currencyCode)`
  - [ ] `List<String> findDistinctCurrencyCodesByDate(LocalDate date)`
- [ ] Write unit tests (AC: 7)
  - [ ] Mock repository; verify formula outputs match manual calculation

---

## Dev Notes

**Repository:** `i2o-retail/sales-insights-api`  
**Package:** `com.corecompete.i2o.salesinsights.service`

**Conversion formula (from architecture.md Section 8.5):**
```java
// EUR as base currency
// rate_to_eur for EUR = 1.0 (hardcoded, ECB feed doesn't include EUR)
BigDecimal fromRate = "EUR".equals(fromCurrency) ? BigDecimal.ONE
    : fxRatesRepository.findByDateAndCurrencyCode(date, fromCurrency)
        .orElseThrow(() -> new CurrencyNotSupportedException(fromCurrency))
        .getRateToEur();

BigDecimal toRate = "EUR".equals(toCurrency) ? BigDecimal.ONE
    : fxRatesRepository.findByDateAndCurrencyCode(date, toCurrency)
        .orElseThrow(() -> new CurrencyNotSupportedException(toCurrency))
        .getRateToEur();

// converted = localValue ÷ fromRate × toRate
// (normalise to EUR then convert to target)
return localValue
    .divide(fromRate, 10, RoundingMode.HALF_UP)
    .multiply(toRate)
    .setScale(2, RoundingMode.HALF_UP);
```

**Note:** ECB feed reports rates as `1 EUR = X foreign currency` stored as `rate_to_eur`. Double-check direction: ECB's `rate` attribute means "1 EUR = rate USD", so `rate_to_eur` in DB = ECB's `rate` value (i.e., how many units of that currency equal 1 EUR). Verify with sample data on first ingestion.

**`FxRate` JPA entity:**
```java
@Entity @Table(name = "fx_rates")
public class FxRate {
    @Id @EmbeddedId private FxRateId id; // composite: date + currencyCode
    private BigDecimal rateToEur;
    private Instant ingestedAt;
    private boolean isFallback;
}
```

### Testing

- **Location:** `src/test/java/.../service/FxConversionServiceTest.java`
- **Framework:** JUnit 5 + Mockito
- **Test cases:**
  - `convert(100, "EUR", "EUR", date)` → `100.00`
  - `convert(100, "EUR", "GBP", date)` where `GBP.rate_to_eur = 0.85` → `100 × 0.85 = 85.00`
  - `convert(100, "USD", "GBP", date)` where `USD.rate_to_eur = 1.08`, `GBP = 0.85` → `100 ÷ 1.08 × 0.85 = 78.70`
  - Unknown currency → `CurrencyNotSupportedException`
  - Rate = 0 → `ArithmeticException` / `IllegalStateException`

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
