# Gap Taxonomy

Use this taxonomy when reviewing ticket quality and alignment.

## 1. Coverage Gap

Definition: A PRD or architecture requirement has no corresponding Epic/Story.

Detection hints:
- Requirement cannot be mapped to any ticket scope.
- Only partial coverage exists and the missing part is material.

## 2. Architecture Misalignment

Definition: Ticket scope conflicts with documented architecture decisions.

Detection hints:
- Ticket introduces a component path not in architecture.
- Ticket bypasses required data flow, boundary, or ownership rules.

## 3. Sequencing/Dependency Gap

Definition: Ticket order or dependencies make delivery impractical.

Detection hints:
- Story depends on an API/schema/component not planned earlier.
- Integration stories exist without enabling infrastructure stories.

## 4. Non-Functional Gap

Definition: Required NFRs are absent or untestable in tickets.

Detection hints:
- No explicit performance/security/observability acceptance criteria.
- No evidence of monitoring, logging, alerting, or failure handling where required.

## 5. Ticket Quality Gap

Definition: Ticket cannot be reliably implemented or tested.

Detection hints:
- Missing or vague acceptance criteria.
- No measurable done condition.
- Mixed responsibilities (frontend/backend/data/ops) without clear boundary.

## 6. Duplication/Overlap Gap

Definition: Multiple tickets claim the same deliverable or ownership.

Detection hints:
- Similar acceptance criteria repeated across stories.
- Competing implementations implied by separate epics.

## 7. Ambiguity

Definition: Intent exists, but meaning is unclear enough to risk divergence.

Detection hints:
- Undefined business term.
- Missing owner/system of record.
- Unclear edge cases, error handling, or data contract.

Ambiguity wording guidance:
- Use direct language: "Ambiguous because..."
- Add "Clarify by..." with one concrete question.
