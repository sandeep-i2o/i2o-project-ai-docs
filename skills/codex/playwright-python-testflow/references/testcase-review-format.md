# Test Case Review Format

Present generated executable tests in a compact table before execution.

| Test ID | User Story | Scenario | File Path | Marker/Tag |
| --- | --- | --- | --- | --- |
| PW-001 | US-12 | Buyer login with valid credentials | tests/e2e/playwright/test_login.py::test_valid_login | smoke |
| PW-002 | US-13 | Buyer receives validation for invalid password | tests/e2e/playwright/test_login.py::test_invalid_password | regression |

Rules:
- Keep one scenario per row.
- Map each row to at least one user story.
- Ask for explicit approval after presenting the table.
