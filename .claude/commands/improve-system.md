---
description: Review this session for durable behavioral signals/preferences worth remembering, and persist them as memory files for future sessions.
---

Review the current session for one genuine, durable signal worth saving — a stated preference, a correction the user made, or a pattern that repeated more than once. This is not a transcript summary: most sessions contain zero or one thing actually worth persisting, not a dozen.

## What counts as a signal

- A behavioral/style preference the user expressed or implied through correction (e.g. "shorter," "don't ask before X," "always do Y this way").
- A refinement of an *existing* stored preference (e.g. they already said "be concise" and this session showed concise-but-structurally-complete is what they actually meant) — update the existing memory rather than creating a near-duplicate.
- Do **not** save: one-off task details, project-specific facts that won't matter next session, or anything that's really just normal task execution rather than a lasting preference.

## Where it goes

- **Auto-memory** (`memory/*.md`): cross-session behavioral preferences and corrections — the kind of thing that should silently shape how future sessions behave.
- **Experience entries** (`knowledge/me/experiences/`, if that convention exists in this project): a story worth remembering in the user's own voice, not a behavioral rule. Don't file a behavioral preference here just because it happened during an interesting session.

If it's ambiguous which bucket a signal belongs in, say so and ask, rather than filing a silent judgment call.

## How to write it

1. Give the memory file a clear, descriptive filename (e.g. `memory/feedback_long_means_thorough_not_verbose.md`), not a generic `notes.md`.
2. Keep the entry short and specific — the signal and the concrete evidence for it, not a paraphrase of the whole conversation.
3. Update the memory index (`memory/MEMORY.md` or equivalent) so the new file is actually discoverable next session — an orphaned memory file that isn't indexed might as well not exist.
4. If an existing memory file covers the same ground, edit it in place instead of creating a near-duplicate.

## Before finishing

- Report what was written (or that nothing met the bar this session — that's a valid outcome).
- Flag anything you noticed but didn't file — e.g. a memory file that exists on disk but is missing from the index, or a judgment call about which bucket something belongs in — so the user can confirm or correct it.
