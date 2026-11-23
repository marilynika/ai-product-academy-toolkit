# Worked example: AI meeting assistant (fictional)

**Vision:** Summarize meetings and suggest follow-up tasks, saving participants time. **Demo:** The assistant captures decisions and suggests tasks for review.

These five *illustrative* failures show how a review works. They are not real user incidents and **not** an empirical estimate of rates.

| ID | Observed failure | Primary type | Severity (illustrative) | Expected product response | Proposed disposition |
|---|---|---|---|---|---|
| EX-01 | Invents a deadline no one agreed to | Factual / unsupported claim | High | Mark unsourced date, request confirmation | Guardrail + verification |
| EX-02 | Assigns a sensitive task to wrong teammate | Privacy / security | High | Restrict visibility, confirm assignee | Blocker pending permission tests |
| EX-03 | Labels a brainstorm idea as a final decision | Instruction following | Medium | Show source quote and editable status | Guardrail |
| EX-04 | Misses a commitment in an accented speaker's turn | Fairness / accessibility | High | Evaluate segmented transcription, confirm task owner | Blocker pending slice testing |
| EX-05 | Creates external task without confirmation | Tool / unauthorized action | Critical | Require explicit user approval before action | Blocker |

## Evidence to bring
1. A representative, appropriately consented meeting dataset with task-success metrics and sample sizes; segmented performance where relevant.
2. Adversarial tests for uncertain decisions, ambiguous assignees and action permissions.
3. Recorded verification of confirmation flows, access restrictions and task rollback.
4. Monitoring owners and explicit stop/rollback thresholds.

## Example meeting decision
**No-go for autonomous task creation** until permission confirmation is enforced and verified. A limited *draft-only* pilot may be considered after separate privacy, task-quality and segment tests pass their predefined gates.

The five examples are teaching cases; they do not establish what any particular product does.
