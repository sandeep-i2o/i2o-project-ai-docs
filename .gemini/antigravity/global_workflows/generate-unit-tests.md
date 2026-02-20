---
description: Generate Unit Tests
---

# Generate Unit Tests Command

**Usage:** `/generate-unit-tests <target> [options]`

## Description

Generates comprehensive unit test suites using the quality-engineer agent, focusing on individual functions, methods, or components to ensure isolated logic correctness.

## Arguments

### Required

- `<target>` - The target file path, function name, or component to generate unit tests for.
- `<path>` - Target path where the unit tests will be saved.

### Options

- `--resume` - Resume test generation from existing task_list.md.
- `--check-completeness` - Check completion percentage and show pending items.
- `--validate` - Validate that generated tests are accurate, runnable, and follow standards.
- `--coverage` - Include coverage analysis and identify gaps.
- `--mocks` - Generate mock objects and fixtures.
- `--async` - Generate async test patterns (auto-supported).
- `--output <path>` - Custom output directory (defaults to unit test folder).

## Examples

```bash
# Generate unit tests for a Python service
/generate-unit-tests src/backend/services/validation_service.py
# Creates: backend/tests/unit/test_validation_service.py

# Generate unit tests for a React component
/generate-unit-tests src/frontend/components/Button.tsx
# Creates: frontend/tests/unit/Button.test.tsx
```

## Implementation

Following the quality-engineer systematic approach:

1. **Initialize Task Management**: Create `task_list.md` for process tracking and resumability.
2. **Analyze Target Code**: Parse structure, identify testable units, and detect async patterns.
3. **Generate Test Strategy**: Apply unit testing patterns, identify edge cases, and load config.
4. **Create Test Suites**: Generate isolated tests with setup, teardown, and mocks.
5. **Quality Assurance**: Validate against quality checklists and ensure coverage.

## Task Management

Uses a shared `task_list.md` format for progress tracking and process recovery. The command identifies existing work and only generates missing components if resumed.

## Quality Standards

- **Backend**: Standard Pytest fixtures and parametrization.
- **Frontend**: Component isolation using React Testing Library/Vitest.
- **Coverage**: Minimum 80% coverage with meaningful assertions.
- **Maintainability**: Clear naming and modular structure.
