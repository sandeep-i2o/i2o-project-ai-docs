# GA-SI-001 – Product Requirements Document
# Growth Accelerator - Sales Insights - Unified EMEA Sales Dashboard

## Section A: Epic Definition

| Field | Details |
| :--- | :--- |
| **Epic ID** | GA-SI-001 |
| **Epic Name** | Growth Accelerator - Sales Insights - Unified EMEA Sales Dashboard |
| **Epic Type** | New Module |
| **Parent Epic** | N/A |
| **Product(s)** | Growth Accelerator |
| **Module(s)** | Sales Analytics, Currency Conversion Service, Data Ingestion Pipeline |
| **Is New Module?** | Yes |
| **Cross-Module?** | No |
| **Cross-Product?** | No |
| **Priority** | P0: Critical |
| **Target Release** | Q2 2026 |
| **Epic Owner** | PM: Sandeep, Tech Lead: AI Agent |
| **Timeline** | 8 weeks |
| **Known Blockers** | External dependency on ECB XML feed stability; Access to regional marketplace data feeds |

---

## Section B: Problem & Objectives

### B1. Problem Statement
Panasonic EMEA currently manages sales reporting across five regional marketplaces (DE, FR, IT, ES, UK) using fragmented, manual processes. This results in a 2-3 day lag in visibility and high risk of data inconsistency due to manual currency math and spreadsheet merging.

*   **Manual FX Lookup:** Regional managers spend 4-6 hours per week manually calculating exchange rates.
*   **Data Inconsistency:** Human error during Excel merging leads to conflicting sales figures in weekly reviews.
*   **Reporting Latency:** Executive leadership receives "stale" data that is at least 48 hours old, preventing agile market responses.

### B2. Why Now?
**Revenue & Operational Efficiency:** Manual reporting is no longer scaling with the volume of regional data. Automating this "Cold Path" will save over 20+ man-hours per week and enable real-time strategic pivots based on accurate, harmonized data.

### B3. Who Benefits & How?

| Persona | Pain | Solution Benefit | Impact |
| :--- | :--- | :--- | :--- |
| Regional Sales Manager | Spends 4-6 hrs/week on FX lookup & Excel merging | Automated ingestion and conversion | 90% reduction in reporting effort |
| Executive VP | Delayed visibility into pan-EMEA performance | Real-time unified dashboard in primary currency | Instant decision-making capability |
| Data Analyst | Resolving data discrepancies between regions | Single Source of Truth for all EMEA sales | 100% data consistency |

### B4. Success Metrics

| Metric | Baseline → Target | Timeline | Measurement |
| :--- | :--- | :--- | :--- |
| Reporting Turnaround | 2-3 Days → < 5 Seconds | 30 days post-launch | System log of report generation time |
| Adoption | N/A → 100% | 90 days post-launch | % of Regional Managers with active accounts |
| Dashboard Latency | N/A → < 200ms P95 | At Launch | P95 Page Load Time monitoring |

### B5. Scope

**In Scope:**
*   Automated daily ingestion of sales data from DE, FR, IT, ES, and UK regions.
*   Historical exchange rate ingestion from official ECB XML feed.
*   On-the-fly currency conversion for EUR, GBP, USD, CAD, and MXN.
*   Interactive dashboard with trend charts, summary KPIs, and detailed data grids.
*   Support for multiple time granularities: Daily, Weekly, Monthly, Quarterly.

**Out of Scope:**
*   Custom user-defined exchange rates (MVP constraint).
*   Real-time (hourly) data streams (Future phase).
*   Predictive sales forecasting (Future phase).

---

## Section C: User Stories

### User Story #1
**Story ID:** GA-SI-001-US001
**Title:** Automated ECB Rate Ingestion

**Story:**
As a System,
I want to fetch and store daily exchange rates from the ECB XML feed,
So that I have a trusted, historical FX source for multi-currency reporting.

**Metadata:**
*   **Modules:** Currency Conversion Service
*   **Priority:** P0
*   **Type:** Backend

**Dependencies:**
*   **Depends on:** N/A
*   **Blocks:** GA-SI-001-US002 (Calculations require FX rates)

**Requirements:**
*   **Business Logic Flow:**
    1.  CRON trigger daily at 16:30 CET.
    2.  Fetch XML from `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml`.
    3.  Validate XML schema.
    4.  Extract rates and store in `fx_rates` table with timestamp.
    5.  On failure: Retry 3 times, then alert admin. Fallback to last known rate if needed.
*   **Data Sources:**
    | Table | Purpose | Key Fields |
    | :--- | :--- | :--- |
    | `fx_rates` | Store historical rates | `date, currency_code, rate_to_eur` |

**Corner Cases & Error Handling:**

| # | What Could Go Wrong | How Should It Be Handled | What User Experiences |
| :--- | :--- | :--- | :--- |
| 1 | ECB XML feed is down | Retry with exponential backoff; use last cached rate | Dashboard shows "Rates as of [Date]" warning |
| 2 | XML structure changes | Validation fails; log error; notify dev team | System uses previous day's rates |
| 3 | Duplicate entries for same date | UPSERT logic to ensure unique date/currency pairs | No visible impact; data remains clean |
| 4 | Network timeout | 10s timeout with 3 retries | Delayed data refresh |
| 5 | Missing currency in feed | Log warning; skip specific currency | Warning icon on dashboard for that currency |
| 6 | Huge spike in FX rate (outlier) | Sanity check (>20% change); flag for review | Dashboard shows "Verification Required" flag |
| 7 | System disk full during write | Fail gracefully; clear old logs; alert | No data update for that day |
| 8 | Partial XML download | Checksum/Size validation | Discard partial file; retry |
| 9 | API rate limiting | Respect headers; backoff | Slight delay in ingestion |
| 10 | Leap year handling | Logic must handle Feb 29 | Correct historical mapping |

**Acceptance Criteria:**
| # | Given-When-Then | Verification |
| :--- | :--- | :--- |
| AC1 | Given it's 16:30 CET, When the CRON runs, Then daily rates are successfully stored in PostgreSQL. | SQL Query verification |
| AC2 | Given the ECB feed is offline, When the system attempts ingestion, Then it falls back to the last available rate without crashing. | Integration test (mock failure) |
| AC3 | Given all AC pass + QA complete, When PO reviews, Then story = Done | PO Sign-off |

---

### User Story #2
**Story ID:** GA-SI-001-US002
**Title:** Unified Multi-Region Sales Aggregation

**Story:**
As a Regional Sales Manager,
I want to filter sales data by multiple regions and view totals in my preferred currency,
So that I can compare performance across EMEA without manual math.

**Metadata:**
*   **Modules:** Sales Analytics
*   **Priority:** P0
*   **Type:** Full-stack

**Dependencies:**
*   **Depends on:** GA-SI-001-US001 (FX rates needed)
*   **Blocks:** GA-SI-001-US003 (Visualization needs processed data)

**Requirements:**
*   **User Flow:**
    1.  Select Regions (e.g., DE, FR) via multi-select.
    2.  Select Currency (e.g., GBP).
    3.  Select Time Granularity (Weekly).
    4.  System calculates totals and returns results within 200ms.
*   **KPIs & Calculations:**
    | KPI/Metric | Source Table(s) | Calculation Logic |
    | :--- | :--- | :--- |
    | Ordered Revenue | `sales_data`, `fx_rates` | SUM(local_revenue * rate_to_base_eur * rate_from_eur_to_chosen) |
    | ASP | `sales_data` | Total Ordered Revenue / Total Ordered Units |
    | LY Revenue | `sales_data` | Revenue from same period last year (364-day offset) |
*   **Business Rules:**
    Rule: Base Currency Conversion
    IF currency == EUR THEN return raw base value
    ELSE IF currency exists in `fx_rates` THEN return converted value
    ELSE return error "Currency Not Supported"

**Corner Cases & Error Handling:**

| # | What Could Go Wrong | How Should It Be Handled | What User Experiences |
| :--- | :--- | :--- | :--- |
| 1 | No sales data for selected region | Show "0" or "No Data" state | Empty state cards with clear labels |
| 2 | Invalid date range selected | Prevent selection of future dates | Date picker disables future dates |
| 3 | Selected currency not in FX DB | Default to EUR; show notification | "Currency unavailable, showing EUR" alert |
| 4 | DB query takes too long | Optimized indexing; query timeout | "Request timed out, please narrow filters" |
| 5 | Region data feed delayed | Show "Stale" indicator if data > 24h old | Yellow warning dot next to region name |
| 6 | User selects 100+ items in filter | Limit multi-select if performance degrades | "Max 10 items allowed" message |
| 7 | LY data missing (new region) | Show "N/A" for LY metrics | Dashboard shows "N/A" with tooltip status |
| 8 | Currency rate is 0 | Fallback to latest valid rate; alert admin | System remains stable |
| 9 | Unauthorized access to region | Filter out unauthorized regions from list | User only sees permitted regions |
| 10 | Rapid clicking of filters | Debounce inputs; abort previous requests | Smooth UI transition |

**Acceptance Criteria:**
| # | Given-When-Then | Verification |
| :--- | :--- | :--- |
| AC1 | Given a mix of UK (GBP) and DE (EUR) data, When I select EUR as display, Then total revenue is correctly aggregated using historical rates. | Manual audit vs Calc |
| AC2 | Given a selected week, When LY metric is toggled, Then the comparison matches the corresponding week from the previous year. | Data validation test |
| AC3 | Given all AC pass + QA complete, When PO reviews, Then story = Done | PO Sign-off |

---

### User Story #3
**Story ID:** GA-SI-001-US003
**Title:** Command Center Dashboard Visualization

**Story:**
As an Executive VP,
I want a consolidated view of EMEA performance with trend charts and detailed data grids,
So that I can identify sales intervals and SKU-level performance instantly.

**Metadata:**
*   **Modules:** Sales Analytics
*   **Priority:** P0
*   **Type:** UI

**UI Screens & Interactions:**

**Screen: Main Dashboard**
![Main View](./images/Multi%20Region%20Screen.png)
*   **Context:** User logs in and arrives at the EMEA Overview.
*   **Key Elements:**
    1.  Summary Cards - Displays Revenue, Units, and ASP.
    2.  Context Bar - Top sticky bar for Region, Granularity, and Currency.
    3.  Trend Chart - Multi-line graph for regional comparison.
*   **Interactions:**
    - 👆 Click Region -> Update all cards and charts.
    - 🖱️ Hover Point -> Show tooltip with specific metrics for that date.

**Screen: Detailed Table**
![Detailed Table](./images/View%20By%20Table.png)
*   **Context:** Scroll down from the main chart to see SKU-level data.
*   **Key Elements:**
    1.  Search Column - Filter by SKU or Product Name.
    2.  Export Button - Download current grid as CSV.
*   **Interactions:**
    - 👆 Click Header -> Sort by Revenue/Units ascending/descending.

**Screen: Analytics Filters**
![Currency Filter](./images/Currency%20Filter.png)
![Region Filter](./images/Region%20Filter.png)
![Time Series Graph](./images/Graph.png)
*   **Context:** Selection controls and visualization details for region and currency switching.

**Corner Cases & Error Handling:**

| # | What Could Go Wrong | How Should It Be Handled | What User Experiences |
| :--- | :--- | :--- | :--- |
| 1 | Chart fails to render | Show placeholder with reload button | "Unable to load chart" widget |
| 2 | Screen resolution too low | Responsive design; vertical stack | Usable layout on small screens |
| 3 | Table too large (10k+ rows) | Virtualized rendering (AG Grid) | Smooth scrolling without lag |
| 4 | Export fails due to size | Paginated export or server-side CSV | Notification: "Large file, please check email" |
| 5 | Images fail to load | Default CSS avatars/placeholders | No broken image icons |
| 6 | API returns malformed JSON | Comprehensive error boundary | "Something went wrong" full-screen overlay |
| 7 | User session expires | Auto-save filter state; redirect to login | Logout with friendly message |
| 8 | Multiple colors for 5+ regions | Use distinctive color patterns | Accessible, high-contrast chart lines |
| 9 | Hovering tiny data points | Increase hover hit-area (radius) | Easy interaction |
| 10 | Slow network on chart load | Show skeleton screens | Pulsing grey boxes while loading |

**Acceptance Criteria:**
| # | Given-When-Then | Verification |
| :--- | :--- | :--- |
| AC1 | Given the main dashboard, When a region is toggled off, Then the chart and cards update dynamically in < 200ms. | Performance profiling |
| AC2 | Given the data grid, When I click the CSV export, Then a file is generated containing the filtered SKU data. | Exported file check |
| AC3 | Given all AC pass + QA complete, When PO reviews, Then story = Done | PO Sign-off |

---

## Section D: Release Plan & Timeline

### Release 1: Alpha (Core Pipeline)
*   **Goal:** Establish data ingestion and FX storage.
*   **Target Date:** Week 3
*   **Stories:**
    | Story ID | Title | Priority | Status |
    | :--- | :--- | :--- | :--- |
    | GA-SI-001-US001 | Automated ECB Rate Ingestion | P0 | 📋 Backlog |
*   **Timeline:**
    - Week 1: Monorepo Setup & Ingestion Script
    - Week 2: ECB API Integration
    - Week 3: Database Optimization (TimescaleDB)
*   **Show Stopper:** Failure to normalize incoming marketplace CSVs. Mitigation: Pre-production schema validation tool.

### Release 2: Beta (MVP Dashboard)
*   **Goal:** Full multi-region aggregation and UI visualization.
*   **Target Date:** Week 8
*   **Stories:**
    | Story ID | Title | Priority | Status |
    | :--- | :--- | :--- | :--- |
    | GA-SI-001-US002 | Unified Multi-Region Sales Aggregation | P0 | 📋 Backlog |
    | GA-SI-001-US003 | Command Center Dashboard Visualization | P0 | 📋 Backlog |
*   **Timeline:**
    - Week 4-5: Aggregation Logic & API Development
    - Week 6-7: Frontend Component Development
    - Week 8: UAT & Data Validation
*   **Show Stopper:** Aggregation latency > 1s for large date ranges. Mitigation: Implement daily pre-aggregated materialized views in PostgreSQL.

---

## Section E: Appendix

### E1. Glossary
| Term | Definition |
| :--- | :--- |
| **ASP** | Average Selling Price (Revenue / Units) |
| **ECB** | European Central Bank (FX Source of Truth) |
| **FX** | Foreign Exchange |
| **LY** | Last Year (Comparison metric) |
| **Cold Path** | Batch processing of data for non-real-time ingestion |
| **WBR** | Weekly Business Review (Primary Use Case) |

### E2. References
*   **ECB API:** `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html`
*   **Internal Data Schema:** Refer to `knowledge/bigquery_schemas/sales_data_schema.md`

### E3. FAQ for Developers
**Q: Why do we use a 364-day offset for LY metrics?**
**A:** This ensures that we compare the same day of the week (e.g., Monday vs Monday), which is critical for retail sales accuracy. Refer to Section C UI logic.

**Q: Can we add more currencies later?**
**A:** Yes, the system is designed to support any currency present in the ECB XML feed by simply adding it to the `active_currencies` config list.

### E4. Change Log
| Date | Ver | Author | Changes | Sections Affected |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-26 | 1.0 | AI Agent | Initial PRD for Sales Insights | All |
