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
- `copywriting` — writes individual persuasive copy (headlines, product descriptions, email copy, CTAs) via a Problem → Promise → Proof → CTA framework, once `content-strategy` has picked the topic
- `marketing-psychology` — 8 behavioral persuasion principles (framing, social proof, anchoring, curiosity, loss aversion, specificity, pricing context, decision friction) to pick the right lever for a message instead of stacking random tactics
- `internal-comms` — company newsletters, FAQs, general internal communications
- `doc-coauthoring` — structured workflow for co-authoring docs, proposals, and specs
- `attachment-intake` — how to handle uploaded files (zips, photo batches, docs) that arrive with no or mismatched instructions, instead of guessing at intent
- `design-dev-resources` — curated directory of free design/frontend tool sites (unDraw, SVGL, Aceternity, Glassmorphism generator, JSON Crack, Mobbin) plus notable external AI tools (Genspark, Google Stitch, Google Flow, Gumloop, Figma Make, Kombai) and a design-engineering job board (Design Engineer Jobs) worth knowing about
- `ai-search-marketing-2026` — the SEO/SXO/AEO/GEO/AIO five-discipline wheel, a modern-marketing taxonomy, 5 exec-level marketing-analytics questions, a 15-day day-by-day AI-search action plan, and a 20-source AI-visibility ecosystem map cross-checked against which sources this account can actually query via a live MCP connector
- `growth-operating-framework` — a 7-step sequence for capital-efficient growth (real-business alignment → North Star metric → data foundation → feedback loop → cross-functional accountability → capital-efficient scale → fast iteration)
- `linkedin-virality-playbook` — 9 tactics for LinkedIn posts that reach beyond the author's own network (proof-led hooks, repostable angles, reusable visual templates, real engagement questions)
- `outbound-campaign-brief` — turns a one-line plain-English brief into a B2B outbound campaign (derived target filters, drafted outreach via `copywriting`, real prospecting data instead of fabricated leads) gated behind explicit human approval and a stated send cap before anything sends

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
- `claude-code-tooling` — curated directory of external Claude Code tools (a design-engine desktop app, a senior-engineer skill pack, multi-agent orchestration, a skills package manager, an agent context/memory database, five browser-automation frameworks, a hive-mind team workspace, five open-source AI video-generation models) that are standalone software, not skill files, so they're documented here rather than vendored in
- `web-task-scoping` — governance procedure for scoping any browser-automation task (Target → Limit → Run → Review) before granting a web agent more autonomy; companion to `/scope-web-task`
- `night-shift-workflow` — design and govern a scheduled/unattended Claude workflow (a recurring brief, digest, or Routine) that gathers, triages, and drafts while the user is away, with an explicit Claude-may/human-approval boundary; companion to the `night-shift-canvas` procedure
- `video-model-evaluation` — the "five-clip test": a controlled comparison method (same brief, source, duration, aspect ratio, and rubric fixed before generating) for picking an AI video-generation model based on usable footage instead of a hand-picked demo clip

Drop this repo into a Claude Code project (or point `.claude/skills` at it) to make these available.

## Commands

Slash commands live in `.claude/commands/` — unlike skills (which Claude loads
automatically when relevant), commands are invoked explicitly by name:

- `/ask-the-board [question]` — answers a question using the advisory board set up by the `advisory-board` skill; refuses to improvise generic advisor impressions if no board has been configured yet
- `/improve-system` — reviews the current session for one genuine, durable behavioral signal (not a transcript summary) and persists it to a `memory/` file, updating the memory index
- `/design-review [file or description]` — runs the `design-review-audit` checklist against a build and reports a prioritized punch list
- `/scope-web-task [task]` — applies the `web-task-scoping` skill's Target/Limit/Run/Review discipline to a browser-automation task before it runs; refuses to proceed on side-effecting tasks (submit/purchase/post/delete) until all four are explicit
- `/tool-stack-check [current tools]` — checks a described software stack against `lean-software-stack`'s free alternatives and applies the `free-vs-paid-tool-decision` procedure to recommend switch/keep-paid per tool

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
  `copywriting` handles short persuasive pieces specifically (headlines, CTAs,
  product/pricing copy), drawing on `marketing-psychology`'s principles for
  the persuasive lever and `humanizer` for the final pass.
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

- `outbound-campaign-brief` turns a one-line target/channel brief into a
  B2B outbound campaign: real prospecting data (not fabricated leads) →
  `copywriting` (using `marketing-psychology`'s persuasive lever) for the
  message → `night-shift-workflow`'s Claude-may/human-approval boundary,
  applied as an explicit send cap, before anything actually goes out.
  `sales-enablement` picks up the conversation once a reply comes in.

- `video-model-evaluation`'s five-clip test is the fixed-rubric-before-generating
  discipline applied to picking one of `claude-code-tooling`'s open
  video-generation models — the same "define everything before running, or
  it isn't ready" discipline `night-shift-canvas` applies to workflow setup
  and `design-review-audit` applies to a finished build.

`attachment-intake`, `claude-code-tooling`, `web-task-scoping`,
`night-shift-workflow`, and `video-model-evaluation` are separate,
meta-level skills and aren't part of the business/design content chain
above.

### ⚠️ `brand-guidelines` applies Anthropic's brand, not the user's

That skill is hardcoded to Anthropic's own colors (`#d97757` orange, etc.) and
fonts (Poppins/Lora) — it's for artifacts that should carry *Anthropic's*
look-and-feel specifically. For the user's own company or client branding, use
`product-marketing-context` to capture their real brand and apply it manually
in the design skills instead.

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
- `personal-voice-skill.md` — how to use Anthropic's Skill Creator to turn a
  person's real writing samples into a reusable private voice skill (not
  vendored here — it's Anthropic's own meta-tool, same category as the
  `claude-code-tooling` entries), so future drafts sound like them without
  re-explaining preferences each time.
