---
name: design-templates
description: Ready-to-use, self-contained HTML/CSS templates for common content-visual needs — an iMessage chat mockup, a vertical social/story device frame, a 3D-tilted product screenshot mockup, a halftone/dithered image effect (both CSS-only and real canvas dithering), a logo/reference moodboard grid, a brand board (wordmark + palette + type pairing + app preview), a SaaS pricing table + comparison grid, a restrained editorial hero, a numbered infographic card grid (light/dark variants), a filterable design-reference-site dashboard, a light "Save For Later" social carousel (carousel-save-for-later), a dark neon agent info card (dark-neon-agent-card), a dark orange-gradient tutorial step-cards layout (dark-orange-agent-tutorial), a GitHub-style dark trending repo card (github-trending-card), a bold red grunge AI-tools carousel (@ai.global.lee style, red-grunge-ai-tools), a warm editorial carousel for thinking-partner / Claude workflow content (@parm.ai style, editorial-thinking-partner), a dark space-themed OSS repo card (@datawarlord_official style, datawarlord-oss-card), and a nature photo background with glassmorphism panels carousel (@softgirlnocode AI video style, softgirlnocode-nature-glassmorphism), a light/dark copy-this-prompt carousel (prompt-card-carousel), a repo-showcase card set (repo-card-grid), an agent explainer flow card (agent-flow-chat-card), and an orange mascot tips carousel (mascot-tips-orange), plus three Batch 104 templates: a near-black navy-grid repo spotlight with a browser mockup (repo-spotlight-browser-card), a full-bleed photo-under-scrim tool card (photo-overlay-tool-card) and a six-step highlightable code card (code-card-six-lines), plus five Batch 105 templates: a teal-and-gold skill spotlight (skill-spotlight-teal-gold), a grid-paper repo and command card (grid-paper-repo-command-card), a glossy AI-team role card (ai-team-role-card), a lavender "try this instead" tool card (swap-tool-lavender-card) and a two-approach comparison infographic (compare-two-approaches-cream), plus five Batch 106 templates: a charcoal-and-terracotta explainer table and list (mod-explainer-dark-terracotta), a cream repo-feature card with rank number and stats (repo-feature-cream-number), a beige prompt card with a dark copy box (prompt-card-beige-green), caption strips on a blue grid or photo (caption-highlight-blue-grid) and a pale-blue dashboard showcase (dashboard-showcase-light-blue). Use these instead of reaching for a paid single-purpose tool (or hand-rolling from scratch) when a design/frontend task needs a device mockup, a stylized image effect, a moodboard layout, a brand-kit deliverable, a SaaS pricing section, a quiet typography-led hero, a "N things you should know" carousel/infographic layout, a reusable reference dashboard, or any of the social-carousel/card layouts above. Batch 107 adds a red-cream numbered prompt-step carousel (prompt-step-red-cream), a night GitHub leaderboard (trending-top10-leaderboard) and a dark amber code-pane explainer (quant-code-pane-dark). Batch 108 adds a photo-scrim step carousel with tool rows (photo-step-tools-caption) and a periwinkle three-stage GTM chart (gtm-stage-three-column). Batch 109 adds a photo-scrim GitHub swap card (swap-card-photo-github). Batch 110 adds a grey-teal avoid / reason / say grid (avoid-reason-say-grid). Batch 111 adds eight templates: a paid-versus-free comparison card (paid-vs-free-signal-card), a 16-tile cream drawing sheet (blueprint-sheet-16), a four-quadrant disc with side lists (quadrant-puzzle-center), a dark 10-department org chart (org-chart-neon-dark), a report-versus-check pairs spine (metric-pairs-spine), a radial evidence-tier wheel drawn by script (evidence-wheel-radial), a 3 x 3 olive prompt grid (prompt-grid-9-olive) and a gold board dashboard with 14 panels (board-dashboard-gold). Each template is copy-paste-ready with clear swap points marked in comments.
---

## When to use this skill

Reach for a template here instead of improvising when a task needs:

- **A light social carousel** in "Save For Later" style (paper texture, coral accent, numbered slides) → `templates/carousel-save-for-later.html`
- **A dark neon agent/tool card** (cyan/purple glow, code block, step list, dark bg) → `templates/dark-neon-agent-card.html`
- **A dark orange-gradient tutorial layout** (numbered step cards, agent loop diagram, charcoal bg) → `templates/dark-orange-agent-tutorial.html`
- **A GitHub-style dark trending repo card** (green accent, star/fork stats, topic pills, monospace counts) → `templates/github-trending-card.html`
- **A chat-app screenshot mockup** (testimonials, feature announcements, social proof) → `templates/imessage-mockup.html`
- **A vertical social/story device frame** (TikTok/Reels/Stories content previews) → `templates/device-frame-social.html`
- **A 3D-angled product/app screenshot** for marketing (hero images, feature cards) → `templates/product-3d-tilt.html`
- **A halftone or dithered image treatment** (retro/print-poster look, or an actual 1-bit dithered image) → `templates/halftone-dither.html`
- **A moodboard/reference grid** (competitor logos, brand color references, visual inspiration boards) → `templates/logo-moodboard-grid.html`
- **A brand board** (wordmark, palette, type pairing, app-preview mockup for a new brand direction) → `templates/brand-board.html`
- **A SaaS pricing table or feature-comparison grid** → `templates/saas-pricing-table.html`
- **A restrained, typography-led hero or section divider** (when "loud" is the wrong register) → `templates/editorial-hero.html`
- **A "N things you should know" numbered card grid** (skill lists, tool roundups, GitHub-repo carousels — the layout behind most infographic-style social carousels) → `templates/infographic-card-grid.html`
- **A numbered "Top N tools / workflows" social carousel slide** (two items per 4:5 slide, gradient headline, workflow node card) → `templates/numbered-workflow-carousel.html`
- **A dark carousel cover** (label block, big headline, two tilted 3D app tiles) → `templates/carousel-cover-dark.html`
- **A layered framework / operating-model infographic** (side columns + colour-coded layer bands + bottom flow strip) → `templates/layered-framework-infographic.html`
- **A layered stack / N-layer architecture pyramid** (tinted 3D slabs, tool chips) → `templates/stacked-layer-pyramid.html`
- **An inside-out maturity model as concentric rings** (data-driven label placement) → `templates/concentric-rings-framework.html`
- **An old-way vs new-way comparison** (grey vs pink/lilac columns, numbered cards) → `templates/two-column-shift-comparison.html`
- **A process of N steps under one control/orchestrator node** → `templates/control-plane-pipeline.html`
- **A dense 50-100 item icon-tile catalog grid** → `templates/workflow-grid-catalog.html`
- **A bookmarkable, filterable reference dashboard** of curated design-inspiration sites → `templates/design-reference-shelf.html` (also published as an Artifact — see `design-dev-resources` for the live link and site notes)
- **A bold red grunge AI-tools carousel** (@ai.global.lee style — red `#FF0000` bg, grunge texture, Impact-style white headline, yellow highlighted keywords, monospace body, B&W closing slide) → `templates/red-grunge-ai-tools.html`
- **A warm editorial thinking-partner carousel** (@parm.ai style — beige `#F5F0E8` bg, Playfair Display italic in burnt orange, dark monospace prompt code blocks, clean numbered step layout) → `templates/editorial-thinking-partner.html`
- **A dark space-themed OSS repo card** (@datawarlord_official "Open Source Builds a Brighter Tomorrow" style — `#080B14` bg, dot-grid texture, per-card neon gradient glow, floating 3D icon area, GitHub pill, category tags, DW footer bar) → `templates/datawarlord-oss-card.html`
- **A nature photo + glassmorphism panels carousel** (@softgirlnocode "How I edit Videos with AI" style — full-bleed outdoor photo bg, dark scrim overlay, large bold white headline, frosted-glass quote card, pill context labels, step-dot progress indicator) → `templates/softgirlnocode-nature-glassmorphism.html`
- **A GitHubNow-style 9:16 repo briefing set** (navy→black gradient, green tag pill + amber outline stars pill, mono `owner/name` title, 4-step flow strip with one highlighted step, 3 feature cards, org footer; cover / repo / CTA slides) → `templates/repo-briefing-card.html`
- **A glowing-numeral font specimen carousel** (@designarchitect001 "FONT 0N" style — giant dark numeral with coloured rim glow + grain, two rim-lit spheres, specimen name, "Save it for later / Swipe →"; one colour per slide) → `templates/font-showcase-glow.html`
- **A black-and-red "fonts that look like a logo" wordmark carousel** (red gradient spheres, silver-gradient wordmark, `01 | NAME` index bar, cover and "Was this helpful?" end card) → `templates/wordmark-noir-card.html`
- **A white tool-spotlight carousel** (@will.ai.m "free tools Big Tech doesn't want you to run" style — icon tile, giant title, REPLACES / DOWNLOAD / GITHUB rows, browser-frame screenshot, intro + follow slides) → `templates/tool-spotlight-light.html`
- **An engineering-lesson carousel card** (@jek.notes style — off-white paper, heavy condensed headline with one red line, red "The problem / What to do / Think" tags, arrow bullets, mini flow) → `templates/bug-lesson-card.html`
- **A checklist panel grid** (@aisimplified23 "Claude Checklist" style — peach panels with black header tabs and checkbox rows, bold keywords; data-driven `PANELS`) → `templates/checklist-panels-peach.html`
- **A KPI framework one-pager** (Oana Labes style — black title bar with a yellow keyword, cream lagging panel in 3 columns, three gold leading panels, checkbox KPIs with formulas) → `templates/kpi-framework-gold.html`
- **A UI do / don't tip card** (@iqonicdesign style — pale blue-white card, wireframe pair with red X and green check, "Save this for later" pill) → `templates/ui-tip-do-dont.html`
- **A SalesDaily-style 20-card methodology grid** (teal title bar, white cards with teal headers, grey "when to use it" box, "best for" line, teal footer; data-driven `CARDS` array) → `templates/sales-method-grid-teal.html`
- **A three-level stepped pastel card poster** (NipPro "3 Levels" style — serif headline with grey highlight, pink / peach / lilac cards of rising height, big percentage, looks-like list, next move, two stat tiles) → `templates/level-cards-pastel.html`
- **A pale-cyan prompt text card set** (@theaiguyhere style — avatar + handle header, numbered heading, one large bold prompt paragraph, corner watermark) → `templates/prompt-text-card-cyan.html`

- **A "copy this prompt" carousel** in two looks - light StackFlo (blue pill, light-blue quote box, `04 / 07` counter) or black ai_slacker (big white caps heading, plain prompt text) → `templates/prompt-card-carousel.html`
- **A repo-showcase carousel** (@joshualevi.ai grey grid paper, glossy orange 3D asterisk, `#N` rank, white GitHub-style stat card; dark @replace.so variant via `THEME`) → `templates/repo-card-grid.html`
- **An agent explainer card** (@ai.global.lee "5 AI agents" - numbered pill, accent-coloured headline word, chat mock-up, trigger → agent → 4 outputs → result flow panel) → `templates/agent-flow-chat-card.html`
- **An orange mascot tips carousel** (@aicareersuite "11 Ways to Master Claude" - peach number tile, black + orange headline with underline, check pills, inline-SVG robot mascot, takeaway box, `n/8` CTA bar) → `templates/mascot-tips-orange.html`

- **A teal-and-gold "fine print" skill carousel** (@ai.easily - radial teal gradient, giant gold numeral, gold-outlined THE FINE PRINT box, `AI EASILY - 03 / 07` footer) → `templates/fine-print-skill-card.html`
- **A 21-role poster** (51ultron "Hottest AI Role" - serif title with blue italic, 21 : 1 badges, grid of coloured role cards) → `templates/role-map-infographic.html`

- **A blue-violet gradient prompt card** (@ai.blueprint - orange corner glow, orange starburst, white/orange two-tone headline, prompt text, icon tile) → `templates/gradient-prompt-orange.html`
- **A lime-on-black explainer carousel** (@tinrovicai - section pill, `01 / 08` counter, white + lime headline, outlined highlight card, progress dots) → `templates/lime-explainer-dark.html`
- **A frosted-glass app-category card** (@jeanbbttyct - blurred photo background, big white title, glass panel of app tiles) → `templates/app-category-glass.html`
- **A textured-paper "tool of the day" card** (@clicksandranks - heavy grotesque title, teal link, browser screenshot, `SAVE FOR LATER`) → `templates/paper-tool-card.html`
- **A charcoal install card** (@the.wealth.lab - black logo band, yellow heading, `INSTALL` command) → `templates/dark-grey-install-card.html`

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
| `infographic-card-grid.html` | GenAI Works / ByteByteGo / AIForLeaders.com / replace.so carousel infographics (see `.claude/commands/claude-skills-13.md`, `top-12-agent-skill-repos.md`) | Numbered circular badge + icon chip + title + short description, repeated in a responsive 4→2→1 CSS Grid, with an eyebrow/headline header and a source-attribution footer; ships both the cream/serif "light" variant and a near-black "dark" variant (toggle via `<body class="light\|dark">`), verified via Playwright screenshot in both modes |
| `numbered-workflow-carousel.html` | "Best 8 AI Automation Tools" carousel (@theromanknox) | 1080×1350 slide, brown→peach `background-clip:text` headline, numbered badge, ✱ bullet, light/dark workflow node cards; theme `warm-creator-carousel` |
| `carousel-cover-dark.html` | Same carousel, cover slide | Radial espresso glow + masked grid + ring, peach label block, rotated 3D tiles with inset shadows, SVG curved swipe arrow |
| `layered-framework-infographic.html` | "The Governed Marketing Team" (prosp / Claude) | 3-column grid (who-talks-to-what · layer stack · what-it-prevents) with per-layer `--c`/`--t` colour tokens, 5-step flow strip; pre-filled with `governed-marketing-team`; Aptos 32/14/11 pt; responsive + dark mode; theme `governed-infographic` |
| `stacked-layer-pyramid.html` | "The 5-layer GTM engine" (Cold IQ) | Slabs with per-slab `--w` width and `--top` lid colour drawn by a clipped `::before` trapezoid; pre-filled with `gtm-outbound-engine`; theme `peach-stack` |
| `concentric-rings-framework.html` | "5 Layers of Operational Excellence" (Eric Partaker) | Nested CSS circles + JS that spreads each ring's label pills evenly around the band and staggers alternate rings; edit the `RINGS` array, not coordinates; pre-filled with `operational-excellence-layers`; theme `concentric-rainbow`. Keep ≤ 12 labels per ring or pills start to touch |
| `two-column-shift-comparison.html` | "Very few measure adaptability" (Andrea Rubik) | 5/7 grid, alternating pink/violet `nth-child` badges and icon tiles; pre-filled with `marketing-adaptability-score`; theme `adaptive-pink` |
| `control-plane-pipeline.html` | "The All-in-One Outbound Pipeline — inside Claude Code" | Dark control node + bracket connector + N pastel step columns with per-step `--bg-s`/`--c` tokens, collapses to one column on mobile |
| `workflow-grid-catalog.html` | "The Complete Claude + n8n Sales System — 100 workflows" | Data-driven grid built from one `ITEMS` array (n, label, icon) so item count is an array edit, not hand-placed divs; pre-filled with all 100 from `sales-workflow-catalog`; theme `workflow-grid-sunset`; tile labels run below 11pt by necessity at this density |
| `design-reference-shelf.html` | The 5-site design-inspiration list itself | Card-catalog-style dashboard (Fraunces display + IBM Plex Mono utility faces, light/dark tokens, small JS tag filter) indexing Awwwards/Godly/SiteInspire/Land-book/Httpster by what each is for; built and verified as a Claude Artifact, not a plain copy-paste snippet like the rest of this table |
| `carousel-save-for-later.html` | @clickandrank "Save For Later" social carousel | Light paper-texture bg, coral accent, slide counter badge, bookmark pill tag, progress dots — drop-in for any numbered carousel/listicle |
| `dark-neon-agent-card.html` | @aigenesis.official Hermes agent cards | Dark bg (#0A0A12), cyan/purple neon glow via absolute blurred circles, animated pulse dot, numbered steps, monospace code block — swap colours via CSS custom properties |
| `dark-orange-agent-tutorial.html` | @skilldropai 7-step Claude agent carousel | Dark charcoal (#0F0F0F), orange gradient header + step-num badges, left-bar hover accent, autonomous loop diagram — duplicate `.step-card` for each step |
| `github-trending-card.html` | @githubnow daily trending briefing | GitHub dark palette, green accent, monospace star/fork counts, language colour dots, topic pills, today-stars badge — duplicate `.repo-card` for each repo |
| `red-grunge-ai-tools.html` | @ai.global.lee "5 AI tools worth saving" carousel | Red `#FF0000` bg, SVG fractalNoise grunge overlay, Impact-family display headline, yellow `#FFE600` `.highlight` spans, monospace body, `.slide--bw` closing variant — duplicate `.slide` for each tool |
| `editorial-thinking-partner.html` | @parm.ai "Claude as thinking partner" carousel | Warm beige `#F5F0E8` bg, Playfair Display italic serif, burnt orange `#C4622D` accent, dark `#1E1E1E` `.prompt-block` with monospace syntax colouring, numbered `.step-row` layout, `.callout` blockquote — duplicate `.slide` for each step |
| `datawarlord-oss-card.html` | @datawarlord_official "Open Source Builds a Brighter Tomorrow" | Dark `#080B14` bg, dot-grid radial texture, per-card `--accent-start`/`--accent-end` gradient glow via `::after` pseudo, floating icon area, gradient tool-name text, GitHub pill with octicon SVG, category tag pills, DW footer bar — includes 9-card accent palette comment |
| `softgirlnocode-nature-glassmorphism.html` | @softgirlnocode "How I edit Videos with AI" carousel | Full-bleed outdoor photo bg via `background-image`, dark scrim via `linear-gradient` overlay, large `font-weight: 900` uppercase headline, `.glass-card` with `backdrop-filter: blur(20px)`, `.pill-row` context labels, `.step-dots` progress indicator — includes cover slide + 4 technique slides |

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

`infographic-card-grid.html` (Batch 82) was extracted from a recurring visual
pattern noticed across an uploaded photo batch — nearly every "N things you
should know" carousel/infographic in that batch (GenAI Works' 13 Claude
Skills, ByteByteGo's Top 12 Agent Skills, AIForLeaders.com's AI Industry
Trends, replace.so's GitHub-repo carousels) used the same numbered-badge
card grid, just with different colors. This is original CSS/HTML built to
approximate that recurring layout, not a copy of any one source's actual
code or assets. Verified in both light and dark variants via a headless
Chromium screenshot with zero console errors before being added.


## Batch 98 additions — four social-card themes (rendered and checked in headless Chromium)

| File | Theme tokens | Technique |
|---|---|---|
| `repo-briefing-card.html` | `--bg-top #14213f` → `--bg-bot #05070d`, `--green #3fb950`, `--amber #d9a93f`, mono `JetBrains Mono` | 1080×1920 slides generated from one `REPO` data object; flow strip highlights step `REPO.hi`; preview scale `--s`, export at `--s:1` |
| `font-showcase-glow.html` | per-slide `--glow`: cyan `#2fd5e6`, green `#2fe08a`, violet `#8a6bff`, blue `#2f8bff`, orange `#ff9a5c`, yellow `#f5d63d`, pink `#ff5a78` on `#060608` | numeral = dark fill + `-webkit-text-stroke` + stacked `drop-shadow` glow via `color-mix()`; SVG `feTurbulence` grain overlay; rim-lit orbs |
| `wordmark-noir-card.html` | `--bg #080808`, spheres `#2a0004 → #ff3b3f`, silver `#f6f6fa → #7d7d88` | `background-clip:text` gradient wordmark, 135°/315° sphere gradients, ruled index bar |
| `tool-spotlight-light.html` | white, ink `#0a0a0a`, dim `#8b867f`, chrome `#ecebe8`, `Hanken Grotesk` | `**bold**` markup in the body string, browser frame with traffic lights bleeding off the slide |
| `prompt-card-carousel.html` | @StackFlo / @ai_slacker (Batch 99) | One data array drives both a light and a dark card style; `[PLACEHOLDER]` words are auto-highlighted; flow layout so long prompts never overlap the footer |
| `repo-card-grid.html` | @joshualevi.ai / @replace.so (Batch 99) | CSS-only 3D asterisk from four rotated gradient bars; stat card with a language colour bar; `THEME` switches to the dark pixel-grid variant |
| `agent-flow-chat-card.html` | @ai.global.lee (Batch 99) | Per-agent `--accent` colour tints the pill, headline word, chat bubbles, tiles and bar via `color-mix()` |
| `mascot-tips-orange.html` | @aicareersuite (Batch 99) | Inline-SVG mascot recoloured by one variable; headline size auto-fits the longest line |
| `fine-print-skill-card.html` | @ai.easily (Batch 100) | One frame for cover, recap and skill slides; gold keywords via `<b>` in the headline string |
| `role-map-infographic.html` | 51ultron (Batch 100) | Data-driven 3-column card grid; colours cycle through a palette array; tall 1080 x 2100 poster |
| `gradient-prompt-orange.html` | @ai.blueprint (Batch 101) | Layered radial gradients plus a CSS-only 12-ray starburst from rotated bars |
| `lime-explainer-dark.html` | @tinrovicai (Batch 101) | One slide builder drives cover, comparison and warning cards; highlight card gets a lime outline and glow |
| `app-category-glass.html` | @jeanbbttyct (Batch 101) | `backdrop-filter` glass panel over a swappable background; app tiles are coloured initials, not vendor logos |
| `paper-tool-card.html` | @clicksandranks (Batch 101) | SVG `feTurbulence` paper grain as a data-URI background; cover uses a yellow highlighter mark |
| `dark-grey-install-card.html` | @the.wealth.lab (Batch 101) | Flat charcoal card; the install command is a data field so each card carries the right one |
| `sales-method-grid-teal.html` | SalesDaily.co "20 Sales Methodologies for B2B Selling" | 4 x 5 CSS grid built from a `CARDS` array (title, what, when, best); teal `--teal` tokens; collapses to 2 columns on mobile; pre-filled from `sales-methodologies-20`; theme `salesdaily-teal` |
| `level-cards-pastel.html` | NipPro AI "The 3 Levels of Agentic Marketing" | Three cards of stepped min-heights from a `LEVELS` array with per-card `--c/--t/--k` pastel tokens, serif display numerals, two `STATS` tiles; pre-filled from `agentic-marketing-levels`; theme `pastel-levels` |
| `prompt-text-card-cyan.html` | @theaiguyhere "ChatGPT / LLM / Prompts" cards | 540 x 675 (4:5) cards from a `CARDS` array under one `SERIES` header (avatar, handle); pale cyan `--bg`; large bold text kept legible on a phone; pre-filled with two prompts from `photoshoot-prompts-7`; theme `cyan-prompt-text` |
| `bug-lesson-card.html` | @jek.notes "10 Developer Problems You Won't See Until Production" | 540 x 675 card from one `SLIDE` object (kicker, headline lines with one `<em>` red line, problem, flow chips, to-do list, think box, counter); Anton/Impact fallback; theme `engineering-red` |
| `checklist-panels-peach.html` | @aisimplified23 "Claude Checklist" | 3-column panel grid built from a `PANELS` array with `**bold**` markers parsed safely (no innerHTML); collapses to 2 then 1 column; pre-filled with three panels from `claude-checklist`; theme `peach-checklist` |
| `kpi-framework-gold.html` | Oana Labes "The CEO KPI Framework" | `LAG` and `LEAD` arrays render checkbox KPIs with formulas; three gold tints via `nth-child`; pre-filled with 18 of the 33 KPIs from `ceo-kpi-framework` (corrected churn formula); theme `kpi-gold` |
| `ui-tip-do-dont.html` | @iqonicdesign "5 Tips To Help You In UI Design" | Wireframe pair from placeholder blocks, circular mark half-overlapping the card edge; pre-filled with tip 1 of `ui-image-layout-5-tips`; theme `soft-blue-tip` |

**Gotcha found while verifying:** a font name passed into an inline `style="font-family:…"` must use *single* quotes (`'Fredoka'`) — double quotes silently break the attribute and the card falls back to the default font.

**Sandbox note:** Google Fonts is not reachable from the cloud sandbox, so screenshots taken there show fallback fonts; layouts are sized with headroom for that. Re-check in a normal browser before exporting.

### Font substitutes (the specimens are mostly NOT on Google Fonts)

The @designarchitect001 carousels captioned "google fonts", but checking the Google Fonts metadata endpoint (`fonts.google.com/metadata/fonts`, 2026-10-01) found only **Urbanist** and **Outfit** among the twelve names shown. Use the real files if you license them; otherwise these Google families are look-alike substitutes — **judgement calls, not matches**:

| Specimen (as shown) | On Google Fonts? | Substitute used in templates | Character being approximated |
|---|---|---|---|
| Nura | no | Fredoka 600 | heavy rounded geometric caps |
| Ancola | no | Sora 700 | wide geometric lowercase with cut strokes |
| Urbanist | **yes** | Urbanist 500 | — |
| Alro | no | Manrope 800 | bold geometric, stencil-like bar |
| Outfit | **yes** | Outfit 800 | — |
| Surgena | no | Comfortaa 700 | rounded display with quirky terminals |
| Ourova / Qurova (first glyph unclear) | no | Quicksand 300 | monoline circular geometric |
| Rigter | no | Gabarito 800 | heavy tight grotesk |
| Malison | no | Saira Condensed 700 | tall condensed, techno |
| Keratus | no | Syne 600 | calligraphic-geometric hybrid |
| Sparling | no | Unbounded 800 | heavy rounded with sharp notches |
| Badoga | no | Cormorant Garamond 400 | high-contrast display serif with swashes |

Original-source files for the unlisted ones are probably commercial or free-for-personal-use foundry releases — **licence unverified**; check before commercial use.

## Batch 99 theme tokens (colours and fonts read from the screenshots)

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| StackFlo light | paper `#f6f8fd`, blue `#2f6fe0`, navy `#151c3a`, quote box `#eef3fd` | Poppins |
| ai_slacker dark | `#000` on `#fff`, no accent | Inter (the original looks like a grotesque similar to Neue Montreal) |
| joshualevi.ai | grid paper `#eeede9`, orange `#cf5a2e`, ink `#1d1d1d`, soft `#77736d` | Inter |
| replace.so dark | `#111` with green pixel grid, white type | Inter |
| ai.global.lee agent card | cream `#fbf6ef`, accents blue `#1f63e6` / orange `#f26a1b`, green `#1f9d55` | Inter 900 |
| aicareersuite mascot | cream `#fdf8f3`, peach `#fbe6d2`, orange `#f26a1b`, ink `#111` | Inter 900 |

The original specimens use proprietary or unidentified fonts; these are look-alikes, not matches.

| Batch 100 theme | Colours | Font (look-alike) |
|---|---|---|
| @ai.easily teal and gold | gold `#e3a72f`, cream `#f4efe6`, teal field `#16444f` to `#0b1519` | Plus Jakarta Sans |
| 51ultron cream poster | paper `#f6efe4`, ink `#151b2d`, blue `#2a5fc0` | Playfair Display + Inter |

| Batch 101 theme | Colours | Font (look-alike) |
|---|---|---|
| @ai.blueprint | deep `#0b1033`, violet `#2b1f9c`, sky `#1e6cf0`, orange `#ff6a2b` | Poppins |
| @tinrovicai | field `#08081a`, card `#0f1022`, lime `#c6f432` | Space Grotesk + Inter |
| @jeanbbttyct | glass `rgba(255,255,255,.14)` over a dark photo | Inter |
| @clicksandranks | paper `#efebe4`, ink `#0c0c0c`, teal `#1596a8`, highlighter `#f8f0a4` | Archivo |
| @the.wealth.lab | charcoal `#404044`, band `#000`, yellow `#ffe51f`, amber `#f2b705` | Oswald + Inter |


## Batch 102 theme tokens (colours read from the screenshots)

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `salesdaily-teal` | teal `#3F7F95`, dark teal `#2C6478`, ink `#1F2A44`, warm grey `#E9E3E2`, accent red `#D6453D` | Poppins or Inter (bold uppercase title) |
| `pastel-levels` | pink `#FBB0CC`, peach `#FFD791`, lilac `#CDB8FF`, ink `#111`, footer beige `#F7EFE9` | Playfair Display + Inter |
| `cyan-prompt-text` | cyan `#CFFFFF`, ink `#1F2933` | Nunito Sans (bold) |
| Cyberman AI dream-job card | cream `#FFF7F0`, orange-red `#E8420F`, ink `#111` | Archivo Black + Inter |
| Reno Perry hacks | white, ink `#111`, orange highlight `#F5841F`, per-box accents pink/teal/blue/purple/amber | Inter |
| Partaker mental models | pastel boxes: yellow `#FFF3C4`, pink `#FADBD8`, lilac `#E6DBFA`, green `#D9F2E1`, blue `#DCE6FA`; footer blue `#2B6FE0` | Playfair Display + Inter |
| Lever analytics | mint `#DFF3E9`, olive `#EDE7C4`, ink `#17382E`, highlight `#F3F7B5` | Inter |

## Batch 103 theme tokens (colours read from the screenshots)

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `engineering-red` | paper `#F1F0EE`, ink `#141414`, red `#C8202F` | Anton (headline), Inter |
| `peach-checklist` | bg `#F6E9E4`, panel `#E9B8A6`, edge `#D8997F`, header `#17171A`, accent `#E07A52` | Playfair Display Black, Inter |
| `kpi-gold` | black `#0B0B0B`, yellow `#F4C81D`, cream `#FBF4D6`, golds `#F1E2B4` `#E7D08A` `#D6B65A` | Inter ExtraBold |
| `soft-blue-tip` | `#F4F7FF` to `#E6EDFB`, placeholders `#C9CDD3`, red `#D63B3B`, green `#2DB45A` | Plus Jakarta Sans |
| itsaiguide thumbnail | red radial glow, white title, red underlined section number, black bold quote | Anton + Inter (photo not reproduced) |


## Batch 104 additions — three templates (rendered and checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `repo-spotlight-browser-card.html` | "6 / 7 GitHub repos so good they shouldn't be free" carousels (@replace.so) | 1080×1350 slides; fading navy square grid built from two `repeating-linear-gradient` layers and a `mask-image`; app tile + star row; light browser window with a URL bar and a `.shot` slot; cover and repo slide in one file |
| `photo-overlay-tool-card.html` | "Open-source tools for your app business" carousel (@dotdevs) | 1080×1920 slides; `--photo` custom property under a `--scrim` gradient (default is a CSS dusk scene, so it works with no image); centred wordmark, framed screenshot slot, three-line caption |
| `code-card-six-lines.html` | "6 ML Algorithms" code video (@machinelearningtogo) | Editor window with numbered lines and syntax spans; six colour-coded chips (click or press 1-6) highlight one line range each and update the caption; pre-filled with the six lines in `scripts/ml_six_key_lines.py` |

All three use a placeholder handle (`@yourhandle`). No source photo, logo, screenshot or watermark was reused. Pre-filled text is the carousel text or the video's code; swap it before publishing as your own.

## Batch 104 theme tokens

Colours marked **sampled** were read from pixels in the screenshots; the rest were judged by eye.

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `navy-repo-spotlight` | bg `#121214` (sampled `#151314`), grid navy `rgba(48,76,140,.40)`, title `#F3F1F2` (sampled), browser bar `#F3F2F4` (sampled), browser body `#FEFEFE` (sampled), caption `#A9ADBA`, star `#F5B72D` | Inter 800 with tight tracking (the specimen is a heavy grotesk; the match is a judgement) |
| `porch-photo-scrim` | sky `#4A5359`, foliage `#13180E`, table `#292929` (all sampled after the scrim), white text, scrim 55% black | Outfit (on Google Fonts; a close match to the specimen) |
| `ml-code-card` | page `#0A0F17` and window `#0A0E1B` (sampled), keyword `#5AA2FF`, number `#F6B93B`, function `#4DD0E1`, comment `#7080A0`, step chips yellow `#F6C445`, blue `#4FA3FF`, green `#4ADE80`, orange `#FB923C`, violet `#A78BFA`, pink `#F472B6` | JetBrains Mono + Inter |

## Batch 105 additions — five templates (rendered and geometry-checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `skill-spotlight-teal-gold.html` | "4 Claude skills for people who don't code" (@ai.easily) | 1080×1350; radial teal gradient, oversized gold counter, gold-outlined "fine print" panel; cover, skill and recap slides in one file |
| `grid-paper-repo-command-card.html` | "Top 5 Claude Code design skills" (@awayfromlovable) | 1080×1920; CSS-grid paper background, terracotta rank over a heavy headline, screenshot slot, GitHub-style repo card, monospace command line, and a save/share/follow slide with a clipped ribbon |
| `ai-team-role-card.html` | "I replaced myself with 10 AIs" (@aigenesis.official) | 1080×1350; faint grid, glossy tile built from gradients and inset shadows, spaced role label, huge tool name, dark screenshot slot, tile-cluster cover |
| `swap-tool-lavender-card.html` | "8 underrated open source tools" (@coreclasseducation) | 1080×1296; layered radial blooms on lavender, dark app tile, "If you're paying for X, try this instead", dark window with placeholder rows. The window says to replace it with a real screenshot: the source carousel used generated mockups |
| `compare-two-approaches-cream.html` | "JEV vs LLM" infographic (AIForLeaders.com) | 1080×1350; cream page, two flow cards around a shared-context node, two "use when" lists, caution line, dark footer bar. Geometry checks confirm no node leaves its card and the caution line clears the bar |

All five use placeholder handles (`@yourhandle`, `Your brand`). No source logo, photo, screenshot, copy or watermark was reused; pre-filled text is the carousel's own wording or neutral filler, so swap it before publishing as your own.

## Batch 105 theme tokens

Colours marked **sampled** were read from pixels in the screenshots; the rest were judged by eye.

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `teal-gold-skill` | gradient `#173D49` to `#122E37` to `#0E1922` (all sampled), panel `#202F33` (sampled), gold `#E8A92E`, ink `#F4F1EA`, muted `#8A98A1` | Plus Jakarta Sans 800 (a close match; not confirmed) |
| `grid-paper-terracotta` | paper `#F5EEE8` (sampled), terracotta `#D77655` (sampled), ink `#121212`, repo link blue `#0B63D6`, grid `#E6DCD3` | Inter 900 with tight tracking, JetBrains Mono for commands |
| `org-chart-glossy` | page `#FDFDFD` (sampled), dark screenshot body `#020202` (sampled), role label `#C9684A`, ink `#0F0F0F`, sub `#727272` | Space Grotesk 700, Space Mono for the label |
| `lavender-swap` | indigo `#4D23D8` (sampled), window `#222631` (sampled), window button `#A282F9` (sampled), page `#FAF9FF`, bloom `rgba(139,92,246,.22)` | Plus Jakarta Sans 800 |
| `cream-compare` | cream `#F6F0E9` (sampled), card `#FBF8F1` (sampled), navy `#16294D`, teal `#0B9C86`, blue `#2450D8`, caution `#E5543A` | Source Serif 4 800 for titles, Inter for body |

## Batch 106 additions — five templates (rendered; element overlap and containment checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `mod-explainer-dark-terracotta.html` | "Redesign Claude Code yourself" (@taha_pathionai) | 1080×1350; charcoal page, heavy tight headline with a terracotta last line, definition rows with one lit row, hairline numbered list, counter and handle |
| `repo-feature-cream-number.html` | weekly trending-repos carousel (@aiclawbots) | 1080×1350; huge terracotta rank number, GitHub-style white card with stats and a blue accent rule, three info pills, and a "which ones I would use" table slide; the mascot is a plain CSS badge |
| `prompt-card-beige-green.html` | micro-app prompt carousel (@earchoe) | 1080×1920; beige page, serif all-caps headline, green instruction bar, dark monospaced prompt box, three step tiles; second slide for a quote and four numbered checks |
| `caption-highlight-blue-grid.html` | Hermes LinkedIn series (@aiclawbots), money-photo captions (@penny.blanco6) | 1080×1920; graph-paper blue page with a white diagram card, and captions as individual white highlighter strips; second slide puts the same strips over a photo through one `--photo` property |
| `dashboard-showcase-light-blue.html` | "Top 5 dashboard design of the month" (@amirabanal) | 1080×1350; pale blue page, "01 — Name" title, industry line, feature bullets, counter pill, large screenshot frame and a designer credit line; cover with a tilted device frame. The credit line is there on purpose: show the designer's name when the design is not yours |

All five use placeholder handles (`@yourhandle`). No source logo, mascot, screenshot, photo or caption copy was reused. Two layout bugs (a footer sentence colliding with the fourth row; a feature list too close to the title) were found on first render and fixed.

## Batch 106 theme tokens

Colours marked **sampled** were read from pixels in the screenshots; the rest were judged by eye.

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `charcoal-terracotta` | bg `#141414` (sampled), row `#1F1D1C` (sampled), terracotta `#D77655` (sampled), ink `#F1EEE6`, muted `#9A958C` | Red Hat Display 900 plus Red Hat Mono (the specimen looks like Red Hat Display; not confirmed) |
| `cream-terracotta` | cream `#F8F3E7` (sampled), rank number `#D45733` (sampled), card white, rule blue `#3B82F6` | Archivo 800, IBM Plex Mono |
| `beige-green-prompt` | beige `#DAD5C1` (sampled), tile `#CEC7B1` (sampled), green bar `#71AD79` (sampled; label green `#2FA054` eyeballed), code box `#151310` | Playfair Display 900, JetBrains Mono |
| `blueprint-captions` | blue `#044672` (sampled), white strip, accent `#3AA0FF` | Montserrat 700 |
| `pale-blue-showcase` | pale blue `#DBE9FD` (sampled), ink `#0E1A2B`, pill `#8C97A6` | Inter, Instrument Serif for the cover |

## Batch 107 additions — three templates (rendered; element overlap and containment checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `prompt-step-red-cream.html` | "Stop using Claude one prompt at a time" (@ai.am.claude) | 1080×1080; cream page, huge red step number, heavy two-tone headline, red-dot bullets, rounded "prompt example" box, small-caps tagline and counter, flat red/slate/stone block art on the right; cover and step slides |
| `trending-top10-leaderboard.html` | "10 hottest GitHub repos today" (@githubnow) | 1080×1920; near-black page, green date pill, ten-row leaderboard (rank, repo, purpose, stars today) with a lit top row, and an "unverified" note |
| `quant-code-pane-dark.html` | "Quant finance from scratch" and "Machine Learning from Scratch" (@quantfinancetogo, @machinelearningtogo) | 1080×1920; near-black page, amber part label, centred title, chart card with a CSS bell-curve placeholder, caption, numbered code pane with one lit line and muted comments, disclaimer footer |

All three use placeholder handles (`@yourhandle`). No source illustration, figure, animation, logo or caption copy was reused. A cover headline running under the art blocks and a headline overlapping its lead line were found on first render and fixed.

## Batch 107 theme tokens

Colours marked **sampled** were read from pixels in the screenshots or video frames; the rest were judged by eye.

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `red-cream-workflow` | cream `#FAF7EF` (sampled), red `#DE2918` (sampled), dark red `#5F0904` (sampled), stone `#E5E0D4` (sampled), prompt box `#F8F6F5` (sampled), slate `#3B4A52` | Inter 900 with tight tracking (the specimen looks like a heavy grotesque; not confirmed) |
| `night-leaderboard` | bg `#0D1117`, row `#161B22`, green `#3FB950`, muted `#8B949E` (GitHub-dark look, eyeballed) | Inter 900, JetBrains Mono |
| `night-amber-code` | bg `#08090E` (sampled), panel `#0C0F16` (sampled), amber `#F2A93B` (eyeballed), muted `#6B7385`; the Attention video uses bg `#0A0F17` (sampled) | Inter 800, JetBrains Mono |

## Batch 108 additions — two templates (rendered; element overlap and containment checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `photo-step-tools-caption.html` | "The exact app-building method" (@dolorstca2h) | 1080×1920; full-bleed photo (CSS gradient fallback) under a dark scrim, numbered step title, one or two tool rows with icon tile, "Tool — Role" label and caption, handle bottom right; cover, one-tool and two-tool slides |
| `gtm-stage-three-column.html` | "9 GTM Infographics" cover | 1080×1350; periwinkle page, centred title with arrow, three-step rising chart and three stage cards (name, ARR pill, goal, bullets) |

Both use placeholder handles (`@yourhandle`). No source photo, logo, graphic or caption copy was reused.

## Batch 108 theme tokens

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `photo-scrim-white` | scrim `rgba(8,8,10,.52)` over a photo, white ink, tile white, accent `#2F6BFF` (eyeballed) | Inter 600 |
| `periwinkle-stages` | bg `#D4DFFE` (sampled), card `#F2F9FF` (sampled), stage 3 `#A4E7FF` (sampled), stage 1 `#FFE9A8` and stage 2 `#FFC9A8` (eyeballed), ink `#0E1A2B` | Inter 800 |
| `night-briefing-green` (reference only, existing template `github-trending-card` is close) | bg `#111526` (sampled), green `#4EAE5E` (sampled), gold stars pill (eyeballed) | Inter, JetBrains Mono |

## Batch 109 additions — one template (rendered; element overlap and containment checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `swap-card-photo-github.html` | "5 open source apps that replace paid subscriptions" (@dotdevs) | 1080×1920; dark photo (CSS gradient fallback) under a scrim, round-corner app icon, tool name, "replaces ..." line, white GitHub-style repo card with stat chips, link line and handle; cover slide with an icon row |

Uses the existing `photo-scrim-white` theme; placeholder handle `@yourhandle`; no source photo, icon or caption copy reused.

## Batch 110 additions — one template (rendered; element overlap and containment checked in headless Chromium)

| File | Inspired by | Technique |
|---|---|---|
| `avoid-reason-say-grid.html` | "10 Things NOT to Say in a Job Interview" (Dr. Christian Poensgen) | 1080×1350; warm grey page, big condensed navy title with teal tag, three-column grid of numbered cards each with Avoid (red cross), Reason (amber question mark) and Say (green tick), footer bar |

## Batch 110 theme tokens

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `grey-teal-guide` | bg `#E7E5E4` (sampled), number line `#CEE4DF` (sampled), navy `#0F2D3A` and teal `#8CC1B5` (eyeballed), red `#D8342C`, amber `#F2A93B`, green `#2E9D4F` | Oswald 700 for the title, Inter for body |
| GTM roadmap (reference only; existing template `gtm-stage-three-column` is close) | black `#0A0A0A` (sampled), purple `#60369E` (sampled), yellow `#F0EF4B` (nearly sampled), green block `#B8F56A` (eyeballed) | Inter 800 |

## Batch 111 additions - eight templates (rendered; element overlap and containment checked in headless Chromium, 19 Oct 2026)

| File | Inspired by | Technique |
|---|---|---|
| `paid-vs-free-signal-card.html` | "Use these free dev tools instead" carousel (@modelsignal) | 1080x1350; cool grey page, huge tight title, a pale PAID card and a rust FREE card with icon tiles, big prices, mono captions, verdict line; print the price-check date in the caption |
| `blueprint-sheet-16.html` | "LinkedIn Client Acquisition in one page" | 1080x1350; cream drawing sheet, mono title block, 4x4 grid of pastel mini-cards with code label, title, preview band and arrow caption, blue CTA pill |
| `quadrant-puzzle-center.html` | four-quadrant unified-intelligence analyst graphic | 1080x1350; sky gradient, orange-bordered callout, navy disc cut by a white cross with a glowing centre label, a five-bullet list per quadrant |
| `org-chart-neon-dark.html` | Claude Code marketing-team org chart | 1080x1350; near-black page, gradient headline, orchestrator node, two rows of five coloured department chips each over five neon-outlined role cards |
| `metric-pairs-spine.html` | "Your Marketing Metrics Can Lie" | 1080x1350; serif headline, blue and plum pill headers, six numbered pairs of tinted cards joined by lime arrow nodes on a grey spine, black footer bar |
| `evidence-wheel-radial.html` | clinical evidence-level wheel | 1080x1350; SVG ring drawn from a `SEGMENTS` array (tiers high / mid / wip), legend row, centre disc with title and ticked principles; **placeholder labels only, a cited source is required before real clinical content is shown** |
| `prompt-grid-9-olive.html` | "9 AI prompts for better sales emails" | 1080x1350; huge olive numeral and condensed headline, nine white cards with number badge, icon square, prompt with highlighted placeholders and an Impact line, newsletter footer |
| `board-dashboard-gold.html` | "The Complete Board Dashboard" | 1080 wide, auto height; cream page, four black KPI tiles, twelve-cell ratio grid with ok/bad colouring, fourteen gold-tabbed panels with placeholder bars, black footer; every number is an `X` placeholder |

All eight use original CSS and placeholder wording; no source logo, avatar, illustration or copy is reused.

## Batch 111 theme tokens (files in `Artifacts/theme-*.html`)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-signal-rust-mono.html` | bg `#E1E6EC` (sampled), surface `#F1F4FB` (sampled), text `#0B1C2E` (sampled), accent `#B4321A` (sampled) | bg `#0B1C2E`, accent `#E0573A` | Inter 800 + JetBrains Mono |
| `theme-blueprint-cream-sheet.html` | bg `#F3ECE1`, surface `#FBF7EF`, accent `#1D5FD1` | bg `#1A1814`, accent `#6FA0FF` | Inter + JetBrains Mono |
| `theme-neon-org-dark.html` | bg `#F3F5FB`, accent `#6D28D9` | bg `#000D1D` (sampled), surface `#07162B`, accent `#8E3FE6` (sampled) | Inter + JetBrains Mono |
| `theme-olive-paper.html` | bg `#EBEBE9` (sampled), surface `#FFFFFF`, accent ink `#5C6000` | bg `#151610`, accent `#C9CE3A` | Inter 800 (+ Oswald for display) |
| `theme-quadrant-navy.html` | bg `#E2F2FF` (sampled), text `#0A2A66`, accent `#2198FF` (sampled) | bg `#06142F`, accent `#4DB1FF` | Inter |

Each theme file sets body 11pt, title 32pt, headings 14pt, Aptos first in the font stack, and tables aligned top and centre.

## Batch 112 additions - four templates (rendered; containment checked in headless Chromium, 19 Oct 2026)

| File | Inspired by | Technique |
|---|---|---|
| `ui-tip-before-after.html` | UI-design-tips carousel (@ux_dose) | 1080x1350; white page, five pill tabs with one active, huge tight headline, grey rule line, two cards tagged Before (heavy shadow) and After (soft shadow), SWIPE pill footer |
| `side-hustle-serif-dark.html` | AI side-hustle carousel (@earchoe) | 1080x1350; near-black, green rule, serif headline with a capitals second line, monospace body, SOURCE-AI-CHECK-PACKAGE-SELL pipeline or COPY THIS prompt box |
| `replaces-list-card.html` | "25 tools that feel illegal to be free" list (@will.ai.m) | 1080x1350; white page, five numbered soft-shadow rows with icon square, REPLACES label, name, job and FREE star count; footer states stars are unverified |
| `parchment-repo-card.html` | "5 GitHub projects" series (@sitetusk) | 1080x1350; parchment page, wordmark and heavy rule, large repo slug, white README-screenshot panel, one-sentence description |

All four use original CSS and placeholder wording; no source logo, mascot, texture or copy is reused. A fifth, a GitHub-trending dark card, was dropped because `github-trending-card` and `repo-briefing-card` already cover that style.

## Batch 112 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed, not sampled)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-ui-white-ink.html` | bg `#F6F6F7`, text `#0E0F12`, accent `#3B5BFF` | bg `#0F1013`, accent `#8EA2FF` | Inter |
| `theme-hustle-serif-dark.html` | bg `#F4F1E8`, accent `#1E8A4C` | bg `#141310`, accent `#5EE08A` | Playfair Display + JetBrains Mono |
| `theme-replaces-list-white.html` | bg `#FFFFFF`, accent `#D9481F` | bg `#111215`, accent `#FF7A4D` | Inter |
| `theme-parchment-tusk.html` | bg `#E2D8C5`, accent `#134B4B` | bg `#17150F`, accent `#6FC2C2` | Jost |

## Batch 113 additions - four templates (rendered; containment checked in headless Chromium, 20 Oct 2026)

| File | Inspired by | Technique |
|---|---|---|
| `periodic-table-grid.html` | glossary "periodic table" graphics (AEO terms, product-marketing terms) | 1080x1350; 5x7 grid of dashed-border square tiles (abbreviation, rule, full term), six family colours, legend beside the title, footer bar; placeholder terms only |
| `iceberg-waterline-steps.html` | "build a list in 7 steps, below the waterline" infographic | 1080x1350; sky half with a clip-path iceberg between two cards, waterline, deep-blue half with seven step cards around a numbered spine |
| `three-column-purpose-cards.html` | "3 types of content" comparison | 1080x1350; headline with highlighted word, three outlined columns (orange, violet, green) each with number, title, screenshot placeholder and four labelled sections, black footer |
| `file-explorer-system-card.html` | "complete system" folder-tree graphics | 1080x1350; dark code-editor window, sidebar tree, gradient headline, four outlined panels of eight numbered items, gradient call-to-action bar |

All four use original CSS and placeholder wording; no source logo, mascot, term list or copy is reused. Overlap checked: the existing `prompt-grid-9-olive` already covers the nine-card prompt grid, so no template was added for it; the dark MCP command card is covered by `dark-grey-install-card`.

## Batch 113 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed, not sampled)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-periodic-pastel.html` | bg `#FFFFFF`, text `#1A2250`, accent `#4A3FD0` | bg `#12142B`, accent `#A9A4FF` | Inter |
| `theme-iceberg-blue.html` | bg `#EEF3FF`, text `#0F1A3C`, accent `#2F5BFF` | bg `#0B1230`, accent `#7C9BFF` | Inter |
| `theme-purpose-columns.html` | bg `#FFFFFF`, text `#14161C`, accent `#C8552D` (violet `#6A4FD0` and green `#3C9B45` as column colours) | bg `#14151A`, accent `#FF8A5C` | Inter |
| `theme-explorer-neon.html` | bg `#F3F5FB`, text `#0F1424`, accent `#5B3DDC` | bg `#070A12`, accent `#4DA3FF` | Inter + JetBrains Mono |


## Batch 114 additions

| Template | Use for | Layout |
|---|---|---|
| `tools-20-numbered-grid.html` | "20 tools" directory graphics | 1080x1350; two-line headline with one highlighted word, credit or sponsor line, 4x5 grid of numbered tiles (number, tool name, category, one-line job) with four category colours, dark footer |
| `keyword-framework-board.html` | SEO or strategy framework one-pagers | 1080x1350; teal headline, left spine of seven numbered steps, right chip cloud (ten types) and 2x4 metric grid, dark formula bar of five plus-joined terms ending in an amber result pill, teal footer |

Both use original CSS and placeholder wording only. Overlap checked: `workflow-grid-catalog` and `trending-top10-leaderboard` are list layouts of a different shape, and no existing template has a formula bar.

## Batch 114 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed from the template palette)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-gtm-tools-slate.html` | bg `#EEF1F6`, text `#101828`, accent `#2F6BFF` | bg `#0C1220`, accent `#7FA3FF` | Inter |
| `theme-keyword-teal-paper.html` | bg `#F6F1E7`, text `#10282C`, accent `#0F7C86` | bg `#0C1D20`, accent `#4FC3CD` | Inter |

## Batch 115 additions

| Template | Use for | Layout |
|---|---|---|
| `callout-hub-20.html` | "20 templates around one picture" graphics | 1080x1350; pill headline bar, tall central picture placeholder with a round badge, ten callout cards down each side (numbered bubble, coloured title bar, three lines of text) joined to the centre by dashed lines, dark footer |
| `spine-steps-detail-cards.html` | Seven-step process infographics with a checklist per step | 1080x1350; headline, vertical spine with seven numbered nodes, wide step cards (icon, title, description) with a tinted five-bullet panel on the right, footer with handle and save line |

Both use original CSS and placeholder wording only; no source illustration, logo or text is reused.

## Batch 115 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-callout-navy-pink.html` | bg `#FFFFFF`, text `#14213D`, accent `#E8479A` | bg `#0E1630`, accent `#FF7DBA` | Inter |
| `theme-spine-blue-soft.html` | bg `#F1F6FD`, text `#10223F`, accent `#2563EB` | bg `#0B1424`, accent `#6EA0FF` | Inter |


## Batch 116 additions

| Template | Use for | Layout |
|---|---|---|
| `two-tier-tree-14.html` | Two-level strategy trees (for example who you are / how you grow) | 1080x1350; highlighted headline, two dark head pills each joined by a bracket to a row of seven cards (icon circle, title, three lines), name pill and brand tag footer |
| `system-steps-grid-10.html` | "Build the whole system" ten-step graphics | 1080x1350; section tag, two-tone headline, 3x3 grid of numbered step cards plus one wide tenth card, red call-to-action bar |
| `story-stat-card.html` | One slide of a "I scanned and found" story carousel | 1080x1350; grid-paper page, counter, large number, mono tag line, bold headline, paragraph, six-row data card, two stat pills, next pointer |

All three use original CSS and placeholder wording only. Overlap checked: `workflow-grid-catalog`, `trending-top10-leaderboard` and `spine-steps-detail-cards` are different shapes.

## Batch 116 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-brand-tree-sage.html` | bg `#F5F2EA`, text `#1E2A24`, accent `#2E7D5B` | bg `#101A15`, accent `#5CC795` | Inter |
| `theme-system-red-white.html` | bg `#FFFFFF`, text `#1A1A1F`, accent `#D7263D` | bg `#170C0E`, accent `#FF5A6E` | Inter |
| `theme-story-grid-paper.html` | bg `#F7F4EE`, text `#1B1B1D`, accent `#D4623A` | bg `#14120F`, accent `#F08A62` | Inter + JetBrains Mono |


## Batch 117 additions

| Template | Use for | Layout |
|---|---|---|
| `framework-lever-board.html` | One-page "four levers" framework summaries (Influence-Model style) | 1080x1350; tag, two-tone headline, subtitle, 2x2 board of lever cards (number badge, title, quoted line, ask-your-team row, red-flag row), four-step strip, orange footer bar |
| `five-stage-column-matrix.html` | Five-stage journeys and five-phase models (Decision-Journey style) | 1080x1350; centred headline, dashed stage strip, five tall columns (header plus what happens, evidence, ask your team, your move, track), two summary panels, dark brand bar |
| `prompt-rows-6.html` | "N prompts to build X" guides | 1080x1350; uppercase title with orange band, dashed subtitle, six alternating rows (icon circle, big number, step name, prompt, description), promo bar and follow strip |

All three use original CSS and placeholder wording only. Overlap checked: `system-steps-grid-10`, `spine-steps-detail-cards` and `callout-hub-20` are different shapes. Render and overflow check done with Playwright at 1080x1350: no overflow or clipping.

## Batch 117 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed from the source graphics)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-framework-orange-ink.html` | bg `#FFFFFF`, text `#14213D`, accent `#E8590C` | bg `#0F1626`, accent `#FF8A3D` | Inter |
| `theme-journey-teal-gold.html` | bg `#F4F7F6`, text `#0F2A2E`, accent `#0E7C7B` (second accent gold `#C9962B` in the template) | bg `#0B1D20`, accent `#3CC3BF` | Inter |
| `theme-prompt-rows-orange.html` | bg `#F6F5F0`, text `#1B1B1B`, accent `#F26B1D` (second accent olive `#6B8E23` in the template) | bg `#17140F`, accent `#FF8A3D` | Inter |


## Batch 118 additions

| Template | Use for | Layout |
|---|---|---|
| `equation-multipliers-board.html` | Formula-style framework one-pagers (result = factor x factor x factor x factor) with supporting panels | 1080x1350; serif title, framed top panel with equation chips and captions, three coloured panels, numbered-list panel, red-header table panel, blue footer bar |
| `prompt-cards-2col-10.html` | "Best prompts for X" ten-card guides | 1080x1350; navy header band with two-tone title, 2x5 grid of cream cards (number circle, yellow name tag, icon block, quoted prompt), credit strip |

Both use original CSS and placeholder wording. Overlap checked: `prompt-rows-6` (six full-width rows), `callout-hub-20` and `tools-20-numbered-grid` are different shapes. Rendered at 1080x1350, no overflow.

## Batch 118 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-multiplier-blue-sky.html` | bg `#F6F7F9`, text `#12151C`, accent `#2F6BFF` (template adds teal, gold, green, orange, red panels; serif title Playfair Display) | bg `#0E1220`, accent `#6C95FF` | Inter |
| `theme-office-teal-orange.html` | bg `#EEF1F4`, card `#FBF6E9`, text `#14213D`, accent `#0B7F69` (template uses brighter teal `#17C3A0` and orange `#F26B1D` on a navy band) | bg `#0A1628`, accent `#2FD1B0` | Inter |


## Batch 119 additions

| Template | Use for | Layout |
|---|---|---|
| `landing-anatomy-callouts.html` | Annotated page anatomies (a wireframe with numbered callouts) | 1080x1350; serif title with highlighted italic word, subtitle band, browser wireframe in the centre, seven numbered callout cards each side, credit line |
| `radial-principles-7.html` | Seven-principle frameworks around a quote hub | 1080x1350; bold uppercase two-tone title, three rows (7, 1, 2 / 6, hub, 3 / 5, spare note, 4), each card with ring number, title, rule, why it works, example; blue footer bar |
| `ide-install-list-40.html` | "N things to install" lists styled as an editor README | 1080x1350; window bar, tab strip, file-tree sidebar with folder counts, large title, five colour-coded groups listing 40 numbered rows, credit bar |

Original CSS and placeholder wording only. Overlap checked: `callout-hub-20` (20 spokes) and `framework-lever-board` (2x2) are different shapes; `radial-principles-7` is the seven-spoke version. Rendered at 1080x1350 with no overflow or clipping.

## Batch 119 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-anatomy-royal-blue.html` | bg `#F6F7FB`, text `#0B0F2A`, accent `#1F2BD6` (template title uses Playfair Display) | bg `#0A0D1F`, accent `#7C86FF` | Inter |
| `theme-story-blue-ink.html` | bg `#FFFFFF`, text `#0A0A0A`, accent `#1D4ED8`, hub `#CFE6FB` | bg `#090B12`, accent `#6C95FF` | Inter |
| `theme-terminal-orange-night.html` | bg `#F4F5F8`, text `#10131A`, accent `#C2561B` (the template is dark-first with bright orange `#F2874B`) | bg `#0A0D14`, accent `#F2874B` | Inter + JetBrains Mono |


## Batch 120 additions

| Template | Use for | Layout |
|---|---|---|
| `cowork-prompt-grid-10.html` | "10 prompts that save N hours" guides | 1080x1350; logo chip, three-line title with an orange last line, 3x3 grid of white cards (number circle, icon block, bold title, prompt text) plus one wide tenth card, outlined newsletter pill |
| `use-case-columns-50.html` | "N use cases" reference lists | 1080x1350; bold title with an accent pill, three tall outlined columns in blue, amber and purple holding 17, 17 and 16 numbered entries, follow bar |

Original CSS and placeholder wording only. Overlap checked: `prompt-grid-9-olive` (nine cards), `prompt-cards-2col-10` (2x5) and `tools-20-numbered-grid` are different shapes. Rendered at 1080x1350, no overflow.

## Batch 120 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-cowork-orange-cream.html` | bg `#FBF3EA`, text `#14110F`, accent `#C84A08` (template uses `#E8590C`) | bg `#16110C`, accent `#FF8A3D` | Inter + Playfair Display |
| `theme-usecases-triple-border.html` | bg `#FFFFFF`, text `#101418`, accent `#0C70DB` (template adds amber `#F2A900` and purple `#9B51E0` columns) | bg `#0B0F16`, accent `#5AB0FF` | Inter |


## Batch 121 additions

| Template | Use for | Layout |
|---|---|---|
| `framework-cards-lavender-5.html` | "N simple frameworks" explainers (best for, why it works, structure) | 1080x1350; periwinkle frame, two-line title with lavender highlight, italic subtitle, two columns of five cards of different heights with lavender headers and orange-edged structure rows, footer bar |
| `hub-tall-center-4-sides.html` | "Who owns what" function maps | 1080x1350; gradient page, title with pink-highlighted word, tall pink centre card (what it is, day-to-day work, success metrics, closing line) with two coloured cards on each side |

Original CSS and placeholder wording only. Overlap checked: `spine-steps-detail-cards`, `framework-lever-board` and `five-stage-column-matrix` are different shapes. Not built this batch: an isometric staircase diagram (the TAM playbook graphic) and a tall four-section setup guide; both need hand-drawn art and were skipped rather than faked. Rendered at 1080x1350, no overflow.

## Batch 121 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-framework-lavender-orange.html` | bg `#FFFFFF`, card `#FFFBF2`, text `#0B0B12`, accent `#4A5BE8` (template adds lavender `#E9E4FF` and orange `#F5A623`) | bg `#0E1020`, accent `#8E9CFF` | Inter |
| `theme-pmm-pastel-pink.html` | bg `#EEF0FF`, text `#17104D`, accent `#C0147F` (template adds pink `#FF9AD1` and four pastel header colours) | bg `#120C2E`, accent `#FF7CC4` | Inter |


## Batch 122 additions

| Template | Use for | Layout |
|---|---|---|
| `variance-chart-gallery-8.html` | "N ways to show X" chart-type galleries (finance variance views, dashboard widgets) | 1080x1350; charcoal page, white title with two lime-highlighted words, subtitle, four-by-two grid of light tiles (number badge, name, small CSS chart, "Best for" line), footer strip |
| `verdict-table-5.html` | "Which ones I would use" verdict slides ending a repo or tool roundup | 1080x1350; cream grid-paper page, mono handle and page counter, very large two-line title, white card of five rows (mono name, verdict; first row tinted), italic-style closing line |

Original CSS and placeholder wording only. Overlap checked: `trending-top10-leaderboard`, `repo-card-grid` and `two-column-shift-comparison` are different shapes. Not built: more repo-spotlight cards (the library already has seven repo-card templates). Rendered at 1080x1350, no overflow; a first waterfall tile was drawn with margins and broke, then rebuilt with absolute positions.

## Batch 122 theme tokens (files in `Artifacts/theme-*.html`; colours eyeballed)

| Theme file | Light | Dark | Fonts (free) |
|---|---|---|---|
| `theme-fpna-charcoal-lime.html` | bg `#F4F5F2`, text `#14171A`, accent `#3F7A0C` (template uses lime `#A8F04B` on charcoal `#2B2E31`) | bg `#2B2E31`, accent `#A8F04B` | Inter |
| `theme-trending-cream-rust.html` | bg `#FBF4E8`, text `#0F0F10`, accent `#C2410C` | bg `#1B1712`, accent `#FF8A4C` | Inter + JetBrains Mono |
