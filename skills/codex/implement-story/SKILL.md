---
name: implement-story
description: Implement Jira issues end-to-end with an architecture-first workflow, specialized frontend/backend agent routing, branch discipline, testing/quality gates, and issue status updates. Use when asked to execute a Jira story/issue/comment into code changes while validating against architecture docs and Definition of Done.
---

# Implement Story

## Goal
Coordinate Jira issue implementation with architecture compliance, code quality, and clear delivery status.

## Command Interface
Use this skill for commands shaped like:

```bash
/implement-issue --issue 123 [--type issue|pr|comment] [--instruction "additional instructions"] [--help]
```

Inputs:
- `--issue` (required): Jira issue number or key
- `--type` (optional): `issue`, `pr`, or `comment`
- `--instruction` (optional): additional constraints/context that complement issue requirements

## Agent Routing

Select implementation path based on repository and scope:

- Frontend: use `frontend-developer` skill for Angular/TypeScript/UI work in `frontendapplication-i2o`
- Backend: use `backend-developer` skill for Java service work
- Full-stack: run frontend and backend streams in parallel when both are required

## Mandatory Rules
- Read relevant architecture docs before coding. Prioritize `/docs/design/architecture.md`; also inspect related files under `/docs/architecture/`.
- Do not implement before architecture verification.
- Create or update checkpoint log at `projects/{project_name}/progress.md` for resumability.
- Prefer updating existing implementation threads/comments over duplicating work.

## Workflow

### 1) Fetch and Classify Jira Context
1. Retrieve issue:
   ```bash
   acli jira workitem view {story_issue_id}
   ```
2. Auto-detect `--type` when omitted:
   - unresolved implementation comments present -> `comment`
   - otherwise -> `issue`
   - infer issue class (Epic/Feature/Story/Bug) from labels/title
3. Merge `--instruction` into plan as additive guidance (never override core issue requirements).
4. Record checkpoint in `projects/{project_name}/progress.md`.

### 2) Branch Strategy (First Implementation Step)
1. Check current branch.
2. If current branch already matches issue number pattern, continue.
3. Otherwise create a fresh feature branch:
   ```bash
   git checkout main && git pull
   git checkout -b feature/issue-{{ issue }}-{{ suffix }}
   ```

### 3) Architecture Verification

1. Identify relevant architecture docs using task type (data model/API/frontend/workflow/security/infrastructure).
2. Read selected docs before changing code.
3. Validate design decisions against documented patterns (models, APIs, components, tech stack).
4. Log consulted files in `projects/{project_name}/progress.md`.

Reference: [references/architecture-file-mapping.md](references/architecture-file-mapping.md)

### 4) Analysis and Implementation

1. Analyze Jira requirements and affected modules.
2. Map work to existing codebase patterns.
3. Implement backend/frontend changes as required.
4. Keep changes architecture-compliant and consistent with project conventions.

### 5) Testing Loop (Maximum 5 Iterations)

Run generate/fix/test cycles up to 5 times or stop earlier when all checks pass.

- Java services: write/run JUnit tests, validate with `mvn clean test`
- Python services: write/run tests with `unittest`
- UI changes: execute Playwright MCP validations

Never exceed 5 full loops.

### 6) Quality Gates

Run all relevant checks:
- lint and format tools
- type checks (if applicable)
- architecture alignment validation
- build sanity check: `mvn run compile`

### 7) Commit, Push, and Status Update

After passing quality gates:

```bash
git add .
git commit -m "feat: #{{ issue }} - Architecture-compliant implementation"
git push origin feature/issue-{{ issue }}-{{ suffix }}
```

Update issue status with comment:

```bash
acli jira workitem comment create --jql "project = IAC AND selectedIssue = {story_issue_id}" --body "✅ Architecture-compliant implementation completed

Branch: feature/issue-{{ issue }}-{{ suffix }}

Changes include:
- [Summary of changes made]
- Architecture files consulted: [List relevant files]
- Story DoD checklist validated: ✅

Ready for review."
```

### 8) Final Validation Checklist
Confirm all items before completion:
- architecture docs read before coding
- implementation matches architecture patterns
- tests written and passing
- lint/type/build checks pass
- story DoD checklist validated
- branch pushed and issue updated
- progress checkpoints captured

For UI changes, additionally require:
- Playwright MCP validation completed
- cross-browser coverage verified
- WCAG 2.1 AA accessibility checks pass
- visual regression checks pass
- responsive flows validated
- no console errors blocking release

Reference: [references/playwright-ui-validation.md](references/playwright-ui-validation.md)

## Error Handling
- Validate `acli` and GitHub authentication before starting.
- If architecture files are missing, search for nearest equivalent names and document assumptions.
- If branch creation or push fails, stop and report exact failure.
- Retry failed UI tests up to 3 times, then provide a failure summary and artifacts.
- If architecture compliance cannot be established, block implementation and report gaps.

## Success Criteria
1. Implementation aligns with architecture documentation.
2. Quality gates and tests pass.
3. UI validation passes for UI changes.
4. Jira/GitHub status is updated with clear traceability.
5. `projects/{project_name}/progress.md` includes resumable checkpoints.
