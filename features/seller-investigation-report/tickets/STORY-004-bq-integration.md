# User Story: BigQuery Evidence Data Integration

## Story
**As a** Developer,
**I want** to source Buy Box and Marketplace identity data from BigQuery,
**so that** the investigation report content is accurate, fresh, and evidentiary.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Ensures the evidence provided to clients is data-backed and reflective of current marketplace conditions.
- **Technical (Bob-Builder)**: Requires performant SQL queries against `CC_I2O_DATA_MART` and mapping results to Java DTOs. High confidence based on existing `i2o-reseller` patterns.

## Acceptance Criteria
1. Extend `BigQueryService` to query `viz_bbx_filtered_detail`.
2. Implement data aggregation for: Buy Box ownership history, Marketplace violation counts, and Marketplace presence matrix.
3. Handle "Empty result" scenarios by returning a DTO with default values or "N/A" flags.

## Tasks
- [ ] [Backend] Write SQL aggregation logic for Buy Box history.
- [ ] [Backend] Implement `MarketplacePresence` data fetcher in `i2o-reseller`.
- [ ] [Backend] Create `InvestigationDataDTO` to wrap all BigQuery results.

## Dev Notes
Use vertical slices of evidence: Invoices, Test Buy records, and Brand Violations as defined in PRD.

### Architecture References
- Section 5.2: BigQuery Data Sources.
- Section 6.3: i2o-reseller Analytics Data APIs.

### Testing Standards
- **Frameworks**: JUnit 5, BigQuery Dry Run validation.
- **Requirements**: Verify zero-row results do not cause NullPointerExceptions in the PDF service.
