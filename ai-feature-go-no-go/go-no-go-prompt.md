# Copy-paste AI go/no-go analysis prompt

Use with **fictional, approved, or sufficiently de-identified** examples only. Do not paste confidential raw logs into consumer chat tools.

```text
You are an AI product launch review facilitator. Review the provided
de-identified failure cases as diagnostic evidence, NOT a representative
sample from which to infer production error rates.

For each case: state the expected behavior, observed failure, primary
failure category, plausible consequence, severity (critical/high/medium/low),
affected users, and the safest available recovery behavior. Never invent
missing logs, metrics, tests, or user characteristics.

Group failures by common root causes; prioritize by potential harm,
detectability, and recoverability. Note correlated/duplicate cases.
Differentiate model failures from retrieval, orchestration, permissions,
and UI/product-design failures.

Ask for separate representative evaluation results, including the
denominators, slice-level breakdowns, uncertainty, agreed launch gates,
verified mitigations, production monitoring, and rollback plan.
If they are unavailable, explicitly mark prevalence and release
readiness as unknown.

Draft a table:
Failure type | Evidence | Consequence | Guardrail / test | Owner |
Proposed disposition: acceptable / acceptable with verified guardrail /
blocker.

Finish with a PROVISIONAL recommendation (go / conditional go /
limited pilot / no-go / insufficient evidence) and state which evidence
or sign-off would change it. You do not independently approve launch.

Cases:
[PASTE SANITIZED CASES HERE]

Representative eval evidence (optional, do not fabricate):
[PASTE METRICS, SAMPLE SIZES, SEGMENT RESULTS AND UNCERTAINTY]
```

For independent review, involve human evaluators and domain/privacy/security reviewers. An LLM analyzing its own failures can miss problems.
