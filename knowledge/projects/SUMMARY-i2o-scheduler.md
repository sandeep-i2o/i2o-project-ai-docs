GitHub URL: https://github.com/i2o-retail/i2o-scheduler.git

# i2o-scheduler - Project Summary

## Description

The **i2o-scheduler** is a **task scheduling microservice** for the i2o retail platform. It provides infrastructure for managing periodic and event-driven tasks, including data scraping jobs, report generation, notification delivery, and data migration workflows. The service orchestrates scheduled jobs across multiple organizations with configurable distribution lists and supports both time-based and event-triggered execution.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 3.1.7 |
| **Language** | Java 17 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Hibernate, Hypersistence Utils |
| **API Documentation** | SpringDoc OpenAPI (Swagger UI) 2.2.0 |
| **Cloud Services** | Google Cloud (BigQuery, Cloud SQL) |
| **Email Service** | SendGrid |
| **HTTP Client** | Retrofit 2.9.0, OkHttp 4.9.0, Apache HttpClient5 |
| **Template Engine** | Freemarker |
| **CSV Processing** | SuperCSV |
| **Monitoring** | Spring Boot Actuator, Micrometer Tracing |
| **Testing** | JUnit, JaCoCo |
| **Utilities** | Lombok, Apache Commons Lang3 |
| **Security** | Bouncy Castle (cryptography) |

---

## Key Components

### Controllers (5 total)
- **SchedulerController** - Core schedule management and task execution
- **BuyBoxNotificationController** - Buy box alert notifications
- **DistributionListController** - Email distribution list management
- **EventWebhookController** - SendGrid event webhook handling
- **BaseController** - Common controller functionality

### Services (23 total)
- **SchedulerService** - Schedule configuration and management
- **SchedulerTaskService** - Task execution orchestration
- **BuyBoxNotificationService** - Buy box notification processing
- **BuyboxDeliveryReportsService** - Delivery report generation
- **DistributionListService** - Distribution list CRUD operations
- **EmailService** - Email composition and sending
- **ExcelDownloadClientService** - Report download handling
- **CsvService** - CSV file generation
- **SendgridEventService** - Email event tracking
- **ProductDiscoverySchedulerService** - Product discovery job scheduling

### Task Classes (11 total)
- **GenericSchedulerTask** - Configurable generic task executor
- **DataScrapingTask** - Web data scraping orchestration
- **SchedulerBuyboxReportTask** - Buy box report generation
- **SchedulerDeliveryReportTask** - Delivery status reporting
- **ProductDiscoverySchedulerTask** - Product discovery jobs
- **ResellerMetadataDailyMigrationTask** - Daily reseller data sync
- **SubscribedPlatformWeeklyMigrationTask** - Weekly platform data sync
- **UpdateResellerUrlTask** - Reseller URL updates
- **UpdateSalesRankTask** - Sales rank calculations
- **CleanupSchedulerTask** - Scheduled cleanup operations
- **RunnableTask** - Base runnable task interface

### Entities/Models (11 total)
- Schedule configurations, distribution lists, task execution records

### Repositories (6 total)
- JPA repositories for schedule and distribution list data

---

## Project Structure

```
i2o-scheduler/
├── src/
│   ├── main/
│   │   ├── java/com/corecompete/i2o/
│   │   │   ├── controller/          # Base controller
│   │   │   ├── scheduler/
│   │   │   │   ├── controller/      # REST controllers (4 files)
│   │   │   │   ├── dto/             # Data transfer objects (25 files)
│   │   │   │   ├── model/           # Domain models (11 files)
│   │   │   │   ├── repository/      # JPA repositories (6 files)
│   │   │   │   ├── service/         # Business logic (22 files)
│   │   │   │   ├── task/            # Scheduled tasks (11 files)
│   │   │   │   └── validators/      # Input validators
│   │   │   └── utility/             # Utility services
│   │   └── resources/
│   │       ├── application-{env}.properties
│   │       ├── logback-spring.xml   # Logging config
│   │       ├── i2o_logo.png         # Email assets
│   │       └── report.png
│   └── test/                        # Unit tests (18 files)
├── debugging/                       # Debugging guides
├── development/                     # Development templates
├── docs_generation/                 # Documentation scripts
├── Dockerfile
└── pom.xml
```

---

## Key API Endpoints

### Scheduler Management (`/scheduler`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/save` | POST | Save/update schedule configuration |
| `/execute` | POST | Execute a scheduled task immediately |

### Buy Box Notifications (`/buybox-notification`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/send-notification` | POST | Trigger buy box notification emails |

### Distribution List Management (`/distribution-list`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/all` | GET | Get all distribution lists |
| `/user/{user}` | GET | Get distribution lists by user |
| `/org-id/{id}` | GET | Get distribution lists by organization |
| `/list-type/{listType}` | GET | Get distribution lists by type |
| `/` | POST | Create a new distribution list |
| `/` | PUT | Update an existing distribution list |

### Event Webhooks (`/event`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sendgrid` | POST | Handle SendGrid email event callbacks |

---

## Scope of the Project

The i2o-scheduler service covers:

1. **Schedule Management** - Create, update, and delete scheduled jobs
2. **Task Execution** - Run periodic and on-demand tasks
3. **Data Scraping** - Orchestrate web scraping jobs for product data
4. **Report Generation** - Schedule buy box and delivery reports
5. **Email Notifications** - Send scheduled emails with distribution lists
6. **Distribution Lists** - Manage email recipient groups
7. **Data Migration** - Schedule reseller and platform data sync jobs
8. **Event Tracking** - Process SendGrid webhook events
9. **Product Discovery** - Schedule product discovery jobs
10. **Sales Rank Updates** - Calculate and update sales rankings

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Scheduled Reporting** | Automated generation and delivery of business reports |
| **Buy Box Alerts** | Notify stakeholders of buy box changes |
| **Data Scraping Orchestration** | Schedule and manage web scraping workflows |
| **Email Campaign Tracking** | Track email delivery and engagement events |
| **Distribution List Management** | Maintain recipient lists for notifications |
| **Data Synchronization** | Schedule periodic data migration and sync jobs |
| **Sales Analytics** | Calculate and update product sales rankings |
| **Platform Integration** | Sync data across marketplace platforms |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment configurations:
- `local` - Local development
- `dev`, `qa` - Development/testing environments
- `uat`, `preuat`, `demouat` - UAT environments
- `preprod` - Pre-production staging
- `prod` - Production environment
- `demo`, `custdemo` - Demo environments

### Packaging
- Packaged as **WAR** file for Tomcat deployment
- Docker support with included `Dockerfile`
- Includes App Engine Maven plugin for GCP deployment

### Docker Deployment
```dockerfile
FROM openjdk:17-jre-slim
COPY target/*.war app.war
ENTRYPOINT ["java", "-jar", "/app.war"]
```

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) for persistent storage
- **Google BigQuery** for analytics queries
- **SendGrid** for email delivery and event tracking

### Build Commands
```bash
# Build
./mvnw clean package

# Run locally
./mvnw spring-boot:run -Dspring.profiles.active=local

# Run tests with coverage
./mvnw test jacoco:report

# Deploy to App Engine
./mvnw appengine:deploy
```

### Key Configuration Properties
- Database connection via Cloud SQL socket factory
- SendGrid API configuration for email delivery
- BigQuery project and dataset settings
- Task scheduling cron expressions
- Retry policies via Spring Retry

### API Documentation
- Swagger UI available at `/swagger-ui/index.html`
- OpenAPI spec at `/v3/api-docs`

### Monitoring
- Spring Boot Actuator endpoints for health checks
- Micrometer tracing for distributed tracing
