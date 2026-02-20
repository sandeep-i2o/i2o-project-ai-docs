GitHub URL: git@github.com:i2o-retail/i2o-image-comparison-producer.git

# i2o-image-comparison-producer Project Summary

## Description
`i2o-image-comparison-producer` is a Google Cloud Function that initiates the image comparison workflow. It queries Google BigQuery to identify products or images that require comparison (e.g., new listings, periodic checks) and publishes these tasks as messages to a Google Cloud Pub/Sub topic. This effectively decouples the job identification logic from the heavy processing logic handled by the `i2o-image-comparison` service.

## Technology Stack
- **Language:** Python 3.x
- **Platform:** Google Cloud Functions
- **Cloud Services:**
  - **Google BigQuery:** Source of truth for product data and comparison candidates.
  - **Google Cloud Pub/Sub:** Messaging middleware to distribute comparison tasks.
  - **Google Cloud Secret Manager:** For secure storage of configuration and credentials.
- **Key Libraries:**
  - `google-cloud-bigquery`: For executing SQL queries.
  - `google-cloud-pubsub`: For publishing messages.
  - `pandas`: Data handling.
  - `SQLAlchemy`, `psycopg2-binary`: Database interactions (likely for audit/status logging).

## Key Components
- **Cloud Function Entry Points (`main.py`):**
  - `hello_world`: Standard trigger for generating comparison jobs.
  - `trigger_backlog`: Trigger for processing backlog items (likely without auditing).
- **Record Generator (`record_generator.py`):** The orchestrator that calls the BigQuery reader, iterates through results, and invokes the writer to publish messages.
- **BigQuery Reader (`bq_record_reader.py`):** Executes queries against BigQuery to fetch image URLs and metadata for comparison.
- **Writers (`pubsub_writer.py`, `api_writer.py`):** Handles the actual dispatch of tasks either to Pub/Sub (production) or directly to an API (local/dev).
- **Job Status Service:** Updates the status of jobs in a relational database (PostgreSQL) to track progress and prevent duplicate processing.

## Project Structure
```
i2o-image-comparison-producer/
├── main.py                  # Cloud Function entry points
├── requirements.txt         # Dependencies
├── core/
│   ├── service/             # Business logic (record generation, job updates)
│   ├── reader/              # BigQuery interaction
│   ├── writer/              # PubSub/API publishers
│   └── transform/           # Data transformation logic
├── db/                      # Database connection and queries
├── config/                  # Configuration management
└── resources/               # SQL queries and other resources
```

## Key API Endpoints
This project is primarily a Cloud Function triggered via HTTP or Cloud Scheduler, rather than a REST API server.
- `trigger_job` (Internal function called by HTTP triggers): Accepts JSON payload with parameters like `project_id`, `start_date`, `end_date`, `marketplace`, etc.

## Scope & Target Use Cases
- **Batch Processing:** Periodically identifying large sets of images that need comparison (e.g., daily validation of product listings).
- **Pipeline Integration:** Serving as the "Source" in an Event-Driven Architecture, feeding work to the `i2o-image-comparison` "Sink".

## Deployment Notes
- **Google Cloud Functions:** Deployed as a scalable, serverless function.
- **Triggers:** Typically triggered by Google Cloud Scheduler for recurring jobs or via HTTP for ad-hoc requests.
- **Environment Variables:** Configuration for GCP Project ID, BigQuery datasets, and Pub/Sub topics is managed via environment variables.
