---
description: Generate Frontend Tests
---

# Generate Frontend Tests Command

**Usage:** `/generate-frontend-tests <target> [options]`

## Description

Generates frontend integration tests for React components, focusing on component interactions, state management, and API integration.

## Arguments

### Required

- `<target>` - The target component or feature to generate tests for.
- `<path>` - Target path where the frontend tests will be saved.

### Options

- `--resume` - Resume test generation from existing task_list.md.
- `--check-completeness` - Check completion percentage and show pending items.
- `--validate` - Validate that generated tests are accurate and follow standards.
- `--mocks` - Generate API mocking infrastructure for components.
- `--async` - Handle complex async operation testing.

## Examples

```bash
# Generate frontend tests for an upload component
/generate-frontend-tests src/frontend/components/DocumentUpload.tsx
# Creates: frontend/tests/integration/*.test.js, run-frontend-tests.sh
```

## Generated File Structure

```
tests/frontend/
├── test_*.test.js              # Frontend test files
├── run-frontend-tests.sh       # Executable runner script
├── utils/                      # Reporting utilities
└── reports/                    # Executive and Technical reports
```

## Quality Standards

- **Component Isolation**: React Testing Library patterns with proper mocking.
- **API Integration**: Standardized API service mocking and integration testing.
- **Async Handling**: Proper use of `waitFor` and async operation handling.
- **Maintainability**: Clear naming, proper documentation, and modular structure.

## Implementation Workflow

1. **Analysis**: Parse component structure, props, and external API calls.
2. **Strategy**: Define user interaction paths and state transitions.
3. **Creation**: Generate test files with setup, mock services, and assertions.
4. **Validation**: Validate against accessibility and quality checklists.
