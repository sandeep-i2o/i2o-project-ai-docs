---
description: Generate PRD ACLI
---

# Generate Product Requirements Document (PRD)

## Overview
This action generates a comprehensive Product Requirements Document (PRD) based on a initial idea document provided by the user. The PRD follows the structured template defined in `./templates/prd-tmpl-i2o.yaml`. 

IMPORTANT: Use the skill sam-strategist.

## Input Required

- **Project Name**: Project name from i2o-feature-ai-docs/features (required), If user doesn't provide this parameter, explicitly ask user to select one feature project
- **Confluence Page**: Fetch the confluence page from the link e.g. https://i2oretail.atlassian.net/wiki/spaces/IR/pages/2487812114/7.5+Price+Monitor+Requirements


## Output

Strictly generate the prd.md in i2o-feature-ai-docs/features/{{project_name}}/docs/requirements/prd.md


## Process

### Step 1: Gather Project Information
1. Use the `acli` command to pull the content of the provided Confluence Page link. Ensure you maintain the rich formatting and properly include/download any images from the page.
2. Save this extracted content to a file named `extracted-prd.md` in the `i2o-feature-ai-docs/features/{{project_name}}/docs/requirements/` directory.
3. Read the `extracted-prd.md` along with any other project idea documents in the docs/requirements folder.
4. Extract key information:
   - Project name and vision
   - Problem statement
   - Target users
   - Success metrics
   - MVP scope
   - Known constraints

### Step 2: Generate PRD Sections

**CRITICAL: Follow the template and insructions as per the template defined in ./templates/i2o_prd_tmp.yaml**

**CRITICAL: Follow these epic creation rules:**
- Create only one epic for one PRD

For each epic:
- Title and 2-3 sentence goal
- Sequentially ordered stories
- Each story includes:
  - User story format (As a... I want... So that...)
  - Numbered acceptance criteria
  - Stories sized for 2-4 hour AI agent sessions
  - Vertical slices of functionality
- STRICTLY include all user stories from the documents if they are present

### Step 3: Quality Checks
1. Run PM checklist validation
2. Ensure all requirements are testable
3. Verify epic/story sequencing logic
4. Check for completeness and clarity

### Step 4: Generate Next Steps
- Create UX Expert prompt (if UI/UX requirements exist)
- Create Architect prompt for technical design

## Output Format
Generate a complete PRD in Markdown format following the structure as defined in template

## Key Principles
1. **Elicit Information**: Ask clarifying questions when details are missing
2. **Make Educated Guesses**: Pre-fill sections based on context, clearly marking assumptions
3. **Sequential Logic**: Ensure epics and stories follow logical progression
4. **Completeness**: Cover all aspects needed for development
5. **Clarity**: Write clear, unambiguous requirements
6. **Testability**: All requirements and acceptance criteria must be verifiable

## Example Usage
```
User: "Here is my project idea document for a task management application..."
AI: *Reviews document, asks clarifying questions, then generates complete PRD following the template*
```

## Notes
- Focus on "what" and "why", not "how" (leave implementation to Architect)
- Size stories appropriately for AI agent execution
- Include cross-cutting concerns (logging, security) throughout, not as final items