GitHub URL: git@github.com:i2o-retail/i2o-smartscout-css-download.git

# i2o SmartScout CSS Download

## Description

A Python Flask web service that automates product data extraction from SmartScout using Playwright browser automation. The service scrapes competitive selling scorecard (CSS) data, ASIN information, and product details from SmartScout, processes the data, and stores results in Google Cloud Storage. It supports multiple data extraction modes and integrates with AI services for enhanced data processing.

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.11+ |
| **Framework** | Flask |
| **Web Server** | Gunicorn |
| **Browser Automation** | Playwright (Chromium) |
| **Cloud Platform** | Google Cloud Platform |
| **Storage** | Google Cloud Storage (GCS) |
| **AI Integration** | Google GenAI, OpenAI |
| **Data Processing** | Pandas |
| **Containerization** | Docker |
| **Base Image** | Microsoft Playwright Python |

## Key Components

| Component | File | Description |
|-----------|------|-------------|
| **Flask API** | `app.py` | REST API for triggering data extraction |
| **SmartScout Scraper** | `run_scraper.py` | Main scraping engine with Playwright automation |
| **Product Extraction** | `product_extraction_service.py` | Product data extraction and processing |
| **Prompts** | `prompts.json`, `brand_prompts.json` | AI prompts for data processing |
| **Configuration** | `config.json` | Application configuration |
| **Browser Fixes** | `browser_fixes.py` | Browser automation utilities |

## Project Structure

```
i2o-smartscout-css-download/
├── app.py                          # Flask application entry point
├── run_scraper.py                  # SmartScout scraper implementation
├── run_scraper_old.py              # Legacy scraper version
├── product_extraction_service.py   # Product data extraction
├── browser_fixes.py                # Browser automation utilities
├── config.json                     # Application configuration
├── prompts.json                    # AI processing prompts
├── brand_prompts.json              # Brand-specific AI prompts
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── products.db                     # SQLite database for caching
├── css_data/                       # CSS data output directory
├── asin_data/                      # ASIN data output directory
├── i2o-dev-vertex-ai.json          # GCP Vertex AI credentials
└── smartscout_scraper_docs_V1.0.pdf # Documentation
```

## Key API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/extract` | POST | Triggers data extraction from SmartScout |
| `/extract` | OPTIONS | CORS preflight handler |

### Request Body Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `process_name` | string | Type of extraction: `css_data` or `asin_data` |
| `css_type` | string | CSS type: `base_css` or other variants |
| `region` | string | Market region (default: `US`) |
| `email` | string | Email for completion notification |
| `css_data` | array | List of brands with category/subcategory |
| `sellerid_list` | array | Optional list of seller IDs |
| `max_rows` | integer | Maximum rows to extract (default: 200) |

## Scope of the Project

- Automate SmartScout web scraping for product data
- Extract competitive selling scorecard (CSS) metrics
- Gather ASIN-level product information
- Process and filter data using AI services
- Store results in Google Cloud Storage
- Support multi-region marketplace data extraction
- Send email notifications upon completion

## Target Use Cases

1. **Market Research**: Extract competitive intelligence from SmartScout
2. **Product Analysis**: Gather product metrics and rankings
3. **Brand Monitoring**: Track brand performance across categories
4. **Seller Analysis**: Monitor seller activity and performance
5. **Data Pipeline**: Feed data into downstream analytics systems

## Deployment Notes

### Local Development
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Run locally
python app.py
```

### Docker Build & Run
```bash
docker build -t i2o-smartscout-css-download .
docker run -p 8080:8080 i2o-smartscout-css-download
```

### Google Cloud Run Deployment
```bash
gcloud builds submit --tag gcr.io/<PROJECT_ID>/i2o-smartscout-css-download
gcloud run deploy i2o-smartscout-css-download \
  --image gcr.io/<PROJECT_ID>/i2o-smartscout-css-download \
  --platform managed \
  --memory 2Gi \
  --timeout 3600
```

### Environment Variables
| Variable | Description |
|----------|-------------|
| `PORT` | Application port (default: 8080) |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to GCP service account JSON |
| `GCS_BUCKET` | Google Cloud Storage bucket name |

### Notes
- Uses non-root user (`appuser`) for security in container
- Playwright Chromium browser pre-installed in container
- Requires 2GB+ memory for browser automation
- Long-running requests need extended timeout (3600s recommended)
