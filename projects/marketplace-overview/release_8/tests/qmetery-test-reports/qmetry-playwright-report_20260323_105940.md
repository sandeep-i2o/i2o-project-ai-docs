# QMetry Playwright Test Report

**Project:** marketplace-overview  
**Release:** release_8  
**QMetry Folder:** marketplace-overview (ID: 2320563)  
**QMetry Link:** https://qtmcloud.qmetry.com/rest/api/latest/projects/10537/testcase-folders  
**Test URL:** https://qa.i2oretail.com → https://qa.i2oretail.com/home/brandprotector/marketplace-overview  
**Executed:** 2026-03-23 10:59:40  
**Test File:** tests/e2e/playwright/marketplace-overview/marketplace_overview_brandprotection.spec.ts  

---

## Execution Summary

| Metric | Value |
|--------|-------|
| Total Tests | 31 |
| Passed | 5 ✅ |
| Failed | 26 ❌ |
| Skipped | 0 |
| Pass Rate | 16.1% |
| Duration | 891.4s |
| Videos Captured | 31 |
| Videos Uploaded to QMetry | 31/31 ✅ |

---

## Test Results by Case

| Case Key | Summary | Result | Video Attached |
|----------|---------|--------|----------------|
| IAC-TC-30 | Marketplaces Overview tab is visible for BP-enabled users | ✅ PASS | ✅ Uploaded |
| IAC-TC-31 | Marketplace Overview opens with default all-brand, all-regio | ❌ FAIL | ✅ Uploaded |
| IAC-TC-32 | Marketplaces Overview tab is hidden for users without BP ent | ✅ PASS | ✅ Uploaded |
| IAC-TC-33 | Direct URL access to Marketplace Overview is blocked for non | ✅ PASS | ✅ Uploaded |
| IAC-TC-34 | Brand filter lists all account-associated brands | ❌ FAIL | ✅ Uploaded |
| IAC-TC-35 | Brand filter supports multi-select and aggregates KPI output | ❌ FAIL | ✅ Uploaded |
| IAC-TC-36 | Region filter shows only account-enabled regions | ❌ FAIL | ✅ Uploaded |
| IAC-TC-37 | Calendar defaults to last complete week and View by defaults | ❌ FAIL | ✅ Uploaded |
| IAC-TC-38 | Switching Card and Table views retains active filters | ✅ PASS | ✅ Uploaded |
| IAC-TC-39 | Unsupported brand-region combination shows stable empty stat | ❌ FAIL | ✅ Uploaded |
| IAC-TC-40 | Amazon activated card renders Analytics, Brand Violation, an | ❌ FAIL | ✅ Uploaded |
| IAC-TC-41 | Walmart activated card omits Brand Violation section | ❌ FAIL | ✅ Uploaded |
| IAC-TC-42 | Non-activated eBay/Target cards show Initiate Trial and 3 su | ❌ FAIL | ✅ Uploaded |
| IAC-TC-43 | Card switches from trial to activated layout after marketpla | ❌ FAIL | ✅ Uploaded |
| IAC-TC-44 | Zero KPI values are displayed as 0 in Card view | ❌ FAIL | ✅ Uploaded |
| IAC-TC-45 | Card KPI values honor selected brand-region-week filter scop | ❌ FAIL | ✅ Uploaded |
| IAC-TC-46 | Table view renders one row per marketplace with PRD-defined  | ❌ FAIL | ✅ Uploaded |
| IAC-TC-47 | Walmart Brand Violation columns display -- in Table view | ❌ FAIL | ✅ Uploaded |
| IAC-TC-48 | Non-activated marketplace rows show Initiate Trial action in | ❌ FAIL | ✅ Uploaded |
| IAC-TC-49 | Table view renders pagination controls with default rows-per | ❌ FAIL | ✅ Uploaded |
| IAC-TC-50 | Table data remains aligned with Card view for same filters | ❌ FAIL | ✅ Uploaded |
| IAC-TC-51 | Initiate Trial action sends support email with required subj | ❌ FAIL | ✅ Uploaded |
| IAC-TC-52 | User sees success confirmation after trial request is trigge | ❌ FAIL | ✅ Uploaded |
| IAC-TC-53 | Multiple selected brands require explicit brand selection be | ❌ FAIL | ✅ Uploaded |
| IAC-TC-54 | Repeat click prevention marks trial request as Requested or  | ❌ FAIL | ✅ Uploaded |
| IAC-TC-55 | Email service failure surfaces actionable error and preserve | ❌ FAIL | ✅ Uploaded |
| IAC-TC-56 | Calendar defaults to last complete Monday-Sunday week on pag | ❌ FAIL | ✅ Uploaded |
| IAC-TC-57 | Successful weekly aggregation refresh updates dashboard KPIs | ❌ FAIL | ✅ Uploaded |
| IAC-TC-58 | Failed weekly aggregation shows stale data indicator with la | ❌ FAIL | ✅ Uploaded |
| IAC-TC-59 | KPI values remain stable during week and do not change mid-w | ❌ FAIL | ✅ Uploaded |
| IAC-TC-60 | Historical weekly snapshots are retained for trend readiness | ✅ PASS | ✅ Uploaded |

---

## Passed Tests

- **IAC-TC-30**: Marketplaces Overview tab is visible for BP-enabled users
- **IAC-TC-32**: Marketplaces Overview tab is hidden for users without BP entitlement
- **IAC-TC-33**: Direct URL access to Marketplace Overview is blocked for non-BP users
- **IAC-TC-38**: Switching Card and Table views retains active filters
- **IAC-TC-60**: Historical weekly snapshots are retained for trend readiness

---

## Failed Tests & Root Causes

### IAC-TC-31 — Marketplace Overview opens with default all-brand, all-region, last-week Card view
- **Root cause:** Selector not found within timeout — UI element locator needs tuning for actual DOM
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-34 — Brand filter lists all account-associated brands
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-35 — Brand filter supports multi-select and aggregates KPI output
- **Root cause:** Selector not found within timeout — UI element locator needs tuning for actual DOM
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-36 — Region filter shows only account-enabled regions
- **Root cause:** Selector not found within timeout — UI element locator needs tuning for actual DOM
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-37 — Calendar defaults to last complete week and View by defaults to Card
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-39 — Unsupported brand-region combination shows stable empty state
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-40 — Amazon activated card renders Analytics, Brand Violation, and Enforcement sections
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-41 — Walmart activated card omits Brand Violation section
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-42 — Non-activated eBay/Target cards show Initiate Trial and 3 summary KPIs
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-43 — Card switches from trial to activated layout after marketplace activation
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-44 — Zero KPI values are displayed as 0 in Card view
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-45 — Card KPI values honor selected brand-region-week filter scope
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-46 — Table view renders one row per marketplace with PRD-defined KPI columns
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-47 — Walmart Brand Violation columns display -- in Table view
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-48 — Non-activated marketplace rows show Initiate Trial action in Status column
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-49 — Table view renders pagination controls with default rows-per-page
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-50 — Table data remains aligned with Card view for same filters
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-51 — Initiate Trial action sends support email with required subject and body
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-52 — User sees success confirmation after trial request is triggered
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-53 — Multiple selected brands require explicit brand selection before sending trial request
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-54 — Repeat click prevention marks trial request as Requested or disables duplicate submission
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-55 — Email service failure surfaces actionable error and preserves retry path
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-56 — Calendar defaults to last complete Monday-Sunday week on page load
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-57 — Successful weekly aggregation refresh updates dashboard KPIs
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-58 — Failed weekly aggregation shows stale data indicator with last available range
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

### IAC-TC-59 — KPI values remain stable during week and do not change mid-week
- **Root cause:** Element exists but not visible — may be hidden behind a loading state
- **Video:** `artifacts/playwright-output/` (uploaded to QMetry ✅)

---

## Video Evidence

All 31 video recordings are stored under `artifacts/playwright-output/` and attached to their respective QMetry test cases.

| Case Key | Video Path | QMetry Attachment |
|----------|-----------|-------------------|
| IAC-TC-30 | video.webm | ✅ |
| IAC-TC-31 | video.webm | ✅ |
| IAC-TC-32 | video.webm | ✅ |
| IAC-TC-33 | video.webm | ✅ |
| IAC-TC-34 | video.webm | ✅ |
| IAC-TC-35 | video.webm | ✅ |
| IAC-TC-36 | video.webm | ✅ |
| IAC-TC-37 | video.webm | ✅ |
| IAC-TC-38 | video.webm | ✅ |
| IAC-TC-39 | video.webm | ✅ |
| IAC-TC-40 | video.webm | ✅ |
| IAC-TC-41 | video.webm | ✅ |
| IAC-TC-42 | video.webm | ✅ |
| IAC-TC-43 | video.webm | ✅ |
| IAC-TC-44 | video.webm | ✅ |
| IAC-TC-45 | video.webm | ✅ |
| IAC-TC-46 | video.webm | ✅ |
| IAC-TC-47 | video.webm | ✅ |
| IAC-TC-48 | video.webm | ✅ |
| IAC-TC-49 | video.webm | ✅ |
| IAC-TC-50 | video.webm | ✅ |
| IAC-TC-51 | video.webm | ✅ |
| IAC-TC-52 | video.webm | ✅ |
| IAC-TC-53 | video.webm | ✅ |
| IAC-TC-54 | video.webm | ✅ |
| IAC-TC-55 | video.webm | ✅ |
| IAC-TC-56 | video.webm | ✅ |
| IAC-TC-57 | video.webm | ✅ |
| IAC-TC-58 | video.webm | ✅ |
| IAC-TC-59 | video.webm | ✅ |
| IAC-TC-60 | video.webm | ✅ |

---

## Artifacts

| Artifact | Path |
|----------|------|
| Playwright Results JSON | `artifacts/playwright-results.json` |
| Fetched Test Cases | `artifacts/fetched_testcases.json` |
| Video Attachments Audit | `artifacts/qmetry-video-attachments.json` |
| Video Evidence Root | `artifacts/playwright-output/` |
| Test Spec File | `tests/e2e/playwright/marketplace-overview/marketplace_overview_brandprotection.spec.ts` |
| Login Helper | `tests/e2e/playwright/marketplace-overview/login-helper.ts` |
| Credentials | `.config/credentials.json` |

---

*Generated by qa-qmetry-playwright-tests skill on 2026-03-23 10:59:40*