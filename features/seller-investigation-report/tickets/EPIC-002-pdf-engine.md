# Epic: Professional Evidentiary PDF Generation Engine

## Business Value (Charlie-Conductor)
Enables the generation of high-fidelity, business-ready legal documents that aggregate complex multi-source evidence into a single professional PDF. Ensures 100% branding accuracy and real-time data freshness, which are critical for effective legal enforcement and client trust.

## Two-Agent Analysis
- **Strategic (Charlie)**: The PDF is the "tangible product" of the Cease & Desist ecosystem. It must be authoritative, branded, and legally defensible. This epic handles the critical data aggregation logic from BigQuery and PostgreSQL.
- **Technical (Bob)**: Medium complexity. Leverages the existing `i2o-formatted-reports` service. Primary technical challenge is mapping diverse BigQuery schemas into a unified JasperReports DTO and ensuring performant PDF generation.

## Success Metrics
- **Quality**: 100% of generated reports include mandatory headers, footers, and logo.
- **Performance**: PDF generation latency < 10 seconds for standard seller profiles.

## Technical Foundation (Bob-Builder)
- JasperReports Engine (embedded in `i2o-formatted-reports`).
- BigQuery Dynamic SQL aggregation.
- GCS signed URLs for secure download delivery.

## Architecture Components
From `architecture-opus.md`:
- `i2o-reseller`: `BigQueryService`, `ReportDataController`.
- `i2o-formatted-reports`: `InvestigationPDFService`, `JasperReports Engine`, `.jrxml` templates.

## Dependencies
- **External**: Access to `CC_I2O_DATA_MART.viz_bbx_filtered_detail` table.
- **Technical (Bob)**: Availability of JasperReports library in the classpath of `i2o-formatted-reports`.

## Implementation Readiness
- Ready: Yes (Template structure and API contracts defined).
- POC Needed: No.

## Stories Breakdown
- [ ] [STORY-004] BigQuery Evidence Data Integration - 3 days
- [ ] [STORY-005] JasperReports Template Implementation - 5 days
- [ ] [STORY-006] PDF Generation & Download Service - 4 days
