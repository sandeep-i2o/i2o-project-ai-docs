---
description: Generate Product Requirements Document
---

# Generate Product Requirements Document (PRD)

## Overview
This action generates a comprehensive Product Requirements Document (PRD) based on a project idea document provided by the user. The PRD follows the structured template defined in `./templates/requirements/prd-template-i2o-manjot.yaml`.

## Input Required
- **Project Name**: Project name from i2o-feature-ai-docs/features (required), If user doesn't provide this parameter, explicitly ask user to select one feature project
- **Project Idea Document**: A document describing the project concept, vision, and high-level goals
- **Technical Preferences** (optional): If available, technical choices and constraints

## Output

Strictly generate the prd.md in i2o-feature-ai-docs/features/{{project_name}}/docs/requirements/prd.md


## Process

### Step 1: Gather Project Information
1. Request the project idea document from the user
2. Check if a Project Brief exists (recommended as foundation)
3. If no Project Brief exists, strongly recommend creating one first
4. Extract key information:
   - Project name and vision
   - Problem statement
   - Target users
   - Success metrics
   - MVP scope
   - Known constraints

### Step 2: Generate PRD Sections

#### 2.1 Goals and Background Context
- Create bullet list of desired outcomes (what the PRD will deliver)
- Write 1-2 paragraphs of background context
- Initialize change log with creation entry

#### 2.2 Requirements
- **Functional Requirements (FR)**: 
  - Number each with FR prefix (FR1, FR2, etc.)
  - Focus on what the system must do
  - Be specific and testable
- **Non-Functional Requirements (NFR)**:
  - Number each with NFR prefix (NFR1, NFR2, etc.)
  - Cover performance, security, scalability, etc.

#### 2.3 User Interface Design Goals (if applicable)
- Overall UX vision
- Key interaction paradigms
- Core screens and views (high-level)
- Accessibility requirements (None/WCAG AA/WCAG AAA)
- Branding guidelines
- Target platforms (Web/Mobile/Desktop)

#### 2.4 Technical Assumptions
- Repository structure (Monorepo/Polyrepo)
- Service architecture (Monolith/Microservices/Serverless)
- Testing requirements
- Languages, frameworks, and tools
- Deployment targets
- Additional technical constraints

#### 2.5 Epic List and Details
**CRITICAL: Follow these epic creation rules:**
- Each epic delivers significant, deployable functionality
- Epic 1 must establish foundation + initial functionality
- Epics build sequentially on each other
- Each epic provides tangible user/business value

For each epic:
- Title and 2-3 sentence goal
- Sequentially ordered stories
- Each story includes:
  - User story format (As a... I want... So that...)
  - Numbered acceptance criteria
  - Stories sized for 2-4 hour AI agent sessions
  - Vertical slices of functionality

### Step 3: Quality Checks
1. Run PM checklist validation
2. Ensure all requirements are testable
3. Verify epic/story sequencing logic
4. Check for completeness and clarity

### Step 4: Generate Next Steps
- Create UX Expert prompt (if UI/UX requirements exist)
- Create Architect prompt for technical design

## Output Format
Generate a complete PRD in Markdown format following the structure:
- Goals and Background Context
- Requirements (Functional and Non-Functional)
- User Interface Design Goals (if applicable)
- Technical Assumptions
- Epic List with detailed stories and acceptance criteria
- Checklist Results
- Next Steps with prompts

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
- Always recommend creating a Project Brief first if one doesn't exist
- Focus on "what" and "why", not "how" (leave implementation to Architect)
- Size stories appropriately for AI agent execution
- Include cross-cutting concerns (logging, security) throughout, not as final items