# 55-minute AI Feature Go/No-Go Review

**Feature / version:** [ ] · **Date:** [ ] · **Decision owner:** [ ] · **Attendees:** [ ]

**Purpose:** This is not a pitch to launch. Demonstrate: **(1)** real user value, **(2)** reliable handling of realistic variation, and **(3)** appropriate behavior when the model or workflow is uncertain or wrong.

**Pre-read:** user outcome and demo, representative eval results by segment, 20 diverse realistic failures (de-identified), predefined thresholds, edge-case and tool-failure tests, fallback and guardrail verification, monitoring and rollback plan.

| Time | Section | Required output |
|---|---|---|
| 00:00–00:10 | Value and evidence: show the expected journey plus a few realistic variations the product handles well | User outcome, success conditions and tested coverage |
| 00:10–00:25 | Read the 20 worst outputs **before** looking at scores | Impact, expected behavior, source, owner for each |
| 00:25–00:35 | Cluster failures and assess how often they occur in separately sampled evals, by segment | Failure taxonomy and evidence gaps |
| 00:35–00:45 | Demonstrate reactions to ambiguity, missing/conflicting context, low confidence, failed retrieval/tools, unsafe actions: clarify, abstain, fallback, refuse, confirm, hand off | Verified recovery behavior with tests |
| 00:45–00:55 | Categorize failures: acceptable / acceptable with verified guardrail / blocker | Signed decision, owners, deadlines and rollback triggers |

## Questions to ask out loud
- Who would be harmed or excluded by this behavior? How severe and reversible is it?
- Does this failure happen more often for a particular user segment?
- Does the product respond appropriately to ambiguity, missing or conflicting context, and failures in retrieval/tools?
- Could the system bluff or act when it should ask, refuse or defer?
- Are we evaluating the full product stack, including tools and retrieval?
- Which evidence or test would change our decision?

## Decision record
**Decision:** [Go / Conditional go / No-go / Limited pilot]

**Rationale and supporting evidence:** [ ]

**Unresolved blockers:** [ ]

**Conditions and verification owners:** [ ]

**Production alerting and rollback thresholds:** [ ]

**Sign-off and next review date:** [ ]

> Twenty severe, diverse failures are useful qualitative evidence, not a statistically valid estimate of prevalence. A missing failure collection means *insufficient review evidence*, not proof that the feature is unsafe.
