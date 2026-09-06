# Procedure: Loop Engineering (Inspect → Build → Verify → Red Team → Improve)

## When this applies

Any task handed to an AI assistant — Claude, Codex, Cursor, Grok, or
otherwise — where a single prompt-and-accept pass isn't reliable enough:
drafting a deliverable against a brief, generating code against a spec,
producing analysis that has to hold up to scrutiny. Tool-agnostic by design;
nothing below depends on a specific product.

The shift this procedure encodes: stop treating a prompt as a one-shot
question with one accepted answer. Treat it as a loop that checks its own
output and rewrites until the output clears a bar, then feeds what it
learned back into the next run.

## The portable prompt template

Paste this as a system/instruction block ahead of the actual task, in any
tool. It doesn't require plugins, code execution, or a particular vendor.

```
You are running a 5-stage loop on this task. Do not skip stages or merge
them into one pass — complete each stage's checklist before moving to the
next, and show your work at each stage rather than jumping straight to a
final answer.

STAGE 1 — INSPECT (before generating anything)
Read the brief/files/goal and state explicitly:
- Goal: what does "done" mean here?
- Constraints: what am I not allowed to change or assume?
- Files/inputs: what source material actually exists?
- Tone/format: what does the output need to look like?
- Success criteria: how will this be judged?
If any of these is missing or ambiguous, say so before proceeding — bad
context produces bad output regardless of how good the next stages are.

STAGE 2 — BUILD
Generate the first full output from the Stage 1 context. This is a draft,
not a final answer.

STAGE 3 — VERIFY
Check the Stage 2 output against the brief:
- Did it follow the brief?
- Is the logic/reasoning solid?
- Is the format correct?

STAGE 4 — RED TEAM
Attack your own output before a critic does:
- What is weak?
- What could fail?
- What would a critic attack first?

STAGE 5 — SCORE, REWRITE, REPEAT
- Score the output against the Stage 1 success criteria (e.g. 1-10, or
  pass/fail per criterion).
- If it doesn't clear the bar: rewrite, folding in the Stage 3/4 findings.
- Repeat Stages 3-5 until it clears the bar or you've made 3 passes without
  material improvement — if the latter, stop and say explicitly what's
  still unresolved rather than declaring success.

Report, at the end: the final output, the score, and what Stage 4 flagged
that you did or didn't fix and why.
```

## Steps to run it manually

1. **Inspect first, every time.** Resist the urge to jump straight to
   generating output. Write down goal/constraints/files/format/success
   criteria even for a task that feels obvious — this is the step most
   commonly skipped and the one most likely to silently produce a wrong
   answer.
2. **Build one full draft**, not a partial answer to negotiate over.
3. **Verify and red-team as two separate passes**, not one. Verify checks
   compliance with the brief; red-teaming looks for what an adversarial
   reader would attack. Merging them tends to produce a shallow pass that
   only catches the easy problems.
4. **Score against the Stage 1 criteria specifically** — not a vague sense
   of quality. If Stage 1 didn't produce concrete success criteria, that's
   a sign to go back and fix Stage 1 rather than inventing a score now.
5. **Cap the rewrite loop.** An unbounded "keep trying" loop burns time
   without guaranteeing convergence. Three passes without material
   improvement is the signal to stop and surface what's unresolved, not to
   keep iterating silently.
6. **Improve the system, not just this output.** After the loop closes,
   log what broke, and fold the fix into whatever governs the next run —
   a house-style doc, a checklist, a skill file, a saved prompt. The point
   of this last step is that the same failure shouldn't have to be
   red-teamed again next time.

## Where this already exists as a tool, not just a template

In this Claude Code environment specifically, the `task-loop-runner` agent
already implements Stages 2-5 (act → evaluate → retry) for a single
well-defined task with a checkable success condition — reach for it instead
of hand-running the loop when the task fits that shape. Stage 1 (Inspect)
and Stage 6 (fold the fix back into a durable instruction/skill) are still
worth doing explicitly around it, since those are what keep the fix from
being a one-off.

## Source

Synthesized from a 9-slide "How I Build AI Loops That Improve Themselves"
carousel (@finitopotatoes), which named Claude Code, Codex, Cursor Auto,
and Grok Build as interchangeable engines for the same loop — the loop
itself, not any one tool, is the reusable part.
