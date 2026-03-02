---
name: prd-to-qmetry-testcases
description: Generate non-executable QMetry test cases from PRD user stories in i2o-project-ai-docs. Use when asked to read `prd.md`, derive manual QA test cases, run user review, and push approved cases to QMetry for a specific module/project/release.
---

# PRD To QMetry Testcases

## Goal
Generate high-quality manual (non-executable) test cases from PRD user stories and push them to QMetry only after explicit user approval.

## Inputs
Collect and confirm these inputs before execution:
- `module` (required): expected branch name such as `price_monitoring`, `growth_accelerator`, `brand_protection`
- `project_name` (required): project directory under `projects/`
- `release_version` (required): release folder, default `7.5` when user does not provide one

## Preflight
1. Verify required tools: `git`, QMetry integration CLI/API credentials, and Markdown parsing capability.
2. Ask concise clarification questions when requirements are ambiguous.
3. Do not push anything to QMetry before explicit user confirmation.

Use [scripts/prd_preflight.py](scripts/prd_preflight.py) for deterministic repository/branch/PRD checks.

## Workflow

### 1) Clone Docs Repository
1. Clone repository when absent:
   ```bash
   git clone https://github.com/sandeep-i2o/i2o-project-ai-docs/
   ```
2. Reuse existing local clone when present.

### 2) Resolve Branch from Module
1. Treat `module` as branch name.
2. Check whether branch exists in origin.
3. If branch does not exist, stop and ask user for the correct branch name.
4. Checkout resolved branch.

### 3) Locate PRD
Read this path exactly:
`projects/{project_name}/{release_version}/docs/requirements/prd.md`

If file is missing, stop and report the exact missing path.

### 4) Generate Test Cases from PRD
1. Parse all user stories in `prd.md`.
2. If no user stories exist, stop with an error: `User stories are not present in the document.`
3. Read edge cases and corner cases from PRD and include coverage.
4. Consult product guides from `knowledge/kb_pdfs/` for domain-specific behavior and terminology.
5. Generate only manual/non-executable test cases compatible with QMetry import.

Use QMetry structure from [references/qmetry-testcase-format.md](references/qmetry-testcase-format.md).

### 5) Review Gate (Mandatory)
1. Present generated test cases to the user in a reviewable table/list.
2. Ask for explicit approval and requested edits.
3. Apply requested edits and re-present when needed.

### 6) Push Gate (Mandatory)
1. Push to QMetry only after explicit confirmation such as `Approved`, `Proceed`, or equivalent clear consent.
2. If approval is not explicit, do not push.
3. After push, report created test case keys/IDs and a concise coverage summary.

## QMetry Compatibility Rules
- Set case type to manual/non-executable.
- Keep each test case atomic with clear preconditions, steps, and expected results.
- Map each test case to at least one user story identifier or title.
- Include priority and module labels.
- Include release version metadata.

## Output Contract
Produce both:
1. Human-review markdown table/list.
2. QMetry-ready import structure (CSV/JSON fields as available in the environment).

## Failure Conditions
Stop and report clearly when any condition is met:
- branch missing for provided module
- `prd.md` missing at required path
- user stories absent in PRD
- QMetry credentials/integration unavailable

## Guardrails
- Do not invent user stories.
- Do not skip edge cases documented in PRD.
- Do not push unreviewed test cases.
- Keep communication concise and ask questions when ambiguity blocks accurate test design.
