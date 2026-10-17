---
description: Apply one of five writing checks (compress, translate, strengthen, voice, objections) to a draft, following the claude-writing-5-use-cases skill
argument-hint: "[compress|translate|strengthen|voice|objections] [text or file path]"
---

Use the skill `claude-writing-5-use-cases`.

Arguments: $ARGUMENTS

The first word is the mode: compress, translate, strengthen, voice or objections. The rest is pasted text or a file path (read the file if it is a path). If the mode or the text is missing, ask for it.
- compress: one-page decision memo, no new facts.
- translate: executive, technical and general versions with identical facts.
- strengthen: list premises, name the weakest, say what evidence would support it, give a stronger version.
- voice: ask for the voice guide if none was given, then quote each drift and fix it.
- objections: what a skeptic doubts, what evidence they want, what alternative they suggest, how to answer upfront.
Return the result and one line saying what you could not verify. Do not invent facts, quotes or numbers.
