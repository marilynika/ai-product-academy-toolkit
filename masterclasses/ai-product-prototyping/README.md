# AI Product Prototyping Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 60 min · **Format:** self-paced hands-on lesson

## Outcome
Go from problem to a testable AI product experience.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
Prototype a feedback summarizer for a fictional product team.

## Hands-on lesson
### 1. Define the job (10 min)
A PM needs to turn 20 feedback comments into themes with traceable evidence. Compare against a manual grouping workflow. Decide whether AI is needed for ambiguous language; deterministic filters may suffice for structured tags.
### 2. Design the experience (10 min)
Sketch upload, review, generated themes, evidence links and export. Include empty state, error state and uncertainty. Never present fabricated quotations as customer evidence.
### 3. Build the prototype (25 min)
Use a coding agent or prototyping environment to create a local UI with synthetic sample comments. Start with mocked model output clearly labeled; optionally integrate a model using environment credentials and explicit data consent.
### 4. Evaluate (15 min)
Test duplicate comments, conflicting themes, missing evidence, injection text and an empty file. Ask three consenting testers to perform the task with fictional data; observe completion and correction effort. Document limitations and prioritize next iteration.

## Copyable prompt
```text
Build a prototype with a synthetic feedback dataset. Show theme cards with supporting comment IDs and an editable summary. Include loading, empty and error states. Clearly label mocked outputs. No external calls until approved.
```

## Starter artifact / worked example
```text
User story: As a PM, I can verify every proposed theme against its source comments before exporting it.
```

## Deliverable
Working prototype or labeled mock, user test notes and acceptance criteria.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[Customer-feedback copilot example](../../examples/customer-feedback-copilot.md)

[All masterclasses](../README.md)
