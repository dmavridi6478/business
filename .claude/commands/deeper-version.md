---
description: Rewrite a task as a deeper (not bigger) prompt using the four-step "top professional" check, then wait for approval before running it
argument-hint: "[the task or prompt to deepen]"
---

Use the skill `claude-deeper-version-prompt`.

Task: $ARGUMENTS

If no task was given, ask for one. Then:
1. Answer the four questions from the skill (what a top professional would do that I am not asking for; the rawest material they would start from; the specific methods and tools; what other than you or me would show the result is right).
2. Rewrite my prompt to ask for exactly that.
3. Show the rewritten prompt in a code block and stop. Do not run it until I approve, and mark any step that depends on a source or tool you cannot verify.
