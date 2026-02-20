GitHub URL: git@github.com:i2o-retail/i2o-email-service.git

# i2o-email-service Project Summary

## Description
`i2o-email-service` is a robust Java-based backend service built with Spring Boot. It serves as the centralized communication hub for the i2o platform, handling both outbound transactional emails (e.g., MAP violations, notices) and inbound email processing via webhooks. It tightly integrates with SendGrid for email delivery and Google Cloud Platform services for data handling and event messaging.

## Technology Stack
- **Language:** Java 21
- **Framework:** Spring Boot 3.5.5
- **Build Tool:** Maven
- **Database:** PostgreSQL (`spring-boot-starter-data-jpa`, `JdbcTemplate`)
- **Cloud Services:**
  - **Google Cloud BigQuery:** For querying data related to notices or reports.
  - **Google Cloud Pub/Sub:** Event-driven messaging.
  - **Google Cloud Storage:** Storing email attachments/assets.
  - **Google Cloud Secret Manager:** Configuration security.
- **Key Libraries:**
  - `sendgrid-java`: SendGrid API integration.
  - `spring-ai-pdf-document-reader`: PDF processing (likely for parsing attachments).
  - `handlebars`: Templating engine for email content.
  - `lombok`: Boilerplate reduction.

## Key Components
- **Controllers:**
  - `Controller`: Basic health check and manual trigger for notice generation.
  - `SendGridWebhookController`: Receives callbacks from SendGrid for email delivery events (delivered, opened, clicked) and processes inbound emails parsed by SendGrid.
- **Services:**
  - **Notice Generator (`NoticeGeneratorService`):** Logic to generate and send formal notices to retailers or brands.
  - **MAP Generator (`MapGeneratorService`):** Handles the generation of Minimum Advertised Price (MAP) violation emails.
  - **Webhook Handlers:** Factory-based pattern (`WebhookHandlerFactory`, `InboundEmailHandlerFactory`) to process different types of webhook events and inbound email providers.
- **Mail Senders:** Specialized components for constructing and dispatching emails via SendGrid.

## Project Structure
```
i2o-email-service/
├── pom.xml                  # Maven dependencies
├── src/
│   ├── main/
│   │   ├── java/com/i2oretail/emailservice/
│   │   │   ├── controller/      # API Endpoints
│   │   │   ├── service/         # Business Logic (Notices, MAP, Webhooks)
│   │   │   ├── repository/      # Data Access
│   │   │   ├── webhook/         # Webhook Handler Logic
│   │   │   ├── mailsender/      # Email Dispatching Logic
│   │   │   ├── dto/             # Data Transfer Objects
│   │   │   └── model/           # JPA Entities
│   │   └── resources/
│   │       ├── application.properties # Configuration
│   │       └── templates/            # Handlebars templates
```

## Key API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check and manual trigger for notice generation parameters (`retId`, `qId`, `noticeNumber`). |
| `/webhook/{provider}/notice` | POST | Receives Email Event Webhooks from providers (e.g., SendGrid). |
| `/webhook/{provider}/inbound` | POST | Receives Inbound Parse Webhooks (incoming emails) from providers. |

## Scope & Target Use Cases
- **Transactional Emails:** Sending system alerts, reports, and violation notices to users.
- **Email Interaction:** Processing replies or incoming emails to trigger system actions.
- **Event Tracking:** Monitoring email delivery status (bounces, opens) to maintain sender reputation and audit trails.

## Deployment Notes
- **Containerized:** Includes a `Dockerfile` for container deployment.
- **Configuration:** Uses standard Spring Boot `application.properties`, likely overridden by environment variables in production (GCP).
- **Java Version:** Requires Java 21 runtime.
