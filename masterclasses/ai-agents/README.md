# AI Agents Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 55 min · **Format:** self-paced hands-on lesson

## Outcome
Build a product team that coordinates tasks without uncontrolled autonomy.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
A team is prototyping a customer-feedback assistant.

## Hands-on lesson
### 1. Choose the architecture (10 min)
Use a workflow when steps are predictable; use an agent when decisions depend on intermediate results. Begin with one orchestrator; add specialist roles only when they improve quality or isolation.
### 2. Define contracts (15 min)
PM Twin produces problem brief and acceptance criteria; UX Lead produces user flows and uncertainty states; CTO produces implementation options and risks; Evals Lead produces tests independently. Each handoff is a written artifact, not an assumption of shared memory.
### 3. Run the team (20 min)
Give the PM a fictional brief. Pass its output to UX and CTO separately. Have the Evals Lead challenge all three, then return disagreements to the PM. Keep external actions disabled; require explicit approval for writes, messages or deployments.
### 4. Evaluate the workflow (10 min)
Compare against a single-agent baseline for completeness, contradictions, latency, cost and review effort. Test a missing requirement, injected instruction and failed tool. Set a maximum number of iterations and stop when unresolved risks require human input.

## Copyable prompt
```text
Act as the orchestrator of a four-role product team. Produce PM brief, UX proposal, CTO options and an independent eval plan in separate sections. Treat each role's output as a proposal, identify disagreements, and ask for human approval before any external action. Do not claim parallel agents ran unless they actually did.
```

## Starter artifact / worked example
```text
Handoff: role | input artifact | output artifact | acceptance criteria | unresolved issues | next owner
```

## Deliverable
Four role artifacts, handoff contract and single-agent comparison.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[AI Builder Team](../../ai-builder-team/README.md)

[All masterclasses](../README.md)
