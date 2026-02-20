# User Story: PDF Generation & Download Service

## Story
**As a** System,
**I want** to assemble investigation data and trigger the Jasper engine on-the-fly,
**so that** users can download the most recent data as a PDF document.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Provides the "Action" phase of the feature. Success is measured by how quickly a user can move from viewing to downloading a valid report.
- **Technical (Bob-Builder)**: Orchestrates calls to BigQuery and the Jasper engine. High confidence by extending `i2o-formatted-reports`.

## Acceptance Criteria
1. Implement `POST /report/investigation-report` endpoint.
2. Assemble data from `BigQueryService` and `InvestigationReportRepository`.
3. Invoke Jasper Engine to render PDF byte stream.
4. Set filename format: `YYYYMMDD_sellerID_INVESTIGATION_REPORT.pdf`.

## Tasks
- [ ] [Backend] Implement `InvestigationPDFService` orchestration logic.
- [ ] [Backend] Configure REST endpoint with proper response headers for PDF download.
- [ ] [Backend] Implement dynamic filename generation logic.

## Dev Notes
Ensure the generation date on the report reflects the *download time* per NFR.

### Architecture References
- Section 6.2: i2o-formatted-reports API Specification.
- Section 8.2: Client Download Flow sequence diagram.
