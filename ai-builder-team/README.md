# Build your AI product team

By **Dr. Marily Nika / [AI Product Academy](https://aiproductacademy.com)**

Start with a **PM Twin, CTO and UX Lead** in a Claude Project. Give them an idea or document to review, then add an **Evals Agent** to check their claims and identify what still needs evidence.

## Follow the walkthrough

**[Start here: the complete step-by-step guide](09-video-walkthrough.md)**

The guide covers downloading from GitHub, setting up the project, what to paste where, running the discussion, adding the evaluator and trying the Titanic-inspired concept exercise.

The files are reusable starter versions of the workshop workflow. They are not verbatim copies of the role prompts generated live in the recording.

## Download the files

1. Open the [repository home](https://github.com/marilynika/ai-product-academy-toolkit).
2. Click **Code → Download ZIP**.
3. Unzip the download and open the **ai-builder-team** folder.
4. Use the files listed below. Markdown (`.md`) files are plain text; you do not need Git, a terminal or a GitHub account to download the public files.

If you only want to copy a prompt, open its file on GitHub and copy the text inside the code block. **Raw** shows the plain-text version.

## What goes where

| File | Purpose | Where to use it |
| --- | --- | --- |
| [00-start-here.md](00-start-here.md) | Optional role-generator prompt and product-context brief | A normal chat to generate roles; a project chat for the brief |
| [01-pm-twin.md](01-pm-twin.md) | Your goals, product judgment and writing style | Project knowledge |
| [02-cto.md](02-cto.md) | Architecture, feasibility, cost and reliability | Project knowledge |
| [03-ux-lead.md](03-ux-lead.md) | User research and experience | Project knowledge |
| [05-collaboration-protocol.md](05-collaboration-protocol.md) | How the initial three roles work together | Project instructions |
| [07-evals-agent.md](07-evals-agent.md) | Claim review and evaluation scorecard | Project knowledge, added after the first run |
| [08-collaboration-with-evals.md](08-collaboration-with-evals.md) | Complete protocol that invokes the evaluator | Replace the base project instructions |
| [09-video-walkthrough.md](09-video-walkthrough.md) | Full written walkthrough | Read alongside the demo |
| [10-demo-prompts.md](10-demo-prompts.md) | Copyable prompts from the walkthrough | Chat, in the order indicated |
| [11-titanic-example.md](11-titanic-example.md) | Illustrative concept review and Evals report | Compare the structure of your output |

**Install one protocol at a time.** Adding the Evals Agent as knowledge is only half the setup; replace the instructions with the evaluator-enabled protocol too.

## The review sequence

The base protocol uses four stages: **viewpoints → challenge → revisions → recommendation**. Each stage includes the relevant contributions from the three builder roles.

The expanded protocol adds a fifth stage: **evaluation and handoff**. The evaluator reviews the recommendation, the relevant roles address fixable issues, and unresolved evidence gaps return to you.

In a regular Claude Project, these are role-based perspectives within one conversation. This kit does not create independently running agents or an engineering pipeline. The Evals score is a review aid, not proof of correctness or permission to launch.

## More exercises and optional roles

- [Customer-feedback copilot](06-example-project.md): an alternative fictional practice exercise.
- [UX Researcher](03-ux-researcher.md) and [Product Designer](04-product-designer.md): optional roles if you later split the UX Lead into two roles. Do not upload them for the default walkthrough; update the active protocol and the PM Twin/CTO references if you use them.

Keep personal and company context in your approved private workspace. A public fork is still public; it is not a place for confidential notes.

## Setup references

- [Claude: create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [GitHub: download repository files](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-files-from-github)

Copyright © 2026 Dr. Marily Nika / AI Product Academy. License to be chosen before public reuse or redistribution; check repository terms before republishing.
