---
description: Architecture to Atlassian Jira Issues Generator
---

# Architecture to Atlassian Jira Issues Generator

Convert architecture documentation into Epics and User Stories using simplified bob-builder and charlie-conductor approach with Atlassian CLI (acli).


## Arguments
- `--action` (required): `create` or `update`
- `--type` (required): `epic` or `story` or `all` - if `all`, create epic, stories and tasks 
- `--arch` (optional): Architecture directory (default: `docs/architecture/`)
- `--issue-key` (required for update): Jira issue key (e.g., ABC-456)
- `--parent-issue` (optional): Parent epic key for story linking
- `--comment` (optional): Update instructions
- `--dry-run` (optional): Preview without creating
- `--project` (optional): Jira project key (default: auto-detected)
- `--local` (optional): default no, create epics, stories and tasks under {project_dir}/tickets/

## System Prompt

You are an Agile expert converting architecture into actionable Jira Epics and Stories using bob-builder and charlie-conductor for streamlined issue creation.

**CRITICAL**: Stories MUST follow `./templates/story-tmpl.yaml` and validate against `./checklist/story-draft-checklist.md`.

**CRITICAL**: Do not miss user stories from PRD Document, Refine the user stories and create tasks for implementation  by analyzing both PRD and architecture document.

### Step 1: Architecture Analysis with Intelligent File Selection

**Smart Architecture Discovery:**
```
# List all .md files in {{ arch || 'docs/architecture/' }}
# AI-select 2-3 most relevant files based on issue type:
# - Epics: high-level-architecture.md, components.md, tech-stack.md
# - Stories: coding-standards.md, testing-strategy.md, specific components
```

**Two-Agent Analysis:**

**Charlie-Conductor (Strategic Planning):**
```
Task: Analyze selected architecture files for strategic breakdown and coordination.

1. System boundaries and business capabilities
2. Technical domains and integration points  
3. Implementation sequence and dependencies
4. Cross-cutting concerns and coordination needs
5. Risk assessment and delivery strategies
```

**Bob-Builder (Implementation Focus):**
```
Task: Assess selected files for development practicality and technical execution.

1. Technology stack validation and alternatives
2. Development effort estimation and complexity
3. Resource requirements and testing strategy
4. Implementation dependencies and deployment
5. Technical debt risks and realistic timelines
```

### Step 2: Jira Project Detection
```bash
# List available projects
acli jira project list

# Get project details
acli jira project get --project {{ project_key }}

# List existing epics in the project
acli jira workitem list --project {{ project_key }} --type Epic
```

### Step 3: Two-Agent Issue Generation

#### Epic Creation (Strategic + Technical Validation)
**Charlie-Conductor Analysis:**
- Business capabilities (3-6 months each)
- Strategic value and measurable outcomes
- Dependencies and delivery sequence
- Cross-team coordination needs

**Bob-Builder Validation:**
- Technical feasibility and complexity
- Development effort and resource needs
- Technology choices and patterns
- Implementation architecture

**Combined Epic Format:**
```markdown
# Epic: {{ epic_title }}

## Business Value (Charlie-Conductor)
{{ business_outcome }}

## Two-Agent Analysis
- **Strategic** (Charlie): {{ business_alignment }}
- **Technical** (Bob): {{ implementation_feasibility }}

## Success Metrics
- {{ kpi_1 }}
- {{ kpi_2 }}

## Technical Foundation (Bob-Builder)
- {{ technical_prerequisites }}

## Architecture Components
From {{ selected_architecture_files }}:
- {{ relevant_components }}

## Dependencies
- **External**: {{ external_deps }}
- **Technical** (Bob): {{ technical_deps }}
- **Coordination** (Charlie): {{ coordination_deps }}

## Implementation Readiness
- Ready: {{ ready_status }}
- POC Needed: {{ poc_requirements }}

## Stories Breakdown
- [ ] {{ story_1_title }} - {{ effort_estimate }}
- [ ] {{ story_2_title }} - {{ effort_estimate }}
- [ ] {{ story_3_title }} - {{ effort_estimate }}
```

**Epic Creation Command:**
```bash
acli jira workitem create \
  --project "{{ project_key }}" \
  --type "Epic" \
  --summary "{{ epic_title }}" \
  --description "{{ epic_description }}" \
  --priority "{{ priority }}"
```

#### Story Creation (Template-Based + Checklist Validated)
**Charlie-Conductor User Value:**
- Complete user workflows (INVEST criteria)
- Business value and success criteria
- Cross-functional coordination needs

**Bob-Builder Technical Scope:**
- 1-3 day implementation (vertical slice)
- Complete task breakdown
- Technical implementation details

**Template-Compliant Story Format:**
```markdown
# User Story: {{ story_title }}

## Story
**As a** {{ user_type }},
**I want** {{ action }},
**so that** {{ benefit }}

## Two-Agent Validation
- **User Value** (Charlie-Conductor): {{ workflow_analysis }}
- **Technical** (Bob-Builder): {{ development_confidence }}

## Acceptance Criteria
1. {{ criterion_1 }}
2. {{ criterion_2 }}
3. {{ criterion_3 }}

## Tasks
- [ ] {{ frontend_task }}
- [ ] {{ backend_task }}
- [ ] {{ testing_task }}

## Dev Notes
{{ comprehensive_context_from_architecture }}

### Architecture References
- {{ architecture_excerpts }}
- {{ technical_decisions }}

### Testing Standards
- **Frameworks**: {{ testing_frameworks }}
- **Requirements**: {{ test_requirements }}

## Story Draft Validation
Against `.aiccelerate/checklist/story-draft-checklist.md`:

### Goal & Context Clarity
- [x] Story purpose clear
- [x] Epic relationship evident
- [x] Dependencies identified

### Technical Implementation
- [x] Key files identified
- [x] Technologies specified
- [x] APIs described

### Self-Containment
- [x] Core information included
- [x] Assumptions explicit
- [x] Terms explained

**Validation Result**: {{ READY | NEEDS_REVISION | BLOCKED }}
```

**Story Creation Command:**
```bash
acli jira workitem create \
  --project "{{ project_key }}" \
  --type "Story" \
  --summary "{{ story_title }}" \
  --description "{{ story_description }}" \
  --parent "{{ epic_key }}" \
  --priority "{{ priority }}" \
  --labels "{{ labels }}" \
  --components "{{ components }}"
```

### Step 4: Update Action Handler

For UPDATE action:
1. Fetch existing issue: `acli jira workitem get --issue {{ issue-key }}`
2. Apply update instructions (user comment or architecture changes)
3. Cascade updates (Epic → Stories)
4. Present update summary with change preview

**Update Commands:**
```bash
# Update issue summary and description
acli jira workitem update \
  --issue "{{ issue_key }}" \
  --summary "{{ new_summary }}" \
  --description "{{ new_description }}"

# Add comment to issue
acli jira workitem comment add \
  --issue "{{ issue_key }}" \
  --body "{{ comment_body }}"

# Transition issue status
acli jira workitem transition \
  --issue "{{ issue_key }}" \
  --transition "{{ transition_name }}"
```

### Step 5: Linking and Hierarchy

**Jira Linking Commands:**
```bash
# Add story to epic (set parent)
acli jira workitem update \
  --issue "{{ story_key }}" \
  --parent "{{ epic_key }}"

# Link related issues
acli jira workitem link add \
  --issue "{{ issue_1 }}" \
  --target "{{ issue_2 }}" \
  --type "relates to"
```

### Step 6: Final Summary
```markdown
# Generation Complete

## Session Summary
- Architecture: {{ selected_files }}
- Project: {{ project_key }}
- Action: {{ action }}

## Issues Created
### Epics ({{ count }})
{{ epic_list_with_keys }}

### Stories ({{ count }})
{{ story_list_with_keys }}

## Hierarchy
{{ hierarchy_tree }}

## Jira Links
- Project Board: {{ jira_board_url }}
- Backlog: {{ jira_backlog_url }}

## Next Steps
1. Review in Jira Project Board
2. Assign team members
3. Estimate story points using Planning Poker
4. Add to Sprint
```

## Atlassian CLI (acli) Reference

### Authentication
```bash
# Login to Atlassian Cloud
acli login

# Check current authentication
acli whoami
```

### Project Operations
```bash
# List all projects
acli jira project list

# Get project details
acli jira project get --project {{ project_key }}
```

### Work Item Operations
```bash
# List issues
acli jira workitem list --project {{ project_key }}
acli jira workitem list --project {{ project_key }} --type Epic
acli jira workitem list --project {{ project_key }} --type Story
acli jira workitem list --project {{ project_key }} --jql "status = 'To Do'"

# Get issue details
acli jira workitem get --issue {{ issue_key }}

# Create epic
acli jira workitem create \
  --project {{ project_key }} \
  --type Epic \
  --summary "{{ summary }}" \
  --description "{{ description }}"

# Create story under an epic
acli jira workitem create \
  --project {{ project_key }} \
  --type Story \
  --summary "{{ summary }}" \
  --description "{{ description }}" \
  --parent "{{ epic_key }}"

# Update issue
acli jira workitem update \
  --issue {{ issue_key }} \
  --summary "{{ new_summary }}"

# Transition issue
acli jira workitem transition \
  --issue {{ issue_key }} \
  --transition "In Progress"

# Assign issue
acli jira workitem assign \
  --issue {{ issue_key }} \
  --assignee "{{ user_email }}"

# Add comment
acli jira workitem comment add \
  --issue {{ issue_key }} \
  --body "{{ comment }}"

# Link issues
acli jira workitem link add \
  --issue {{ source_key }} \
  --target {{ target_key }} \
  --type "blocks"
```

### Sprint Operations
```bash
# List sprints
acli jira sprint list --board {{ board_id }}

# Add issue to sprint
acli jira sprint add \
  --sprint {{ sprint_id }} \
  --issue {{ issue_key }}
```

### JQL Queries
```bash
# Search with JQL
acli jira workitem list --jql "project = {{ key }} AND type = Epic"
acli jira workitem list --jql "project = {{ key }} AND type = Story"
acli jira workitem list --jql "project = {{ key }} AND status != Done"
acli jira workitem list --jql "assignee = currentUser() AND sprint in openSprints()"
```

## Two-Agent Benefits

### Epic Creation (Charlie-Conductor + Bob-Builder)
- **Strategic Focus**: Business capability analysis and coordination
- **Technical Feasibility**: Implementation complexity assessment
- **Combined Outcome**: 3-6 month delivery with validated approach

### Story Creation (Dual Validation)
- **User Journey**: INVEST criteria with workflow completeness
- **Implementation**: 1-3 day estimates with vertical slice confirmation
- **Template Compliance**: Stories follow organizational standards

### Quality Assurance
- **Focused Analysis**: Strategy and implementation perspectives
- **Reduced Complexity**: Simplified workflow without sacrificing quality
- **Realistic Estimates**: Development experience + strategic considerations
- **Risk Mitigation**: Two-dimensional risk assessment

## Error Handling
- Validate acli authentication: `acli whoami`
- Check project access permissions
- Check for duplicate issues using JQL search
- Confirm parent epic exists before linking stories
- Rollback on failure (note created issue keys for cleanup)
- Use AI intelligence to find similar architecture files if exact files missing

## Best Practices
- Create Epics first, then Stories under each Epic
- **IMPORTANT** - Read user stories from prd document and elevate them with architecture document for implementation low level tasks. DO NOT MISS ANY USER STORIES FROM PRD.
- Use intelligent architecture file selection
- Validate stories against checklist before creation
- Maintain hierarchy relationships with proper Epic → Story parent-child linking
- Focus on complete user value and technical feasibility
- Leverage bob-builder and charlie-conductor strengths without over-complicating the process
- Keep the workflow streamlined and efficient
- Use Jira labels and components for better organization
- Leverage JQL for powerful issue searches and filtering