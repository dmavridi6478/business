---
description: Run the design-review-audit checklist against a specified build (file, artifact, or URL) and report a prioritized punch list.
argument-hint: [file or description of what to review]
---

Run a design review on: $ARGUMENTS

Follow the `design-review-audit` skill's checklist in full — spacing/rhythm, typographic hierarchy, color/contrast, consistency, generic AI-slop tells (cross-referencing `frontend-design`'s aesthetic guidance for that category), and responsiveness/edge cases.

If the target is a live file, read it directly. If it's a rendered page/artifact and a screenshot would materially help spot spacing/alignment/contrast issues, take one (e.g. via the Playwright CLI: `playwright screenshot <url> <output>.png`) before reviewing rather than reviewing markup alone.

Report findings as a prioritized punch list: **blocking**, **should-fix**, **polish** — each naming the specific element and the concrete fix, not general praise or vague direction.

If nothing in the target is reachable (no file path given, no context on what to review), ask rather than guessing what "the current build" refers to.
