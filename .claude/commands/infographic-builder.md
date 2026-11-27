---
description: Turn text into a shareable 1080 x 1350 infographic as a self-contained HTML file with the key numbers sourced
argument-hint: [the text or data, audience, brand colours]
---

Input: $ARGUMENTS

Use `infographic-prompts` and the 1080x1350 templates in `design-templates`.

1. Extract the one message, three to six supporting points and any figures. Every figure needs its source from my text; drop any that has none.
2. Pick the closest template layout, say why, and write one HTML file at 1080x1350 with text on real elements (no text baked into images), readable at phone size.
3. Check for overflow by rendering if a browser is available; otherwise say it is unchecked.
4. Return the file path and a plain-text alt description.
