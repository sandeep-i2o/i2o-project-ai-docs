---
name: prd-validator
description: Validate projects/*/docs/requirements/prd.md files against the canonical i2o PRD template (Sections A–E, success metrics, stories, release plan, appendix) whenever you need a systematic audit plus the `prd-validate.md` report for a specific project_id and release_version.
---

# PRD Validator Skill

## Parameters
- `project_id`: folder name under `projects/` (e.g., `marketplace-overview`).
- `release_version`: release folder (e.g., `release_8`).

## Workflow
1. Run the validator from the repo root so it can locate `projects/{project_id}/{release_version}/docs/requirements/prd.md`:
   ```sh
   cd /Users/sandeepofficial/Documents/workspace/automation/i2o-project-ai-docs
   python ~/.codex/skills/private/prd-validator/scripts/prd_validator.py \
     --project_id marketplace-overview \
     --release_version release_8
   ```
2. The script loads the bundled template (`references/i2o-prd-template.yaml`), scans for the Section A–E headings plus B1–B5, story metadata, success metrics, corner cases, release timeline, and appendix entries, and flags missing content or ambiguous placeholders.
3. It prints a short validation summary and writes `prd-validate.md` next to the PRD (same requirements folder).
4. Review `prd-validate.md` before sharing; it contains the coverage counts, uncovered sections, gap/ambiguity notes, and actionable suggestions derived from the template's validation rules.

## Validation checks
- Section coverage: A–E block headings, B1/B2/B3/B4/B5, and Section C story scaffolding (Story ID, Acceptance Criteria, Corner Cases) are required.
- Data completeness: success metrics, metric definition callouts, release plan milestones, and appendix entries (glossary, references, FAQ, changelog).
- Style gaps: missing acceptance criteria or corner cases, placeholders such as `TBD`/`TBA`, or ambiguous metrics without SMART context.
- Story hygiene: ensures each story includes metadata, dependencies, and acceptance criteria in Given-When-Then form.

## Output
- `/projects/{project_id}/{release_version}/docs/requirements/prd-validate.md`: Markdown report with coverage summary, numbered gaps, ambiguity warnings, and recommendations tied to the template.
- Console summary printed by the script for quick sanity checks.

## References
- Template definitions: `references/i2o-prd-template.yaml`
