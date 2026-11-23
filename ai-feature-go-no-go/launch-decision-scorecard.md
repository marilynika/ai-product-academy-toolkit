# Launch decision scorecard

**Feature/version:** [ ] · **Decision owner:** [ ] · **Date:** [ ]

## Launch gates (set thresholds BEFORE reviewing results)
| Gate | Threshold / policy | Observed evidence, sample and uncertainty | Pass? | Owner |
|---|---|---|---|---|
| Primary task success | [ ] | [ ] | [ ] | [ ] |
| Severe or critical failures | [ ] | [ ] | [ ] | [ ] |
| Important user segments | [ ] | [ ] | [ ] | [ ] |
| Tool/action permissions | [ ] | [ ] | [ ] | [ ] |
| Failure fallback / handoff | [ ] | [ ] | [ ] | [ ] |
| Privacy and security checks | [ ] | [ ] | [ ] | [ ] |
| Production monitoring + rollback | [ ] | [ ] | [ ] | [ ] |

Reference: [evaluation scorecard](../templates/evaluation-scorecard.md), [minimum viable quality](../templates/minimum-viable-quality.md), [risk matrix](../templates/hallucination-risk-matrix.md).

## Failure disposition
| Failure category | Impact and affected users | Evidence / frequency from representative set | Decision: acceptable / guardrail / blocker | Owner | Proof needed / due date |
|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## Release decision
- [ ] **Go**: All agreed gates satisfied; residual risk accepted by accountable owners.
- [ ] **Conditional go**: Specific mitigations must be implemented **and verified** before release; otherwise no-go.
- [ ] **Limited pilot**: Tight scope, consent/oversight, monitoring, halt criteria and review date.
- [ ] **No-go**: Blocker, insufficient evidence or missing safeguards.

**Reasoning / known limitations:** [ ]

**Guardrails and verification owners:** [ ]

**Monitoring metrics, trigger thresholds and rollback owner:** [ ]

**Approver(s) and next review:** [ ]

A sample of 20 worst outputs cannot establish a production failure rate. Avoid a single aggregate metric as the sole launch criterion.
