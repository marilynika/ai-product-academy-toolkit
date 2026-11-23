# Start here — assemble your AI Builder Team

The walkthrough starts with **PM Twin + CTO + UX Lead**, then adds an **Evals Agent**.

Read the [full step-by-step walkthrough](09-video-walkthrough.md) for GitHub download instructions, Claude setup and the demo prompts. The files here are reusable starter versions of the workshop setup, not a transcript of prompts generated on screen.

## Choose your starting point

**Use the provided files:** personalize [01-pm-twin.md](01-pm-twin.md), review [02-cto.md](02-cto.md) and [03-ux-lead.md](03-ux-lead.md), and install them using the table below.

**Generate your own roles, as in the workshop:** paste this into an ordinary Claude chat first. Review the generated documents before installing them.

```text
Help me create my AI builder team in a Claude Project.

Create four separate documents:
1. A PM Twin role prompt that reflects my product principles, goals and writing style while challenging weak assumptions.
2. A CTO role prompt covering architecture, feasibility, reliability, cost and technical trade-offs.
3. A UX Lead role prompt covering both user research and user experience.
4. A collaboration protocol to put in project instructions, explaining how those three roles contribute, challenge assumptions, revise proposals and recommend a next action.

My name and role: [NAME / ROLE]
My current goal: [GOAL]
My product principles: [PRINCIPLES]
My writing style and a short sample: [STYLE / SAMPLE]
My constraints: [TIME / BUDGET / SCOPE]

Make each document complete and copyable. Leave missing personal details as placeholders. Ask the team to distinguish supplied facts from assumptions and show concise critiques and revisions.
```

## Put each document in the right place

| Document | Where it goes |
| --- | --- |
| PM Twin, CTO, UX Lead | Project knowledge/context |
| Base collaboration protocol | Project instructions |
| Your product idea, PRD or PRFAQ | Chat inside the project, or project knowledge if it should be reused |
| Evals Agent, when you add it | Project knowledge/context |
| Collaboration protocol with Evals | Replaces the base project instructions |

Use the provided files together, or review your generated set for matching role names and references. If you mix them, update any filenames referenced in the instructions.

## Give the team context

Start a chat **inside the project** and paste a filled-in version of this brief. The project title and description are not a substitute for giving the model your product context.

```text
Use the PM Twin, CTO and UX Lead in this project's knowledge and the active collaboration protocol.

First confirm which role documents you can use. If one is missing, tell me.

MY CONTEXT
- Company/project: [NAME]
- Product and stage: [WHAT EXISTS TODAY]
- Target users and their job: [WHO / WHAT THEY NEED]
- Product principles: [PRINCIPLES]
- Desired outcome: [OUTCOME]
- Constraints: [TIME / BUDGET / TEAM / DATA]
- Evidence available: [FACTS AND SOURCES, OR "NONE YET"]
- Key unknowns: [UNKNOWNS]
- Decision for this session: [QUESTION]

Give me the three roles' views, the meaningful objections, the revisions and a recommendation. Keep the discussion concise and show what changed. Label assumptions; do not invent customer research or test results.
```

If you have added the evaluator and replaced the instructions, include: "Finish with the Evals Agent's claim table, scorecard and verdict."

## Add the evaluator

1. Add [07-evals-agent.md](07-evals-agent.md) to project knowledge.
2. Replace project instructions with the complete block in [08-collaboration-with-evals.md](08-collaboration-with-evals.md) and save.
3. Start a new chat in the project, supply the product context again, and run a prompt from [10-demo-prompts.md](10-demo-prompts.md).
4. Check that you receive three builder viewpoints **and** an Evals report. If not, use the troubleshooting section in the walkthrough.

This chat setup produces role-based reviews. Separate agent execution and implementation are different workflows; installing these prompts does not build or ship software.

Keep private customer or company material in an approved private workspace. Do not commit it to this public repository.
