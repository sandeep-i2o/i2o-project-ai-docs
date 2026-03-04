---
id: STORY-006
title: "[MO] Backend: i2o-reseller Sub-Package Scaffold, MarketplaceEnum & DTOs"
project: marketplace_overview
release: release_8
module: i2o-reseller
type: Story
priority: High
epic: EPIC-002
status: Draft
estimate: 1 day
created: 2026-03-04
---

# STORY-006 — Backend: i2o-reseller Sub-Package Scaffold, MarketplaceEnum & DTOs

## Context

This story creates the foundational Java package structure for the Marketplace Overview backend feature within `i2o-reseller`. It is a prerequisite for STORY-007 and STORY-008 which implement the two new endpoints. Follows the existing `i2o-reseller` package structure (Controller / Service / DTO / Enum layers).

## Module: `i2o-reseller`

### Package Structure to Create

```
com.corecompete.i2o/
└── marketplaceoverview/
    ├── controller/
    │   └── MarketplaceOverviewController.java   (stub — implemented in STORY-007/008)
    ├── service/
    │   ├── MarketplaceOverviewConfigService.java (stub — implemented in STORY-007)
    │   └── MarketplaceTrialEmailService.java    (stub — implemented in STORY-008)
    ├── dto/
    │   ├── MarketplaceConfigResponse.java
    │   ├── MarketplaceConfigItem.java           (activation status per marketplace)
    │   ├── BrandItem.java                       (id + name pair)
    │   └── InitiateTrialRequest.java
    └── enums/
        └── MarketplaceEnum.java                 (AMAZON, WALMART, EBAY, TARGET)
```

### Key DTO Specifications

**`MarketplaceConfigResponse.java`:**
```java
public class MarketplaceConfigResponse {
    private List<BrandItem> brands;
    private List<String> regions;
    private String defaultWeekStart;
    private String defaultWeekEnd;
    private List<MarketplaceConfigItem> marketplaceConfig;
}
```

**`InitiateTrialRequest.java`:**
```java
@Valid
public class InitiateTrialRequest {
    @NotNull @NotBlank
    private String brandId;
    @NotNull
    private MarketplaceEnum marketplace;
}
```

**`MarketplaceEnum.java`:**
```java
public enum MarketplaceEnum {
    AMAZON, WALMART, EBAY, TARGET
}
```

### Controller Stub

```java
@RestController
@RequestMapping("/marketplace-overview")
@RequiredArgsConstructor
public class MarketplaceOverviewController {
    // Methods implemented in STORY-007 and STORY-008
}
```

## Acceptance Criteria

1. Package `com.corecompete.i2o.marketplaceoverview` exists with `controller`, `service`, `dto`, `enums` sub-packages.
2. `MarketplaceEnum` defines AMAZON, WALMART, EBAY, TARGET values.
3. `MarketplaceConfigResponse` includes `brands`, `regions`, `defaultWeekStart`, `defaultWeekEnd`, `marketplaceConfig` fields.
4. `InitiateTrialRequest` has `@Valid`, `@NotNull`, `@NotBlank` annotations on `brandId` and `marketplace`.
5. `MarketplaceOverviewController` stub is annotated with `@RestController` and `@RequestMapping("/marketplace-overview")`.
6. Maven build passes with no compilation errors.

## Definition of Done Checklist

- [ ] Package scaffold created
- [ ] `MarketplaceEnum` created
- [ ] All 4 DTO classes created with Lombok / Jackson annotations
- [ ] Controller stub created with correct Spring annotations
- [ ] Maven build passes
- [ ] JavaDocs added to all public classes and methods

## Architecture References

- Section 5.2 — Backend sub-package structure
- Section 8.2 — DTO field specifications from API contracts
