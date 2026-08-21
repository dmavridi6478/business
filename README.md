# business
Collect Claude material for buiness

## Skills

A starter bundle of business-oriented Claude skills lives in `.claude/skills/`:

- `sales-enablement` — pitch decks, one-pagers, objection handling, MEDDPICC/MEDDIC/BANT
- `business-decision-frameworks` — MoSCoW, RICE, OKRs, Kano, roadmap formats, Minto Pyramid
- `quarterly-okr-architect` — quarterly/annual goal architectures (4DX, MASTER, DUMB, backward planning)
- `business-intelligence-report` — reports for managers/CEO on results, trends, predictive analysis
- `ceo-reporting-skill` — growth/business reports for the CEO (Greek healthcare context)
- `product-marketing-context` — product/audience/positioning context doc used by other marketing skills
- `competitor-profiling` — structured competitor research and profiles
- `content-strategy` — content planning, topic clusters, editorial calendars
- `internal-comms` — company newsletters, FAQs, general internal communications
- `doc-coauthoring` — structured workflow for co-authoring docs, proposals, and specs
- `attachment-intake` — how to handle uploaded files (zips, photo batches, docs) that arrive with no or mismatched instructions, instead of guessing at intent
- `design-dev-resources` — curated directory of free design/frontend tool sites (unDraw, SVGL, Aceternity, Glassmorphism generator, JSON Crack, Mobbin) plus notable external AI tools (Genspark, Google Stitch, Google Flow, Gumloop, Figma Make, Kombai) and a design-engineering job board (Design Engineer Jobs) worth knowing about
- `ai-search-marketing-2026` — the SEO/SXO/AEO/GEO/AIO five-discipline wheel, a modern-marketing taxonomy, 5 exec-level marketing-analytics questions, a 15-day day-by-day AI-search action plan, and a 20-source AI-visibility ecosystem map cross-checked against which sources this account can actually query via a live MCP connector
- `growth-operating-framework` — a 7-step sequence for capital-efficient growth (real-business alignment → North Star metric → data foundation → feedback loop → cross-functional accountability → capital-efficient scale → fast iteration)
- `linkedin-virality-playbook` — 9 tactics for LinkedIn posts that reach beyond the author's own network (proof-led hooks, repostable angles, reusable visual templates, real engagement questions)

A design/output bundle sits alongside it, for turning business content into actual visual deliverables:

- `frontend-design` — distinctive, production-grade web components/pages/artifacts
- `web-artifacts-builder` — complex multi-component HTML artifacts (React/Tailwind/shadcn)
- `canvas-design` — static poster/art pieces (.png/.pdf), ships with real fonts
- `theme-factory` — 10 preset visual themes (colors/fonts) applicable to any artifact
- `premium-html-presentation` — cinematic, dark-mode HTML slide decks
- `the-design-system-prompt` — an alternative cinematic-HTML-deck prompt (secondary to `premium-html-presentation`)
- `campaign-page-one-shot` — one-shot marketing landing pages
- `brand-guidelines` — **Anthropic's own** brand colors/fonts specifically, not a generic client-branding tool (see caveat in the skill itself)
- `pptx` / `docx` / `xlsx` / `pdf` — editable PowerPoint, Word, Excel, and PDF file creation/editing
- `design-templates` — 6 ready-to-use, verified-rendering HTML/CSS templates (iMessage mockup, social device frame, 3D product tilt, halftone/dither effect, moodboard grid, brand board) to drop into a build instead of writing from scratch
- `ui-motion-design` — tasteful UI motion: easing curves, spring physics, timing, and micro-interaction patterns
- `design-review-audit` — audits a finished build against a spacing/hierarchy/contrast/consistency/AI-slop checklist; companion to `/design-review`
- `brandkit-generator` — turns a one-line idea into 2-3 brand directions (wordmark, palette, type pairing, brand board), fast and explicitly non-final
- `design-token-extractor` — extracts a reusable color/type/spacing token set from a reference site or screenshot
- `image-to-code` — clones a reference screenshot into real code, then renders and compares before calling it done

A third bundle covers **setting up a new business** — validating an idea and turning someone's own expertise into a sellable product/service before (or instead of) building a team-scale product:

- `product-strategy-session` — full positioning → discovery → roadmap process for validated direction before committing to execution
- `saas-idea-validator` — critical, non-cheerleading stress-test of a new product/software/service idea (problem-solution fit, market, competition, moat, specific failure mode)
- `the-specific-knowledge-excavator` — reverse-engineers a person's unique intersection of expertise nobody else holds in the same combination
- `the-productize-yourself-blueprint` — converts that expertise into a scalable product/service format that sells without the founder's live presence
- `the-leverage-stack-auditor` — diagnoses whether a business idea is actually leveraged (media/code) or just relabeled labor
- `content-repurposing-service` — a concrete worked example: a productized weekly service that turns one client recording into a 7-asset content pack (carousel, video outlines, email, text posts) on a Mon–Fri cadence
- `lean-software-stack` — curated directory of 8 free/open-source desktop apps (AppFlowy, Joplin, KeePassXC, OBS Studio, Kdenlive, Element, PDFsam Basic, LocalSend) that replace common paid SaaS tools, for controlling software costs before revenue validates the spend; companion to `/tool-stack-check`

A fourth pair covers **personal AI infrastructure** — setting up Claude Code itself as a tool, rather than producing business deliverables:

- `advisory-board` — set up a personal "council of experts" (named advisors + their real source material) that the `/ask-the-board` command draws on
- `ai-discoverable-site` — make a personal/company site readable by AI assistants (semantic HTML, meta descriptions, `llms.txt`, `robots.txt`, an "Ask AI about me" cross-provider block)
- `humanizer` — strips AI-writing tells (inflated symbolism, promotional language, em dash overuse, filler phrases, etc.) from drafted text; vendored for real from [blader/humanizer](https://github.com/blader/humanizer) (MIT)
- `claude-code-tooling` — curated directory of external Claude Code tools (a design-engine desktop app, a senior-engineer skill pack, multi-agent orchestration, a skills package manager, an agent context/memory database, five browser-automation frameworks, a hive-mind team workspace) that are standalone software, not skill files, so they're documented here rather than vendored in
- `web-task-scoping` — governance procedure for scoping any browser-automation task (Target → Limit → Run → Review) before granting a web agent more autonomy; companion to `/scope-web-task`
- `night-shift-workflow` — design and govern a scheduled/unattended Claude workflow (a recurring brief, digest, or Routine) that gathers, triages, and drafts while the user is away, with an explicit Claude-may/human-approval boundary; companion to the `night-shift-canvas` procedure

A fifth bundle was reviewed and vendored from a "Claude tools worth installing"
social-media roundup (GitHub repos / plugins / skills / MCP servers). Each is a
real external project, vendored for real (SKILL.md + LICENSE + a `SOURCE.md`
recording exact repo/commit), the same way `humanizer` above was:

- `caveman` — ultra-compressed "talk like a caveman" response mode, ~65% fewer output tokens with no accuracy loss; vendored from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (MIT). Only the flagship `caveman` skill is vendored — the source repo also ships a CLI, agent runtime, and ~20 related sub-skills (`caveman-commit`, `caveman-review`, etc.)
- `claude-ads` — paid-media audit/optimization orchestrator (250+ checks across Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, X); vendored from [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) (MIT). Full platform sub-skills and bundled Python tooling require the real plugin/repo install (see `SOURCE.md`)
- `claude-seo` — universal SEO analysis orchestrator (technical SEO, schema, E-E-A-T, GEO/AEO for AI Overviews/ChatGPT/Perplexity); vendored from [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT). Same caveat: the 24 sub-skills/18 sub-agents need the full install
- `ai-second-brain` — walks through building a living, searchable wiki from ChatGPT + Claude export history (Karpathy-wiki pattern); vendored from [charlie947/ai-second-brain](https://github.com/charlie947/ai-second-brain) (MIT). **Best-guess match** — several similarly-named repos exist, this one matched the source description most closely but wasn't independently confirmed
- `hook-writer`, `caption-writer`, `carousel-writer` — write the opening hook, the caption/post copy, and swipeable carousel slides respectively, all voice-matched to a `brand-profile`; a curated 3-skill subset of the 106-skill [social-media-skills/skills](https://github.com/social-media-skills/skills) library (MIT). Install the rest with `npx skills add social-media-skills/skills -g -a claude-code -s '*' -y`
- `gstack` — router skill for Garry Tan's 23+-skill "virtual engineering team" setup (CEO/Designer/Eng Manager/Release Manager/Doc Engineer/QA agents); vendored from [garrytan/gstack](https://github.com/garrytan/gstack) (MIT). Only the top-level router is vendored — the real installer needs the `bun` runtime and symlinks into multiple AI-tool configs, so it wasn't run automatically (see `SOURCE.md` for the exact command)

A second roundup ("24 Things to Install in Claude") added four more real,
verified vendors:

- `hyperframes` — "write HTML, render video" agent-native video framework (compositions are plain HTML, no React/proprietary DSL); vendored from [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) (MIT). Only the mandatory entry-point skill is vendored — the full repo ships 19 skills plus the CLI/renderer itself
- `notebooklm-skill` — drives Google NotebookLM (source-grounded Q&A, research-to-content workflows, generated audio/video/slides/study material) from Claude; vendored from [claude-world/notebooklm-skill](https://github.com/claude-world/notebooklm-skill) (MIT). **Best-guess match** — at least 4 similarly-named repos exist; needs its bundled MCP server (not vendored) for full functionality
- `vite`, `vue` — Vite 8/Rolldown build-tool and Vue 3 Composition API reference skills, auto-generated from source docs; **best-guess match** for the infographic's generic "skills" entry ("Vue and Vite core team skills collection") — vendored from [antfu/skills](https://github.com/antfu/skills) (MIT, Anthony Fu's curated collection, 19 skills total — only these 2 are vendored here)

A sixth bundle is original content, not vendored — authored for this repo
after reviewing a "Claude Code outreach project" social post that showed a
26-file skill-tree mockup with no actual source repo to clone. Consolidated
into 8 category skills (rather than 26 thin ones) covering a full
cold-outbound-sales system, orchestrated by `/outreach-campaign`:

- `outreach-strategy` — trigger-based ICP (not static firmographics), per-role persona cards, a signal→pain map, and outcome-framed offer statements
- `outreach-list-building` — company sourcing (Apollo/Clay/lemlist-style filters), people sourcing (Sales Navigator), intent-signal sourcing (G2/Product Hunt), dedup + CSV assembly
- `outreach-copywriting` — signal-led first-touch (<100 words), follow-up + breakup sequence, a VP-toned variant, a strict quality checklist, and a benchmarking pass
- `outreach-channels` — LinkedIn (2-DM max rule), a 6-part cold-call script, and AI-personalized video outreach (Tavus/HeyGen-style)
- `outreach-campaign-design` — 3+ messaging angles per ICP, full multi-touch/multi-channel campaign architecture, and a deliberate GTM stress test before launch
- `outreach-replies-pipeline` — reply triage across 8 reply types, benchmarking against outbound performance data, and stage-by-stage pipeline diagnosis
- `outreach-automation` — n8n workflow building/debugging and supplementary website scraping for enrichment
- `outreach-data-connections` — maps which of the tools above are actually connected in a given environment before the rest of the bundle assumes they are; pairs with the `mcp-integration-scout` agent

A seventh addition, `claude-cheat-sheet`, is also original content rather
than vendored: a social-media "Claude AI Cheat Sheet" infographic turned out
to be unreliable on review (wrong model names, garbled/nonsensical text
throughout, a non-Anthropic URL presented as an official courses link, and
mangled tool names in its tools table) — rather than install any of that,
this is a from-scratch, accurate reference on the parts that were
legitimately generic and worth having: prompting techniques (shot count,
prompt shapes, the role+examples+step-by-step combo) and what Skills, Hooks,
MCP, Projects, and Artifacts actually are and how they differ.

An eighth addition, `ai-project-management`, is the same correction pattern
again: a social "AI-Powered Project Management with Claude" infographic
turned out to be unreliable on inspection (duplicate/conflicting section
numbers, fabricated-looking repeated metrics, garbled labels in every
panel, a tools table with unresolvable names). Rewritten from scratch as
real PM methodology — WBS/critical path/EVM (CPI/SPI/EAC)/RACI/RAG
reporting — with Claude's actual role at each step called out, plus only
the AI-PM tool claims that were independently verifiable.

A ninth addition, `agent-platform-governance`, is the same pattern once
more but with a lighter touch: a "5 Key Learnings from Claude & Copilot
Studio Testing" infographic had a garbled intro paragraph and one unverified
specific claim (dropped rather than repeated), but its core framework —
governance dimensions (monitoring, integration, team sharing, identity,
audit trails, compliance) and full build/govern/monitor/share/maintain
lifecycle thinking — checked out as real and useful, so that part is kept
(rewritten cleanly, with a verified check against Microsoft's own Copilot
Studio governance docs).

Drop this repo into a Claude Code project (or point `.claude/skills` at it) to make these available.

## Plugins

Claude Code **plugins** (bundles of skills + agents + commands + MCP
connectors, installed via `/plugin` rather than copied as files) reviewed from
the same roundup. Plugin state lives in the Claude Code installation, not in
this git repo, so what's tracked here is the marketplace + install commands
needed to reproduce the setup on any machine:

| Item (source) | What it is | Reproduce with |
|---|---|---|
| [`marketingskills`](https://github.com/coreyhaines31/marketingskills) | CRO, copywriting, SEO, analytics, growth-engineering skills for marketers | `claude plugin marketplace add coreyhaines31/marketingskills`<br>`claude plugin install marketing-skills@marketingskills` |
| [`claude-for-legal`](https://github.com/anthropics/claude-for-legal) | Anthropic's official 12-plugin legal suite (commercial, privacy, product, corporate, employment, regulatory, AI-governance, litigation, IP, law-student, legal-clinic, CoCounsel) + ~20 MCP connectors (Ironclad, DocuSign, Box, CourtListener, etc. — each needs its own auth) | `claude plugin marketplace add anthropics/claude-for-legal`<br>`claude plugin install <plugin-name>@claude-for-legal` (see repo for all 12 names) |
| `claude-skills` (**best-guess match, uncertain**) | Generic "many skills across platforms" — no repo matched "263+ skills" exactly; closest candidate installed was [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (5.2k★, 88 bundled plugins) | `claude plugin marketplace add alirezarezvani/claude-skills`<br>`claude plugin install marketing-skills@claude-code-skills` (one of 88 — browse the rest with `/plugin` in an interactive session) |
| [`financial-services`](https://github.com/anthropics/financial-services) | Anthropic's official banking/PE/equity-research suite | `claude plugin marketplace add anthropics/financial-services`<br>`claude plugin install <financial-analysis\|investment-banking\|equity-research\|private-equity\|wealth-management>@claude-for-financial-services` |
| [`superpowers`](https://github.com/obra/superpowers) | Jesse Vincent's (obra) TDD/debugging/brainstorming dev methodology, 20+ composable skills | `claude plugin marketplace add obra/superpowers-marketplace`<br>`claude plugin install superpowers@superpowers-marketplace` |
| [`gstack`](https://github.com/garrytan/gstack) | See the vendored `gstack` skill above — not distributed as a plugin marketplace, needs its own installer | `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` (requires `bun`) |
| [`repomix`](https://github.com/yamadashy/repomix) | Standalone CLI — packs a repo into one LLM-friendly file; not a skill/plugin | `npm install -g repomix` |
| [`codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) | **Verified official** — OpenAI's own plugin to use Codex from inside Claude Code (`/codex:review`, `/codex:rescue`, `/codex:transfer`); needs a ChatGPT subscription or OpenAI API key | `claude plugin marketplace add openai/codex-plugin-cc`<br>`claude plugin install codex@openai-codex` |

The marketingskills, claude-for-legal, claude-skills, financial-services,
superpowers, and openai-codex marketplaces are registered and the plugins
above installed (user scope) in this environment; `repomix` and
`agent-browser` (below) are installed globally via npm. None of this
persists outside this Claude Code installation — rerun the commands above
on any machine that should have the same setup.

## MCP Servers & external tools

Reviewed from the roundups above, plus a personal "daily tool stack" post
(Codex, Claude, Linear, Obsidian, The Pulp — mostly standalone apps rather
than installable connectors, noted below for completeness). Status reflects
**this account/session** — your own account's connector state may differ.

| Item | Status here | Notes |
|---|---|---|
| Slack | ✅ already connected (claude.ai connector) | — |
| Notion | ✅ already connected (claude.ai connector) | — |
| Google Drive | ✅ already connected (claude.ai connector) | — |
| Zapier | ✅ already connected (claude.ai connector) | Bridges to 9,000+ apps' actions, including Instagram — may cover the `instagram-mcp` use case without a dedicated server |
| Perplexity | ❌ not connected | Needs auth via claude.ai connector settings (can't be done from a non-interactive session) |
| `instagram-mcp` (**best-guess match, uncertain**) | ❌ not installed | No single canonical repo; closest name match is [mcpware/instagram-mcp](https://github.com/mcpware/instagram-mcp) (Graph API, 23 tools). Needs an Instagram Graph API token to connect — add with `claude mcp add instagram-mcp -- npx @mcpware/instagram-mcp` once you have credentials |
| `agent-browser` | ✅ installed as a CLI | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — despite the "MCP Servers" slide, Vercel built this as a token-efficient browser-automation **CLI**, not an MCP server. Installed globally: `npm install -g agent-browser && agent-browser install` |
| `granola` (**best-guess, uncertain**) | ❌ not installed | Reads local [Granola](https://granola.ai) meeting notes/transcripts. No official/canonical MCP server found — a dozen community repos share the name (e.g. [chrisguillory/granola-mcp](https://github.com/chrisguillory/granola-mcp), [bhandzo/pantry](https://github.com/bhandzo/granola-mcp)). Requires the Granola desktop app running locally, so nothing to verify from this session — pick one and `claude mcp add` it once you have Granola installed |
| [`kondo`](https://www.trykondo.com/) | ❌ not connected | **Correction: real, but not open-source** — not a GitHub repo (the earlier "could not verify" note was from only searching GitHub). Kondo is a commercial LinkedIn inbox-management Chrome extension ("Superhuman for LinkedIn DMs" — labels, snooze, keyboard triage) that ships a hosted MCP connector on its **Business plan** ($36/user/month), set up at [docs.trykondo.com/mcp-setup](https://docs.trykondo.com/mcp-setup); it requires the Kondo browser extension actively running and reads your live LinkedIn inbox locally in-browser (per their docs, it doesn't store LinkedIn data server-side). Needs a paid account + the extension — can't be connected from this session |
| `higgsfield` | ❌ not installed | Cinematic AI image/video generation. [Official docs](https://higgsfield.ai/mcp) exist but no official GitHub org repo was found; several community MCP servers do ([Hikhakk/higgsfield-mcp-unified](https://github.com/Hikhakk/higgsfield-mcp-unified) — 27 models — looked most complete). Needs a Higgsfield API key/account either way |
| [Linear](https://linear.app) | ✅ **registered** (auth pending) | Official remote MCP server, `https://mcp.linear.app/mcp` — registered in this project with `claude mcp add --transport http linear-server https://mcp.linear.app/mcp`. First real use opens a browser OAuth prompt this non-interactive session can't complete; a project-management-workflow one, separate from `claude-for-legal`'s own Linear connector (which is scoped to `product-legal` only) |
| Obsidian | 📋 documented, not installed | Local note-taking app — no cloud API, so nothing to connect from this session. [coddingtonbear/obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) is the community plugin (install from inside Obsidian → Settings → Community plugins) that now ships a built-in MCP endpoint at `/mcp/`; enable it, then `claude mcp add --transport http obsidian http://localhost:27124/mcp` (port/token from the plugin's settings) |
| Codex | ✅ already covered | Not an MCP server — OpenAI's own coding agent/CLI. The actual Claude-Code-relevant integration is the `codex-plugin-cc` plugin documented above, already installed |
| "Claude Design" | N/A | Not a separate tool — this is Claude itself (Anthropic's own branding), used as a general writing/brainstorming assistant. Nothing to install |
| "The Pulp" | ❓ unverified | Described as a personalized daily-briefing/podcast app. Could not confirm a matching product by that name (an unrelated media-industry podcast shares the name; closest real equivalents are apps like Huxe or Spotify's Personal Podcasts). Even if real, it reads as a closed consumer app with no public API/MCP/skill surface — nothing to clone or install either way |

## Commands

Slash commands live in `.claude/commands/` — unlike skills (which Claude loads
automatically when relevant), commands are invoked explicitly by name:

- `/ask-the-board [question]` — answers a question using the advisory board set up by the `advisory-board` skill; refuses to improvise generic advisor impressions if no board has been configured yet
- `/improve-system` — reviews the current session for one genuine, durable behavioral signal (not a transcript summary) and persists it to a `memory/` file, updating the memory index
- `/design-review [file or description]` — runs the `design-review-audit` checklist against a build and reports a prioritized punch list
- `/outreach-campaign [product/offer and target market]` — runs the `outreach-*` skill bundle end to end (strategy → list-building → copywriting → campaign design) into a single `outreach-brief.md`; stops to ask if the ICP is still vague, or if the GTM stress test finds a serious flaw, rather than shipping a brief built on a plan already known to be broken
- `/content-pipeline [niche/topic]` — runs the 7-agent content team (research → hook → script → design → schedule) in sequence, then always stops for explicit approval before `content-publisher` touches a live platform
- `/scope-web-task [task]` — applies the `web-task-scoping` skill's Target/Limit/Run/Review discipline to a browser-automation task before it runs; refuses to proceed on side-effecting tasks (submit/purchase/post/delete) until all four are explicit
- `/tool-stack-check [current tools]` — checks a described software stack against `lean-software-stack`'s free alternatives and applies the `free-vs-paid-tool-decision` procedure to recommend switch/keep-paid per tool
- `/how-to [task]` — turns a vague "how do I X" into a concrete, numbered step-by-step plan; asks clarifying questions first if the task or starting point is unclear, and add "ELI5" to the arguments for a beginner-level walkthrough
- `/about-me` — loads standing personal/working context from `docs/about-me.md` (role, current priorities, working style, what "good" looks like) for this conversation only; offers to create the file on first use rather than inventing placeholder content
- `/research-synthesis [sources]` — runs the `research-synthesis` procedure's 6 stages (Knowledge Map → Literature Review → Gap Finder → Contradiction Detector → Methodology Auditor → Executive Brief) against a pasted or referenced source set in one pass; distinct from `agentic-researcher`, which finds sources rather than synthesizing ones already in hand
- `/canva-video-plan [content need]` — recommends which of Canva's 5 built-in AI video formats to use (per `canva-ai-video.md`) for a stated platform/goal/footage situation, with the concrete steps and export spec; defers to the `video` skill's heavier stack when the need calls for a custom avatar, programmatic batch rendering, or a dedicated AI-generation model

**Skill vs. command, in this repo:** a skill is background knowledge/procedure
Claude reaches for when relevant ("how do I structure a quarterly OKR cascade");
a command is something the user explicitly invokes by typing `/name` ("run my
board" / "reflect on this session now"). `advisory-board` (skill) documents
*how to set up* the board; `/ask-the-board` (command) is *how you use it* once
set up.

### How the skills connect

Each `SKILL.md` has a "Related skills in this repo" (or annotated "Related
Skills") section pointing at the others that feed it or consume its output:

- `product-marketing-context` is the foundational doc: `sales-enablement`,
  `competitor-profiling`, `content-strategy`, and the design skills (for the
  user's *actual* brand, not `brand-guidelines`) all pull from it.
- `business-decision-frameworks` prioritizes initiatives/topics that feed
  `quarterly-okr-architect` (goal cascades) and `content-strategy` (editorial
  calendars).
- `quarterly-okr-architect` sets the targets that `business-intelligence-report`
  and `ceo-reporting-skill` report progress against.
- `business-intelligence-report` and `ceo-reporting-skill` are a pair —
  the former is the general BU-manager version, the latter is specialized for
  a Greek MedTech CEO audience.
- `content-strategy` decides what to write; `doc-coauthoring` (long-form) and
  `internal-comms` (short-form) draft it; `docx`/`pdf` produce the final file.
- `competitor-profiling` feeds both `sales-enablement` (battle cards) and
  `content-strategy` (competitive content gaps).
- Any of the reporting/planning skills can hand off to `pptx`, `premium-html-presentation`,
  or `xlsx` to become an actual deck or workbook, then `pdf` to export it.
- `design-dev-resources` supplies real icons/illustrations/logos to
  `frontend-design`, `web-artifacts-builder`, `canvas-design`, and
  `campaign-page-one-shot` instead of hand-drawn SVG.
- `design-templates` provides ready-made device-mockup/3D-tilt/halftone/moodboard
  snippets to the same design skills, approximating what `design-dev-resources`'
  niche tools (Javii, Ultramock, Ditther, Logo System) produce.
- `ui-motion-design` and `design-review-audit` (`/design-review`) bookend a
  build: motion guidance going in, a checklist audit coming out.
- `brandkit-generator` turns a one-liner into a brand direction, assembled via
  `design-templates`' `brand-board.html`; `design-token-extractor` turns any
  reference (that or an external site) into reusable tokens; `image-to-code`
  clones a reference screenshot into real code using those tokens.
- For a brand-new business: `the-specific-knowledge-excavator` finds the
  expertise → `the-productize-yourself-blueprint` turns it into a product/service
  format → `saas-idea-validator` / `product-strategy-session` stress-test it →
  `the-leverage-stack-auditor` checks it's actually leveraged →
  `product-marketing-context` captures the validated positioning → the rest of
  the business/design/output skills take over from there.
  `content-repurposing-service` is a ready-made example of running that whole
  chain and landing on a productized content service. `lean-software-stack`
  keeps founder overhead near zero during this phase, checked against the
  `free-vs-paid-tool-decision` procedure via `/tool-stack-check`.

- For personal AI setup: `advisory-board` supplies advisors that
  `product-strategy-session`, `quarterly-okr-architect`, and the new-business
  cluster can sanity-check decisions against via `/ask-the-board`.
  `ai-discoverable-site` pulls its "who they are" content from
  `product-marketing-context` and hands implementation to `frontend-design`.

- `humanizer` is a general-purpose editing pass — run it on drafts from
  `sales-enablement`, `content-strategy`, `doc-coauthoring`, `internal-comms`,
  or `content-repurposing-service` before delivering them.

- `growth-operating-framework` decides *what* to grow and by which metric;
  `quarterly-okr-architect` turns that into a goal cascade; `business-decision-frameworks`
  prioritizes which channels/experiments to run; `ai-search-marketing-2026`'s
  exec questions and `business-intelligence-report`/`ceo-reporting-skill` report
  on how it's going. `linkedin-virality-playbook` and `ai-search-marketing-2026`
  both extend `content-strategy` with channel-specific reach tactics (LinkedIn
  posts; AI-search visibility) once the underlying topic is decided.

- `web-task-scoping` governs *how* to run any of `claude-code-tooling`'s five
  browser-automation frameworks (Playwright MCP, Stagehand, Skyvern,
  Magentic-UI, Steel Browser) against a real site — apply its Target/Limit/Run/Review
  rule via `/scope-web-task` before granting a web agent autonomy on a
  side-effecting task.

- `night-shift-workflow` applies the same match-oversight-to-stakes discipline
  as `web-task-scoping` to scheduled/unattended workflows instead of browser
  tasks — use the `night-shift-canvas` procedure to define a workflow's
  output/trigger/sources/rules/actions/approval boundary before scheduling
  it as a Routine. `business-intelligence-report`/`ceo-reporting-skill` supply
  the reporting structure if the scheduled brief is business-facing rather
  than personal.

`attachment-intake`, `claude-code-tooling`, `web-task-scoping`, and
`night-shift-workflow` are separate, meta-level skills and aren't part of
the business/design content chain above.

### ⚠️ `brand-guidelines` applies Anthropic's brand, not the user's

That skill is hardcoded to Anthropic's own colors (`#d97757` orange, etc.) and
fonts (Poppins/Lora) — it's for artifacts that should carry *Anthropic's*
look-and-feel specifically. For the user's own company or client branding, use
`product-marketing-context` to capture their real brand and apply it manually
in the design skills instead.

## Agents

Subagents live in `.claude/agents/` — unlike skills (loaded automatically
into the main conversation) and commands (invoked by typing `/name`), an
agent runs as a separate subagent via the Agent tool, with its own bounded
context and tool access. These six were built from an "AI Agents: 6 must
know terms" glossary card (MCP, Agent Loops, Skills, Single vs Multi-Agent
Architecture, Agentic RAG, Agent Memory) — each turns one of those concepts
into something that actually runs, scoped to this repo's conventions:

- `mcp-integration-scout` — checks which MCP connectors are already
  available/connectable before a task reaches for a hand-rolled API
  integration or scraper
- `task-loop-runner` — runs a bounded act → evaluate → retry loop on a
  single task with a checkable success condition (refine a draft against a
  checklist, reconcile numbers until they tie out), instead of grinding
  silently or looping forever
- `capability-scout` — matches a task against this repo's own ~50 skills
  and installed plugins before anyone improvises a solution from scratch
- `multi-agent-orchestrator` — splits a complex/high-stakes task across
  specialized passes (retrieve → validate → write) instead of one pass
  doing everything, when the reliability gain is worth the overhead
- `agentic-researcher` — for market/competitor research: routes each claim
  to the right source, validates it actually confirms the claim, and
  decides whether to re-retrieve rather than trusting the first hit
- `memory-keeper` — audits and reconciles the `memory/*.md` store that
  `/improve-system` writes to (orphaned files, near-duplicates,
  contradictions), rather than deciding what's worth saving in the first
  place

A second set of seven — a coherent, working content-team pipeline this
time, not concept demos — came from a "Claude Code AI Company OS: I built
an AI content team, 7 AI employees" post. Each floor of that mockup became
one subagent, wired to this repo's existing content skills rather than
duplicating them, run in sequence by `/content-pipeline`:

- `content-researcher` — finds trends, studies competitors, surfaces ranked content opportunities with evidence
- `content-hook-writer` — applies the `hook-writer` skill to a researched opportunity, producing several distinct ranked angles
- `content-script-writer` — builds the full script/caption around the chosen hook, routing to `caption-writer`/`carousel-writer` per format
- `content-designer` — specifies (and routes to `frontend-design`/`canvas-design`/`design-templates` to produce) the visuals a finished script needs
- `content-analyst` — reads real performance data (retention, saves, CTR — never fabricated) and feeds conclusions back to the researcher/hook-writer stages
- `content-manager` — sequences finished pieces into the content calendar and tracks pipeline state; never publishes
- `content-publisher` — the only stage that touches a live account; **requires an explicit human go-ahead for the specific piece every time**, never auto-chained from a calendar slot

The publisher's confirmation gate is deliberate, not an oversight — see
"Executing actions with care" in this project's standing instructions:
scheduling a slot is a plan, posting to a real audience is a side-effecting
action that needs its own explicit approval regardless of what came before it.

## Procedures

Standard operating procedures live in `docs/procedures/`:

- `attachment-intake.md` — inspect an unlabeled/ambiguous attachment before
  acting, ask a grounded clarifying question, and don't force-fit mismatched
  answers onto the file. Backs the `attachment-intake` skill above.
- `free-vs-paid-tool-decision.md` — team size, sync/collaboration needs,
  portability-vs-support trade-off, and security/compliance handling to weigh
  before swapping a paid SaaS tool for a free/open-source one from
  `lean-software-stack`; revisit at each business-stage change, not just once.
- `night-shift-canvas.md` — the six design decisions (Output, Trigger,
  Sources, Rules, Actions, Approval) plus a system readiness check to run
  before scheduling any autonomous/unattended Claude workflow. Backs the
  `night-shift-workflow` skill.
- `loop-engineering.md` — a tool-agnostic 5-stage loop (Inspect → Build →
  Verify → Red Team → Score/Rewrite) plus a copy-paste prompt template for
  running it in any AI tool, and a note on where `task-loop-runner` already
  covers the middle stages in this environment.
- `research-synthesis.md` — six copy-paste prompts (Knowledge Map →
  Literature Review → Gap Finder → Contradiction Detector → Methodology
  Auditor → Executive Brief) for turning a pile of already-gathered sources
  into a decision-ready brief. Backs the `/research-synthesis` command.
- `canva-ai-video.md` — Canva's 5 built-in AI video formats (animated
  design, talking presentation, video editing, AI voiceover, text-to-video)
  with a decision shortcut, platform export specs, and a 4-week recurring
  content system; fills a real gap in the global `video` skill, which
  covers Hyperframes/Remotion/Veo/HeyGen but never mentions Canva. Backs
  the `/canva-video-plan` command.
