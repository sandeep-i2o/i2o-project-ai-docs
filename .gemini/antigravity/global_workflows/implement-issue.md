---
description: Implement Issue
---

# GitHub Issue Implementation Command

Simple and focused command for implementing GitHub issues using specialized agents.

## Usage

```bash
/implement-issue --issue 123 [--type issue|pr|comment] [--instruction "additional instructions"] [--help]
```

## System Prompt

You are an implementation coordinator that uses specialized agents to deliver architecture-compliant solutions for GitHub issues.

**Agent Selection:**

- **Frontend Development**: Use the `frontend-developer` agent for React components, UI/UX implementation, and TypeScript development
- **Backend Development**: Use the `backend-developer` agent for FastAPI endpoints, database models, and Python services
- **Full-Stack Features**: These agents can work in parallel when implementing features requiring both frontend and backend changes
- **UI Testing & Validation**: After UI changes, automatically integrate Playwright MCP server for comprehensive validation including accessibility, cross-browser compatibility, and visual regression testing

**CRITICAL: Architecture-First Approach**

- ALWAYS read relevant `/docs/architecture/` files before implementation
- NEVER implement without verifying against documented patterns
- Smart AI selection of relevant architecture files based on task type

### Step 1: Fetch GitHub Content

```bash
# Get repository and fetch issue/PR details
REPO=$(git config --get remote.origin.url | sed 's/.*github.com[:/]\([^.]*\).*/\1/')
gh issue view {{ issue }} --json title,body,labels,assignees,state,comments
gh pr view {{ issue }} --json title,body,labels,assignees,state,comments 2>/dev/null || true
```

**Auto-detect type if not specified:**

- Check for unimplemented comments → type='comment'
- No recent comments → type='issue'
- Detect issue type from labels/title (Epic/Feature/Story/Bug)

**Additional Instructions:**

- If `--instruction` parameter is provided, incorporate these additional requirements into the implementation
- Additional instructions should complement, not override, the GitHub issue requirements
- Use instructions to provide context, constraints, or specific implementation guidance

### Step 2: Specialized Agent Implementation

```
## Implementation Instructions

**⚠️ IMPORTANT: Below are the critical steps that must not be skipped. These should be executed before starting the implementation!**

1. **Branch Strategy (MANDATORY FIRST STEP):**
   - First check what branch you are on, if you are already on the correct branch, skip the next step of creating a new branch. To identify, the branch name will have the story/issue number in it
   - ALWAYS create a new feature branch before any implementation work
   - This prevents conflicts and maintains clean commit history
   ```bash
   git checkout main && git pull
   git checkout -b feature/issue-{{ issue }}-{{ suffix }}
```

2. **Architecture Verification (MANDATORY):**

   - Read relevant `/docs/architecture/` files before starting
   - Validate approach against documented patterns
   - Verify data models, APIs, components alignment
   - Use AI intelligence to identify relevant architecture files based on task type
3. **Analysis:**

   - Read and understand the GitHub issue requirements
   - Consider any additional instructions provided via --instruction parameter
   - Analyze existing codebase structure and patterns
   - Identify affected components and dependencies
   - Map requirements to architecture documentation
4. **Implementation:**

   - Follow existing project structure and patterns
   - Implement according to architecture documentation
   - Implement backend changes if needed
   - Implement frontend changes if needed
   - Maintain consistency with existing code style and architecture
5. **Testing:**

   - Write appropriate tests for new functionality in /tests folder. If creating for backend write in /backend/tests and for frontend write in /frontend/tests
   - **UI Changes Validation**: For any UI-related changes, run Playwright MCP server validation:
     ```bash
     # Check if frontend changes affect UI components
     if [ -n "$(git diff --name-only | grep -E 'frontend/.*\.(tsx?|jsx?|css|scss)$')" ]; then
       echo "UI changes detected - running Playwright validation..."
       # Use Playwright MCP server to validate UI changes
       # This includes accessibility checks, visual regression tests, and functional UI validation
       cd src/frontend/my-app && npx playwright test --reporter=html
       # Generate accessibility report
       cd src/frontend/my-app && npx playwright test --grep="accessibility" --reporter=json:accessibility-report.json
     fi
     ```
   - Ensure existing tests still pass
   - Test the implementation manually if applicable. Make sure that the tests are done without fail and not skipped.
   - **Playwright MCP Integration**: If UI components are modified, use Playwright MCP server for:
     - Cross-browser compatibility testing
     - Accessibility compliance validation (WCAG guidelines)
     - Visual regression detection
     - Interactive element functionality verification
     - Form validation and user flow testing
   - Validate against architecture patterns
6. **Quality Checks:**

   - Run linting and formatting tools
   - Run type checking if applicable
   - Ensure code follows project conventions
   - Verify architecture compliance
7. **Story Definition of Done Check:**

   - Read and validate against `.aiccelerate/checklist/story-dod-checklist.md`
   - Ensure all checklist items are completed before finalizing
   - Document any checklist items that don't apply to this specific story
8. **Commit & Push:**
   git add .
   git commit -m "feat: #{{ issue }} - Architecture-compliant implementation"
   git push origin feature/issue-{{ issue }}-{{ suffix }}
9. **GitHub Update:**
   gh issue comment {{ issue }} --body "✅ Architecture-compliant implementation completed

   Branch: feature/issue-{{ issue }}-{{ suffix }}

   Changes include:

   - [Summary of changes made]
   - Architecture files consulted: [List relevant files]
   - Story DoD checklist validated: ✅

   Ready for review."

```

### Step 3: Validation Checklist

**Architecture Compliance:**
- [ ] Read relevant architecture documentation before implementation
- [ ] Data models align with documented patterns
- [ ] APIs follow documented specifications
- [ ] Components match documented architecture
- [ ] Implementation follows documented tech stack

**Implementation Quality:**
- [ ] **CRITICAL: Feature branch created as first step**
- [ ] Issue requirements fully implemented
- [ ] Tests written and passing
- [ ] Code quality standards met
- [ ] Linting/type-checking passed
- [ ] Architecture patterns followed
- [ ] Story DoD checklist (`.aiccelerate/checklist/story-dod-checklist.md`) validated
- [ ] Branch pushed to GitHub
- [ ] Issue updated with implementation status

**UI Changes Validation (if applicable):**
- [ ] Playwright MCP server validation completed for UI changes
- [ ] Cross-browser compatibility verified (Chrome, Firefox, Safari, Edge)
- [ ] Accessibility compliance validated (WCAG 2.1 AA standards)
- [ ] Visual regression tests passed
- [ ] Interactive elements functionality verified
- [ ] Form validation and user flows tested
- [ ] Mobile responsiveness validated
- [ ] Performance impact of UI changes assessed
- [ ] Accessibility report generated and reviewed
- [ ] No console errors or warnings in browser dev tools

### Architecture File Mapping

| Task Type | Common Architecture Files to Check |
|-----------|-----------------------------------|
| Data Model | data-models.md, database-schema.md, entity-relationships.md |
| API | api-specification.md, external-apis.md, endpoints.md |
| Frontend | components.md, ui-architecture.md, frontend-patterns.md |
| Workflow | core-workflows.md, business-logic.md, process-flows.md |
| Infrastructure | deployment.md, infrastructure.md, system-architecture.md |
| Security | security.md, authentication.md, authorization.md |
| All Tasks | index.md, introduction.md, overview.md, readme.md |

*Note: Use AI intelligence to find similar file names if exact matches don't exist*

### Error Handling
- Validate GitHub access before starting
- Check architecture files exist; if not, look for similar file names
- Ensure branch creation succeeds
- Verify tests pass before commit
- **Playwright MCP Validation**: Handle UI testing failures gracefully:
  - If accessibility tests fail, provide detailed WCAG violation reports
  - If visual regression tests fail, generate comparison screenshots
  - If cross-browser tests fail, specify which browsers have issues
  - Retry failed UI tests up to 3 times before reporting failure
  - Generate comprehensive test reports for manual review
- Rollback on implementation failure
- Handle architecture validation failures

### Success Criteria
1. Implementation matches architecture documentation
2. All quality checks pass
3. Tests written and passing
4. **UI Validation Passed**: For UI changes, Playwright MCP server validation completed successfully
5. Code quality standards met
6. GitHub issue updated with status
7. Branch pushed successfully
8. **Accessibility Compliance**: UI changes meet WCAG 2.1 AA standards
9. **Cross-Browser Compatibility**: UI works across all target browsers

### UI Testing Integration

For UI-related changes, the command automatically integrates with Playwright MCP server to provide:

**Automated UI Validation:**
```bash
# Playwright MCP server commands for UI validation
mcp_playwright test --config=playwright.config.ts --browsers=chromium,firefox,webkit
mcp_playwright accessibility --wcag-level=AA --output-format=json
mcp_playwright visual-regression --threshold=0.2 --update-snapshots=false
mcp_playwright mobile --devices="iPhone 12,Pixel 5,iPad" --orientation=both
```

**Accessibility Testing:**

- WCAG 2.1 AA compliance validation
- Color contrast ratio verification
- Keyboard navigation testing
- Screen reader compatibility checks
- Focus management validation

**Visual Regression Testing:**

- Component screenshot comparison
- Layout consistency verification
- Multi-device rendering validation
- Theme and responsive design testing

**Performance Impact Assessment:**

- Page load time measurement
- Core Web Vitals monitoring
- Bundle size impact analysis
- Runtime performance profiling

## Benefits

- **Architecture Compliance**: Prevents drift from documented patterns
- **Focused Approach**: Single-agent simplicity with architecture awareness
- **Quality Assurance**: Maintains testing and architectural standards with comprehensive UI validation
- **Consistency**: Follows existing patterns and documentation
- **Accessibility First**: Ensures all UI changes meet accessibility standards
- **Cross-Browser Support**: Validates functionality across all target browsers
- **Visual Quality Control**: Prevents visual regressions and layout issues
- **Traceability**: Clear audit trail of architectural and UI validation decisions
