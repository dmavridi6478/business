---
name: image-to-code
description: Convert a reference UI screenshot or mockup into matching frontend code (HTML/CSS or React/Tailwind), then render the built version and compare it against the reference — iterating on mismatches instead of stopping at a one-shot guess. Use when given a screenshot/mockup/design export and asked to build it, clone a UI, or match a design closely.
---

## Workflow

1. **Inspect the reference carefully before writing code.** Note the layout structure (grid/flex regions), spacing, type hierarchy, color usage, and component boundaries. Don't start coding from a half-glance.
2. **Extract tokens first** (via `design-token-extractor`) rather than eyeballing hex values and font sizes directly into the markup — the resulting code should reference named tokens, not scattered magic numbers.
3. **Build with real, semantic structure** — proper heading levels, landmark elements, actual CSS (grid/flexbox) rather than absolute-positioning everything to force a pixel match.
4. **Render and compare.** Take a screenshot of the built version at the same viewport size as the reference (e.g. via `playwright screenshot <file> <output>.png --viewport-size=W,H`) and compare it side-by-side against the original — don't just trust that the markup "should" look right.
5. **Iterate on concrete mismatches**: spacing that's off, wrong font-weight, misaligned elements, wrong color — fix and re-screenshot until the comparison holds up, not just "close enough" on first pass.
6. **Flag what can't be determined from the image alone**: exact font family (screenshots rarely allow certain identification — name the closest reasonable match and say so), real copy vs. placeholder text, interaction/hover states not visible in a static image.

## Related skills in this repo

- **design-token-extractor**: Run first to ground colors/type/spacing in named tokens instead of guessed values.
- **frontend-design**: General aesthetic/code-quality guidance that still applies even when the goal is matching a specific reference rather than inventing a design.
- **design-review-audit** / `/design-review`: Run after the comparison pass to catch anything the side-by-side check missed (contrast, responsiveness).
- **web-artifacts-builder**: Use for complex multi-component references (React/Tailwind/shadcn) rather than a single static page.

## Notes

Source: a "Claude Replaces Designers" screenshot-carousel video (@vibes.codes) describing an "Image To Code" skill. The render-and-compare step (not just single-shot generation) is what makes this different from generic code generation — verified the same way the `design-templates` skill's HTML files were checked before being added to this repo (Playwright screenshot, visual comparison).
