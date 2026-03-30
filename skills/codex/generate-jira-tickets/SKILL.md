---
name: generate-jira-tickets
description: Convert architecture documentation into Jira Epics and Stories, or update existing Jira issues, using Atlassian CLI (`acli`) and a two-agent model (charlie-conductor for strategy, bob-builder for implementation). Use when asked to generate Jira backlog items from architecture docs, enforce story template/checklist compliance, maintain Epic->Story hierarchy, and track checkpoint progress in project `progress.md`.
---

# Generate Jira Tickets

## Goal
Generate or update Jira Epics and Stories from architecture docs with consistent structure, strong acceptance criteria, and minimal duplication.

## Arguments
Validate and normalize these arguments before starting:

- `--action` (required): `create` or `update`
- `--type` (required): `epic` or `story`
- `--arch` (optional): architecture directory, default `docs/architecture/`
- `--issue-key` (required for `update`): Jira key like `ABC-456`
- `--parent-issue` (optional, recommended for story create): parent Epic key
- `--comment` (optional): update instructions or comment body
- `--dry-run` (optional): preview only, do not mutate Jira
- `--project` (optional): Jira project key; if missing, auto-detect
- `--local` (optional): default `no`; when `yes`, write drafts under `{project_dir}/tickets/` instead of calling Jira

Reject invalid combinations:
- Require `--issue-key` when `--action update`.
- Require a parent Epic for story creation unless inferable from `--issue-key` context.
- Do not call `acli` when `--local yes`.

## Required Standards
Always enforce these constraints:

- Read and apply story template from `./templates/story-tmpl.yaml`.
- Validate story draft against checklist in this order:
  1. `./checklist/story-draft-checklist.md`
  2. `./.aiccelerate/checklist/story-draft-checklist.md`
- Create or update `{project_dir}/progress.md` at every checkpoint.
- Prefer updates and reuse over creating duplicates.

Load detailed output templates from [references/issue-templates.md](references/issue-templates.md).
Load command syntax from [references/acli-reference.md](references/acli-reference.md).

## Workflow

### 1) Preflight
1. Detect project root (`{project_dir}`).
2. Create `progress.md` if missing; append a timestamped "started" entry.
3. If not local mode, verify auth with `acli whoami`.
4. Resolve architecture directory from `--arch` or `docs/architecture/`.

### 2) Architecture Discovery and File Selection
1. List candidate architecture files:
   ```bash
   rg --files "${ARCH_DIR}" -g '*.md'
   ```
2. Select 2-3 files with highest relevance:
   - For epics: `high-level-architecture.md`, `components.md`, `tech-stack.md`
   - For stories: `coding-standards.md`, `testing-strategy.md`, component-level specs
3. Record selected files in `progress.md`.

### 3) Two-Agent Analysis
Run both lenses on the selected architecture files.

Charlie-Conductor (strategy):
- Identify system boundaries and business capabilities.
- Map technical domains and integration points.
- Define implementation sequence and cross-team coordination.
- Surface risks and delivery strategy.

Bob-Builder (execution):
- Validate stack choices and alternatives.
- Estimate implementation effort and complexity.
- Confirm dependencies, testing scope, and deployment path.
- Highlight technical debt and timeline risk.

Summarize both outputs before issue generation.

### 4) Project Detection
Resolve project key in this order:
1. Use `--project` if provided.
2. Extract from `--issue-key` or `--parent-issue` prefix when available.
3. If still unknown and not local mode, query Jira projects and infer a single viable key from context.
4. If multiple candidates remain, stop and request explicit project key.

Optional check for existing epics:
```bash
acli jira workitem search --jql "project = ${PROJECT_KEY} AND issueType=Epic"
```

### 5) Action: Create
Before creating any issue:
- Search for duplicates via JQL (`summary`, component, labels, parent).
- Reuse/update matching issues instead of creating new ones.

Epic creation:
1. Compose description using the "Epic format" in `references/issue-templates.md`.
2. Include business value (Charlie), technical feasibility (Bob), dependencies, readiness, and story breakdown.
3. Create Epic unless `--dry-run`:
   ```bash
   acli jira workitem create \
     --project "${PROJECT_KEY}" \
     --type "Epic" \
     --summary "${EPIC_TITLE}" \
     --description "${EPIC_DESCRIPTION}" \
     --priority "${PRIORITY}"
   ```

Story creation:
1. Compose story using template/checklist requirements and the "Story format" in `references/issue-templates.md`.
2. Keep implementation to a 1-3 day vertical slice.
3. Mark checklist result as `READY`, `NEEDS_REVISION`, or `BLOCKED`.
4. Create Story unless `--dry-run`:
   ```bash
   acli jira workitem create \
     --project "${PROJECT_KEY}" \
     --type "Story" \
     --summary "${STORY_TITLE}" \
     --description "${STORY_DESCRIPTION}" \
     --parent "${EPIC_KEY}" \
     --priority "${PRIORITY}" \
     --labels "${LABELS}" \
     --components "${COMPONENTS}"
   ```

Local mode (`--local yes`):
- Write artifacts under:
  - `{project_dir}/tickets/epics/*.md`
  - `{project_dir}/tickets/stories/*.md`
  - `{project_dir}/tickets/tasks/*.md` (only when explicitly required)
- Keep the same template/checklist rules.
- Add local hierarchy references (epic->story) in file frontmatter or headings.

### 6) Action: Update
1. Fetch current issue:
   ```bash
   acli jira workitem get --issue "${ISSUE_KEY}"
   ```
2. Apply update instructions from `--comment` and/or architecture deltas.
3. If updating an Epic, propagate necessary scope changes to linked Stories.
4. Preview in `--dry-run`; otherwise execute updates:
   ```bash
   acli jira workitem update \
     --issue "${ISSUE_KEY}" \
     --summary "${NEW_SUMMARY}" \
     --description "${NEW_DESCRIPTION}"
   ```
5. Add comment when provided:
   ```bash
   acli jira workitem comment add \
     --issue "${ISSUE_KEY}" \
     --body "${COMMENT_BODY}"
   ```

### 7) Linking and Hierarchy
Maintain clean Epic->Story relationships and related links:

```bash
acli jira workitem update --issue "${STORY_KEY}" --parent "${EPIC_KEY}"
acli jira workitem link add --issue "${ISSUE_1}" --target "${ISSUE_2}" --type "relates to"
```

### 8) Progress Tracking and Final Output
1. Update `progress.md` after each checkpoint:
   - selected architecture files
   - project key decision
   - created/updated issue keys
   - link operations
   - dry-run vs applied
2. Produce final summary using "Generation Complete" format from `references/issue-templates.md`.

## Guardrails
- Do not duplicate stories/tasks when suitable issues already exist.
- Create Epics before Stories when both are needed.
- Keep stories self-contained and testable.
- Preserve traceability to architecture references.
- Fail fast on auth/access errors, invalid keys, or missing parent Epic.
