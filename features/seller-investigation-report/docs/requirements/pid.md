# Project Brief: Seller Investigation Report

## Executive Summary
The **Seller Investigation Report** is a core component of the Cease & Desist (C&D) Management feature. It enables clients and internal users (Account Managers) to review recommended sellers, approve C&D actions, track legal progress, and download comprehensive investigation evidence in a business-ready PDF format. This report serves as critical evidence for legal actions across various marketplaces.

## Problem Statement
Currently, collecting and presenting evidence for seller investigations is a manual and fragmented process. There is a need for a centralized system that:
1.  Compiles seller identity, marketplace presence, and enforcement history.
2.  Aggregates evidence like invoices, test buy orders, and brand violations.
3.  Ensures reports are verified by internal experts (AMs) before being shared with clients to maintain legal and audit standards.
4.  Standardizes the report format with professional branding and confidentiality notices.

## Proposed Solution
A dedicated **C&D Management Dashboard** and **PDF Generation Engine** that:
- Provides a structured workflow from "Active Recommendations" to "Closed Cases".
- Allows AMs to "Preview" and "Mark as Ready" reports. 
- Restricts Client users from downloading reports until they are formally approved by an AM.
- Generates a PDF containing high-fidelity evidence, metadata, and branding.

## Target Users
### Primary User Segment: Client Users
- **Needs:** Prioritize sellers for C&D, view detailed seller context, approve actions, and download evidence for legal/audit purposes.
- **Goals:** Effectively stop unauthorized sellers and protect brand integrity.

### Secondary User Segment: Account Managers (Internal Users)
- **Needs:** Access internal enforcement controls, update legal statuses, preview reports, and confirm report readiness.
- **Goals:** Oversee legal operations and ensure clients receive accurate, high-quality evidence.

## Goals & Success Metrics
### Business Objectives
- Reduce time taken to compile legal evidence for C&D.
- Standardize enforcement documentation across all marketplaces.
- Improve compliance rates through better evidence tracking.

### User Success Metrics
- Average time from "Recommendation" to "Report Ready".
- Number of successful C&D actions supported by the report.

### Key Performance Indicators (KPIs)
- **Report Turnaround Time:** Target < 48 hours for AM verification.
- **Download Readiness:** 100% of downloaded reports must meet branding and confidentiality standards.

## MVP Scope
### Core Features (Must Have)
- **Report Generation:** Create a PDF with i2o logo, generation date, and confidentiality footer.
- **Wait/Gating Mechanism:** Disable download for clients until AM marks the report as `READY`.
- **Seller Details Section:** Business name, contact info, and location.
- **Marketplace Presence:** List of all marketplaces where the seller is active.
- **Evidence Sections:** Invoices, Test Buy Order details, and Brand Violations.
- **Search/Sort/Filter:** Ability to manage large lists of sellers in the dashboard.

### Out of Scope for MVP
- Client-side editing of report content.
- Automatic email delivery of reports.
- Partial section-wise downloads.

## Technical Considerations
### Platform Requirements
- **Target Platforms:** Web-based dashboard.
- **Browser/OS Support:** Modern browsers (Chrome, Firefox, Safari).

### Technology Preferences
- **File Format:** PDF.
- **Naming Convention:** `YYYYMMDD_sellerID_INVESTIGATION_REPORT.pdf`.

### Architecture Considerations
- **Status Flag:** `report_status` field (Values: `PENDING`, `READY`).
- **Permissions:** Role-Based Access Control (RBAC) to differentiate Client and AM actions.

## Constraints & Assumptions
### Constraints
- Reports must exactly match the header requirements (Logo, Date, Confidentiality notice).
- Download button must be disabled by default for clients.

### Key Assumptions
- AMs have the necessary backend access to verify invoice and buy box data.
- The generation date on the report should be the date of *download*, not creation.

## Risks & Open Questions
### Key Risks
- **Data Inconsistency:** Fixed-status sync issue must be thoroughly tested to prevent "In Progress" sellers from appearing in "Active Recommendations".
- **Missing Data:** Ensure Buy Box ownership history is reliably captured for all reports.

### Open Questions
- What is the specific logic for "Compliance Monitoring" after a case is closed?

## Next Steps
1.  **Generate PRD:** Use this brief to create detailed functional and technical requirements.
2.  **UX Design:** Define the visual state of the "Disabled" vs "Enabled" download button with tooltips.
3.  **Backend Integration:** Define the AM `publish` endpoint and `report_status` persistence.
