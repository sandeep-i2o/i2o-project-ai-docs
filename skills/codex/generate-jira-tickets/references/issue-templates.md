# Issue Templates

Use these templates for generated content.

## Epic Format

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

## Story Format

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
Against `./checklist/story-draft-checklist.md` (or `./.aiccelerate/checklist/story-draft-checklist.md`):

### Goal and Context Clarity
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

## Generation Complete Format

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
1. Review in Jira project board
2. Assign team members
3. Estimate story points using planning poker
4. Add to sprint
```
