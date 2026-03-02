---
description: Generate API Tests
---

# Generate API Tests Command

**Usage:** `/generate-api-tests <target> [options]`

## Description

Generates comprehensive Pytest-based API integration tests to validate endpoint functionality, response schemas, and integration logic.

## Arguments

### Required

- `<target>` - The target service or endpoint description to generate API tests for.
- `<path>` - Target path where the API tests will be saved.

### Options

- `--resume` - Resume test generation from existing task_list.md.
- `--check-completeness` - Check completion percentage and show pending items.
- `--validate` - Validate that generated tests are accurate and runnable.
- `--service-discovery` - Automatically identify required API endpoints.
- `--integration-mode <mode>` - Specify approach (isolated, sandbox, contract).
- `--output <path>` - Custom output directory (defaults to backend/tests/integration/).

## Examples

```bash
# Generate API tests for a validation engine service
/generate-api-tests src/backend/src/services/validation_engine_service.py
# Creates: backend/tests/integration/*.py, run-api-tests.sh
```

## Generated File Structure

```
tests/api/
├── test_*.py                   # Pytest API test files
├── run-api-tests.sh            # Executable runner script
├── utils/                      # Reporting utilities
└── reports/                    # Executive and Technical reports
```

## Quality Standards

- **Pytest Structure**: Standard fixtures, parametrization, and authentication patterns.
- **Response Validation**: Comprehensive schema validation and status code verification.
- **Performance Thresholds**: Response time and concurrent request testing.
- **Reliability**: Maximum 2% flaky test rate.

## Implementation Workflow

1. **Code Analysis**: Parse target endpoints and dependency maps.
2. **Strategy**: Apply API testing patterns from templates; identify error scenarios.
3. **Creation**: Generate test files with standardized naming and structure.
4. **Validation**: Validate against quality checklists and ensure comprehensive coverage.
