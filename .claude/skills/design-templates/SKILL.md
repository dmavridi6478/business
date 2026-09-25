---
name: design-templates
description: Ready-to-use, self-contained HTML/CSS templates for common content-visual needs — an iMessage chat mockup, a vertical social/story device frame, a 3D-tilted product screenshot mockup, a halftone/dithered image effect (both CSS-only and real canvas dithering), a logo/reference moodboard grid, a brand board (wordmark + palette + type pairing + app preview), a SaaS pricing table + comparison grid, a restrained editorial hero, and a filterable design-reference-site dashboard. Use these instead of reaching for a paid single-purpose tool (or hand-rolling from scratch) when a design/frontend task needs a device mockup, a stylized image effect, a moodboard layout, a brand-kit deliverable, a SaaS pricing section, a quiet typography-led hero, or a reusable reference dashboard. Each template is copy-paste-ready with clear swap points marked in comments.
---

## When to use this skill

Reach for a template here instead of improvising when a task needs:

- **A chat-app screenshot mockup** (testimonials, feature announcements, social proof) → `templates/imessage-mockup.html`
- **A vertical social/story device frame** (TikTok/Reels/Stories content previews) → `templates/device-frame-social.html`
- **A 3D-angled product/app screenshot** for marketing (hero images, feature cards) → `templates/product-3d-tilt.html`
- **A halftone or dithered image treatment** (retro/print-poster look, or an actual 1-bit dithered image) → `templates/halftone-dither.html`
- **A moodboard/reference grid** (competitor logos, brand color references, visual inspiration boards) → `templates/logo-moodboard-grid.html`
- **A brand board** (wordmark, palette, type pairing, app-preview mockup for a new brand direction) → `templates/brand-board.html`
- **A SaaS pricing table or feature-comparison grid** → `templates/saas-pricing-table.html`
- **A restrained, typography-led hero or section divider** (when "loud" is the wrong register) → `templates/editorial-hero.html`
- **A numbered "Top N tools / workflows" social carousel slide** (two items per 4:5 slide, gradient headline, workflow node card) → `templates/numbered-workflow-carousel.html`
- **A dark carousel cover** (label block, big headline, two tilted 3D app tiles) → `templates/carousel-cover-dark.html`
- **A layered framework / operating-model infographic** (side columns + colour-coded layer bands + bottom flow strip) → `templates/layered-framework-infographic.html`
- **A layered stack / N-layer architecture pyramid** (tinted 3D slabs, tool chips) → `templates/stacked-layer-pyramid.html`
- **An inside-out maturity model as concentric rings** (data-driven label placement) → `templates/concentric-rings-framework.html`
- **An old-way vs new-way comparison** (grey vs pink/lilac columns, numbered cards) → `templates/two-column-shift-comparison.html`
- **A process of N steps under one control/orchestrator node** → `templates/control-plane-pipeline.html`
- **A dense 50-100 item icon-tile catalog grid** → `templates/workflow-grid-catalog.html`
- **A bookmarkable, filterable reference dashboard** of curated design-inspiration sites → `templates/design-reference-shelf.html` (also published as an Artifact — see `design-dev-resources` for the live link and site notes)

## How to use a template

1. Open the relevant file in `templates/` and read its top comment — each documents what it's inspired by and exactly what to swap (background image, text, colors).
2. Copy the whole file (or the relevant `<style>`/markup block) into the actual deliverable — these are starting points, not a library to link against.
3. Replace placeholder content (gradients, lorem-ish captions) with the real screenshot, logo, or copy before delivering.
4. Adjust the CSS custom properties at the top of each `<style>` block (e.g. `--accent`, `--tilt-x`/`--tilt-y`) rather than hunting through the rules for hardcoded values.

All are verified to render correctly with no console errors (checked via Playwright screenshot before being added to this repo).

## Templates

| File | Inspired by | Technique |
|---|---|---|
| `imessage-mockup.html` | Javii (javii.tools) | Pure CSS chat bubbles + phone frame, no images/fonts required |
| `device-frame-social.html` | Javii (javii.tools) | CSS phone frame + notch, overlay caption/action-bar pattern for Story-style content |
| `product-3d-tilt.html` | Ultramock (ultramock.io) | CSS 3D `perspective`/`rotateX`/`rotateY` with a floor shadow; includes optional live mouse-tilt JS for previewing angles |
| `halftone-dither.html` | Ditther (ditther.com) | Two techniques: a CSS-only `radial-gradient` dot overlay (fast, approximate), and real 4×4 Bayer ordered dithering on `<canvas>` (actual 1-bit pixel output) |
| `logo-moodboard-grid.html` | Logo System (logosystem.co) | CSS Grid with mixed tile spans (`tile--wide`/`tile--tall`) for a curated-board look instead of a uniform grid |
| `brand-board.html` | The `brandkit-generator` skill's output shape | CSS Grid board combining a wordmark card, named-role color swatches, a type-pairing sample, and a mock application preview into one shareable board |
| `saas-pricing-table.html` | Land-book (land-book.com) | 3-tier pricing table + feature-comparison table in one file, the two patterns Land-book names as what people actually go there to unstick themselves on |
| `editorial-hero.html` | SiteInspire (siteinspire.com) / Httpster (httpster.net) | Oversized serif headline with one italic accent word, thin gradient rule under a category label, dotted-radial-gradient canvas — the "clean, restrained, European" register both sites curate for |
| `numbered-workflow-carousel.html` | "Best 8 AI Automation Tools" carousel (@theromanknox) | 1080×1350 slide, brown→peach `background-clip:text` headline, numbered badge, ✱ bullet, light/dark workflow node cards; theme `warm-creator-carousel` |
| `carousel-cover-dark.html` | Same carousel, cover slide | Radial espresso glow + masked grid + ring, peach label block, rotated 3D tiles with inset shadows, SVG curved swipe arrow |
| `layered-framework-infographic.html` | "The Governed Marketing Team" (prosp / Claude) | 3-column grid (who-talks-to-what · layer stack · what-it-prevents) with per-layer `--c`/`--t` colour tokens, 5-step flow strip; pre-filled with `governed-marketing-team`; Aptos 32/14/11 pt; responsive + dark mode; theme `governed-infographic` |
| `stacked-layer-pyramid.html` | "The 5-layer GTM engine" (Cold IQ) | Slabs with per-slab `--w` width and `--top` lid colour drawn by a clipped `::before` trapezoid; pre-filled with `gtm-outbound-engine`; theme `peach-stack` |
| `concentric-rings-framework.html` | "5 Layers of Operational Excellence" (Eric Partaker) | Nested CSS circles + JS that spreads each ring's label pills evenly around the band and staggers alternate rings; edit the `RINGS` array, not coordinates; pre-filled with `operational-excellence-layers`; theme `concentric-rainbow`. Keep ≤ 12 labels per ring or pills start to touch |
| `two-column-shift-comparison.html` | "Very few measure adaptability" (Andrea Rubik) | 5/7 grid, alternating pink/violet `nth-child` badges and icon tiles; pre-filled with `marketing-adaptability-score`; theme `adaptive-pink` |
| `control-plane-pipeline.html` | "The All-in-One Outbound Pipeline — inside Claude Code" | Dark control node + bracket connector + N pastel step columns with per-step `--bg-s`/`--c` tokens, collapses to one column on mobile |
| `workflow-grid-catalog.html` | "The Complete Claude + n8n Sales System — 100 workflows" | Data-driven grid built from one `ITEMS` array (n, label, icon) so item count is an array edit, not hand-placed divs; pre-filled with all 100 from `sales-workflow-catalog`; theme `workflow-grid-sunset`; tile labels run below 11pt by necessity at this density |
| `design-reference-shelf.html` | The 5-site design-inspiration list itself | Card-catalog-style dashboard (Fraunces display + IBM Plex Mono utility faces, light/dark tokens, small JS tag filter) indexing Awwwards/Godly/SiteInspire/Land-book/Httpster by what each is for; built and verified as a Claude Artifact, not a plain copy-paste snippet like the rest of this table |

## Related skills in this repo

- **design-dev-resources**: The source tools these templates approximate — reach for the real tool instead of the template when its specific feature (e.g. Ultramock's motion-blur export, Ditther's ASCII mode) is actually needed, not just the static look.
- **frontend-design**, **web-artifacts-builder**, **canvas-design**: Use these templates as building blocks within a larger page/artifact/poster built with those skills.
- **campaign-page-one-shot**, **content-strategy**: The device-frame and moodboard templates are useful for landing-page social proof sections and content-planning references, respectively.
- **content-repurposing-service**: The social device frame is a natural fit for previewing the carousel/short-video assets that playbook produces.
- **brandkit-generator**: Assembles its brand-direction output into `brand-board.html`.
- **ui-motion-design**: Add restrained entrance/hover motion to any of these templates instead of leaving them fully static, when the deliverable is interactive.

## Notes

Source: a "6 design tools that never make the lists" screenshot carousel (@webnailed) for the first five templates; `brand-board.html` was built for the `brandkit-generator` skill, sourced from a "Claude Replaces Designers" video (@vibes.codes). These templates are original CSS/HTML written to approximate each tool's visual output — not copies of the tools' code, which isn't open source.

`saas-pricing-table.html`, `editorial-hero.html`, and `design-reference-shelf.html` were added after reviewing an uploaded photo batch — a "5 sites we actually check before designing" carousel (@goluda.ai) listing Awwwards, Godly, SiteInspire, Land-book, and Httpster. This session's network egress is blocked to all five of those domains (a general restriction, not specific to this list), so they weren't live-browsed; the two content templates and the dashboard's site notes are built from each site's own well-established, independently verifiable curation focus (and match what the carousel itself said), not from a live visit. Say so if asked whether these were actually browsed.
