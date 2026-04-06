---
ticket_type: story
local_key: MPO-R9-ST-007
epic_ref: MPO-R9-EP-001
status: Draft
priority: P1
---

# User Story: Audit Sample Banner and Download Flow

## Story
**As a** Brand Protection client,
**I want** to preview an audit sample report,
**so that** I can understand report scope before requesting a paid audit.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Reduces uncertainty and increases conversion on `Request Audit Report`.
- **Technical (Bob-Builder):** Simple signed-URL endpoint plus banner CTA integration; low complexity and isolated blast radius.

## Acceptance Criteria
1. `GET /marketplace-overview/audit-sample` returns signed URL and filename for static PDF object.
2. Banner (`Not sure what an audit includes?`) is rendered in unsubscribed column with accessible CTA.
3. Expired/invalid signed URL errors are handled with user-facing fallback message and retry affordance.

## Tasks
- [ ] Implement/verify backend signed URL generation for configured audit sample object path (AC: 1).
- [ ] Implement banner component CTA wiring, accessibility labels, and fallback messaging (AC: 2, 3).
- [ ] Add tests for signed URL success and expired URL error handling path (AC: 1, 3).

## Dev Notes
Keep this flow independent from WBR contract decisions. Audit sample remains a static PDF served via signed URL policy.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 6.5, 8.6, 9.4, 14)
- `projects/marketplace-overview/release_9/docs/requirements/prd.md` (US007)

### Testing Standards
- **Frameworks**: JUnit/Mockito, Jasmine/Karma, Playwright.
- **Requirements**: Validate banner visibility, keyboard access, and signed-URL error UX.

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
