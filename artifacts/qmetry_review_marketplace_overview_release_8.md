| ID | Story | Summary | Priority | Layer | Type |
|---|---|---|---|---|---|
| TC-001 | BP-MO-001-US001 | Marketplaces Overview tab is visible for BP-enabled users | Blocker | UI | Sanity |
| TC-002 | BP-MO-001-US001 | Marketplace Overview opens with default all-brand, all-region, last-week Card view | Blocker | UI | Feature |
| TC-003 | BP-MO-001-US001 | Marketplaces Overview tab is hidden for users without BP entitlement | High | UI | Regression |
| TC-004 | BP-MO-001-US001 | Direct URL access to Marketplace Overview is blocked for non-BP users | High | UI | Regression |
| TC-005 | BP-MO-001-US002 | Brand filter lists all account-associated brands | Blocker | UI | Feature |
| TC-006 | BP-MO-001-US002 | Brand filter supports multi-select and aggregates KPI output | High | UI | Regression |
| TC-007 | BP-MO-001-US002 | Region filter shows only account-enabled regions | Blocker | UI | Feature |
| TC-008 | BP-MO-001-US002 | Calendar defaults to last complete week and View by defaults to Card | Blocker | UI | Sanity |
| TC-009 | BP-MO-001-US002 | Switching Card and Table views retains active filters | High | UI | Regression |
| TC-010 | BP-MO-001-US002 | Unsupported brand-region combination shows stable empty state | Medium | UI | Regression |
| TC-011 | BP-MO-001-US003 | Amazon activated card renders Analytics, Brand Violation, and Enforcement sections | Blocker | UI | Feature |
| TC-012 | BP-MO-001-US003 | Walmart activated card omits Brand Violation section | High | UI | Feature |
| TC-013 | BP-MO-001-US003 | Non-activated eBay/Target cards show Initiate Trial and 3 summary KPIs | High | UI | Feature |
| TC-014 | BP-MO-001-US003 | Card switches from trial to activated layout after marketplace activation | High | UI | Regression |
| TC-015 | BP-MO-001-US003 | Zero KPI values are displayed as 0 in Card view | High | UI | Regression |
| TC-016 | BP-MO-001-US003 | Card KPI values honor selected brand-region-week filter scope | High | API | Regression |
| TC-017 | BP-MO-001-US004 | Table view renders one row per marketplace with PRD-defined KPI columns | Blocker | UI | Feature |
| TC-018 | BP-MO-001-US004 | Walmart Brand Violation columns display -- in Table view | High | UI | Regression |
| TC-019 | BP-MO-001-US004 | Non-activated marketplace rows show Initiate Trial action in Status column | High | UI | Feature |
| TC-020 | BP-MO-001-US004 | Table view renders pagination controls with default rows-per-page | Medium | UI | Sanity |
| TC-021 | BP-MO-001-US004 | Table data remains aligned with Card view for same filters | High | UI | Regression |
| TC-022 | BP-MO-001-US005 | Initiate Trial action sends support email with required subject and body | High | API | Feature |
| TC-023 | BP-MO-001-US005 | User sees success confirmation after trial request is triggered | High | UI | Feature |
| TC-024 | BP-MO-001-US005 | Multiple selected brands require explicit brand selection before sending trial request | High | UI | Regression |
| TC-025 | BP-MO-001-US005 | Repeat click prevention marks trial request as Requested or disables duplicate submission | Medium | UI | Regression |
| TC-026 | BP-MO-001-US005 | Email service failure surfaces actionable error and preserves retry path | Medium | API | Regression |
| TC-027 | BP-MO-001-US006 | Calendar defaults to last complete Monday-Sunday week on page load | High | UI | Sanity |
| TC-028 | BP-MO-001-US006 | Successful weekly aggregation refresh updates dashboard KPIs | High | API | Feature |
| TC-029 | BP-MO-001-US006 | Failed weekly aggregation shows stale data indicator with last available range | High | UI | Regression |
| TC-030 | BP-MO-001-US006 | KPI values remain stable during week and do not change mid-week | Medium | API | Regression |
| TC-031 | BP-MO-001-US006 | Historical weekly snapshots are retained for trend readiness | Medium | SQL_Query | Regression |
