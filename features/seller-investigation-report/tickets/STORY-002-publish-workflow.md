# User Story: AM Verification & Publish Workflow

## Story
**As an** Account Manager,
**I want** to preview report data and toggle status to 'READY',
**so that** I can verify evidence quality before releasing it to the client.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Enforces the Expert-Verified gateway, which is critical for legal risk mitigation.
- **Technical (Bob-Builder)**: Requires careful RBAC handling and audit log persistence in PostgreSQL.

## Acceptance Criteria
1. "Mark as Ready" toggle is ONLY visible to users with `INTERNAL_AM` role.
2. Status change persists to `investigation_report` table.
3. Every status change creates a record in `report_audit_log` with AM ID and timestamp.
4. Preview button opens `ReportHubDialog` populated with BigQuery data.

## Tasks
- [ ] [Backend] Create `PUT /enforcement/investigation-report/{id}/publish`.
- [ ] [Backend] Implement `report_audit_log` repository and service logic.
- [ ] [Frontend] Implement `ReportHubDialog` and `PublishToggle` components.
- [ ] [Frontend] Add RBAC check to the Publish action.

## Dev Notes
Ensure the UI state updates immediately after the mutation using `queryClient.invalidateQueries`.

### Architecture References
- Section 8.1: AM Preview & Publish Flow.
- Section 5.1: Database Schema.

### Testing Standards
- **Frameworks**: JUnit 5 (Backend), Vitest (Frontend).
- **Requirements**: Verify role-based gating prevents client-side publishing.
