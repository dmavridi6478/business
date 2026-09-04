Use the AskUserQuestion tool to ask targeted clarifying questions about the task described in $ARGUMENTS before producing any output.

Ask only questions that would meaningfully change what you produce — not generic questions, but specific gaps in your understanding. If the task is already clear enough, proceed without asking.

Once the user answers, execute the task incorporating their responses.

If $ARGUMENTS is empty, ask what they want to accomplish first, then ask any follow-up clarifying questions before proceeding.

This is the "clarify first" pattern: gathering the right information before outputting anything, rather than starting and revising.
