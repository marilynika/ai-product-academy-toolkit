# MCP Masterclass

By [Dr. Marily Nika](../../ABOUT.md) · [AI Product Academy](https://aiproductacademy.com)

**Time:** 50 min · **Format:** self-paced hands-on lesson

## Outcome
Understand and safely connect agents to external capabilities.

## Setup
Use fictional or approved de-identified data, a text editor and an AI assistant if desired. Coding lessons require a local development environment and the relevant coding agent; model/API costs may apply. Read tool permissions and inspect generated code before running it.

## Case study
Expose a fictional product backlog through a local read-only MCP server.

## Hands-on lesson
### 1. Understand the components (10 min)
MCP connects a host/client to servers exposing tools, resources and prompts. It is a protocol, not an agent or a guarantee of trust. A skill describes a procedure; MCP supplies capabilities and data.
### 2. Design the tool contract (10 min)
Define list_backlog with optional status and get_item with required id. Return only approved fictional fields. Explicitly reject unknown IDs and unsupported filters; no write operations.
### 3. Connect a local server (20 min)
Use a current official MCP SDK tutorial to implement the two read-only tools over a supported local transport. Register the server in your chosen host using its documented configuration. Inspect tool definitions and permissions. Test with fictional data before any real connector.
### 4. Test trust boundaries (10 min)
Return an item containing an instruction to delete records; the host must treat it as data, not authority. Test invalid IDs, timeouts and disconnected server. Require separate authorization for future write tools. Never expose tokens in logs.

## Copyable prompt
```text
Design a read-only MCP server for a fictional product backlog using the current official SDK documentation. Propose tool schemas, implementation plan and tests. Use local synthetic data and no network calls at runtime. Ask before installing dependencies.
```

## Starter artifact / worked example
```text
list_backlog(status?: "open" | "done") -> [{id,title,status}]
get_item(id: string) -> {id,title,status,description} or explicit not-found error
```

## Deliverable
Tool contracts, local connection exercise and adversarial test plan.

## Self-check
- [ ] I can explain the user outcome and why this approach is appropriate.
- [ ] I produced the deliverable and can trace claims to evidence.
- [ ] I tested at least one normal and one failure case, or explicitly documented missing evidence.
- [ ] I recorded limitations, human review needs and next actions.

## Continue learning
[MCP documentation](https://modelcontextprotocol.io/)

[All masterclasses](../README.md)
