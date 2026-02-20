GitHub URL: git@github.com:i2o-retail/i2o-framework.git

# i2o Framework (common-utils)

## Description

A core Java library providing common utilities, services, and configurations for the i2o platform. This framework serves as the central utility layer that other i2o microservices depend on, offering authentication, email services, BigQuery operations, rate limiting, and various shared functionalities. It builds upon `db-utils` and extends it with higher-level service abstractions.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Java 17 |
| **Framework** | Spring Boot 3.1.7 |
| **Build Tool** | Maven |
| **ORM** | Spring Data JPA, Hibernate |
| **Database** | PostgreSQL |
| **Cloud Platform** | Google Cloud Platform |
| **Data Warehouse** | Google BigQuery |
| **Authentication** | Keycloak 22.0.5, Microsoft MSAL |
| **Email Service** | SendGrid |
| **Metrics** | Micrometer, Prometheus |
| **Rate Limiting** | Bucket4j |
| **HTTP Client** | WebFlux, Unirest |

## Key Components

| Component | Package | Description |
|-----------|---------|-------------|
| **BigQuery Service** | `bigquery` | BigQuery data operations and query execution |
| **Common Reports** | `commonreport` | Shared report generation utilities |
| **Configuration** | `config` | Application and service configurations |
| **Excel Processing** | `excel` | Advanced Excel file handling |
| **Graph API** | `graphapi` | Microsoft Graph API integration |
| **GCS Service** | `gcsservice` | Google Cloud Storage operations |
| **Product Discovery** | `productdiscovery` | Product discovery services |
| **Report Framework** | `reportfwk` | Report generation framework |
| **Services** | `service` | Core business services |
| **Upload Commons** | `uploadCommons` | File upload handling utilities |
| **Utilities** | `util`, `utility` | Helper classes and utilities |
| **Secret Manager** | `GoogleSecretManager` | GCP Secret Manager integration |

## Project Structure

```
i2o-framework/
├── pom.xml                     # Maven build configuration
├── Dockerfile                  # Container configuration
├── src/
│   └── main/
│       └── java/
│           └── com/corecompete/i2o/
│               ├── DemoApplication.java      # Application entry point
│               ├── GoogleSecretManager.java  # Secret management
│               ├── RestTemplateConfig.java   # REST client config
│               ├── SendGridConfig.java       # Email configuration
│               ├── bigquery/                 # BigQuery services
│               ├── commonreport/             # Report utilities
│               ├── config/                   # Configurations
│               ├── constants/                # Application constants
│               ├── dao/                      # Data Access Objects
│               ├── dto/                      # Data Transfer Objects
│               ├── excel/                    # Excel processing
│               ├── exception/                # Custom exceptions
│               ├── gcsservice/               # GCS integration
│               ├── graphapi/                 # MS Graph API
│               ├── helper/                   # Helper classes
│               ├── models/                   # Domain models
│               ├── organizationtypes/        # Org type utilities
│               ├── orgutil/                  # Organization utilities
│               ├── productdiscovery/         # Product discovery
│               ├── reportfwk/                # Report framework
│               ├── rest/                     # REST utilities
│               ├── service/                  # Business services
│               ├── uploadCommons/            # Upload handling
│               └── util/                     # Common utilities
└── target/                     # Build output
```

## Key Features

| Feature | Description |
|---------|-------------|
| **Keycloak Integration** | OAuth2/OIDC authentication and authorization |
| **SendGrid Email** | Email sending capabilities |
| **Microsoft Graph API** | Office 365 and Azure AD integration |
| **Rate Limiting** | API rate limiting with Bucket4j |
| **Secret Management** | GCP Secret Manager for secure configuration |
| **Prometheus Metrics** | Application metrics and monitoring |
| **Distributed Tracing** | Micrometer tracing with Brave |

## Scope of the Project

- Provide common service abstractions for i2o microservices
- Centralize authentication and authorization logic
- Offer email and notification services
- Enable BigQuery operations with standard patterns
- Manage GCP resource access (Storage, Secrets)
- Implement rate limiting for API protection

## Target Use Cases

1. **Authentication**: Centralized Keycloak authentication for all services
2. **Email Notifications**: SendGrid-based email services
3. **Data Analytics**: BigQuery data access and reporting
4. **File Processing**: Excel generation and GCS storage
5. **Monitoring**: Prometheus metrics collection

## Deployment Notes

### Build
```bash
mvn clean install
```

### Usage as Dependency
Add to your service's `pom.xml`:
```xml
<dependency>
    <groupId>com.corecompete.i2o</groupId>
    <artifactId>common-utils</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
```

### Docker Build
```bash
docker build -t i2o-framework .
```

### Required Environment Variables
| Variable | Description |
|----------|-------------|
| `SPRING_DATASOURCE_URL` | PostgreSQL connection string |
| `GCP_PROJECT_ID` | Google Cloud project ID |
| `SENDGRID_API_KEY` | SendGrid API key for email |
| `KEYCLOAK_AUTH_SERVER_URL` | Keycloak server URL |
| `MS_GRAPH_CLIENT_ID` | Microsoft Graph API client ID |
| `MS_GRAPH_CLIENT_SECRET` | Microsoft Graph API secret |

### Dependencies
This library depends on `db-utils`:
```xml
<dependency>
    <groupId>com.corecompete.i2o</groupId>
    <artifactId>db-utils</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
```
