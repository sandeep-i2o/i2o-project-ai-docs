---
description: Generate Product Requirements Document
---

# Generate Product Requirements Document (PRD)

## Overview
This action generates a comprehensive Product Requirements Document (PRD) based on a initial idea document provided by the user. The Generated PRD should strictly follow the structured template defined in `./templates/i2o-prd-template.yaml`. Look for the templates, skills in Antigravity gemini system root folder ~/.gemini/antigravity/**

IMPORTANT: Use the skill sam-strategist.

## Input Required

- **Project Name**: Project name from i2o-feature-ai-docs/features (required), If user doesn't provide this parameter, explicitly ask user to select one feature project
- **Project Seed Documents**: Check all documents inside i2o-feature-ai-docs/features/{{project_name}}/docs/requirements/ for generating the PRD. It will have all initial research documents.
- **Technical Preferences** (optional): If available, technical choices and constraints


## Output

Strictly generate the prd.md in i2o-feature-ai-docs/features/{{project_name}}/docs/requirements/prd.md


## Process

### Step 1: Gather Project Information
1. Check all the project idea document in the docs/requirements folder
2. Extract key information:
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
- Create user stories with mockup images
- DO NOT MISS ANY USER STORIES THAT IS PRESENT IN SEED DOCUMENTS UNDER REQUIREMENTS FOLDER

### Step 3: Quality Checks
1. Run PM checklist validation
2. Ensure all requirements are testable
3. Verify epic/story sequencing logic
4. Check for completeness and clarity


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