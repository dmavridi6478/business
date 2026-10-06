---
name: design-templates
description: Ready-to-use, self-contained HTML/CSS templates for common content-visual needs — an iMessage chat mockup, a vertical social/story device frame, a 3D-tilted product screenshot mockup, a halftone/dithered image effect (both CSS-only and real canvas dithering), a logo/reference moodboard grid, a brand board (wordmark + palette + type pairing + app preview), a SaaS pricing table + comparison grid, a restrained editorial hero, a numbered infographic card grid (light/dark variants), a filterable design-reference-site dashboard, a light "Save For Later" social carousel (carousel-save-for-later), a dark neon agent info card (dark-neon-agent-card), a dark orange-gradient tutorial step-cards layout (dark-orange-agent-tutorial), a GitHub-style dark trending repo card (github-trending-card), a bold red grunge AI-tools carousel (@ai.global.lee style, red-grunge-ai-tools), a warm editorial carousel for thinking-partner / Claude workflow content (@parm.ai style, editorial-thinking-partner), a dark space-themed OSS repo card (@datawarlord_official style, datawarlord-oss-card), and a nature photo background with glassmorphism panels carousel (@softgirlnocode AI video style, softgirlnocode-nature-glassmorphism), a light/dark copy-this-prompt carousel (prompt-card-carousel), a repo-showcase card set (repo-card-grid), an agent explainer flow card (agent-flow-chat-card), and an orange mascot tips carousel (mascot-tips-orange), plus seven Batch 104 templates: a navy GTM diagnostic heatmap (gtm-heatmap-navy), an agent-roster department grid (agent-roster-grid), a first-100-customers staircase (stage-roadmap-steps), a radial 60-tool wheel (tool-wheel-radial), a four-theme repo-of-the-day slide (repo-card-slide), an avoid/say-instead list (avoid-say-instead) and feed/ask/output cards (feed-ask-output-cards). Use these instead of reaching for a paid single-purpose tool (or hand-rolling from scratch) when a design/frontend task needs a device mockup, a stylized image effect, a moodboard layout, a brand-kit deliverable, a SaaS pricing section, a quiet typography-led hero, a "N things you should know" carousel/infographic layout, a reusable reference dashboard, or any of the social-carousel/card layouts above. Each template is copy-paste-ready with clear swap points marked in comments.
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
- **A GTM diagnostic heatmap** (Union Square style - dark navy, pink sub-headline, rows = GTM areas, columns = maturity levels, G/Y/R cells with computed dashed danger zones) → `templates/gtm-heatmap-navy.html`
- **An agent-roster infographic** ("N best agents to run your X" - numbered coloured department cards with agent chips and a CTA bar; themes `claude` and `navy`) → `templates/agent-roster-grid.html`
- **A staged roadmap** ("first 100 customers" - rising black/green/yellow/purple blocks over one column per stage with goal, lead generation, channels, build, working-when) → `templates/stage-roadmap-steps.html`
- **A radial tool wheel** (12 wedges x 5 tools, outer category ring, text only) → `templates/tool-wheel-radial.html`
- **A repo-of-the-day carousel slide** in four looks selected with `?theme=grid-light|pixel-dark|blueprint|cyber-red` (rank, name, what it really does, real stats) → `templates/repo-card-slide.html`
- **A "things not to say" list** (avoid / reason / say instead rows, meaning carried by symbols as well as colour) → `templates/avoid-say-instead.html`
- **Feed / ask / output cards** (six numbered cards + input pack + rules; SalesDaily "AI Sales Prep" look) → `templates/feed-ask-output-cards.html`
- **A Venn diagram** (two translucent circles, lilac and amber, with a collaboration panel in the overlap; ruled-paper background) → `templates/venn-two-circles.html`
- **An AI-playbook slide** (beige paper, serif headline, four-box input/AI/output/check chain, black copy-this-prompt block, numbered checks; accents indigo or pink via `data-accent`, dark via `data-mode`) → `templates/playbook-workflow-beige.html`
- **A grid of prompt cards in Greek or English** (@ai_with_dr.t style: grey paper, italic serif title, white cards with a mock chat input) → `templates/prompt-chat-cards-grey.html`
- **A numbered tool list** (big red numbers, initials tile, bold red name, divider, job) → `templates/tool-list-red-numbers.html`
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
| `gtm-heatmap-navy.html` | Union Square "GTM Ops Diagnostic Framework" | `ROWS` of `[area, 'GGYR']`; danger zone = Optimization/Amplification scored G/Y on a red or yellow Fundamentals/Adoption; letters inside cells so colour is never the only signal; theme `gtm-navy` |
| `agent-roster-grid.html` | "100 Best Claude Agents" / "200 Claude Agents To Run Your Entire GTM" | `DEPTS` strings `Dept|agent|agent...`; auto-fit grid; `data-theme` `claude` (warm white + orange) or `navy` (dark + blue/mint CTA) |
| `stage-roadmap-steps.html` | "How to Unlock GTM" (OneGTM Lab) | `STAGES` array drives both the staircase and the columns; channels rendered as text chips; theme `stairs-pastel` |
| `tool-wheel-radial.html` | "60 AI Marketing + Sales Tools" | SVG built with `createElementNS`; right-half labels run outward, left-half labels are flipped so they read upright; theme `wheel-navy-orange` |
| `repo-card-slide.html` | @joshualevi.ai, @replace.so, @aiclawbots, @martiendejong_dev carousels | 4:5 slide in container-query units (`cqw`) so it scales; four themes; mascot slot is a dashed placeholder, not a reproduction |
| `avoid-say-instead.html` | Dr. Christian Poensgen "10 Things NOT to Say in a Job Interview" | `ROWS` of `[avoid, reason, say]`; symbols X ? tick; theme `teal-paper` |
| `feed-ask-output-cards.html` | SalesDaily.co "AI Sales Prep" | `STEPS` of `[title, feed, ask, output]` + `PACK` and `RULES`; theme `salesdaily-cards` |
| `venn-two-circles.html` | "Where AI And Sales Meet" | Circles are CSS, overlap panel absolutely centred; stacks to one column under 760 px; theme `venn-lilac-amber` |
| `playbook-workflow-beige.html` | @earchoe AI playbook slides | Everything from constants; `data-accent` and `data-mode` switch palette; serif and mono fall back to Georgia and ui-monospace; theme `playbook-beige` |
| `prompt-chat-cards-grey.html` | @ai_with_dr.t prompt carousels | `PROMPTS` strings split on blank lines; mock input drawn with text glyphs, no icons; no Greek word in capitals; theme `drt-grey` |
| `tool-list-red-numbers.html` | @ai_slacker "50 AI tools" | `TOOLS` rows with initials tiles (logos are not reproduced); collapses to two columns under 520 px; theme `tools-red` |
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

## Batch 104 theme tokens (colours read from the screenshots)

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `gtm-navy` | navy `#0A1130`, panel `#101A44`, pink-red `#FF2D75`, green `#2F9E5B`, amber `#E8B92F`, red `#D6405A` | Inter or Aptos (bold uppercase title) |
| `claude-agent-roster` | white `#FFFFFF`, ink `#16181D`, Claude orange `#E8602C`, department colours blue `#2F6FDB` green `#2F9E5B` purple `#7A3FD1` red `#D6405A` amber `#E6951C` teal `#0F8F9F` | Inter |
| `linkedin-navy-roster` | navy `#0B1533`, card `#0F1D45`, line `#2A4287`, orange `#FF8A3D`, CTA gradient mint `#5FE0C4` to sky `#7AD0FF` | Inter |
| `stairs-pastel` | black `#111`, mint `#A8EF9A`, butter `#FFD873`, purple `#5B2F9E`, highlight `#D8FFD0` | Inter |
| `wheel-navy-orange` | field `#07123D` to `#173A9C`, wedge orange `#FF8A1F`, navy `#16276B`, pale `#E9EDF8`, ring `#0F1C55` | Inter |
| `repo-grid-light` | paper `#EFEFE9`, ink `#141414`, orange `#D9582B` (3D asterisk motif) | Archivo Black + Inter |
| `repo-pixel-dark` | near-black `#101011`, green pixels `#1E3A24`, accent `#7EE08F` | Inter |
| `repo-blueprint` | blueprint blue `#0B4A7D`, grid `#FFFFFF22`, label white, accent `#3B82F6` | Inter ExtraBold |
| `repo-cyber-red` | black `#0A0606`, neon red `#FF2B2B`, panel `#150B0B` | Anton + Inter |
| `teal-paper` | paper `#E9E9E6`, ink `#14323D`, teal `#8EC5BD`, cross `#C0262D`, query `#E39A1B`, tick `#1F8A3E` | Inter |
| `salesdaily-cards` | paper `#F1F1EE`, card `#FFFFFF`, teal `#1B8A94`, navy `#10243A` | Inter |

All seven Batch 104 templates were rendered in headless Chromium at 1100 px and 390 px in light and dark (no script errors, no horizontal overflow). The mascot art, brand logos and tool logos in the sources are deliberately not reproduced.

## Batch 105 theme tokens (colours read from the screenshots)

| Theme | Colours | Fonts (look-alike, free) |
|---|---|---|
| `venn-lilac-amber` | paper `#F4F3EF`, rule `#E4E2DC`, lilac `#CDBCF6`, amber `#F2C36B`, overlap `#CF9F9D`, label blue `#3B4FD1` | Inter ExtraBold |
| `playbook-beige` | beige `#DDD6C1`, panel `#CFC7AE`, code `#14120E`, ink `#16140F`, indigo `#4B3FD6` or pink `#D63A7A`, dark page `#14120E` | Playfair Display Black + JetBrains Mono |
| `drt-grey` | paper `#ECEBE8`, card `#F7F7F6`, ink `#1D1D20`, send button `#8E8E93`, accent `#6B8FD6` | Georgia italic bold (Greek-capable) |
| `tools-red` | white `#FFFFFF`, red `#D6261B`, ink `#17171A`, divider `#1A1A1A` | Inter Black |

All four Batch 105 templates were rendered in headless Chromium at 1100 px and 390 px (the Venn in light and dark) with no script errors and no horizontal overflow. Tool logos and brand marks are not reproduced.
