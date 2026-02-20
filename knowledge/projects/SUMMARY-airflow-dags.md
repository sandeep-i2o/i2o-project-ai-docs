GitHub URL: https://github.com/i2o-retail/airflow-dags.git

# i2o-retail/airflow-dags

## Description
The `airflow-dags` project contains the **Apache Airflow DAGs (Directed Acyclic Graphs)** responsible for orchestrating the data pipelines for i2o Retail. It handles the end-to-end data lifecycle, including data ingestion from various sources (e.g., Vendor Central, Seller Central), data transformation, loading into **Google BigQuery**, and archiving raw files in **Google Cloud Storage (GCS)**. It also includes automation for onboarding new clients and managing DAG execution.

## Technology Stack
-   **Orchestration:** Apache Airflow
-   **Programming Language:** Python, SQL, Shell
-   **Cloud Provider:** Google Cloud Platform (GCP)
    -   **Storage:** Google Cloud Storage (GCS)
    -   **Data Warehouse:** Google BigQuery
-   **Database:** PostgreSQL (for metadata and configuration)
-   **Key Libraries:**
    -   `apache-airflow`: Core orchestration framework.
    -   `pandas`: Data manipulation.
    -   `google-cloud-bigquery` & `google-cloud-storage`: GCP interactions.
    -   `sqlalchemy` & `psycopg2`: Database connectivity.
    -   `python-dotenv`: Environment configuration.

## Key Components

### 1. Onboarding Automation (`airflow_onboarding.py`)
-   **Purpose:** Automates the setup of DAGs for new clients or updates existing ones.
-   **Functionality:**
    -   Reads configuration and active client lists from the Postgres database.
    -   Triggers shell scripts to generate client-specific DAG files.
    -   Interacts with the Airflow REST API to enable DAGs and trigger initial runs.
    -   Updates the `client_project_mapper.json`.

### 2. Data Pipeline DAGs
These DAGs manage the data flow for specific data types (e.g., Advertising, Sales, Inventory).
-   **`adv_files_load.py`:** Handles advertising data loading.
-   **`vc_files_load.py` / `sc_files_load.py`:** Handles Vendor Central and Seller Central data loading.
-   **`marketplace_combined_metrics.py`:** Aggregates metrics from different marketplaces.
-   **Key Steps in DAGs:**
    1.  **Prestage:** Loads data from GCS to a staging table in BigQuery.
    2.  **Stage:** Performs initial transformations.
    3.  **Lake:** Loads data into the Data Lake layer.
    4.  **Archive:** Moves processed files to an archive bucket in GCS.
    5.  **Latest Data Load:** Updates the "latest" view of the data.
    6.  **Mart Creation:** Creates Data Marts for reporting (Campaign reports, Product data).
    7.  **Validation:** Runs sanity checks on the data marts.

### 3. Shared Utilities
The project relies on a shared library (likely `i2o_data_pipeline_automation`) locally available at `/opt/airflow/i2o_data_pipeline_automation` for:
-   `dag_methods`: Common DAG operations.
-   `custom_operators`: Specialized Airflow operators (e.g., `CloudStorageToBigQueryOperator`).
-   `read_config_json`: Configuration management.

## Project Structure
```
airflow-dags/
├── config/                 # JSON configuration files for DAGs
│   ├── airflow_onboarding.json
│   ├── airflow_configuration/
│   └── ...
├── src/
│   ├── python/             # Python scripts defining the DAGs
│   │   ├── airflow_onboarding.py
│   │   ├── adv_files_load.py
│   │   └── ...
│   ├── sql/                # SQL scripts for BigQuery transformations
│   │   └── ...
│   └── shell/              # Shell scripts for execution
│       └── airflow_onboarding.sh
├── .env                    # Environment variables (not committed)
└── README.md               # Project documentation
```

## Key Configuration & APIs
This project does not expose a REST API itself but orchestrates calls to:
-   **Airflow REST API:** Used internally by the onboarding script to manage DAG states.
-   **Database APIs:** Interacts with Postgres for metadata management.

## Scope
The scope of this project is limited to the **Data Orchestration Layer** of the i2o Retail platform. It assumes the existence of:
-   Data being delivered to GCS buckets.
-   A BigQuery environment for data warehousing.
-   A Postgres database for metadata.
-   A shared library for common functions.

## Target Use Cases
1.  **Daily Data Ingestion:** Automatically load and process daily reports from Amazon Vendor/Seller Central.
2.  **Client Onboarding:** Quickly set up data pipelines for new customers without manual DAG creation.
3.  **Data Quality Checks:** Ensure data integrity through automated sanity checks in the pipeline.
4.  **Data Archival:** maintain a history of raw data files for audit and replay purposes.

## Deployment Notes
-   **Environment:** Designed to run in a Dockerized Airflow environment (suggested by usage of `/opt/airflow`).
-   **Dependencies:** Requires the `i2o_data_pipeline_automation` library to be present in the `PYTHONPATH` or specific directory.
-   **Configuration:**
    -   Environment variables must be set (likely via `.env` file mounted to the container).
    -   GCP Service Account credentials are required for GCS and BigQuery access.
    -   Postgres connection strings must be configured in the Airflow connections or environment variables.
