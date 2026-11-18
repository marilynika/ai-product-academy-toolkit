# Example project — an AI customer feedback copilot

This is a **fictional practice scenario**, not a customer case study.

## Context to paste into Start Here
- Company/project: FeedbackFlow (fictional)
- Product and stage: SaaS dashboard, early prototype
- Target users: PMs who triage support requests and customer feedback
- Business goal: reduce time from feedback intake to prioritized insight
- Constraints: 2 engineers, 4 weeks, limited labeled data, cannot expose customer PII
- Facts: feedback currently arrives in multiple channels; no validated baseline yet
- Decision: should we launch an autonomous prioritization agent or a human-reviewed clustering assistant?

## Example first-round outputs (illustrative)
**PM Twin:** Start with a human-reviewed weekly digest. The user value is faster synthesis; autonomous prioritization assumes too much about strategy and impact.

**CTO:** Use deterministic ingestion and a constrained clustering/summarization pipeline. PII filtering, traceability, evaluation and a reversible review path are mandatory. Do not let a model silently change roadmap priorities.

**UX Researcher:** We do not know whether PMs trust clusters or what their review workflow looks like. Observe five real triage sessions, then test whether people can trace summaries back to sources.

**Product Designer:** Make each cluster expandable to the underlying feedback. Provide merge/split/edit controls, uncertainty cues, and a clear "review before sharing" state.

## Productive disagreement
- **CTO challenges PM:** Four weeks may not support reliable automatic ingestion from all channels. **Revision:** pilot one channel.
- **Researcher challenges PM:** "Faster" may not matter if synthesis misses high-impact customers. **Revision:** measure recall of important issues as well as time saved.
- **Designer challenges CTO:** A technically accurate cluster without source traceability is unusable. **Revision:** require source drill-down in v1.
- **PM challenges Designer:** Full editing could balloon scope. **Revision:** start with rename, merge and exclude.

## Example decision
Pilot a human-reviewed feedback clustering assistant in one data source with source links and simple corrections. Run an evaluation on a representative labeled set and a usability test before expanding. Success metrics and launch thresholds must be defined from actual baseline and failure consequences; don't invent them.

## Follow-up challenge prompt
"Now imagine the CTO's integration estimate doubled and the UX Researcher found that users rarely open a weekly digest. Rerun the disagreement protocol and recommend a revised MVP."
