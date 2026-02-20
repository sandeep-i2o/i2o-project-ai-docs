GitHub URL: git@github.com:i2o-retail/i2o-db-utils.git

# i2o Database Utilities (db-utils)

## Description

A shared Java library providing common database utilities, entity definitions, and data access components for the i2o platform. This module serves as the foundation layer for data operations across multiple i2o microservices, offering pre-built JPA entities, repositories, BigQuery integrations, and utility classes for consistent data handling.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Java 17 |
| **Framework** | Spring Boot 3.1.7 |
| **Build Tool** | Maven |
| **ORM** | Spring Data JPA, Hibernate 6.2 |
| **Database** | PostgreSQL |
| **Cloud Platform** | Google Cloud Platform |
| **Data Warehouse** | Google BigQuery |
| **Object Storage** | Google Cloud Storage |
| **Code Quality** | JaCoCo (Code Coverage), SonarQube |

## Key Components

| Component | Package | Description |
|-----------|---------|-------------|
| **ALEBCM Module** | `alebcm` | Alerts, Exceptions, and Business Critical Metrics handling |
| **BigQuery Integration** | `bigquery`, `bq` | BigQuery data access and query utilities |
| **Business Review** | `businessreview` | Business review reporting entities |
| **Configuration** | `configuration` | Shared configuration properties |
| **Report Framework** | `reportfwk` | Reporting framework entities and repositories |
| **Reseller Module** | `reseller` | Reseller data management |
| **Scheduler** | `scheduler` | Scheduled job utilities |
| **Utilities** | `utility` | Common utility classes |
| **Excel Processing** | `excel` | Excel file handling with Apache POI |
| **Forecasting** | `forecasting` | Forecasting data entities |

## Project Structure

```
i2o-db-utils/
├── pom.xml                     # Maven build configuration
├── src/
│   └── main/
│       └── java/
│           └── com/corecompete/i2o/
│               ├── albcm/              # BCM utilities
│               ├── alebcm/             # Alerts & Exceptions BCM
│               ├── bigquery/           # BigQuery integration
│               ├── bq/                 # BQ query utilities
│               ├── businessreview/     # Business review entities
│               ├── configuration/      # Shared configurations
│               ├── constants/          # Application constants
│               ├── dao/                # Data Access Objects
│               ├── dto/                # Data Transfer Objects
│               ├── excel/              # Excel processing
│               ├── exception/          # Custom exceptions
│               ├── forecasting/        # Forecasting entities
│               ├── lookup/             # Lookup tables
│               ├── pg/                 # PostgreSQL utilities
│               ├── reportfwk/          # Report framework
│               ├── reseller/           # Reseller module
│               ├── resellermastermgmt/ # Reseller master data
│               ├── response/           # Response DTOs
│               ├── scheduler/          # Scheduler utilities
│               └── utility/            # Common utilities
└── target/                     # Build output
```

## Key Features

| Feature | Description |
|---------|-------------|
| **JPA Entities** | Pre-defined entity classes for common data models |
| **Repository Interfaces** | Spring Data JPA repositories for data access |
| **BigQuery Utilities** | Helpers for BigQuery read/write operations |
| **PostgreSQL Socket Factory** | Cloud SQL connection management |
| **Excel Streaming** | Memory-efficient Excel file processing |
| **Password Hashing** | BCrypt-based password utilities |

## Scope of the Project

- Provide shared database entities and repositories
- Standardize data access patterns across i2o microservices
- Offer BigQuery integration utilities
- Implement common data transformation utilities
- Enable Excel file import/export capabilities
- Manage PostgreSQL connections via Cloud SQL

## Target Use Cases

1. **Microservice Development**: Foundation library for new i2o backend services
2. **Report Generation**: Common report framework entities and utilities
3. **Data Migration**: Utilities for data movement between PostgreSQL and BigQuery
4. **Batch Processing**: Support for batch data operations

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
    <artifactId>db-utils</artifactId>
    <version>0.0.1-SNAPSHOT</version>
</dependency>
```

### Required Environment Variables
- `SPRING_DATASOURCE_URL` - PostgreSQL connection string
- `GCP_PROJECT_ID` - Google Cloud project identifier
- Cloud SQL socket factory configurations

### Cloud SQL Connection
Uses `postgres-socket-factory` for secure Cloud SQL connectivity without IP whitelisting.
