GitHub URL: git@github.com:i2o-retail/i2o-cloud-scheduler.git

# i2o-cloud-scheduler - Project Summary

## Description

The **i2o-cloud-scheduler** is a **cloud-native event-driven scheduler service** for the i2o retail platform. It handles asynchronous job processing via Google Cloud Pub/Sub, generating and distributing business review reports, promo day analytics, buy box reports, and content change notifications. The service operates as an event-driven worker that consumes messages from Pub/Sub topics and orchestrates report generation and email delivery.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 3.1.7 |
| **Language** | Java 17 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Hibernate, Hypersistence Utils |
| **Cloud Services** | Google Cloud (Pub/Sub, BigQuery, Cloud SQL) |
| **Messaging** | Google Cloud Pub/Sub (spring-cloud-gcp-starter-pubsub 4.11.0) |
| **Email Service** | SendGrid |
| **Template Engine** | Freemarker |
| **CSV Processing** | Apache Commons CSV |
| **Monitoring** | Spring Boot Actuator, Micrometer Tracing |
| **Testing** | JUnit, JaCoCo |
| **Utilities** | Lombok, Apache Commons IO |
| **Containerization** | Docker (multi-stage build) |

---

## Key Components

### Modules (3 main modules)

#### 1. Cloud Scheduler Module (`cloudscheduler/`)
- **PubSubCloudSchedulerMessageHandlerService** - Consumes Pub/Sub messages
- **CloudSchedulerReportService** - Report generation orchestration
- **BuyBoxReportHtmlService** - Buy box report HTML generation
- **ContentChangeReportService** - Content change notifications
- **CloudSchEmailService** - Email delivery
- **DataLoadService** - Data loading utilities
- **ReportMappingService** - Report configuration mapping

#### 2. Business Review Module (`businessreview/`)
- **PubSubMessageHandlerService** - Business review message handling
- **BusinessReviewReportService** - Business review report generation
- **BusinessReviewReportDataService** - Data queries and validation
- **BusinessReviewEmailService** - Business review email delivery
- **ValidateController** - Data validation endpoint

#### 3. Promo Day Module (`promoday/`)
- **PubSubPromoMessageHandlerService** - Promo day message handling
- **PromoDayReportService** - Promo day report generation
- **PromoReportDataService** - Promo analytics data
- **PromoDayEmailService** - Promo notification emails

### Controllers (1 total)
- **ValidateController** - Data validation endpoint for business review

### Services (21 total)
- Report generation, email delivery, Pub/Sub message handling, data loading

---

## Project Structure

```
i2o-cloud-scheduler/
├── src/
│   └── main/
│       └── java/com/corecompete/i2o/
│           ├── I2oCloudSchedulerApplication.java
│           ├── SendGridConfig.java
│           ├── cloudscheduler/      # Cloud scheduler module
│           │   ├── dao/             # Data access (1 file)
│           │   ├── dto/             # DTOs (13 files)
│           │   ├── exception/       # Exceptions (1 file)
│           │   ├── model/           # Domain models (2 files)
│           │   ├── pubsub/          # Pub/Sub handlers (3 files)
│           │   ├── service/         # Services (10 files)
│           │   └── util/            # Utilities (3 files)
│           ├── businessreview/      # Business review module
│           │   ├── constants/       # Constants
│           │   ├── controller/      # REST controller (1 file)
│           │   ├── dao/             # Data access (3 files)
│           │   ├── dto/             # DTOs (14 files)
│           │   ├── exception/       # Exceptions
│           │   ├── models/          # Domain models (9 files)
│           │   ├── pubsub/          # Pub/Sub handlers (3 files)
│           │   ├── service/         # Services (4 files)
│           │   └── util/            # Utilities (5 files)
│           └── promoday/            # Promo day module
│               ├── constants/       # Constants
│               ├── dao/             # Data access (3 files)
│               ├── dto/             # DTOs (3 files)
│               ├── exception/       # Exceptions
│               ├── model/           # Domain models (6 files)
│               ├── pubsub/          # Pub/Sub handlers (3 files)
│               ├── service/         # Services (4 files)
│               └── util/            # Utilities (3 files)
├── Dockerfile
├── docker-compose.yml
└── pom.xml
```

---

## Key API Endpoints

### Data Validation (`/validate`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/validate/run-data-validations` | POST | Run data validation checks for business review reports |

### Pub/Sub Message Handlers (Event-Driven)
The service primarily operates as a Pub/Sub consumer rather than exposing REST APIs. It handles:

| Message Topic | Handler | Description |
|---------------|---------|-------------|
| Cloud Scheduler Topic | PubSubCloudSchedulerMessageHandlerService | General scheduled job processing |
| Business Review Topic | PubSubMessageHandlerService | Business review report generation |
| Promo Day Topic | PubSubPromoMessageHandlerService | Promo day report generation |

---

## Scope of the Project

The i2o-cloud-scheduler service covers:

1. **Event-Driven Processing** - Consume Pub/Sub messages for scheduled jobs
2. **Business Review Reports** - Generate weekly/monthly business review reports
3. **Promo Day Analytics** - Generate promo day performance reports
4. **Buy Box Reports** - HTML buy box report generation
5. **Content Change Detection** - Monitor and report content changes
6. **Email Delivery** - Send reports via SendGrid
7. **Data Validation** - Validate data before report generation
8. **BigQuery Integration** - Query analytics data from BigQuery
9. **Multi-Tenant Support** - Process reports for multiple organizations
10. **Template-Based Reports** - Freemarker-based report templates

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Weekly Business Reviews** | Automated generation of WBR reports |
| **Monthly Business Reviews** | Automated generation of MBR reports |
| **Promo Performance** | Track and report promo day performance |
| **Buy Box Monitoring** | Generate buy box status reports |
| **Content Change Alerts** | Notify stakeholders of content changes |
| **Scheduled Email Reports** | Automated email distribution of reports |
| **Data Quality Validation** | Validate data before report generation |
| **Event-Driven Processing** | Process triggers from Cloud Scheduler |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment profiles (defined in pom.xml):
- `local` (default) - Local development
- `dev` - Development environment
- `qa` - QA testing
- `uat` - User acceptance testing
- `preprod` - Pre-production staging
- `prod` - Production environment

### Docker Deployment
Multi-stage Docker build included:

```dockerfile
# Build stage
FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
RUN mvn clean package -DskipTests

# Runtime stage
FROM openjdk:17
COPY --from=build /app/target/cloud-scheduler-0.0.1-SNAPSHOT.jar /app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

### Docker Compose
```bash
docker-compose up
```

### Cloud Dependencies
- **Google Cloud Pub/Sub** - Message consumption for job triggers
- **Google BigQuery** - Analytics data queries
- **Google Cloud SQL** (PostgreSQL) - Persistent storage
- **SendGrid** - Email delivery service

### Build Commands
```bash
# Build
./mvnw clean package

# Build with specific profile
./mvnw clean package -Pdev

# Run locally
./mvnw spring-boot:run -Plocal

# Run tests with coverage
./mvnw test jacoco:report

# Docker build
docker build -t i2o-cloud-scheduler .
```

### Key Configuration Properties
- Pub/Sub subscription configurations
- BigQuery project and dataset settings
- SendGrid API key
- Cloud SQL connection settings
- Email template configurations

### Monitoring
- Spring Boot Actuator endpoints for health checks
- Micrometer tracing for distributed tracing
- JaCoCo for test coverage reporting
