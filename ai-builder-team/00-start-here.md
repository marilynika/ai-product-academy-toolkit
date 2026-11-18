# Start here — assemble your AI Builder Team

Copy this prompt into your AI workspace. Add the four role files and collaboration protocol as project context.

```text
Build my AI-native product team using the attached PM Twin, CTO, UX Researcher, Product Designer, and Collaboration Protocol documents.

MY CONTEXT
- Company/project: [NAME]
- Product and stage: [WHAT EXISTS TODAY]
- Target users and their jobs: [WHO / WHY]
- My product philosophy: [PRINCIPLES]
- Business goal: [MEASURABLE OUTCOME]
- Constraints (time, budget, team, data, legal): [CONSTRAINTS]
- What we've learned so far (with evidence): [FACTS]
- Key unknowns: [UNKNOWN]
- Decision for this session: [QUESTION]

Run the team as four distinct perspectives, not four affirmations:
1. PM Twin defines the user problem, desired outcome and strategic choice.
2. CTO tests technical feasibility, reliability, cost and delivery risk.
3. UX Researcher identifies assumptions, alternative user explanations and evidence needed.
4. Product Designer proposes a clear, controllable workflow and failure states.
5. Run the collaboration protocol: independent perspectives, substantive objections, revisions, and decision.

Do not invent customer interviews, metrics or technical validations. Mark assumptions as assumptions. If information is missing, make provisional recommendations and list the critical question to investigate.

Output:
- Decision statement
- Four brief independent viewpoints
- Three material disagreements and what changed
- Recommended direction and trade-offs
- Fastest experiment to falsify the riskiest assumption
- Owner, success metric, and next action
```

## Tool setup notes
- **Claude Projects:** store files as project knowledge; put the orchestration request in the chat.
- **Claude Code or agent frameworks:** use separate role files/agents where supported; keep shared collaboration rules accessible to all.
- **Chat-based tools:** paste or attach the files and ask for clearly labeled role turns. This simulates multiple perspectives but is not independent agent execution.

Never include confidential customer data or unpublished company information without authorization.
