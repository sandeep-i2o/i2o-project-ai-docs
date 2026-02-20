GitHub URL: https://github.com/i2o-retail/i2o-image-comparison.git

# i2o-image-comparison Project Summary

## Description
`i2o-image-comparison` is a specialized microservice designed to perform advanced image similarity analysis. It leverages deep learning models (specifically ResNet) to extract features and compute similarity scores between images. This service is critical for identifying identical or similar product images across different datasets or timeframes. It offers both a synchronous REST API for real-time comparison and an asynchronous background worker that consumes comparison jobs from Google Cloud Pub/Sub.

## Technology Stack
- **Language:** Python 3.11
- **Framework:** Flask (Web API), Gunicorn (WSGI Server)
- **ML/AI:**
  - **PyTorch:** For running deep learning models (ResNet).
  - **OpenCV (`opencv-python-headless`):** For image preprocessing and alignment.
  - **Scikit-image, Scikit-learn:** Additional image processing utilities.
- **Cloud Services:**
  - **Google Cloud Run:** Optimized deployment target.
  - **Google Cloud Pub/Sub:** Asynchronous message queue for comparison jobs.
  - **Google Cloud Storage:** For downloading source images.
- **Key Libraries:**
  - `torch`, `torchvision`: Model inference.
  - `flask`, `flask_cors`: API handling.
  - `tenacity`: Retry logic.

## Key Components
- **Compare API (`compare_api.py`):** Exposes endpoints for synchronous image comparison (`/api/image/compare`) and system health checks.
- **PubSub Worker (`compare_api_pull.py`):** A background thread that continuously polls a Pub/Sub subscription for new comparison tasks, initiating the Deep Feature comparison logic.
- **Deep Feature Comparator (`CompareDeepFeature`):** The core engine that downloads images, preprocesses/aligns them, and calculates similarity using ResNet vectors and cosine distance.
- **UI Tool:** A simple HTML frontend (`/api/image/test`) for testing image comparison manually.

## Project Structure
```
i2o-image-comparison/
├── Dockerfile                   # container definition
├── deploy-cloud-run.sh          # Deployment script
├── requirements.txt             # Dependencies
├── image_comparison/
│   ├── api/                     # API routes and PubSub consumer
│   ├── core/
│   │   ├── similarity/          # Core comparison logic (DeepFeature, etc.)
│   │   ├── image_processor/     # Image processing pipelines
│   │   ├── service/             # Business logic layer
│   │   └── utils/               # Helper utilities
│   ├── config/                  # Configuration management
│   └── templates/               # HTML templates for UI tool
└── ...
```

## Key API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/image/compare` | POST | Synchronously compares two images and returns a similarity score. |
| `/api/image/pubsub/push` | POST | Pub/Sub push trigger endpoint (alternative to pull). |
| `/api/image/readiness_check` | GET | Checks if the ML models are loaded and service is ready. |
| `/api/image/test` | GET | Renders a UI for manual testing. |

## Scope & Target Use Cases
- **Product Matching:** verifying if product images from different sources (e.g., retailer vs. brand site) match.
- **Change Detection:** Monitoring listing images for unauthorized changes.
- **High-Fidelity Comparison:** Going beyond simple pixel matching to understand semantic similarity using deep features.

## Deployment Notes
- **Cloud Run:** The `deploy-cloud-run.sh` script optimizes the service for Cloud Run with specific memory (8Gi) and CPU (4 cores) settings to handle the ML workload.
- **Environment Variables:** Critical configuration for tuning PyTorch (`OMP_NUM_THREADS`, `MKL_NUM_THREADS`) is handled in the deployment script/Dockerfile.
