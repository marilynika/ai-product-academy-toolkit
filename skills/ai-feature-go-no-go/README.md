# AI Feature Go/No-Go Reviewer

An Agent Skill by Dr. Marily Nika / AI Product Academy, based on the [original review kit](../../ai-feature-go-no-go/README.md).

## Install from a terminal
Clone the toolkit, then copy this skill into your project. Run these commands from your target project's root (choose the relevant environment).

```bash
git clone https://github.com/marilynika/ai-product-academy-toolkit.git /tmp/aipa-toolkit
# Claude Code
mkdir -p .claude/skills
cp -R /tmp/aipa-toolkit/skills/ai-feature-go-no-go .claude/skills/
# Codex
mkdir -p .agents/skills
cp -R /tmp/aipa-toolkit/skills/ai-feature-go-no-go .agents/skills/
```

Start the relevant agent in your project and ask: "Use the ai-feature-go-no-go skill to review this feature. Here are my sanitized eval results and worst outputs." In other chat environments, upload the skill folder as a ZIP if skill import is supported, or provide SKILL.md and both reference files as context. No external runtime dependencies. Updates require re-copying or re-importing.

## Try it
Use the fictional example in the [review kit](../../ai-feature-go-no-go/example-meeting-assistant.md). With only diagnostic cases and no representative evidence, the expected outcome is insufficient evidence or no-go if a blocker is established; never an unconditional go.

Do not upload confidential data. The skill provides a recommendation, not launch authorization. See repository reuse terms.
