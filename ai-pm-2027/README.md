# AI PM Portfolio Exercise: Customer Interview Assistant

Build a read-only assistant that turns one interview into an evidence-backed finding and one follow-up question. Use a chat model, fresh conversations, and a spreadsheet or text editor. The five cases are synthetic.

1. Copy [prompt.md](prompt.md) into a fresh conversation and paste one transcript from [cases.md](cases.md) in the input slot. Repeat each case in its own conversation.
2. Read each output against the expected behavior after running it. Verify the quote is verbatim, attributed to the right speaker, and supports the finding. Score the output with [scorecard.csv](scorecard.csv). Mark unsupported requirements or invented quotes as critical failures, even when the rest reads well.
3. Change one variable at a time, then rerun the same cases. Keep a failing output and record what changed. Add a fresh case before treating an improvement as general.
4. Ask a reviewer to turn a fresh synthetic interview into a shareable finding with and without the assistant. Compare time to a verified finding and corrections. Try matched transcripts or vary order to reduce practice effects.

For case 03, an acceptable finding is “The participant reports using screenshots.” The evidence is line 2. The need for CSV export is unestablished. One follow-up is “What do you do with the screenshots after you take them?” This is an illustrative answer.

If your model keeps inventing findings, check whether speaker labels are intact and whether your output instructions allow insufficient evidence. This small exercise measures prototype behavior on specific cases. A pilot with approved inputs is needed to learn how it works for your users.
