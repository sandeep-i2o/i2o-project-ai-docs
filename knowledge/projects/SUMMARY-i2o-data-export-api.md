GitHub URL: https://github.com/i2o-retail/i2o-data-export-api.git

# i2o-data-export-api - Project Summary

## Description

The **i2o-data-export-api** is a **data export and integration service** for the i2o retail platform. It enables organizations to export their data to external destinations using **Airbyte** as the underlying data pipeline orchestrator. The service supports multiple destination types including Snowflake, BigQuery, S3, GCS, Redshift, PostgreSQL, and SFTP. It provides a complete pipeline management system with scheduling, job history tracking, callbacks, and real-time status updates via WebSocket.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python 3.10 |
| **Web Framework** | Flask 3.0.3 |
| **ASGI Server** | Gunicorn 22.0.0, Uvicorn 0.23.2 |
| **WebSocket** | Flask-SocketIO 4.3.1, Eventlet 0.39.0 |
| **ORM** | SQLAlchemy 2.0.30 |
| **Database** | PostgreSQL (psycopg2-binary 2.9.9) |
| **Data Pipeline** | Airbyte (external integration) |
| **Cloud Services** | Google Cloud (Secret Manager, Logging) |
| **Email** | SendGrid 6.9.7 |
| **Authentication** | PyJWT 2.10.1, python-jose 3.3.0 |
| **HTTP Client** | httpx 0.28.1, Requests 2.32.3 |
| **Data Processing** | Pandas 2.2.1, NumPy 1.26.4 |
| **Retry Logic** | Tenacity 8.3.0 |
| **API Documentation** | OpenAPI 3.0 (Swagger) |

---

## Key Components

### API Layer
- **connectors_api.py** - Connector configuration management
- **data_destination_api.py** - Destination CRUD operations
- **data_pipeline_api.py** - Pipeline lifecycle management
- **jobs_history_api.py** - Job history and status
- **callback_api.py** - External callback endpoints
- **callback_internal_api.py** - Internal callback processing
- **socket_io.py** - Real-time WebSocket updates
- **auth.py** - JWT authentication

### Core Services
- **service.py** - Main service orchestration
- **error.py** - Custom error handling
- **utils.py** - Utility functions

### Providers (Airbyte Integration)
- **airbyte_config.py** - Airbyte configuration
- **airbyte_connector_config.py** - Connector configuration service
- **airbyte_destination.py** - Destination management
- **airbyte_pipeline_service.py** - Pipeline CRUD operations
- **airbyte_source_service.py** - Source management
- **airbyte_callback_service.py** - Callback processing
- **airbyte_job_history.py** - Job history retrieval
- **auth.py** - Airbyte API authentication

### SPI (Service Provider Interface)
- **auth_service.py** - Authentication abstraction
- **connector_config_service.py** - Connector config interface
- **destination_service.py** - Destination interface
- **pipeline_service.py** - Pipeline interface
- **source_service.py** - Source interface
- **callback_service.py** - Callback interface
- **job_history_service.py** - Job history interface

### Data Access Objects (DAOs)
- **connector_config_dao.py** - Connector configurations
- **data_destination_dao.py** - Destinations
- **data_pipeline_dao.py** - Pipelines
- **data_source_dao.py** - Data sources
- **data_schedule_dao.py** - Schedules
- **job_log_dao.py** - Job logs
- **audit_log_dao.py** - Audit logs
- **organization_dao.py** - Organizations
- **modules_dao.py** - Data modules

### Wrappers
- **data_pipeline.py** - Pipeline wrapper
- **data_destination.py** - Destination wrapper
- **data_source.py** - Source wrapper
- **connector_config.py** - Connector config wrapper
- **callback.py** - Callback wrapper
- **job_history.py** - Job history wrapper
- **audit.py** - Audit wrapper

### IO Utilities
- **db/** - Database connections (app, de, dp)
- **secretmanager/** - GCP Secret Manager
- **email/** - Email notifications (SendGrid)

---

## Project Structure

```
i2o-data-export-api/
├── i2o/
│   ├── main.py                   # Flask app entry point
│   ├── api/                      # REST API endpoints
│   │   ├── auth.py
│   │   ├── connectors_api.py
│   │   ├── data_destination_api.py
│   │   ├── data_pipeline_api.py
│   │   ├── jobs_history_api.py
│   │   ├── callback_api.py
│   │   ├── callback_internal_api.py
│   │   └── socket_io.py
│   ├── config/                   # Configuration
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── env_config.py
│   │   └── logger_config.py
│   ├── core/                     # Core services
│   │   ├── service.py
│   │   ├── error.py
│   │   ├── dao/                  # Data Access Objects
│   │   ├── providers/            # Provider implementations
│   │   │   └── airbyte/          # Airbyte integration
│   │   ├── spi/                  # Service Provider Interfaces
│   │   └── wrappers/             # Business logic wrappers
│   └── ioutils/                  # IO utilities
│       ├── db/                   # Database connections
│       ├── email/                # Email service
│       └── secretmanager/        # GCP Secret Manager
├── resources/
│   ├── swagger.yaml              # API documentation
│   ├── airbyte_draft_json/       # Airbyte config templates
│   ├── mail_templates/           # Email templates
│   ├── scripts/                  # DDL/DML scripts
│   └── er-diagram/               # ER diagrams
├── tests/                        # Unit tests
│   ├── providers/airbyte/
│   └── wrappers/
├── dev.yaml / qa.yaml / uat.yaml / preprod.yaml / prod.yaml
├── requirements.txt
├── run.sh
└── Dockerfile (implied)
```

---

## Key API Endpoints

### Health Check
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthcheck` | GET | Health check endpoint |

### Connector Configuration
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/connector_config` | GET | List all connector configurations |
| `/api/v1/dataexport/connectors_config/test` | POST | Test connector configuration |

### Data Destinations
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/{org_id}/destinations` | GET | List organization destinations |
| `/api/v1/dataexport/{org_id}/destinations` | POST | Create new destination |
| `/api/v1/dataexport/{org_id}/destinations/{id}` | GET | Get destination details |
| `/api/v1/dataexport/{org_id}/destinations/{id}` | PUT | Update destination |
| `/api/v1/dataexport/{org_id}/destinations/{id}` | DELETE | Delete destination |

### Pipelines
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/{org_id}/pipeline` | GET | List organization pipelines |
| `/api/v1/dataexport/{org_id}/pipeline` | POST | Create new pipeline |
| `/api/v1/dataexport/{org_id}/pipeline` | PUT | Enable/disable pipeline |
| `/api/v1/dataexport/{org_id}/pipeline/{id}` | GET | Get pipeline details |
| `/api/v1/dataexport/{org_id}/pipeline/{id}/sync` | POST | Trigger manual sync |

### Modules
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/{org_id}/modules` | GET | List available data modules |

### Job History
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/{org_id}/pipeline/{id}/jobs` | GET | Get pipeline job history |

### Callbacks
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/dataexport/callback` | POST | Airbyte sync callback |

---

## Supported Destinations

| Destination | Description |
|-------------|-------------|
| **Snowflake** | Cloud data warehouse |
| **Google BigQuery** | GCP analytics data warehouse |
| **Amazon S3** | AWS object storage |
| **Google Cloud Storage** | GCP object storage |
| **Amazon Redshift** | AWS data warehouse |
| **PostgreSQL** | Relational database |
| **SFTP (JSON)** | Secure file transfer |

---

## Scope of the Project

The i2o-data-export-api covers:

1. **Pipeline Management** - Create, update, enable/disable data pipelines
2. **Destination Configuration** - Configure export destinations
3. **Connector Testing** - Validate destination credentials
4. **Sync Scheduling** - Configure sync frequency (manual, hourly, daily)
5. **Job Monitoring** - Track sync job status and history
6. **Callback Processing** - Handle Airbyte sync completion events
7. **Email Notifications** - Success/failure email alerts
8. **Real-time Updates** - WebSocket status notifications
9. **Audit Logging** - Track all configuration changes
10. **Multi-tenant Support** - Organization-scoped pipelines

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Data Warehouse Export** | Export data to Snowflake/BigQuery |
| **Cloud Storage Backup** | Export to S3/GCS for backup |
| **Custom Analytics** | Export to customer's own data warehouse |
| **Data Lake Integration** | Feed data to external data lakes |
| **Scheduled Exports** | Automated periodic data exports |
| **On-demand Sync** | Manual trigger for immediate export |
| **Multi-destination** | Export to multiple destinations |
| **Status Monitoring** | Real-time sync status tracking |

---

## Deployment Notes

### Environment Configuration
Multiple YAML configuration files for different environments:
- `dev.yaml` - Development
- `qa.yaml` - QA testing
- `uat.yaml` - User acceptance testing
- `preprod.yaml` - Pre-production
- `prod.yaml` - Production

### Running Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run with Gunicorn
./run.sh

# Or with Eventlet (for WebSocket)
./run-eventlet.sh

# Direct Flask run
python -m i2o.main
```

### Cloud Dependencies
- **Airbyte** - External data pipeline orchestrator
- **Google Secret Manager** - Credential storage
- **Google Cloud Logging** - Centralized logging
- **SendGrid** - Email notifications
- **PostgreSQL** - Application database

### Database Setup
```bash
# Run DDL scripts
psql -f resources/scripts/data-export-ddl.sql

# Run DML scripts (seed data)
psql -f resources/scripts/data-export-dml.sql
```

### API Documentation
- Swagger/OpenAPI spec available at `resources/swagger.yaml`
- Postman collection at `resources/Data Export API.postman_collection.json`

### Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=i2o tests/
```

### Key Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:pass@host:port/db

# Airbyte
AIRBYTE_API_URL=https://api.airbyte.com
AIRBYTE_API_KEY=your-api-key

# GCP
GOOGLE_CLOUD_PROJECT=your-project-id
SECRET_MANAGER_PROJECT=your-project-id

# SendGrid
SENDGRID_API_KEY=your-api-key
```
