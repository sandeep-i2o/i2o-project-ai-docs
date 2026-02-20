# i2o-feature-ai-docs
This repository hosts the features and documentation templates used for AI-accelerated development.

## Global Access Setup
The `.gemini/antigravity` directory contains custom workflows and skills designed for the Antigravity AI agent. To make these commands available globally across all your local repositories, you should copy this directory to your global Gemini configuration folder.

### Installation Steps
Run the following command from the root of this repository:
```bash
# Copy the antigravity configuration to your global home directory folder
cp -r .gemini/antigravity ~/.gemini/
```
Once copied, these workflows can be invoked in any project by using their respective slash commands (e.g., `/generate-prd`).

---

## Global Workflows
The following workflows are located in `.gemini/antigravity/global_workflows` and provide specialized AI assistance for different phases of the development lifecycle.

### 1. `/create-project`
*   **What it does**: Initializes the standard directory structure for a new feature project within this repository.
*   **Execution Steps**:
    1.  Invoke the command: `create_project --project_name "Your Project Name"`.
    2.  The agent creates a directory in `features/` with subfolders: `docs/design`, `docs/requirements`, and `docs/tests`.

### 2. `/generate-pid` (Project Brief)
*   **What it does**: Generates a comprehensive Project Brief (PID) based on initial ideas, market research, or brainstorming sessions.
*   **Execution Steps**:
    1.  Invoke `/generate-pid` and provide the `project-name`.
    2.  Select a mode: **Interactive** (step-by-step collaboration) or **YOLO** (instant full draft).
    3.  The agent gathers context (problem statement, goals, MVP scope) and generates `docs/brief.md`.

### 3. `/generate-prd` (Product Requirements Document)
*   **What it does**: Creates a detailed PRD including functional/non-functional requirements and user stories.
*   **Execution Steps**:
    1.  Invoke `/generate-prd` and specify the `project_name`.
    2.  Provide a Project Idea Document or the existing Project Brief as a foundation.
    3.  The agent generates `features/{{project_name}}/docs/requirements/prd.md` following standard templates.

### 4. `/generate-architecture`
*   **What it does**: Generates a fullstack architecture document covering tech stack, data models, API specs, and infrastructure.
*   **Execution Steps**:
    1.  Invoke `/generate-architecture` using the PRD and Project Brief as context.
    2.  The agent guides you through platform selection and tech stack decisions.
    3.  The agent produces a detailed `architecture.md` file and runs an automated quality checklist.

### 5. `/review-architecture`
*   **What it does**: Reviews an existing architecture document against the organizational Architect Checklist.
*   **Execution Steps**:
    1.  Invoke `/review-architecture` and point to the target architecture file.
    2.  The agent provides a PASS/FAIL report with specific recommendations for improvements.

### 6. `/generate-epics`
*   **What it does**: Converts the system architecture into actionable Jira Epics and User Stories using the Atlassian CLI (`acli`).
*   **Execution Steps**:
    1.  Invoke `/generate-epics --action create --type epic`.
    2.  The agent analyzes the architecture and creates Epics in your specified Jira project.
    3.  Repeat for `--type story` to populate those Epics with detailed User Stories.

### 7. `/generate-unit-tests`
*   **What it does**: Generates isolated unit tests for specific files, functions, or components.
*   **Execution Steps**:
    1.  Invoke `/generate-unit-tests <target_file>`.
    2.  The agent analyzes the code patterns and generates tests with appropriate mocks and fixtures.

### 8. `/generate-api-tests`
*   **What it does**: Generates Pytest-based integration tests for backend API services.
*   **Execution Steps**:
    1.  Invoke `/generate-api-tests <service_path>`.
    2.  The agent creates a structured test suite including response schema validation and status code checks.

### 9. `/generate-frontend-tests`
*   **What it does**: Generates unit and integration tests for React/Angular components using Vitest or Jest.
*   **Execution Steps**:
    1.  Invoke `/generate-frontend-tests <component_path>`.
    2.  The agent generates isolated tests focusing on UI interactions and state management.

### 10. `/generate-e2e-tests`
*   **What it does**: Generates end-to-end test scenarios using Playwright to validate complete user journeys.
*   **Execution Steps**:
    1.  Invoke `/generate-e2e-tests`.
    2.  The agent maps out critical user flows and generates automation scripts to test them across browsers.

---

## Directory Structure
- `features/`: Contains specific feature implementation designs and requirements.
- `knowledge/`: Shared technical documentation, database schemas, and project summaries.
- `utils/`: Helper tools (e.g., Markdown-to-PDF conversion).
- `.gemini/antigravity/`: Custom AI workflows and skills.
