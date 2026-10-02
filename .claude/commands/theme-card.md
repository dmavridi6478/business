---
description: Produce a social card from one of the Batch 98 design themes (noir red-sphere wordmark, glow-numeral font specimen, GitHubNow repo briefing, light tool spotlight) by filling the matching template.
argument-hint: <noir|glow|briefing|spotlight> "<content or topic>"
---

Theme: $1 · Content: $2

Template map (all in `.claude/skills/design-templates/templates/`):
- `noir` → `wordmark-noir-card.html` (black field, red gradient spheres, silver wordmark, numbered index bar)
- `glow` → `font-showcase-glow.html` (giant glowing numeral, specimen name, "Save it for later / Swipe")
- `briefing` → `repo-briefing-card.html` (9:16: cover / repo / CTA; tag pill, stars pill, 4-step flow, 3 feature cards)
- `spotlight` → `tool-spotlight-light.html` (white 4:5: tile, giant title, REPLACES / DOWNLOAD / GITHUB rows, browser frame)

Steps:
1. Copy the template to a new file under `Artifacts/templates/` named `social-card-<theme>-<slug>.html`; do not edit the original.
2. Edit only the data arrays at the bottom (and `:root` tokens if I asked for a re-tint).
3. **Fact rule:** any repo name, star count, date or "replaces X" claim must come from a source I gave you or from a live check — otherwise leave it marked `[verify]`. Never fill in plausible numbers.
4. If the card shows a font specimen, say whether the family is a real Google Font; the Batch 98 specimens Rigter, Malison, Keratus, Sparling, Badoga, Nura, Ancola, Alro, Surgena and Qurova/Ourova are **not** on Google Fonts — use the listed look-alike or ask me for the licensed file.
5. Render with headless Chromium at `--s: 1`, look at the screenshot, and fix overflow before showing me.
