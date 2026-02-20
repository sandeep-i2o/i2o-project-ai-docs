GitHub URL: git@github.com:i2o-retail/i2o-rules-engine.git

# i2o-rules-engine - Project Summary

## Description

The **i2o-rules-engine** is a **business rules engine microservice** for the i2o retail platform. Built on **Drools**, it provides intelligent rule-based evaluation for generating automated insights, weekly highlights, and business analytics. The service processes organizational data through configurable business rules to generate narrative highlights for revenue trends, category performance, brand analytics, and ASIN-level metrics.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 2.1.6.RELEASE |
| **Language** | Java 8 |
| **Build Tool** | Maven |
| **Rules Engine** | Drools 7.49.0.Final |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Spring JDBC |
| **Cloud Services** | Google Cloud (BigQuery) |
| **API Documentation** | Springfox Swagger 2.9.2 |
| **Excel Processing** | Apache POI 4.1.1 |
| **Object Mapping** | ModelMapper 2.3.5 |
| **Tracing** | Spring Cloud Sleuth |
| **Monitoring** | Spring Boot Actuator |
| **Code Quality** | Checkstyle, PMD, FindBugs, JaCoCo |
| **Utilities** | Lombok |

---

## Key Components

### Controllers (1 total)
- **HighlightController** - REST endpoint for triggering weekly highlight generation

### Services (1 total)
- **HighlightService** - Core service with 21+ methods for highlight data processing:
  - Revenue highlight generation
  - Category analytics processing
  - Brand performance analysis
  - ASIN-level metric calculations
  - Priority-based narrative generation

### Drools Components
- **KieContainer** - Drools knowledge container
- **KieSession** - Rule execution session (`rulesSession`)
- **Business Rules** - DRL files for highlight generation logic

### Domain Models
- **Highlight** - Core domain object for highlight data
- **HighlightResponse** - API response wrapper
- **HighlightDto** - Data transfer objects

### Integrations
- **WeeklyHighlightService** - BigQuery interaction for highlight storage
- **ChartService** - Chart data retrieval
- **ReportService** - Report data processing
- **OrganizationRepository** - Organization data access

---

## Project Structure

```
i2o-rules-engine/
├── src/
│   ├── main/
│   │   ├── java/com/corecompete/i2o/
│   │   │   ├── I2oRulesEngineApplication.java
│   │   │   ├── config/              # Configuration (1 file)
│   │   │   ├── constants/           # Constants (1 file)
│   │   │   ├── controller/          # REST controllers (1 file)
│   │   │   ├── domain/              # Domain models (2 files)
│   │   │   ├── dto/                 # DTOs (10 files)
│   │   │   └── service/             # Business services (1 file)
│   │   └── resources/
│   │       ├── application-{env}.properties
│   │       └── rules/               # Drools DRL files
│   └── test/                        # Unit tests
├── checkstyle.xml                   # Code style configuration
└── pom.xml
```

---

## Key API Endpoints

### Highlight Generation (`/populateHighlights`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/populateHighlights` | POST | Generate weekly highlights for an organization |

### Request Body (HighlightRequest)
```json
{
  "projectId": "string",
  "startDate": "yyyy-MM-dd",
  "endDate": "yyyy-MM-dd"
}
```

### Response (HighlightResponse)
```json
{
  "message": "Success"
}
```

### Processing Flow
1. Receives highlight request with date range
2. Fetches organization configuration
3. Deletes existing highlights for the period
4. Collects data for various metrics:
   - Ordered revenue
   - Shipped COGS
   - Category performance
   - Brand analytics
   - ASIN metrics
5. Executes Drools rules to generate narratives
6. Persists highlights to BigQuery

---

## Scope of the Project

The i2o-rules-engine service covers:

1. **Business Rules Execution** - Drools-based rule evaluation
2. **Weekly Highlights** - Automated insight generation
3. **Revenue Analytics** - Ordered revenue trend analysis
4. **Category Performance** - Category-level metric processing
5. **Brand Analytics** - Brand performance insights
6. **ASIN Metrics** - Product-level analytics
7. **Priority Narratives** - Rule-based text generation
8. **BigQuery Integration** - Data queries and storage
9. **Multi-Tenant Support** - Organization-specific processing
10. **Data Aggregation** - Cross-metric highlight consolidation

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Weekly Business Reviews** | Generate automated highlights for WBR meetings |
| **Revenue Trend Analysis** | Identify revenue changes and patterns |
| **Category Insights** | Surface category-level performance changes |
| **Brand Performance** | Track brand metrics and generate narratives |
| **Product Analytics** | ASIN-level insight generation |
| **Priority Flagging** | Identify high-priority items requiring attention |
| **Executive Summaries** | Automated narrative generation for reports |
| **Data-Driven Alerts** | Rule-based threshold notifications |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment configurations:
- `local` - Local development
- `dev` - Development environment
- `qa` - QA testing
- `uat`, `demouat` - UAT environments
- `preprod`, `prodstg` - Pre-production staging
- `prod` - Production environment
- `demo`, `custdemo` - Demo environments

### Packaging
- Packaged as **WAR** file (`rules-1.0.war`) for Tomcat deployment
- Includes App Engine Maven plugin for GCP deployment

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) for organization data
- **Google BigQuery** for analytics data and highlight storage

### Build Commands
```bash
# Build (with code quality checks)
./mvnw clean package

# Skip code quality checks
./mvnw clean package -Dcheckstyle.skip=true -Dpmd.skip=true -Dfindbugs.skip=true

# Run locally
./mvnw spring-boot:run

# Run tests with coverage
./mvnw test jacoco:report

# Code quality checks only
./mvnw checkstyle:check pmd:check findbugs:check
```

### Code Quality Configuration
- **Checkstyle** - Custom rules in `checkstyle.xml`
- **PMD** - Static code analysis
- **FindBugs** - Bug pattern detection
- **JaCoCo** - Test coverage reporting

### API Documentation
- Swagger UI available at `/swagger-ui.html`
- API docs at `/v2/api-docs`

### Key Configuration Properties
- BigQuery project and dataset settings
- Cloud SQL connection configuration
- Drools rule file locations
- Organization repository settings

### Drools Integration
The service uses Drools for:
- Rule-based highlight generation
- Threshold-based alerting
- Narrative template processing
- Priority classification
