# 55-minute AI Feature Go/No-Go Review

**Feature / version:** [ ] · **Date:** [ ] · **Decision owner:** [ ] · **Attendees:** [ ]

**Pre-read:** vision/demo, 20 diverse realistic failures (de-identified), representative eval results by segment, proposed thresholds, guardrails, monitoring and rollback plan.

| Time | Section | Required output |
|---|---|---|
| 00:00–00:10 | Vision: show the best-case demo; identify user and outcome | One-sentence value proposition |
| 00:10–00:25 | Read the 20 worst outputs **before** looking at scores | Impact, expected behavior, source, owner for each |
| 00:25–00:35 | Cluster failures and assess how often they occur in separately sampled evals, by segment | Failure taxonomy and evidence gaps |
| 00:35–00:45 | Demonstrate behavior on failure: uncertainty, fallback, refusal, confirmation, handoff | Verified guardrails and recovery plan |
| 00:45–00:55 | Categorize failures: acceptable / acceptable with verified guardrail / blocker | Signed decision, owners, deadlines and rollback triggers |

## Questions to ask out loud
- Who would be harmed or excluded by this behavior? How severe and reversible is it?
- Does this failure happen more often for a particular user segment?
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
