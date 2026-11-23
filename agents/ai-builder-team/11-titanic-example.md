# Titanic-inspired concept — illustrative example

This is a fictional teaching example for [the walkthrough](09-video-walkthrough.md). It follows the kind of product exercise used in the workshop. These are newly written sample review notes, not a transcript, a live model run, customer evidence or a working emergency product.

Use the Titanic prompt in [10-demo-prompts.md](10-demo-prompts.md) after installing the Evals Agent and the expanded collaboration protocol. Your output will differ.

## Starting point

**Proposed concept:** a family-preparedness planner that helps a household agree on contacts and coordination plans in advance.

**Evidence available:** the exercise brief only. There are no customer interviews, demand estimates, competitor comparisons or technical tests.

**Question:** which part of this idea is worth researching and prototyping first?

## 1. Viewpoints

**PM Twin:** Start by investigating whether households struggle to make and maintain a shared plan. Propose a simple preparedness checklist and contact sheet. Willingness to use it is an assumption.

**CTO:** Separate an offline-readable document from live location sharing or message delivery. Do not promise that a device can send messages without a usable network. Research platform constraints and test each proposed capability before choosing the architecture.

**UX Lead:** Map how family members create, find, understand and update the plan. Ask whose device access, permissions or accessibility needs the concept overlooks. We have no evidence yet that people would find the information when needed.

## 2. Challenge and revisions

| Challenge | Resulting change |
| --- | --- |
| CTO questions a promise of always-available location and SMS features. | Remove those promises from the first concept; create explicit feasibility questions. |
| UX Lead questions whether a checklist solves the user's actual coordination problem. | Put interviews and a small comprehension test before expanding the feature set. |
| PM Twin questions a large first-release scope. | Explore one narrow planning task before adding alerts or integrations. |

## 3. Provisional recommendation

Investigate the preparation workflow and test a simple concept with appropriate participants. In parallel, have an engineer review the proposed offline behavior. Keep live messaging and location features as unvalidated options.

This recommendation proposes research and a bounded prototype. It is not evidence that the product should launch or be used in emergencies.

## 4. Example Evals report

### Verdict

**Needs grounding before acting.** The target need, differentiation, adoption and technical assumptions are unverified. Proceed only with the proposed research and feasibility checks.

### Claim review

| Claim | Available evidence | Classification | Check needed |
| --- | --- | --- | --- |
| The brief asks us to explore family preparedness. | The supplied fictional exercise. | EVIDENCED, as a brief requirement only | Confirm the user's real project objective if adapting it. |
| Families would adopt a separate planning app. | None supplied. | ASSUMPTION | Investigate current behavior, alternatives and adoption barriers. |
| Reducing coordination effort could be useful. | A general product hypothesis. | PATTERN | Establish whether that problem matters in the target setting. |
| Offline access will work as users expect. | No implementation or device test. | ASSUMPTION | Define what works offline and test it. |
| The concept is differentiated and has a viable business model. | No market or business evidence. | ASSUMPTION | Review alternatives and test the business assumptions. |

### Illustrative scorecard

These scores are examples of applying the starter rubric, not scores from the recording.

| Dimension | Score | Basis and remaining gap |
| --- | --- | --- |
| Grounding | 1/2 | Claims are labeled, but important product assumptions lack evidence. |
| Completeness | 1/2 | Scope and constraints are discussed; target segment and user needs remain unresolved. |
| Confidence calibration | 2/2 | The recommendation is explicitly provisional. |
| Logical integrity | 2/2 | The recommendation follows the stated uncertainties and avoids unsupported promises. |
| Gaps and escalation | 1/2 | Checks are named; participants, owner and decision thresholds still need agreement. |
| **Total** | **7/10** | **A review score, not 70% confidence or a readiness measure.** |

The material gaps keep the verdict at **Needs grounding before acting**, even with a 7/10 total.

### Decision for the user

Choose the target setting and the first question to investigate. Agree who will conduct the research and technical checks. Set the experiment's success/failure criteria before running it, then bring the resulting evidence back to the team.

## What to look for in your own run

- Three distinct builder perspectives and a separate Evals report.
- Specific objections that change the proposal.
- Claims tied to actual supplied evidence, with missing support clearly named.
- Feasibility questions that remain questions until tested.
- A next action proportionate to the evidence, with the user deciding what proceeds.
