GitHub URL: https://github.com/i2o-retail/i2o_flask_api_module.git

# i2o_flask_api_module Project Summary

## Description
`i2o_flask_api_module` is a multi-purpose Flask API service that acts as a utility hub for the i2o retail platform. It aggregates several distinct functionalities into a single deployable service, including client onboarding orchestration, Docusign OAuth integration, product discovery job management, buybox monitoring, and recurring subscription handling (Recurly). It serves as a backend interface for various frontend applications and internal automations.

## Technology Stack
- **Language:** Python 3.10
- **Framework:** Flask (Web API), Gunicorn (WSGI Server)
- **Database:** PostgreSQL (`psycopg2`)
- **Third-Party Integrations:**
  - **Docusign:** For electronic signature workflows and OAuth.
  - **SendGrid:** For transactional email delivery.
  - **Recurly:** For subscription billing management.
  - **Selenium:** For browser automation tasks (likely Buybox checks or validation).
- **Cloud Services:**
  - **Google Cloud Logging:** Centralized logging.
  - **Google Cloud Secret Manager:** configuration security.
- **Key Libraries:**
  - `flask`, `flask_cors`: API development.
  - `selenium`: Web automation.
  - `google-cloud-*`: GCP integration.

## Key Components
- **Index (`src/python/index.py`):** The main entry point that registers Blueprints for different functional areas.
- **Onboarding Module (`src/python/onboarding`):** Manages the logic for onboarding new organizations and accounts (`onboarding_org_api`, `onboarding_account_api`).
- **Docusign Module (`src/python/docusign`):** Handles Docusign OAuth flows and token management (`docusign_oauth_api`).
- **Buybox Module (`src/python/buybox`):** APIs related to monitoring and analyzing product buybox status.
- **Utils:**
  - `otp_generator`: Generates One-Time Passwords for verification.
  - `product_discovery_job_creator`: Triggers product discovery jobs.
  - `validate`: Credentials validation service.

## Project Structure
```
i2o_flask_api_module/
├── dev.yaml, qa.yaml, etc.  # App Engine/Cloud Run config
├── requirements.txt         # Dependencies
├── chrome_driver/           # Selenium driver
├── src/
│   └── python/
│       ├── index.py         # App Entry Point
│       ├── config.py        # Configuration loading
│       ├── onboarding/      # Onboarding APIs
│       ├── docusign/        # Docusign Integration
│       ├── buybox/          # Buybox Logic
│       ├── recurly/         # Subscription Logic
│       └── utils/           # Shared Utilities (Email, OTP, Validation)
```

## Key API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/dp/validate` | POST | Validates user credentials against a source. |
| `/dp/pd_job_creator` | POST | Creates a generic Product Discovery job. |
| `/dp/pd_job_status` | POST | Checks the status of a Product Discovery job. |
| `/dp/get_refresh_token` | POST | Swaps an auth code for a refresh token (OAuth flow). |
| `/dp/get_otp` | POST | Generates a 2FA OTP code. |
| `/docusign/...` | Various | Endpoints for Docusign auth and webhook handling. |

## Scope & Target Use Cases
- **Centralized Utility Service:** Providing shared backend logic (email, auth, validation) for multiple frontend apps.
- **Integration Hub:** Managing 3rd party connections (Docusign, Recurly) in one place.
- **Automation Support:** Triggering background jobs like product discovery.

## Deployment Notes
- **App Engine Flex:** configured via `dev.yaml` to run in a custom runtime ("ubuntu22") with specific resources.
- **Environment Variables:** critical for service configuration (`ENV`, `DOCUSIGN_*`), loaded at runtime.
