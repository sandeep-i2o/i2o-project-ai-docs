GitHub URL: git@github.com:i2o-retail/i2o-brand-violations.git

# i2o Brand Violations

## Description

A Python FastAPI microservice that captures and manages brand violation reports. It works as the backend service for a Chrome extension browser plugin that enables users to capture brand violations directly from the browser. The service handles file uploads, manages violation records, and integrates with Google Cloud services for storage and deployment.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.11+ |
| **Framework** | FastAPI |
| **Web Server** | Uvicorn |
| **Cloud Platform** | Google Cloud Platform |
| **Storage** | Google Cloud Storage |
| **Deployment** | Google Cloud Run |
| **Package Manager** | uv |
| **Containerization** | Docker |

## Key Components

| Component | Description |
|-----------|-------------|
| **Plugin Server** | FastAPI backend service handling violation capture and management |
| **Chrome Extension** | Browser plugin for capturing brand violations directly from web pages |
| **GCS Integration** | File upload and storage management via Google Cloud Storage |
| **REST API** | RESTful endpoints for CRUD operations on violation records |

## Project Structure

```
i2o-brand-violations/
├── plugin/
│   ├── server/
│   │   └── i2o-brand-violations-plugin-server/
│   │       ├── app/                    # FastAPI application
│   │       │   └── config/             # Configuration modules
│   │       ├── tests/                  # Test suites
│   │       └── resources/              # Environment configurations
│   └── extension-client/               # Chrome extension source
│       ├── tsconfig.json               # TypeScript configuration
│       └── package-lock.json           # Node.js dependencies
├── README.md
└── o3-mini-README.md                   # Extended documentation
```

## Key API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/api/violation/clients` | GET | Returns a list of clients with their IDs and names |
| `/v1/api/violation` | GET | Retrieves violation records based on suspect product code |
| `/v1/api/violation` | POST | Creates a new brand violation record with file upload |

## Scope of the Project

- Capture and store brand violation reports from authorized users
- Manage violation records with full CRUD capabilities
- Integrate with Chrome extension for seamless violation capture
- Store violation evidence files in Google Cloud Storage
- Provide client management for multi-tenant architecture

## Target Use Cases

1. **Brand Protection Teams**: Capture unauthorized reseller violations
2. **Compliance Officers**: Track and document brand misuse across e-commerce platforms
3. **Legal Teams**: Gather evidence for enforcement actions
4. **Market Analysts**: Monitor brand presence and violations across marketplaces

## Deployment Notes

### Local Development
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
uv install -r requirements.txt

# Run locally
uvicorn app.api:app --reload
```

### Docker Deployment
```bash
docker build -t i2o-brand-violations .
docker run -p 8080:8080 i2o-brand-violations
```

### Cloud Run Deployment
```bash
gcloud builds submit --tag gcr.io/<PROJECT_ID>/i2o-brand-violations
gcloud run deploy i2o-brand-violations \
  --image gcr.io/<PROJECT_ID>/i2o-brand-violations \
  --platform managed \
  --region <REGION>
```

### Environment Variables
- Database URL configuration
- Google Cloud project and bucket details
- Service-specific settings (see `resources/.env.example`)
