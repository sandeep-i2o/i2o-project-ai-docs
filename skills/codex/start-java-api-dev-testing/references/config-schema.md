# API Curl Config Schema

Use `.config/api_curl_tests/config.yaml` in the target repository.

## Fields

- `app.base_url`: Service base URL, for example `http://localhost:8080`.
- `app.startup_wait_seconds`: Max wait before startup/readiness fails.
- `app.ready_path`: Optional path checked before tests (empty string skips HTTP readiness check).
- `app.ready_expected_status`: Expected HTTP code for `ready_path`.
- `tests[]`: Curl tests list.

Each test supports:

- `name`: Friendly test name.
- `enabled`: Run only when `true`.
- `method`: HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- `endpoint`: Path relative to `app.base_url`.
- `expected_status`: Expected HTTP status code.
- `headers`: Optional header map.
- `payload`: Optional raw request body string.

## Example

```yaml
app:
  base_url: "http://localhost:8080"
  startup_wait_seconds: 120
  ready_path: ""
  ready_expected_status: 200

tests:
  - name: "POST /widget/getWidgetMetadata"
    enabled: true
    method: "POST"
    endpoint: "/widget/getWidgetMetadata"
    expected_status: 200
    headers:
      Content-Type: "application/json"
    payload: |
      {
        "orgId": "CHANGE_ME",
        "userId": "CHANGE_ME"
      }
```
