# Seller Investigation Report – Product Requirements Document (Execution PRD)

## Metadata
- **Author:** Antigravity (AI PM)
- **Stakeholders:** Account Managers, Client Users, Legal Team
- **Jira Epic:** [Link to be assigned]
- **Confluence Page:** [Link to be assigned]

---

## 1. Objective of the Requirement

### Problem Statement
Currently, collecting and presenting evidence for seller investigations is a manual and fragmented process. Account Managers (AMs) spend significant time aggregating data from multiple sources (Buy Box history, marketplace identity, policy violations), leading to delays in Cease & Desist (C&D) actions. Furthermore, there is no centralized gateway to ensure reports are expert-verified before being shared with clients, posing a risk of legal or branding inconsistencies.

### Why Now?
C&D management is a core competitive feature for i2o. Standardizing legal evidence and automating its compilation is critical to scaling enforcement operations and maintaining high audit standards for global brands.

### Impacted Users
- **Account Managers (Internal):** Needs to oversee legal operations and verify evidence quality.
- **Client Users (External):** Needs to prioritize sellers for C&D and download business-ready evidence for legal actions.
- **Legal/Compliance Team:** Needs high-fidelity, standardized audit trails.

### Success Metrics
- **Efficiency:** Reduce average time to compile evidence from manual (hours) to automated (seconds).
- **Latency:** Target < 48 hours for AM report verification ("Pending" to "Ready").
- **Quality:** 100% of downloaded reports must contain the required i2o branding, date, and confidentiality notices.
- **Actionability:** Increase the volume of successful C&D actions per client month by 20% due to faster evidence delivery.

### Non-Goals
- Real-time editing of the PDF content within the browser.
- Automated email delivery of the PDF (will be handled in a later phase).
- Historical audit of reports generated *before* this system launch.

---

## 2. Metric Definitions (Single Source of Truth)

| Metric Name | Business Definition | Formula | Aggregation | Time Granularity | Source of Truth |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **report_turnaround_time** | Time taken for an AM to mark a report as READY after it appears in the dashboard. | `ready_timestamp - creation_timestamp` | AVG | Monthly | `investigation_audit_log` |
| **available_report_count** | Total number of sellers with an investigation report status of 'READY'. | `COUNT(DISTINCT seller_id) WHERE report_status = 'READY'` | SUM | Daily | `investigation_status_table` |
| **evidence_completeness** | % of reports that successfully pull all three evidence types: Invoice, Test Buy, Violations. | `(Reports with all types / Total Reports) * 100` | AVG | Weekly | `i2o-formatted-reports` logs |

---

## 3. User Stories (Breakdown + Dependency Map)

### 3.1 Story Index

| ID | Title | Story Type | Standalone | Depends On | Blocks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US-1** | Seller Discovery & Dashboard | UI | Yes | None | US-4, US-5 |
| **US-2** | PDF Generation Engine (Jasper) | Backend | No | US-3 | US-4, US-5 |
| **US-3** | Evidence Data Integration (BQ) | Backend | Yes | None | US-2 |
| **US-4** | AM verification / "READY" Workflow | Hybrid | No | US-1, US-3 | US-5 |
| **US-5** | Client Access Gating & Download | UI | No | US-4 | None |

---

### 3.2 Story Details

#### **US-1: Seller Discovery Dashboard (Admin & Client)**
- **User Story:** As a user, I want a structured dashboard with search and filter capabilities so that I can easily manage and locate specific seller investigations.
- **Story Type:** UI
- **Dependency Map:** Standalone.
- **Artifacts (UI):**
  - **Components:** DataTable (Shadcn), SearchBar, Marketplace Filter, Status Filter.
  - **Interactions:** Clicking row opens Seller Detail view.
  - **States:** Loading spinner for data fetch; "No sellers found" empty state.
- **Corner Cases:**
  - Seller active in 50+ marketplaces (ensure filter/list handles overflow).
  - Search by partial Seller ID or Business Name.
- **Acceptance Criteria:**
  - Search filters update results in < 500ms.
  - Users can filter by `report_status` (PENDING, READY).

#### **US-2: Automated PDF Generation Engine**
- **User Story:** As a system, I want to generate a branded PDF report containing seller identity and evidence so that professional evidence is available for legal use.
- **Story Type:** Backend
- **Dependency Map:** Depends on US-3 (Data Integration).
- **Artifacts (Backend):**
  - **Logic:** Trigger `i2o-formatted-reports` using JasperReports template.
  - **Tables:** `viz_bbx_filtered_detail`.
  - **API Contract:** `POST /report/seller-investigation` (Request: `seller_id`, `am_id`).
- **Corner Cases:**
  - Missing evidence sections: Use "N/A" or "No evidence records found" instead of leaving blank or crashing.
- **Acceptance Criteria:**
  - PDF filename matches: `YYYYMMDD_sellerID_INVESTIGATION_REPORT.pdf`.
  - Header contains i2o logo and generation date.
  - Footer contains confidentiality notice.

#### **US-3: Evidence Data Integration (BigQuery)**
- **User Story:** As a developer, I want to source Buy Box and Seller identity data from the data mart so that the report content is accurate and fresh.
- **Story Type:** Backend
- **Artifacts (Backend):**
  - **Tables:** `CC_I2O_DATA_MART.viz_bbx_filtered_detail`.
  - **Columns:** `seller_id`, `seller_name`, `marketplace`, `buy_box_percentage`, `evidence_url_invoices`.
- **Acceptance Criteria:**
  - SQL query successfully retrieves vertical slices of evidence: Invoices, Test Buy Order records, and Brand Violations.

#### **US-4: AM "Mark as Ready" Workflow**
- **User Story:** As an Account Manager, I want to preview the report and toggle its status to 'READY' so that I can control what the client sees.
- **Story Type:** Hybrid
- **Artifacts (UI/Backend):**
  - **UI Component:** "Preview" button (opens in new tab), "Mark as Ready" toggle.
  - **Backend Logic:** Update `report_status` field in PostgreSQL.
- **Corner Cases:**
  - AM tries to mark "Ready" without previewing (add a confirmation modal).
- **Acceptance Criteria:**
  - Only users with `INTERNAL_AM` role can see the "Mark as Ready" button.
  - Status change is reflected immediately (UI state update).

#### **US-5: Client Access Gating**
- **User Story:** As a Client, I want to see which sellers are being investigated but have the download disabled until an AM approves, so I only use verified evidence.
- **Story Type:** UI
- **Artifacts (UI):**
  - **Logic:** Check `report_status`. If `PENDING`, show "Download (Pending Verification)" disabled with a tooltip.
- **Acceptance Criteria:**
  - Download button is disabled and greyed out if `status == PENDING`.
  - Tooltip explanation: "Your Account Manager is currently verifying this evidence."

---

## 4. Technical Assumptions
- **Frontend:** Integrated into `i2o-admin-UI` (React/TypeScript).
- **Backend:** Extensions to `i2o-formatted-reports` (Spring Boot/Java) for Jasper integration.
- **Data Source:** `CC_I2O_DATA_MART` BigQuery tables for raw evidence; PostgreSQL for status tracking.
- **Permissions:** Keycloak roles `CLIENT_USER` and `INTERNAL_AM`.

---

## 5. Global Corner Case Inventory
- **Late Arriving Data:** If BigQuery sync lags, show "Data Refreshed: [Timestamp]" on the UI.
- **Large Seller Identity:** If a seller name is extremely long, ensure the PDF template handles text wrapping without breaking the layout.
- **Browser Compatibility:** PDF preview must work on Chrome, Safari, and Firefox.

---

## 6. PM Checklist Validation

- [x] All requirements are testable.
- [x] Sequential logic: Backend integration (US-3) precedes PDF generation (US-2).
- [x] MVP scope strictly followed (no client-side editing).
- [x] Branding requirements (Logo, Date, Confidentiality) included.
- [x] RBAC constraints defined for AM vs Client.

---

## 7. Next Steps

### UX Expert Prompt
"Design a dashboard for Seller Investigations in i2o-admin-UI. The dashboard needs a search bar, marketplace filter, and status filter (Pending/Ready). The main table should show Seller ID, Business Name, Status, and an Action column. If status is 'Pending', the 'Download' action should be disabled with a tooltip explaining 'AM verification in progress'. Provide a secondary 'Preview' view for AMs only."

### Architect Prompt
"Design the technical architecture for the Seller Investigation Report. The system should use BigQuery (`viz_bbx_filtered_detail`) as the data source. PDF generation must leverage the existing `i2o-formatted-reports` service with JasperReports. Status persistence (`PENDING`/`READY`) should live in the application's PostgreSQL DB. Ensure RBAC is handled via the Keycloak middleware."
