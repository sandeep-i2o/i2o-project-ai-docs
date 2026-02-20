GitHub URL: https://github.com/i2o-retail/i2o_data_pipeline_automation.git

# i2o Data Pipeline Automation

## Project Overview

The **i2o Data Pipeline Automation** framework is a robust, Python-based system designed to orchestrate the entire lifecycle of data within the i2o retail analytics platform. It creates, manages, and executes ETL (Extract, Transform, Load) processes, moving data from diverse sources—such as Amazon SP-API, Vendor Central, advertising platforms, and web scrapers—into a centralized Google BigQuery data warehouse.

The system leverages **Apache Airflow** for workflow orchestration, ensuring reliable scheduling, dependency management, and error handling. It features dynamic DAG generation based on client configurations, automated data quality checks, and a comprehensive alerting system to maintain data integrity and pipeline health.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Core Language** | Python 3.x |
| **Orchestration** | Apache Airflow |
| **Cloud Platform** | Google Cloud Platform (GCP) |
| **Data Warehouse** | Google BigQuery |
| **Object Storage** | Google Cloud Storage (GCS) |
| **Secret Management** | GCP Secret Manager |
| **Database** | PostgreSQL (Metadata & Tracking) |
| **Web Scraping** | Selenium, Chrome WebDriver, ScrapeHero Integration |
| **Data Processing** | Pandas, NumPy, Parquet |
| **Notification** | SMTP (SendGrid) |
| **Configuration** | JSON, INI, Environment Variables |

---

## Detailed Component Breakdown

### 1. Airflow (`airflow/`)

**Description**: The orchestration engine for the entire platform. Contains DAG (Directed Acyclic Graph) definitions, custom operators, and SQL scripts used by Airflow tasks.

**Key Workflow**:
- **DAG Generation**: Reads configuration files to dynamically create DAGs for each client and data source.
- **Task Execution**: Executes Python and SQL tasks to extract data, load it to GCS, and transform/load it into BigQuery.
- **Scheduling**: Manages dependencies and schedules (daily, weekly, ad-hoc).

**Scope**:
- DAGs for all data sources (Amazon, Walmart, Target, etc.).
- Custom Airflow operators for specific i2o tasks.
- SQL templates for data transformation and loading.

**Target Use Cases**:
- "Run the daily sales report ingestion for Client X at 2 AM."
- "Trigger a retry if the Vendor Central scrape fails."

### 2. Common Utilities (`common/`)

**Description**: A shared library of utility functions and classes used across all other modules. This ensures code reusability and consistency.

**Key Workflow**:
- **Authentication**: Handles GCP authentication, database connections, and website logins.
- **Data Encapsulation**: Provides models and schema definitions.
- **Communication**: Sends emails via SMTP.
- **IO Operations**: wrappers for GCS/S3 uploads, file systems, and BigQuery interactions.

**Scope**:
- Database connections (Postgres, BigQuery).
- Email notifications.
- Generic file handling and data processing logic.

**Target Use Cases**:
- "Send an email alert when a job fails."
- "Upload a pandas DataFrame to GCS as a Parquet file."

### 3. Job Creator (`job_creator/`)

**Description**: The "brain" of the dynamic pipeline. Scripts here generate the configuration and DAG structure for Airflow based on client metadata.

**Key Workflow**:
- **Client Configuration**: Reads client-specific settings (marketplaces, report types).
- **DAG Factory**: Generates Python code or JSON configs that Airflow interprets as DAGs.
- **Incremental Logic**: Handles logic for incremental data loads (only fetching new data).

**Scope**:
- incremental_aws_api_job_creator, incremental_vc_job_creator, etc.
- Logic to support new client onboarding automatically.

**Target Use Cases**:
- "Onboard a new client, 'BrandY', and automatically generate all their daily ETL jobs for Amazon US and UK."

### 4. File Triggers (`file_triggers/`)

**Description**: Event-driven automation scripts that detect the arrival of specific files (e.g., from an external scraper or manual upload) and trigger downstream processing.

**Key Workflow**:
- **File Sensing**: Monitors GCS buckets or local directories for specific file patterns.
- **Trigger**: Once a file arrives, it triggers a corresponding Airflow DAG or data loading script.
- **Validation**: Performs initial checks on file format and integrity.

**Scope**:
- `airflow_files_trigger.py`, `external_api_trigger.py`.
- Handling asynchronous data arrival.

**Target Use Cases**:
- "Start the 'Price Analysis' pipeline as soon as the 'competitor_prices.csv' file lands in the GCS bucket."

### 5. Data Movement (`data_movement/`)

**Description**: Scripts and utilities focused on moving large volumes of data between storage systems, primarily into and out of BigQuery.

**Key Workflow**:
- **Transfer**: Efficiently moves data from GCS to BigQuery tables.
- **Backup**: Scripts to snapshot or backup BigQuery datasets (`bq_dataset_backup.py`).
- **Migration**: Tools to help migrate data between environments or datasets.

**Scope**:
- BigQuery Data Transfer Service integration.
- Disaster recovery backup scripts.

**Target Use Cases**:
- "Backup the 'Sales' dataset before running a major schema migration."
- "Import a massive historical CSV dump into BigQuery."

### 6. Alerting (`alerting/`)

**Description**: A monitoring system that queries pipeline metadata and data quality metrics to generate alerts for the operations team.

**Key Workflow**:
- **Monitoring Queries**: Runs SQL queries against the metadata database or BigQuery logs (e.g., `failed_jobs_hourly_level_alert.sql`).
- **Notification**: Sends consolidated emails summarizing failures, SLAs missed, or data anomalies.

**Scope**:
- Pipeline health checks (failed jobs, hung tasks).
- Data SLA monitoring (did the data arrive on time?).
- Data quality alerts (null checks, volume anomalies).

**Target Use Cases**:
- "Alert the team if the 'Daily Sales' job hasn't completed by 8 AM EST."
- "Notify us if the number of rows in the 'Inventory' table drops by 50% unexpectedly."

### 7. Scraping (`scraping/`)

**Description**: Modules relating to direct web scraping of data sources that do not provide an API.

**Key Workflow**:
- **Source Modules**: Organized by source (e.g., `sharepoint`, `vantage_point`, `vendor_central`).
- **Extraction**: Uses Selenium/Python to log in, navigate, and download reports.

**Scope**:
- Vendor Central (Amazon) scraping.
- Vantage Point data extraction.
- SharePoint file retrieval.

**Target Use Cases**:
- "Log into Vendor Central and download the 'Net PPM' report for the last week."

### 8. ScrapeHero (`scrapehero/`)

**Description**: Integration specifically for handling data from ScrapeHero, a third-party competitive intelligence data provider.

**Key Workflow**:
- **Ingestion**: Detects and processes incoming files from ScrapeHero.
- **Transformation**: Normalizes ScrapeHero's data format into i2o's standard schema.
- **Loading**: Loads processed data into specific BigQuery tables for competitive analysis.

**Scope**:
- Custom logic for ScrapeHero data structures.

**Target Use Cases**:
- "Process the daily 'Competitor Price' feed from ScrapeHero and update the 'Price War' dashboard."

### 9. Crons (`crons/`)

**Description**: Contains crontab configuration files for various servers in the infrastructure.

**Key Workflow**:
- **Scheduling**: Defines the schedule for scripts that run outside of Airflow (e.g., system maintenance, lightweight triggers).
- **Deployment**: These files are likely deployed to `/etc/cron.d/` on respective servers.

**Scope**:
- `airflow_server`, `migration_server`, `rt_server` cron definitions.

**Target Use Cases**:
- "Run the 'disk space cleanup' script every Sunday at midnight."

### 10. Onboarding (`onboarding/`)

**Description**: Scripts to automate the technical setup for new clients.

**Key Workflow**:
- **Schema Creation**: Deploys standard BigQuery datasets and tables for a new tenant (`bq_deployment_scripts_executor.py`).
- **Configuration**: Sets up initial metadata in the database.

**Scope**:
- Client provisioning and setup automation.

**Target Use Cases**:
- "Initialize the database and BigQuery environment for a new customer signing up today."

### 11. Adhoc Scripts (`adhoc_scripts/`)

**Description**: A collection of one-off scripts, utilities, and temporary tools used by engineers for maintenance or specific data fixes.

**Scope**:
- `i2o_vp_sdk_download`: Miscellaneous utility implementations.

---

## Folder Summary Table

| Folder Name | Description | Key Tech / Features |
|:---|:---|:---|
| **`airflow/`** | Orchestration logic, DAGs, and SQL tasks | Apache Airflow, SQL, Python DAGs |
| **`common/`** | Shared utilities and helper functions | Python, SMTP, GCS/BQ Clients |
| **`job_creator/`** | Dynamic DAG generation factory | Python, Jinja2 (implied), Configuration Parsing |
| **`file_triggers/`** | Event-based execution triggers | Python, GCS Triggers, File Watchers |
| **`data_movement/`** | Bulk data transfer and backup | BigQuery API, Python |
| **`alerting/`** | Pipeline monitoring and alerting | SQL-based alerts, Python Emailer |
| **`scraping/`** | Web scraper implementations | Selenium, Python |
| **`scrapehero/`** | ScrapeHero data integration | Python, ETL logic |
| **`crons/`** | Server cron schedules | Crontab files |
| **`onboarding/`** | Client setup automation | Python, SQL DDL deployment |
| **`adhoc_scripts/`** | Miscellaneous tools | Python, Shell |

## Deployment Notes

### Environment Setup
1.  **Virtual Environment**: Create a Python 3.x virtual environment and install dependencies from `requirements.txt`.
2.  **Environment Variables**: Ensure `.env` files are configured at `/opt/airflow/i2o_env_dir/i2o_dp.env` with DB credentials and API keys.
3.  **GCP Service Accounts**: Functionality heavily relies on GCP Service Accounts with permissions for BigQuery, GCS, and Secret Manager.

### Application Deployment
- **Airflow**: Deploy `airflow/src/python` DAGs to the `dags/` folder of your Airflow scheduler.
- **SQL Scripts**: Deploy `airflow/src/sql` and `alerting/src/sql` to a known path accessible by the Airflow workers.
- **Cron Jobs**: Install crontab files from `crons/` to the respective servers.
