---
ticket_type: story
local_key: MPO-R9-ST-008
epic_ref: MPO-R9-EP-001
status: Draft
priority: P1
---

# User Story: Outbox Retry Scheduler and Observability Hardening

## Story
**As a** platform/support owner,
**I want** failed pilot/audit emails retried automatically with visibility,
**so that** client-confirmed requests are eventually delivered or escalated safely.

## Two-Agent Validation
- **User Value (Charlie-Conductor):** Preserves trust by honoring optimistic confirmations through reliable asynchronous delivery.
- **Technical (Bob-Builder):** Bounded implementation in `i2o-scheduler` (`MarketplaceOverviewEmailRetryJob`) with retry backoff, terminal failure handling, and metrics/logging.

## Acceptance Criteria
1. `i2o-scheduler` job polls `marketplace_email_outbox` for `PENDING`/`RETRYING` rows where `next_retry_at <= NOW()` and applies configured backoff schedule.
2. Rows transition deterministically across `PENDING -> RETRYING -> SENT/FAILED` with attempt counts and timestamps updated atomically.
3. Operational signals (retry count, terminal failures, lag) are emitted for monitoring and support alerting.

## Tasks
- [ ] Implement scheduler retry worker contract and state-transition logic in `i2o-scheduler` integration path (AC: 1, 2).
- [ ] Add backend observability hooks (structured logs + Micrometer counters/timers) for retry outcomes (AC: 3).
- [ ] Add tests for retry backoff sequencing, terminal failure, and successful resend cleanup (AC: 1, 2, 3).

## Dev Notes
Retry executor ownership is explicitly assigned to `i2o-scheduler` in release_9 decisions. Keep API-layer behavior aligned: synchronous pilot/audit endpoints may return `202` while delivery is finalized asynchronously.

### Architecture References
- `projects/marketplace-overview/release_9/docs/design/architecture.md` (Sections 10.3, 12.1.1, 13.4)
- `projects/marketplace-overview/release_9/docs/design/architecture-review.md` (AR-010 resolved decision)

### Testing Standards
- **Frameworks**: JUnit + integration tests (scheduler path), Testcontainers for DB-backed outbox semantics.
- **Requirements**: Validate retry window filtering, idempotent transitions, and terminal failure alerts.

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
