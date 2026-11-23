# AI Feature Launch Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 55 min · **Format:** self-paced hands-on lesson

## Outcome
Facilitate an evidence-backed go/no-go review.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
A fictional meeting assistant extracts tasks from meeting transcripts.

## Hands-on lesson
### 1. Value and happy path (10 min)
Identify the outcome, baseline and normal behavior. Define pre-agreed gates for task accuracy, permissions, privacy, fallback and operational readiness.
### 2. Worst outputs (15 min)
Review 20 diverse diagnostic failures, or fewer if unavailable. Include wrong owner, invented task, unauthorized calendar action, uncertain transcript and conflicting instructions. Record severity, consequence and recovery.
### 3. Quantify and cluster (10 min)
Separate representative eval results from selected failures. Calculate rates only from representative datasets with known sampling and denominator. Cluster model, retrieval, orchestration, permissions and UX failures.
### 4. Recovery review (10 min)
Check that uncertain assignments require confirmation, retries avoid duplicate writes and unauthorized actions never execute. Verify safeguards rather than assuming they work.
### 5. Decide (10 min)
Record GO, conditional GO, limited pilot, NO-GO or insufficient evidence. Define conditions, accountable owners, monitoring, rollback and next review. Human decision-makers authorize release.

## Copyable prompt
```text
Use the go/no-go skill to review this fictional meeting assistant. Distinguish observed facts from assumptions, compare representative results with pre-agreed gates and identify blockers. Do not infer error rates from worst outputs.
```

## Starter artifact / worked example
```text
Illustrative gate: no unauthorized calendar writes observed in the designated permissions test suite. Evidence: one unauthorized write observed. Disposition: blocker until corrected and verified; zero observed later would not prove zero risk.
```

## Deliverable
Decision scorecard, prioritized mitigations and rollout plan.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[Review kit and installable skill](../../skills/ai-feature-go-no-go/README.md)

[All masterclasses](../README.md)
