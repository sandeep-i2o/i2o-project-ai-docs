GitHub URL: git@github.com:i2o-retail/i2o-dp-cf.git

# i2o-dp-cf Project Summary

## Description
`i2o-dp-cf` is a collection of Google Cloud Functions and Python-based data processing scripts capable of handling various aspects of the i2o retail data pipeline. The project encompasses modules for data migration, data integrity sanity checks, client onboarding orchestration, and integration with external platforms like Digishare and Amazon SP-API. These functions primarily operate on data stored in Google Cloud Storage (GCS) and PostgreSQL (Cloud SQL), ensuring data validity and consistency across the platform.

## Technology Stack
- **Language:** Python 3.x
- **Frameworks:**
  - `Flask`: Used for HTTP-triggered functions and API endpoints.
  - `Google Cloud Functions Framework`: Implicitly used for function deployment and execution.
- **Cloud Services:**
  - **Google Cloud Storage (GCS):** For storing input/output files (XML, CSV).
  - **Google Cloud SQL (PostgreSQL):** Primary relational database for application and pipeline data.
  - **Google Cloud Secret Manager:** For secure management of database credentials and API keys.
  - **Google Cloud BigQuery:** Destination for some data listings (e.g., L1/L2 listings).
- **Key Libraries:**
  - `pandas`: Data manipulation and analysis.
  - `psycopg2-binary`, `SQLAlchemy`: Database interaction.
  - `lxml`, `beautifulsoup4`: XML parsing and validation.
  - `google-cloud-storage`, `google-cloud-secret-manager`, `google-cloud-bigquery`: GCP SDKs.
  - `tenacity`: For retry logic in API requests.
  - `requests`, `httpx`: HTTP clients for external API interactions.

## Key Components

### 1. Digishare Cloud Function (`digishare_cloud_function`)
- **Type:** GCS Background Function
- **Trigger:** File finalization in GCS bucket.
- **Functionality:** Processes XML files uploaded to GCS. It validates them against XSD schemas, performs data transformation, and loads valid data into the PostgreSQL database. It handles archiving of processed files and error notifications via SMTP.

### 2. Onboarding Orchestration (`onboarding_orchestration_function`)
- **Type:** HTTP Function (Flask)
- **Functionality:** Manages the client onboarding workflow using a state machine approach. It reads pending onboarding stages from the `onboarding_api_view`, executes necessary setup steps (via external API calls), and updates the status in `client_onboarding_status`. Supports retries and dependency checks (e.g., waiting for previous stages).

### 3. Migration Services (`hourly_migration_cf1`, `hourly_migration_cf2`)
- **Type:** HTTP Function (Flask)
- **Functionality:** Exposes endpoints to trigger data migration tasks for specific process instances. Uses `ThreadPoolExecutor` for concurrent processing of multiple instances.

### 4. Sanity Checks (`sanity_check_cf1`, `sanity_check_cf2`)
- **Type:** HTTP Function (Flask)
- **Functionality:** Performs data integrity and sanity checks on processed data. Similar to the migration service, it processes lists of instance IDs concurrently and reports status.

### 5. SP-API Trigger (`sp-api-trigger`)
- **Type:** HTTP Function
- **Functionality:** Acts as a trigger for Amazon SP-API data fetching. It fetches pending records from an API endpoint and triggers downstream processing for each record, respecting time limits to avoid timeouts.

### 6. Listings Processing (`L1_L2_Listings`)
- **Type:** GCS Trigger / Data Processing
- **Functionality:** Processes reseller listing files (CSV) from GCS, cleans the data (price formatting, type conversion), and loads it into BigQuery. Sends email alerts on failure.

## Project Structure
```
i2o-dp-cf/
├── L1_L2_Listings/                  # Listings data to BigQuery loader
│   ├── main.py
│   └── requirements.txt
├── digishare_cloud_function/        # Digishare XML processing
│   ├── main.py                      # Entry point
│   ├── common/                      # DB and utility modules
│   ├── xsd_files/                   # XML schemas
│   └── requirements.txt
├── onboarding_orchestration_function/ # Onboarding workflow manager
│   ├── main.py
│   └── requirements.txt
├── hourly_migration_cf2/            # Data migration service
│   ├── main.py                      # Flask app entry point
│   └── cf2/src/python/              # Migration logic
├── sanity_check_cf2/                # Data sanity check service
│   ├── main.py
│   └── cf2/src/python/              # Sanity check logic
├── sp-api-trigger/                  # Amazon SP-API trigger
│   ├── main.py
│   └── requirements.txt
├── data_migration/                  # General data migration scripts
├── event_based_triggers/            # Event processing utilities
└── ... (other helper functions)
```

## Key API Endpoints

| Component | Endpoint | Method | Description |
|-----------|----------|--------|-------------|
| `hourly_migration_cf2` | `/process_instances` | POST | Triggers migration for a list of `process_instance_ids`. |
| `sanity_check_cf2` | `/process_instances` | POST | Triggers sanity checks for a list of `process_instance_ids`. |
| `onboarding_orchestration`| `/` (Root) | ANY | Triggers the onboarding orchestration logic (typically scheduled or event-driven). |
| `sp-api-trigger` | `/` (Root) | ANY | Fetches pending SP-API tasks and triggers downstream processing. |

## Scope & Target Use Cases
- **Automated Data Ingestion:** Seamlessly ingesting and validating partner data (Digishare) dropped into GCS buckets.
- **Pipeline Orchestration:** Managing complex, multi-step onboarding processes for new clients or markets.
- **Data consistency:** Regularly migrating data and running sanity checks to ensure the `dp` (data pipeline) and `app` databases are in sync and valid.
- **Scalability:** Using Cloud Functions allows independent scaling of these components based on load (e.g., file volume or onboarding requests).

## Deployment Notes
- **Environment Variables:** Each function relies heavily on environment variables for configuration (e.g., `secret_project_id`, `pg_secret_id`, `app_schema`, `bucket_names`).
- **Secrets:** Database credentials and SMTP configs are fetched dynamically from Google Secret Manager at runtime.
- **Concurrency:** Some functions (`migration`, `sanity_check`) implement internal concurrency using `ThreadPoolExecutor`, but Cloud Functions also scale out automatically.
- **Triggers:** Deployment must configure the correct triggers:
    - `digishare_cloud_function`: Cloud Storage trigger (Finalize/Create).
    - `onboarding`, `migration`, `sanity`, `sp-api`: HTTP triggers.
