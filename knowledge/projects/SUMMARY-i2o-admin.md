GitHub URL: https://github.com/i2o-retail/i2o-admin.git

# i2o-admin - Project Summary

## Description

The **i2o-admin** project is a **Customer Onboarding & Administration API** service that serves as the backend administration layer for the i2o retail platform. It provides comprehensive functionality for client management, reseller enforcement, notice handling, product categorization, user administration, and integration with various cloud services including Google Cloud Platform and Microsoft Azure.

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **Framework** | Spring Boot 2.3.4.RELEASE |
| **Language** | Java 1.8 |
| **Build Tool** | Maven |
| **Database** | PostgreSQL (with Cloud SQL integration) |
| **ORM** | Spring Data JPA, Hibernate |
| **Cloud Services** | Google Cloud (BigQuery, Cloud Storage, Pub/Sub), Firebase |
| **Email Services** | Microsoft Graph API, SendGrid |
| **Document Processing** | Apache POI (Excel), Apache PDFBox (PDF) |
| **API Documentation** | SpringFox (Swagger 3.0) |
| **Distributed Tracing** | Spring Cloud Sleuth |
| **Testing** | JUnit 5, Mockito, PowerMock |
| **Utilities** | Lombok, Jackson, Jsoup |

---

## Key Components

### Controllers (45 total)
Handles HTTP request/response processing for various API endpoints.

### Services (52 total)
Contains core business logic implementation.

### DAO Layer
Data access objects for PostgreSQL and BigQuery operations.

### DTO Layer (146 classes)
Data transfer objects for API request/response handling.

### PubSub Integration
Google Cloud Pub/Sub messaging for asynchronous email scheduling and event processing.

### Mail Sender
Email services supporting Microsoft Graph API and SendGrid integration.

### Notifications
Firebase Cloud Messaging (FCM) for push notifications.

### Map Module
Marketplace authorization program (MAP) notice services.

---

## Project Structure

```
i2o-admin/
├── src/
│   ├── main/
│   │   ├── java/com/corecompete/i2o/admin/
│   │   │   ├── config/         # Application configurations
│   │   │   ├── constants/      # Application constants & error messages
│   │   │   ├── controller/     # REST API controllers (45 files)
│   │   │   ├── dao/            # Data access objects (25 files)
│   │   │   ├── dto/            # Data transfer objects (146 files)
│   │   │   ├── exception/      # Custom exception handlers
│   │   │   ├── interceptor/    # Request interceptors
│   │   │   ├── mailsender/     # Email services (Graph & Grid)
│   │   │   ├── map/            # MAP notice services
│   │   │   ├── model/          # JPA entity models
│   │   │   ├── notifications/  # FCM notification services
│   │   │   ├── processor/      # Data processors
│   │   │   ├── pubsub/         # Google Pub/Sub handlers
│   │   │   ├── repository/     # JPA repositories
│   │   │   ├── service/        # Business logic layer (93 files)
│   │   │   ├── transformer/    # Data transformers
│   │   │   └── validation/     # Input validators
│   │   └── resources/
│   │       └── application-{env}.properties  # Environment configs
│   └── test/                   # Unit tests
├── pom.xml                     # Maven dependencies
└── README.md
```

---

## Key API Endpoints

### Client Onboarding (`/onboarding`)
| Endpoint | Description |
|----------|-------------|
| `POST /clientOnboarding` | Onboard a new client with organization setup |
| `POST /updateKeycloakAttributes` | Update Keycloak user attributes |
| `POST /trailExpiry/emails` | Send trial expiry notification emails |
| `POST /updateLogo` | Update organization and agency logos |

### Account Management (`/account`)
| Endpoint | Description |
|----------|-------------|
| `POST /validateAccount` | Validate marketplace account credentials |
| `POST /getAccountMetadataList` | Get metadata for multiple accounts |
| `POST /filteredAccountList` | Search and filter accounts |

### User Management (`/user`)
| Endpoint | Description |
|----------|-------------|
| `POST /save` | Create or update user |
| `POST /toggleStatus` | Enable/disable user status |
| `POST /removeOrgAccess` | Remove user organization access |

### Product Management (`/product`)
| Endpoint | Description |
|----------|-------------|
| `POST /productcatList` | Get product category list |
| `POST /productcatDetail` | Get product category details |
| `POST /uploadProductCat` | Upload product category template |
| `GET /downloadProductCatTemplate` | Download product category template |

### Reseller Enforcement (`/enforcement`)
| Endpoint | Description |
|----------|-------------|
| `POST /list` | Get reseller enforcement data |
| `PUT /{enforcementId}/escalation` | Update escalation status |
| `PUT /{enforcementId}/status` | Update enforcement status |
| `GET /{trackerId}` | Get reseller attribute data |
| `PUT /{trackerId}/buyerNotice` | Update buyer notice status |
| `PUT /{enforcementId}/notes` | Update enforcement notes |
| `PUT /{enforcementId}/invoice` | Update invoice status |

### Notice Management (`/notices`)
| Endpoint | Description |
|----------|-------------|
| `POST /{id}/send` | Send notice to a seller |
| `POST` | Send notices to multiple sellers |
| `POST /send-reply` | Send reply mail with attachments |
| `POST /uploadInvoice` | Upload invoice attachments |

### Client Reseller (`/client/reseller`)
| Endpoint | Description |
|----------|-------------|
| `POST /info` | Get reseller information |
| `POST /pop/timeline` | Get POP timeline data |

### Widget Data (`/widget`)
| Endpoint | Description |
|----------|-------------|
| `POST /getWidgetMetadata` | Get widget metadata configuration |
| `POST /getCardData` | Get card data for dashboard |

---

## Scope of the Project

The i2o-admin service covers:

1. **Client Lifecycle Management** - Onboarding, configuration, and account management
2. **User Administration** - User creation, status management, and access control
3. **Reseller Enforcement** - Tracking, escalation, and notice management for reseller violations
4. **Product Management** - Product category configuration and template handling
5. **Notification Services** - Email (via Graph/SendGrid) and push notifications (FCM)
6. **Reporting & Analytics** - Integration with BigQuery for data analytics
7. **Document Processing** - Excel report generation and PDF handling
8. **Multi-marketplace Support** - Managing accounts across various e-commerce platforms

---

## Target Use Cases

| Use Case | Description |
|----------|-------------|
| **New Client Onboarding** | Register and configure new clients in the i2o platform |
| **Reseller Violation Tracking** | Monitor and enforce MAP policies against unauthorized resellers |
| **Notice Dispatch** | Send cease & desist and other legal notices to violating sellers |
| **User Access Management** | Manage platform users and their organizational access |
| **Test Buy Management** | Handle test purchases for violation verification |
| **Invoice Processing** | Manage enforcement-related invoicing and billing |
| **Dashboard Widgets** | Provide data for administrative dashboards |
| **Email Communication** | Automated email notifications for various business events |

---

## Deployment Notes

### Environment Profiles
The application supports multiple environment configurations:
- `local`, `dev`, `qa`, `qa1` - Development/testing environments
- `uat`, `preuat`, `demouat` - UAT environments
- `preprod`, `prodstg` - Pre-production staging
- `prod` - Production environment
- `demo`, `custdemo` - Demo environments

### Packaging
- Packaged as **WAR** file for deployment on Tomcat
- Uses `spring-boot-starter-tomcat` with `provided` scope

### Cloud Dependencies
- **Google Cloud SQL** (PostgreSQL) with socket factory for database connectivity
- **Google Cloud Storage** for file/attachment storage
- **Google BigQuery** for analytics queries
- **Google Pub/Sub** for asynchronous message processing
- **Firebase Admin SDK** for push notifications

### Build Commands
```bash
# Build
./mvnw clean package

# Run locally
./mvnw spring-boot:run -Dspring.profiles.active=local

# Run tests
./mvnw test
```

### Key Configuration Properties
- Database connection via Cloud SQL socket factory
- Email service configuration (Microsoft Graph / SendGrid)
- Firebase credentials for FCM
- GCP project and bucket configurations
- Keycloak integration settings
