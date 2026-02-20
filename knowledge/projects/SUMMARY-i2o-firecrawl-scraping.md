GitHub URL: git@github.com:i2o-retail/i2o-firecrawl-scraping.git

# i2o-firecrawl-scraping Project Summary

## Description
`i2o-firecrawl-scraping` is a Python-based microservice built with FastAPI that orchestrates web scraping jobs using the **Firecrawl** third-party service. It manages the lifecycle of scraping tasks, including submission of batch jobs, handling webhook callbacks for progress updates, automatic retries for missing data, and final reconciliation of results. The processed data is then stored in Google Cloud Storage (GCS).

## Technology Stack
- **Language:** Python 3.x
- **Framework:** FastAPI (Web API), Uvicorn (ASGI Server)
- **External Integration:** [Firecrawl](https://firecrawl.dev) (Scraping Service)
- **Database:** PostgreSQL (via `psycopg2`, implied for job status/metadata storage)
- **Cloud Services:**
  - **Google Cloud Storage (GCS):** For storing scraped data (JSON/CSV).
  - **Google Cloud Secret Manager:** For API keys and credentials.
- **Key Libraries:**
  - `firecrawl`: SDK for interacting with the Firecrawl API.
  - `pandas`: Data manipulation.
  - `requests`: HTTP client.
  - `pydantic`: Data validation (implied by FastAPI).

## Key Components
- **Job Processor (`process_pending_jobs_service`):** Polls for pending jobs, fetches URL lists, and submits batch scrape requests to Firecrawl.
- **Webhook Handler (`firecrawl_webhook_service`):** Listens for events from Firecrawl (`started`, `page`, `completed`) to update job status and process incoming data in real-time.
- **Reconciliation Service (`reconcile_stuck_jobs_service`):** Periodically checks for jobs that have stalled or missed webhook events, actively searching Firecrawl for results and triggering retries if necessary.
- **Scrapers Module:** Contains logic to process raw Firecrawl results and format them into the final output structure.

## Project Structure
```
i2o-firecrawl-scraping/
├── api.py                   # FastAPI application entry point and route definitions
├── service.py               # Core business logic (job submission, webhook handling, reconciliation)
├── scrapers.py              # Data processing and formatting logic
├── utils.py                 # Helper functions (DB access, GCS operations)
├── config.py                # Configuration (Prompts, Schemas for Firecrawl)
└── requirements.txt         # Dependencies
```

## Key API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/jobs/process` | GET | Triggers the processing of pending scraping jobs from the database. |
| `/firecrawl/webhook` | POST | Receives event notifications from Firecrawl (started, page, completed). |
| `/jobs/reconcile-stuck` | GET | Triggers reconciliation for jobs stuck in progress for more than X minutes. |

## Scope & Target Use Cases
- **High-Volume Scraping:** efficiently scraping large lists of product or offer URLs from various e-commerce platforms using Firecrawl's infrastructure.
- **Resilient Data Collection:** Handling failures via automatic retries and reconciliation logic to ensure high data completeness.
- **Asynchronous Processing:** Decoupling job submission from result processing using webhooks.

## Deployment Notes
- **Environment Variables:** Requires `WEBHOOK_URL` (for Firecrawl callback), `FIRECRAWL_API_KEY` (via Secret Manager), and database credentials.
- **Concurrency:** Designed to handle asynchronous webhook events; care must be taken with database connections (`psycopg2`).
