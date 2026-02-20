GitHub URL: git@github.com:i2o-retail/i2o-upload-framework.git

# i2o-upload-framework - Project Summary

## Description

The **i2o-upload-framework** is a **file upload processing service** for the i2o retail platform. It provides a comprehensive framework for handling file uploads (primarily Excel files), performing multi-level validations, tracking upload history, and integrating with asynchronous processing pipelines. The service supports various upload types, organization-specific configurations, and provides notification capabilities for upload status updates.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 3.1.7 |
| **Language** | Java 17 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Hibernate, Hypersistence Utils |
| **API Documentation** | SpringDoc OpenAPI (Swagger UI) |
| **Cloud Services** | Google Cloud (Storage, Pub/Sub) |
| **Messaging** | Google Cloud Pub/Sub |
| **Excel Processing** | Apache POI 4.1.2 |
| **Object Mapping** | MapStruct 1.4.2 |
| **Validation** | JSON Schema (Everit) |
| **Testing** | JUnit 4/5, Testcontainers, JaCoCo |
| **Utilities** | Lombok, Guava 31.1 |
| **Tracing** | Micrometer Tracing (Brave) |

---

## Key Components

### Controllers (3 total)
- **UploadMasterController** - Core file upload handling and type management
- **UploadHistoryController** - Upload history tracking and file downloads
- **UploadMapController** - Specialized Excel map/mapping uploads

### Services (24 total)
- **UploadMasterService** - Upload type configuration and processing initiation
- **UploadHistoryService** - History tracking and status management
- **UploadMapService** - Excel mapping file processing
- **UploadProcessorService** - Core upload processing logic
- **UploadDumpService** - Failed/rejected record management
- **StorageService** - GCS file storage operations
- **PubSubService** - Asynchronous message publishing
- **L1ExcelValidationService** - Level 1 Excel validation (structure/format)
- **L2ExcelValidationService** - Level 2 Excel validation (business rules)
- **NotificationService** - Email/notification delivery
- **CommonService** - Shared utility functions

### Entities
- **UploadMasterEntity** - Upload type configurations
- **UploadTypeEntity** - Supported upload types per organization
- **UploadHistoryEntity** - Upload job tracking
- **UploadDumpEntity** - Failed/rejected records storage
- **SamsungAuditHistoryEntity** - Samsung-specific audit tracking

### Repositories (5 total)
- **UploadMasterRepository** - Upload configuration queries
- **UploadHistoryRepository** - History CRUD operations
- **UploadTypeRepository** - Upload type queries
- **SamsungAuditHistoryRepository** - Samsung audit operations

---

## Project Structure

```
i2o-upload-framework/
├── src/
│   ├── main/
│   │   ├── java/com/i2oretail/uploadframework/
│   │   │   ├── aspect/              # AOP aspects (2 files)
│   │   │   ├── configuration/       # App configurations (2 files)
│   │   │   ├── constants/           # Constants and enums
│   │   │   ├── controllers/         # REST controllers (3 files)
│   │   │   ├── dao/                 # Data access objects (6 files)
│   │   │   ├── dto/                 # Data transfer objects (7 files)
│   │   │   ├── exception/           # Custom exceptions (6 files)
│   │   │   ├── mapper/              # MapStruct mappers (4 files)
│   │   │   ├── pg/                  # PostgreSQL entities
│   │   │   │   ├── entity/          # JPA entities
│   │   │   │   └── enumerator/      # Enum types
│   │   │   ├── repository/          # JPA repositories (5 files)
│   │   │   ├── response/            # Response models (3 files)
│   │   │   ├── runnable/            # Async runnable tasks
│   │   │   ├── service/             # Business logic (25 files)
│   │   │   │   └── validations/     # Validation services
│   │   │   └── util/                # Utility classes (4 files)
│   │   └── resources/
│   │       ├── application-{env}.properties
│   │       ├── schema.json          # JSON schema for validation
│   │       └── logback-spring.xml   # Logging configuration
│   └── test/                        # Unit tests (16 files)
└── pom.xml
```

---

## Key API Endpoints

### Upload Master (`/upload`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/upload/master` | GET | Get all possible upload types for organization |
| `/upload/types` | GET | Get supported upload types for specific org and user |
| `/upload/file/{orgId}` | POST | Upload a new file for processing |
| `/upload/columnDefinition` | GET | Get column definition for upload type |
| `/uploadDump` | GET | Get paginated upload dump entries |

### Upload History (`/upload/history`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/upload/history/{orgId}` | GET | Get paginated upload history for organization |
| `/upload/history/downloadUrl` | GET | Get temporary download URL for uploaded/rejected files |
| `/upload/history/gcsLink` | GET | Get GCS download link for files |
| `/upload/history/updateStatus` | PATCH | Update upload status and send notifications |
| `/upload/history/errors` | POST | Get upload history with validation error details |

### Upload Map (`/api/excel`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/excel/upload` | POST | Upload and process Excel mapping files |

---

## Scope of the Project

The i2o-upload-framework service covers:

1. **File Upload Processing** - Handle multipart file uploads with size limits
2. **Multi-Level Validation**
   - **L1 Validation** - Structure, format, column headers, sheet names
   - **L2 Validation** - Business rules, data types, required fields
3. **Upload Type Management** - Organization-specific upload configurations
4. **History Tracking** - Complete audit trail of all upload operations
5. **Error Handling** - Capture and store validation failures
6. **File Storage** - GCS integration for upload and error files
7. **Notifications** - Email notifications for upload status
8. **Async Processing** - Pub/Sub integration for background processing
9. **Download URLs** - Signed URL generation for file downloads
10. **Platform/Region Support** - Multi-platform upload handling

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Bulk Product Import** | Upload product master data via Excel files |
| **Reseller Data Upload** | Import reseller information and metadata |
| **Brand/Category Import** | Bulk upload brand and category hierarchies |
| **Pricing Updates** | Upload pricing data for products |
| **MAP Upload** | Upload MAP (Minimum Advertised Price) data |
| **Content Updates** | Upload product content and descriptions |
| **Audit History** | Track and review all upload activities |
| **Error Resolution** | Download rejected files with error details |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment configurations:
- `local` - Local development
- `dev`, `qa` - Development/testing environments
- `uat`, `preuat`, `demouat` - UAT environments
- `preprod` - Pre-production staging
- `prod` - Production environment
- `demo` - Demo environment

### Packaging
- Packaged as **WAR** file (`uploadframework.war`) for deployment on Tomcat
- Includes App Engine Maven plugin for GCP deployment

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) for database storage
- **Google Cloud Storage** for file uploads and error files
- **Google Cloud Pub/Sub** for asynchronous processing

### Build Commands
```bash
# Build
./mvnw clean package

# Run locally
./mvnw spring-boot:run -Dspring.profiles.active=local

# Run tests with coverage
./mvnw test jacoco:report
```

### Key Configuration Properties
- Database connection via Cloud SQL socket factory
- Pub/Sub topic/subscription configurations
- GCS bucket for upload storage
- File size limits configuration
- Notification email settings

### API Documentation
- Swagger UI available at `/swagger-ui.html`
- OpenAPI spec at `/v3/api-docs`

### Upload Processing Flow
1. File received at upload endpoint
2. L1 validation (structure, headers)
3. File stored in GCS
4. Pub/Sub message published for async processing
5. L2 validation (business rules)
6. Results stored in database
7. Notification emails sent
8. Error file generated if validation fails
