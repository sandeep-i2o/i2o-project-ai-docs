GitHub URL: https://gitlab.i2oretail.com/i2o/automation/i2o-dp-onboarding-service.git

# i2o-dp-onboarding-service Project Summary

## Description
The `i2o-dp-onboarding-service` is a Flask-based REST API microservice designed to orchestrate and manage the client onboarding process within the i2o data pipeline. It acts as a central hub for triggering and tracking various onboarding stages, including database setup, Airflow DAG generation, BigQuery migration, and historical data loading. It integrates with Google Cloud services and the internal PostgreSQL database to maintain the state of onboarding for different organizations.

## Technology Stack
- **Language:** Python 3.10
- **Framework:** Flask (Web API), Gunicorn (WSGI Server)
- **Database:** PostgreSQL (Cloud SQL)
- **Cloud Services:**
  - **Google Cloud Secret Manager:** For retrieving secure credentials.
  - **Google Cloud Logging:** For centralized application logging.
  - **Google Cloud BigQuery:** Interaction for migration and data loading.
- **Key Libraries:**
  - `flask`, `flask_cors`: API development.
  - `psycopg2-binary`, `SQLAlchemy`: Database connectivity.
  - `pandas`: Data manipulation.
  - `selenium`: Browser automation (likely for specific scraping/validation tasks during onboarding).
  - `google-cloud-*`: SDKs for GCP services (Storage, Secret Manager, PubSub, etc.).

## Key Components
- **Onboarding API (`onboard_route`):** Manages the lifecycle and status of client onboarding (create, get status, update status).
- **Airflow Onboarding (`airflow_onboarding_route`):** Triggers the generation or update of Airflow DAGs for new clients.
- **DB Setup (`db_setup_route`):** Handles the initialization of database schemas and tables for new clients.
- **Migration APIs (`bq_migration_route`, `sync_migration_job_creator_route`):** Manages migration jobs for moving data between systems or environments.
- **Product Discovery (`product_discovery_job_creator`):** Utilities for initiating product discovery jobs (likely utilizing Selenium).

## Project Structure
```
i2o-dp-onboarding-service/
├── dev.yaml, qa.yaml, uat.yaml, preprod.yaml # App Engine/Cloud Run configuration per environment
├── requirements.txt                          # Python dependencies
├── src/
│   └── python/
│       ├── index.py                          # Main Flask application entry point
│       ├── onboarding/
│       │   ├── api/                          # Route definitions (Controllers)
│       │   ├── config/                       # Configuration and constants
│       │   ├── core/                         # Business logic and services
│       │   │   └── service/
│       │   └── db_setup/                     # Database initialization logic
│       └── utils/                            # Helper utilities (email, otp, etc.)
└── venv/                                     # Virtual environment
```

## Key API Endpoints
| Endpoint Base | Method | Description |
|---------------|--------|-------------|
| `/dp/onboard` | POST, GET, PATCH | Create onboarding requests, check status by Org/Stage, and update progress. |
| `/dp/airflowsetup/dagsonboard` | POST | Triggers the creation of Airflow DAGs for a client. |
| `/dp/dp_db_setup` | POST | Initiates the setup of the Data Pipeline database for a client. |
| `/dp/bq_migration` | POST | Triggers BigQuery data migration tasks. |
| `/dp/processing_server_setup` | POST | Sets up processing server resources. |

## Scope & Target Use Cases
- **New Client Setup:** Automates the technical onboarding of new retail clients onto the i2o platform.
- **Process Orchestration:** Ensures dependencies between onboarding steps (DB setup -> Airflow DAGs -> Data Load) are respected.
- **Status Tracking:** Provides visibility into the progress of onboarding for internal admin tools.

## Deployment Notes
- **App Engine / Cloud Run:** Configured via `dev.yaml`, `qa.yaml`, etc., suggesting deployment to Google App Engine or Cloud Run.
- **Environment Variables:** Critical for configuration (`ENV`, `PROJECT_ID`), loaded at runtime.
- **Port:** Defaults to port 5000.
