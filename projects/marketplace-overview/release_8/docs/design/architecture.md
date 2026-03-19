# Architecture Document — Marketplace Overview
**Project:** BP-MO-001 | **Release:** release_8 | **Date:** 2026-03-13  
**Status:** Draft

---

## 1. Introduction & Goals

### 1.1 Purpose
This document describes the technical architecture for the **Marketplace Overview** feature under Brand Protector → Benefits. The feature consolidates KPI data from multiple sub-modules (Analytics, Brand Violations, Enforcement Centre) across four marketplaces (Amazon, Walmart, eBay, Target) into a single-screen dashboard with Card and Table view formats.

### 1.2 Quality Goals

| Priority | Goal | Metric |
|----------|------|--------|
| 1 | Performance | Dashboard loads < 3s (P95) |
| 2 | Correctness | KPI values match sub-module source of truth |
| 3 | Availability | 99.5% uptime for data read paths |
| 4 | Extensibility | Adding a 5th marketplace requires no core refactoring |
| 5 | Security | Role-based access — BP feature flag enforcement |

### 1.3 Stakeholders

| Role | Concern |
|------|---------|
| Brand Protection Users | Fast, consolidated KPI view per marketplace |
| Account Managers | Client reporting efficiency |
| Support Team | Receive Initiate Trial email alerts |
| Engineering Team | Maintainability, reuse of existing services |

---

## 2. Constraints & Assumptions

- **Reuse existing stack**: Angular 15 frontend, Spring Boot 3.x backends, BigQuery source warehouse, PostgreSQL metadata and KPI snapshot DB.
- **No new microservice** required for MVP — extend `i2o-reseller` with a new Marketplace Overview module.
- **Reuse existing generic APIs**: `POST /widget/getCardData` and `POST /report/getGridCardData` already exist in `i2o-reseller`; the Marketplace Overview feature will call these APIs with specific `query_id` and filter parameters — **no new data-fetch endpoints will be introduced** (decision confirmed 2026-03-04).
- **Weekly data refresh** only — KPI data is pre-aggregated weekly via `i2o-scheduler`.
- Email for "Initiate Trial" sent via existing `i2o-email-service` (SendGrid).
- Brand/Region filter data sourced from `i2o-master-data` (org-level brand + region metadata).
- Feature is gated by BP feature flag (existing Keycloak role check).
- Marketplace activation status stored in PostgreSQL (`i2o-master-data` org/marketplace entity).

---

## 3. System Context

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Browser (Angular 15)                        │
│         frontendapplication-i2oretail / marketplace-overview module │
└───────────────────┬────────────────┬────────────────────────────────┘
                    │ REST (HTTPS)   │ REST (HTTPS)
           ┌────────▼──────┐  ┌─────▼──────────────────┐
           │ i2o-reseller  │  │   i2o-email-service     │
           │ (Spring Boot) │  │   (Spring Boot/SendGrid)│
           └────────┬──────┘  └────────────────────────┘
                    │ JDBC / JPA
           ┌────────▼────────────────────────────────────┐
           │ PostgreSQL (i2oretail DB)                  │
           │ - marketplace_kpi_weekly_snapshot          │
           │ - marketplace_scheduler_audit_log          │
           │ - i2oretail.component / ui_config          │
           └─────────────────────────────────────────────┘
                    ▲
                    │ weekly upsert + audit write
           ┌────────┴────────────────────────────────────┐
           │ i2o-scheduler (Spring Boot)                │
           │ Reads BigQuery sources, writes PostgreSQL  │
           └────────┬────────────────────────────────────┘
                    │ BigQuery client (read-only sources)
           ┌────────▼────────────────────────────────────┐
           │ Google BigQuery (CC_I2O_DATA_MART/REPO)    │
           │ Source only: viz_lost_sales,               │
           │ reseller_progress_by_week,                 │
           │ listings_progress_by_week,                 │
           │ viz_reseller_filtered_detail, bp_wbr_detail│
           └─────────────────────────────────────────────┘

           ┌────────────────────────────────────────────┐
           │      i2o-master-data (Spring Boot)         │
           │  PostgreSQL — brand, org, marketplace data │
           └────────────────────────────────────────────┘
```

---

## 4. Solution Strategy & Project Modules

### 4.1 Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Frontend Module | New lazy-loaded Angular module inside `frontendapplication-i2oretail` | Follows existing module pattern |
| Data APIs (Card/Grid) | **Reuse** `POST /widget/getCardData` and `POST /report/getGridCardData` with BP-specific `query_id` values | Both APIs already exist in `i2o-reseller`; avoids duplicating data-fetch logic. **Confirmed: no new data-fetch endpoint will be created.** |
| Config / Filter API | New `GET /marketplace-overview/config` endpoint in `i2o-reseller` | Only new endpoint needed; returns brands, regions, activation status, default week |
| Initiate Trial API | New `POST /marketplace-overview/initiate-trial` endpoint in `i2o-reseller` | Calls `i2o-email-service` internally |
| Multi-brand Trial Enforcement | Frontend prompts user to select a single brand before firing request | Frontend-only enforcement (confirmed 2026-03-04); backend trusts the single `brandId` sent in the request payload |
| KPI Aggregation Store | PostgreSQL tables `marketplace_kpi_weekly_snapshot` and `marketplace_scheduler_audit_log` (both include `org_id`) | Release_8 update mandates relational storage with tenant key + durable scheduler audit trail |
| BQ Source Tables | `CC_I2O_DATA_MART.viz_lost_sales`, `reseller_progress_by_week`, `listings_progress_by_week`, `viz_reseller_filtered_detail`, `bp_wbr_detail` | Confirmed from `query_described.csv` — all pre-existing mart tables |
| Weekly Refresh | New `MarketplaceOverviewWeeklyAggregationTask` in `i2o-scheduler` | Scheduler already runs weekly migration tasks |
| Email Notification | Existing `i2o-email-service` via REST call from `i2o-reseller` | Centralized email service, avoids duplication |
| Activation Status | PostgreSQL table in `i2o-master-data` (`org_market_mapping`) | Confirmed table name; consistent with MDM patterns |

### 4.2 Modules Involved

| Module | Repository | Change Type |
|--------|-----------|-------------|
| `frontendapplication-i2oretail` | i2o-retail/frontendapplication-i2oretail | NEW Angular module |
| `i2o-reseller` | i2o-retail/i2o-reseller | NEW `marketplaceoverview` sub-package |
| `i2o-scheduler` | i2o-retail/i2o-scheduler | NEW weekly aggregation task |
| `i2o-email-service` | i2o-retail/i2o-email-service | No change — consumed as-is |
| `i2o-master-data` | i2o-retail/i2o-master-data | Existing `org_market_mapping` table used for activation status — no schema change required |

### 4.3 Update Delta (2026-03-13)

- **What changed:** Moved `marketplace_kpi_weekly_snapshot` and `marketplace_scheduler_audit_log` from BigQuery sink tables to PostgreSQL tables.
- **Why:** Release instruction requires both tables to be in PostgreSQL with `org_id` for tenant-scoped storage and auditability.
- **Impact on modules:** `i2o-scheduler` now writes snapshot + audit rows to PostgreSQL; `i2o-reseller` reads dashboard KPI rows from PostgreSQL; BigQuery remains source-only for raw KPI extraction.
- **Impact on APIs:** `POST /widget/getCardData` and `POST /report/getGridCardData` remain unchanged at contract level.
- **Impact on operations/tests:** Runbook, DDL, timeout handling, and integration testing updated for PostgreSQL persistence path.
- **ADR:** [ADR 13-03-2026](ADR/adr-13-03-2026.MD)

---

## 5. Building Block View

### 5.1 Frontend — Angular Module Structure

```
src/app/modules/marketplace-overview/
├── marketplace-overview.module.ts           # Feature module (lazy-loaded)
├── marketplace-overview-routing.module.ts   # Route: /brand-protector/benefits/marketplace-overview
├── components/
│   ├── marketplace-overview-page/          # Parent page component
│   │   ├── marketplace-overview-page.component.ts
│   │   ├── marketplace-overview-page.component.html
│   │   └── marketplace-overview-page.component.scss
│   ├── filter-bar/                         # Brand, Region, Calendar, View Toggle
│   │   ├── filter-bar.component.ts
│   │   ├── filter-bar.component.html
│   │   └── filter-bar.component.scss
│   ├── marketplace-card/                   # Card view — single marketplace card
│   │   ├── marketplace-card.component.ts
│   │   ├── marketplace-card.component.html
│   │   └── marketplace-card.component.scss
│   ├── marketplace-card-list/              # Card view — list wrapper
│   │   └── ...
│   ├── marketplace-table/                  # Table view — AG Grid table
│   │   ├── marketplace-table.component.ts
│   │   ├── marketplace-table.component.html
│   │   └── marketplace-table.component.scss
│   └── initiate-trial-dialog/             # Confirmation dialog for trial request
│       └── ...
├── services/
│   ├── marketplace-overview-api.service.ts     # HTTP calls to i2o-reseller backend
│   └── marketplace-overview-state.service.ts  # RxJS BehaviorSubject state management
└── models/
    ├── marketplace-kpi.model.ts                # Interfaces for KPI data
    ├── marketplace-filter.model.ts             # Filter state types
    └── marketplace-activation.model.ts         # Marketplace activation config
```

### 5.2 Backend — i2o-reseller API Strategy

#### Existing APIs (reused as-is)

| API | Endpoint | Usage |
|-----|---------|-------|
| `getCardData` | `POST /widget/getCardData` | Fetch KPI summary cards per marketplace (Card View) |
| `getGridCardData` | `POST /report/getGridCardData` | Fetch all marketplace KPIs in table/grid format (Table View) |

The frontend calls these APIs with BP Marketplace Overview-specific `query_id` values (registered in the `i2oretail.ui_config` component config table in PostgreSQL) and filter payload `{ marketplaces, brand, region, weekStart, weekEnd }`.

#### New Sub-Package (minimal additions)

```
com.corecompete.i2o/
└── marketplaceoverview/
    ├── controller/
    │   └── MarketplaceOverviewController.java   # Config + Initiate Trial endpoints only
    ├── service/
    │   ├── MarketplaceOverviewConfigService.java # Returns brands, regions, activation status, week defaults
    │   └── MarketplaceTrialEmailService.java     # Calls i2o-email-service
    ├── dto/
    │   ├── MarketplaceConfigResponse.java        # Config payload (brands, regions, week)
    │   └── InitiateTrialRequest.java             # Email trigger request
    └── enums/
        └── MarketplaceEnum.java                  # AMAZON, WALMART, EBAY, TARGET
```

> **Note:** Data retrieval (KPI cards, table rows) is handled entirely by the existing `getCardData` / `getGridCardData` generic query engine. Only 2 new endpoints are needed: config and initiate-trial.

### 5.3 Scheduler — New Weekly Task

```
com.corecompete.i2o.scheduler.task/
└── MarketplaceOverviewWeeklyAggregationTask.java
    # Runs every Monday 06:00 UTC (Cron: 0 6 * * MON)
    # Reads from Analytics, Brand Violations, Enforcement Centre BQ tables
    # Upserts into PostgreSQL marketplace_kpi_weekly_snapshot
    # Inserts status rows into PostgreSQL marketplace_scheduler_audit_log
```

---

## 6. Runtime View — Key Scenarios

### 6.1 Load Marketplace Overview Dashboard

> **Decision (confirmed 2026-03-04):** Data retrieval strictly uses the existing `POST /widget/getCardData` (Card view) and `POST /report/getGridCardData` (Table view) generic endpoints. No `GET /marketplace-overview/data` endpoint is introduced.

**Step 1 — Config load (on page entry):**
```
Browser                  i2o-reseller                        i2o-master-data
  │                           │                                      │
  │ GET /marketplace-overview/config                                 │
  │──────────────────────────>│                                      │
  │                           │── SELECT org_id, marketplace, is_activated ──>│
  │                           │   FROM org_market_mapping WHERE org_id=?       │
  │                           │<── activation status per marketplace ──────────│
  │                           │── SELECT brands, regions (org_id=?) ──────────>│
  │                           │<── brands[], regions[] ────────────────────────│
  │<── { brands, regions, defaultWeekStart, marketplaceConfig } ───────────────│
```

**Step 2 — Card view data load:**
```
Browser                  i2o-reseller                             PostgreSQL
  │                           │                                        │
  │ POST /widget/getCardData  │                                        │
  │ { componentId: "bp_marketplace_overview_card",                     │
  │   filters: { brand_id, region, start_date, end_date } }            │
  │──────────────────────────>│                                        │
  │                           │── SQL: SELECT * FROM marketplace_kpi_weekly_snapshot
  │                           │    WHERE org_id=:token_org_id AND brand_id=?       │
  │                           │      AND region=? AND week_start=?                  │
  │                           │───────────────────────────────────────>│
  │                           │<── KPI rows per marketplace ───────────│
  │<── card group response ───│                                        │
  │ Render Card view          │                                        │
```

**Step 3 — Table view data load (on toggle):**
```
Browser                  i2o-reseller                             PostgreSQL
  │                           │                                        │
  │ POST /report/getGridCardData                                       │
  │ { componentId: "bp_marketplace_overview_table",                    │
  │   filters: { brand_id, region, start_date, end_date },             │
  │   page: 0, pageSize: 10, sort: "marketplace ASC" }                │
  │──────────────────────────>│                                        │
  │                           │── same SQL query (org_id filtered) ───>│
  │                           │<── rows ──────────────────────────────│
  │<── grid row response ─────│                                        │
  │ Render Table view         │                                        │
```

### 6.2 Initiate Trial Email Flow

```
Browser          i2o-reseller           i2o-email-service         SendGrid
  │                   │                        │                       │
  │ POST /marketplace-overview/initiate-trial  │                       │
  │  {brand, marketplace}                      │                       │
  │──────────────────>│                        │                       │
  │                   │── POST /send-trial-email│                       │
  │                   │   {to: support@i2o,    │                       │
  │                   │    brand, marketplace} │                       │
  │                   │───────────────────────>│                       │
  │                   │                        │── SendGrid API ───────>│
  │                   │                        │<── 202 Accepted ───────│
  │                   │<── 200 OK ─────────────│                       │
  │<── { message: "Trial request sent" } ──────│                       │
  │ Show confirmation toast                    │                       │
```

### 6.3 Weekly KPI Aggregation (Scheduled)

```
i2o-scheduler                 BigQuery sources                    PostgreSQL sink
  │                                │                                   │
  │ [Monday 06:00 UTC]             │                                   │
  │ MarketplaceOverviewWeeklyAggregationTask.run()                     │
  │                                │                                   │
  │── SELECT Analytics KPIs ──────>>                                   │
  │   FROM CC_I2O_DATA_MART.viz_lost_sales                             │
  │   FROM CC_I2O_DATA_MART.reseller_progress_by_week                  │
  │   FROM CC_I2O_DATA_MART.listings_progress_by_week                  │
  │<<────────────────────────────── │                                   │
  │                                │                                   │
  │── SELECT BV/EC KPIs ──────────>>                                   │
  │   FROM CC_I2O_DATA_MART.viz_reseller_filtered_detail               │
  │   FROM CC_I2O_DATA_MART.bp_wbr_detail                              │
  │<<────────────────────────────── │                                   │
  │                                                                    │
  │───────────────────────────────────────────────────────────────────>>│
  │ UPSERT marketplace_kpi_weekly_snapshot                             │
  │ (org_id, week_start, marketplace, brand_id, region, KPI columns)  │
  │<<───────────────────────────────────────────────────────────────────│
  │                                                                    │
  │───────────────────────────────────────────────────────────────────>>│
  │ INSERT marketplace_scheduler_audit_log                             │
  │ (job_id, org_id, week_start, status='SUCCESS', completed_at)      │
  │<<───────────────────────────────────────────────────────────────────│
```

---

## 7. Data Architecture

### 7.1 BigQuery Source Tables (Confirmed from `query_described.csv`)

| KPI Category | Source Table | Key Columns Used |
|-------------|-------------|------------------|
| **Analytics — Lost Sales** | `CC_I2O_DATA_MART.viz_lost_sales` | `lost_sales`, `lost_sales_units`, `marketplace`, `region`, `period`, `reporting_range` |
| **Analytics — Reseller Removed / Buybox Win** | `CC_I2O_DATA_MART.reseller_progress_by_week` | `closed_reseller_count`, `buy_box_winning_reseller_count_closed`, `week_date` |
| **Analytics — Closed Listings** | `CC_I2O_DATA_MART.listings_progress_by_week` | `List_Count_Closed`, `Cumm_List_Count_Closed`, `week_date` |
| **Brand Violations** | `CC_I2O_DATA_MART.viz_reseller_filtered_detail` (via `enforcement_status` CTE) | Brand violation counts per marketplace |
| **Enforcement Centre** | `CC_I2O_DATA_MART.bp_wbr_detail` | `queue`, `cnd_pending`, `total_cnd_sent`, `test_purchase` |
| **Marketplace Filter Lookup** | `CC_I2O_DATA_REPO.marketplace` | `platform`, `platform_priority_order` |
| **Marketplace Filter Dropdown** | `CC_I2O_DATA_MART.viz_lost_sales` JOIN `CC_I2O_DATA_REPO.marketplace` | DISTINCT marketplace values ordered by priority |

### 7.2 PostgreSQL Snapshot Table: `marketplace_kpi_weekly_snapshot`

> **AR-001 Fix:** `org_id` is added as a mandatory key column to enforce tenant isolation. All scheduler writes and read queries filter by `org_id`. This resolves the P0 data-isolation gap.

```sql
CREATE TABLE IF NOT EXISTS marketplace_kpi_weekly_snapshot (
  id                    BIGSERIAL PRIMARY KEY,
  -- Tenant isolation key (mandatory — all queries must filter by this column)
  org_id                BIGINT NOT NULL,
  week_start            DATE NOT NULL,
  week_end              DATE NOT NULL,
  marketplace           VARCHAR(32) NOT NULL,   -- AMAZON | WALMART | EBAY | TARGET
  brand_id              BIGINT NOT NULL,
  region                VARCHAR(32) NOT NULL,   -- US | UK | DE | etc.
  -- Analytics KPIs (from viz_lost_sales + reseller_progress_by_week + listings_progress_by_week)
  lost_sales            NUMERIC(18,2),
  total_closed_listings BIGINT,
  reseller_removed      BIGINT,
  buybox_win_pct        NUMERIC(7,2),
  -- Brand Violation KPIs (nullable for Walmart — from viz_reseller_filtered_detail)
  total_brand_violation BIGINT,
  violations_closed     BIGINT,
  -- Enforcement Centre KPIs (from bp_wbr_detail)
  notification_in_queue BIGINT,
  cnd_pending           BIGINT,
  total_cnd_sent        BIGINT,
  test_purchase         BIGINT,
  -- Trial Marketplace KPIs (for eBay/Target — subset of above sources)
  no_of_listings        BIGINT,
  no_of_resellers       BIGINT,
  wow_change_pct        NUMERIC(7,2),
  -- Metadata
  data_staleness_flag   BOOLEAN NOT NULL DEFAULT FALSE,
  created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  CONSTRAINT uq_marketplace_kpi_snapshot
    UNIQUE (org_id, week_start, marketplace, brand_id, region)
);

CREATE INDEX IF NOT EXISTS idx_marketplace_kpi_snapshot_lookup
  ON marketplace_kpi_weekly_snapshot (org_id, brand_id, region, week_start DESC);
-- Primary access pattern: WHERE org_id=? AND brand_id=? AND region=? AND week_start=?
-- Cross-tenant isolation: org_id is extracted from the Keycloak Bearer token at request time and injected into every PostgreSQL query by i2o-reseller. It is never trusted from the client request payload.
```

### 7.3 PostgreSQL Entity: `org_market_mapping` (in i2o-master-data)

> **Table name confirmed 2026-03-04:** The existing table is `org_market_mapping` — no schema migration required.

```sql
-- Existing table in i2o-master-data (read-only from i2o-reseller)
SELECT org_id, marketplace, is_activated, activated_at, regions_enabled
FROM org_market_mapping
WHERE org_id = ?;
-- Used by GET /marketplace-overview/config to populate activation status per marketplace.
```

### 7.4 Key TypeScript Interfaces (Frontend)

```typescript
// models/marketplace-kpi.model.ts

export type ViewMode = 'card' | 'table';
export type MarketplaceName = 'AMAZON' | 'WALMART' | 'EBAY' | 'TARGET';
export type MarketplaceStatus = 'ACTIVATED' | 'TRIAL';

export interface MarketplaceFilter {
  brandIds: string[];        // selected brand IDs
  region: string;            // e.g., 'US'
  weekStart: string;         // ISO date string (Monday)
  weekEnd: string;           // ISO date string (Sunday)
  viewMode: ViewMode;
}

export interface KpiGroup {
  category: string;          // 'Analytics' | 'Brand Violation' | 'Enforcement Centre'
  kpis: KpiItem[];
}

export interface KpiItem {
  label: string;             // e.g., 'Lost Sales'
  value: number | null;      // null = N/A (shown as --)
  format: 'number' | 'currency' | 'percentage';
}

export interface MarketplaceCard {
  marketplace: MarketplaceName;
  logoUrl: string;
  countryFlag: string;
  status: MarketplaceStatus;
  kpiGroups: KpiGroup[];     // empty for trial marketplaces (use trialKpis)
  trialKpis?: KpiItem[];     // only for trial: Listings, Resellers, WoW
  dataStalenessFlag: boolean;
}

export interface MarketplaceOverviewResponse {
  weekStart: string;
  weekEnd: string;
  cards: MarketplaceCard[];
  staleDateRange?: string;   // only if staleness detected
}
```

---

## 8. API Specification

### 8.1 Reused `i2o-reseller` APIs (no changes required)

#### `POST /widget/getCardData` — Marketplace KPI Card View
Used by the frontend to load KPI summary cards per marketplace.

**Request payload (example for BP Marketplace Overview card):**
```json
{
  "componentId": "bp_marketplace_overview_card",
  "filters": {
    "marketplace": ["AMAZON", "WALMART"],
    "brand": ["brand_001"],
    "region": "US",
    "start_date": "2026-02-24",
    "end_date": "2026-03-02"
  }
}
```
The `componentId` maps to a component registered in `i2oretail.component` (PostgreSQL), which references the specific `query_id` entries for BP Marketplace Overview KPIs in `query_described.csv`-equivalent config.

#### `POST /report/getGridCardData` — Marketplace KPI Table View
Used for the Table view layout. Same filter contract as `getCardData`, returns rows instead of card groups.

> **AR-006 Fix:** Default `pageSize` corrected to `10` (PRD US004 requirement) and default sort set to `marketplace ASC` (PRD US004 alphabetical sort rule).

```json
{
  "componentId": "bp_marketplace_overview_table",
  "filters": {
    "marketplace": ["AMAZON", "WALMART", "EBAY", "TARGET"],
    "brand": ["brand_001"],
    "region": "US",
    "start_date": "2026-02-24",
    "end_date": "2026-03-02"
  },
  "page": 0,
  "pageSize": 10,
  "sort": "marketplace ASC"
}
```

> **Business rule (PRD US004):** Default page size is `10`. Default column sort is `marketplace ASC` (alphabetical). Column-level sorting is optional for MVP.

### 8.2 New `i2o-reseller` Endpoints (Marketplace Overview only)

#### GET `/marketplace-overview/config`
Returns filter metadata (brands, enabled regions, current week range, activation status per marketplace).

**Response:**
```json
{
  "brands": [{ "id": "brand_001", "name": "Nike" }],
  "regions": ["US", "UK"],
  "defaultWeekStart": "2026-02-24",
  "defaultWeekEnd": "2026-03-02",
  "marketplaceConfig": [
    { "marketplace": "AMAZON", "status": "ACTIVATED" },
    { "marketplace": "WALMART", "status": "ACTIVATED" },
    { "marketplace": "EBAY",   "status": "TRIAL" },
    { "marketplace": "TARGET", "status": "TRIAL" }
  ]
}
```

#### POST `/marketplace-overview/initiate-trial`
Triggers email to support team.

> **AR-003 Decision (confirmed 2026-03-04):** Multi-brand disambiguation is enforced by the frontend only. The frontend prompts the user to select a single brand before the request is fired. The backend trusts the single `brandId` provided in the payload. The `brandName` is derived server-side from `i2o-master-data` using `brandId` to prevent client injection into the email subject/body.

**Request:**
```json
{
  "brandId": "brand_001",
  "marketplace": "EBAY"
}
```

> Note: `brandName` is intentionally omitted from the request — `i2o-reseller` derives the brand name from `i2o-master-data` using `brandId` before constructing the email. This prevents email-content injection via client-supplied strings.

**Response:**
```json
{
  "success": true,
  "message": "Trial request sent successfully."
}
```

**Frontend pre-condition (enforced by Angular component):**
- If `filterState.brandIds.length > 1`, the Initiate Trial button opens a brand-selection dialog. The API call is only fired once the user selects a single brand from the dialog.
- If `filterState.brandIds.length === 1`, the API call fires immediately.

### 8.3 Email Payload to `i2o-email-service`

The `MarketplaceTrialEmailService` in `i2o-reseller` calls:

```
POST {email-service-url}/send
{
  "to": ["support@i2oretail.com"],
  "subject": "Initiate L1 report for {Brand Name}",
  "body": "Hey Team, can you run L1 audit for {Brand Name} on {Marketplace}",
  "template": "plain_text"
}
```

---

## 9. Frontend Architecture

### 9.1 Routing

Add to `app-routing.module.ts`:
```typescript
{
  path: 'brand-protector/benefits/marketplace-overview',
  loadChildren: () => import('./modules/marketplace-overview/marketplace-overview.module')
    .then(m => m.MarketplaceOverviewModule),
  canActivate: [KeycloakAuthGuard, RoleBasedAuthGuard],
  data: { roles: ['brand-protector'] }
}
```

### 9.2 State Management Pattern

Uses existing RxJS `BehaviorSubject` pattern (consistent with codebase):

```typescript
// marketplace-overview-state.service.ts
@Injectable({ providedIn: 'root' })
export class MarketplaceOverviewStateService {
  private filterSubject = new BehaviorSubject<MarketplaceFilter>(DEFAULT_FILTER);
  private dataSubject = new BehaviorSubject<MarketplaceOverviewResponse | null>(null);
  private loadingSubject = new BehaviorSubject<boolean>(false);

  filter$ = this.filterSubject.asObservable();
  data$ = this.dataSubject.asObservable();
  loading$ = this.loadingSubject.asObservable();

  setFilter(filter: Partial<MarketplaceFilter>): void { ... }
  loadData(): void { ... }  // triggers API call, updates dataSubject
}
```

### 9.3 Component Interaction Diagram

```
MarketplaceOverviewPageComponent
  │
  ├── FilterBarComponent
  │     ├── Brand multi-select (PrimeNG Dropdown)
  │     ├── Region dropdown (PrimeNG Dropdown)
  │     ├── Calendar (PrimeNG Calendar, week mode)
  │     └── View toggle (Card | Table)    → emits filterChange event
  │
  ├── [*ngIf="viewMode === 'card'"]
  │   MarketplaceCardListComponent
  │     └── MarketplaceCardComponent × N
  │           ├── Activated Badge (green)
  │           ├── KpiGroupComponent × N
  │           │   └── KpiItemComponent × N
  │           └── [*ngIf="status === 'TRIAL'"]
  │               InitiateTrialButtonComponent
  │
  └── [*ngIf="viewMode === 'table'"]
      MarketplaceTableComponent (AG Grid Community)
        ├── Column: Marketplace (logo + name)
        ├── Columns: KPI values (10 total)
        └── Column: Status (badge | Initiate Trial button)
```

### 9.4 Default Filter State

```typescript
const DEFAULT_FILTER: MarketplaceFilter = {
  brandIds: [],          // empty = all brands
  region: '',            // empty = all regions
  weekStart: getLastMonday(),
  weekEnd: getLastSunday(),
  viewMode: 'card'
};
```

---

## 10. Integration Design

### 10.1 External Dependencies

| Dependency | Service | Type | Notes |
|------------|---------|------|-------|
| `CC_I2O_DATA_MART.viz_lost_sales` | BigQuery | Read (aggregation) | Lost sales per marketplace/region/period |
| `CC_I2O_DATA_MART.reseller_progress_by_week` | BigQuery | Read (aggregation) | Reseller removed, buybox win counts |
| `CC_I2O_DATA_MART.listings_progress_by_week` | BigQuery | Read (aggregation) | Closed listing counts per week |
| `CC_I2O_DATA_MART.viz_reseller_filtered_detail` | BigQuery | Read (aggregation) | Brand violation KPIs via enforcement_status CTE |
| `CC_I2O_DATA_MART.bp_wbr_detail` | BigQuery | Read (aggregation) | Enforcement Centre KPIs (queue, C&D, test purchase) |
| `marketplace_kpi_weekly_snapshot` | PostgreSQL (i2o-reseller DB) | Read/Write | Aggregated weekly destination table keyed by `org_id` |
| `marketplace_scheduler_audit_log` | PostgreSQL (i2o-reseller DB) | Write/Read | Scheduler execution status per org/week |
| `CC_I2O_DATA_REPO.marketplace` | BigQuery | Read | Marketplace filter dropdown with priority order |
| `i2oretail.component` / `ui_config` | PostgreSQL (i2o-reseller) | Read | Component config linking componentId → query_id for getCardData/getGridCardData |
| `org_market_mapping` | i2o-master-data (PostgreSQL) | Read | Activation status per org/marketplace |
| Brand/region metadata | i2o-master-data | Read | For filter dropdowns |
| Email sending | i2o-email-service | REST call | SendGrid delivery |
| Weekly cron | i2o-scheduler | Internal task | Aggregation job |
| Auth | Keycloak | Token injection | Existing interceptor |

### 10.2 Error Handling Strategy

| Scenario | Handling |
|----------|---------|
| PostgreSQL query timeout | Return 504; frontend shows "Data temporarily unavailable" |
| Stale data (aggregation job failed) | Return last available week + `dataStalenessFlag: true`; frontend shows stale data banner with date range. Alert fires if >24h since last successful scheduler run (see Section 17). |
| Scheduler job failure | Retry up to 3 times with 30-minute backoff. After all retries exhausted, write `status='FAILED'` to `marketplace_scheduler_audit_log` in PostgreSQL and trigger PagerDuty alert. On-call team follows Section 17 runbook. |
| Email service unreachable | Return 503; frontend shows "Failed to send — please try again" |
| No KPIs available for a marketplace | Return 0 for all KPIs (not hidden) |
| N/A KPI for marketplace (e.g., BV for Walmart) | Return `null`; frontend renders `--` |
| Multiple brands selected → Initiate Trial | **Frontend-only enforcement (confirmed 2026-03-04):** Angular component blocks the API call and opens a brand-selection dialog. The backend trusts the single `brandId` sent in the payload. |

---

## 11. Deployment & Infrastructure

### 11.1 Deployment Targets

| Component | Platform | Packaging |
|-----------|----------|-----------|
| Angular frontend | GCP App Engine / CDN | `npm run build_prod` → dist/i2o-retail |
| i2o-reseller | GCP App Engine | WAR file (Maven) |
| i2o-scheduler | GCP App Engine / Docker | WAR / Container |
| i2o-email-service | GCP Cloud Run | Docker container |
| i2o-master-data | GCP App Engine | WAR file (Maven) |

### 11.2 Environment Configuration

i2o-reseller `application-{env}.properties` additions:
```properties
# Marketplace Overview — PostgreSQL Snapshot/Audit
marketplace.pg.snapshot-table=marketplace_kpi_weekly_snapshot
marketplace.pg.audit-table=marketplace_scheduler_audit_log
marketplace.pg.query-timeout-ms=2000

# Marketplace Overview — Email Service
marketplace.email-service.url=https://{email-service-url}
marketplace.trial.support-email=support@i2oretail.com
```

i2o-scheduler additions:
```properties
# Weekly aggregation cron (Monday 06:00 UTC)
scheduler.marketplace-overview.cron=0 6 * * MON
```

---

## 12. Security Architecture

| Concern | Approach |
|---------|---------|
| Authentication | Keycloak Bearer token — existing `KeycloakBearerInterceptor` |
| Authorization | `RoleBasedAuthGuard` — `brand-protector` role required |
| Data isolation | `org_id` extracted from Keycloak token at request time; injected into all PostgreSQL reads/writes as mandatory `WHERE org_id=?` / `VALUES (:org_id)` clauses. `org_id` is never accepted from client request payload. Snapshot uniqueness is enforced by `(org_id, week_start, marketplace, brand_id, region)` (Section 7.2). Cross-tenant integration tests are required (Section 14.2). |
| API validation | Spring `@Valid` on all request DTOs; reject unknown fields |
| Email injection prevention | `brandName` derived server-side from `i2o-master-data` using `brandId`; user-supplied strings are never interpolated directly into email subject/body |
| Rate limiting | Initiate Trial endpoint: 1 request per marketplace per brand per hour (server-side check against PostgreSQL) |

---

## 13. Performance Design

| Concern | Strategy |
|---------|---------|
| Dashboard load time | PostgreSQL `marketplace_kpi_weekly_snapshot` is pre-aggregated weekly; indexed lookup with 3-4 filters targets < 1s |
| Filter config API | Cache brand/region metadata in Spring in-memory cache (TTL 5 min) |
| Frontend rendering | AG Grid virtual scroll for table; Card view deferred rendering with `@defer` or `OnPush` |
| Cold start | Warm-up via App Engine `/_ah/warmup` for i2o-reseller |

---

## 14. Testing Strategy

### 14.1 Unit Tests

| Layer | Tool | Coverage Target |
|-------|------|----------------|
| Angular services | Jasmine/Karma | 80% |
| Angular components | Jasmine/Karma | 70% |
| Spring Boot services | JUnit 5 + Mockito | 80% |
| Scheduler task | JUnit 5 + Mockito | 70% |

### 14.2 Integration Tests
- Spring Boot `@SpringBootTest` for `MarketplaceOverviewController` with PostgreSQL repository/integration fixtures for `marketplace_kpi_weekly_snapshot`
- Scheduler integration tests with mock BigQuery source responses and PostgreSQL sink writes (`marketplace_kpi_weekly_snapshot`, `marketplace_scheduler_audit_log`)
- Angular `HttpClientTestingModule` for API service tests
- **Cross-tenant isolation test (required — AR-001):** Create two orgs (`org_A`, `org_B`). Insert snapshot rows for `org_A`. Assert that queries scoped to `org_B` return zero rows. Assert that `org_id` is never derived from the request payload.

### 14.3 E2E Test Scenarios (User Stories → AC)

| Story | Scenario | AC |
|-------|---------|-----|
| US001 | Tab visible for BP user, hidden for non-BP | AC 6–9 |
| US002 | Filter defaults; filter persistence on view toggle | AC 17–21 |
| US003 | Amazon card shows 3 KPI sections; eBay shows trial card | AC 29–34 |
| US004 | Table view renders with `--` for Walmart BV columns | AC 41–44 |
| US005 | Initiate Trial triggers confirmation; multi-brand prompts brand selection | AC 50–53 |
| US006 | Calendar defaults to last complete week | AC 59–62 |

---

## 15. Architecture Quality Checklist

| # | Category | Item | Status | Evidence / Notes |
|---|----------|------|--------|-----------------|
| 1 | Alignment | Architecture covers all 6 user stories from PRD | ✅ PASS | All US001–US006 addressed |
| 2 | Reuse | Existing services reused (no new microservice) | ✅ PASS | i2o-reseller, i2o-scheduler, i2o-email-service, i2o-master-data |
| 3 | Data | PostgreSQL snapshot + audit persistence aligned with release change | ✅ PASS | Section 7.2 and Section 17 define PostgreSQL DDL, indexes, and write path |
| 4 | Security | Tenant isolation enforced at data layer | ✅ PASS | `org_id` is mandatory for snapshot/audit tables (Section 7.2 and Section 17); all reads/writes enforce `org_id` from token (Section 12); cross-tenant integration test required (Section 14.2). |
| 5 | Security | Auth/Authz defined | ✅ PASS | Keycloak + RoleBasedAuthGuard |
| 6 | API Contract | Data retrieval endpoint contract resolved | ✅ PASS | Confirmed: reuse `getCardData`/`getGridCardData` only; no `GET /marketplace-overview/data` (Section 6.1, Section 8.1). |
| 7 | Resilience | Stale data fallback + alerting defined | ✅ PASS | Section 10.2 — staleness flag + banner + PagerDuty alert >24h + retry policy (Section 17). |
| 8 | Resilience | Email failure handling defined | ✅ PASS | 503 + frontend retry message |
| 9 | Extensibility | 5th marketplace addition = zero core refactoring | ✅ PASS | `MarketplaceEnum` + `org_market_mapping` table |
| 10 | Frontend | Consistent with existing Angular patterns | ✅ PASS | Lazy module, PrimeNG, AG Grid, BehaviorSubject state |
| 11 | Backend | Consistent with existing Spring Boot patterns | ✅ PASS | Controller/Service/DTO/JPA repository pattern in i2o-reseller + scheduler |
| 12 | Testing | Testing strategy covers unit + integration + E2E | ✅ PASS | Section 14; cross-tenant isolation test added (Section 14.2). |
| 13 | Performance | Pre-aggregation prevents slow request-time computation | ✅ PASS | Weekly snapshot table in PostgreSQL + lookup index + in-memory metadata cache |
| 14 | Rate Limiting | Initiate Trial spam prevention | ✅ PASS | Server-side rate limit (1/hour/marketplace/brand) |
| 15 | Input Validation | Email injection prevention | ✅ PASS | `brandName` derived server-side from master-data; not trusted from client. |
| 16 | N/A KPIs | Walmart Brand Violation appears as `--` not `0` | ✅ PASS | `null` value → frontend renders `--` |
| 17 | Table Defaults | Sort and pageSize match PRD US004 | ✅ PASS | `pageSize: 10`, `sort: marketplace ASC` in `getGridCardData` contract (Section 8.1). |

> **Updated 2026-03-04:** BigQuery source table names confirmed from `query_described.csv`. API strategy confirmed: reuse existing `getCardData` and `getGridCardData` only. `org_id` tenant isolation gaps (AR-001) resolved. Table name corrected to `org_market_mapping`.
>
> **Updated 2026-03-13:** Storage decision updated for release_8. `marketplace_kpi_weekly_snapshot` and `marketplace_scheduler_audit_log` are now PostgreSQL tables keyed by `org_id`. See [ADR 13-03-2026](ADR/adr-13-03-2026.MD).

**Overall Confidence Score: 8/10** — Architecture is conditionally implementation-ready. The component `componentId` registration (Open Item #2) is a **hard go/no-go gate** before frontend integration begins. All other changes are implementable.

---

## 16. Open Items & Risks

| # | Item | Owner | Due | Gate? | Risk Level |
|---|------|-------|-----|-------|------------|
| 1 | ~~Confirm BigQuery source table names~~ | Data Team | ✅ RESOLVED | — | ✅ Closed |
| 2 | **Register BP Marketplace Overview `componentId` values** in `i2oretail.component` PostgreSQL table — required to wire `getCardData`/`getGridCardData` calls. Steps: (a) create `bp_marketplace_overview_card` and `bp_marketplace_overview_table` component entries pointing to correct `query_id` rows. (b) Deploy config changes to DEV, then QA, then PROD before frontend integration testing begins. | Engineering Lead | Week 1 | 🚦 **GO/NO-GO GATE** — Frontend integration testing is blocked until this is done | 🔴 High |
| 3 | Confirm support team email address for Initiate Trial | PM/Ops | Week 4 | No | 🟡 Medium |
| 4 | ~~Confirm `org_marketplace_config` table~~ | Engineering | ✅ RESOLVED | — | ✅ Closed — table is `org_market_mapping`, no migration needed |
| 5 | Confirm eBay/Target BQ data availability for trial KPIs (Listings, Resellers, WoW) | Data Team | Week 2 | No | 🟡 Medium |
| 6 | Confirm `bp_wbr_detail` column names for Enforcement Centre KPIs | Data Team | Week 1 | No | 🟡 Medium — needed for aggregation task |
| 7 | AG Grid licence coverage for table view | Engineering | — | No | 🟢 Low — already licensed |
| 8 | Apply PostgreSQL DDL migration for snapshot + audit tables in all environments | Backend + DevOps | Week 1 | 🚦 Gate for scheduler deployment | 🔴 High |

---

## 17. Operational Runbook — Scheduler Failure

### Detection
- **Primary:** `marketplace_scheduler_audit_log` table: `status='FAILED'` row for current week's `week_start`.
- **Secondary:** `data_staleness_flag = true` in the PostgreSQL snapshot table for the current week.
- **Alert:** PagerDuty alert fires automatically when no `status='SUCCESS'` row exists for the current `week_start` within 24 hours of the scheduled run time (Monday 07:00 UTC threshold).

### Escalation
1. On-call engineer receives PagerDuty alert.
2. Check `marketplace_scheduler_audit_log` for failure reason and stack trace.
3. If transient (DB connection pool saturation, lock timeout, or network): re-trigger task manually via scheduler admin endpoint `POST /admin/scheduler/run?task=MarketplaceOverviewWeeklyAggregationTask`.
4. If source data missing: escalate to Data Team to verify upstream mart table availability.

### Backfill
If the scheduler missed a week, run the aggregation task with an explicit `week_start` override:
```
POST /admin/scheduler/run?task=MarketplaceOverviewWeeklyAggregationTask&weekStart=2026-02-24
```
Confirm by querying:
```sql
SELECT COUNT(*) FROM marketplace_kpi_weekly_snapshot
WHERE week_start = '2026-02-24';
```

### Scheduler Audit Log Schema
```sql
CREATE TABLE IF NOT EXISTS marketplace_scheduler_audit_log (
  id            BIGSERIAL PRIMARY KEY,
  job_id        VARCHAR(128) NOT NULL,
  org_id        BIGINT NOT NULL,
  week_start    DATE NOT NULL,
  status        VARCHAR(16) NOT NULL,   -- SUCCESS | FAILED | RETRYING
  attempt       INT NOT NULL DEFAULT 1,
  error_message TEXT,
  started_at    TIMESTAMPTZ,
  completed_at  TIMESTAMPTZ,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_marketplace_scheduler_audit_log_lookup
  ON marketplace_scheduler_audit_log (org_id, week_start DESC, status);
```

### Verification
- Confirm `data_staleness_flag` resets to `false` for the repaired week in the next scheduler run.
- Confirm frontend stale data banner disappears on next page load.

---

## 18. Appendix A — KPI Mapping

> **AR-007:** Deterministic KPI definitions for the aggregation task. All formulas apply per `(org_id, marketplace, brand_id, region, week_start)` partition.

| KPI Label | Column in Snapshot | Source Table | Aggregation Formula | Unit | Null/Zero Policy | Applies To |
|-----------|-------------------|-------------|---------------------|------|-----------------|------------|
| Lost Sales | `lost_sales` | `viz_lost_sales` | `SUM(lost_sales)` where `reporting_range='weekly'` | Currency (USD) | 0 if no rows matched; never NULL | All activated marketplaces |
| Total Closed Listings | `total_closed_listings` | `listings_progress_by_week` | `SUM(List_Count_Closed)` | Count | 0 if no rows matched | All activated marketplaces |
| Reseller Removed | `reseller_removed` | `reseller_progress_by_week` | `SUM(closed_reseller_count)` | Count | 0 if no rows matched | All activated marketplaces |
| Buybox Win % | `buybox_win_pct` | `reseller_progress_by_week` | `SUM(buy_box_winning_reseller_count_closed) / NULLIF(SUM(closed_reseller_count), 0) * 100` | Percentage | NULL if denominator = 0; frontend renders `--` | All activated marketplaces |
| Total Brand Violation | `total_brand_violation` | `viz_reseller_filtered_detail` via `enforcement_status` CTE | `COUNT(DISTINCT reseller_id)` where brand violation applies | Count | NULL for Walmart (not applicable); 0 for others with no violations | Amazon only (Walmart: NULL → rendered as `--`) |
| Violations Closed | `violations_closed` | `viz_reseller_filtered_detail` | `COUNT(DISTINCT reseller_id)` where `enforcement_status='CLOSED'` | Count | NULL for Walmart | Amazon only |
| Notification in Queue | `notification_in_queue` | `bp_wbr_detail` | `SUM(queue)` | Count | 0 if no rows matched | All activated marketplaces |
| C&D Pending | `cnd_pending` | `bp_wbr_detail` | `SUM(cnd_pending)` | Count | 0 if no rows matched | All activated marketplaces |
| Total C&D Sent | `total_cnd_sent` | `bp_wbr_detail` | `SUM(total_cnd_sent)` | Count | 0 if no rows matched | All activated marketplaces |
| Test Purchase | `test_purchase` | `bp_wbr_detail` | `SUM(test_purchase)` | Count | 0 if no rows matched | All activated marketplaces |
| No. of Listings | `no_of_listings` | `viz_lost_sales` | `COUNT(DISTINCT listing_id)` (where available per marketplace) | Count | NULL if marketplace has no listing data; 0 otherwise | Trial marketplaces (eBay, Target) |
| No. of Resellers | `no_of_resellers` | `reseller_progress_by_week` | `COUNT(DISTINCT reseller_id)` | Count | NULL if no data for marketplace | Trial marketplaces (eBay, Target) |
| WoW Change % | `wow_change_pct` | `marketplace_kpi_weekly_snapshot` (PostgreSQL self-join) | `(current_week.lost_sales - prev_week.lost_sales) / NULLIF(prev_week.lost_sales, 0) * 100` | Percentage | NULL if no prior week exists; frontend renders `--` | Trial marketplaces (eBay, Target) |

---

*Generated: 2026-03-04 | Updated: 2026-03-13 (PostgreSQL snapshot/audit storage update + ADR) | Release: release_8 | Template: arc42 (adapted)*
