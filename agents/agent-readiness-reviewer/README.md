# Agent Readiness Reviewer

Assess autonomy, permissions and recovery risks. By [Dr. Marily Nika](../../ABOUT.md).

## Run locally
From the repository root, follow the [Agent Lab setup](../README.md), then preview with no API calls:

```bash
python3 agents/run.py agent-readiness-reviewer --dry-run
```

To generate a real response, set your chosen provider API key and model ID as described in the setup, then run:

```bash
python3 agents/run.py agent-readiness-reviewer --provider openai --allow-api
```

Use `--input path/to/approved-data.md` for your own approved data, or the default fictional example. API usage may incur charges. Outputs require review.

[Instructions](instructions.md) · [Example](example.md) · [Agent Lab](../README.md)
