# Alternative exercise — an AI customer-feedback copilot

This is a **fictional practice scenario**, not a customer case study or the video demonstration. For the Titanic-inspired exercise, use [11-titanic-example.md](11-titanic-example.md).

## Context to paste into Start Here

- Company/project: FeedbackFlow (fictional).
- Product and stage: SaaS dashboard, early prototype.
- Target users: PMs who triage support requests and customer feedback.
- Goal: reduce time from feedback intake to a useful insight.
- Constraints: two engineers, four weeks, limited labeled data; customer PII must not be exposed.
- Scenario premise: feedback arrives in multiple channels.
- Evidence available: no actual research, measured baseline or technical validation.
- Decision: an autonomous prioritization agent or a human-reviewed clustering assistant?

## Illustrative viewpoints

**PM Twin:** Propose a human-reviewed digest before autonomous prioritization. Whether faster synthesis is useful still needs evidence.

**CTO:** Start with one source. Investigate ingestion, PII handling, traceability and evaluation before promising an integration.

**UX Lead:** Test whether PMs can trace a cluster back to its underlying feedback and correct it. We do not yet know whether a weekly digest fits their workflow.

## Material disagreements and revisions

- CTO challenges PM: multiple integrations may not fit four weeks. Narrow the first test to one source.
- UX Lead challenges PM: time saved may hide missed important issues. Measure issue coverage as well as time.
- PM challenges UX Lead: extensive editing may expand scope. Test rename, merge and exclude first.

These are illustrative objections, not results from a real team or customer study.

## Example recommendation and Evals questions

Explore a small, human-reviewed clustering assistant. Before committing to the product, check the user workflow and test summary traceability on an appropriate dataset.

The Evals Agent should flag the assumed user need, untested integration estimate, missing baseline and unvalidated measures. No measured success rate is available. Success and failure criteria need to be set from actual evidence.

## Follow-up exercise

```text
For this fictional exercise, change two scenario assumptions: the integration estimate has doubled, and the proposed weekly digest does not fit the users' workflow. Have the affected roles revise the smallest useful scope. Then have the Evals Agent identify which assumptions still require real research.
```
