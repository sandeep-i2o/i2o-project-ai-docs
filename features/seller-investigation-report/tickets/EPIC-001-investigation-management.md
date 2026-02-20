# Epic: Centralized Seller Investigation Management & Workflow

## Business Value (Charlie-Conductor)
Automates the fragmented evidence collection process and establishes a "Truth-at-Source" verified evidentiary workflow. This reduces Account Manager (AM) manual overhead from hours to seconds and ensures legal consistency across client communications by gating unverified reports.

## Two-Agent Analysis
- **Strategic (Charlie)**: This is the core coordination point for C&D operations. It bridges the gap between raw data collection and legal actionability. Strategic alignment with the 2026 quality assurance roadmap for legal evidence.
- **Technical (Bob)**: High feasibility as it extends the existing `i2o-admin` and `i2o-admin-UI` ecosystems. The primary technical focus is on robust status management in PostgreSQL and real-time UI updates using TanStack Query.

## Success Metrics
- **Efficiency**: Average time to compile evidence reduced by 90%.
- **Integrity**: 100% of client-downloaded reports are AM-verified.

## Technical Foundation (Bob-Builder)
- PostgreSQL `investigation_report` and `report_audit_log` tables.
- Keycloak roles: `INTERNAL_AM` (can publish) and `CLIENT_USER` (can only download READY).

## Architecture Components
From `architecture-opus.md`:
- `i2o-admin-UI`: `InvestigationModule`, `InvestigationDashboard`, `ReportStatusBadge`, `DownloadButton`.
- `i2o-admin`: `InvestigationReportController`, `InvestigationReportService`.

## Dependencies
- **External**: BigQuery (`CC_I2O_DATA_MART`) for seller discovery.
- **Technical (Bob)**: RBAC middleware implementation in both Frontend and Backend.
- **Coordination (Charlie)**: Legal team sign-off on the "READY" status definition.

## Implementation Readiness
- Ready: Yes (Architecture and Data Models defined).
- POC Needed: No.

## Stories Breakdown
- [ ] [STORY-001] Seller Discovery Dashboard - 3 days
- [ ] [STORY-002] AM Verification & Publish Workflow - 4 days
- [ ] [STORY-003] Client Access Gating & Download UI - 2 days
