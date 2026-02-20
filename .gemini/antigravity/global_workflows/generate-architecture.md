---
description: Generate Architecture Document
---

# Generate Fullstack Architecture Document

## Overview
This action generates a comprehensive fullstack architecture document that covers all technical aspects of the system design. The document follows the structured template defined in `./templates/design/fullstack-architecture-tmpl.yaml` and provides detailed guidance for AI-driven development.

## Input Required
- **Project Idea Document**: High-level project concept and vision
- **Product Requirements Document (PRD)**: Detailed functional and non-functional requirements from `docs/prd.md`
- **Frontend Specification** (optional): Check SUMMARY-frontend.md file inside directory `i2o-feature-ai-docs/knowledge/projects`
- **Technical Preferences** (optional): Check all SUMMARY-***.md files inside directory `i2o-feature-ai-docs/knowledge/projects`

## Process

### Step 1: Initial Setup and Context Gathering
1. Request and review all input documents (Project Idea, PRD, Frontend Spec)
2. Check for starter templates or existing projects
3. Extract key architectural drivers:
   - Functional requirements from PRD
   - Non-functional requirements (performance, security, scalability)
   - Technical assumptions and constraints
   - UI/UX requirements
   - Epic and story breakdown

### Step 2: High-Level Architecture Design

#### 2.1 Platform and Infrastructure Selection
- Analyze requirements to recommend 2-3 viable platform options:
  - **Vercel + Supabase**: Rapid development, built-in auth/storage
  - **AWS Full Stack**: Enterprise scale with Lambda, API Gateway, etc.
  - **Azure/GCP**: Based on specific ecosystem needs
- Present pros/cons and get user confirmation
- Document selected platform and key services

#### 2.2 Repository Structure
- Recommend repository approach (typically monorepo for fullstack)
- Select appropriate tooling (Nx, Turborepo, npm workspaces)
- Define package boundaries for shared code

#### 2.3 Architecture Patterns
- Define overall patterns (Jamstack, Serverless, Microservices)
- Frontend patterns (Component-based, State management)
- Backend patterns (Repository, CQRS, Event-driven)
- Integration patterns (BFF, API Gateway)

### Step 3: Technology Stack Selection
**CRITICAL: This is the definitive technology selection**
- Work with user to finalize every technology choice
- Document specific versions for all tools
- Cover all categories:
  - Frontend: Language, Framework, UI Library, State Management
  - Backend: Language, Framework, API Style
  - Data: Database, Cache, File Storage
  - DevOps: Build Tools, CI/CD, Monitoring
  - Testing: Unit, Integration, E2E tools

### Step 4: Data Architecture

#### 4.1 Conceptual Data Models
- Identify core business entities from PRD
- Define relationships between entities
- Create TypeScript interfaces for type sharing
- Design for both frontend and backend needs

#### 4.2 Database Schema Design
- Transform conceptual models to concrete schemas
- Design tables/collections based on chosen database
- Plan indexes and constraints
- Consider performance and scalability
- Include migration strategy

### Step 5: API Specification
Based on chosen API style:
- **REST**: Create OpenAPI 3.0 specification
- **GraphQL**: Define complete schema
- **tRPC**: Show router definitions
- Include all endpoints from PRD epics/stories
- Define authentication requirements
- Document request/response formats

### Step 6: Component Architecture

#### 6.1 System Components
- Identify major logical components/services
- Define boundaries and interfaces
- Map to technology choices
- Create component diagrams

#### 6.2 Frontend Architecture
- Component organization and patterns
- State management architecture
- Routing structure
- Frontend service layer (API communication)
- Design system integration

#### 6.3 Backend Architecture
- Service organization (serverless vs traditional)
- Controller/function structure
- Data access layer patterns
- Authentication/authorization implementation
- Middleware and cross-cutting concerns

### Step 7: UI/UX Architecture

#### 7.1 UI Flow Design
- Map user journeys from PRD stories
- Create flow diagrams for key interactions
- Define navigation structure
- Plan responsive breakpoints

#### 7.2 UI Component Mockups
- Create wireframes for core screens from PRD
- Show component hierarchy
- Demonstrate state variations
- Include error and loading states
- Consider accessibility requirements

### Step 8: Integration Design

#### 8.1 External APIs
- List all third-party integrations
- Document authentication methods
- Specify endpoints and rate limits
- Plan error handling and fallbacks

#### 8.2 Core Workflows
- Create sequence diagrams for critical paths
- Show frontend-backend interactions
- Include external API calls
- Document async operations

### Step 9: Deployment and Operations

#### 9.1 Project Structure
- Create detailed monorepo structure
- Show file organization for both frontend and backend
- Include shared packages
- Plan for scalability

#### 9.2 Development Workflow
- Local setup instructions
- Environment configuration
- Development commands
- Testing procedures

#### 9.3 Deployment Architecture
- Frontend deployment strategy
- Backend deployment approach
- CI/CD pipeline configuration
- Environment management

### Step 10: Quality Attributes

#### 10.1 Security Architecture
- Frontend security (CSP, XSS prevention)
- Backend security (validation, rate limiting)
- Authentication/authorization flows
- Data protection strategies

#### 10.2 Performance Design
- Frontend optimization targets
- Backend performance goals
- Caching strategies
- Database optimization

#### 10.3 Testing Strategy
- Testing pyramid approach
- Test organization and examples
- Coverage requirements
- E2E test scenarios

### Step 11: Standards and Guidelines

#### 11.1 Coding Standards
- Project-specific critical rules
- Naming conventions
- Error handling patterns
- Type sharing approach

#### 11.2 Monitoring Strategy
- Frontend monitoring setup
- Backend observability
- Key metrics to track
- Alerting configuration

### Step 12: Architecture Quality Verification
**CRITICAL: Run the architect checklist before finalizing**

1. **Load and Review Checklist**:
   - Read `.aiccelerate/checklist/architect-checklist.md`
   - Understand all quality criteria
   - Prepare to evaluate architecture against each item

2. **Execute Checklist Validation**:
   - Go through each checklist item systematically
   - Mark items as PASS/FAIL with specific evidence
   - Document any gaps or concerns
   - Note recommendations for improvement

3. **Address Gaps**:
   - For any FAIL items, revise the architecture
   - Incorporate checklist recommendations
   - Ensure all critical items PASS
   - Document trade-offs for any acceptable gaps

4. **Generate Checklist Report**:
   - Include complete checklist results in the document
   - Summarize overall architecture quality
   - List any remaining action items
   - Provide confidence score for implementation readiness

## Output Format
Generate a complete architecture document in Markdown following the template structure:
1. Introduction with starter template decisions
2. High-level architecture with diagrams
3. Definitive technology stack table
4. Data models and database schemas
5. API specifications
6. Component architecture (frontend and backend)
7. UI flows and mockups
8. Integration patterns
9. Deployment architecture
10. Security and performance considerations
11. Testing strategy
12. Coding standards
13. Monitoring approach
14. **Checklist Results Report** (from architect-checklist.md validation)

## Key Principles
1. **Comprehensiveness**: Cover all aspects of fullstack architecture
2. **Alignment**: Ensure all decisions support PRD requirements
3. **Specificity**: Make concrete technology choices with versions
4. **Visual Design**: Include diagrams, mockups, and code examples
5. **Practicality**: Focus on implementable designs
6. **AI-Friendly**: Structure for AI agent implementation
7. **Quality Assured**: Validate against architect checklist

## Elicitation Strategy
- Present each major section for user review
- Ask targeted questions for unclear requirements
- Offer educated recommendations with rationale
- Get explicit confirmation on critical decisions
- Mark assumptions clearly
- Iterate based on checklist feedback

## Architecture Deliverables
The document should enable:
- Developers to implement without ambiguity
- AI agents to generate code following the design
- Teams to understand system structure
- Stakeholders to validate technical approach
- Quality assurance through checklist validation

## Quality Assurance Process
1. **Pre-Checklist Review**: Before running the checklist, offer to output the full architecture document for user review
2. **Checklist Execution**: Once user confirms, execute the architect-checklist validation
3. **Gap Remediation**: Address any failures or recommendations from the checklist
4. **Final Validation**: Ensure the architecture meets all quality criteria
5. **Sign-off Ready**: Document should be implementation-ready after checklist passes

## Notes
- Always check for existing starter templates first
- Ensure frontend and backend designs are cohesive
- Include concrete examples and templates
- Focus on vertical integration across the stack
- Consider AI agent capabilities when sizing components
- The architect checklist is mandatory - do not skip this validation
- Use checklist recommendations to improve the architecture
- Document any acceptable deviations from checklist with justification