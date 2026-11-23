# Agent Skills Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 45 min · **Format:** self-paced hands-on lesson

## Outcome
Create a reusable portable skill instead of repeating a prompt.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
Create a skill that reviews a product requirements document for missing evaluation criteria.

## Hands-on lesson
### 1. Identify a repeatable task (5 min)
Select a task with stable inputs, procedure and output. A skill is instructions and optional resources, not a model or a standalone runtime.
### 2. Create the folder (15 min)
Create prd-eval-review/SKILL.md with YAML front matter containing name and description. Explain when to use it, required inputs, step-by-step workflow, output format and boundaries. Put detailed examples in references/ and optional deterministic helpers in scripts/.
### 3. Load it (10 min)
Copy the folder into .claude/skills/ for Claude Code or .agents/skills/ for Codex in the project root; restart or refresh discovery if needed. Consult the platform's current documentation if discovery differs. For a chat environment without skill import, supply the files as context.
### 4. Test and iterate (15 min)
Test a complete PRD, a PRD with no eval plan and an irrelevant request. Check that it activates appropriately, does not invent evidence, and gives consistent actionable outputs. Review any bundled scripts before running; never include secrets.

## Copyable prompt
```text
Create a skill named prd-eval-review. It should inspect a PRD for user outcome, failure modes, representative datasets, quality gates, guardrails and monitoring. Return missing evidence and next steps without fabricating results.
```

## Starter artifact / worked example
```text
---
name: prd-eval-review
description: Review product requirements for missing AI evaluation criteria. Use when reviewing an AI PRD.
---
Read the PRD; identify outcome, risks, metrics and missing evidence.
Return a table of gap, consequence, suggested test and owner.
Do not invent test results or approve release.
```

## Deliverable
A skill folder, three activation tests and a versioned improvement.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[Go/No-Go skill](../../skills/ai-feature-go-no-go/README.md)

[All masterclasses](../README.md)
