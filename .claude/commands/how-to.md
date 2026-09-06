Turn "$ARGUMENTS" into a full, actionable step-by-step plan — not just a
direct answer to the literal question asked.

1. If the task, its scope, or the starting point is unclear, ask up to 4
   clarifying questions with `AskUserQuestion` before planning (the actual
   goal, any constraints, current progress/starting point, desired depth) —
   don't guess at intent for a vague "how do I X" request. Skip this step
   only when the request is already fully specified.
2. Produce a numbered plan that takes the user from wherever they are now
   to done. Each step should be concrete enough to act on immediately —
   name the specific action, not just the topic — and note any
   prerequisite or dependency a step relies on.
3. If "$ARGUMENTS" contains "ELI5" anywhere, explain each step in plain
   language a complete beginner would understand: no unexplained jargon,
   and attach a one-line definition the first time a technical term
   appears.
4. Match depth to the task's real complexity. Don't pad a simple task with
   unnecessary steps to look thorough, and don't compress a genuinely
   multi-step task into a couple of vague bullets.
5. End with what "done" looks like — a concrete way for the user to verify
   the task actually succeeded, so they don't have to come back and ask.
