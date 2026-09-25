---
description: 5 prompts to run at each stage of an AI coding session — spec, debug, split, test, review (@build.dev "5 prompts I never ask my AI to code without")
argument-hint: [spec | debug | split | test | review] [file, trace, or context]
---

You are running the 5-prompt coding checklist from @build.dev: "I never ask my AI to code without these 5 prompts." Each one targets a specific failure mode of AI coding sessions (guessed schemas, wasted context on raw traces/dumps, files that grow past what an agent can hold, missing edge-case tests, and self-approved diffs).

If no argument is given, display all five and ask which stage the user is at.

---

## PROMPTS

### /spec — Spec Before You Build
Use when a feature starts as a one-liner — even a strong model won't guess your schema.

```
Turn this one-liner into a spec. List data model, edge cases, and what's
out of scope. No code yet.
```

---

### /debug — Debug the Exact Trace
Use as soon as a stack trace appears — dumping the whole repo wastes context that could go to the actual fix.

```
Here is the stack trace and the line I changed. Explain the root cause and
exact fix.
```

---

### /split — Split the Bloated File
Use before a file becomes a dump — effective recall only reaches about 60-70% of a model's advertised context window.

```
This file grew too large. Propose a module split. Map every exported
function to its new home before editing.
```

---

### /test — Write Tests Right Away
Use right after a behavior change, while the change is still fresh.

```
Write unit tests for the function I changed. Mirror my test style. Cover
empty input and the error path.
```

---

### /review — Review Your Own Diff
Run pre-merge, when you're too deep in your own change to see it clearly — a missed bug here triggers retry turns that multiply context cost.

```
Review this diff as a skeptical reviewer. List bugs, races, and SQL issues
by file and line. No praise.
```
