# Atlassian CLI Quick Reference

## Authentication

```bash
acli login
acli whoami
```

## Project Operations

```bash
acli jira project list
acli jira project get --project {{ project_key }}
```

## Work Item Operations

```bash
acli jira workitem list --project {{ project_key }}
acli jira workitem list --project {{ project_key }} --type Epic
acli jira workitem list --project {{ project_key }} --type Story
acli jira workitem list --project {{ project_key }} --jql "status = 'To Do'"

acli jira workitem get --issue {{ issue_key }}

acli jira workitem create \
  --project {{ project_key }} \
  --type Epic \
  --summary "{{ summary }}" \
  --description "{{ description }}"

acli jira workitem create \
  --project {{ project_key }} \
  --type Story \
  --summary "{{ summary }}" \
  --description "{{ description }}" \
  --parent "{{ epic_key }}"

acli jira workitem update \
  --issue {{ issue_key }} \
  --summary "{{ new_summary }}"

acli jira workitem transition \
  --issue {{ issue_key }} \
  --transition "In Progress"

acli jira workitem assign \
  --issue {{ issue_key }} \
  --assignee "{{ user_email }}"

acli jira workitem comment add \
  --issue {{ issue_key }} \
  --body "{{ comment }}"

acli jira workitem link add \
  --issue {{ source_key }} \
  --target {{ target_key }} \
  --type "blocks"
```

## Sprint Operations

```bash
acli jira sprint list --board {{ board_id }}
acli jira sprint add --sprint {{ sprint_id }} --issue {{ issue_key }}
```

## JQL Examples

```bash
acli jira workitem list --jql "project = {{ key }} AND type = Epic"
acli jira workitem list --jql "project = {{ key }} AND type = Story"
acli jira workitem list --jql "project = {{ key }} AND status != Done"
acli jira workitem list --jql "assignee = currentUser() AND sprint in openSprints()"
```

## Error Handling Checklist

- Validate authentication (`acli whoami`).
- Validate project access permissions.
- Check duplicates with JQL before create.
- Confirm parent Epic exists before linking stories.
- Track created keys to support cleanup/rollback.
- If expected architecture files are missing, choose the closest matching files and record the assumption.
