# Architecture File Mapping

Use this map to pick high-signal architecture files before coding.

| Task Type | Common Files to Check |
|---|---|
| Data Model | `data-models.md`, `database-schema.md`, `entity-relationships.md` |
| API | `api-specification.md`, `external-apis.md`, `endpoints.md` |
| Frontend | `components.md`, `ui-architecture.md`, `frontend-patterns.md` |
| Workflow | `core-workflows.md`, `business-logic.md`, `process-flows.md` |
| Infrastructure | `deployment.md`, `infrastructure.md`, `system-architecture.md` |
| Security | `security.md`, `authentication.md`, `authorization.md` |
| All Tasks | `index.md`, `introduction.md`, `overview.md`, `readme.md` |

Selection guidance:
- Prefer `/docs/design/architecture.md` first when present.
- Then load only the minimum additional files needed for the current task.
- If exact names do not exist, choose closest semantic matches and record the decision.
