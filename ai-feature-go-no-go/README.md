# AI Feature Go/No-Go Review Kit

**A free, practical 55-minute review for teams deciding whether an AI feature is ready to ship.**

By Dr. Marily Nika · [AI Product Academy](https://aiproductacademy.com)

A go/no-go review is **not a launch pitch**. The question is not simply, "Look how cool this is — can we ship?" It is: **"Look what this does for users, look at the real-world conditions it handles well, and look at what it does when those conditions break."** A decision requires evidence of value, reliable behavior, and safe recovery — not enthusiasm for the demo.

**The review should demonstrate three things:**
1. **Value:** The feature solves a meaningful user problem, and the normal user experience works.
2. **Reliability:** It responds appropriately to realistic variation: ambiguous requests, missing or conflicting context, different user segments, retrieval or tool errors, and other important edge cases.
3. **Graceful failure:** When it cannot deliver the right answer or action, it makes uncertainty clear, asks, falls back, refuses, or hands off as appropriate — rather than bluffing or taking an unsafe action.

The "20 worst outputs" make hidden failure modes concrete, **not** statistically representative. Pair them with representative evaluations and launch thresholds to understand frequency and readiness.

## Start in 3 minutes — no coding required
1. Open [the 55-minute agenda](review-agenda.md) and copy it into your meeting invite.
2. Click [worst-20-template.csv](worst-20-template.csv) → **Raw** → save the file; open it in Google Sheets or Excel. Replace the illustrative rows with *de-identified* failures from realistic testing. Aim for 20 diverse, high-risk examples, not 20 duplicates.
3. Use the [failure taxonomy](failure-taxonomy.md) to label the cases and [decision scorecard](launch-decision-scorecard.md) to record launch criteria, owner, guardrail, and decision.
4. Optionally copy the [analysis prompt](go-no-go-prompt.md) into ChatGPT or Claude with sanitized cases.
5. Walk through the [fictional meeting assistant example](example-meeting-assistant.md).

**Want a summary generated from CSV?** Download this folder (or clone the repository) and run Python 3.9+:

```bash
python3 ai-feature-go-no-go/analyze_failures.py ai-feature-go-no-go/worst-20-template.csv
```

No external packages required. The command prints counts by failure type and user segment, flags critical/high-severity cases, and creates **no files**. The included CSV rows are illustrative only.

To download everything: from the [main repository](https://github.com/marilynika/ai-product-academy-toolkit), select **Code → Download ZIP**, unzip it, then open this folder. Or clone:

```bash
git clone https://github.com/marilynika/ai-product-academy-toolkit.git
cd ai-product-academy-toolkit
```

## The meeting (55 minutes)
| Part | Minutes | Question |
|---|---:|---|
| Value + tested happy path | 10 | What user outcome does this enable, and when does it work reliably? |
| 20 worst realistic outputs | 15 | What can go wrong? |
| Cluster and quantify failures | 10 | Who is affected and how often? |
| Real-world behavior and recovery | 10 | Does it react appropriately to ambiguity, missing context, tool failures and uncertainty? |
| Explicit decision and owners | 10 | Ship, conditional launch, or no-go? |

## Evidence needed **in addition** to the worst 20
- Representative evaluations with denominators, sampling methods, and confidence/uncertainty.
- Slice-level results for important user groups, languages, tasks and contexts.
- High-severity red-team cases, where applicable, and verification of guardrails/fallbacks.
- Agreed launch thresholds, monitoring, rollback criteria and named decision-makers.

The worst-20 set is a *diagnostic collection biased toward bad outcomes*. **Never use its counts to estimate real-world error rates.** For frequency estimates, analyze your separate representative evaluation data.

## Related tools already in this repo
- [Evaluation scorecard](../templates/evaluation-scorecard.md) — define metrics and thresholds.
- [Minimum viable quality](../templates/minimum-viable-quality.md) — establish the quality bar.
- [Hallucination risk matrix](../templates/hallucination-risk-matrix.md) — severity and recoverability.
- [Builder Team Evals Agent](../ai-builder-team/07-evals-agent.md) — challenge product-team claims; does **not** replace independent testing.

## Sharing and safety
Never upload private user messages, employee/customer information, keys, secrets, internal incidents, or proprietary outputs to a public repository or third-party chatbot. Use fictional or properly approved/de-identified data. Example cases are fictional. Adapt review thresholds to the domain, including privacy, security, legal, accessibility and safety obligations. This is a decision aid, not a safety certification.
