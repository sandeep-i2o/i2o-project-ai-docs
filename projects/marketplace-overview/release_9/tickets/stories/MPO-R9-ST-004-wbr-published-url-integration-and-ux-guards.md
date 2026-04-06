---
ticket_type: story
local_key: MPO-R9-ST-004
epic_ref: MPO-R9-EP-001
status: Draft
priority: P0
---

# User Story: WBR Published URL Integration and UX Guards

## Story
**As a** Brand Protection client,
**I want** the WBR action to open the latest published report URL,
**so that** I can access my weekly business review without AM support.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** WBR access is a primary retention touchpoint and must be one-click from the overview page.
- **Technical (Bob-Builder):** Implementable through deterministic `schedule_wbr_details` lookup and `sw.gcs_location` JSON parsing with fallback when the current period is unavailable.

## Acceptance Criteria
1. `GET /marketplace-overview/wbr-report` resolves latest successful ARCHIVING row for org and returns the published `PPT url` from `sw.gcs_location` JSON.
2. UI handles missing report state with explicit message (`Report not yet available for this period`) and no broken navigation.
3. Click telemetry captures `mo_wbr_download_initiated`; completion is treated as approximate for release_9.

## Tasks
- [ ] Implement backend WBR query + JSON extraction for published URL, with org/period guards (AC: 1).
- [ ] Wire frontend WBR card action and unavailable-state UX with loading/disable behavior (AC: 2).
- [ ] Add API + UI tests for success and no-report branches; validate telemetry emission on click (AC: 2, 3).

## Dev Notes
Release_9 canonical artifact is published PPT URL (not zip/PDF bundle). This aligns with accepted risk AR-015 and leaves PRD wording update as a follow-up.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 6.4, 8.1, 8.3, 12.5)
- `projects/marketplace-overview/release_9/docs/design/architecture-review.md` (AR-012, AR-015)

### Testing Standards
- **Frameworks**: JUnit/Mockito/REST Assured, Jasmine/Karma, Playwright.
- **Requirements**: Validate published URL extraction from JSON payload and report-unavailable UX guard path.

## Story Draft Validation
Against checklist templates:
- `checklist/story-draft-checklist.md`
- `templates/story-draft-checklist.md` (fallback for missing `.aiccelerate` path)

### Goal and Context Clarity
- [x] Story purpose clear
- [x] Epic relationship evident
- [x] Dependencies identified

### Technical Implementation
- [x] Key files identified
- [x] Technologies specified
- [x] APIs described

### Self-Containment
- [x] Core information included
- [x] Assumptions explicit
- [x] Terms explained

**Validation Result**: READY
