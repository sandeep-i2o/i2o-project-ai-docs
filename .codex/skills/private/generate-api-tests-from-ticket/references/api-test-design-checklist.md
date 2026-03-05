# API Test Design Checklist

Use this checklist to keep endpoint coverage complete and consistent.

## 1) Endpoint Contract

- Confirm method + path from ticket (`GET/POST/...` and URI).
- Confirm request payload/query/path parameters.
- Confirm required headers and auth model.
- Confirm expected status codes from acceptance criteria.
- Confirm response shape (required fields and types).

## 2) Minimum Scenario Set

For each endpoint/method, cover:
- Success path with strong response assertions.
- Input validation failure (missing/invalid required fields).
- Authentication missing/invalid token (if protected).
- Authorization denied for insufficient role/scope (if applicable).
- Not found / missing resource behavior (when resource lookup is required).

## 3) Business Rule and Data Integrity Cases

- Verify ticket-specific business constraints (for example unique fields, state transitions, ownership checks).
- Verify side effects (DB writes, events, downstream calls) when part of ticket scope.
- Verify idempotency rules for PUT/PATCH/DELETE/retry scenarios when required.

## 4) Test Reliability

- Use deterministic fixtures/factories.
- Freeze time when testing time-sensitive logic.
- Avoid asserting entire payloads when only partial contract is stable.
- Reuse existing test helpers and setup conventions from repo.

## 5) Assertion Quality

- Assert status code and error code/message (where standardized).
- Assert key response fields, not only status.
- Assert persistence/state change for mutating endpoints.
- Assert no unintended mutation for rejected requests.

## 6) Traceability

- Tag each test with ticket ID in test name or nearby comment.
- Keep one-to-many mapping from ticket acceptance criteria to tests in the report.
- Document any deferred case with reason (blocked, out-of-scope, dependency gap).
