GitHub URL: git@github.com:i2o-retail/i2o-api-reports-downloader.git

# i2o API Reports Downloader

## Description

A Java Spring Boot microservice for downloading and managing reports through Amazon Selling Partner APIs (SP-API). The service provides a reliable way to trigger, execute, and download various types of reports from Amazon marketplaces with robust error handling, rate limiting, and retry mechanisms. It supports multiple API types including inventory reports, catalog lookups, pricing data, purchase orders, and financial events.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Java 8 |
| **Framework** | Spring Boot 2.6.11 |
| **Build Tool** | Maven |
| **ORM** | Spring Data JPA |
| **Database** | PostgreSQL |
| **Cloud Platform** | Google Cloud Platform |
| **Secret Management** | GCP Secret Manager |
| **Object Storage** | Google Cloud Storage |
| **HTTP Client** | Spring WebFlux |
| **Distributed Tracing** | Spring Cloud Sleuth |
| **Email Service** | SendGrid |
| **API Documentation** | SpringDoc OpenAPI (Swagger) |
| **Code Quality** | JaCoCo, SonarQube |
| **Containerization** | Docker |

## Key Components

| Component | Package | Description |
|-----------|---------|-------------|
| **Report Controller** | `controller` | REST endpoints for report triggering and management |
| **WebHook Controller** | `controller` | Webhook endpoints for async callbacks |
| **Report Service** | `service` | Core business logic for report generation |
| **Runnable Service** | `service` | Task execution and scheduling |
| **Email Service** | `service` | Email notifications via SendGrid |
| **API Services Helper** | `service` | Helper for SP-API interactions |
| **GCS Service** | `service` | Google Cloud Storage operations |
| **SP-API Integration** | `service/spapi` | Selling Partner API integration |
| **AD-API Integration** | `service/adapi` | Amazon Advertising API integration |
| **DAO Layer** | `dao` | Data Access Objects (13 classes) |
| **DTOs** | `dto` | Data Transfer Objects (20 classes) |
| **Runnable Tasks** | `runnable` | Background task implementations (17 classes) |
| **Exception Handling** | `exceptions` | Custom exceptions (16 classes) |
| **Configuration** | `config` | App configuration (10 classes) |

## Project Structure

```
i2o-api-reports-downloader/
├── pom.xml                     # Maven build configuration
├── Dockerfile                  # Container configuration
├── docker-compose.yml          # Docker Compose setup
├── openapi.yaml                # OpenAPI 3.0 specification
├── src/
│   └── main/
│       ├── java/
│       │   └── com/i2oretail/scraping/
│       │       ├── I2oApplication.java      # Spring Boot entry point
│       │       ├── config/                  # Configuration classes
│       │       │   ├── ControllerConfig.java
│       │       │   └── TaskSchedulerConfig.java
│       │       ├── constants/               # Application constants
│       │       ├── controller/              # REST controllers
│       │       │   ├── ReportController.java
│       │       │   └── WebHookController.java
│       │       ├── dao/                     # Data Access Objects
│       │       ├── dto/                     # Data Transfer Objects
│       │       ├── entity/                  # JPA entities
│       │       ├── exceptions/              # Custom exceptions
│       │       ├── models/                  # Domain models
│       │       ├── repository/              # JPA repositories
│       │       ├── runnable/                # Background tasks
│       │       │   └── ApiRunnable.java
│       │       ├── service/                 # Business services
│       │       │   ├── ReportService.java
│       │       │   ├── RunnableService.java
│       │       │   ├── EmailService.java
│       │       │   ├── adapi/               # Amazon Ads API
│       │       │   └── spapi/               # Selling Partner API
│       │       └── utility/                 # Utility classes
│       └── resources/
│           └── swagger.yaml                 # Swagger configuration
├── docs/                       # Documentation
└── target/                     # Build output
```

## Key API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/request` | POST | Execute a Selling Partner API request |
| `/scraping/trigger` | POST | Trigger a report generation process |

### API Types Supported

| apiType | Description |
|---------|-------------|
| `getReport` | Generate SP-API reports (sales, traffic, inventory) |
| `getCatalog` | Retrieve catalog item information |
| `getProductPricing` | Get product pricing data |
| `getPurchaseOrder` | Retrieve purchase orders (Vendor Central) |
| `getFinancing` | Get financial event groups |

### Request Example
```json
{
  "marketplaceId": 1,
  "secretName": "aws-secret-prod-sp-api",
  "appSecretName": "aws-secret-app-credentials",
  "refreshToken": "Atzc2IY8h2Ym...",
  "apiType": "getReport",
  "traceId": "550e8400-e29b-41d4-a716-446655440000",
  "specification": {
    "reportType": "GET_SALES_AND_TRAFFIC_REPORT",
    "marketplaceIds": ["ATVPDKIKX0DER"],
    "dataStartTime": "2025-12-01T00:00:00Z",
    "dataEndTime": "2025-12-25T23:59:59Z"
  }
}
```

## Scope of the Project

- Integrate with Amazon Selling Partner APIs (SP-API)
- Execute report generation requests with configurable parameters
- Handle catalog lookups and product pricing queries
- Support purchase order and financial event retrieval
- Implement robust retry mechanisms with exponential backoff
- Provide rate limiting to avoid overwhelming target services
- Store and manage credentials securely via GCP Secret Manager
- Send email notifications on report completion

## Target Use Cases

1. **E-commerce Analytics**: Download sales and traffic reports from Amazon
2. **Inventory Management**: Retrieve inventory data for stock planning
3. **Pricing Intelligence**: Fetch competitive pricing information
4. **Vendor Operations**: Access purchase orders from Vendor Central
5. **Financial Reconciliation**: Retrieve financial events for accounting
6. **Data Pipeline**: Feed Amazon data into downstream analytics systems

## Deployment Notes

### Build
```bash
mvn clean package -Pdev
```

### Run Locally
```bash
java -jar target/api-report-downloader-1.0.0.jar --spring.profiles.active=local
```

### Docker Build
```bash
docker build -t i2o-api-reports-downloader .
docker run -p 8080:8080 i2o-api-reports-downloader
```

### Docker Compose
```bash
docker-compose up -d
```

### Available Profiles
| Profile | Description |
|---------|-------------|
| `local` | Local development (default) |
| `dev` | Development environment |
| `qa` | QA/Testing environment |
| `uat` | User Acceptance Testing |
| `prod` | Production environment |

### Dependencies
This service depends on:
- `common-utils` (i2o-framework)
- `db-utils` (i2o-db-utils)
- `i2o-sc-scraping-swagger-autogen`

### Environment Variables
| Variable | Description |
|----------|-------------|
| `SPRING_DATASOURCE_URL` | PostgreSQL connection string |
| `GCP_PROJECT_ID` | Google Cloud project ID |
| `SENDGRID_API_KEY` | SendGrid API key for email |
| SP-API credentials via GCP Secret Manager |

### API Documentation
Swagger UI available at: `http://localhost:8080/swagger-ui.html`
