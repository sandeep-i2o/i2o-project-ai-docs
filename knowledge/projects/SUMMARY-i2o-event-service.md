GitHub URL: git@github.com:i2o-retail/i2o-event-service.git

# i2o-event-service - Project Summary

## Description

The **i2o-event-service** is a **data pipeline orchestration service** for the i2o retail platform. It provides capabilities for creating, scheduling, and monitoring data processing events using **Google Cloud Dataflow**. The service manages event execution, tracks job statuses, provides dashboard analytics for event performance, and handles client performance metrics aggregation.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 2.7.1 |
| **Language** | Java 8 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Hibernate |
| **Cloud Services** | Google Cloud (BigQuery, Dataflow, Storage, Secret Manager) |
| **Data Pipeline** | Apache Beam (Dataflow runner) 2.40.0 |
| **Tracing** | Spring Cloud Sleuth 3.1.3, Zipkin Brave |
| **Monitoring** | Spring Boot Actuator |
| **Networking** | Netty, gRPC |
| **Utilities** | Lombok |

---

## Key Components

### Controllers (2 total)
- **EventsController** - Main REST controller for event operations
- **BaseController** - Common controller functionality

### Services (4 total)
- **EventServices** - Core event scheduling and dashboard logic
- **DataflowService** - Google Cloud Dataflow job execution
- **BigQueryServices** - BigQuery data operations
- **SchedulerTaskService** - Scheduled task management

### Repositories (6 total)
- **EventHasOrganizationRepository** - Event-organization mappings
- **EventDefinitionRepository** - Event definitions and configurations
- Additional repositories for event data management

### Models (23 total)
- Event definitions, job responses, dashboard filters, performance metrics
- Organization mappings, event configurations

### Utilities (10 total)
- **GoogleSecretManager** - GCP Secret Manager integration
- Data transformation and helper utilities

---

## Project Structure

```
i2o-event-service/
├── src/
│   └── main/
│       └── java/com/corecompete/i2o/
│           ├── I2oEventApplication.java
│           ├── GoogleSecretManager.java
│           ├── bq/                  # BigQuery services (2 files)
│           ├── constants/           # Constants (2 files)
│           ├── controller/          # REST controllers (2 files)
│           ├── exception/           # Custom exceptions (1 file)
│           ├── models/              # Domain models (23 files)
│           ├── repository/          # JPA repositories (6 files)
│           ├── scheduler/           # Scheduled tasks (1 file)
│           ├── services/            # Business services (2 files)
│           └── utility/             # Utilities (10 files)
└── pom.xml
```

---

## Key API Endpoints

### Event Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check endpoint |
| `/run-event` | POST | Trigger data processing event(s) |
| `/job-details` | GET | Get Dataflow job details by job ID |
| `/job-details` | POST | Get multiple job details by list of IDs |
| `/get-event-dashboard-by-filterV2` | POST | Get event dashboard analytics with filters |
| `/update-client-performance-metrics` | POST | Update client performance metrics |

### Request/Response Examples

#### Run Event Request
```json
[
  {
    "eventId": "string",
    "orgId": "string",
    "startDate": "yyyy-MM-dd",
    "endDate": "yyyy-MM-dd"
  }
]
```

#### Job Response
```json
{
  "jobId": "string",
  "status": "RUNNING|COMPLETED|FAILED"
}
```

---

## Scope of the Project

The i2o-event-service covers:

1. **Event Orchestration** - Schedule and run data processing events
2. **Dataflow Integration** - Launch and monitor Google Cloud Dataflow jobs
3. **Job Monitoring** - Track job status and progress
4. **Dashboard Analytics** - Event performance visualization
5. **Client Metrics** - Performance metrics tracking and updates
6. **Secret Management** - Secure credential retrieval from GCP
7. **BigQuery Integration** - Analytics data queries
8. **Multi-Organization Support** - Organization-scoped events
9. **Flex Templates** - Dataflow Flex Template job launches
10. **Data Pipeline Automation** - Automated data processing workflows

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Data Pipeline Execution** | Trigger ETL/data processing jobs |
| **Event Scheduling** | Schedule data processing events |
| **Job Monitoring** | Track Dataflow job status and progress |
| **Performance Analytics** | Dashboard for event performance metrics |
| **Client Metrics** | Update and track client performance |
| **Automated Processing** | Scheduled automated data workflows |
| **Multi-Tenant Events** | Organization-specific event execution |
| **Pipeline Dashboards** | Visualize data pipeline health |

---

## Deployment Notes

### Environment Configuration
The application requires configuration properties for:
- `project_id` - GCP project ID
- `location` - Dataflow job location
- `zone` - GCP zone
- `network` / `sub_network` - VPC network settings
- `gcs_path` - Dataflow template GCS path
- `gcs_temp_location` - Temporary GCS location
- `write_to_table` - BigQuery destination table
- `secret-manager-db-id` - Secret Manager ID for database credentials

### Packaging
- Packaged as **WAR** file (`events-0.0.1.war`) for Tomcat deployment

### Cloud Dependencies
- **Google Cloud Dataflow** - Data pipeline execution
- **Google BigQuery** - Analytics data storage and queries
- **Google Cloud Storage** - Dataflow templates and temp files
- **Google Secret Manager** - Secure credential storage
- **Google Cloud SQL** (PostgreSQL) - Event metadata storage

### Build Commands
```bash
# Build
./mvnw clean package

# Run locally
./mvnw spring-boot:run

# Run tests
./mvnw test
```

### Dataflow Integration
The service launches Dataflow jobs using:
- **Flex Templates** - Container-based job definitions
- **REST API** - Direct Dataflow API calls
- **OAuth2 Authentication** - Google credentials with required scopes:
  - `cloud-platform`
  - `compute`
  - `userinfo.email`

### Key Configuration Properties
```properties
# GCP Configuration
project_id=your-gcp-project
location=us-central1
zone=us-central1-a

# Network Configuration
network=your-vpc-network
sub_network=your-subnet

# GCS Configuration
gcs_path=gs://bucket/templates/template.json
gcs_temp_location=gs://bucket/temp

# Secret Manager
secret-manager-db-id=db-credentials-secret
```

### Monitoring
- Spring Boot Actuator endpoints for health checks
- Spring Cloud Sleuth for distributed tracing
- Dataflow job status monitoring via GCP Console
