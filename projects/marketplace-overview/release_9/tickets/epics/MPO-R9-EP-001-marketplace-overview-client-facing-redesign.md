# Epic: Marketplace Overview Client-Facing Redesign (release_9)

## Metadata
- Local Key: `MPO-R9-EP-001`
- Project: `marketplace-overview`
- Release: `release_9`
- Source Mode: `local`
- Status: `Draft`

## Business Value (Charlie-Conductor)
Deliver a single client-facing Brand Protector overview so brand managers can review active coverage, request pilots/audits, and access WBR artifacts without AM-assisted workflows.

## Two-Agent Analysis
- Strategic (Charlie): The capability boundary is a single Marketplace Overview journey that combines visibility (active subscriptions), conversion actions (pilot/audit CTAs), and retention artifacts (WBR/audit sample) in one screen.
- Technical (Bob): Feasible on existing stack by reworking Angular module and adding bounded `i2o-reseller` endpoints; highest implementation risks are dependency readiness (bucket paths/contracts) and PRD-alignment deltas for US002/US004.

## Success Metrics
- Pilot requests submitted via screen (`mo_pilot_requested` trend).
- Audit requests submitted via screen (`mo_audit_requested` trend).
- WBR access rate (`mo_wbr_download_initiated`; completion via access-log approximation).
- Screen adoption (`mo_screen_viewed`).

## Technical Foundation (Bob-Builder)
- Frontend: `frontendapplication-i2oretail` `marketplace-overview` module rework.
- Backend: `i2o-reseller` `marketplaceoverview` package, `i2o-email-service` integration.
- Data: `org_market_mapping`, `brand_master`, `account/account_brand`, `ui_config`, `schedule_wbr_details`.
- Operations: `marketplace_pilot_requests`, `marketplace_email_outbox`, `i2o-scheduler` retry job.

## Architecture Components
From:
- `projects/marketplace-overview/release_9/docs/design/architecture.md`
- `projects/marketplace-overview/release_9/docs/design/architecture-review.md`
- `projects/marketplace-overview/release_9/docs/design/architecture-remediation.md`

Relevant components:
- `MarketplaceOverviewController`
- `MarketplaceOverviewConfigService`
- `MarketplaceWbrService`
- `MarketplacePilotService`
- `MarketplaceAuditService`
- Angular components: filter bar, subscription card, unsubscribed card, pilot/audit dialogs, audit sample banner

## Dependencies
- External: WBR/audit bucket readiness, SendGrid path validation.
- Technical: `org_market_mapping + marketplace` contract sign-off, `ui_config` property contract sign-off.
- Coordination: PRD text alignment for accepted risks (US002 placeholder scope, US004 published PPT contract).

## Implementation Readiness
- Ready: `Partially Ready`
- POC Needed: `No`, but dependency closures in architecture Section 10.5 remain required for production promotion.

## Stories Breakdown
- [ ] `MPO-R9-ST-001` Active subscription cards + module-gated navigation (2-3 days)
- [ ] `MPO-R9-ST-002` Unsubscribed cards placeholder implementation (1-2 days)
- [ ] `MPO-R9-ST-003` Brand/enforcement filter behavior + state handling (2 days)
- [ ] `MPO-R9-ST-004` WBR published URL integration + UX guards (2 days)
- [ ] `MPO-R9-ST-005` Start Free Pilot flow (validation, persistence, email) (2-3 days)
- [ ] `MPO-R9-ST-006` Request Audit flow (duplicate semantics + retry) (2-3 days)
- [ ] `MPO-R9-ST-007` Audit sample banner and download flow (1-2 days)
- [ ] `MPO-R9-ST-008` Retry scheduler + observability hardening (2 days)

