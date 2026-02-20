# User Story: Seller Discovery Dashboard

## Story
**As an** Account Manager or Client User,
**I want** a structured dashboard with search, marketplace filters, and status badges,
**so that** I can easily locate and manage specific seller investigations.

## Two-Agent Validation
- **User Value (Charlie-Conductor)**: Provides the primary entry point for managing legal actions. Essential for user efficiency (FR1).
- **Technical (Bob-Builder)**: Uses standard `i2o-admin-UI` patterns (React + AG Grid). Confidence is high (< 3 days).

## Acceptance Criteria
1. Register route `/enforcement/investigation` in `App.tsx`.
2. Implement AG Grid in `SellerReportList.tsx` with columns: Seller ID, Business Name, Status, Last Notice, and Actions.
3. Filters for `report_status` (PENDING, READY) and Marketplace functionality working.
4. Search bar implementation with < 500ms latency.

## Tasks
- [ ] [Frontend] Scaffold `InvestigationModule` directory structure.
- [ ] [Frontend] Implement `InvestigationDashboard` and `SellerReportList` components.
- [ ] [Backend] Implement `POST /enforcement/investigation-report/list` in `i2o-admin`.
- [ ] [Integration] Connect `useInvestigationReports` hook to Backend API.

## Dev Notes
Leverage existing `i2o-admin-UI` components for consistency. Use TanStack Query for caching.

### Architecture References
- See Section 7.2 of `architecture-opus.md` (Frontend Components).
- See Section 11.1 (Module Structure).

### Testing Standards
- **Frameworks**: Vitest (Unit), Playwright (E2E).
- **Requirements**: 80% coverage on new components.
