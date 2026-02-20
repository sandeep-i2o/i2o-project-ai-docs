GitHub URL: git@github.com:i2o-retail/i2o-formatted-reports.git

# i2o-formatted-reports - Project Summary

## Description

The **i2o-formatted-reports** project is a **Framework for Generating Formatted Reports** for the i2o retail platform. It provides a comprehensive reporting engine that generates professional reports in multiple formats (PDF, Excel, PowerPoint, HTML) using JasperReports and Aspose Slides. The service supports business review reports, content analytics, and scheduled report generation with Google Cloud Storage integration.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 3.1.7 |
| **Language** | Java 17, Kotlin 1.6.21 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA |
| **Report Engine** | JasperReports 6.17.0 |
| **Presentation** | Aspose Slides 21.10 |
| **Excel Processing** | Apache POI 5.0.0 |
| **Template Engine** | Freemarker |
| **Cloud Services** | Google Cloud (BigQuery, Cloud Storage, Secret Manager) |
| **HTTP Client** | Retrofit 2.9.0, OkHttp |
| **Distributed Tracing** | Micrometer Tracing (Brave) |
| **Code Quality** | Checkstyle 9.0, PMD, JaCoCo |
| **Testing** | JUnit 5, JUnit Vintage |
| **Utilities** | Lombok, Guava 32.1.2 |

---

## Key Components

### Controllers
- **ReportController** - Main report generation endpoints
- **BusinessReviewReportController** - Weekly/monthly business review reports
- **BpBusinessReviewReportController** - Scheduled BP WBR Excel job
- **HealthCheckController** - Application health monitoring

### Services
- **ReportService** - Core report generation interface
- **DetailedReportService** - Detailed report processing
- **BusinessReviewReportService** - Business review report generation
- **BpBusinessReviewReportService** - BP WBR scheduled report service
- **GcsService** - Google Cloud Storage operations
- **PPCReportService** - PPC (Pay-Per-Click) report handling
- **AsposePptService** - PowerPoint generation using Aspose

### Framework Components
- Report template compilation and caching
- Multi-format export (PDF, Excel, PPT, HTML)
- Dynamic data binding and parameterization
- Large file compression (ZIP) support

---

## Project Structure

```
i2o-formatted-reports/
├── src/
│   ├── main/
│   │   ├── java/com/i2oretail/
│   │   │   ├── constants/          # Application constants
│   │   │   ├── controller/         # Base controller
│   │   │   ├── exception/          # Custom exceptions
│   │   │   ├── reporting/
│   │   │   │   ├── business/       # Business review reports (50 files)
│   │   │   │   │   └── review/
│   │   │   │   │       ├── aspose/      # Aspose PPT service
│   │   │   │   │       ├── controller/  # BR controllers
│   │   │   │   │       ├── dto/         # Request/Response DTOs
│   │   │   │   │       ├── model/       # Report models
│   │   │   │   │       └── service/     # BR services
│   │   │   │   ├── config/         # Configuration classes
│   │   │   │   ├── configuration/  # Additional configs
│   │   │   │   ├── controller/     # Report controllers
│   │   │   │   ├── dto/            # Data transfer objects (24 files)
│   │   │   │   ├── framework/      # Report framework (114 files)
│   │   │   │   ├── service/        # Report services
│   │   │   │   └── utils/          # Utility classes
│   │   │   └── utility/            # Common utilities
│   │   └── resources/
│   │       ├── application-{env}.properties
│   │       └── *.png, *.json       # Report assets
│   └── test/                       # Unit tests (32 files)
├── Dockerfile                      # Docker configuration
├── checkstyle.xml                  # Code style rules
└── pom.xml                         # Maven dependencies
```

---

## Key API Endpoints

### Report Generation (`/report`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/report/health` | GET | Health check endpoint |
| `/report/{reportName}` | POST | Generate report by name (PDF/Excel/HTML) |
| `/report/consolidated-email-body` | POST | Generate consolidated email content |
| `/report/intimation-email-body` | POST | Generate intimation email content |
| `/report/content-view/{reportName}` | POST | Generate content view report |
| `/report/content-grid/{gridName}` | POST | Get content grid data |
| `/report/content-grid-alert` | POST | Get content change grid alert data |
| `/report/scheduled-report` | POST | Trigger scheduled PPC report |

### Business Review Reports (`/generate`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate/report/{reportName}` | POST | Generate business review report (PDF/Excel/PPT) |

### Scheduled Jobs (`/invoke`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/invoke/BP_WBR_EXCEL_JOB` | POST | Trigger BP Weekly Business Review Excel job |

---

## Scope of the Project

The i2o-formatted-reports service covers:

1. **Multi-Format Report Generation** - PDF, Excel, PowerPoint, HTML exports
2. **Business Review Reports** - Weekly/monthly performance summaries
3. **Content Analytics Reports** - Content change tracking and alerts
4. **Email Report Generation** - Consolidated and intimation email bodies
5. **Scheduled Report Jobs** - Automated report generation with GCS upload
6. **Large File Handling** - Automatic compression for files > 10MB
7. **Template Management** - JasperReports template compilation and caching
8. **Cloud Integration** - GCS storage for generated reports

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Business Performance Reports** | Generate weekly/monthly business review presentations and spreadsheets |
| **Content Monitoring Reports** | Track content changes and generate alerts |
| **Scheduled Report Distribution** | Automated report generation on schedule with cloud storage |
| **Email Report Content** | Generate formatted email bodies for report distribution |
| **PPC Analytics** | Generate pay-per-click performance reports |
| **Custom Report Export** | Export data in multiple formats (PDF, Excel, PPT, HTML) |
| **Large Report Handling** | Automatic compression and streaming for large reports |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment configurations:
- `local`, `dev`, `qa` - Development/testing environments
- `uat`, `preuat`, `demouat` - UAT environments
- `preprod` - Pre-production staging
- `prod` - Production environment
- `demo` - Demo environment

### Packaging
- Packaged as **WAR** file for deployment on Tomcat/external container
- Docker support via **Dockerfile**

### Docker Configuration
```dockerfile
# Build stage uses OpenJDK 17
# Runtime uses Tomcat 10
# Application deployed as ROOT.war
```

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) with socket factory
- **Google Cloud Storage** for report file storage
- **Google BigQuery** for data queries
- **Google Secret Manager** for credential management

### Build Commands
```bash
# Build with checkstyle and PMD
./mvnw clean package

# Run locally
./mvnw spring-boot:run -Dspring.profiles.active=local

# Run tests with coverage
./mvnw test jacoco:report

# Checkstyle only
./mvnw checkstyle:checkstyle
```

### Report Generation Considerations
- JasperReports templates (.jrxml) are compiled at startup
- Large reports (>10MB) can be auto-zipped with `zipLargeFile=true` parameter
- Aspose Slides requires valid license for production use
- Temporary files are cleaned up after report generation

### Resource Files
- Report templates and assets in `resources/`
- Logo images: `i2o_logo.png`, `amazon.png`, etc.
- Configuration: `jasperreports.properties`, `jasperreports_extension.properties`
