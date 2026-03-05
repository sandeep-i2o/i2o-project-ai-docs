# Finding to Remediation Action Map

Use this mapping to convert review findings into deterministic ticket updates.

## 1) Coverage Gap

Signals:
- Requirement exists in PRD/architecture but no ticket AC owns it

Preferred actions:
1. Add explicit AC in existing story that already owns nearest scope
2. Add DoD evidence line (test artifact, API response proof, UI validation)
3. If no clear owner exists, create a new story and link it in Epic

## 2) Non-Functional Gap

Signals:
- Performance/availability/security/observability requirement not testable in backlog

Preferred actions:
1. Add measurable AC (`P95 < x`, `uptime >= y`, etc.)
2. Add verification method (load test, monitoring check, negative test)
3. Add release gate language (pass/fail evidence required)
4. Create dedicated NFR story when changes would overload existing stories

## 3) Sequencing/Dependency Gap

Signals:
- Prerequisite is documented but dependency chain is not explicit

Preferred actions:
1. Add explicit dependency statements in affected stories and epic
2. Identify single owner ticket for the gate
3. Remove duplicate ownership language from other tickets

## 4) Duplication/Overlap Gap

Signals:
- Multiple epics/stories claim same deliverable

Preferred actions:
1. Keep one canonical owner
2. Convert others to cross-reference/dependency only
3. Preserve business context but remove duplicate execution scope

## 5) Ticket Quality Gap

Signals:
- AC vague, contradictory, or not testable

Preferred actions:
1. Rewrite AC in observable pass/fail terms
2. Add bounded scope statements
3. Add explicit constraints and expected artifacts

## 6) Ambiguity

Signals:
- Terms/ownership/contract unclear across docs and tickets

Preferred actions:
1. Add explicit assumption or decision in target ticket
2. Add open question only if blocker remains
3. Mark finding as `Deferred` when authoritative answer is unavailable

## Disposition Rules

- `Resolved`: ticket updates fully address the finding with testable AC/dependency clarity.
- `Partially Resolved`: progress made, but an external decision or dependency remains.
- `Deferred`: blocked by missing authority, conflicting source docs, or out-of-scope decision.

Every disposition must include:
- Finding ID
- Ticket files changed (or why no change)
- One-line rationale
