# AI Product Academy Agent Lab

Nine runnable, model-backed product management assistants with a shared Python CLI. These are focused single-workflow agents, not autonomous tool-using systems or hosted services. Each has its own instructions and fictional example. By [Dr. Marily Nika](../ABOUT.md).

| Agent | Purpose | Portable skill |
|---|---|---|
| [AI Launch Reviewer](ai-launch-reviewer/README.md) | Review AI feature release readiness | [SKILL.md](../skills/ai-feature-go-no-go/SKILL.md) |
| [AI PRD Builder](ai-prd-builder/README.md) | Draft an AI-specific product requirements document | [SKILL.md](../skills/ai-prd-builder/SKILL.md) |
| [AI Evals Designer](ai-evals-designer/README.md) | Design evaluation datasets and rubrics | [SKILL.md](../skills/ai-evals-designer/SKILL.md) |
| [Minimum Viable Quality Agent](minimum-viable-quality/README.md) | Propose context-sensitive minimum quality gates | [SKILL.md](../skills/minimum-viable-quality/SKILL.md) |
| [AI User Research Agent](ai-user-research/README.md) | Synthesize qualitative user research | [SKILL.md](../skills/ai-user-research/SKILL.md) |
| [Agent Readiness Reviewer](agent-readiness-reviewer/README.md) | Assess autonomy, permissions and recovery risks | [SKILL.md](../skills/agent-readiness-reviewer/SKILL.md) |
| [AI PM Interview Coach](ai-pm-interview-coach/README.md) | Practice AI PM interview reasoning | [SKILL.md](../skills/ai-pm-interview-coach/SKILL.md) |
| [AI Product Metrics Agent](ai-product-metrics/README.md) | Design product, quality and guardrail metrics | [SKILL.md](../skills/ai-product-metrics/SKILL.md) |
| [AI PM Twin](ai-pm-twin/README.md) | Support product decisions and weekly planning | [SKILL.md](../skills/ai-pm-twin/SKILL.md) |

## Setup
Clone or download the repository. From its root, use Python 3.10+:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r agents/requirements.txt
python agents/run.py ai-launch-reviewer --dry-run
python -m unittest discover -s agents -p 'test_*.py'
```

Windows PowerShell activation: `.venv\\Scripts\\Activate.ps1`.

For a live response, set `OPENAI_API_KEY` and `OPENAI_MODEL` to your own API key and an available model ID, using your shell or secret manager. Never put keys in Git. For Anthropic use `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` and `--provider anthropic`. Then run:

```bash
python agents/run.py ai-launch-reviewer --provider openai --allow-api
```

`--dry-run` is offline. `--allow-api` sends the instructions and selected input to the provider and may incur charges. Use only fictional or approved data. To supply a file, add `--input path/to/file.md`. Output is Markdown printed to your terminal; redirect to a local file if desired. This starter has no autonomous writes, external tools, persistent memory or hosted UI. Live API execution requires your own credentials and model access.

## Existing Builder Team
[AI Builder Team prompts and walkthrough](ai-builder-team/README.md).
