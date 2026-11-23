# Claude Code Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 60 min · **Format:** self-paced hands-on lesson

## Outcome
Build and test a small product with a coding agent.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
Build a local feedback tagging tool using synthetic comments.

## Hands-on lesson
### 1. Scope the MVP (10 min)
Inputs are a CSV of comment_id and text; output is a table of comment IDs and editable labels. No external data transfer by default. Write acceptance criteria for invalid CSV, blank text, and export.
### 2. Prepare the workspace (10 min)
Install Claude Code using its official documentation, authenticate, create a new local folder and initialize Git. Start Claude Code from the folder. Add CLAUDE.md describing constraints, tests and commands. Keep secrets out of Git.
### 3. Implement iteratively (25 min)
Ask for a plan first, then approve a minimal Python implementation using the standard library. Request a small fictional dataset and tests. Inspect diffs, run tests locally and correct errors. Optional model integration is a separate change behind explicit consent and environment-variable credentials.
### 4. Review and demonstrate (15 min)
Run the app using instructions generated for the actual implementation. Test malformed data and export. Check git diff, document limitations and create a local commit only after review.

## Copyable prompt
```text
Inspect this empty project. Propose a minimal offline CSV feedback tagger with a command-line interface, editable keyword rules, export and tests. Wait for my approval before editing. Do not install packages, contact external services or commit without approval.
```

## Starter artifact / worked example
```text
Acceptance: valid CSV produces one label per ID; empty text becomes unknown; missing required headers produces a clear error; original file is unchanged.
```

## Deliverable
Runnable local prototype, tests, CLAUDE.md and README.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[AI PRD template](../../templates/ai-prd.md)

[All masterclasses](../README.md)
