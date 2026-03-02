---
description: Generate or update Jira epics/stories from architecture docs with progress tracking
---

Goal
Generate or update Jira Epics and Stories from architecture docs with consistent structure, strong acceptance criteria, and minimal duplication.

Arguments
Validate and normalize these arguments before starting:

--action (required): create or update
--type (required): epic or story
--arch (optional): architecture directory, default docs/architecture/
--issue-key (required for update): Jira key like ABC-456
--parent-issue (optional, recommended for story create): parent Epic key
--comment (optional): update instructions or comment body
--dry-run (optional): preview only, do not mutate Jira
--project (optional): Jira project key; if missing, auto-detect
--local (optional): default no; when yes, write drafts under {project_dir}/tickets/ instead of calling Jira
Reject invalid combinations:

Require --issue-key when --action update.
Require a parent Epic for story creation unless inferable from --issue-key context.
Do not call acli when --local yes.
Required Standards
Always enforce these constraints:

Read and apply story template from ./templates/story-tmpl.yaml.
Validate story draft against checklist in this order:
./checklist/story-draft-checklist.md
./.aiccelerate/checklist/story-draft-checklist.md
Create or update {project_dir}/progress.md at every checkpoint.
Prefer updates and reuse over creating duplicates.
Load detailed output templates from issue-templates.md.
Load command syntax from acli-reference.md.

Workflow
1) Preflight
Detect project root ({project_dir}).
Create progress.md if missing; append a timestamped "started" entry.
If not local mode, verify auth with acli whoami.
Resolve architecture directory from --arch or docs/architecture/.
2) Architecture Discovery and File Selection
List candidate architecture files:
rg --files "${ARCH_DIR}" -g '*.md'
Select 2-3 files with highest relevance:
For epics: high-level-architecture.md, components.md, tech-stack.md
For stories: coding-standards.md, testing-strategy.md, component-level specs
Record selected files in progress.md.
3) Two-Agent Analysis
Run both lenses on the selected architecture files.

Charlie-Conductor (strategy):

Identify system boundaries and business capabilities.
Map technical domains and integration points.
Define implementation sequence and cross-team coordination.
Surface risks and delivery strategy.
Bob-Builder (execution):

Validate stack choices and alternatives.
Estimate implementation effort and complexity.
Confirm dependencies, testing scope, and deployment path.
Highlight technical debt and timeline risk.
Summarize both outputs before issue generation.

4) Project Detection
Resolve project key in this order:

Use --project if provided.
Extract from --issue-key or --parent-issue prefix when available.
If still unknown and not local mode, query Jira projects and infer a single viable key from context.
If multiple candidates remain, stop and request explicit project key.
Optional check for existing epics:

acli jira workitem search --jql "project = ${PROJECT_KEY} AND issueType=Epic"
5) Action: Create
Before creating any issue:

Search for duplicates via JQL (summary, component, labels, parent).
Reuse/update matching issues instead of creating new ones.
Epic creation:

Compose description using the "Epic format" in references/issue-templates.md.
Include business value (Charlie), technical feasibility (Bob), dependencies, readiness, and story breakdown.
Create Epic unless --dry-run:
acli jira workitem create \
  --project "${PROJECT_KEY}" \
  --type "Epic" \
  --summary "${EPIC_TITLE}" \
  --description "${EPIC_DESCRIPTION}" \
  --priority "${PRIORITY}"
Story creation:

Compose story using template/checklist requirements and the "Story format" in references/issue-templates.md.
Keep implementation to a 1-3 day vertical slice.
Mark checklist result as READY, NEEDS_REVISION, or BLOCKED.
Create Story unless --dry-run:

acli jira workitem create \
  --project "${PROJECT_KEY}" \
  --type "Story" \
  --summary "${STORY_TITLE}" \
  --description "${STORY_DESCRIPTION}" \
  --parent "${EPIC_KEY}" \
  --priority "${PRIORITY}" \
  --labels "${LABELS}" \
  --components "${COMPONENTS}"
Local mode (--local yes):

Write artifacts under:
{project_dir}/tickets/epics/*.md
{project_dir}/tickets/stories/*.md
{project_dir}/tickets/tasks/*.md (only when explicitly required)
Keep the same template/checklist rules.
Add local hierarchy references (epic->story) in file frontmatter or headings.

6) Action: Update
Fetch current issue:
acli jira workitem get --issue "${ISSUE_KEY}"
Apply update instructions from --comment and/or architecture deltas.
If updating an Epic, propagate necessary scope changes to linked Stories.
Preview in --dry-run; otherwise execute updates:
acli jira workitem update \
  --issue "${ISSUE_KEY}" \
  --summary "${NEW_SUMMARY}" \
  --description "${NEW_DESCRIPTION}"
Add comment when provided:
acli jira workitem comment add \
  --issue "${ISSUE_KEY}" \
  --body "${COMMENT_BODY}"

7) Linking and Hierarchy
Maintain clean Epic->Story relationships and related links:

acli jira workitem update --issue "${STORY_KEY}" --parent "${EPIC_KEY}"
acli jira workitem link add --issue "${ISSUE_1}" --target "${ISSUE_2}" --type "relates to"

8) Progress Tracking and Final Output

Update progress.md after each checkpoint:
selected architecture files
project key decision
created/updated issue keys
link operations
dry-run vs applied
Produce final summary using "Generation Complete" format from references/issue-templates.md.

Guardrails
Do not duplicate stories/tasks when suitable issues already exist.
Create Epics before Stories when both are needed.
Keep stories self-contained and testable.
Preserve traceability to architecture references.
Fail fast on auth/access errors, invalid keys, or missing parent Epic.
Each story should be detailed and include the project_name module in which changes will be done. e.g. i2o-admin, i2o-reseller etc. as per architecture document.