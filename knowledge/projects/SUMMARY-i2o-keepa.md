GitHub URL: git@github.com:i2o-retail/i2o-keepa.git

# i2o-keepa - Project Summary

## Description

The **i2o-keepa** is a **product data collection service** for the i2o retail platform. It integrates with **Keepa API** and **DataSpark** to fetch product pricing history, sales rank, buy box data, and product details from Amazon marketplaces. The service uses **Celery** for asynchronous task processing, supports rate limiting via Redis, and stores results in **Google Cloud Storage** as Parquet files and loads them to **BigQuery** for downstream analytics.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python 3.10 |
| **Web Framework** | Flask 2.3.2 |
| **Task Queue** | Celery 5.3.1 |
| **Message Broker** | Redis 4.5.4 |
| **Data APIs** | Keepa 1.3.6, DataSpark |
| **Database** | PostgreSQL (psycopg2-binary 2.9.10) |
| **Cloud Services** | Google Cloud (Storage, BigQuery, Secret Manager) |
| **Data Processing** | Pandas 2.0.2, NumPy 1.25.0, PyArrow 8.0 |
| **HTTP Client** | aiohttp 3.8.4, Requests 2.31.0 |
| **Retry Logic** | Tenacity 8.3.0 |
| **Monitoring** | Flower 2.0.1 (Celery monitoring) |
| **Container** | Docker (Python 3.10 slim base) |
| **Reverse Proxy** | Nginx |

---

## Key Components

### Core Application
- **app.py** - Flask application with Celery integration and task endpoints
- **celerymethod.py** - Celery app initialization
- **config.py** - Environment configuration
- **task.py** - Main task orchestration and job initialization
- **models.py** - Data models (KeepaProductAuditRecord, KeepaProgressRecord)
- **utils.py** - Utility functions for data processing and time logging
- **secret.py** - Google Secret Manager integration

### Jobs Module
- **task_factory.py** - Factory pattern for creating API tasks
- **api_task.py** - Base API task interface
- **api_task_helper.py** - Task execution helpers
- **keepa/keepa_buybox_api_task.py** - Keepa BuyBox and product details processor
- **dataspark/** - DataSpark-specific job processors

### Database Layer
- **db/app_db.py** - Application database (ASIN management, progress records)
- **db/dp_db.py** - Data processing database (audits, job status)
- **db_service.py** - Task ID storage/retrieval for idempotency

### Rate Limiting
- **rate_limiter/keepa_rate_limiter.py** - Keepa API rate limiting
- **rate_limiter/redis_rate_limiter.py** - Redis-based rate limiter
- **rate_limiter/lua_script.lua** - Atomic Redis operations

### Resources
- **resources/dataschema.json** - BigQuery schema definitions

---

## Project Structure

```
i2o-keepa/
├── i2o/
│   ├── __init__.py
│   ├── app.py                    # Flask + Celery app
│   ├── celerymethod.py           # Celery initialization
│   ├── config.py                 # Configuration
│   ├── db_service.py             # Task ID storage
│   ├── models.py                 # Data models
│   ├── secret.py                 # Secret Manager
│   ├── task.py                   # Task orchestration
│   ├── utils.py                  # Utilities
│   ├── db/                       # Database layer
│   │   ├── app_db.py             # App database
│   │   └── dp_db.py              # DP database
│   ├── jobs/                     # Job processors
│   │   ├── api_task.py           # Base API task
│   │   ├── api_task_helper.py    # Task helpers
│   │   ├── task_factory.py       # Task factory
│   │   ├── keepa/                # Keepa jobs
│   │   │   └── keepa_buybox_api_task.py
│   │   └── dataspark/            # DataSpark jobs
│   ├── rate_limiter/             # Rate limiting
│   │   ├── keepa_rate_limiter.py
│   │   ├── redis_rate_limiter.py
│   │   └── lua_script.lua
│   └── resources/
│       └── dataschema.json       # BQ schema
├── scripts/
│   ├── startup.sh                # Production startup
│   ├── startup-dev.sh            # Dev startup
│   └── healthcheck.sh            # Health check
├── tests/                        # Unit tests
│   ├── test_app_db.py
│   ├── test_db_service.py
│   ├── test_get_pending_job_details.py
│   └── test_keepa_buybox_api_task.py
├── Dockerfile                    # Production Docker
├── Dockerfile-dev                # Dev Docker
├── docker-compose.yml
├── nginx.conf
└── requirements.txt
```

---

## Key API Endpoints

### Flask REST Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/result/<id>` | GET | Get Celery task result by task ID |

### Celery Tasks
| Task Name | Description |
|-----------|-------------|
| `main_thread` | Main Keepa/DataSpark data collection task |
| `main_task_health_check` | Idempotency and health check for tasks |
| `check_for_new_dp_jobs` | Scheduled job to find new pending audits |

### KeepaBuyBoxApiTask Methods
| Method | Description |
|--------|-------------|
| `read_inputs()` | Read ASINs and configuration |
| `call_api()` | Fetch data from Keepa API |
| `convert_results()` | Transform API response |
| `json_to_csv()` | Convert JSON to CSV format |
| `save_file_to_gcs()` | Upload to Google Cloud Storage |
| `load_to_bq()` | Load data to BigQuery |
| `close_job()` | Finalize job status |

### Task Result Response
```json
{
  "ready": true,
  "successful": true,
  "state": "SUCCESS",
  "value": {
    "detail_id": "123",
    "output_folder": "gs://bucket/path"
  }
}
```

---

## Scope of the Project

The i2o-keepa service covers:

1. **Keepa API Integration** - Fetch product pricing history and sales rank
2. **Buy Box Data Collection** - Track buy box status and pricing
3. **Product Details Retrieval** - Comprehensive product information
4. **DataSpark Integration** - Alternative data source for product data
5. **Async Task Processing** - Celery-based job execution with progress tracking
6. **Rate Limiting** - Redis-based API rate limiting with Lua scripts
7. **Chunked Processing** - Split large ASIN lists into manageable chunks
8. **GCS Storage** - Store results as Parquet files
9. **BigQuery Loading** - Direct load to analytics tables
10. **Job Idempotency** - Prevent duplicate task execution
11. **Health Monitoring** - Task state tracking and recovery

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Price History Collection** | Fetch historical pricing data from Keepa |
| **Sales Rank Tracking** | Track product sales rank over time |
| **Buy Box Monitoring** | Monitor buy box status and ownership |
| **Product Discovery** | Collect new product data and details |
| **Periodic Data Refresh** | Scheduled data collection jobs |
| **Historical Backfill** | Bulk historical data collection |
| **Marketplace Analytics** | Cross-marketplace product analysis |
| **Rate-Limited API Calls** | Manage API quotas efficiently |
| **Analytics Pipeline** | Feed data to BigQuery for analysis |

---

## Deployment Notes

### Docker Deployment
```dockerfile
FROM python:3.10-slim

# Install Redis and Nginx
RUN apt update && apt install redis-server nginx -y

# Install Python dependencies
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=5 \
  CMD ./scripts/healthcheck.sh || exit 1

CMD [ "/bin/bash", "-c", "./scripts/startup-dev.sh"]
```

### Docker Compose
```bash
docker-compose up
```

### Cloud Dependencies
- **Google Cloud Storage** - Parquet file storage
- **Google BigQuery** - Analytics data loading
- **Google Secret Manager** - API keys and credentials
- **Redis** - Celery broker and rate limiter backend

### Environment Variables
```bash
# Required configuration
REDIS_URL=redis://localhost:6379
KEEPA_API_KEY=your-keepa-api-key
GCS_BUCKET=your-gcs-bucket
SHARED_ORG_ID=your-org-id
SHARED_PROJECT_ID=your-gcp-project
KEEPA_PRODUCT_DETAILS_TEMP_TABLE=your-bq-table
```

### Running Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Start Redis
redis-server

# Start Celery worker
celery -A i2o.app.celery_app worker --loglevel=info

# Start Celery beat (scheduler)
celery -A i2o.app.celery_app beat --loglevel=info

# Start Flask app
python -m i2o.app

# Start Flower (monitoring)
celery -A i2o.app.celery_app flower
```

### Testing
```bash
# Run tests
pytest tests/

# Specific test files available:
# - test_app_db.py
# - test_db_service.py
# - test_get_pending_job_details.py
# - test_keepa_buybox_api_task.py
```

### Monitoring
- **Flower Dashboard** - Celery task monitoring at `:5555`
- **Health Check Endpoint** - Container health via `healthcheck.sh`
- **Task Progress** - Track via `/result/<task_id>`
