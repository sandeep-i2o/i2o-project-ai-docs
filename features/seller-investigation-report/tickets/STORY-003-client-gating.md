# User Story: Client Access Gating & Download UI

## Story
**As a** Client User,
**I want** to see investigation progress but have the download disabled until verified,
**so that** I only use confirmed evidence for legal actions.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Protects the client from taking premature action on unverified data.
- **Technical (Bob-Builder)**: UI-side gating based on the `report_status` field. Low complexity.

## Acceptance Criteria
1. Download button in `SellerReportList` is disabled if `report_status` is `PENDING`.
2. Tooltip appears on disabled download button: "Report pending verification by Account Manager".
3. Download button triggers the PDF generation API if status is `READY`.

## Tasks
- [ ] [Frontend] Implement `DownloadButton` logic with status check and tooltips.
- [ ] [Frontend] Implement `useReportDownload` hook to handle blob responses.
- [ ] [Integration] Map PDF generation endpoint to the button click action.

## Dev Notes
Check Section 9.3 of `architecture-opus.md` for the explicit TypeScript logic for the DownloadButton.

### Architecture References
- Section 9.3: Download Button Gating Logic.
- Section 8.2: Client Download Flow.
