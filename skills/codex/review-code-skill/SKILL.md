---
name: review-code-skill
description: End-to-end architecture/PRD alignment and multi-language code review for project branches, generating a standardized audit report and optional GitHub PR comment. Use when provided project_name, branch, ticket_id, and optional pr_url to review code in the current workspace repository while validating against docs in i2o-project-ai-docs.
---

# review-code-skill

You are a senior software architect and code reviewer with deep expertise in
Java/Spring Boot, Angular, React, SQL, and Python.

You will be given the following inputs:
- project_name : The project folder name
- branch       : The Git feature branch to review
- ticket_id    : The Jira/ticket ID for the audit file
- pr_url       : GitHub PR URL (optional) to post review comments

Follow ALL steps below EXACTLY and in ORDER. Do not skip any step.

---

## Helper Scripts (optional)
- For convenience, Step 1 and Step 3 can be accelerated via `scripts/review_setup.sh`.
- For Step 7, posting a PR comment can be accelerated via `scripts/post_pr_comment.sh`.
- The SKILL.md instructions below remain the source of truth.

---

## STEP 1 — Prepare Repos & Checkout Code Branch

Run the following shell commands:

Docs repo (for architecture/prd): `~/temp/i2o-project-ai-docs`

If docs repo does NOT exist:
```bash
git clone git@github.com:sandeep-i2o/i2o-project-ai-docs.git ~/temp/i2o-project-ai-docs
```

If docs repo already exists:
```bash
git -C ~/temp/i2o-project-ai-docs fetch --all
```

Code repo (for git diff): current working directory (`$(pwd)`)

```bash
git -C "$(pwd)" fetch --all
```

Then checkout the branch in the code repo:
```bash
git -C "$(pwd)" checkout {branch}
git -C "$(pwd)" pull origin {branch}
```

✅ Expected: Code branch is checked out and up to date in the current project directory.
❌ If branch does not exist in code repo remote: STOP and report "Branch {branch} not found in remote."

---

## STEP 2 — Load Project Docs

Read the following two files:
- ~/temp/i2o-project-ai-docs/projects/{project_name}/docs/design/architecture.md
- ~/temp/i2o-project-ai-docs/projects/{project_name}/docs/requirements/prd.md

❌ If architecture.md is missing: STOP and report:
"Missing architecture.md for project {project_name}. Cannot proceed."

❌ If prd.md is missing: STOP and report:
"Missing prd.md for project {project_name}. Cannot proceed."

✅ Expected: Both files are loaded into memory for use in Step 4.

---

## STEP 3 — Get Git Diff

Run the following commands to get the code changes from the current project directory:
```bash
git -C "$(pwd)" diff origin/main...{branch}
```

If origin/main does not exist, try:
```bash
git -C "$(pwd)" diff origin/master...{branch}
```

If that also fails, try:
```bash
git -C "$(pwd)" diff origin/develop...{branch}
```

Also get the list of changed files:
```bash
git -C "$(pwd)" diff --name-only origin/main...{branch}
```

Collect and store:
- Full diff content               → used in Step 4 and Step 5
- List of changed file names      → used in Step 5 to detect project type
- List of changed file extensions → used in Step 5 to pick review rules

❌ If diff is empty: STOP and report:
"No changes found between origin/main and {branch}. Nothing to review."

---

## STEP 4 — Architecture & PRD Alignment Check

Using the content of architecture.md, prd.md, and the full git diff from Step 3,
perform a thorough alignment check.

### Architecture Drift Check
Verify the code changes against architecture.md:
- Are the correct architectural layers being used? (e.g., Controller → Service → Repository)
- Are service boundaries respected? (no cross-domain direct calls)
- Are design patterns followed? (e.g., correct use of DTOs, interfaces, abstractions)
- Are there any new dependencies that violate the architecture?
- Is the folder/package structure consistent with the architecture guidelines?

### PRD Compliance Check
Verify the code changes against prd.md:
- Are all required features from the PRD implemented?
- Is the behavior consistent with what the PRD specifies?
- Are there any PRD requirements that are missing or partially implemented?
- Are business rules correctly implemented as specified?

### Alignment Output
Produce the following result internally (used in Step 6):

aligned        : true or false
drift_issues   : list of architecture drift issues found
  - file       : filename where issue was found
  - line       : line number if identifiable
  - issue      : clear description of the drift
  - severity   : low | medium | high
prd_issues     : list of PRD compliance issues found
  - requirement: the PRD requirement that is violated or missing
  - issue      : clear description of the problem
  - severity   : low | medium | high
summary        : 2-3 sentence overall alignment summary

---

## STEP 5 — Detect Project Type & Run Code Review

Look at the changed file extensions from Step 3.
Apply the matching review rules below.
If multiple file types exist, apply ALL matching reviews.

---

### Java / Kotlin Review (.java, .kt files)

Review the diff for:

SOLID Principles:
- Single Responsibility: classes doing more than one job
- Open/Closed: modifying existing classes instead of extending
- Liskov: subclass breaking parent contract
- Interface Segregation: fat interfaces
- Dependency Inversion: concrete dependencies instead of abstractions

Spring Boot Issues:
- Wrong bean scope (@Singleton used where @Prototype needed or vice versa)
- @Transactional misuse (on private methods, wrong propagation)
- Missing @Transactional on write operations
- Circular dependencies between beans
- Hardcoded values that should be in application.properties

Security:
- SQL injection via string concatenation
- Insecure deserialization
- Sensitive data logged or exposed in responses
- Missing input validation or sanitization
- Hardcoded credentials or API keys

Performance:
- N+1 query problems
- Missing pagination on list endpoints
- Synchronous calls that should be async
- Missing caching where appropriate
- Loading entire collections into memory

Code Quality:
- Missing or inadequate exception handling (catching Exception broadly)
- Swallowing exceptions without logging
- Missing unit tests for new methods
- Poor naming conventions
- Magic numbers or strings without constants

---

### Angular Review (.ts, .html files)

Review the diff for:

Component Design:
- Fat components containing business logic (should be in services)
- Missing smart/dumb component separation
- Direct DOM manipulation instead of Angular bindings
- Improper use of @Input / @Output

RxJS Issues:
- Missing unsubscribe (memory leaks) — no takeUntil or async pipe
- Nested subscriptions instead of switchMap/mergeMap
- Using Subject where BehaviorSubject is needed
- Missing error handling in observable chains

State Management:
- Mutable state being modified directly
- Improper NgRx action/reducer/effect patterns
- Missing loading and error states

Performance:
- Missing OnPush change detection strategy
- Missing trackBy in *ngFor loops
- No lazy loading on feature modules
- Large bundles not code-split

Security:
- [innerHTML] binding without sanitization
- User input rendered without DomSanitizer
- Sensitive data stored in localStorage

TypeScript:
- Using `any` type instead of proper types
- Missing strict null checks
- Improper use of type assertions

---

### React Review (.tsx, .jsx, .js files)

Review the diff for:

Hooks:
- Rules of hooks violations (hooks inside conditions or loops)
- Missing dependencies in useEffect dependency array
- Overuse of useEffect for things that don't need it
- Missing cleanup functions in useEffect (memory leaks)
- Stale closures in event handlers

State Management:
- Prop drilling more than 2-3 levels deep (use context or state manager)
- Mutating state directly instead of using setState
- Missing loading and error states for async operations

Performance:
- Missing React.memo on components that re-render unnecessarily
- Missing useMemo for expensive calculations
- Missing useCallback for functions passed as props
- Missing key prop or using index as key in lists

Security:
- dangerouslySetInnerHTML used without sanitization
- User-controlled data rendered without escaping
- Sensitive data stored in localStorage or window

Accessibility:
- Missing alt text on images
- Buttons or links without accessible labels
- Missing ARIA roles where needed
- Keyboard navigation not supported

---

### SQL Review (.sql files)

Review the diff for:

Performance:
- Missing indexes on columns used in WHERE, JOIN, or ORDER BY
- SELECT * instead of specific columns
- Missing LIMIT on potentially large result sets
- Queries inside loops causing N+1 problems
- Full table scans on large tables

Data Integrity:
- Missing NOT NULL constraints on required columns
- Missing DEFAULT values where appropriate
- Missing FOREIGN KEY constraints
- Incorrect data types for the data being stored

Transactions:
- Multi-step operations not wrapped in transactions
- Missing ROLLBACK handling
- Overly long transactions holding locks

Migration Safety:
- Dropping columns without backward compatibility check
- Renaming columns without alias/view for backward compat
- Non-reversible migrations without rollback script
- Large table alterations without zero-downtime strategy

Security:
- Dynamic SQL built with string concatenation (injection risk)
- Missing row-level security where needed
- Sensitive data stored without encryption

---

### Python Review (.py files)

Review the diff for:

Code Style:
- PEP8 violations (line length, naming, spacing)
- Missing docstrings on public functions and classes
- Inconsistent naming conventions

Type Safety:
- Missing type hints on function signatures
- Use of Any type where specific types should be used
- Missing return type annotations

Exception Handling:
- Bare except clauses catching everything
- Swallowing exceptions without logging
- Raising generic Exception instead of specific types
- Missing finally blocks for resource cleanup

Security:
- Use of eval() or exec() on user input
- Hardcoded credentials, tokens, or API keys
- Insecure deserialization (pickle with untrusted data)
- Missing input validation

Performance:
- Inefficient list operations that should use generators
- Repeated expensive operations that should be cached
- Blocking I/O in async functions
- Unnecessary object creation in loops

Testability:
- Missing dependency injection (hardcoded dependencies)
- Functions doing too many things (hard to unit test)
- Missing or inadequate unit tests for new code

---

### Code Review Output
Produce the following result internally (used in Step 6):

skill_used      : java | angular | react | sql | python (or multiple)
findings        : list of all findings
  - title       : short title of the finding
  - file        : filename
  - line        : line number if identifiable
  - severity    : critical | warning | suggestion
  - issue       : clear description of the problem
  - recommendation : specific actionable fix
critical_count  : total number of critical findings
warning_count   : total number of warning findings
suggestion_count: total number of suggestion findings

---

## STEP 6 — Write Audit Report

Create this directory if it does not exist:
$(pwd)/docs/reviews/

Write the audit report to this exact path:
$(pwd)/docs/reviews/review-{ticket_id}.md

Use the following exact format:

---
# Audit Report — {ticket_id}

| Field        | Value                    |
|---|---|
| Project      | `{project_name}`         |
| Branch       | `{branch}`               |
| Ticket       | `{ticket_id}`            |
| Skill Used   | `{skill_used}`           |
| Generated At | {current datetime in UTC}|

---

## Architecture & PRD Alignment

**Status:** ✅ PASSED (if aligned = true) or ⚠️ ISSUES FOUND (if aligned = false)

> {alignment summary}

### Architecture Drift Issues

| File | Line | Severity | Issue |
|---|---|---|---|
(for each drift_issue)
| `{file}` | {line} | 🔴 high or 🟡 medium or 🟢 low | {issue} |

(if no drift issues, write: "✅ No architecture drift issues found.")

### PRD Compliance Issues

| Requirement | Severity | Issue |
|---|---|---|
(for each prd_issue)
| {requirement} | 🔴 high or 🟡 medium or 🟢 low | {issue} |

(if no prd issues, write: "✅ All PRD requirements are fulfilled.")

---

## Code Review Findings ({skill_used})

| 🔴 Critical | 🟡 Warnings | 💡 Suggestions |
|---|---|---|
| {critical_count} | {warning_count} | {suggestion_count} |

---

### Detailed Findings

(Repeat for each finding, numbered sequentially)

#### {number}. 🔴 or 🟡 or 💡 {title}

- **File:** `{file}`
- **Line:** {line}
- **Issue:** {issue}
- **Recommendation:** {recommendation}

---

(if no findings at all, write: "✅ No issues found. Code looks good!")

---
*This report was auto-generated by review-code-skill using an AI coding agent.*
*Project: {project_name} | Branch: {branch} | Ticket: {ticket_id}*
---

---

## STEP 7 — Post GitHub PR Comment

Only execute this step if pr_url was provided and is not empty.

Extract owner, repo, and PR number from the pr_url:
Example: https://github.com/sandeep-i2o/payments-service/pull/42
  owner     = sandeep-i2o
  repo      = payments-service
  pr_number = 42

Post a comment to the GitHub PR using this API call:
```bash
curl -s -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "body": "## 🤖 AI Code Review — `{ticket_id}`\n\n**Architecture Alignment:** {✅ Passed or ⚠️ Issues Found}\n> {alignment summary}\n\n| 🔴 Critical | 🟡 Warnings | 💡 Suggestions |\n|---|---|---|\n| {critical_count} | {warning_count} | {suggestion_count} |\n\n📄 Full report: `docs/reviews/review-{ticket_id}.md`"
  }' \
  https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments
```

✅ Expected: Comment appears on the GitHub PR.
❌ If GITHUB_TOKEN is not set: Skip this step and report "Skipping PR comment — GITHUB_TOKEN not set."

---

## STEP 8 — Final Summary

When all steps are complete, print this summary:

✅ review-code-skill completed successfully!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Project      : {project_name}
  Branch       : {branch}
  Ticket       : {ticket_id}
  Skill Used   : {skill_used}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Architecture : ✅ Aligned or ⚠️ {drift_issues count} drift issues
  PRD          : ✅ Compliant or ⚠️ {prd_issues count} compliance issues
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔴 Critical  : {critical_count}
  🟡 Warnings  : {warning_count}
  💡 Suggestions: {suggestion_count}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Audit Report : $(pwd)/docs/reviews/review-{ticket_id}.md
  PR Comment   : ✅ Posted or ⏭️ Skipped
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
