GitHub URL: git@github.com:i2o-retail/i2o-master-data.git

# i2o-master-data - Project Summary

## Description

The **i2o-master-data** project is a **Master Data Management (MDM)** service for the i2o retail platform. It provides centralized management of product catalogs, brand hierarchies, category mappings, reseller metadata, and scraping input configurations. The service handles data validation, auditing, synchronization across marketplaces, and scheduled data processing jobs for web scraping pipelines.

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
| **Cloud Services** | Google Cloud (BigQuery, Cloud Storage, Pub/Sub) |
| **Messaging** | Google Cloud Pub/Sub |
| **HTTP Client** | Retrofit 2.9.0, OkHttp |
| **Email Service** | SendGrid |
| **Object Mapping** | MapStruct 1.4.2, ModelMapper |
| **Validation** | Spring Validation, JSON Schema (Everit) |
| **Template Engine** | Freemarker |
| **Data Processing** | Apache Commons CSV, Commons Compress |
| **Testing** | JUnit 4/5, Testcontainers, JaCoCo |
| **Utilities** | Lombok, Guava 31.1 |

---

## Key Components

### Controllers (15 total)
- **ProductMasterListController** - Product catalog CRUD operations
- **BrandMasterController** - Brand management and hierarchies
- **CategoryMasterController** - Category mappings
- **ResellerMetadataController** - Reseller information management
- **SchedulerController** - Scheduled job triggers
- **ProductCatalogController** - Product catalog operations
- **DataFetchFromDBController** - Database data extraction
- **MigrationController** - Data migration endpoints
- **OrgDataController** - Organization data management
- **MultiplatformController** - Multiplatform operations

### Services (62 total)
- Core business logic for product, brand, category, and reseller management
- Scheduler services for automated data processing
- PubSub integration for asynchronous messaging
- Scraping input generation services
- GCS service for cloud storage operations
- Validation and audit services

### Entities (30 total)
- Product Master, Brand Master, Category Master
- Reseller Master, Reseller Metadata
- Product Catalog, Product Channel Master
- Organization, Marketplace, Scraping Config

### Repositories (30 total)
- JPA repositories with custom queries
- Native SQL support for complex operations

---

## Project Structure

```
i2o-master-data/
├── src/
│   ├── main/
│   │   ├── java/com/i2oretail/masterdata/
│   │   │   ├── aspect/              # AOP aspects (2 files)
│   │   │   ├── configuration/       # App configurations (2 files)
│   │   │   ├── constant/            # Constants (8 files)
│   │   │   ├── controllers/         # REST controllers (15 files)
│   │   │   ├── dto/                 # Data transfer objects (47 files)
│   │   │   ├── entities/            # JPA entities (30 files)
│   │   │   ├── enums/               # Enumerations (6 files)
│   │   │   ├── exception/           # Custom exceptions (9 files)
│   │   │   ├── mappers/             # MapStruct mappers (2 files)
│   │   │   ├── reporting/           # Reporting utilities
│   │   │   ├── repository/          # JPA repositories (30 files)
│   │   │   ├── retrofit/            # HTTP client configs (3 files)
│   │   │   ├── serdeserializers/    # JSON serializers (7 files)
│   │   │   ├── services/            # Business logic (133 files)
│   │   │   │   ├── impl/            # Service implementations
│   │   │   │   ├── migration/       # Migration services
│   │   │   │   └── validation/      # Validation services
│   │   │   ├── utility/             # Utility classes
│   │   │   └── utils/               # Helper utilities
│   │   └── resources/
│   │       ├── application-{env}.properties
│   │       ├── jsons/               # JSON configs and templates
│   │       └── templates/           # Freemarker templates
│   └── test/                        # Unit tests (53 files)
└── pom.xml
```

---

## Key API Endpoints

### Product Master (`/mdm/products`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Get paginated product list for organization |
| `/saveProductMaster` | POST | Save product master changes |
| `/auditForProductMaster` | POST | Get product master audit logs |
| `/summaryForProductMaster` | POST | Get product master summary card data |

### Brand Master (`/mdm/brands`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/brandAlias/{id}` | PATCH | Update brand alias |
| `/parentBrand/{id}` | PATCH | Update parent brand relationship |
| `/saveBrandMaster` | POST | Save brand master changes |
| `/update-deleted-brands` | POST | Update products for deleted brands |

### Reseller Metadata (`/mdm/resellerMetadata`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/saveResellerMetadata` | POST | Save reseller metadata changes |

### Product Catalog (`/mdm/productCatalog`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET/POST | Product catalog CRUD operations |

### Scheduler Jobs (`/mdm/scheduler`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/run/{timeRange}` | GET | Trigger scheduled data processing |
| `/audit-email` | GET | Trigger audit email notification |
| `/product-scraping-input` | GET | Generate product scraping input files |
| `/product-attribute/{timeRange}` | GET | Trigger product attribute processing |
| `/product-attribute-update/{timeRange}` | GET | Trigger product attribute updates |
| `/product-channel/{timeRange}` | GET | Trigger product channel updates |
| `/product-catalog/{timeRange}` | GET | Trigger product catalog processing |
| `/product-catalog/email` | GET | Trigger product catalog email |
| `/cleanup-vendor-config` | GET | Clean up vendor scraping configs |

### Data Fetch (`/mdm/dataFetch`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | POST | Fetch data from database |

### Migration (`/mdm/migration`)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | POST | Execute data migration |

---

## Scope of the Project

The i2o-master-data service covers:

1. **Product Master Management** - CRUD operations, validation, and auditing
2. **Brand Hierarchy** - Brand aliases, parent brands, and relationships
3. **Category Mapping** - Platform-specific category configurations
4. **Reseller Metadata** - Reseller information and classification
5. **Scraping Input Generation** - Generate inputs for web scraping pipelines
6. **Marketplace Integration** - Multi-marketplace product synchronization
7. **Scheduled Jobs** - Automated data processing and notifications
8. **Data Migration** - Tools for migrating and synchronizing data
9. **Audit Logging** - Track changes to master data with email notifications
10. **PubSub Integration** - Asynchronous event-driven processing

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Product Catalog Management** | Maintain centralized product master data across marketplaces |
| **Brand Standardization** | Normalize brand names and hierarchies for analytics |
| **Scraping Pipeline Input** | Generate input files for automated web scraping |
| **Data Quality Audits** | Track and audit changes to master data |
| **Reseller Classification** | Manage and categorize reseller metadata |
| **Scheduled Data Sync** | Automated synchronization of product attributes |
| **Multi-Marketplace Support** | Handle product data across different sales channels |
| **API Integration** | Provide RESTful APIs for frontend and other services |

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
- Packaged as **WAR** file (`mdm.war`) for deployment on Tomcat
- Includes App Engine Maven plugin for GCP deployment

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) with socket factory
- **Google Cloud Storage** for file storage (scraping inputs, reports)
- **Google BigQuery** for analytics queries
- **Google Cloud Pub/Sub** for asynchronous messaging

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
- Pub/Sub topic/subscription configurations
- GCS bucket configurations for scraping inputs
- SendGrid API key for email notifications
- BQ project and dataset configurations

### API Documentation
- Swagger UI available at `/swagger-ui.html`
- OpenAPI spec at `/v3/api-docs`
