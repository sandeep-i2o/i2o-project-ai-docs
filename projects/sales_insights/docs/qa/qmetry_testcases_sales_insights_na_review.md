# QMetry Review Draft - Sales Insights (release: na)

- Module: growth_accelerator
- Project: sales_insights
- Release: na
- Total cases: 36
- Type: Manual (Non-Executable)

## Review Table

| ID | Title | User Story | Priority | Edge | Labels |
|---|---|---|---|---|---|
| TC-001 | ECB CRON ingests daily FX rates at 16:30 CET | GA-SI-001-US001 | High | No | growth_accelerator,sales_insights,na,US001,happy-path |
| TC-002 | ECB feed outage falls back to last known rates | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,fallback |
| TC-003 | Schema validation failure on changed ECB XML structure | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,validation |
| TC-004 | Duplicate rate rows for same date/currency are UPSERTed | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,data-integrity |
| TC-005 | Network timeout triggers configured retry policy | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,retry |
| TC-006 | Missing currency in ECB payload is skipped with warning | GA-SI-001-US001 | Medium | Yes | growth_accelerator,sales_insights,na,US001,edge,currency |
| TC-007 | Outlier FX rate change >20% is flagged | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,outlier |
| TC-008 | Disk-full during FX write fails gracefully and alerts | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,storage |
| TC-009 | Partial XML download is rejected and retried | GA-SI-001-US001 | High | Yes | growth_accelerator,sales_insights,na,US001,edge,download |
| TC-010 | ECB rate limiting is respected with backoff | GA-SI-001-US001 | Medium | Yes | growth_accelerator,sales_insights,na,US001,edge,rate-limit |
| TC-011 | Leap-year date (Feb 29) FX ingestion and lookup | GA-SI-001-US001 | Medium | Yes | growth_accelerator,sales_insights,na,US001,edge,leap-year |
| TC-012 | Multi-region aggregation converts and sums correctly | GA-SI-001-US002 | High | No | growth_accelerator,sales_insights,na,US002,happy-path |
| TC-013 | EUR selection returns raw base values | GA-SI-001-US002 | High | No | growth_accelerator,sales_insights,na,US002,rule-validation |
| TC-014 | Unsupported currency defaults to EUR with alert | GA-SI-001-US002 | High | Yes | growth_accelerator,sales_insights,na,US002,edge,currency |
| TC-015 | No sales data shows explicit empty-state cards | GA-SI-001-US002 | Medium | Yes | growth_accelerator,sales_insights,na,US002,edge,empty-state |
| TC-016 | Future dates are blocked in date picker | GA-SI-001-US002 | Medium | Yes | growth_accelerator,sales_insights,na,US002,edge,date |
| TC-017 | Long-running query times out with guidance message | GA-SI-001-US002 | High | Yes | growth_accelerator,sales_insights,na,US002,edge,performance |
| TC-018 | Stale region feed indicator appears after 24h lag | GA-SI-001-US002 | Medium | Yes | growth_accelerator,sales_insights,na,US002,edge,freshness |
| TC-019 | Region multi-select enforces maximum item limit | GA-SI-001-US002 | Medium | Yes | growth_accelerator,sales_insights,na,US002,edge,filters |
| TC-020 | Missing LY baseline shows N/A with tooltip | GA-SI-001-US002 | Medium | Yes | growth_accelerator,sales_insights,na,US002,edge,ly |
| TC-021 | Zero FX rate value falls back to latest valid rate | GA-SI-001-US002 | High | Yes | growth_accelerator,sales_insights,na,US002,edge,fx-zero |
| TC-022 | Unauthorized regions are excluded from user filter options | GA-SI-001-US002 | High | Yes | growth_accelerator,sales_insights,na,US002,edge,authz |
| TC-023 | Rapid filter changes debounce requests and prevent race conditions | GA-SI-001-US002 | High | Yes | growth_accelerator,sales_insights,na,US002,edge,debounce |
| TC-024 | LY comparison uses corresponding prior-year week | GA-SI-001-US002 | High | No | growth_accelerator,sales_insights,na,US002,ac,ly |
| TC-025 | Region toggle updates cards and chart within performance SLA | GA-SI-001-US003 | High | No | growth_accelerator,sales_insights,na,US003,ac,performance |
| TC-026 | CSV export contains currently filtered SKU rows | GA-SI-001-US003 | High | No | growth_accelerator,sales_insights,na,US003,ac,export |
| TC-027 | Chart render failure shows fallback widget | GA-SI-001-US003 | Medium | Yes | growth_accelerator,sales_insights,na,US003,edge,chart |
| TC-028 | Dashboard remains usable on low-resolution displays | GA-SI-001-US003 | Medium | Yes | growth_accelerator,sales_insights,na,US003,edge,responsive |
| TC-029 | Large data grid (10k+ rows) remains smooth via virtualization | GA-SI-001-US003 | High | Yes | growth_accelerator,sales_insights,na,US003,edge,virtualization |
| TC-030 | Oversized export triggers fallback strategy | GA-SI-001-US003 | Medium | Yes | growth_accelerator,sales_insights,na,US003,edge,export-size |
| TC-031 | Image/asset load failures show placeholders | GA-SI-001-US003 | Low | Yes | growth_accelerator,sales_insights,na,US003,edge,assets |
| TC-032 | Malformed API JSON triggers full-screen error boundary | GA-SI-001-US003 | High | Yes | growth_accelerator,sales_insights,na,US003,edge,error-boundary |
| TC-033 | Session expiry preserves filter state and redirects to login | GA-SI-001-US003 | High | Yes | growth_accelerator,sales_insights,na,US003,edge,session |
| TC-034 | Trend lines remain distinguishable for 5+ regions | GA-SI-001-US003 | Medium | Yes | growth_accelerator,sales_insights,na,US003,edge,accessibility |
| TC-035 | Tiny chart points are still easy to hover | GA-SI-001-US003 | Low | Yes | growth_accelerator,sales_insights,na,US003,edge,usability |
| TC-036 | Slow network shows skeleton loaders before data arrives | GA-SI-001-US003 | Medium | Yes | growth_accelerator,sales_insights,na,US003,edge,loading |

## Story Coverage

- GA-SI-001-US001: 11 cases
- GA-SI-001-US002: 13 cases
- GA-SI-001-US003: 12 cases

## Files

- JSON import draft: projects/sales_insights/docs/qa/qmetry_testcases_sales_insights_na.json
- CSV import draft: projects/sales_insights/docs/qa/qmetry_testcases_sales_insights_na.csv
