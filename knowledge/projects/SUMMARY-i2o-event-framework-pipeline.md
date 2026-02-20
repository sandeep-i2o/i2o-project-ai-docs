GitHub URL: git@github.com:i2o-retail/i2o-event-framework-pipeline.git

# i2o-event-framework-pipeline - Project Summary

## Description

The **i2o-event-framework-pipeline** is an **Apache Beam data pipeline** for the i2o retail platform. It provides a configurable event processing framework that runs on **Google Cloud Dataflow**. The pipeline dynamically generates SQL queries based on event definitions, executes them against BigQuery, and writes results to specified destination tables. It's packaged as a **Dataflow Flex Template** for easy deployment and execution.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 2.1.6.RELEASE |
| **Language** | Java 8 |
| **Build Tool** | Maven |
| **Data Pipeline** | Apache Beam 2.39.0 |
| **Pipeline Runners** | DirectRunner, PortableRunner, DataflowRunner |
| **Database** | PostgreSQL (for event definitions) |
| **Cloud Services** | Google Cloud (BigQuery, Dataflow, Storage) |
| **Container** | Dataflow Flex Template (Java 11 base) |
| **Monitoring** | Spring Boot Actuator |
| **Networking** | Netty, gRPC |
| **Utilities** | Lombok, Commons IO, Commons Codec |

---

## Key Components

### Pipeline Core (3 files)
- **EventGenerator** - Main entry point for pipeline execution
- **EventPipeline** - Core pipeline definition and transforms
- **EventOptions** - Pipeline configuration options

### Services (4 files)
- **BigQueryServices** - BigQuery table operations
- **EventDefinitionService** - Event configuration retrieval
- **EventSchemaService** - Schema management for output tables
- **QueryBuilderService** - Dynamic SQL query generation

### Models (15 files)
- **EventDefinition** - Event configuration model
- **Events** - Event instance data
- **Monitor** - Monitoring configuration
- **MonitorFields** - Monitor field definitions
- **BeamQuery** - Beam SQL query model
- **QueryColumn** - Column definitions for queries
- **QueryJoins** - Join configurations
- **QueryWindow** - Windowing configurations
- **Source** / **TableSource** - Data source definitions
- **Cadence** - Event scheduling cadence
- **ProductMaster** - Product reference data
- **WriteTableSchema** - Output table schema
- **RunTimeEventMetadata** - Runtime event metadata

### Database Components (2 files)
- **BasicConnectionPool** - JDBC connection pooling
- **ConnectionPool** - Connection pool interface

### Utilities (8 files)
- **JsonbToBeamQuery** - JSONB to BeamQuery converter
- **JsonbToCadence** - JSONB to Cadence converter
- **JsonbToMonitor** - JSONB to Monitor converter
- **JsonbToQueryColumn** - JSONB to QueryColumn converter
- **JsonbToSource** - JSONB to Source converter
- **PgJsonbToMapConverter** - PostgreSQL JSONB converter
- Additional type converters

### Schemas
- **WriteSchema** - Output schema definitions

### UDFs
- **OperatorUDFs** - Custom SQL operator functions

---

## Project Structure

```
i2o-event-framework-pipeline/
├── src/
│   └── main/
│       └── java/com/corecompete/i2o/
│           ├── db/                  # Database connection (2 files)
│           ├── events/
│           │   ├── beam/            # Pipeline core (3 files)
│           │   ├── schemas/         # Output schemas (1 file)
│           │   ├── services/        # Business services (4 files)
│           │   └── udfs/            # User-defined functions (1 file)
│           ├── models/              # Domain models (15 files)
│           └── utility/             # Type converters (8 files)
├── Dockerfile                       # Flex Template container
├── README.md
└── pom.xml
```

---

## Key API Endpoints

This is a **batch pipeline** rather than a REST service. It doesn't expose HTTP endpoints. Instead, it's triggered via:

### Pipeline Parameters (EventOptions)
| Parameter | Description |
|-----------|-------------|
| `eventId` | Event definition ID to execute |
| `postgresURL` | PostgreSQL connection URL |
| `postgresDriver` | JDBC driver class |
| `postgresUsername` | Database username |
| `postgresPassword` | Database password |
| `writeToTable` | BigQuery destination table |
| `tempLocation` | GCS temp location |
| `date` | Execution date |
| `startDate` | Query start date |
| `endDate` | Query end date |
| `productDiscovery` | Product discovery GCS path |
| `productBsr` | Product BSR GCS path |

---

## Scope of the Project

The i2o-event-framework-pipeline covers:

1. **Dynamic Query Generation** - Build SQL from event definitions
2. **BigQuery Integration** - Read/write from BigQuery tables
3. **PostgreSQL Integration** - Read event definitions from PostgreSQL
4. **Beam SQL Execution** - Execute SQL using Apache Beam
5. **Schema Management** - Dynamic output schema generation
6. **Windowing Support** - Time-based windowing for aggregations
7. **Custom UDFs** - Operator functions for SQL queries
8. **Flex Template Support** - Containerized pipeline deployment
9. **Multi-Runner Support** - Direct, Portable, and Dataflow runners
10. **Event Configuration** - Configurable event processing logic

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **Event Processing** | Execute configured event definitions |
| **Data Aggregation** | Aggregate metrics by time windows |
| **ETL Pipelines** | Extract, transform, load data workflows |
| **Scheduled Analytics** | Time-based analytical computations |
| **Data Migration** | Move data between BigQuery tables |
| **Metric Calculations** | Compute business metrics |
| **Monitoring Events** | Generate monitoring alerts |
| **Product Analytics** | Product performance calculations |

---

## Deployment Notes

### Docker Build
Multi-stage Dockerfile for Flex Template:

```dockerfile
# Build stage
FROM adoptopenjdk/maven-openjdk11:latest AS build
ADD . /app
WORKDIR /app
RUN mvn clean package -Dmaven.test.skip=true

# Runtime stage (Dataflow Flex Template)
FROM gcr.io/dataflow-templates-base/java11-template-launcher-base:latest
COPY --from=build /app/target/i2o-event-framework-pipeline-2.9.3-SNAPSHOT.jar /template/
COPY --from=build /app/target/lib/ /template/lib/

ENV FLEX_TEMPLATE_JAVA_CLASSPATH=/template/i2o-event-framework-pipeline-2.9.3-SNAPSHOT.jar
ENV FLEX_TEMPLATE_JAVA_MAIN_CLASS=com.corecompete.i2o.events.beam.EventGenerator
```

### Build Commands
```bash
# Build with default (direct-runner) profile
mvn clean package

# Build with dataflow-runner profile
mvn clean package -Pdataflow-runner

# Run locally with DirectRunner
mvn exec:java -Dexec.mainClass=com.corecompete.i2o.events.beam.EventGenerator \
  -Dexec.args="--eventId=123 --postgresURL=jdbc:... ..."

# Run on Dataflow
mvn exec:java -Pdataflow-runner \
  -Dexec.mainClass=com.corecompete.i2o.events.beam.EventGenerator \
  -Dexec.args="--runner=DataflowRunner --project=... ..."
```

### Cloud Dependencies
- **Google Cloud Dataflow** - Pipeline execution engine
- **Google BigQuery** - Data source and destination
- **Google Cloud Storage** - Temporary files and templates
- **Cloud SQL** (PostgreSQL) - Event definitions storage

### Maven Profiles
| Profile | Description |
|---------|-------------|
| `direct-runner` (default) | Local execution with DirectRunner |
| `portable-runner` | Cross-language portable runner |
| `dataflow-runner` | Google Cloud Dataflow execution |

### Flex Template Deployment
```bash
# Build template image
gcloud builds submit --tag gcr.io/PROJECT/i2o-event-pipeline:latest

# Create Flex Template
gcloud dataflow flex-template build \
  gs://BUCKET/templates/i2o-event-pipeline.json \
  --image gcr.io/PROJECT/i2o-event-pipeline:latest \
  --sdk-language JAVA

# Run from template
gcloud dataflow flex-template run "job-name" \
  --template-file-gcs-location gs://BUCKET/templates/i2o-event-pipeline.json \
  --parameters eventId=123,date=2024-01-01
```

### Key Configuration
- Main class: `com.corecompete.i2o.events.beam.EventGenerator`
- Beam SDK version: 2.39.0
- Packaged as JAR with dependencies in `lib/` directory
