# Agent Readiness Checklist

**Agent:** [ ]  **Owner:** [ ]  **Environment:** [ ]  **Date:** [ ]

## Task and autonomy
- [ ] Clearly defined task, success and stop conditions
- [ ] Allowed and prohibited actions listed
- [ ] Human approval for consequential or irreversible actions
- [ ] Escalation and handoff to a human are possible

## Tools, data and security
- [ ] Least-privilege credentials and scoped permissions
- [ ] Authentication and authorization tested
- [ ] Privacy and data retention reviewed
- [ ] Prompt injection and untrusted tool output tested
- [ ] No secrets in prompts, logs or public repositories

## Reliability and recovery
- [ ] End-to-end tests include edge cases and adversarial cases
- [ ] Timeouts, errors and retry behavior handled
- [ ] Duplicate or repeated actions prevented where necessary
- [ ] Partial actions have rollback or compensation plans
- [ ] Model and tool changes trigger new evaluations

## Human oversight and operations
- [ ] Users can review, pause, stop and revoke permissions
- [ ] Audit logs show actions and outcomes
- [ ] Rate limits, cost ceilings and monitoring in place
- [ ] Kill switch, rollout and rollback exercised
- [ ] Named incident response and maintenance owners

## Launch decision
| Critical risk | Test evidence | Owner | Status |
|---|---|---|---|
| Unauthorized actions | [ ] | [ ] | [ ] |
| Incorrect actions | [ ] | [ ] | [ ] |
| Failed recovery | [ ] | [ ] | [ ] |

**Decision:** [No-go / Sandbox / Human-approved pilot / Scoped production]

**Unresolved conditions:** [ ]

A checklist does not guarantee safety; evaluate controls in proportion to the consequences of each action.