---
name: claude-remotion-no-ai-slop-rules
description: The dabsterlabs.cy rules for making Claude and Remotion videos without AI slop (ban list for glow, glass cards, mud gradients, fake dashboards and cards from nowhere, real terminal output, highlighted proof from the article, real logos and UI checked first then scored 8 of 10 or redone) from a Greek TikTok carousel video, with Greek terms kept and a reusable checklist. Use before generating motion graphics with Remotion.
---

# Claude + Remotion without AI slop (dabsterlabs.cy video)

Source: a Greek-language 21-second slideshow with nine slides. Greek wording is kept in brackets. The comment-to-get-the-setup call ("Γράψτε MOVE") was **not** answered; no comment was made.

## The rules shown
| Slide | Rule (Greek original) | Meaning |
|---|---|---|
| 04 | **Τι απαγορεύεται ρητά** | Explicitly banned: "Glow και νέον" (glow and neon), "Γυάλινες κάρτες" (glass cards), "Μωβ και γαλάζια gradients" (purple and blue gradients), "Ψεύτικα dashboards και νούμερα" (fake dashboards and numbers), "Κάρτες που πετάγονται στο κενό" (cards that pop out of nowhere) |
| 06 | **Τερματικά που μοιάζουν αληθινά** | Terminals that look real: real keystrokes, real output ("Αληθινό πληκτρολόγημα, αληθινή έξοδος") |
| 07 | **Η απόδειξη από άρθρο, υπογραμμισμένη** | Proof from an article, highlighted: find the line, then pass a marker over the right line only |
| 08 | **Ελέγχει τα στοιχεία, μετά βαθμολογείται** | Checks the facts first, then is scored: real logos and real UI first; below 8 out of 10 it is redone ("Η από την αρχή") |
| 09 | **Θέλετε όλο το setup;** | A sales hook: comment "MOVE" to receive the repo and the install command |

## Checklist to reuse (my wording)
1. No decorative glow, glass or gradient defaults; one flat palette.
2. Never show invented dashboards or numbers; use a real screenshot or a real data file.
3. Terminals show a real recorded session, not typed fiction.
4. When citing an article, highlight the exact line and show the source.
5. Verify every logo, UI and figure before rendering; score the render out of 10 against a written rubric and redo below 8.

## Notes
- **[Certain]** The slides give no repo or install command; the "setup" is behind a comment gate, so it could not be inspected. Do not paste an install command from a stranger's reply without reading it.
- Use with `remotion-video-creation`, `claude-anti-slop-stack` and `avoid-ai-writing`.
