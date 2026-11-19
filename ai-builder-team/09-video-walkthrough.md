# How to build your own AI product team in Claude

*A PM Twin, a CTO, a UX Lead, and an Evals Agent. Here’s the setup, including what to download and where to put it.*

I’m on my way to Montreal, my favorite city, and the airplane WiFi says “messaging only.”

Funny, because that’s enough for quite a lot of my work now. I can send an idea to my AI builder team, ask for feedback, and work through the decisions in the chat.

The team starts with three roles: my PM Twin, a CTO, and a UX Lead. Then I add an Evals Agent to check the claims they’re making. That last part is particularly useful when the discussion sounds convincing and I’m tempted to move on.

Here’s how to set it up yourself. I’ve put the starter files on GitHub so you can follow along without writing every instruction from scratch. They reproduce the workflow I teach; they’re reusable starting points, not a word-for-word copy of every prompt on screen.

## 1. Get the files from GitHub

Open the [AI Product Management Toolkit](https://github.com/marilynika/ai-product-academy-toolkit).

If GitHub is new to you:

1. Stay on that main repository page.
2. Click **Code**, then **Download ZIP**.
3. Unzip the download on your computer.
4. Open the extracted folder, then open **ai-builder-team**.

You don’t need to install Git or use a terminal. The `.md` files are Markdown files, which are just text with some formatting. You can open them in a text editor.

If you’d rather copy one file at a time, open it on GitHub, click **Raw**, and copy the plain text. Here are [GitHub’s download instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-files-from-github) if you get stuck.

These are the files we’ll use:

| File | Where it goes |
|---|---|
| [01-pm-twin.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/01-pm-twin.md) | Project knowledge, after you personalize it |
| [02-cto.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/02-cto.md) | Project knowledge |
| [03-ux-lead.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/03-ux-lead.md) | Project knowledge |
| [05-collaboration-protocol.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/05-collaboration-protocol.md) | Project instructions for the initial three-role team |
| [07-evals-agent.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/07-evals-agent.md) | Project knowledge when we add the evaluator |
| [08-collaboration-with-evals.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/08-collaboration-with-evals.md) | Replaces the initial project instructions when we add the evaluator |

Use **UX Lead** for this walkthrough. The separate UX Researcher and Product Designer files are optional alternatives for a different team setup.

## 2. Create your Claude Project

Open Claude, go to **Projects**, and select **+ New Project**. Call it **My builder team**. [Claude’s project setup guide](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) shows the current controls.

We’re going to use two different places inside the project:

- **Project instructions:** the rules for how the team works together.
- **Project knowledge:** the documents defining each role.

The project description isn’t the place to give Claude your working product context. We’ll put that context into the chat when we give the team its first task.

This setup uses one assistant taking different roles in a conversation. Creating a project and uploading files doesn’t create separate agents running independently in the background.

## 3. Make the PM Twin yours

My PM Twin reflects my goals and the way I approach product decisions. Yours should reflect you.

Open `01-pm-twin.md` and edit the personal context. Include your priorities, product principles, preferred writing style, and the tradeoffs you usually care about. If you’re working on a particular product, include its stage and constraints.

You can also open a regular Claude chat, attach the PM Twin file, and use this:

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

Read the result and save your version. Also look through the CTO and UX Lead files. The CTO should examine feasibility, reliability, cost, and delivery. The UX Lead covers both user research and the experience someone would actually have using the product.

In the demo, I ask Claude to generate these role documents and the collaboration rules. You can do that too; the [Start Here file](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/00-start-here.md) includes that route. The supplied files let you start with something concrete and edit it.

## 4. Put the collaboration rules in project instructions

Open `05-collaboration-protocol.md` and copy the text inside its prompt block.

Back in your project, open **Set project instructions**, paste the protocol, and save it.

The starter protocol gives the discussion four stages: each role offers its perspective, the roles challenge assumptions, they revise their positions, and the team produces a decision for you to review.

Pay attention to what disagreement has to produce. An objection should change the proposal, lead to an experiment, identify an accepted risk, or leave a clear unresolved question. Otherwise you can spend a surprising amount of time reading a debate that goes nowhere.

## 5. Add the three roles to project knowledge

Use the project’s **+** upload control to add:

1. Your personalized `01-pm-twin.md`.
2. `02-cto.md`.
3. `03-ux-lead.md`.

Check that all three appear in project knowledge. If you copied text from GitHub instead of downloading, save each role as its own text or Markdown file before uploading it.

You should now have three role documents in knowledge and the collaboration protocol in instructions.

## 6. Give the team a real decision

Start a chat inside **My builder team**. Attach a PRD or PRFAQ you want reviewed, or write a couple of sentences about an idea.

In the workshop I use a draft subscription concept as an initial exercise. Your own unfinished document is a good place to start. Give the team enough context to question the proposal usefully:

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

Look for specific objections. “We should consider scalability” gives you little to work with. An objection about an integration, missing user evidence, or an unclear recovery path gives you something to investigate.

If you only get a polished final answer, ask:

```text
Show me a concise review summary from the PM Twin, CTO, and UX Lead.
For each, include their main objection, the change they recommend, and
what evidence would resolve the question. Then update the proposal.
```

## 7. Add the Evals Agent—and update the instructions

This is the part I’d spend extra time on.

The three roles can make a discussion feel thorough while still relying on the same unsupported assumption. The Evals Agent reviews their claims and records where the support is missing.

In the demo, I ask the team to create that role and revise its collaboration rules. Here’s a reusable version of that request if you want to customize the setup:

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

For the supplied setup, add `07-evals-agent.md` to **project knowledge**. Then open `08-collaboration-with-evals.md` and use the text inside its prompt block to **replace the earlier project instructions**. Save the change.

Do both. Adding the evaluator document to knowledge doesn’t tell the team when to call on it. The updated instructions make the evaluation part of the workflow.

If you generated your own versions, use your reviewed evaluator file and updated protocol together instead. Keep one current protocol in instructions.

## 8. Try the example from the demo

I give the team a slightly odd starting point: a product inspired by *Titanic*. It develops into a disaster-preparedness and family-safety concept.

Start a new chat inside the project so you can check the updated setup. Give it the context again if you’re continuing your own project. For the demo exercise, use this prompt:

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

Your output will vary. I’ve included an [illustrative example](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/11-titanic-example.md) so you can inspect the structure. It isn’t a transcript of the recorded output.

## 9. Read the scorecard before accepting the recommendation

The useful question is: what has the team actually established?

The claim review should distinguish:

- **EVIDENCED:** supported by an identifiable source or observation provided to the team.
- **PATTERN:** a general analogy or commonly observed pattern; it is not evidence for this product.
- **ASSUMPTION:** an unverified premise the recommendation depends on.

For each material claim, look for its source and the next check. If the team says families would use the app, what supports that? If it proposes an offline feature or SMS fallback, what has actually been verified about the conditions it would work under?

In the starter files, the five dimensions are each scored from 0 to 2, giving a total out of 10. Read the explanations. A high total doesn’t resolve a missing piece of evidence. Material unsupported claims should still produce **“Needs grounding before acting.”**

In the demo, the evaluator surfaces questions about the market, differentiation, and business model. That gives me a useful list of things to investigate before getting attached to the concept.

The evaluator is another AI-generated review. Check consequential claims against real sources, research, and technical work.

## 10. Keep the decision and improve the setup

Once you’ve reviewed the discussion, ask for something you can use:

```text
Prepare a short decision record I can save as Markdown.
Include the proposed decision, alternatives, material assumptions,
unresolved objections, evidence to collect, and the next experiment.
Mark anything awaiting my decision as pending.

Then suggest specific edits to the role instructions or collaboration
protocol based on this session. Show the proposed edits separately so I
can review them before updating my saved files and project instructions.
```

Save the decision locally. When you change a role, keep the previous version and update the corresponding knowledge file. When you change the team’s workflow, update project instructions too.

All the copyable prompts from this walkthrough are also in [10-demo-prompts.md](https://github.com/marilynika/ai-product-academy-toolkit/blob/main/ai-builder-team/10-demo-prompts.md).

### If something isn’t working

| What you see | What to check |
| --- | --- |
| A generic answer with no role labels | Are you chatting inside the project? Are the three role files in knowledge and the protocol saved in instructions? |
| No Evals report | Check both changes: the evaluator file is in knowledge **and** the evaluator-enabled protocol has replaced the old instructions. |
| A fourth builder role you didn’t intend to add | Remove the optional UX Researcher/Product Designer documents from this project and keep the combined UX Lead. |
| The team invents interviews or metrics | Ask it to remove unsupported claims, label assumptions and rerun the evaluation. |
| A new chat has lost your latest decision | Paste the saved decision record and current evidence, or add them to project knowledge. |

### Optional: keep your template changes on GitHub

If you want your own GitHub copy, sign in and use **Fork** on the main repository page. Choose your account under **Owner**, then click **Create fork**. Open a file in your fork, choose the pencil/edit control, make the change, and select **Commit changes** to save it.

A public fork is public. Keep personal context, company documents, and private decision records on your own computer or in an approved private workspace. Uploading a file to Claude also doesn’t update GitHub; they’re separate copies.

Start with one decision you’re already working through. I’d love to hear which objection made you reconsider your first idea.

