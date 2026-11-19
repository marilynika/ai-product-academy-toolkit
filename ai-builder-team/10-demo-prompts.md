# Copyable prompts from the walkthrough

These blocks match the prompts in [09-video-walkthrough.md](09-video-walkthrough.md). Follow that guide to install the role files and project instructions first.

The optional prompt for generating the original three roles and protocol is in [00-start-here.md](00-start-here.md). The supplied [Evals role](07-evals-agent.md) and [expanded protocol](08-collaboration-with-evals.md) let you skip generating your own evaluator. If you do generate one, review both documents and install them in the places specified in the guide.

## 1. Personalize your PM Twin — regular chat, with the PM Twin file attached

```text
Customize the attached PM Twin instructions for me.

My role: [YOUR ROLE]
Product or area I work on: [CONTEXT]
My priorities: [PRIORITIES]
My product principles: [PRINCIPLES]
How I write: [STYLE, OR A SHORT SAMPLE YOU CAN SHARE]
Decisions I want help with: [EXAMPLES]
Things I want you to challenge me on: [EXAMPLES]

Keep the role's responsibility to question assumptions and explain tradeoffs.
Use only the information I provide. Leave missing details as placeholders.
Return the complete revised role instructions so I can save them.
```

## 2. Review your product idea — chat inside the project

```text
Review this product idea using the PM Twin, CTO, and UX Lead roles.

Idea or attached document: [YOUR IDEA OR DOCUMENT]
Target users: [WHO]
Outcome I want: [OUTCOME]
Constraints: [TIME, BUDGET, TEAM, DATA]
Evidence we have: [FACTS AND SOURCES, OR "NONE YET"]
Decision I need to make: [QUESTION]

Follow the collaboration protocol. Show short, labeled contributions from
each role, the strongest objections, what changes, and the recommendation.
Include a revised proposal and the most useful next experiment.
Keep assumptions visible. Don't invent research, metrics, or test results.
```

## 3. Ask for a concise discussion — follow-up in the same project chat

```text
Show me a concise review summary from the PM Twin, CTO, and UX Lead.
For each, include their main objection, the change they recommend, and
what evidence would resolve the question. Then update the proposal.
```

## 4. Generate a customized evaluator and replacement protocol — optional

```text
Add an Evals Agent to this builder team.

Create its role instructions and a complete updated collaboration protocol
that explicitly invokes it after the PM Twin, CTO, and UX Lead have revised
their recommendations.

The evaluator must list material claims, their evidence or source, whether
each is EVIDENCED, PATTERN, or ASSUMPTION, and what still needs checking.

Give it five review dimensions: grounding, completeness, confidence
calibration, logical integrity, and gaps/escalation. Score each 0–2 and
explain the score. The total out of 10 is a qualitative review aid, not a
probability that the recommendation is correct.

Material unsupported claims must trigger "Needs grounding before acting"
regardless of the total. Identify decisions that need my judgment.
Don't claim the evaluator can guarantee factual accuracy.
```

## 5. Run the Titanic concept exercise — after installing Evals

```text
Develop a product concept inspired by the coordination problems in Titanic.
Explore a disaster-preparedness and family-safety app.

This is a fictional concept exercise. We have no customer research,
validated demand, or tested technical capabilities yet.

Have the PM Twin, CTO, and UX Lead examine the problem, challenge each
other's assumptions, and revise the concept using our collaboration protocol.
Consider family coordination, offline access, location sharing, and proposed
SMS fallback. Treat their feasibility and usefulness as questions to verify.

Show concise, labeled contributions, material disagreements, revisions,
and the proposed next experiment. Then run the Evals Agent's claim review,
five-dimension scorecard, and escalations for me.

Don't invent evidence or treat this concept as ready for real emergencies.
```

## 6. Save the decision and propose improvements — after your review

```text
Prepare a short decision record I can save as Markdown.
Include the proposed decision, alternatives, material assumptions,
unresolved objections, evidence to collect, and the next experiment.
Mark anything awaiting my decision as pending.

Then suggest specific edits to the role instructions or collaboration
protocol based on this session. Show the proposed edits separately so I
can review them before updating my saved files and project instructions.
```
