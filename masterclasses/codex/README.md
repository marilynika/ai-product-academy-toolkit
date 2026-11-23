# OpenAI Codex Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 60 min · **Format:** self-paced hands-on lesson

## Outcome
Use a coding agent to move from product brief to tested implementation.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
Build an offline evaluation scorecard CLI that reads scored cases and summarizes results.

## Hands-on lesson
### 1. Specify outcomes (10 min)
Input CSV fields: case_id, slice, passed (0 or 1), severity. Output: totals, pass rates by slice and failed critical cases. Require explicit denominators and reject invalid values.
### 2. Prepare project context (10 min)
Open a local project in Codex or connect a sandbox repository in a supported cloud workflow. Add AGENTS.md with repo conventions, test commands and limitations. Check the selected environment's permissions and avoid private data.
### 3. Implement and test (25 min)
Ask Codex for a plan and tests. Approve a small standard-library Python implementation. Request unit tests for empty data, invalid pass values, duplicate IDs and critical failures. Run the available test command and inspect actual output; do not assume a successful test run.
### 4. Review changes (15 min)
Inspect changed files, check that the tool never equates diagnostic cases with production prevalence, and document sample commands. Approve any commit or PR separately as needed.

## Copyable prompt
```text
Read AGENTS.md and propose a minimal offline eval scorecard CLI. Include a test plan and edge cases before implementation. Use no external services. Show changes and actual test output, and do not deploy.
```

## Starter artifact / worked example
```text
case_id,slice,passed,severity
A1,normal,1,low
A2,edge,0,critical
A3,normal,1,medium
Expected: 2/3 overall, normal 2/2, edge 0/1, critical failure A2.
```

## Deliverable
Tested CLI, AGENTS.md and reviewable diff.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[Existing failure analyzer](../../ai-feature-go-no-go/README.md)

[All masterclasses](../README.md)
