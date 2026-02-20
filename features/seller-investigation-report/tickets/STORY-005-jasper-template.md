# User Story: JasperReports Template Implementation

## Story
**As a** System,
**I want** to render beautifully styled and branded PDFs using JasperReports templates,
**so that** clients receive professional, legal-grade investigation reports.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Branded reports increase client confidence and perceived value of the i2o service. Mandated by PRD Success Metrics.
- **Technical (Bob-Builder)**: High dependency on `.jrxml` design accuracy. Complexity is in the multi-page/sub-report structure.

## Acceptance Criteria
1. Design `investigation_report.jrxml` master template with dynamic sub-reports for Profile, Buy Box, and History.
2. Include mandatory i2o logo (Header-Left) and Generation Date (Header-Right) on every page.
3. Include Confidentiality Footer on every page.
4. Implement data binding for all fields defined in the `InvestigationReportDTO`.

## Tasks
- [ ] [Design] Create master `.jrxml` with company styling (Inter font, i2o colors).
- [ ] [Design] Implement sub-reports for individual data sections.
- [ ] [Design] Embed assets (logo) in the project classpath.

## Dev Notes
Use `i2o_logo.png` as the primary branding asset. Ensure text wrapping handles long seller names correctly.

### Architecture References
- Section 10: PDF Report Template Design.
- Section 10.3: JasperReports Template Structure.

### Testing Standards
- **Requirements**: Visual validation of PDF layout across different data volumes (1 marketplace vs 10 marketplaces).
