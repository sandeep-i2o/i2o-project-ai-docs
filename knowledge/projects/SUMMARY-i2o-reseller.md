GitHub URL: https://github.com/i2o-retail/i2o-reseller.git

# i2o-reseller

## Description

**i2o-reseller** is a Spring Boot 3.1.7 backend service designed for **Detailed Reports, Reseller Management, and Sales Analytics**. It provides a comprehensive reporting framework, data visualization APIs, forecast management, and integration with Google Cloud Platform services (BigQuery, GCS). The application serves as a central backend for reseller analytics, portfolio views, and team management.

---

## Technology Stack

| Technology | Version |
|------------|---------|
| Java | 17 |
| Spring Boot | 3.1.7 |
| Spring Cloud | 2022.0.5 |
| Google Cloud BigQuery | 2.40.0 |
| PostgreSQL | Runtime |
| Apache POI (Excel) | 4.1.1 |
| Lombok | 1.18.34 |
| SpringDoc OpenAPI | 2.3.0 |
| SendGrid | 4.6.5 |

---

## Key Components

### 1. Report Framework (`reportfwk`)
Core reporting engine providing configurable data retrieval, filtering, and metadata management for dynamic report generation from BigQuery.

### 2. Widget & Chart Service (`reseller`)
Data visualization layer providing chart data, card metrics, calendar views, and tooltip data for dashboard widgets.

### 3. Forecast Module (`forecast`)
Manages forecast data including supply worksheet grids, PO forecast charts, and forecast CRUD operations with pagination support.

### 4. Portfolio View (`portfolioview`)
Provides client metric details and portfolio analytics with metric conversion capabilities.

### 5. Teams Management (`teams`)
User and feedback management for teams including CRUD operations for team users with organization-level filtering.

### 6. Excel Generation (`excel`)
Dynamic Excel report generation with customizable columns and streaming workbook support (SXSSF).

### 7. GCS Download Service (`gcsdownload`)
Google Cloud Storage integration for file downloads and signed URL generation.

### 8. Reseller Master Management (`resellermastermgmt`)
Bulk data import functionality via Excel file upload and processing.

### 9. Reseller Enforcement Prioritization (`resellerenforcementprioritize`)
Prioritization logic for reseller enforcement workflows.

---

## Project Structure

```
src/
├── main/
│   ├── appengine/                    # App Engine configuration
│   ├── java/com/corecompete/i2o/
│   │   ├── I2oResellerApplication.java    # Main Spring Boot application
│   │   ├── config/                   # Application configurations
│   │   ├── constants/                # Application constants
│   │   ├── controller/               # Base controllers (Sales Download, SharePoint)
│   │   ├── dao/                      # Data access layer
│   │   ├── exception/                # Custom exception handlers
│   │   ├── filters/                  # Request/Response filters
│   │   ├── utility/                  # Helper utilities
│   │   │
│   │   ├── reportfwk/                # Report Framework module
│   │   │   ├── controller/
│   │   │   ├── dto/
│   │   │   ├── entity/
│   │   │   └── service/
│   │   │
│   │   ├── reseller/                 # Widget & Chart services
│   │   │   ├── controller/
│   │   │   ├── dto/
│   │   │   ├── entity/
│   │   │   └── service/
│   │   │
│   │   ├── forecast/                 # Forecast management
│   │   │   ├── controller/
│   │   │   ├── dto/
│   │   │   └── service/
│   │   │
│   │   ├── portfolioview/            # Portfolio analytics
│   │   ├── teams/                    # Teams user & feedback
│   │   ├── excel/                    # Excel report generation
│   │   ├── gcsdownload/              # GCS integration
│   │   ├── resellermastermgmt/       # Master data management
│   │   ├── resellerenforcementprioritize/ # Enforcement prioritization
│   │   └── addentriesinfilter/       # Filter configuration
│   │
│   └── resources/                    # Application properties & configs
│
└── test/                             # Unit and integration tests
```

---

## Key API Endpoints

### Widget APIs (`/widget`)
| Endpoint | Description |
|----------|-------------|
| `POST /getWidgetMetadata` | Retrieves widget metadata configuration |
| `POST /getUiLayoutJson` | Gets UI layout JSON configuration |
| `POST /getAppliedConfigurations` | Fetches applied widget configurations |
| `POST /getChartData` | Returns chart visualization data |
| `POST /getCardData` | Provides card/KPI metrics data |
| `POST /getCalendarData` | Retrieves calendar heatmap data |
| `POST /getToolTipData` | Gets tooltip content for charts |
| `POST /getPriceAcrossPlatformCardData` | Price comparison across platforms |

### Report APIs (`/report`)
| Endpoint | Description |
|----------|-------------|
| `POST /getReportMetadata` | Retrieves report configuration metadata |
| `POST /getReportData` | Fetches paginated report data from BigQuery |
| `POST /getFilterData` | Gets filter dropdown values |
| `POST /getGridCardData` | Returns grid-style card data |
| `POST /getDynamicColumnsGridCardData` | Dynamic column grid data |
| `POST /getSearchFilterData` | Search-based filter data |
| `POST /getGenericReportMetadata` | Generic report configuration |
| `POST /portfolio-view` | Portfolio view client metrics |

### Forecast APIs (`/forecast`)
| Endpoint | Description |
|----------|-------------|
| `POST /data/insert` | Inserts new forecast records |
| `POST /data/find` | Finds specific forecast record |
| `POST /data/all` | Retrieves all forecast records (paginated) |
| `POST /data/filter` | Filters forecast records with pagination |
| `POST /overview/getPOForecastChartData` | PO forecast chart visualization |

### Teams APIs (`/teams-user`)
| Endpoint | Description |
|----------|-------------|
| `POST /` | Creates new teams user |
| `GET /` | Gets all teams users (paginated) |
| `GET /{userId}` | Gets specific user by ID |
| `GET /org/{orgId}` | Gets users by organization ID |

### Excel Export (`/excelReport`)
| Endpoint | Description |
|----------|-------------|
| `POST /exportExcel` | Generates and downloads Excel report |

### GCS Integration (`/gcs`)
| Endpoint | Description |
|----------|-------------|
| `GET /filedownload` | Downloads file from Google Cloud Storage |
| `GET /generateSignedUrl` | Generates signed URL for GCS object |
| `GET /downloadFileByModelAndProperty` | Downloads file by module/property configuration |

### Reseller Management (`/resellerMaster`, `/enforcementPrioritize`)
| Endpoint | Description |
|----------|-------------|
| `POST /readFile` | Uploads and processes Excel master data |
| `POST /` | Submits reseller for prioritization |
| `POST /getEnforcementPrioritizedReseller` | Checks if reseller is prioritized |

---

## Scope of the Project

### Primary Functions
- **Sales Analytics & Reporting**: Dynamic report generation with configurable filters, columns, and data sources from BigQuery
- **Dashboard Visualization**: Chart data, KPI cards, calendar heatmaps, and widget configurations
- **Reseller Management**: Master data import, enforcement prioritization, and reseller analytics
- **Forecast Management**: Supply planning with forecast data CRUD operations
- **Portfolio Analytics**: Client portfolio views with metric calculations

### Integration Points
- **Google BigQuery**: Primary data warehouse for analytics queries
- **Google Cloud Storage**: File storage and download services
- **PostgreSQL**: Application database for configurations and metadata
- **SendGrid**: Email notification services
- **SharePoint**: Document integration

### Target Use Cases
1. Multi-tenant SaaS reporting for reseller analytics
2. Price monitoring across e-commerce platforms
3. Sales forecasting and supply planning
4. Team collaboration and user management
5. Bulk master data processing via Excel imports

---

## Deployment

The application is configured for deployment on **Google App Engine** with:
- WAR packaging
- Cloud SQL PostgreSQL connectivity
- Micrometer tracing for observability
- JaCoCo for code coverage analysis
