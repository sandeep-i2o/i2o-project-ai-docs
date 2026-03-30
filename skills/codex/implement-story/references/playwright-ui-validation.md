# Playwright UI Validation

Run this flow for UI-related changes.

## Core Commands

```bash
mcp_playwright test --config=playwright.config.ts --browsers=chromium,firefox,webkit
mcp_playwright accessibility --wcag-level=AA --output-format=json
mcp_playwright visual-regression --threshold=0.2 --update-snapshots=false
mcp_playwright mobile --devices="iPhone 12,Pixel 5,iPad" --orientation=both
```

## Coverage Requirements
- Cross-browser behavior: Chrome/Chromium, Firefox, Safari/WebKit, Edge-equivalent target
- Accessibility: WCAG 2.1 AA, keyboard paths, focus order, contrast, screen reader compatibility
- Visual regression: component and page-level snapshots with threshold `0.2`
- Responsiveness: mobile/tablet and orientation changes
- Performance impact: verify load/runtime impact is acceptable

## Failure Handling
- Retry failed UI validations up to 3 times.
- For accessibility failures, report violated WCAG criteria.
- For visual failures, include before/after comparison references.
- For browser-specific failures, identify impacted browser/version and reproduction steps.
- Produce a concise test report for manual review when unresolved.
