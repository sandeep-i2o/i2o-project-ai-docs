GitHub URL: git@github.com:i2o-retail/i2o-alerts-exceptions-bcm.git

# i2o-alerts-exceptions-bcm

## Description

A Spring Boot-based backend microservice for the **i2oRetail** platform that provides APIs for managing **Alerts & Exceptions**, **Business Content Management (BCM)**, **User Preferences**, **Filtering**, and **UI Configuration**. This service acts as a central hub for handling real-time business insights, KPI dashboards, user-specific filter configurations, and product content analytics.

---

## Technology Stack

| Category         | Technology                              |
|------------------|-----------------------------------------|
| **Language**     | Java 17                                 |
| **Framework**    | Spring Boot 3.1.7                       |
| **ORM**          | Spring Data JPA / Hibernate 6.2         |
| **Database**     | PostgreSQL                              |
| **Analytics**    | Google Cloud BigQuery                   |
| **API Docs**     | SpringDoc OpenAPI (Swagger UI)          |
| **Reactive**     | Spring WebFlux                          |
| **Email**        | SendGrid                                |
| **Build Tool**   | Maven                                   |
| **Deployment**   | Google App Engine (Flex Environment)    |
| **Auth**         | Keycloak (OAuth2/Bearer Token)          |
| **Observability**| Micrometer Tracing, Spring Actuator     |
| **Testing**      | JUnit, JaCoCo for code coverage         |

---

## Project Structure

```
i2o-alerts-exceptions-bcm/
├── src/main/java/com/corecompete/i2o/
│   ├── I2oAlertsExceptionsApplication.java   # Main Spring Boot entry point
│   ├── alebcm/                               # Alerts & Exceptions module
│   │   ├── config/                           # Configuration classes (Swagger, Alerts)
│   │   ├── constants/                        # Enums and constant definitions
│   │   ├── controller/                       # REST API controllers
│   │   ├── dto/                              # Data Transfer Objects
│   │   ├── exception/                        # Custom exception handling
│   │   ├── filter/                           # HTTP filters
│   │   ├── model/                            # DAO and entity models
│   │   └── service/                          # Business logic services
│   └── bcm/                                  # Business Content Management module
│       ├── controller/                       # BCM REST controllers
│       ├── dto/                              # BCM DTOs
│       ├── model/                            # BCM entity models
│       ├── service/                          # BCM services
│       └── utility/                          # BCM utility classes
├── src/main/resources/
│   ├── application.properties                # Base configuration
│   └── application-{env}.properties          # Environment-specific configs
├── src/main/appengine/
│   └── app.yaml                              # Google App Engine deployment config
└── pom.xml                                   # Maven build file
```

---

## Key Components

### Controllers
| Controller                   | Description                                           |
|------------------------------|-------------------------------------------------------|
| `AlertsExceptionsController` | Date view data for alerts and exceptions overview     |
| `SalesInsightsController`    | KPI cards user preferences for sales insights         |
| `FilterController`           | Dynamic filter data for various screen modules        |
| `HeaderController`           | User preferences for UI headers and portfolio views   |
| `SavedFilterController`      | CRUD operations for saved/preset filters              |
| `UIController`               | UI configuration and user info for the frontend app   |
| `ProductController` (BCM)    | Product content details, charts, and trendlines       |

### Services
| Service                      | Description                                           |
|------------------------------|-------------------------------------------------------|
| `AlertsExceptionService`     | Business logic for alerts and exceptions data         |
| `FilterService`              | Dynamic filter generation based on screen/org context |
| `HeaderService`              | User preference management and validation             |
| `SalesInsightsService`       | KPI/Sales insights preferences management             |
| `SavedFilterService`         | Preset filter CRUD operations                         |
| `SchedulerFilterService`     | Scheduler-based filter configurations                 |
| `UserService`                | User information retrieval                            |
| `ProductDashboardService`    | BCM product analytics and content scoring             |

### Data Access
| Component                    | Description                                           |
|------------------------------|-------------------------------------------------------|
| `UIConfigDAO`                | UI configuration and theme data access                |
| `OrgMetadataDAO`             | Organization metadata access layer                    |
| BigQuery Integration         | Analytics queries via Google Cloud BigQuery           |

---

## Key API Endpoints

### Alerts & Exceptions
| Endpoint                     | Method | Description                                  |
|------------------------------|--------|----------------------------------------------|
| `/alerts/date-view`          | POST   | Retrieves date-based view of alerts data     |

### Sales Insights / KPI Cards
| Endpoint                                         | Method | Description                                  |
|--------------------------------------------------|--------|----------------------------------------------|
| `/kpi-cards/user/getSalesInsightsPreferences`    | POST   | Get user KPI preferences                     |
| `/kpi-cards/user/updateSalesInsightsPreferences` | POST   | Update user KPI preferences (max 5 metrics)  |
| `/kpi-cards/user/deleteSalesInsightsPreferences` | POST   | Delete user KPI preferences                  |

### Filters
| Endpoint                     | Method | Description                                  |
|------------------------------|--------|----------------------------------------------|
| `/filters`                   | POST   | Get dynamic filters by org/screen context    |

### User Preferences
| Endpoint                     | Method | Description                                  |
|------------------------------|--------|----------------------------------------------|
| `/saveUserPreference`        | POST   | Save user header/UI preferences              |
| `/deleteUserPreference`      | POST   | Delete user preferences                      |
| `/checkUserPreference`       | POST   | Check if user has preferences                |
| `/getUserPreference`         | POST   | Retrieve user preferences                    |
| `/removeUserPreference`      | POST   | Remove specific user preference              |
| `/portfolio/get-preference`  | POST   | Get portfolio view preferences               |
| `/portfolio/save-preference` | POST   | Save portfolio view preferences              |

### Saved Filters
| Endpoint                             | Method | Description                              |
|--------------------------------------|--------|------------------------------------------|
| `/savefilters/save`                  | POST   | Save a new filter preset                 |
| `/savefilters/getfilters`            | POST   | Get all saved filters for user           |
| `/savefilters/schedulerFilters`      | GET    | Get scheduler-related filters            |
| `/savefilters/deletePreset`          | POST   | Delete a filter preset                   |
| `/savefilters/editPreset`            | POST   | Edit an existing filter preset           |
| `/savefilters/increasePresetUsedCount`| POST  | Increment usage count of a preset        |

### UI Configuration
| Endpoint                     | Method | Description                                  |
|------------------------------|--------|----------------------------------------------|
| `/getUserInfo/{email}`       | GET    | Get user information by email                |
| `/getUIConfig/{orgId}`       | GET    | Get UI configuration by organization         |
| `/healthCheck`               | GET    | Health check endpoint                        |

### BCM (Business Content Management)
| Endpoint                     | Method | Description                                  |
|------------------------------|--------|----------------------------------------------|
| `/bcm/content_detail`        | POST   | Get product content details and scores       |
| `/bcm/chart`                 | POST   | Get product chart data                       |
| `/bcm/trendline`             | POST   | Get product trend data                       |
| `/bcm/detail`                | POST   | Get detailed product information             |

---

## Scope of the Project

This microservice is responsible for:

1. **Alerts & Exceptions Management** — Provides date-view data for monitoring business alerts and exceptions across the retail platform.

2. **User Preference Management** — Stores and retrieves user-specific UI configurations, header settings, and filter preferences per screen/widget.

3. **Dynamic Filtering** — Generates dynamic filter options based on organization context, screen codes, and org type.

4. **KPI Dashboard Support** — Manages sales insights and KPI card preferences for personalized dashboard experiences.

5. **Saved/Preset Filters** — Enables users to save, edit, and reuse filter presets across sessions.

6. **UI Configuration** — Serves frontend configuration such as themes, logos, landing pages, and module access roles.

7. **BCM Analytics** — Provides product content scoring, trend analysis, and chart data for business content management.

---

## Target Use Cases

- **Retail Operations Dashboard** — Real-time visibility into alerts and exceptions for category managers and business analysts.
- **Personalized KPI Cards** — Users can customize their homepage KPI cards with preferred sales metrics.
- **Filter Management** — Business users can save complex filter combinations for quick access.
- **Multi-Tenant UI Configuration** — Different organizations can have custom themes, logos, and landing pages.
- **Product Content Analytics** — Track and analyze product content health scores and trends over time.

---

## Deployment Notes

### Google App Engine Configuration
The application is deployed on **Google App Engine Flex Environment** with the following settings:

```yaml
runtime: java
env: flex
service: alerts

automatic_scaling:
  min_num_instances: 1
  max_num_instances: 4
  cpu_utilization:
    target_utilization: 0.6

resources:
  cpu: 1
  memory_gb: 2
  disk_size_gb: 10
```

### Environment Profiles
Multiple environment profiles are available:
- `local` — Local development
- `dev` — Development environment
- `qa`, `qa1` — QA environments
- `uat`, `preuat`, `demouat` — UAT environments
- `preprod`, `prodstg` — Pre-production/Staging
- `prod` — Production
- `demo`, `custdemo` — Demo environments
- `cob` — COB environment

### Build & Run
```bash
# Build the project
./mvnw clean package

# Run locally
./mvnw spring-boot:run -Dspring-boot.run.profiles=local

# Deploy to App Engine
./mvnw appengine:deploy
```

### Key Configuration Properties
| Property                          | Description                         |
|-----------------------------------|-------------------------------------|
| `spring.profiles.active`          | Active Spring profile               |
| `spring.jpa.database-platform`    | PostgreSQL dialect                  |
| `keycloak.*`                      | Keycloak authentication settings    |
| `sendgrid.api.key`                | SendGrid API key for emails         |
| `azure.graph.*`                   | Azure Graph API integration         |

---

## Dependencies on Other Services

| Dependency          | Description                                      |
|---------------------|--------------------------------------------------|
| `common-utils`      | Shared utility library (`com.corecompete.i2o`)   |
| `db-utils`          | Database utility library (`com.corecompete.i2o`) |
| PostgreSQL          | Primary relational database                      |
| Google BigQuery     | Analytics and large-scale data queries           |
| Keycloak            | Identity and access management                   |
| SendGrid            | Email notification service                       |
