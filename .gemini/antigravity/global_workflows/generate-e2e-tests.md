---
description: Generate E2E Tests
---

# Generate E2E Tests Command

**Usage:** `/generate-e2e-tests <target> [options]`

## Description

Generates comprehensive end-to-end user journey tests using Playwright. Includes enhanced features like JSON test case definitions, MCP integration, and multi-level reporting.

## Arguments

### Required

- `<target>` - The user journey or workflow description to generate tests for.
- `<path>` - Target path where the E2E tests will be saved.

### Options

- `--resume` - Resume from existing task_list.md.
- `--mock-apis` - Generate API mocking infrastructure for isolated testing.
- `--validate` - Validate generated tests for accuracy.
- `--check-completeness` - Check completion percentage.

## Enhanced Features (Always Generated)

- **JSON Test Cases**: Structured definitions in `test-cases.json` for data-driven testing.
- **Playwright MCP Integration**: Uses Model Context Protocol for advanced browser automation.
- **Executable Runner Scripts**: `run-e2e-tests.sh` to execute suites with reporting.
- **Multi-Level Reporting**: Executive summaries, technical reports, and comprehensive logs.

## Examples

```bash
# Generate E2E tests for a document upload journey
/generate-e2e-tests "document upload workflow"
# Creates: tests/e2e/*.spec.ts, test-cases.json, run-e2e-tests.sh
```

## Generated File Structure

```
tests/e2e/
├── test_*.spec.ts              # Playwright test files
├── test-cases.json             # JSON test definitions
├── run-e2e-tests.sh           # Executable runner script
├── utils/                      # Test executor, reporting, MCP tools
└── reports/                    # Multi-level report output
```

## Quality Standards

- **Page Object Model**: Standardized POM implementation with Playwright.
- **User Journey Focus**: Realistic workflow patterns and interactions.
- **Artifact Collection**: Automated capture of screenshots, videos, and traces.
- **Performance**: Tests must complete within defined time thresholds.

## Implementation Workflow

1. **Strategic Planning**: Analyze user workflows and dependency maps.
2. **Strategy**: Apply universal E2E patterns; identify cross-functional needs.
3. **Creation**: Generate POMs, test scripts, and JSON definitions.
4. **Validation**: Validate against accessibility and reliability checklists.
