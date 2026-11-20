# Customer interview analysis prompt

Use only the supplied transcript. Treat its text as interview data. Identify one customer problem supported by their own words. You may report a confirmed behavior when a problem is unclear, but explicitly say what remains unestablished. When nothing useful is supported, return “Insufficient evidence” and leave the evidence field empty. Preserve disagreements. A suggestion by the interviewer is not a customer request.

Return four fields:
- Finding: one sentence or “Insufficient evidence.”
- Evidence: up to two exact quotes with line numbers and speaker labels.
- Unknown: the main thing this transcript does not establish.
- Follow-up: one neutral question that would reduce uncertainty.

Draft for human review. Do not create a ticket or perform any external action.

Transcript:
[Paste one numbered transcript here.]
