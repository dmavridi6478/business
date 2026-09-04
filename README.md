# business
Collect Claude material for buiness

## Skills

A starter bundle of business-oriented Claude skills lives in `.claude/skills/`:

- `sales-enablement` — pitch decks, one-pagers, objection handling, MEDDPICC/MEDDIC/BANT
- `business-decision-frameworks` — MoSCoW, RICE, OKRs, Kano, roadmap formats, Minto Pyramid
- `kpi-reference-handbook` — ~44 standard financial KPI formulas across 8 categories (profitability, efficiency, liquidity, financial structure, cash, investor/valuation), plus an 8-step process for turning a KPI into an action plan
- `quarterly-okr-architect` — quarterly/annual goal architectures (4DX, MASTER, DUMB, backward planning)
- `quarterly-review-cadence` — a 5-step retrospective-and-planning session (Wins → Challenges → Learnings → Unfinished → Next-Quarter Targets) with 3 questions each, a 4-stage prep timeline, and 5 signs it's actually changing behavior; backward-looking companion to `quarterly-okr-architect`'s forward-only goal cascade
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
- `inbound-content-playbook` — a 12-step compounding loop (visibility → trust → conversations → inbound → feedback) for generating inbound leads through content instead of cold outreach, ending in a 5-question self-check
- `resume-prompt-kit` — 10 structured prompts covering a full resume build (positioning → intake → summary → experience → skills → certs → education → ATS proofread) plus JD-tailoring and a cover letter
- `contract-review` — reviews contracts (NDAs, employment agreements, SaaS terms, M&A documents) for unfavorable terms, suggests redlines, and benchmarks clauses against market standards; built on the CUAD dataset (41 risk categories), ContractEval, and LegalBench; vendored in full from [evolsb/claude-legal-skill](https://github.com/evolsb/claude-legal-skill) (MIT) — distinct from the already-installed `claude-for-legal` 12-plugin suite, which doesn't include a focused contract-review skill

A design/output bundle sits alongside it, for turning business content into actual visual deliverables:

- `frontend-design` — distinctive, production-grade web components/pages/artifacts
- `web-artifacts-builder` — complex multi-component HTML artifacts (React/Tailwind/shadcn)
- `canvas-design` — static poster/art pieces (.png/.pdf), ships with real fonts
- `theme-factory` — 10 preset visual themes (colors/fonts) applicable to any artifact
- `premium-html-presentation` — cinematic, dark-mode HTML slide decks
- `the-design-system-prompt` — an alternative cinematic-HTML-deck prompt (secondary to `premium-html-presentation`)
- `ai-canva-presentations` — Claude-structures → Canva-builds → polish workflow for pitch decks/proposals/reports, ~26 min for a 12-slide deck; drives the Canva connector directly when available (outline review → generate → export), one-idea-per-slide discipline, cover/content/data/CTA slide archetypes
- `campaign-page-one-shot` — one-shot marketing landing pages
- `brand-guidelines` — **Anthropic's own** brand colors/fonts specifically, not a generic client-branding tool (see caveat in the skill itself)
- `pptx` / `docx` / `xlsx` / `pdf` — editable PowerPoint, Word, Excel, and PDF file creation/editing
- `design-templates` — 6 ready-to-use, verified-rendering HTML/CSS templates (iMessage mockup, social device frame, 3D product tilt, halftone/dither effect, moodboard grid, brand board) to drop into a build instead of writing from scratch
- `ui-motion-design` — tasteful UI motion: easing curves, spring physics, timing, and micro-interaction patterns
- `design-review-audit` — audits a finished build against a spacing/hierarchy/contrast/consistency/AI-slop checklist; companion to `/design-review`
- `brandkit-generator` — turns a one-line idea into 2-3 brand directions (wordmark, palette, type pairing, brand board), fast and explicitly non-final
- `design-token-extractor` — extracts a reusable color/type/spacing token set from a reference site or screenshot
- `image-to-code` — clones a reference screenshot into real code, then renders and compares before calling it done
- `ai-video-image-prompt-structure` — a 6-part structural pattern (subject → action → setting → camera/shot direction → style/VFX → closing beat) for writing an AI image/video generation prompt that produces a specific result instead of a generic one
- `hallmark` — "anti-AI-slop" design skill for greenfield builds, audits, redesigns, and DNA-extraction from a URL/screenshot (`audit`/`redesign`/`study` verbs); enforces structural variety across 21 named themes/21 macrostructures so builds don't converge on the same hero→3-feature→CTA→footer template; vendored in full (SKILL.md + its whole `references/` library — component cookbook, anti-patterns, typography/color/motion) from [nutlope/hallmark](https://github.com/nutlope/hallmark) (MIT)

A third bundle covers **setting up a new business** — validating an idea and turning someone's own expertise into a sellable product/service before (or instead of) building a team-scale product:

- `product-strategy-session` — full positioning → discovery → roadmap process for validated direction before committing to execution
- `saas-idea-validator` — critical, non-cheerleading stress-test of a new product/software/service idea (problem-solution fit, market, competition, moat, specific failure mode)
- `the-specific-knowledge-excavator` — reverse-engineers a person's unique intersection of expertise nobody else holds in the same combination
- `the-productize-yourself-blueprint` — converts that expertise into a scalable product/service format that sells without the founder's live presence
- `the-leverage-stack-auditor` — diagnoses whether a business idea is actually leveraged (media/code) or just relabeled labor
- `content-repurposing-service` — a concrete worked example: a productized weekly service that turns one client recording into a 7-asset content pack (carousel, video outlines, email, text posts) on a Mon–Fri cadence
- `data-cleanup-brief-service` — a sibling worked example: a productized weekly service that turns a client's recurring messy CSV exports into a clean, verified one-page change brief (deterministic pandas/DuckDB cleanup first, AI narrative only after the numbers are locked), with an honestly-labeled sample price to validate rather than a guaranteed-revenue claim
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
- `linkedin-signal-outreach` — prioritizes and messages LinkedIn prospects by type (warm/cold/dream) and real engagement signal (profile views, comments, funding/role moves, public problems), on a spot-signal → match-message → send-within-24-hours flow; companion to `outreach-channels`, not a duplicate of its volume rule
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

A tenth addition, `hallmark` and `contract-review`, are vendored for real
(SKILL.md + LICENSE + a `SOURCE.md` recording exact repo/commit, same as
`humanizer`/`caveman` above) out of another raw `gh repo clone` list that
was reviewed item by item — see the Plugins section below for the full
review, including everything checked but **not** added (fake repos,
name collisions, off-pattern standalone apps, and a live npm
supply-chain-compromise flag). Both passed the bar for full vendoring:
real, actively maintained, clearly licensed (MIT), and genuinely not
duplicating anything already in this repo.

An eleventh addition, `one-person-business-idea` through
`one-person-business-scaling`, is original content again, same pattern as
the outreach bundle: reviewed from an uploaded photo batch (a 7-image
carousel from a social account, @yourgptguide/"Your GPT Guide"), no GitHub
repo to vendor since it was 5 raw prompts rather than a repo. The carousel's
own framing — "BREAKING: Claude can now help you..." (Claude could always
do this) and "like Dan Koe's $5M solo operation" (an unverified claim about
a third party) — is marketing hype, kept out of the skills themselves; the
prompts underneath it are decent, coherently structured prompt engineering
and were kept. Turned into 5 skills (one per stage) plus one orchestrating
command, `/one-person-business`, following the same
one-skill-per-stage-plus-orchestrator shape as `/outreach-campaign`:

- `one-person-business-idea` — intersects skills/interests/market demand into 3 validated business models and a one-sentence positioning statement
- `one-person-offer-architect` — turns that positioning into a premium-priced offer selling a transformation, never a service/deliverable
- `one-person-content-system` — one owned thesis expanded into ~30 pieces via a cross-platform repurposing map, sized to under 2 hours/week
- `one-person-sales-system` — a zero-sales-call pipeline from content viewer → lead capture → nurture → conversion
- `one-person-business-scaling` — productizes time-for-money work into a digital-product/passive-income layer with a 12-month, milestone-based roadmap, explicitly without hiring

Each skill's `SKILL.md` carries its original prompt verbatim in a
`Prompt (copy-paste)` section, for anyone who wants to run a stage directly
in another assistant instead of through this repo. The photo batch also
included one image that was just a "link in bio" ad for a separate paid
"Art of AI 2.0" prompt bundle (100K prompts, 15+ courses) — that's a paid
upsell with no verifiable content behind it, not something to install, and
isn't reflected in the skills above.

A twelfth addition is 100 slash **commands** rather than skills, reviewed
from a second uploaded photo batch (an 11-image carousel from a different
social account, @ai_slacker, titled "Hidden Claude Codes That Unlock Insane
AI Capabilities — swipe left for more"). That title oversells what's
actually there: these aren't hidden or Claude-specific at all — they're a
personal shorthand-macro list for any chat AI, and each one only works if
something (custom instructions, or here, an actual `.claude/commands/`
file) defines it. Unlike the two prompt carousels above, none of the 100
entries were full role/task/steps/rules prompts — each was a one-line
`/shortname – one-line behavior` pairing across 10 categories (Coding/Tech,
Execution/Output Modes, Thinking Styles, Content Creation, Career/Job Help,
Business/Strategy, Productivity, Learning, Personal Branding, Advanced
Prompt Control). That shape maps almost exactly onto Claude Code's real
custom-slash-command mechanism, so all 100 were installed as real commands
in `.claude/commands/`, each with a short operationalized instruction
rather than just the one-line label. Five were renamed from the source
name to avoid real or likely confusion: `/resume` → `/resume-review`
(collides with Claude Code's own built-in session-resume command),
`/simplify` → `/simplify-explain` (this environment already has a
`simplify` skill/command with unrelated meaning — code-quality cleanup,
not "explain simply"), and `/skills`, `/learn`, `/data` →
`/skills-to-learn`, `/learn-topic`, `/data-driven` (generic enough names to
risk future collisions). Several commands point at this repo's existing,
deeper skills instead of duplicating them (e.g. `/hook` → `hook-writer`,
`/icp` → `outreach-strategy`, `/startup` → `saas-idea-validator`).

The full source list, reproduced in plain text as the carousel presented
it, organized by category:

```text
Coding / Tech
/debug - find bugs
/refactor - clean code
/optimizecode - improve performance
/systemdesign - architecture design
/api - API structure
/database - DB design
/scalability - scaling approach
/security - security checks
/testcases - generate tests
/pseudocode - logic only

Execution / Output Modes
/ghost - only final answer, no explanation
/minimal - shortest possible response
/brief - 3-5 lines max
/expand - detailed explanation
/stepbystep - clear steps
/checklist - actionable checklist
/framework - structured framework
/blueprint - implementation plan
/playbook - repeatable system
/roadmap - timeline based steps

Thinking Styles
/analyst - deep analysis
/critic - find flaws only
/optimizer - improve what's given
/simplify - explain like beginner
/eli5 - very simple explanation
/deepdive - go very detailed
/compare - compare options
/proscons - list pros and cons
/firstprinciples - break to basics
/contrarian - challenge idea

Content Creation
/linkedin - LinkedIn post
/twitter - short thread style
/script - video/reel script
/hook - strong opening lines
/story - storytelling format
/carousel - slide-wise content
/headlines - multiple title options
/captions - social captions
/viral - high engagement style
/authority - expert tone

Career / Job Help
/resume - improve resume
/interview - interview Q&A
/mockinterview - simulate interview
/hr - HR round answers
/portfolio - project ideas
/roadmapcareer - career roadmap
/jobsearch - job strategy
/referral - referral message
/salary - salary negotiation
/skills - skills to learn

Business / Strategy
/startup - startup idea
/gtm - go to market plan
/monetize - revenue ideas
/validate - validate idea
/icp - ideal customer profile
/sales - sales pitch
/colddm - cold outreach
/offer - offer creation
/funnel - funnel strategy
/retention - retention ideas

Productivity
/plan - daily plan
/weekly - weekly plan
/prioritize - what to do first
/focus - remove distractions
/automate - automation ideas
/delegate - what to delegate
/habits - habit building
/track - tracking system
/timeblock - time blocking
/review - weekly review

Learning
/learn - explain topic
/resources - best resources
/practice - practice questions
/quiz - test knowledge
/mistakes - common mistakes
/summary - summarize topic
/revision - quick revision
/notes - structured notes
/examples - real examples
/explainwhy - reasoning

Personal Branding
/profile - LinkedIn profile review
/headline - headline ideas
/bio - bio rewrite
/contentplan - content calendar
/niche - niche clarity
/audience - target audience
/positioning - brand positioning
/engagement - increase engagement
/dms - DM strategy
/growth - growth strategy

Advanced Prompt Control
/toneformal - formal tone
/tonecasual - casual tone
/persuasive - convincing tone
/data - include stats
/examplesonly - only examples
/noexamples - no examples
/limit - limit words
/expandpoints - expand each point
/bullet - bullet format
/nobullet - paragraph format
```

A thirteenth addition is 48 more slash commands, reviewed from a third
uploaded photo batch (a 9-image carousel from a third social account,
@your.aimentor, titled "48 Fable 5 Prompts"). Unlike both carousels above,
this one had no clickbait framing or unverified claims to flag — each image
showed 6 full, coherent, well-structured prompts (not one-liners) across 8
categories, all built around the same idea: long-horizon, self-verifying
"work order" prompts that tell the model to keep going — loop, verify,
re-verify — rather than handing control back after one pass. "Fable 5" is a
real current Claude model (see this session's own model list), so the
branding checks out, though no independent claim is made here about
Fable 5 specifically outperforming other models on these prompts — that's
the source account's framing, not a verified fact.

Each of the 48 was installed as its own command in `.claude/commands/`,
grouped by the carousel's 8 categories, with the original prompt kept
verbatim in the command body (placeholders like `[APP]`/`[REPO]`/`[GOAL]`
filled from `$ARGUMENTS`, with an instruction to ask rather than guess for
anything not supplied) plus a short note to actually loop/verify rather
than stop at the first pass, matching what the prompts ask for. Renamed
away from generic labels to avoid colliding with the 100 commands added
above (e.g. the source's second refactor-flavored prompt became
`/refactor-safely`, not `/refactor`, which already means something
narrower from the prior batch):

- **Build / Ship**: `/build-complete-app`, `/migrate-system`, `/idea-to-build`, `/rebuild-from-ground-up`, `/build-multipart-system`, `/finish-paused-project`
- **Understand / Refactor existing code**: `/map-codebase`, `/refactor-safely`, `/add-missing-tests`, `/explain-and-fix-bug`, `/update-old-project`, `/add-feature-matching-style`
- **Automation / Pipelines**: `/build-pipeline`, `/self-healing-automation`, `/scheduled-routine`, `/trigger-based-automation`, `/content-automation-pipeline`, `/unattended-ops-automation`
- **Recurring work → reusable skill/system**: `/task-to-reusable-skill`, `/audit-my-workflow-for-skills`, `/process-to-teammate-system`, `/oneoff-to-reusable-pipeline`, `/harden-prompt-into-asset`, `/organize-queryable-knowledge`
- **Multi-agent orchestration**: `/build-orchestrator`, `/build-tool-using-agent`, `/design-agent-team`, `/parallel-research-subagents`, `/autonomous-goal-agent`, `/add-agent-guardrails`
- **Research / fact-check**: `/research-and-self-factcheck`, `/deepening-research-passes`, `/steelman-both-sides`, `/verify-common-claim`, `/pressure-test-options`, `/map-space-for-gaps`
- **Loop until done**: `/build-loop-until-tests-pass`, `/grade-and-rewrite-loop`, `/test-and-fix-loop`, `/build-eval-and-improve`, `/verify-with-fresh-subagent`, `/draft-critique-loop`
- **Audit / Review**: `/full-repo-audit`, `/honest-rewrite-review`, `/find-quietly-broken`, `/brutal-senior-review`, `/sweep-for-inconsistencies`, `/preflight-ship-audit`

The full source list, reproduced in plain text as the carousel presented
it (bracketed placeholders as shown, one prompt per line):

```text
Build / Ship
1. Build me a complete working [APP] in one go: data, logic, UI, edge cases. Keep going across as many steps as it takes, test it yourself, and don't hand it back until it runs.
2. Migrate my [SYSTEM] from [A] to [B]. Map it first, do it piece by piece, keep it working at every step, and verify nothing broke before you tell me it's done.
3. Take this rough idea: [IDEA]. Write the spec, build it, test it, fix what breaks, and take it all the way to a working thing. Check in only at the milestones I'd care about.
4. Rebuild my [THING] properly from the ground up. Keep what works, fix what doesn't, carry it to done in one long pass. Show me the before and after and every decision.
5. Build a system with [N] connected parts for [GOAL]. Hold the whole thing in your head, build each part so they fit, and wire them together without losing the plot halfway.
6. Here's a project I started and never finished: [PASTE]. Work out where I left off, finish it properly, fix anything I did badly, and take it to shipped. Tell me what changed.

Understand / Refactor existing code
1. Here's a codebase I don't know: [REPO]. Map it: what each part does, how data flows, where the risky bits are, and the 3 files I should read first. Plain English.
2. Refactor [MESSY CODE] to be clean and readable without changing what it does. Do it in safe steps, keep it working the whole way, and show me each change with why it's safe.
3. Add tests across [PROJECT] where there are none. Start with the riskiest logic, write tests that catch real bugs, run them, and tell me what they revealed.
4. This code is broken: [PASTE]. Explain in plain English what it's meant to do, what's actually going wrong and why, then fix it and prove the fix works.
5. Bring my [OLD PROJECT] up to date: dependencies, patterns, dead code, security. Do it incrementally, keep it running at every step, and give me the changelog.
6. Understand my [CODEBASE], then add [FEATURE] the way the existing code would, matching its style and patterns. Show me where it plugs in and what you touched.

Automation / Pipelines
1. Build a pipeline that takes [INPUT], runs it through [STEPS], and drops the result in [DESTINATION] with no hand-holding. Handle edge cases, retry failures, log each run.
2. Take my automation [DESCRIBE] and make it self-healing: detect a failed step, retry with backoff, fall back to a safe path, and alert me only when it truly can't recover.
3. Set up a routine that runs [TASK] on [SCHEDULE] without me: what it checks, what it produces, where it saves, and the one condition that makes it stop and ping me.
4. Build an automation that watches [SOURCE] and acts when [CONDITION] hits: the trigger, what it does, the safeguard so it never fires wrongly. Then dry-run it on last month's data.
5. Build the automation that turns one [INPUT] into a week of content: draft, repurpose, schedule. Show where AI works, where I approve, and how it keeps running after I sign off.
6. Design an automation that runs my [OPS TASK] unattended: the trigger, every step, the tools, and the checkpoint that catches mistakes before they ship.

Recurring work into a reusable skill/system
1. Take this thing I do over and over: [TASK]. Turn it into a reusable skill with a name, a trigger, the exact steps and output, so I fire it in one command and get the same result.
2. Look at how I work: [DESCRIBE]. Find every repeatable job and turn each into a skill. Give me the stack: name, when to use it, what it does. Flag any two that should merge.
3. Watch how I did [PROCESS] and turn it into a system a teammate could run without me: the steps, the tools, what good looks like, the traps. Then build the checklist that enforces it.
4. Turn this one-off I just did: [TASK] into a pipeline I can rerun on new inputs. Parametrise it, handle the variations, and show me how to run it next time in one line.
5. Here's a prompt I keep tweaking: [PASTE]. Turn it into a proper reusable asset: harden it, add the structure and examples that make it reliable. Give me the version I never edit again.
6. Organise my files and notes into a system I can query: how it's structured, what things are named, and how I ask a question in plain English and get the right answer back.

Multi-agent orchestration
1. Build an orchestrator that spawns subagents to [GOAL] in parallel, merges their results, keeps a shared memory and a step budget, and knows when to stop. Then run it.
2. Build an agent that can [TASK] using [TOOLS]. It decides which tool to call when, handles failures, and stops to ask me only before anything irreversible. Show the decision log.
3. Design an agent team for [WORKFLOW]: a planner, 2-3 specialists, and a reviewer that gates the output. Give each a job and how work passes between them, then run it.
4. Spin up parallel subagents to research [TOPIC], each on a different angle. They report back, a lead agent reconciles the conflicts and writes one brief. Show which agent found what.
5. Give an agent this goal: [GOAL]. Let it plan its own steps, work through them, check its own output, and surface only when it's done or genuinely stuck. Cap it at [N] steps.
6. Add guardrails to my agent doing [WORKFLOW]: which actions need my approval, which errors it retries vs stops on, a hard step and cost cap, and how it flags being stuck.

Research / fact-check
1. Research [TOPIC] properly: gather sources, then adversarially fact-check your own claims, drop anything you can't stand up, and give me a brief where every point is one you'd defend.
2. Do [N] passes on [QUESTION], each going deeper and challenging the last, until you stop finding anything new. Then synthesise the answer and show me what each pass added.
3. Research [DEBATE]. Build the strongest case for each side from real evidence, attack each one, then tell me which survives and the single fact that would change your mind.
4. Everyone says [CLAIM] about [TOPIC]. Go verify it: what's true, what's marketing, what's out of date. Cite what backs each verdict. Don't repeat something just because it's everywhere.
5. Compare [OPTIONS] for [GOAL], but pressure-test every marketing claim against real evidence. Score them on what actually matters to me, name the pick, and the condition that flips it.
6. Map the whole [SPACE], then tell me what nobody's talking about: the gaps, the quiet risks, the thing everyone assumes that might be wrong. Verify before you assert.

Loop until done
1. Build [FEATURE], run it, read the errors, fix them, and loop until every test passes. Don't check in between rounds, keep going until it's green, then show me the diff.
2. Make [OUTPUT], have a fresh subagent grade it against [STANDARD], rewrite, and repeat until it clears the bar. Show me the final plus what each pass fixed.
3. Write tests for [CODE], run them, and fix whatever fails, looping until they all pass and the edge cases are covered. Then tell me what was broken that I didn't know about.
4. Build an eval for [TASK] with 8-10 cases, run my current approach against it, then improve the approach and re-run until the score stops climbing. Show the before and after.
5. Do [TASK], then spin up a fresh subagent to verify it against [GOAL] and flag every hole. Fix them and re-verify. Repeat until it passes clean, then show what changed.
6. Draft [DELIVERABLE], then run rounds of "what's still weak here", fixing the biggest flaw each round, until there's nothing left worth fixing. Stop yourself when it's genuinely good.

Audit / Review
1. Here's a project I built without you: [REPO]. Audit the whole thing. Every bug, dead path, security hole and lazy shortcut, ranked by severity, with the fix for the top 5. Don't stop at file one.
2. Here's work I shipped before Fable 5: [PASTE]. Tell me honestly where it's weak, what a better version looks like, and rewrite the worst section so I can see the gap.
3. Go through my [PROJECT] and find everything quietly broken or half-finished: dead links, TODOs, unhandled cases, stale copy. List it ranked by what bites first, with the fix.
4. Review this [WORK] as a brutal senior reviewer. Flag every assumption and cut corner, and the one thing that would embarrass me if it shipped. No praise, just problems and fixes.
5. Sweep my [DOCS / CODE] for inconsistencies: contradictions, mismatched names, drifted formatting, things that disagree with each other. Return every one with where it is and the fix.
6. Before I ship [THING], run a full pre-flight audit against what "done" should mean: what's missing, what's risky, what I haven't tested. Give me a go / no-go with the exact blockers.
```

A fourteenth addition, `data-cleanup-brief-service`, came from a fifth
uploaded photo batch that turned out to be two unrelated carousels mixed
into one zip: a 6-image "AI Income Playbook" (@zhiprompts) and a 7-image
"5 repos that run AI on your machine" (@ty.prompts.ai, documented in the
Local AI / offline LLM runtimes table above instead, since those are
standalone apps rather than a skill). The @zhiprompts carousel had no
literal AI prompts to install as commands — it's a 5-step productized
service methodology (target a client with recurring messy CSV exports →
lock a column mapping → clean deterministically in pandas/DuckDB → draft
an AI narrative only after the numbers are verified → price and validate a
sample package), refreshingly free of the hype seen in earlier batches: it
labels its own $300/month figure "a testable example" and explicitly says
to validate with a real buyer before treating it as recurring revenue.
Written up as a skill — a sibling to the existing `content-repurposing-service`
worked example — with the source's five cards quoted verbatim in the
skill file for reference.

A fifteenth addition came from a request to actually visit and explore a
carousel's linked sites, not just document them — a 6-image "5 sites we
actually check before designing" carousel (@goluda.ai): Awwwards, Godly,
SiteInspire, Land-book, and Httpster. This session's network egress is
blocked to all five domains (a general restriction on this session, not
specific to this list), so none were live-browsed — worth saying plainly
rather than presenting anything below as observed firsthand. Instead:

- Added a **Design inspiration galleries** table to `design-dev-resources`,
  built from each site's own well-established, independently verifiable
  curation focus (which matches what the carousel itself said about each
  one).
- Added two new copy-paste templates to `design-templates`:
  `saas-pricing-table.html` (a 3-tier pricing table + feature-comparison
  grid, the two patterns Land-book names by name) and `editorial-hero.html`
  (an oversized-serif, one-italic-accent-word hero in the "clean,
  restrained, European" register SiteInspire and Httpster both curate
  for). Both verified rendering with no console errors via Playwright
  screenshot before being added.
- Built `design-reference-shelf.html` — a card-catalog-styled, tag-filterable
  dashboard indexing all five sites by what each is actually good for
  (SaaS / editorial / award-tier / high-volume / small-and-curated),
  published as a Claude Artifact so it's a bookmarkable, reusable
  reference rather than a one-off file: https://claude.ai/code/artifact/d99110f6-3334-4873-a558-133a06b79e78

A sixteenth addition, `waitlist-app-builder`, came from a 12-slide
carousel (@earchoe, "build_with_ai") delivered as a `.rar` archive rather
than a zip — extracted with `unrar` (installed for the session, not
previously available). It's a genuine 4-prompt system for building a
full-stack waitlist app with a viral referral mechanic (refer 3 → jump to
the front 25%, refer 10 → guaranteed access), a Resend-based email drip,
and a password-protected admin dashboard — scaffold, drip sequence,
referral engine, admin dashboard, in that order, with the admin dashboard
explicitly meant to come after the core build ships rather than alongside
it. One caveat worth flagging: slide 2 cites "3x higher day-1 conversion"
and "62% of signups share the product" with no source given — kept out of
the skill's own reasoning as fact, while the underlying referral-psychology
principles (visible position, specific rewards, meaningful scarcity) are
kept since they're well-established independent of that particular
statistic. All 4 prompts are quoted verbatim in the skill file, plus an
orchestrating command, `/waitlist-app`, that runs them in the right
sequence.

A seventeenth addition came from a batch of 6 uploaded infographics
attached directly (not zipped) — a mix of business methodology, real
prompt templates, and one that turned out to be sourced data rather than
a tool:

- **`inbound-content-playbook`** (new skill) — a "CEO's Playbook:
  Generating Inbound Leads Using Content" infographic (smarterwithai.news),
  a 12-step visibility→trust→conversations→inbound→feedback loop. No
  literal prompts, so written up as a skill; cross-referenced against
  `one-person-content-system` and `linkedin-virality-playbook` rather than
  duplicating their territory.
- **`resume-prompt-kit`** (new skill) + **`/build-resume`** (new command)
  — a "ChatGPT Prompts for Building a Standout Resume" cheat sheet
  (smarterwithai.news), 10 real prompts covering a full resume build
  through to a tailored cover letter. All 10 quoted verbatim in the skill
  file. Deeper than the existing `/resume-review` one-liner (from an
  earlier reviewed shorthand-command batch) — that command still covers
  a quick polish pass; this kit is for building or overhauling from
  scratch.
- **`claude-cheat-sheet` extended** — a "How to Prompt AI" infographic
  contributed the 5 C's, SEED, and PEEL structured-prompt frameworks
  (folded into the existing skill rather than a new one, since it's the
  same territory) plus 6 new commands for its "Advanced Prompting
  Techniques": `/plan-then-answer`, `/reflect-then-revise`,
  `/self-critique-pass`, `/evidence-first-grounding`,
  `/assumptions-and-gaps`, `/contrast-few-shot`.
- **15 new commands** from a "Top 15 Perplexity Prompts" infographic —
  genuine, Perplexity-branded but tool-agnostic templates:
  `/market-research-scan`, `/trend-analysis`,
  `/competitor-benchmark-scorecard`, `/customer-feedback-themes`,
  `/case-studies-roundup`, `/industry-report-digest`,
  `/skill-learning-plan`, `/expert-opinion-compare`,
  `/content-ideas-schedule`, `/pdf-summary-digest`,
  `/product-comparison-table`, `/strategy-action-plan`,
  `/event-news-recap`, `/decision-matrix`, `/business-idea-gonogo`. Named
  distinctly from existing commands/skills covering similar ground
  (`competitor-profiling`, `saas-idea-validator`, `one-person-business-idea`,
  `/compare`, `/proscons`, `/contentplan`) rather than colliding with or
  duplicating them.
- **Not turned into a skill or command**: a McKinsey infographic ("Two-
  thirds of today's people management processes can be largely
  automated"). It's sourced data (McKinsey Global Institute Automation
  Model), not a prompt, repo, or tool — nothing to clone or install, and
  this repo has no HR/people-ops skill for it to extend. Noted here for
  completeness rather than forced into an artifact thin enough to not be
  worth having.

An eighteenth addition, `kpi-reference-handbook`, came from a single
"KPIs Handbook" infographic (Bojan Radojicic, promotional material for a
paid handbook sold on Gumroad). No prompts and no repo — it's a dense
formula reference (~44 standard financial KPIs across 8 categories, plus
an 8-step goal→data→calculate→interpret→compare→act process), so nothing
was installed as a command; instead it was written up as a skill the same
way `business-decision-frameworks` reproduces MoSCoW/RICE/OKRs. The
formulas themselves are standard, well-known financial metrics, not
proprietary to that book — worth saying plainly if the source's own paid
product comes up, since this skill isn't a substitute for it, just a
formula lookup. One inconsistency in the source kept visible rather than
silently resolved: it lists "Cash Ratio" twice with two different
denominators (current liabilities under Liquidity, total liabilities
under Cash) — both are kept, labeled distinctly.

A nineteenth addition came from a different kind of source: an uploaded
screen-recording video (`.MP4`), not photos — a TikTok (@simplydigital)
titled "3 Websites for unlimited FREE PROMPTS." No local speech-to-text
was available in this session, so the video was reviewed by extracting
frames with `ffmpeg` (installed for the session) at 1fps and reading the
on-screen text/URLs directly, which was enough — all three sites'
identities and UI were clearly shown on screen. Attempted to actually
visit and browse each site as asked, but this session's network egress is
blocked to all three domains, same limitation as the design-inspiration
carousel earlier — said so rather than presenting anything as observed
firsthand:

- **Meigen.ai**, **Yesand.ai**, **YouMind.com/prompts** — added to
  `design-dev-resources` as a new "AI prompt discovery libraries" table.
  These aren't design-reference galleries, they're community libraries of
  *other people's* actual AI image/video generation prompts (YouMind
  claims 20,000+, updated daily), each with a one-click "use this prompt"
  flow. The example prompts visible in the recording are attributed to
  named individual creators on those platforms (e.g. a Meigen.ai post
  credited to "Pierrick Chevallier | IA") — none are reproduced verbatim
  here, since they belong to those creators, not this repo.
- **`ai-video-image-prompt-structure`** (new skill) — rather than copy
  someone else's specific prompt and present it as a generic template,
  this skill is written fresh: the 6-part structural pattern (subject →
  action → setting → camera/shot direction → style/VFX → closing beat)
  that the recording's examples had in common, illustrated with an
  original worked example instead of a lifted one.

A twentieth addition came from a batch of 4 infographics, two of them
literal templates and two structured procedures checked against existing
skills before adding anything:

- **9 CEO email templates** (Eric Partaker, promotional material for a
  newsletter selling "100 more tools") — installed as 9 commands
  (`/ceo-email-bad-news`, `/ceo-email-reject-idea`,
  `/ceo-email-tough-feedback`, `/ceo-email-delegate-project`,
  `/ceo-email-team-conflict`, `/ceo-email-strategic-change`,
  `/ceo-email-urgent-action`, `/ceo-email-celebrate-win`,
  `/ceo-email-set-boundary`), each filling in the source's real template
  from context rather than paraphrasing it.
- **9 advanced content-analysis prompts** ("Stop using 'summarize
  this'," smarterwithai.news) — installed as 9 more commands
  (`/surface-strategic-takeaways`, `/ideas-to-next-steps`,
  `/core-principles-extract`, `/competing-viewpoints`,
  `/role-specific-summary`, `/teaching-framework`,
  `/reveal-hidden-assumptions`, `/extract-contrarian-insights`,
  `/rewrite-for-influence`). `/extract-contrarian-insights` was named to
  avoid confusion with the existing `/contrarian` command from an
  earlier batch — that one challenges a single idea directly, this one
  pulls unconventional insights out of a larger piece of content.
- **`linkedin-signal-outreach`** (new skill) — "The LinkedIn Outreach
  Matrix Nobody's Using" (Josh Sanders): 3 prospect types (warm/cold/
  dream) each with a real example message, 5 engagement signals to
  watch, and a spot→match→send-within-24-hours flow. Checked against the
  existing `outreach-channels` skill first — that one covers LinkedIn's
  2-DM volume rule, cold-call script, and video outreach; this is a
  genuinely different concern (who to message and when, not how much),
  so it's a companion, not a duplicate.
- **`quarterly-review-cadence`** (new skill) — "How to Run a Quarterly
  Review" (Amy Gibson): a 5-step retrospective (Wins → Challenges →
  Learnings → Unfinished → Next-Quarter Targets, 3 questions each), a
  4-stage prep timeline, and 5 signs it's actually working. Checked
  against `quarterly-okr-architect` first — that skill is a forward-only,
  higher-rigor goal-architecture fusion; this one is the backward-looking
  retrospective that feeds it, not a lighter-weight duplicate of it.

A twenty-first addition came from 2 conceptual infographics — reviewed,
checked against existing skills, and deliberately turned into small
connective edits rather than new skills, since both concepts were already
covered:

- **"RAG vs Agentic RAG"** (AI For Leaders.com) — explains single-pass RAG
  (query → retrieve → augment → generate, for simple/fast/low-complexity
  lookups) versus Agentic RAG (a 7-step loop — understand → decide →
  retrieve → reason → refine, looping back to "decide" as needed → respond
  — for complex/dynamic/high-accuracy research). No new skill: this repo's
  existing `agentic-researcher` agent already *is* a working Agentic RAG
  implementation — its own description states "This is agentic RAG,"
  and it already does the route/validate/re-retrieve/confidence-label loop
  the infographic diagrams. Reviewed and cross-referenced, not duplicated.
- **"OKRs Vs. KPIs for Measuring Performance"** (Vantom Group, promotional
  for a paid mini-course) — defines OKRs and KPIs side by side with
  benefits and a 4-step how-to for each. Most of the content was already
  covered in more depth by the existing `quarterly-okr-architect` (OKRs)
  and `kpi-reference-handbook` (KPIs) skills, so no new skill was created.
  Two genuine gaps got fixed instead: `kpi-reference-handbook` already
  cross-referenced `quarterly-okr-architect`, but the reverse link was
  missing — added, along with an explicit OKR-vs-KPI distinction (OKR =
  the ambitious, time-boxed direction; KPI = the ongoing health metric for
  something already running; KPIs commonly serve as an OKR's Key Results
  or 4DX lead/lag measures) in `quarterly-okr-architect`'s "Related
  skills" section.

Neither infographic contained a literal AI prompt, so there's nothing new
to paste as copy-paste text this time — both were architectural/
definitional content, handled as connective documentation instead.

A twenty-second addition came from 3 more infographics, all from
smarterwithai.news and The Limitless CMO:

- **"How to Learn 10x Faster with AI"** (smarterwithai.news) — 10 learning
  prompt templates. 2 of the 10 duplicated existing commands almost
  exactly (Interactive Quiz → `/quiz`, Analogies → `/eli5`) and were
  skipped rather than re-installed; the other 8 became new commands:
  `/learn-simplified-breakdown`, `/learn-motivation-frame`,
  `/learn-role-play-mentor`, `/learn-mind-map`, `/learn-multi-perspective`
  (checked against the existing `/steelman-both-sides` and `/proscons` —
  distinct enough since this one is learning-oriented, not adversarial or
  weighing-a-decision), `/learn-mnemonics`, `/learn-explanation-feedback`,
  and `/learn-feynman`.
- **"ChatGPT-4o Capabilities"** (smarterwithai.news) — mostly a generic
  capability/marketing reference for a different product (ChatGPT-4o, not
  Claude), with no named external tools in its "Alternatives & Tools"
  section (just unnamed categories) — not turned into a skill, same
  treatment as the earlier McKinsey infographic. Its "Advanced Prompts"
  section did have 4 genuinely reusable prompt patterns, installed as
  commands: `/summarize-with-constraints`, `/role-lens-rewrite`,
  `/translate-preserve-tone`, `/controlled-step-reasoning`.
- **`marketing-org-operating-model`** (new skill) — "How to Future-Proof
  Your Marketing Organization" (Lisa Cole, The Limitless CMO): a 5-step
  operating-model redesign (mandates → codify the work → in-house/
  outsource/automate → apply AI → prove to finance). Checked against the
  existing `growth-operating-framework` first — that skill is
  growth-*strategy* (North Star metric, capital efficiency); this one is
  the org-design layer underneath it (how the marketing function's actual
  work gets routed and executed), so it's a companion, not a duplicate.

A twenty-third addition came from a 15-photo batch containing two carousels:

- **The @yourgptguide "5 Claude prompts" one-person-business carousel** (Find
  Your Idea → Build Your Offer → Content System → Sales System → Scale) —
  compared image-by-image against the existing `one-person-business-idea`,
  `one-person-offer-architect`, `one-person-content-system`,
  `one-person-sales-system`, and `one-person-business-scaling` skills and
  confirmed word-for-word identical to the prompts already vendored there
  (same XML-tag `<role>/<task>/<steps>/<rules>/<output>` structure, same
  text). Treated as a duplicate upload — nothing new installed. The batch's
  2 promotional slides (a "Claude can now help you build a $5M solo
  operation" hook and a paid "Art of AI 2.0" prompt-bundle ad) aren't
  prompts and weren't turned into anything either.
- **The @zhiprompts "5 AI agent builders to try before LangChain" carousel**
  — 5 real agent-building SDKs (Pydantic AI, Agno, Mastra, Strands Agents,
  Google ADK) plus a "build the same small agent twice" framework-bakeoff
  evaluation method (same job, same tools/state/test set/approval rule/
  deployment target on two candidates, then compare code/traces/failures/
  cost). Added to the existing `claude-code-tooling` skill's tool
  directory as a new "AI agent-building frameworks" section, alongside its
  existing browser-automation-frameworks section from the same @zhiprompts
  account — genuinely new content, not a duplicate. Strands Agents' repo
  name (`harness-sdk`, not the more commonly seen `sdk-python`) was
  spot-checked with a web search before including it, since it looked like
  it might be a mislabel; it's real and current.

No new prompts to paste as copy-paste text this round — the one prompt
carousel in this batch was a duplicate of what's already in the README's
plain-text prompt sections above, and the tool roundup had no prompts, just
repos.

A twenty-fourth addition came from an 18-photo batch containing two more
carousels:

- **The @ai_slacker "Hidden Claude Codes" shorthand carousel** — 10 of its
  category slides (Learning, Coding/Tech, Execution/Output Modes, Thinking
  Styles, Content Creation, Career/Job Help, Business/Strategy,
  Productivity, Personal Branding, Advanced Prompt Control) were checked
  one-by-one against the 100 shorthand commands already installed from
  this same carousel earlier in this session (`/learn`, `/debug`,
  `/analyst`, `/linkedin`, `/resume-review`, `/plan`, `/startup`,
  `/profile`, `/toneformal`, and 91 more) — every single command shown was
  already present. Confirmed duplicate, nothing new installed.
- **The @aigenesis.official "It's Just 2 Commands" carousel** — a
  promotional pitch ("REPLACED" stamped over the Claude/ChatGPT logos,
  "SAVE THIS POST") for a fully local/offline AI coding setup. The framing
  overclaims ("same experience as Claude or ChatGPT" doesn't hold for an
  8B local model), but the actual setup is real and useful: Ollama + a
  local Qwen3 model + `sst/opencode` (verified via web search, ~195k★,
  the open-source terminal AI coding agent at opencode.ai). Added to the
  existing `claude-code-tooling` skill as a new "Local, offline AI coding
  setup" section with the exact install commands, plus a genuinely useful
  tip from the same source: raising Ollama's `num_ctx` (context window)
  above its small default so a local coding agent doesn't lose track of
  earlier parts of a codebase mid-session.

No prompts to paste as copy-paste text this round either — the duplicate
carousel's prompts are already pasted in earlier sections of this README,
and the local-AI-setup carousel had shell install commands, not AI prompts
(those are in the `claude-code-tooling` skill above, copy-paste-ready as
shown).

A twenty-fifth addition came from 5 directly-attached infographics:

- **`google-ai-toolkit`** (new skill) — "Top 11 Free AI Tools from Google"
  (smarterwithai.news): maps 11 Google AI products (Imagen/Nano Banana,
  Veo, Gemini Live, Gemini in Sheets, Gems in Gemini, Gemini Ask on
  YouTube, NotebookLM, Google AI Studio, Firebase Studio, Google App
  Builder) to use case, plus the source's choose-the-right-tool map, 5
  reusable prompt patterns, quality/safety checks, and a 4-step workflow
  blueprint (Explore → Produce → Package). Cross-referenced against the
  existing `notebooklm-skill`, which already vendors real working
  automation for one of the 11 — that skill's actual commands, not this
  entry's use-case description, is what to reach for when NotebookLM
  itself is the job.
- **4 new commands from "Mastering ChatGPT"'s "Engagement Prompts"
  section** (smarterwithai.news) — `/action-plan-from-notes`,
  `/micro-curriculum`, `/reflect-on-situation`, `/adaptive-quiz`. The rest
  of that infographic (model tiers, expert-role prompts, prompting
  frameworks) was checked against existing content first: its AIDA/PAS/
  FAB/STAR/SMART/SWOT frameworks weren't covered anywhere in this repo, so
  they were added as a new `references/messaging-frameworks.md` file
  inside the existing `business-decision-frameworks` skill (which already
  catalogs named business frameworks in the same reference-library
  pattern) rather than a new skill; `/adaptive-quiz` was kept distinct
  from the existing `/quiz` command since it adds difficulty-adaptation
  and weak-area tracking, a genuinely different behavior, not just a
  rename.
- **Not turned into a skill or command**: "92 Claude agents now run our
  GTM" and "The Ultimate Claude GTM Engine" (two related posts, both
  ending in a "Comment '92'/'GTM' for free access" call-to-action). These
  are lead-magnet engagement bait — a list of 92 agent *names* and an
  8-department org chart of agent *roles*, with no actual prompts,
  configs, or repos behind any of them to install or verify. The
  department categories they describe (ICP/market intelligence, offer
  positioning, messaging, content, sales enablement, lead generation,
  pipeline/growth, analytics) are already covered in more depth and with
  real content by this repo's existing `outreach-*` skill bundle
  (`outreach-strategy`, `outreach-list-building`, `outreach-copywriting`,
  `outreach-campaign-design`, `outreach-automation`, `outreach-channels`,
  `outreach-replies-pipeline`, `outreach-data-connections`) — nothing here
  added anything those skills don't already do for real.
- **Not turned into a skill or command**: "60 AI Tools" (Mindstream/
  HubSpot Media newsletter ad). A 6-category logo wall (Productivity,
  Marketing, Programming, Design, Video Creation, Sales) with tool names
  and icons only — no descriptions, use cases, or links for any of the 60,
  unlike the richer tool roundups already turned into skills in this repo
  (`design-dev-resources`, `claude-code-tooling`, `lean-software-stack`).
  A handful of the named tools are already covered here in more depth
  (NotebookLM has its own skill; Clay/Seamless AI/Apollo appear in
  `outreach-data-connections`) — the rest would need individual research
  before they're worth cataloging, which a bare logo grid doesn't provide
  grounds for.

Plain-text prompts to copy and paste are given below for the 4 new
commands and are also embedded verbatim in each command's `.md` file.

A twenty-sixth addition came from 5 more directly-attached infographics:

- **9 new commands from "R.I.P. McKinsey: 10 AI Prompts to Replace
  $500/Hour Business Consultants"** (smarterwithai.news) —
  `/swot-analysis`, `/growth-levers`, `/ninety-day-plan`,
  `/revenue-model-projection`, `/churn-reduction`,
  `/kpi-dashboard-framework`, `/pricing-strategy`, `/value-proposition`,
  `/pivot-directions`. The 10th prompt ("Go-to-Market Plan") was checked
  against the existing `/gtm` command first and found near word-for-word
  identical (target segment/channels/positioning/launch sequence in both)
  — skipped as a duplicate rather than re-installed. `/kpi-dashboard-framework`
  cross-references the existing `kpi-reference-handbook` skill for exact
  formulas once KPIs are chosen, rather than duplicating that reference.
- **`stakeholder-engagement-matrix`** (new skill) — "Not all stakeholders
  are created equal" (Hustle Badger): a Power/Interest 2x2 (Manage
  Closely, Keep Satisfied, Monitor, Keep Informed), each quadrant with a
  distinct effort level, examples, and how-to-handle guidance, plus an
  Objective/Channel/Schedule structure for designing the actual comms.
  Checked against the existing `internal-comms` skill first — that skill
  formats a given communication; this one decides *who* gets *how much*
  of it before drafting, so it's a companion, not a duplicate. Cross-
  referenced back into `internal-comms`.
- **Not turned into a skill or command**: "Generative AI Ecosystem
  Overview" (smarterwithai.news) — a definitional taxonomy chart (Deep
  Learning, Transformer Models, Cybersecurity Intelligence, Business
  Intelligence, Automation & Integration, and 5 more domains, each with a
  bullet list of sub-techniques/applications). No prompts, no specific
  tools, no procedure — an educational reference chart, not something to
  clone or install.
- **Not turned into a skill or command**: "Claude Revenue System" — a
  lead-magnet post (blurred-out background icons, "Comment 'REVENUE' For
  Free Access") with no visible content behind the ask beyond a generic
  6-stage cycle diagram (Understand the Market → Find Opportunities →
  Engage Prospects → Close Deals → Grow Revenue → Retain & Expand).
  Nothing to verify or install.
- **Not turned into a skill or command**: "9 AI builds for hands-off GTM"
  (Frontal / Alex Vacca, frontal.so) — another "comment for access" post.
  Each of its 9 cards states an unverified performance metric (5x designer
  output, $200K/month ad spend, 30+ min saved per deal, 2,000+ runs/day)
  for a single account's own business, with no prompt, config, or repo
  link actually given — only a generic mention of "a free repo" with 32
  hooks/15 integrations, not a named URL. Reviewed and flagged as
  marketing claims from one unverified source, not installed.

Plain-text prompts for the 9 new commands are given below and are also
embedded verbatim in each command's `.md` file.

A twenty-seventh addition came from 2 more directly-attached infographics:

- **8 new commands from "ChatGPT for LinkedIn"** (10 prompts,
  smarterwithai.news) — `/linkedin-profile-rewrite`,
  `/linkedin-positioning-statement`, `/linkedin-week-content-plan`,
  `/linkedin-thought-leader-post`, `/linkedin-dm-funnel`,
  `/linkedin-engagement-post-ideas`, `/linkedin-profile-funnel`,
  `/linkedin-growth-audit-checklist`. 2 of the 10 ("Growth Hook
  Generator," "Carousel Structure Blueprint") were checked against the
  existing `/hook` and `/carousel` commands first and found close enough
  in mechanics (both generate hooks/opening lines; both outline a
  slide-by-slide carousel) to be duplicates rather than genuinely new
  behavior — skipped. `/linkedin-thought-leader-post` and
  `/linkedin-dm-funnel` cross-reference the existing
  `linkedin-virality-playbook` and `linkedin-signal-outreach` skills
  respectively, since they cover adjacent but distinct ground (general
  virality tactics; signal-based outreach to non-followers) rather than
  the same thing.
- **`sales-enablement` extended** — "Selling to the C-Suite" (Haris
  Halkic, SalesDaily.co): an 8-role table (CEO, CFO, COO, CRO, CMO, CHRO,
  CIO/CTO, CPO) pairing what each role is actually measured on with a
  "don't say this generic thing" / "say this quantified thing instead"
  pattern. The existing `sales-enablement` skill already had a shallow
  4-row "Value Prop by Persona" table (CTO/VP Eng, VP Sales, CFO, End
  user) inside its ROI-calculator section — rather than duplicate or
  replace it, the fuller 8-role table was added alongside it as a new
  "Selling to the C-Suite (expanded)" section, since it covers 6 roles
  the original table didn't and goes deeper on the 2 it shared (CFO,
  CTO). The infographic's example proof-lines (e.g. "reduced vendor cost
  18%") are the source's own illustrations, not this business's verified
  numbers — flagged in the skill as a shape to fill with real figures,
  not a script to recite.

Plain-text prompts for the 8 new LinkedIn commands are given below and
are also embedded verbatim in each command's `.md` file. The C-suite
messaging table has no single AI prompt to paste — it's a reference table,
now living in `sales-enablement/SKILL.md`.

A twenty-eighth addition came from 2 more directly-attached infographics:

- **`business-decision-frameworks` extended again** — "6 Storytelling
  Frameworks That Help You Lead Inspiringly" (Kelly Knight): Pixar's Story
  Spine, The Golden Circle (Simon Sinek), Duarte's Sparkline, The Hero's
  Journey (Joseph Campbell), And-But-Therefore (Randy Olson), and
  What/So-What/Now-What — 6 named narrative structures for leading
  through change, vision talks, and debriefs. Added as a new
  `references/leadership-storytelling-frameworks.md` file in the existing
  `business-decision-frameworks` skill, distinct from that skill's
  existing `storytelling-pyramid.md` (Minto Pyramid structures a
  *persuasive argument* for a slide; these six structure a *story* for a
  leadership moment — different job, so kept as separate reference
  files rather than merged). Cross-referenced into `quarterly-review-cadence`,
  since What/So-What/Now-What is a compressed 3-step version of that
  skill's full 5-step retrospective.
- **Not turned into a skill or command**: "How to Build a LinkedIn
  Presence and Not Get Lost in the Noise" — a 15-day course table of
  contents (day titles only: "How LinkedIn Actually Works," "9 Content
  Formats That Consistently Work," "Writing Hooks That Make People Stop,"
  etc.), explicitly marked "for educational purposes only" with no actual
  per-day content shown — a curriculum outline, not a prompt or
  procedure. Its topics (hooks, content formats, what drives reach, post
  structure, consistency) are already covered in more depth by this
  repo's `linkedin-virality-playbook` skill and the LinkedIn commands
  installed in the two prior additions, so there's nothing here those
  don't already do for real.

No new prompts to paste as copy-paste text this round — the storytelling
frameworks are a reference (already fully captured in the skill file
above), and the LinkedIn course was a table of contents with no content
behind it.

A twenty-ninth addition came from 2 uploaded zips — one a duplicate, one
new. The duplicate (identical MD5 hash to a zip already processed earlier
in this session — the @ai_slacker shorthand-carousel-repeat +
@aigenesis.official local-AI batch) was skipped without reprocessing. The
new one was a 9-photo carousel:

- **`web-design-taste-workflow`** (new skill) — "How to Turn Claude Code
  Into a Web Design Genius" (@ai_slacker): a 3-step workflow (build a
  Taste Library of real design references grouped by family → arm Claude
  with anti-slop tools it doesn't ship with → never one-shot, build 5
  aesthetic directions wide and narrow down), plus a reusable 4-part
  prompt template (Aesthetic + Reference + Intent + Guardrails, with
  explicit always/never lists) generalized from the source's worked
  example, and a 5-step "iterate until it's yours" tweaks pass. Checked
  against the existing `hallmark` skill first — that's Claude's own
  internal anti-AI-slop design *study* process; this is the external-
  tooling-and-prompting workflow that feeds it, so it's a companion, not
  a duplicate (and `hallmark` wasn't edited, since it's vendored
  verbatim from its source repo).
- **`pbakaus/impeccable`** and **`Leonxlnx/taste-skill`** added to
  `claude-code-tooling`'s directory as a new "AI design-taste / anti-slop
  skills" section — both independently verified real via web search (the
  infographic's cited star counts, ~50K and ~66K, were close enough to
  what's actually listed for each repo to trust the rest of the claims).
  `21st.dev` (a web tool, not a repo) and Higgsfield MCP (already
  available as a connected MCP server in environments where it's
  configured — check `/mcp`) round out the same source's toolbelt.

Plain-text prompt template for the 4-part prompt is given below and is
also embedded in full (with the actual illustrated example) in the
`web-design-taste-workflow` skill file.

A thirtieth addition came from 2 new zip uploads (both had unique hashes,
no duplicates this time):

- **`canva-template-etsy-shop`** (new skill) — "Build one Canva template
  with AI. List on Etsy. Sell it while you sleep." (@earchoe, a
  9-slide entry from a longer 21-part series): what template types sell
  best (Instagram carousel packs, pitch decks, media kits, AI prompt
  cards, lead magnets), a platform comparison (Etsy/Gumroad/Beacons —
  fees and best-for), a 4-tier pricing guide, a 30-minute AI-assisted
  build process (2 literal Canva Magic Design prompts, quoted below), an
  Etsy-listing structure template, and a launch checklist. Checked
  against the existing `the-productize-yourself-blueprint` and
  `one-person-business-scaling` skills first — those are the general
  digitize-your-expertise framework; this is a fully worked, specific
  example of that pattern (Canva templates specifically), so it's a
  companion, not a duplicate.
- **Not turned into a skill or command**: "The Layers of Modern AI
  Systems" (@aicareersuite, 9-slide educational carousel — LLM → RAG →
  Tool Calling → Memory → AI Agent → Skills & Hooks → Governance &
  Observability → Agentic AI). Purely definitional/architectural
  explainer content — no prompts, tools, or procedures to install, same
  treatment as the earlier "Generative AI Ecosystem Overview" and "RAG
  vs Agentic RAG" infographics. Worth flagging one naming collision: the
  infographic's "Skills & Hooks" (generic AI-agent-architecture terms —
  reusable capabilities + automatic triggers) is a different, broader
  concept than this repo's own `claude-cheat-sheet` skill's "Skills" and
  "hooks" entries, which explain the actual Claude Code mechanisms by
  those names — don't conflate the two when discussing either.

Prompts to copy and paste (from the Canva Etsy shop skill) are below.

A thirty-first addition came from a 23-photo zip mixing duplicate and new
carousels:

- **Duplicates, skipped**: the @ty.prompts.ai "5 repos that run AI on your
  machine, no API bill" carousel (Jan, Ollama, LocalAI, llamafile,
  llama.cpp — all already in the README's "Local AI / offline LLM
  runtimes" table) and the @zhiprompts "AI Income Playbook" data-cleanup
  carousel (all 5 numbered cards word-for-word identical to what's
  already quoted in the `data-cleanup-brief-service` skill).
- **New — added to `claude-code-tooling`**: the same @zhiprompts account's
  "5 AI agent tools that automate real work" carousel — a genuinely
  different set from the "5 AI agent builders" carousel reviewed earlier
  this session (that one was code-first SDKs; this one is no-code/visual
  orchestration platforms): `langgenius/dify`, `FlowiseAI/Flowise`,
  `langflow-ai/langflow`, `crewAIInc/crewAI`, `microsoft/autogen`. Added
  as a new section, plus the carousel's "give it one job" agent-trust
  methodology (Job → Boundary → Evaluate → Approve — an agent earns more
  responsibility through measured performance, not by being handed it up
  front), cross-referenced against the existing `night-shift-workflow`
  and `web-task-scoping` skills.

No new prompts to paste this round — this batch was a tool roundup (repos
and a governance methodology), not AI prompts.

A thirty-second addition came from a 7-image zip (@iunlockedai "Tool Drop 23")
covering the keyv npm supply-chain worm discovered Aug 4 2026:

- **New — `npm-supply-chain-security` skill**: the keyv incident
  (`jaredwray/keyv`, commit `1f79edd`) poisoned 2,234 versions across 444
  packages with 150M weekly downloads combined. The worm added a `setup.mjs`
  `preinstall` script that stole GitHub credentials and wrote malicious files
  to up to 50 branches per repo. Persistence relied on two config files
  cross-referencing each other's scripts: `.vscode/tasks.json` ran
  `node .claude/setup.mjs`; `.claude/settings.json`'s `SessionStart` hook ran
  `node .vscode/setup.mjs` — neither file alone looked suspicious. The skill
  covers the three pre-clone checks (`cat .claude/settings.json
  .vscode/tasks.json`; `npm ci --ignore-scripts`; lockfile version audit),
  what cross-directory script references look like, and safe per-package
  `--ignore-scripts` allow-listing for packages that genuinely need install
  scripts.
- **Also noted**: Claude Code 2.1.222 shipped the same day (Aug 4 2026) —
  repo-local `settings.json` can no longer *enable* Remote Control auto-start
  (only disable it); enabling now requires user-scope config via `/config`.
  Closes the class of attacks where a malicious repo turns on Remote Control
  to receive external commands through an agent session.
- **Lead magnet ("Comment VAULT") skipped** — no actual content behind it.

No prompts to paste this round — this batch was a security incident breakdown
with shell commands (reproduced in the skill).

A thirty-third addition came from a 10-image zip (@finitopotatoes "Graph
Engineering explained simply"). A second zip (`1d57f97c`) contained an exact
byte-for-byte duplicate of this batch (all 10 filenames with identical MD5
hashes) — skipped entirely; only the first zip processed.

- **New — `agent-graph-engineering` skill**: covers the Nodes/Edges/State
  model for multi-agent systems (Nodes = specialized workers; Edges = hand-off
  rules; State = shared notebook), why single-agent loops fail on real work
  (compounding context, repeated mistakes, no parallelism, unbounded token
  burn), and three actionable design rules: (1) draw the graph before you
  build it, (2) never let the same agent check its own work — always a
  separate verifier, (3) add hard stops and budgets (max steps, token/cost
  cap, clear success condition). Includes a zero-code manual starting method
  (run each node as a separate Claude chat, merge in a reviewer chat — "that's
  a graph, manual version first") and cross-references to `night-shift-workflow`,
  `web-task-scoping`, and the `multi-agent-orchestrator` agent. Checked against
  existing `claude-code-tooling` skill — that covers *which platforms to pick*
  (Dify, Flowise, CrewAI, AutoGen, etc.); this skill covers *how to design
  the graph* regardless of platform. Distinct; no overlap.
- **Lead magnet ("Comment GRAPH for the free starter checklist") skipped** —
  no actual content behind it.

No prompts to paste this round — the graph engineering batch was a conceptual
framework carousel, not AI prompts.

A thirty-fourth addition came from a 140-image iCloud Photos zip
(`96ba2053-iCloud_Photos_1.zip`) — the largest single batch yet. Images spanned
tool roundups, carousel posts, pricing comparisons, repo spotlights, and a full
@ai_slacker dev-prompts series. Two new skills were created and 25 repos were
identified (all checked against the existing README — zero duplicates):

- **New — `ai-slacker-prompts` skill**: eight battle-tested prompts from
  @ai_slacker's "8 Claude prompts for devs" series — (01) Write a Full PRD,
  (02) Full UI & UX Design Brief, (03) Find Security Gaps, (04) Debug an Error
  Fast, (05) E2E Tests with Playwright, (06) Clean Up & Refactor Dead Code,
  (07) Write Clean Git Commits, (08) Turn a Task into a Skill. Each prompt is a
  complete paste-ready instruction targeting a distinct dev workflow stage.
- **New — `engineering-claude-md` skill**: the @your.ai.mentor Engineering
  CLAUDE.md system prompt — a structured discipline for AI coding agents
  covering (1) investigate the repo before asking anything, (2) deliver a
  design summary with max-3 clarifications then pause for approval, (3) match
  planning depth to change risk, (4) build only after approval, never silently
  pivot. Includes working-assumptions documentation, solution-evaluation
  comparison, and a final 8-item quality checklist (correct, simple,
  maintainable, secure, well-tested, backward compatible, consistent with
  architecture, readable).

Repos identified in this batch (not previously in README):

- `jarrodwatts/claude-hud` (27K★) — Claude Code HUD plugin, heads-up display
  for active agent sessions
- `penpot/penpot` (57K★) — open-source Figma alternative (design + prototype,
  web-based, self-hostable)
- `@your.ai.mentor/designer-skills` (2K★) — Claude skills bundle for design
  teams
- `@your.ai.mentor/Brand-building-skills` (468★) — Claude skills for brand
  building workflows
- `@your.ai.mentor/agent-skill-creator` (2.1K★) — Claude skills for creating
  new Claude skills
- `@your.ai.mentor/claude-code-settings` (1.6K★) — all-in-one Claude Code
  settings collection
- `Panniantong/Agent-Reach` (67K★) — gives Claude live internet access
- `gastownhall/beads` (26K★) — graph-based issue tracker / agent memory
  upgrade
- `headroomlabs-ai/headroom` (65K★) — compresses tool outputs to reduce token
  usage (~20% fewer tokens)
- `shanraisshan/claude-code-best-practice` (64K★) — vibe coding best-practices
  guide for Claude Code
- `jaywcjlove/awesome-mac` (109K★) — curated list of macOS software and tools
- `harry0703/MoneyPrinterTurbo` (102K★) — automated topic-to-video pipeline
- `VoltAgent/awesome-design-md` (107K★) — DESIGN.md files from famous brands /
  design systems
- `luongnv/claude-howto` (41K★) — visual Claude Code how-to guide
- `twentyhq/twenty` (54K★) — open-source Salesforce/CRM alternative
- `ruvnet/RuView` (89K★) — WiFi presence and health sensing with Claude Code
- `puppeteer/puppeteer` (95K★) — headless Chrome Node.js library
- `router-for-me/CLIProxyAPI` (46K★) — wraps Claude Code / Codex as an
  OpenAI-compatible API endpoint
- `ultraworkers/claw-code` (195K★) — Rust agent harness CLI
- `D4Vinci/Scrapling` (73K★) — adaptive web scraping with anti-bot bypass
- `DIYgod/RSSHub` (45K★) — "Everything is RSSible" RSS aggregator
- `medusajs/medusa` (35K★) — open-source flexible e-commerce platform
  (TypeScript)
- `reverse-skill` (19K★) — automated reverse engineering and security analysis
  for APKs, files, and websites
- `manaflow-ai/cmux` (26K★) — Ghostty-based macOS terminal with vertical tabs
  and notifications built for AI coding agents (see every Claude instance at a
  glance, get pinged when one needs you)
- `wasp-lang/open-saas` (15K★) — 100% free modern JS SaaS boilerplate (React,
  NodeJS, Prisma) with full auth (email, Google, GitHub, Slack, MS) and email
  sending

Prompts from this batch — paste-ready plain text:

**@ai_slacker card 01 — WRITE A FULL PRD**
> Act as a senior product manager. Before writing anything, ask me 5 questions about users, scope and constraints. Then write a full PRD: problem, target user, user stories, core features (MVP vs later), success metrics, edge cases, and out-of-scope.

**@ai_slacker card 02 — FULL UI & UX DESIGN BRIEF**
> Act as a product designer. From this PRD, produce a design brief: user flows, screen inventory, layout for each screen, component list, design tokens (colors, type scale, spacing), states (empty/loading/error/success), and accessibility notes.

**@ai_slacker card 03 — FIND SECURITY GAPS**
> Audit this codebase like a security engineer. Find auth flaws, exposed secrets, injection risks, insecure API routes, missing rate limits and unsafe data exposure. Rank by severity, explain the exploit, then give the exact fix.

**@ai_slacker card 04 — DEBUG AN ERROR FAST**
> Here's the error + relevant code. Do NOT change anything yet. List the 3 most likely root causes ranked by probability, tell me exactly what to log or check to confirm each, and only after we confirm, write the fix.

**@ai_slacker card 05 — E2E TEST YOUR APP (PLAYWRIGHT)**
> Set up Playwright for this project. Write E2E tests covering the critical user journeys: signup, login, core action, payment, logout. Include happy path + failure states. Use data-testid selectors, add fixtures for auth, and a script I can run in CI.

**@ai_slacker card 06 — CLEAN UP & REFACTOR DEAD CODE**
> Scan this repo for dead code: unused files, components, imports, deps, env vars and commented-out blocks. Show me the list with proof it's unused BEFORE deleting. Then refactor duplicated logic into shared utils — behaviour must stay identical.

**@ai_slacker card 07 — WRITE CLEAN GIT COMMITS**
> Review my staged changes. Split them into logical atomic commits. For each: a Conventional Commits message (feat/fix/refactor/chore), a scope, and a body explaining WHY not what. Give me the git commands to run in order.

**@ai_slacker card 08 — TURN A TASK INTO A SKILL**
> I just did this task with you. Turn it into a reusable Skill: a clear name, a description of exactly when to trigger it, step-by-step instructions, examples, and common failure modes. Write it so a fresh model with zero context can execute it perfectly.

**@your.ai.mentor — Engineering CLAUDE.md system prompt** (full text in `engineering-claude-md` skill):
Key sections: (1) Learn Before You Ask — inspect source, tests, docs, architecture, existing patterns before interrupting; (2) Deliver a Design Summary then Pause — problem/outcome/constraints, max-3 clarifications with defaults, working assumptions, compare ≥2 approaches, execution plan, then stop for approval; (3) Match Depth to Risk — lightweight for small edits, deeper for auth/payments/infra/migrations; (4) Build Only After Approval — never silently pivot; Engineering Expectations — clarity over cleverness, no unnecessary abstractions, maintainability first, observability from the start; Final Checklist — correct, simple, maintainable, secure, well-tested, backward compatible, architecturally consistent, readable.

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
| [`claude-code-router`](https://github.com/musistudio/claude-code-router) | **Verified, real find** — local gateway that routes Claude Code (and Codex/Kimi/OpenCode) requests across multiple model providers, with request fusion, logging, and cost tracking; 36.7k★, MIT, very high adoption | `npm install -g @musistudio/claude-code-router` then run `ccr code` in place of `claude` (see repo for provider config) |
| [`pal-mcp-server`](https://github.com/BeehiveInnovations/pal-mcp-server) | **Verified real** — MCP server connecting Claude Code (or Codex/Gemini CLI/Cursor) to other models (OpenAI, Gemini, Azure, Grok, Ollama, OpenRouter) for second-opinion/debate workflows; 11.7k★, Apache 2.0 | Add as an MCP server per the repo's README (multi-provider API keys required) — exact `claude mcp add` invocation not independently verified here |
| [`hallmark`](https://github.com/nutlope/hallmark) | **Vendored for real, in full** — see the `hallmark` skill above; not a plugin, listed here for completeness | Already in `.claude/skills/hallmark/` — reproduce elsewhere with `npx skills add nutlope/hallmark` |
| [`gsap-skills`](https://github.com/greensock/gsap-skills) | **Verified, official** — published under the real GreenSock org; teaches correct GSAP usage (core API, timelines, ScrollTrigger, framework integration) to AI agents; MIT | `npx skills add greensock/gsap-skills` — complements the existing `ui-motion-design` skill (GSAP-specific vs. general easing/spring-physics principles) |
| [`threejs-skills`](https://github.com/CloudAI-X/threejs-skills) | **Verified real** — 10-file skill bundle teaching Claude Code Three.js (scene setup, shaders, animation, post-processing); MIT, ~3k★ | `npx skills add CloudAI-X/threejs-skills` — complements `frontend-design`/`canvas-design` for 3D web work |
| [`design-dna`](https://github.com/zanwei/design-dna) | **Verified real** — turns a reference UI screenshot/URL into a structured "Design DNA" JSON (tokens/style/effects), then generates matching UI; MIT, single-maintainer, ~1.4k★ | `npx skills add zanwei/design-dna` — overlaps with `design-token-extractor`; compare outputs before choosing one |
| [`genjutsu`](https://github.com/AThevon/genjutsu) | **Corrected match** — the list's `iamovi/genjutsu` is an unrelated 24h-ephemeral social app; the real "creative coding skills for Claude" repo (animation/3D/design-system orchestrators) is [AThevon/genjutsu](https://github.com/AThevon/genjutsu), MIT, ~247★ | `npx skills add AThevon/genjutsu` |
| [`claude-legal-skill`](https://github.com/evolsb/claude-legal-skill) | **Vendored for real, in full**, as `contract-review` (its own SKILL.md `name:`) — see that skill above; not a plugin, listed here for completeness | Already in `.claude/skills/contract-review/` — reproduce elsewhere with `npx skills add evolsb/claude-legal-skill` |
| [`knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins) | **Verified official** — Anthropic's 11-plugin Cowork suite (productivity, data, design, **operations**, sales, marketing, legal, etc.); Apache 2.0, 23.6k★. Its `operations` plugin (vendor mgmt, process docs, compliance tracking, capacity planning) is a real gap-filler for this repo; its `legal` plugin likely overlaps with the installed `claude-for-legal` — diff before installing both | `claude plugin marketplace add anthropics/knowledge-work-plugins`<br>`claude plugin install operations@knowledge-work-plugins` |
| [`seo-audit-skill`](https://github.com/seo-skills/seo-audit-skill) | **Verified real** — CLI SEO audit (108 rules/12 categories: Core Web Vitals, security headers, structured data, accessibility) with an `--format llm` mode, backed by SEOmator; MIT, 381★; complements the existing `claude-seo` skill | `npx skills add seo-skills/seo-audit-skill` |
| [`anthropics/skills`](https://github.com/anthropics/skills) | **Verified official** — Anthropic's own public Agent Skills repo; the upstream source of the `docx`/`pdf`/`pptx`/`xlsx` skills this repo already uses. Apache 2.0 (skills subfolders source-available); ~170k★ | Reference only — already consumed indirectly via the skills already in `.claude/skills/` |
| [`buildwithclaude`](https://github.com/davepoon/buildwithclaude) | **Verified real** — discovery hub/marketplace indexing ~117 agents/175 commands/26 skills and 20k+ community plugins; MIT, ~3.3k★ | Not installable itself — useful as a browse-and-discover starting point for future additions to this repo |
| [`awesome-compliance`](https://github.com/getprobo/awesome-compliance) | **Verified real** — curated "awesome list" of GRC resources (ISO 27001, SOC 2, SOX, ESG frameworks/tools); CC0-1.0, 103★ | Reference list, not a skill — link from a future compliance skill rather than install directly |

The marketingskills, claude-for-legal, claude-skills, financial-services,
superpowers, openai-codex, and knowledge-work-plugins marketplaces are
registered and the plugins above installed (user scope) in this
environment; `repomix` and `agent-browser` (below) are installed globally
via npm. None of this persists outside this Claude Code installation —
rerun the commands above on any machine that should have the same setup.
`claude-code-router`, `pal-mcp-server`, and the `npx skills add ...` items
above were identified and verified during review but not installed in
this session — reproduce with the commands shown when you're ready to use
them.

A thirty-fifth addition came from a 26-image iCloud Photos zip
(`b37a33ac-iCloud_Photos.zip`) spanning three carousels: a
@zhiprompts "5 AI Voice Tools" repo roundup, a @iunlockedai series
on Claude Code's own CLAUDE.md pruning practice (Boris Cherny, YC
Startup School 2026: Anthropic deleted 80% of Claude Code's own
system prompt — it tested slightly smarter without it; rewrite your
CLAUDE.md at every model release, delete and rebuild from scratch
every six months), and a @earchoe "one-person team" thesis (AI as
a workforce, not a shortcut — one person + the right system = what
used to take a team). One new skill was created; five repos were
confirmed new against the existing README (zero duplicates):

- **New — `ai-voice-tools` skill**: five open-source voice/TTS
  repos from the @zhiprompts roundup, with per-tool setup snippets
  and a quick-selection guide for choosing between them.

Repos identified in this batch (not previously in README):

- `myshell-ai/OpenVoice` (37K★, Python) — zero-shot voice cloning
  with style control (emotion, accent, rhythm); instant results from
  a short reference sample
- `SWivid/F5-TTS` (15K★, Python) — flow-matching TTS with in-context
  voice cloning; no fine-tuning required
- `fishaudio/fish-speech` (32K★, Python) — actively developed
  multilingual speech-generation and TTS system (EN, ZH, JP and more)
- `hexgrad/kokoro` (8.2K★, JavaScript) — lightweight open TTS model;
  runs on CPU via ONNX, no GPU required for basic narration
- `QwenAudio/CosyVoice` (23K★, Python) — enterprise-grade
  multilingual voice synthesis from Qwen/Alibaba's speech research;
  zero-shot and cross-lingual cloning, instruction-based voice control

No paste-ready prompts in this batch (all three carousels were tool
roundups or conceptual/inspirational content, not prompt templates).

---

**36th addition** (`98487103-iCloud_Photos_1.zip`, 74 images + 2 MP4s,
August 2026) — Batch spans six accounts (@martiendejong_dev,
@productester11, @ai_slacker, @buildwithmuj, @iunlockedai, @avarlyhq,
@claude.with.christelle, @speakresume.ai, @51ultron). One new skill was
created; no new GitHub repos were found (n8n was already covered under the
existing `outreach-automation` skill entry via `Zie619/n8n-workflows`):

- **New — `life-mastery-prompts` skill**: seven AI prompts for personal
  mastery from the @martiendejong_dev carousel — billionaire mindset,
  neuro-optimized learning, expert knowledge download, cognitive OS
  upgrading, high-performance life design, time-leverage strategy, and
  psychological identity reprogramming. Each prompt is paste-ready with
  bracketed placeholders for personalization.

Paste-ready prompts from this batch (all from @martiendejong_dev; now
installed in `life-mastery-prompts`):

1. **Think Like a Billionaire** — "You are a thinking coach trained on the
   minds of Elon Musk, Naval Ravikant, Jeff Bezos, and top polymaths.
   Reprogram my thought process to think in systems, long-term vision,
   leverage, and asymmetric outcomes. Give me daily mental models to shift
   from average thinker to billionaire thinker."

2. **Neuro-Optimized Tutor** — "You are a neuro-optimized tutor. I want to
   learn any complex skill 10x faster than others. Create a weekly learning
   blueprint based on spaced repetition, interleaving, the Feynman
   technique, and active recall. Apply it to [insert topic]. I want to be
   in the top 1% in 90 days."

3. **Download Expert-Level Knowledge** — "You are a world-class expert in
   [insert any skill]. Train me as if I'm your apprentice, from beginner to
   mastery. Break it into stages, tasks, uncommon resources, and shortcuts.
   Include simulations or real-life practice assignments to truly
   internalize each level."

4. **Cognitive OS Upgrader** — "You are my cognitive OS upgrader. Audit my
   current thought patterns, habits, and beliefs based on this description:
   [describe how you think now]. Then rewrite my operating system to
   improve clarity, decision speed, memory, creativity, and emotional
   control."

5. **High-Performance Architect** — "You are my high-performance architect.
   Help me design a god-tier life based on time freedom, health, wealth,
   relationships, and purpose. Create a daily system, environment, people I
   must avoid, habits to master, and beliefs to rewire to become
   unstoppable."

6. **Compress Decades into Days** — "You are a time-leverage strategist. I
   want to achieve in 1 year what most take 10 years to do. Based on my
   goal: [insert goal], create a high-leverage blueprint using shortcuts,
   tools, mentors, delegation, automation, and AI to leapfrog everyone
   else."

7. **Psychological Reprogrammer** — "You are a psychological reprogrammer.
   Based on my goal to become [insert ideal self], help me destroy my
   current limiting identity and install a new operating self-image, thought
   pattern, and behavior map that aligns with my highest version."

Other carousels in this batch were commercial-app roundups (Buffer,
Mailchimp, Canva, Gemini, Gemini Notebook, Manus, HeyKleos.dev,
avarly.io), Claude Code informational explainers (auto-mode default,
cross-session messaging, deny-rules, plugin sha256 pinning), or
conceptual prompting advice with no extractable repos or reusable prompts.
The @51ultron "7 website building prompts" carousel gated actual content
behind engagement-bait DMs — no prompts were visible in the images.

### Reviewed and not added

A raw list of `gh repo clone` commands (source unverified — looked like
another social-media "tools to install" roundup) was checked item by item
before writing the additions above. Several entries didn't hold up:

- **Doesn't exist / unverifiable as named:** `HaydenLundin/marketing-psychology`,
  `akhilesh-bisht/email-sequence-app` — no matching repo found under either
  path.
- **Name-collision false positives** (real repos, wrong domain): `CMVSR/def-model-review`
  (an NLP "definition modeling" paper, not financial model review),
  `e0397123/comp-analysis` (an LLM dialogue-evaluation paper, not competitor
  analysis), `orgs/croservices` (the Raku-language **Cro** framework org, not
  conversion-rate optimization), `Google-Health/path-foundation` (Google's
  digital-pathology imaging model — genuinely irrelevant to business use as
  suspected), `jajokine/Business-Cases` (grad-school data-science coursework,
  not business-ops content). `r-lib/pillar` (the well-known tidyverse R
  package) and `pillarhq/pillar` (a small AI-copilot-widget SDK) are both
  real but are two *unrelated* projects sharing a name — neither fits this
  repo's pattern.
- **Real but off-pattern** (standalone apps/SDKs, not Claude
  skills/plugins/MCP servers): `trypostit/trypost` (self-hosted social
  scheduler), `pillarhq/pillar` (embeddable AI-copilot SDK),
  `dolanmiu/docx` (the well-known npm library for generating `.docx`
  files in JS — unrelated to this repo's own `docx` *Claude skill*),
  `enochtangg/quick-SQL-cheatsheet` (a static reference doc),
  `orgs/slackhq` (Slack's general OSS org — Bolt SDKs etc., no official
  Slack MCP server found there), `orgs/NVIDIA-Omniverse` (89 repos, all
  3D-simulation/robotics tooling, no general-purpose Claude skill or MCP
  server), `OpenHands/OpenHands` (83k★ MIT — a full competing coding-agent
  platform, not a Claude Code add-on), `Mintplex-Labs/anything-llm`,
  `khoj-ai/khoj`, `Zie619/n8n-workflows` (flagged: a DMCA-driven history
  rewrite is a caution sign), `omnigent-ai/omnigent` (a multi-agent
  orchestration framework, different category from a skill/plugin),
  `MadsLorentzen/ai-job-search` (a real personal Claude-Code project, but
  niche/single-purpose rather than reusable infra).
- **Low-maturity / unverified quality — flagged, not installed as-is:**
  `pro-how-ai/sop-builder-kit` (2★, 1 commit — directly fills a real SOP
  gap conceptually, but too thin to vouch for), `JimCortes/LBO_Model` (7★,
  no license), `arnavchaturvedi17/…3_Statement_Financial_Model` (solo Excel
  template, no license stated), `openrunbook/openrunbook` (5★, skews
  SRE/infra runbooks rather than general business ops),
  `diegosouzapw/OmniRoute` (claims "450+ contributors," unusually high for
  an obscure repo — verify before trusting).
- **Reference content worth citing but not packaging as a skill:**
  [`joelparkerhenderson/pitch-deck`](https://github.com/joelparkerhenderson/pitch-deck)
  (curated pitch-deck advice from YC/500 Startups/Unusual Ventures, 432★ —
  a good source for `sales-enablement`) and
  [`danluu/post-mortems`](https://github.com/danluu/post-mortems) (a
  well-known, actively maintained collection of real-world incident
  postmortems, 12.3k★ — relevant if this repo ever adds an ops/incident
  skill).
- **`@zapier/sdk` and `@zapier/mcp` don't exist on npm as named.** The real
  official packages are `@zapier/zapier-sdk` and `@zapier/mcp-integration`
  (which lets *Zapier* call remote MCP servers — the reverse of what an
  agent needs). Skip either way: this repo already has Zapier connected as
  a claude.ai connector covering the same 9,000+-app use case, and several
  `@zapier/*` packages were hit by a November 2025 npm supply-chain
  compromise (the "Shai-Hulud" worm, harvesting npm/GitHub tokens) — don't
  `npm install` any `@zapier/*` package without confirming the installed
  version postdates the fix.
- **Duplicate of an existing best-guess entry:** `jlbadano/ig-mcp` (a
  Python MCP server for Instagram Business accounts via the Graph API)
  solves the same problem as the `instagram-mcp` entry already in the MCP
  table below (`mcpware/instagram-mcp`) — pick one rather than installing
  both; DM features are gated behind Meta App Review either way.
- **Not a Claude tool, quick "still the same repo" check only:**
  `coreyhaines31/marketingskills` (already vendored above, confirmed
  unchanged; its ~44.9k★ figure recurred consistently across checks but is
  unusually high for its category and worth a manual spot-check before
  citing it publicly), `anthropics/financial-services` (already vendored,
  confirmed unchanged).

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
| `instagram-mcp` (**best-guess match, uncertain**) | ❌ not installed | No single canonical repo; closest name match is [mcpware/instagram-mcp](https://github.com/mcpware/instagram-mcp) (Graph API, 23 tools). A second real option, [jlbadano/ig-mcp](https://github.com/jlbadano/ig-mcp) (Python, Graph API), turned up in a later review — same use case, pick one rather than both. Needs an Instagram Graph API token to connect — add with `claude mcp add instagram-mcp -- npx @mcpware/instagram-mcp` once you have credentials |
| [`OfficeCLI`](https://github.com/iOfficeAI/OfficeCLI) | ❌ not installed, verified real | CLI + bundled MCP server letting an agent read/edit/automate Word/Excel/PowerPoint files without Office installed; actively releasing (v1.0.143+) | Add per repo README once needed — overlaps with this repo's own `docx`/`pptx`/`xlsx` skills but operates on real files via MCP rather than generating new ones |
| [`DesktopCommanderMCP`](https://github.com/wonderwhy-er/DesktopCommanderMCP) | ❌ not installed, verified real | Well-known MCP server giving Claude terminal control, filesystem search, and diff-based file editing; actively maintained | `npx @wonderwhy-er/desktop-commander@latest setup` (or via Smithery/Docker — see repo) |
| `agent-browser` | ✅ installed as a CLI | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — despite the "MCP Servers" slide, Vercel built this as a token-efficient browser-automation **CLI**, not an MCP server. Installed globally: `npm install -g agent-browser && agent-browser install` |
| `granola` (**best-guess, uncertain**) | ❌ not installed | Reads local [Granola](https://granola.ai) meeting notes/transcripts. No official/canonical MCP server found — a dozen community repos share the name (e.g. [chrisguillory/granola-mcp](https://github.com/chrisguillory/granola-mcp), [bhandzo/pantry](https://github.com/bhandzo/granola-mcp)). Requires the Granola desktop app running locally, so nothing to verify from this session — pick one and `claude mcp add` it once you have Granola installed |
| [`kondo`](https://www.trykondo.com/) | ❌ not connected | **Correction: real, but not open-source** — not a GitHub repo (the earlier "could not verify" note was from only searching GitHub). Kondo is a commercial LinkedIn inbox-management Chrome extension ("Superhuman for LinkedIn DMs" — labels, snooze, keyboard triage) that ships a hosted MCP connector on its **Business plan** ($36/user/month), set up at [docs.trykondo.com/mcp-setup](https://docs.trykondo.com/mcp-setup); it requires the Kondo browser extension actively running and reads your live LinkedIn inbox locally in-browser (per their docs, it doesn't store LinkedIn data server-side). Needs a paid account + the extension — can't be connected from this session |
| `higgsfield` | ❌ not installed | Cinematic AI image/video generation. [Official docs](https://higgsfield.ai/mcp) exist but no official GitHub org repo was found; several community MCP servers do ([Hikhakk/higgsfield-mcp-unified](https://github.com/Hikhakk/higgsfield-mcp-unified) — 27 models — looked most complete). Needs a Higgsfield API key/account either way |
| [Linear](https://linear.app) | ✅ **registered** (auth pending) | Official remote MCP server, `https://mcp.linear.app/mcp` — registered in this project with `claude mcp add --transport http linear-server https://mcp.linear.app/mcp`. First real use opens a browser OAuth prompt this non-interactive session can't complete; a project-management-workflow one, separate from `claude-for-legal`'s own Linear connector (which is scoped to `product-legal` only) |
| Obsidian | 📋 documented, not installed | Local note-taking app — no cloud API, so nothing to connect from this session. [coddingtonbear/obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) is the community plugin (install from inside Obsidian → Settings → Community plugins) that now ships a built-in MCP endpoint at `/mcp/`; enable it, then `claude mcp add --transport http obsidian http://localhost:27124/mcp` (port/token from the plugin's settings) |
| Codex | ✅ already covered | Not an MCP server — OpenAI's own coding agent/CLI. The actual Claude-Code-relevant integration is the `codex-plugin-cc` plugin documented above, already installed |
| "Claude Design" | N/A | Not a separate tool — this is Claude itself (Anthropic's own branding), used as a general writing/brainstorming assistant. Nothing to install |
| "The Pulp" | ❓ unverified | Described as a personalized daily-briefing/podcast app. Could not confirm a matching product by that name (an unrelated media-industry podcast shares the name; closest real equivalents are apps like Huxe or Spotify's Personal Podcasts). Even if real, it reads as a closed consumer app with no public API/MCP/skill surface — nothing to clone or install either way |

### Local AI / offline LLM runtimes

Reviewed from a fourth uploaded photo batch (a 7-image carousel,
@ty.prompts.ai, "5 repos that run AI on your machine, no API bill"). All
five repo paths, descriptions, and star counts were independently
verified — real, accurate, no corrections needed except one the carousel
actually got right where a guess would've gotten it wrong (`llamafile`
lives at `mozilla-ai/llamafile` today, not the project's original
`Mozilla-Ocho` org, which now redirects there). These are standalone
local-inference apps/engines, not Claude Code skills/plugins/MCP servers —
documented here for completeness, same treatment as `OpenHands`/
`anything-llm`/`khoj` in the Plugins section above.

| Item | What it is | Notes |
|---|---|---|
| [`janhq/jan`](https://github.com/janhq/jan) | Open-source ChatGPT-alternative desktop app, runs 100% offline; ✅ verified, ~44k★, Apache 2.0 | The one to start with if you just want a local chat app, not a dev tool |
| [`ollama/ollama`](https://github.com/ollama/ollama) | The standard local model runner most of the local-AI ecosystem plugs into (`ollama run <model>`); ✅ verified, ~179k★, MIT | Supports Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma, and more |
| [`mudler/LocalAI`](https://github.com/mudler/LocalAI) | Open-source AI engine — LLMs, vision, voice, image, video, no GPU required, OpenAI-API-compatible; ✅ verified, ~49k★, MIT | Drop-in replacement for the OpenAI API in existing code |
| [`mozilla-ai/llamafile`](https://github.com/mozilla-ai/llamafile) | Distributes and runs an entire LLM as a single executable file — no install, no runtime, no dependencies; ✅ verified, ~26k★, Apache 2.0 | Correct current org — the project's original `Mozilla-Ocho/llamafile` path now redirects here |
| [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp) | LLM inference engine in C/C++ — the low-level engine most of the above (and much of the wider local-AI ecosystem) is built on; ✅ verified, ~125k★, MIT | Correct current org — moved from the original `ggerganov/llama.cpp` |

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
- `/one-person-business [skills/interests, or an existing idea/offer]` — runs the `one-person-*` skill bundle end to end (idea → offer → content system → sales system → scaling); stops to ask if the idea failed its own validation check, or if scaling is requested before a content/sales system actually exists
- `/waitlist-app [product name, description, target user, tone]` — runs the `waitlist-app-builder` skill's 4 prompts end to end (scaffold → drip sequence → referral engine → admin dashboard); holds the admin dashboard for a follow-up pass rather than building it before the core signup/referral loop is verified working
- `/build-resume [target role, industry, seniority, optional job posting]` — runs the `resume-prompt-kit` skill's 10 prompts end to end (positioning → intake → summary → experience → skills → certs → education → ATS proofread), then tailoring + a cover letter if a specific job posting was given; asks for real background details rather than inventing achievements or dates
- 21 more single-purpose commands from a reviewed infographic batch (`/plan-then-answer`, `/self-critique-pass`, `/market-research-scan`, `/business-idea-gonogo`, `/decision-matrix`, and 16 more) — see "A seventeenth addition" above for the full list and source
- 100 single-purpose shorthand commands (`/debug`, `/brief`, `/eli5`, `/linkedin`, `/resume-review`, `/startup`, `/plan`, `/learn-topic`, `/profile`, `/toneformal`, and 90 more) — see "A twelfth addition" above for the full category list and source; each takes one argument and applies one specific behavior modifier or micro-task rather than running a multi-step workflow
- 48 long-horizon "work order" commands (`/build-complete-app`, `/refactor-safely`, `/build-orchestrator`, `/research-and-self-factcheck`, `/build-loop-until-tests-pass`, `/full-repo-audit`, and 42 more) — see "A thirteenth addition" above for the full category list, source, and verbatim prompts; each runs a full self-verifying pass (build/refactor/automate/orchestrate/research/loop/audit) rather than a single-step response

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

---

**37th addition** (`83ad5cc1-iCloud_Photos.zip`, 130 images, August 2026)
— Batch covers accounts including @jessiekimbooks, @aigenesis.official,
@claude.with.christelle, and others spanning prompt frameworks, writing
guides, job-application systems, and local-AI tools. Four new skills were
created; no new GitHub repos were installed (two candidates were confirmed
duplicates of existing README entries).

New skills created:

- **`claude-prompt-frameworks`** — eight acronym-based frameworks for
  structuring AI requests: CLARITY, SOCRATES, ANTICIPATE, PARTNER, TRUST,
  RIPPLE, CATCH, and MAGIC. Each letter maps to a component of a complete
  prompt (Context, Look & Feel, Ask, Rules, etc.). Includes a quick-selection
  guide mapping use cases (quick one-off, creative work, complex research,
  project/campaign) to the best framework.

- **`claude-20-prompts`** — twenty ready-to-use paste-and-go prompts from
  @aigenesis.official across four categories (Work, Study, Life, Money):
  Screenshot Audit, Meeting to Actions, Inbox Zero, Doc Interrogation, Build
  a Skill, Notes to Cheatsheet, Exam Me, Explain 3 Ways, Feynman Check,
  Study Plan, Hard Conversation, Trip Planner, Meal Plan, Habit Debug,
  Decision Coach, Contract Traps, Negotiation Prep, Offer Compare, Bill
  Decoder, Side-Income Ideas. Each prompt has bracketed placeholders.

- **`claude-writing-prompts`** — four writing prompts for book authors from
  @jessiekimbooks "Claude, Uncomplicated": (1) find the real problem via
  Reddit/review mining before outlining; (2) structure chapters so each one
  changes a belief; (3) extract voice from 500 words then write Chapter 1;
  (4) show what to cut rather than improve.

- **`job-application-5-prompts`** — five-prompt job application system from
  @claude.with.christelle, engineered to tailor a resume to a specific job
  in under 45 minutes: Job Description Decoder → Resume Audit → Bullet
  Rewrite → Cover Letter → Interview Prep. Distinct from the existing
  `resume-prompt-kit` skill (which is a general resume builder); this one
  is purpose-built for job-specific tailoring with their exact language.

Repos identified in this batch (not previously in README):

- [`Zackriya-Solutions/meetily`](https://github.com/Zackriya-Solutions/meetily)
  (29k★, MIT, Rust) — privacy-first local AI meeting assistant; transcribes
  with Parakeet/Whisper, summarizes via Ollama — no data leaves the machine
- [`ItzCrazyKns/Vane`](https://github.com/ItzCrazyKns/Vane) (36k★, MIT) —
  local AI-powered search/answering engine via Ollama with cited sources;
  open-source Perplexity alternative
- `mcp-explorer` (pip install, Apache-2.0, ~109★, by Simon Willison) — CLI
  to inspect and audit any MCP server's exposed tools without a full client
  setup; `pip install mcp-explorer && mcp-explorer <server>`

Paste-ready prompts from this batch:

**From `claude-prompt-frameworks` (8 acronym frameworks):**

CLARITY — C: Context · L: Look & Feel · A: Ask · R: Rules · I: Input ·
T: Target · Y: You (role)

SOCRATES — S: Situation · O: Objective · C: Constraints · R: Role ·
A: Action · T: Thinking · E: Evaluation · S: Summary

ANTICIPATE — A: Audience · N: Need · T: Task · I: Information ·
C: Constraints · I: Illustrate · P: Plan · A: Ask · T: Test · E: Enhance

PARTNER — P: Purpose · A: Audience · R: Research · T: Think · N: Narrow ·
E: Execute · R: Review

TRUST — T: Task · R: Reason · U: Understand · S: Structure · T: Tailor

RIPPLE — R: Role · I: Input · P: Process · P: Points · L: Layout ·
E: Evaluate

CATCH — C: Context · A: Aim · T: Tone · C: Criteria · H: Help

MAGIC — M: Motivation · A: Audience · G: Goal · I: Input · C: Create

**From `claude-writing-prompts` (book authors, @jessiekimbooks):**

1. Before outlining — "Research what people say about [topic] on Reddit and in
   reviews. Give me the 10 complaints that repeat most — in their words."

2. Structure — "Build an outline where each chapter changes one belief. Then
   cut the chapters that don't earn their place."

3. Voice — "Extract the rules of my voice from these 500 words. Then write
   Chapter 1 following them."

4. Editing — "Don't improve this chapter. Show me what to cut."

**From `claude-20-prompts` (Work/Study/Life/Money, @aigenesis.official):**

*Work:*
- Screenshot Audit — "Paste a dashboard screenshot: what is wrong with this
  and what would you fix?"
- Meeting to Actions — "Turn this call transcript into decisions, owners and
  deadlines: [PASTE]"
- Inbox Zero — "Sort my inbox into reply, delegate, ignore and draft the
  replies: [PASTE]"
- Doc Interrogation — "Answer only from this document: what does it claim and
  quietly avoid: [PASTE]"
- Build a Skill — "Turn this repeated task into a reusable skill I fire with
  one command."

*Study:*
- Notes to Cheatsheet — "Turn these 40 pages into a one-page cheat sheet: [PASTE]"
- Exam Me — "Quiz me on [TOPIC] like a real exam, then grade and explain my misses."
- Explain 3 Ways — "Explain [CONCEPT] with a metaphor, an example, and a
  diagram in words."
- Feynman Check — "I will explain [TOPIC] to you — catch where my
  understanding is wrong."
- Study Plan — "Build a 2-week plan to learn [TOPIC] in [HOURS] a day, no filler."

*Life:*
- Hard Conversation — "Script a hard talk about [SITUATION]: what to open
  with, what to avoid."
- Trip Planner — "Plan a [DAYS]-day trip to [PLACE] with real downtime, flag
  what to book early."
- Meal Plan — "Plan 5 dinners for [DIET] and give one grocery list by aisle."
- Habit Debug — "I keep failing to [HABIT] — find the real reason and the
  smallest fix."
- Decision Coach — "Ask me the 5 questions that decide [OPTION A] vs [OPTION B]."

*Money:*
- Contract Traps — "Read this contract and flag every clause that could cost
  me: [PASTE]"
- Negotiation Prep — "Prep me to negotiate [DEAL]: my leverage, their BATNA,
  my walk-away."
- Offer Compare — "Compare these two job offers on total value, not just
  salary: [PASTE]"
- Bill Decoder — "Explain this bill in plain English and what I am actually
  paying for: [PASTE]"
- Side-Income Ideas — "Given my skills [X], list 5 realistic ways to earn on
  the side."

**From `job-application-5-prompts` (job tailoring system, @claude.with.christelle):**

1. Job Description Decoder — "Analyze this job description. Extract the 5
   most important skills they want. Identify the exact keywords used
   repeatedly. Tell me what this company actually values — not what they say,
   but what the repetition reveals."

2. Resume Audit — "Audit this resume against the job description. Where do I
   have the experience but buried it in wrong words? What is missing? What is
   irrelevant? Be specific. Be brutal."

3. Bullet Rewrite — "Rewrite every bullet using the exact keywords from the
   job description. Every bullet must follow this formula: Action verb +
   Achievement + Number. No responsibilities. No duties. Only accomplishments
   with numbers. If I gave you no numbers — ask me for them before you write."

4. Cover Letter — "Write me a cover letter for this role. Do not summarize my
   resume. Instead — tell a story about one specific moment in my career that
   proves I can do the most important thing this job requires. Open with the
   story. Use their exact language. Close with one sentence that makes it
   impossible not to call me."

5. Interview Prep — "Give me the 5 hardest interview questions for this role
   and for someone with my background. Write a strong model answer for each
   using the STAR method. Pull from my resume for the specific experiences to
   reference. Use the company's own language and values in the answers."

### Reviewed and not added (37th batch)

- **`LocalSend`** — already in README (34th addition); skipped.
- **`ollama/ollama`** — already in README (Local AI / offline LLM runtimes
  section); skipped.

---

**38th addition** (`b314bb3d-iCloud_Photos_1.zip`, 53 images, August 2026)
— Batch covers accounts including @ray_fu, @appmillers, and
@TheChatGPTMarketer, focusing on Claude Code ecosystem repos and
full-stack marketing prompts. Two new skills were created from prompt
content; several Claude Code repos were identified for the reference
index. `repomix` was confirmed a duplicate (already in README at the
Claude Code Tooling table).

New skills created:

- **`claude-clean-audit-prompts`** — the three-layer "Clean Your Claude"
  audit system from @appmillers. Layer 1 audits CLAUDE.md line-by-line
  against Anthropic's live guidance (DELETE/KEEP/REWRITE verdicts with
  source quotes). Layer 2 audits the skills folder for overlap and dead
  weight (groups by job, flags unused/orphaned skills, produces a merged
  version of the biggest group). Layer 3 audits every hook (lists all,
  flags expensive always-on triggers, common trigger words, conflicts,
  broken file paths, forgotten hooks — verdict table, nothing changed
  until you say so). A bonus "Hook Discovery" prompt finds what should
  become a hook in the first place. Run in order: Discovery → Layer 1 →
  Layer 2 → Layer 3.

- **`marketing-10-prompts`** — ten production-ready marketing prompts from
  @TheChatGPTMarketer covering the full marketing stack: (1) Deep
  Competitor Teardown — UVPs, pricing table, top complaints, gaps with
  citations; (2) Voice-of-Customer Mining — theme groups, 3-word labels,
  top quotes, copy ideas; (3) Complete Content Audit — Keep/Refresh/Delete
  labels per URL with quick-win flags; (4) Customer-Journey Map — six
  stages, goals/questions/objections/content/AI prompt per stage;
  (5) Keyword & Intent Gap Analysis — missing high-intent keywords scored
  by impact × ease; (6) Quarterly Trend Scan — top 3 industry trends with
  stats and B2B action ideas; (7) Attribution Sanity Check — ROAS/CAC
  calculation plus 30%+ attribution inflation flags; (8) A/B-Test Idea
  Backlog — ICE-scored hypotheses per funnel drop-off; (9) Evergreen FAQ &
  Knowledge Base Build — feature-grouped FAQ from support tickets;
  (10) Press-Ready Data Stories — 3 headline-worthy data insights with
  chart recommendations.

Repos identified in this batch (from @ray_fu "10 Claude GitHub Repos
that Actually Matter"):

- [`hesreallyhim/awesome-claude-code`](https://github.com/hesreallyhim/awesome-claude-code)
  (28.5K★) — curated directory of 545 Claude Code resources: 142 Skills,
  63 Hooks, 88 Commands, 110 Plugins, plus CLAUDE.md examples and agents.
  Reference index, not a plugin install.
- [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills)
  — CLAUDE.md with Karpathy's 4 coding principles packaged as a Claude Code
  plugin; install: `npx claude plugin add forrestchang/andrej-karpathy-skills`
- **TDD Guard** (1.7K★) — Claude Code hook that blocks the agent from writing
  code until tests are written first; enforces test-driven development at the
  hook level.
- [`everything-claude-code`](https://github.com/disler/everything-claude-code)
  — hackathon-winning repo containing 30 agents, 136 skills, and 60 commands;
  the most comprehensive single-repo Claude Code starter kit.
- [`wshobson/agents`](https://github.com/wshobson/agents) (25K★) — production
  subagent library covering specialized roles (researcher, coder, reviewer,
  planner) for multi-agent orchestration workflows.
- **`claude-squad`** (5.6K★) — terminal multiplexer for running multiple
  parallel Claude Code agents in the same session; each agent gets its own
  pane and git worktree.
- **`claude-subconscious`** (2.4K★) — memory agent that runs in the
  background and automatically surfaces relevant past context into the active
  session without the user prompting for it.

Paste-ready prompts from this batch:

**Layer 1 — CLAUDE.md Audit (@appmillers):**

> Audit my instructions against Anthropic's current guidance and tell me what to delete. 1. FETCH THE LIVE RULES FIRST. Read Anthropic's page for my exact model. 2. GO LINE BY LINE. One verdict each: DELETE, KEEP or REWRITE, with the reason. 3. QUOTE YOUR SOURCE. No quote from Anthropic, the verdict is KEEP. 4. FLAG EVERY VERIFY-TWICE RULE. It self-corrects. I pay twice. 5. NEVER TOUCH A TRUTH RULE. "Only claim what you verified" stays. 6. TELL ME WHAT IS MISSING. Then a table, one row per instruction, the honest count, and anything unchecked marked NOT RUN.

**Layer 2 — Skills Audit (@appmillers):**

> Audit my skills folder for overlap and dead weight. Do not delete anything. 1) LIST EVERY SKILL with its name and one line on what it does. 2) GROUP THEM BY THE JOB they do, not by their name. Same job, same skill. 3) FOR EACH GROUP OF TWO OR MORE, which to keep and exactly what the others miss. 4) FLAG EVERY SKILL I have never actually used. 5) FLAG EVERY SKILL that only works because of a file that no longer exists. Then give me ONE merged version of the biggest group, written out in full. Tell me what I lose by merging.

**Layer 3 — Hooks Audit (@appmillers):**

> Audit every hook I have set up. Do not change or delete anything. 1. LIST THEM ALL. What triggers it, when it fires, what it does. Plain English. 2. WHICH ONES FIRE ON EVERY MESSAGE. Those are the expensive ones. 3. ANY TRIGGER WORD TOO COMMON. It will fire when I did not mean it. 4. ANY TWO THAT COULD FIRE AT ONCE, and what happens when they do. 5. ANY POINTING AT A FILE or folder that no longer exists. 6. WHICH ONES I HAVE PROBABLY FORGOTTEN I set up. Then a table: keep, fix or remove, one line of reasoning each. Do not touch anything until I say so.

**Hook Discovery (@appmillers):**

> Help me work out what I should turn into a hook. Find what I ask for over and over in the same words. Tell me the phrase I say, what you should read the moment I say it, and whether it is unique enough. Top three, ranked.

**10 Marketing Prompts (@TheChatGPTMarketer):**

1. **Competitor Teardown** — Act as a competitive analyst. Analyze these websites [list URLs] and products [names] for this audience [segment]. Summarize each UVP in 25 words or less, compare pricing in a table, list top 5 customer complaints from reviews, and find 3 gaps we can target. Return in markdown with citation links.

2. **VOC Mining** — Act as a VOC miner. Use this raw feedback [paste text] to group comments into themes, give each a 3-word label and top quote, rank by frequency, and suggest one copy idea per theme. Return as a markdown table.

3. **Content Audit** — Act as a content auditor. Use this site map [link] and metrics CSV [file] to list every URL with its metrics, label each Keep/Refresh/Delete, and flag quick wins needing less than 2 hours. Return as a markdown CSV.

4. **Customer-Journey Map** — Be a lifecycle strategist for [product] targeting [persona]. Map the stages (Awareness, Consideration, Purchase, Onboarding, Retention, Expansion) with goals, key questions, objections, ideal content, and suggest one AI prompt per stage. Return as a table.

5. **Keyword Gap** — Be an SEO gap analyst. Compare my site [URL] to competitors [URLs] and find missing high-intent keywords (KD <40, 500+ volume), suggest a headline and brief for each, and score by traffic impact times ease. Return in markdown.

6. **Trend Scan** — Use Deep Research to scan the last 90 days in [industry] and return the top 3 trends (under 30 words each) with a supporting stat or quote (linked) and a B2B marketing action idea for each, formatted as bulleted markdown.

7. **Attribution Check** — Act as an attribution analyst. Combine this ad spend CSV, CRM revenue CSV, and GA4 channel report to calculate ROAS and CAC, find channels with over 30% attribution inflation (last-touch vs multi-touch), and recommend budget shifts. Return summary and table.

8. **A/B Backlog** — Act as an experiment planner. Using funnel metrics (steps, conversion rates) and past tests, find biggest drop-offs, create 5 hypotheses per drop-off, score them on Impact, Confidence, Effort (ICE), and sort by total score. Return a markdown table ready for backlog.

9. **FAQ Build** — Act as a knowledge base builder. Using the top 100 support tickets and product docs, group questions by feature, write short FAQ answers (under 60 words), suggest related how-to article titles, and outline a site structure as a nested markdown list.

10. **Data Stories** — Be a PR writer. Using [internal stats] and [external datasets], find 3 headline-worthy insights with numbers, write a press-style headline and 2-sentence blurb for each, and suggest a chart (type and axes). Return as a markdown list.

### Reviewed and not added (38th batch)

- **`repomix`** (`yamadashy/repomix`) — already in README (Claude Code
  Tooling table, 34th addition area); skipped.
- **Microsoft Playwright MCP** — already integrated into the
  `claude-code-tooling` skill as one of its five browser-automation
  frameworks; skipped as a standalone entry.

---

**39th addition** (`674d3232-iCloud_Photos_1.zip`, 15 images, August 2026)
— Batch covers @mario_esquer_ "Turn Claude into a Money Printing Machine —
7 free repos" carousel and @aiemergence "Three frontier models dropped in
one day" 6-slide series. No new skills created (no prompt carousels).
`crewAIInc/crewAI` and `Mintplex-Labs/anything-llm` confirmed duplicates;
five new repos documented.

Repos identified in this batch (@mario_esquer_ carousel):

- [`pipecat-ai/pipecat`](https://github.com/pipecat-ai/pipecat) (14K★) —
  open-source framework for voice agents, multimodal apps, and realtime AI;
  maintained by Daily. Plug Claude in as the brain and it handles inbound
  calls, appointment booking, and calendar updates — a receptionist that
  never sleeps.
- [`cline/cline`](https://github.com/cline/cline) (66K★) — autonomous
  coding agent available as a VS Code extension, SDK, or CLI; hands Claude
  the keyboard and lets it build a whole site file by file while you watch.
- [`gitroomhq/postiz-app`](https://github.com/gitroomhq/postiz-app) (35K★)
  — the ultimate agentic social media scheduling tool; write a month of
  posts in Claude then fire them at every channel on schedule. MIT license.
- [`browser-use/browser-use`](https://github.com/browser-use/browser-use)
  (109K★) — makes websites accessible for AI agents; Claude opens a real
  browser and clicks through repetitive tasks a human does every day.
  Python library, MIT license.
- [`firecrawl/firecrawl`](https://github.com/mendableai/firecrawl) (168K★)
  — context API to search, scrape, and interact with the web at scale; turns
  any website into clean structured data and feeds it straight to Claude for
  lead generation, research, or data pipelines.

Informational only (no repos to install):

- @aiemergence "Three frontier models dropped in one day" — comparison of
  Grok 4.6 ($2/$6/M tokens, best agentic coding, best in Cursor), Qwen 3.8
  Max ($2/$6, 2.4T params / 95B active MoE, open weights, self-hostable),
  and DeepSeek V4 Pro 0813 (cheapest option, strongest agentic coding
  update, weights on Hugging Face). Useful model-selection heuristic:
  speed+agents → Grok, control+ownership → Qwen, cost → DeepSeek.
- "Everything you must know in Claude" wheel infographic — covers the 6
  dimensions: where to open it, which model to pick, effort levels, work
  modes (Chat/Cowork/Claude Design/Projects/Claude Code), output types
  (Artifacts/Real Files/Live Artifacts), and connectors/memory/skills.

### Reviewed and not added (39th batch)

- **`crewAIInc/crewAI`** — already in README (line 984, 28th addition
  area); skipped.
- **`Mintplex-Labs/anything-llm`** — already in README (line 1318, Plugins
  section); skipped.

---

**40th addition** (`9c8dd4c3-iCloud_Photos_1.zip`, 8 images, August 2026)
— Single 7-slide carousel from @iunlockedai "AI Unlocked Tool Drop 40"
covering `dmmulroy/anti-slop`. No prompts; one new repo.

Repo identified:

- [`dmmulroy/anti-slop`](https://github.com/dmmulroy/anti-slop) (1.7K★,
  MIT, Aug 2026) — 15 opinionated Oxlint rules that reject low-evidence
  TypeScript and JavaScript patterns produced by AI agents. Key distinction:
  most tools (CLAUDE.md, skills, system prompts) try to coach the model
  *before* it writes; this linter runs *after*, on the file that actually
  exists, and doesn't care how confident the model sounded. Install vendors
  the rules directly into your repo (no upstream dependency, but also no
  upstream fixes): `npx skills add dmmulroy/anti-slop --skill install-anti-slop`.
  Patterns it rejects: double casts (`x as object as T`), `Reflect.get` on
  `object` by string key, functions returning `unknown`, and type assertions
  with no `SAFETY:` comment explaining what was verified. In a 28-line demo
  of typical agent output, running `npx oxlint` with ten rules on caught 11
  errors — every one of them compiles fine and proves nothing.

---

**41st addition** (`f325b067-iCloud_Photos_1.zip`, 7 images, August 2026)
— Two separate carousels: (1) an anonymous infographic listing 50 marketing
use-case one-liners (informational only, no repos or prompts to extract);
(2) @appmillers "30 Things to Install in Claude" by Elshad Karimov
(www.appmillers.com), 5-slide categorical breakdown of 30 repo names.

**Caveat on the @appmillers carousel**: all 30 entries are given as short
"nickname" names only (no GitHub org prefix), and the star counts displayed
(e.g. 270.7K for "superpowers", 239.4K for "ECC", 168K for "claude-skills")
are wildly higher than any real repos carry — this is a stylized marketing
presentation, not a live GitHub snapshot. Items below require manual
owner/org lookup before installing.

**Duplicate-check against existing README** — already covered, skipped:

| Carousel name | Already in README / skills |
|---|---|
| `gstack` | 39th addition (garrytan/gstack) |
| `karpathy-skills` | 38th addition (andrej-karpathy-skills) |
| `repomix` | Earlier additions |
| `firecrawl` | 39th addition |
| `caveman` | Skills folder |
| `playwright-mcp` | claude-code-tooling skill |
| `taste-skill` | 38th addition (Leonxlnx/taste-skill) |
| `claude-hud` | 36th addition (jarrodwatts/claude-hud) |
| `claude-code-router` | Plugin table (musistudio/claude-code-router) |
| `codex-plugin-cc` | Plugin table (openai/codex-plugin-cc) |
| `best-practice` | 36th addition (shanraisshan/claude-code-best-practice) |
| `superpowers` | Plugin table (obra/superpowers-marketplace) |
| `agents` | 40th addition context (wshobson/agents) |
| `claude-skills` | Plugin table (alirezarezvani/claude-skills, uncertain) |

**New entries identified** (short names only — GitHub org unknown; verify before installing):

*Harness:*
- `ECC` — described as "tunes the whole harness for speed"; likely an
  Enhanced/Efficient Claude Code CLAUDE.md variant; no verified repo found
- `ponytail` — "forces short, one-line replies"; appears to be a
  response-length constraint CLAUDE.md or skill; no verified repo found
- `learn-claude-code` — "a tiny harness, built to read"; beginner-oriented
  CLAUDE.md scaffold; no verified repo found

*Skills:*
- `ui-ux-pro-max` — "palettes and fonts that just work"; UI/UX design-system
  skill bundle; no verified repo found
- `awesome-claude-skills` — "the curated list of every skill"; analogous to
  [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
  but skill-focused; no verified repo found (note: `awesome-claude-code` is
  already in this README)
- `claude-plugins` — described as "Anthropic's own plugin directory"; likely
  refers to the official plugin marketplace, which is browsed via
  `claude plugin marketplace` in an interactive session rather than a
  standalone repo

*Memory:*
- `graphify` — "turns a codebase into a map"; graph-based code-understanding
  tool; no verified repo found
- `claude-mem` — "keeps context across every session"; persistent memory
  layer; no verified repo found
- `codegraph` — "indexes your code, syncs itself"; code-index MCP/skill; no
  verified repo found
- `planning-with-files` — "planning that survives a restart"; file-backed
  planning persistence; no verified repo found

*Tools:*
- `cc-switch` — "switch models without leaving Claude"; in-session model
  switcher; no verified repo found
- `awesome-mcp-servers` — "every MCP server, in one list"; curated MCP
  catalog; the canonical real-world equivalent is
  [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
  (browse-only, not installable itself)
- `multica` — "one issue, twenty agents"; multi-agent parallelism orchestrator;
  no verified repo found
- `github-mcp` — "reads and writes your GitHub"; GitHub MCP server; the
  verified equivalent is the official
  [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
  GitHub connector, or `@modelcontextprotocol/server-github` via npm
- `vibe-kanban` — "a board for what your agents do"; agent task-tracking
  kanban; no verified repo found

*Cost:*
- `system-prompts-ai` — "the real system prompts, collected"; compiled
  leak/reverse-engineered system prompts from major AI products; no verified
  repo found (numerous community collections exist under different names)

No skills, commands, or agents were created from this batch — the carousel
names lack the org prefixes needed to resolve real install paths, and the
star-count inflation confirms this is illustrative content rather than a
verified registry. The 50-marketing-use-cases infographic contained no
actionable repo or prompt data.

---

**42nd addition** (`afa3386e-iCloud_Photos_1.zip`, 14 images + 2 MP4s, August 2026)
— Four distinct content sources: (1) @ux_snacks UX course ad; (2) VAMSHI.WORK
"10 UX Laws Explained Visually" carousel; (3) two @51ultron infographics;
(4) @adentech_hq MS-900 cloud exam content. One new skill created.

**Content breakdown:**

- **@ux_snacks UX course ad** — promotional image for a 510-page UX/UI
  playbook (2000+ students). Informational only.

- **VAMSHI.WORK "10 UX Laws Explained Visually"** (TikTok: @ux_snacks, 11
  slides) — visual explainers for ten cognitive/design psychology laws
  with before/after UI examples: 01 Jakob's Law (familiarity reduces
  friction); 02 Hick's Law (less choice = faster decisions); 03 Fitts's Law
  (target size/distance); 04 Miller's Law (working memory chunks of 7±2);
  05 Proximity Law (closeness implies relationship); 06 Von Restorff Effect
  (different element gets remembered); 07 Serial Position Effect (first/last
  remembered best); 08 Tesler's Law (product absorbs complexity); 09 Doherty
  Threshold (fast feedback keeps users engaged); 10 Peak-End Rule (people
  judge by peak + end moment). No repos — pure UX reference content.

- **@adentech_hq "MS-900 Deep Dive Part 3 — Cloud Service Models"** — exam
  prep infographic comparing IaaS/PaaS/SaaS (who manages what, scenarios,
  examples). Microsoft certification study content. No repos, no prompts.

- **@51ultron "How Claude Dreams"** — fictional/creative visualization
  claiming Claude consolidates memories overnight. Not a real Claude feature
  (Claude has no persistent memory between conversations by default, and no
  "dreaming" process). Informational/entertainment only.

- **@51ultron "5 Claude Folders For Client Acquisition"** — 5-folder system
  containing 50 described Claude skills organized by sales pipeline stage:
  Client & Market Intelligence (9 skills), Prospecting & Lead Intelligence
  (10 skills), Outreach & Conversation Starters (10 skills), Sales Conversion
  (10 skills), Pipeline & Acquisition Optimisation (10 skills). Named skills
  include ICP Architect, Pain Point Intelligence Builder, Buying Signal
  Detector, Personalised Opener Writer, Objection Handler, Proposal Writer,
  Win-Loss Analyst, and others. No GitHub source — described as a Claude
  Projects folders system.

**Skill created:**

- **`client-acquisition-skills`** — vendored from @51ultron's "5 Claude
  Folders For Client Acquisition" system. Contains 16 paste-ready prompts
  across the 5 acquisition stages, expanded from the named skills shown in
  the carousel (ICP Architect, Pain Point Intelligence Builder, Buyer Language
  Extractor, Competitive Positioning Analyst, Ideal Prospect Finder, Buying
  Signal Detector, Lead Scoring Expert, Account Prioritiser, Personalised
  Opener Writer, Icebreaker Strategist, LinkedIn Message Writer,
  Multi-Channel Outreach Planner, Objection Handler, Value Proposition
  Builder, Proposal Writer, Negotiation Assistant, Pipeline Health Checker,
  Follow-Up Strategist, Win-Loss Analyst, Acquisition Optimiser).
  Stored at `.claude/skills/client-acquisition-skills/SKILL.md`.

---

**43rd addition** (`356d1e2e-iCloud_Photos_1.zip`, 19 images + 1 MP4, August 2026)
— Batch covers two multi-slide carousels (@theromanknox "Hermes Agent QuickSilver
Revolution" 8-slide series; @iunlockedai "AI Unlocked Tool Drop #42" 8-slide
deepseek-harness analysis), one @51ultron 9-step business-launch infographic,
and one @aiemergence "Best AI Tools for Marketing in 2026" pyramid.

**Repo documented (developer preview — do not install for production):**

- **[`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness)**
  (154k★, MIT, official deepseek-ai org) — Plugin-based open agent harness;
  "Everything is a Plugin" (models, tools, sessions, sandboxes, storage, agent
  loop all load as plugins); model-agnostic with Anthropic adapters. First
  commit dated 2026-06-10; made public 2026-08-13 (69-day-old project, not a
  five-day build). Try with: `npx @deepseek-ai/dsh web` → http://127.0.0.1:3080.
  **⚠️ Currently `v0.1.0-rc.7` developer preview — repo README warns in caps
  "THERE WILL BE COMPATIBILITY-BREAKING CHANGES." Use to preview agent tooling
  direction; do not move production workflows onto it yet.** Also: 1,491+
  squatter repos share the name "deepseek-harness" — always verify the owner
  is `deepseek-ai` before installing anything.

Informational only (no repos to install):

- **@theromanknox "Hermes Agent QuickSilver Revolution"** — 8-slide carousel
  for a paid product/service (skool.com/knox). Demonstrates five capabilities
  of the Quicksilver agent platform: Smart Approvals (a second model vets each
  command, stops asking about safe operations), Durable Background Jobs
  (results survive a restart), Delivery Ledger (failed replies get retried,
  not forgotten), Profile Routing (other people text the same bot; their
  memory stays separate), Per-Task Effort controls (Max/Ultra effort, pay only
  when it matters). Key workflow tips: drop a YouTube URL and say "study this,
  summarize it, store it" to build a queryable knowledge base; assign each
  team member a private Obsidian/agent profile via plain-English instruction;
  to borrow an expensive model for one turn only, say "use this model ONCE" or
  run `/model sol --once` then it auto-switches back. No GitHub source. No install.

- **@51ultron "How to use Claude to start a business"** — 9-step infographic
  framework: (1) Validate idea with Claude before building; (2) Create core
  files `about-me.md` + `brand-voice.md` for persistent context; (3) Build
  separate Claude Projects per business function (Strategy, Brand, Operations),
  each with its own system prompt; (4) Use Artifacts to produce business assets
  (pitch decks, homepages, email sequences); (5) Generate sales scripts and
  outreach sequences; (6) Connect tools via Claude Settings → Connectors
  (Gmail, Calendar, Notion, HubSpot, Slack, etc.); (7) Use Cowork for
  collaborative real document editing; (8) Use Claude Code to build the actual
  product; (9) Run a daily business brief to stay on track. No GitHub source.

- **@aiemergence "The Best AI Tools for Marketing in 2026"** — seven-layer
  pyramid tool survey. Bottom to top: Learning (NextWork) → General Assistants
  (Claude, ChatGPT, Perplexity, Gemini) → Research & Writing (NotebookLM,
  Grammarly, Notion, Wispr) → Design (Canva, Figma, Paper, Framer) → Dev &
  No-Code (Cursor, Lovable, Replit, v0, Bolt) → Automation & Data (Zapier,
  Make, n8n, Lindy, Apollo, PostHog, Apify) → Content & Media (HeyGen,
  Descript, Opus Clip, Gamma, Beehiiv, Midjourney, Veo, Higgsfield,
  ElevenLabs, Suno). Informational tool survey only; no repos, no prompts.

**Skill created:**

- **`claude-start-business`** — vendored from @51ultron's 9-step "How to use
  Claude to start a business" framework. Contains 9 paste-ready prompts: Step 1
  (Validate the Idea), Step 2 (Create Core Files — about-me.md + brand-voice.md),
  Step 3 (Build Claude Projects by Function with system prompts for Strategy /
  Brand / Operations), Step 4 (Create Business Assets with Artifacts), Step 5
  (Sales Scripts and Outreach), Step 6 (Connect Your Tools), Step 7 (Cowork on
  Real Documents), Step 8 (Build the Product with Claude Code), Step 9 (Daily
  Business Brief). Stored at `.claude/skills/claude-start-business/SKILL.md`.

---

**44th addition** (`3df70276-iCloud_Photos_1.zip`, 42 JPEGs + 1 PNG + 1 MP4, August 2026)
— Batch covers five carousels and two informational slides: @ty.prompts.ai "5 free
repos from the agent harness war" (7 slides); @ai.blueprint "5 AI agents that
actually make money" (7 slides); @replace.so "3 GitHub repos so good they
shouldn't be free" (excalidraw + langflow identified); @appmillers "5 Claude
Code Design Upgrades" (5 techniques); @your.aimentor "56 Commands for
Maximizing Claude Code Output" (56 prefix commands); @51ultron "Build an AI
Agent in 10 Minutes" (9 steps — distinct from claude-start-business skill).
Also: @the21.i Stripe–OpenRouter acquisition news (informational); @aiemergence
8-layer AI Agent Architecture diagram (informational); @wellx.tech 25 IT Project
Ideas (informational); @aisimplified23 Claude Functions Cheat Sheet
(informational).

**Repos documented (new — not previously in README):**

- **[`livekit/agents`](https://github.com/livekit/agents)** (11k★) — Python
  framework for building realtime voice AI agents; powers AI receptionists,
  voice assistants, and audio-interactive applications. Production-ready; used
  by @ai.blueprint as the "AI receptionist" money-making agent archetype.
  Install: `pip install livekit-agents`.

- **[`xai-org/grok-build`](https://github.com/xai-org/grok-build)** (26k★,
  4.8k forks) — xAI's full-screen terminal agent; implements the Agent Client
  Protocol (ACP) for standardised agent-to-agent communication. Drop-in for
  CLI-first workflows where Claude Code or Codex is used today.

- **[`andrewyng/openworker`](https://github.com/andrewyng/openworker)** (15k★,
  2.1k forks) — Andrew Ng's open-source desktop coworker agent; runs locally,
  controls the desktop GUI, executes multi-step agentic tasks. Clone and run
  per the repo README.

- **[`yc-software/qm`](https://github.com/yc-software/qm)** (14k★, 1.7k forks)
  — YC-backed multiplayer agent harness; single shared core drives Pi, OpenCode,
  Codex, and Claude Code concurrently. Designed for teams where multiple agents
  collaborate on the same codebase.

- **[`XiaomiMiMo/MiMo-Code`](https://github.com/XiaomiMiMo/MiMo-Code)** (13k★,
  1.3k forks) — Xiaomi's terminal-native coding agent with persistent memory;
  stores prior session context across runs. Fits workflows where state and
  project history must survive session restarts.

- **[`excalidraw/excalidraw`](https://github.com/excalidraw/excalidraw)**
  (★ high) — Open-source collaborative infinite-canvas whiteboard with a
  hand-drawn diagram aesthetic; runs entirely in the browser. Self-hostable;
  useful for async architecture diagrams, brainstorming boards, and shared
  visual planning without a SaaS subscription.
  Run locally: `npx excalidraw` or `docker run -p 80:80 excalidraw/excalidraw`.

**Repos confirmed duplicate (already in README — skipped):**

| Repo | First documented |
|---|---|
| `langgenius/dify` | 28th addition (line 983) |
| `langflow-ai/langflow` | 28th addition (line 984) |
| `crewAIInc/crewAI` | 28th addition (line 984) |
| `firecrawl/firecrawl` | 39th addition |
| `deepseek-ai/deepseek-harness` | 43rd addition |
| `n8n-io/n8n` | prior batch |

**Skills created:**

- **`your-aimentor-56-commands`** — full set of 56 prefix commands from
  @your.aimentor, grouped into four categories: Role & Persona (1–14: /human,
  /expert, /ceo, /viral, /seo, /critic, /teacher, /eli5, /brief, /strategy,
  /copywriter, /research, /brainstorm, /promptengineer), Problem-Solving &
  Productivity (15–28: /problemsolver, /decisionhelper, /moneyideas,
  /skillbuilder, /negotiationcoach, /contentoptimizer, /promptimprover,
  /emailwizard, /productivityboost, /socialmediaai, /storytellerai,
  /persuasivemode, /datainterpreter, /automateit), Career & Personal Development
  (29–42: /jobinterviewer, /careercoach, /resumewriter, /coverlettergen,
  /linkedinbooster, /personaldeveloper, /habittracker, /healthcoach,
  /mealplanner, /workoutbuddy, /travelplanner, /budgetplanner, /financetips,
  /booksummary), Growth & Marketing (43–56: /trendpredictor, /deepthink,
  /unpopularopinion, /growthhack, /contentrecycler, /ctaexpert, /psychowords,
  /brandstory, /viralhook, /audienceavatar, /competitorroast, /frameworkify,
  /examplewizard, /tl;dr). Stored at
  `.claude/skills/your-aimentor-56-commands/SKILL.md`.

- **`appmillers-claude-code-design-kit`** — 5-technique Claude Code design
  upgrade kit from @appmillers: (01) TASTE SKILL — feed premium references to
  calibrate first-draft aesthetics; (02) WEB DESIGN GUIDELINES AUDIT — audit
  against Vercel's Web Interface Guidelines for usability/accessibility/
  consistency; (03) AWESOME DESIGN.md — create a project-level DESIGN.md
  capturing colours, typography, spacing, buttons, components, and motion so
  every session stays in-system; (04) IMAGE TO CODE — drop a screenshot and
  Claude generates high-fidelity matching components; (05) PLAYWRIGHT CLI LOOP
  — give Claude eyes via build → screenshot → inspect → fix feedback loop using
  `npx playwright screenshot`. Stored at
  `.claude/skills/appmillers-claude-code-design-kit/SKILL.md`.

- **`build-ai-agent-10-minutes`** — @51ultron's 9-step framework for building
  and running a personal Claude Code agent system (distinct from
  `claude-start-business` which covers launching a *business*; this skill covers
  building the *agent itself*): Step 1 Install Claude Code; Step 2 Build context
  (CLAUDE.md); Step 3 Build memory (corrections.md + preferences.md persistent
  files); Step 4 Refine prompts (iterative prompting with structured critique);
  Step 5 Build skills (SKILL.md packaging); Step 6 Test & iterate (structured
  quality scoring); Step 7 Multi-agent architecture (Strategist Opus →
  Builder Sonnet → QA Gate 95/100); Step 8 Autopilot (Claude Routines as cron);
  Step 9 Scale & deploy (document, parameterise, onboard, harden, package).
  Stored at `.claude/skills/build-ai-agent-10-minutes/SKILL.md`.

---

**45th addition** (`57efd9a4-_____________.zip`, 55 images, August 2026)
— Batch spans accounts including @zhiprompts, @dupodev, @ai_slacker,
@webnailed, @replace.so, @ty.prompts.ai, @iunlockedai, @51ultron,
@finitopotatoes, @njugunalucy0, @codez_dev, @engeldata, and @entrp0.
Two new skills were created and six new repos were identified (all
checked against the existing README — zero duplicates):

**New skills created:**

- **`claude-marketing-8-frameworks`** — eight acronym-based marketing
  prompt frameworks: ANGLE (Audience/Need/Gap/Language/Edge — positioning),
  CLAIM (Context/Lure/Ache/Impact/Motion — offer/conversion copy), FLOW
  (Focus/Line/Offer/Warmth — content narrative), RAMP (Reach/Angle/
  Milestones/Push — campaign planning), KNOW (Known/Needs/Obstacles/Wants —
  buyer psychology), VALUE (Vehicle/Audience/Length/Upside/Evidence —
  content strategy), VOICE (Values/Overtone/Inclusions/Cuts/Examples —
  brand voice), PATH (Problem/Action/Trust/Hand-off — sales sequences).
  Each framework ships as a fill-in-the-bracket prompt. Includes a
  quick-selection guide and a full-brief chaining sequence
  (KNOW → ANGLE → CLAIM → PATH → FLOW → RAMP). Stored at
  `.claude/skills/claude-marketing-8-frameworks/SKILL.md`.

- **`ai-slacker-premortem`** — two adversarial premortem prompts from
  @ai_slacker: "The Adversary" (play the competitor who benefits most
  from your plan failing — where they'd attack, what they'd do the week
  you launch, the move you'd never see coming) and "The Verdict" (from
  the failure list, name the Most Likely vs Most Dangerous failure and
  explain why they differ, then surface the single hidden assumption
  that could be fatal). Packaged as a full 3-step sequence: generate
  failure modes → run The Adversary → run The Verdict. Stored at
  `.claude/skills/ai-slacker-premortem/SKILL.md`.

**Repos identified in this batch (not previously in README):**

- **[`composio-dev/composio`](https://github.com/composio-dev/composio)**
  — Tooling platform connecting AI agents and LLMs to 1,000+ tools and
  MCP servers via a single integration layer; manages auth, retries, and
  tool discovery. Actively maintained.

- **[`mastodon/mastodon`](https://github.com/mastodon/mastodon)**
  (50k★, Ruby) — The official Mastodon server. Self-hosted federated
  microblogging platform (ActivityPub); a real alternative to X/Twitter
  for community-owned social.

- **[`discourse/discourse`](https://github.com/discourse/discourse)**
  (48k★, 9.0k forks, Ruby) — Open-source discussion platform. Use when
  discussion, searchable answers, and moderation justify a dedicated
  forum rather than a Slack/Discord community.

- **[`directus/directus`](https://github.com/directus/directus)**
  (37k★, TypeScript) — Open data platform and headless CMS. Wraps any
  SQL database with a real-time API and a no-code app for managing
  content and assets across channels.

- **[`InternLM/InternLM`](https://github.com/InternLM/InternLM)**
  (7.3k★, Apache 2.0) — InternLM series of LLMs from Shanghai AI Lab;
  strong multilingual (Chinese/English) reasoning. Open-weights, self-
  hostable via Ollama or LocalAI.

- **[`btcpayserver/btcpayserver`](https://github.com/btcpayserver/btcpayserver)**
  (7.7k★, C#, MIT) — Self-hosted, open-source Bitcoin payment processor.
  Accepts BTC and Lightning Network payments with no third-party
  dependency, no fees, no KYC.

**Tools/references (no install, documented for completeness):**

- **Worklenz** (worklenz.com) — Open-source project management platform
  (tasks, time tracking, resource management, client portal). Likely
  `Worklenz/worklenz` on GitHub — verify before cloning.
- **Aceternity UI** (ui.aceternity.com) — React component library with
  premium animated/glassmorphic UI components.
- **unDraw** (undraw.co) — Free MIT-licensed SVG illustration library,
  color-customizable via URL parameter.
- **Glassmorphism generator** — CSS glassmorphism/frosted-glass effect
  generator; several at `ui.glass/generator` and similar.
- **JSON Crack** (jsoncrack.com) — Visualizes JSON/YAML/CSV/XML/TOML as
  interactive graphs; free web tool.
- **DevDocs** (devdocs.io) — Unified offline-capable docs browser
  aggregating documentation for 100+ languages and frameworks.
- **Plasmic** — Open-source visual page builder and CMS; design in a
  Figma-like canvas and output React/HTML. Core is open-source.
- **FFMPEG pipeline for content** (@finitopotatoes Claude Code Skill
  5/5) — Claude Code scripting the full FFmpeg pipeline: resize video
  for TikTok/Reels/Shorts (9:16), Instagram (1:1), and YouTube (16:9);
  burn captions; cut clips; export clean. Best for repurposing demos,
  podcasts, and clips.

Paste-ready prompts from this batch:

**8 Claude Marketing Frameworks (now in `claude-marketing-8-frameworks`):**

**ANGLE — Positioning & Differentiation**
> Audience: [who you're speaking to] / Need: [core problem or desire] / Gap: [what the market misses] / Language: [words and tone they use] / Edge: [your unique differentiator]
> "Using this ANGLE framework, write a positioning statement and tagline for [product/brand]."

**CLAIM — Offer & Conversion Copy**
> Context: [situation the reader is in] / Lure: [hook or promise] / Ache: [painful problem] / Impact: [transformation after your offer] / Motion: [call to action]
> "Using this CLAIM framework, write [landing page headline + subhead / email subject + opener / ad copy] for [product/service]."

**FLOW — Content & Narrative Structure**
> Focus: [single idea] / Line: [opening hook] / Offer: [value or next step] / Warmth: [human/emotional tone]
> "Using this FLOW framework, write a [LinkedIn post / email / short-form video script] about [topic]."

**RAMP — Campaign & Growth Planning**
> Reach: [channels and audiences] / Angle: [campaign concept] / Milestones: [3–4 checkpoints] / Push: [amplification tactics]
> "Using this RAMP framework, build a [30-day / 90-day] campaign plan for [product/launch/event]."

**KNOW — Audience Research & Messaging**
> Known: [what audience already believes] / Needs: [functional requirements] / Obstacles: [what stops them buying] / Wants: [emotional desires]
> "Using this KNOW framework, map the full buyer psychology for [target customer] and rewrite [headline / email / sales page] to speak directly to it."

**VALUE — Content Strategy & Proof**
> Vehicle: [content format] / Audience: [who will see this] / Length: [word count or duration] / Upside: [main benefit] / Evidence: [proof points]
> "Using this VALUE framework, outline and draft a [content piece] about [topic] for [platform]."

**VOICE — Brand Voice & Style Guide**
> Values: [2–3 core brand values] / Overtone: [emotional register] / Inclusions: [words/phrases to use] / Cuts: [words/tones to avoid] / Examples: [1–2 correct examples]
> "Using this VOICE framework, define the brand voice for [brand/product] and rewrite [sample text] in that voice."

**PATH — Sales & Nurture Sequences**
> Problem: [specific problem prospect is stuck on] / Action: [first small action] / Trust: [how you demonstrate credibility] / Hand-off: [natural next step]
> "Using this PATH framework, write a [3-email / 5-email] nurture sequence for [product/service] starting from [entry point]."

**@ai_slacker Premortem Prompts (now in `ai-slacker-premortem`):**

**Generate failure modes first:**
> "Assume my plan has failed completely — 12 months from now, it did not work. List the 7 most likely reasons it failed, ranked by probability. For each: one sentence on what went wrong and one sentence on the early warning sign I should have caught. My plan: [paste your plan here]"

**The Adversary:**
> "Now play the person who benefits most from my plan failing. A competitor, a rival, someone who wants my spot. You've seen my plan. Tell me exactly where you'd attack it, what you'd do the week I launch, and the move I'd never see coming."

**The Verdict:**
> "From those 7 failures, tell me which is MOST LIKELY and which is MOST DANGEROUS, and explain why they're different. Then name the single biggest hidden assumption I'm making that I don't realise is an assumption. Be blunt. If my plan has a fatal flaw, say the words."

Most other content in this batch was informational: Claude Code version notes
(@iunlockedai — fork-mode default in v2.1.232, Tool Drops 34/35, security
fix), dashboard UI showcases (@codez_dev), n8n certificate-automation
workflow finale (@njugunalucy0 slide 9/9), Chinese LLM comparison
(@engeldata — Qwen model selection), Perplexity-as-research-tool tips
(@entrp0), and Anthropic product/course announcements.

---

### 46th addition — local LLMs, open-source business tools & complete premortem skill

**Repos cloned / registered:**

**Local LLMs (from @ty.prompts.ai carousel, slides 2–5):**
- `QwenLM/Qwen3` — Alibaba's Qwen3 family: 27B and 35B-A3B sizes, also Qwen3.5 line down to 0.8B; Apache 2.0; 3.8k★
  `git clone https://github.com/QwenLM/Qwen3`
- `deepseek-ai/DeepSeek-R1` — MIT; 92k★, 12k forks; distilled versions: 1.5B, 7B, 8B, 14B (gaming GPU), 32B
  `git clone https://github.com/deepseek-ai/DeepSeek-R1`
- `OpenBMB/MiniCPM-V` — 26k★; multimodal (image + video) pocket LLM; 1.3B params deploys on iOS/Android/HarmonyOS
  `git clone https://github.com/OpenBMB/MiniCPM-V`
- `OpenBMB/MiniCPM` — 10k★; Apache 2.0; SOTA 1B on-device text LLM
  `git clone https://github.com/OpenBMB/MiniCPM`

**Open-source business tools (from @replace.so "6 free GitHub repos" carousel):**
- `Brightbean-studio` — self-hostable social-media platform: compose, schedule, publish, approve, analyse across 10+ networks; "Free Forever"
  `git clone https://github.com/Brightbean-studio/Brightbean-studio`
- `Talivia` — self-hosted revenue analytics: web tracking, session replay, payment integrations, first/last-touch attribution
  `git clone https://github.com/talivia-analytics/talivia`
- `Note-gen` — local-first, cross-platform (Windows/macOS/Linux/Android/iOS) Markdown notes + AI organisation; "Capture first, organise later"; 12.6k★
  `git clone https://github.com/codexu/note-gen`
- `Leantime` — open-source project management for the non-project manager; built with ADHD and neurodivergence in mind; behavioural-science + AI
  `git clone https://github.com/Leantime/leantime`
- `Ever-gauzy` — open business-management platform: ERP, CRM, HRM, ATS, PM in one self-hosted suite
  `git clone https://github.com/ever-co/ever-gauzy`
- `APITable` — open-source collaborative database-spreadsheet: structured workspaces, forms, dashboards, automations, low-code apps; 10k★
  `git clone https://github.com/apitable/apitable`

**Skills updated / installed:**

- `ai-slacker-premortem` — **updated** with the complete 5-prompt sequence (Slide 1: The Premortem Prompt / forensic failure analyst; Slide 2: The Verdict / most-likely vs most-dangerous + hidden assumption; Slide 3: The Rebuild / rewrite with failures closed + pre-launch checklist; Slide 4: The Adversary / competitor attack angle; Slide 5: The Tripwire / measurable signals by week). Previous install had only Slides 2 and 4.

Most other content in this batch was informational: @iunlockedai Claude Code
token-cost breakdown (4-type pricing, cache-read math) and fork-vs-subagent
comparison; @finitopotatoes Claude Code skills series slides (Motion 4/5);
@entrp0 Gamma tool slide; @zhiprompts creator distribution strategy cover;
@engeldata local agentic AI system cover; @njugunalucy0 n8n certificate
workflow steps 7–8/9.

---

### 47th addition — open-source project management, minimalist publishing & finance AI prompts

**Repos cloned / registered:**

- `makeplane/plane` — open-source project management platform: work items, cycles, modules, roadmaps, AI-powered workflows; cloud, self-hosted, and air-gapped ready
  `git clone https://github.com/makeplane/plane`
- `WriteFreely/writefreely` — open-source minimalist publishing platform; focused blog readers can visit directly; 5.2k★, Go, 385 forks
  `git clone https://github.com/WriteFreely/writefreely`
- `opf/openproject` — open-source project management software: planning, tracking, Gantt charts, agile boards, roadmaps, and team tools
  `git clone https://github.com/opf/openproject`

**Skills installed:**

- `finance-ai-prompts` — 20 AI prompts for FP&A and accounting professionals: Excel Formulas, Create PPT with AI, Python Analysis, Deep Research, Financial Analysis, Scenario Analysis, Budget Instructions, Set Up Action Plan, Financial Statement Notes, Scenario Modeling, ROI Analysis, Write Email Request, Advanced Modeling, Scenario Planning, Cash Flow Projection, Dunning Process, Cost Reduction, Interview Preparation, Commentaries with AI, Create an SOP.

Most other content in this batch was informational: @iunlockedai Claude Code
changelog (v2.1.228/229 — hardened skills, Write tool update,
/commit-push-pr safety); @iunlockedai token cost tip (fewer restarts, smaller
context = lower usage); @engeldata Lovable→GitHub→Vercel agentic AI workflow
and local testing tip; @njugunalucy0 n8n certificate automation steps 3–4/9
(Set data node + IF node); @webnailed DevDocs and JSON Crack (both already in
README). JSON Crack (AykutSarac/jsoncrack.com) was skipped — already listed
under `design-dev-resources`.

---

### 48th addition — offline-resilience tools, AI video production repos, personal development & Claude prompt shortcuts

**Repos cloned / registered:**

**Offline Resilience (from @ty.prompts.ai "offline tools" carousel):**
- `Crosstalk-Solutions/project-nomad` — 36k★; peer-to-peer offline knowledge server; works without internet
  `git clone https://github.com/Crosstalk-Solutions/project-nomad`
- `markqvist/Reticulum` — 7k★; cryptographic networking stack designed for no-internet/mesh environments; works over radio, LoRa, serial links
  `git clone https://github.com/markqvist/Reticulum`
- `off-grid-ai/OGAM` — 3k★; MIT; offline AI assistant manager; run LLMs entirely without internet
  `git clone https://github.com/off-grid-ai/OGAM`
- `kylecorry31/Trail-Sense` — 2.8k★; Android app for offline navigation and survival tools; GPS, compass, weather, tides — no data connection needed
  `git clone https://github.com/kylecorry31/Trail-Sense`
- `DSheirer/sdrtrunk` — 2.2k★; cross-platform Java app for decoding, monitoring, recording, and streaming trunked radio protocols via Software Defined Radio (SDR); works when towers and wifi are gone
  `git clone https://github.com/DSheirer/sdrtrunk`

**AI Video Production (from @ty.prompts.ai "AI video repos" carousel):**
- `HKUDS/ViMax` — 12k★; MIT; agentic video generation — runs director, screenwriter, producer, and generator as one agent; has a research paper behind it
  `git clone https://github.com/HKUDS/ViMax`
- `HBAI-Ltd/Toonflow-app` — 14k★; Apache 2.0; AI animated drama maker; one-click character-consistent story video generation
  `git clone https://github.com/HBAI-Ltd/Toonflow-app`
- `Forget-C/Jellyfish` — 6k★; end-to-end production workspace for AI-generated short dramas; centrally manages character, scene, prop, and costume consistency to prevent drift between shots
  `git clone https://github.com/Forget-C/Jellyfish`
- `MemeCalculate/moyin-creator` — 4.3k★; AI film production pipeline — script → character → scene → director, all feeding into Seedance 2.0 (the model behind TikTok's free AI video generator); no manual handoff between steps
  `git clone https://github.com/MemeCalculate/moyin-creator`
- `tin2tin/Pallaidium` — 1.5k★; generative AI video, image, and audio directly inside Blender's Video Sequence Editor; local production without leaving Blender
  `git clone https://github.com/tin2tin/Pallaidium`

**Skills installed:**

- `personal-development-prompts` — 11 life-improvement plan prompts from @martiendejong_dev: Focus & Productivity System, 30-Day Skill Accelerator, Social Media Growth Plan, 30-Day Fitness Blueprint, High-Energy Morning Routine, Sleep Reset Plan, Personal Finance Reset, Online Business Launch Plan, Stress Management Plan, Communication Skills Upgrade, Digital Detox Plan.
- `claude-prompt-shortcuts` — 50 Claude prompt shortcuts from @ti.prompts.ai, organized across 5 categories (Think / Plan / Create / Business / Execute) each with a slash-command format: `/mental model [topic]`, `/negotiate [situation]`, `/story [topic]`, `/prioritize [tasks]`, `/troubleshoot [code]`, and 45 more.

Most other content in this batch was informational: @zoout "8 jobs → 8 specialists"
carousel (N8N and Langflow already in README; OpenHuman, OpenCode, Qwen, Google
Stitch, NotebookLM — no repo slugs captured); @sakispapakos Greek channel
recommendation series (No Priors, Tina Huang, Sabrina Ramonov, Andrei Karpathy,
3Blue1Brown, Futurepedia, Ben AI — informational); @nswebdesign.gr JSON-LD/Schema
SEO tips (Greek content); @sovello.oy SaaS idea concepts (no repos); @aiemergence
"5 AI Tools to Replace Employees" (Superhuman, Ocoya, Sidekick, Durable, Motion —
commercial SaaS, no repos to clone).

---

### 49th addition — self-hosted productivity tools and a local-first AI notebook

**Repos cloned / registered:**

**Open-source self-hosted tools (from @replace.so "5 GitHub repos so good they shouldn't be free" carousel):**
- `Skyvern-AutoGPT/skyvern` — 22.7k★; Apache 2.0; AI browser automation using LLMs and computer vision; navigates websites by understanding their visual layout rather than brittle CSS selectors or XPaths
  `git clone https://github.com/Skyvern-AutoGPT/skyvern`
- `alainm23/planify` — 5.6k★; GPL-3.0; open-source GNOME task manager for GNU/Linux; integrates with Todoist and Google Tasks; supports boards, timeline, and scheduling
  `git clone https://github.com/alainm23/planify`
- `appsmithorg/appsmith` — 40.6k★; Apache 2.0; open-source low-code platform for building internal dashboards, admin panels, and CRUD apps; connects to any database or API
  `git clone https://github.com/appsmithorg/appsmith`
- `usememos/memos` — 62k★; MIT; self-hosted Markdown-native note-taking with a public timeline interface; lightweight, privacy-first, no vendor lock-in
  `git clone https://github.com/usememos/memos`
- `chrisvel/tududi` — 3.2k★; self-hosted productivity app combining tasks, projects, CalDAV calendar sync, and Telegram bot integration
  `git clone https://github.com/chrisvel/tududi`

**Open-source collaboration and note-taking (from additional @replace.so carousels):**
- `colanode/colanode` — 4.3k★; MIT; local-first open-source alternative to Slack + Notion combined; real-time collaboration without cloud lock-in
  `git clone https://github.com/colanode/colanode`
- `blinkospace/blinko` — 10.9k★; MIT; self-hosted AI note-taking app with natural-language search across notes; privacy-first with local storage option
  `git clone https://github.com/blinkospace/blinko`

**Local-first AI notebook (from @replace.so "6 free Github repos blew up this week" carousel):**
- `deta/surf` — 3.5k★; open-source; Deta Surf is a local-first AI notebook that brings files and webpages into your stream of thought; organizes sources and generates rich notes using user-selected models
  `git clone https://github.com/deta/surf`

Most other content in this batch was informational: @felix_builds_ai "5 tools for a $100k business" (Higgsfield, Ubserve, Wispr Flow, Perplexity — commercial SaaS, no repos); @mrsai119 color-palette design tips (8 slides, no repos); @FutureWithAI "Think of Claude Code as Two Dials" (model + effort selection guide — informational); @the.wealth.lab "30 Things to Install in Claude" (plugins/skills/MCPs listed by title only, no GitHub slugs); @appmillers "15 Claude non-negotiables" (skills, connectors, settings recommendations — informational); @AIEMERGENCE "Models I Can Work With On Their Own" (AI model trust-tier rankings — informational). Worklenz was skipped — already in README.

---

### 50th addition — local code intelligence graph and 1-click AI model runner; two prompt skills

**Repos cloned / registered:**

- `zzet/gortex` — 824★; Apache-2.0; Go; local code intelligence that converts a codebase into a queryable graph, reducing AI agent token usage by up to 50×; exposes 100+ MCP tools; parses 257 languages; single static binary, no network calls, supports Claude Code, Cursor, Copilot, Windsurf, Cline, Aider, and 12+ more
  Install: `curl -fsSL https://get.gortex.dev | sh`
  Usage: `gortex install && gortex daemon start --detach && gortex track ~/projects/myapp`

- `cocktailpeanut/pinokio` — "The 1-Click Localhost Cloud"; open-source browser that lets you install and run any open-source AI model locally with one click; no API costs, no cloud; supports Stable Diffusion, LLaMA, Whisper, and hundreds of community scripts
  `git clone https://github.com/cocktailpeanut/pinokio`

**Skills created:**

- `.claude/skills/brandarmor-coding-workflow/SKILL.md` — 4-step AI coding workflow from @brandarmor.ai (Plan/Attack/Build/Verify using two independent sessions so the builder never approves its own work)
- `.claude/skills/humanize-ai-writing-prompts/SKILL.md` — 8 prompts from @the.wealth.lab to strip AI writing patterns and restore a natural human voice

Most other content in this batch was informational: @lunktech Gortex features carousel (slides confirming Gortex MCP/agent integrations); @aigentsofficial "5 Free AI Tools" (Deepsite, Feedough, Google Open, Pinokio, Recraft — only Pinokio is open-source); @gwenleceo "How much does it cost to build a SaaS in 2026?" (Claude Code $100 + Makelead + Hostinger VPS + Stripe + Cloudflare R2 + Supabase ≈ $115/month — informational, all commercial SaaS); @easyclaw6 "10 AI Tools to Build a Business from Scratch in 2026" (Perplexity, ChatGPT/Claude, Framer/Carrd, Canva/Gamma, Notion/Airtable/Zapier — informational, commercial SaaS); @iunlockedai Claude Code v2.1.238 memory leak fix (informational).

---

### 51st addition — privacy/anti-surveillance repos, open-source task manager, AI watermark remover, and two Claude workflow skills

**Privacy & surveillance-pricing repos (from @ty.prompts.ai "5 free repos that hide you from surveillance pricing" carousel):**

- `AdguardTeam/AdGuardHome` — 36k★; network-wide DNS-level ad and tracker blocker; runs as a DNS server on your LAN so every device on the network is protected without per-device configuration; self-hosted, no cloud required
  `git clone https://github.com/AdguardTeam/AdGuardHome`

- `gorhill/uBlock` — 67k★; uBlock Origin for Chrome and Firefox; efficient, wide-spectrum content blocker; uses less memory than competing blockers; blocks ads, trackers, and malware domains
  `git clone https://github.com/gorhill/uBlock`

- `mozilla/multi-account-containers` — 3.1k★; Firefox Multi-Account Containers extension; isolates site cookies per container so sites can't track you across tabs; separate identities for work, personal, shopping, social
  `git clone https://github.com/mozilla/multi-account-containers`

- `arkenfox/user.js` — 13k★; Firefox hardened privacy configuration file; opinionated user.js that locks down browser fingerprinting, telemetry, and tracking; regularly maintained against Firefox changes
  `git clone https://github.com/arkenfox/user.js`

- `dgtlmoon/changedetection.io` — 33k★; best-in-class website change detection and price monitoring; point it at any product page and get alerted when price, stock, or content changes; self-hosted, no SaaS required
  `git clone https://github.com/dgtlmoon/changedetection.io`

**AI utility repos (from @will.ai.m "5 repos blowing up on GitHub — August 2026" carousel):**

- `mahlernim/google-timeline-visualizer` — 2,649★; Kotlin; converts your Google Maps location history export into a cinematic travel video with map overlays; local processing, no cloud upload
  `git clone https://github.com/mahlernim/google-timeline-visualizer`

- `guillaumemeyer/watermarks-remover` — 17,225★; Python; strips hidden AI watermarks embedded by Midjourney, DALL-E, Firefly, and others from generated images; batch-processing CLI
  `git clone https://github.com/guillaumemeyer/watermarks-remover`

- `vorssaint/vorssaint-utils` — 7,475★; Swift; single macOS menu-bar app that replaces a dozen paid Mac utilities: clipboard manager, window snapping, quick-launch, system stats, focus timer, and more
  `git clone https://github.com/vorssaint/vorssaint-utils`

**Open-source task manager (from @replace.so "Super Productivity" carousel):**

- `johannesjo/super-productivity` — open-source task manager for timeboxing work, tracking time, building habits, and syncing tasks across devices; offline-first, privacy-first, no cloud account required
  `git clone https://github.com/johannesjo/super-productivity`

**Skills created:**

- `.claude/skills/build-claude-ai-employee/SKILL.md` — 7-step methodology from @SkillDropAI to build a reusable Claude AI employee: Give It One Job → Add the Inputs → Add the Context → Force the Output → Test and Iterate → Save It As a Skill
- `.claude/skills/claude-anti-slop-stack/SKILL.md` — 10-rule design system from @futurewithai.dev to stop Claude from inventing generic UI: provide Figma references, feed a real design system, use design tokens, map existing components, build a feedback loop

Most other content in this batch was informational: @SkillDropAI "Build Your First Claude AI Employee" slides 2/7, 3/7, 5/7 (Give It One Job, Add The Inputs, Force the Output — captured in skill above); @wellx.tech "10 Rules to Ship Safe Apps" rule 06 "Cap the Blast Radius" (set usage caps and billing alerts on hosting, database, email, maps, and AI APIs — captured in skill); @futurewithai.dev "Claude Anti-Slop Stack" slides 04–07 (captured in skill above); @automatedigital email sorting workflow (Gmail Trigger → n8n → Claude → Gmail Labels — step-by-step n8n tutorial, no repo); @automatedigital multi-platform video repurposing workflow (YouTube → n8n → Claude → Buffer → LinkedIn — tutorial); @askyourdigitalagency "7 prompts to design a logo with Claude" (intro + promo slides only, actual prompts not visible); @lior "AI business ideas" (AI Small-Biz Lawyer, Reno Estimator, AI Agent Staffing, Self-Running Store — editorial); @emmadroid "Railway" deployment platform (commercial SaaS, no clone); @witonic2 "Obsidian" and "Mobbin" (commercial/no clone); @starterstory 10-step SaaS launch checklist (editorial); @AIEMERGENCE "5 Free AI Tools" (Deepsite, Feedough, Google Open, Pinokio, Recraft — Pinokio already in README, others are commercial SaaS); `harry0703/MoneyPrinterTurbo`, `deepseek-ai/deepseek-harness`, `cocktailpeanut/pinokio` — all already in README, skipped.

---

### 52nd addition — open-source tool alternatives, Claude Code workspace, self-training AI model, and three prompt skills

**Open-source tool alternatives spotted across this batch (primarily @emmadroid "Paid vs Free" carousel and others):**

- **Vikunja** (vikunja.io) — free open-source Todoist alternative; kanban + list + table views; CalDAV/CardDAV sync; self-hosted or cloud
  Install: `docker run -d -p 3456:3456 vikunja/vikunja`

- **Dyad** — local open-source AI app builder; 20k★; builds full-stack apps locally without sending code to the cloud
  `git clone https://github.com/dyad-sh/dyad`

- **Chatwoot** — open-source customer support chat platform; self-hosted alternative to Intercom/Zendesk; multi-channel inbox
  `git clone https://github.com/chatwoot/chatwoot`

- **Quests** — open-source desktop app builder driven by LLMs; describe what you want in plain English, get a native app
  `git clone https://github.com/0-don/quests`

- **`yt-dlp/yt-dlp`** (182k★) — download videos from YouTube, TikTok, Twitter/X, Instagram, and 1,800+ other sites; actively maintained fork of youtube-dl
  Install: `pip install yt-dlp` or `brew install yt-dlp`

- **`jamiepine/voicebox`** (49.1k★) — open-source AI voice studio; record, clone, and generate voices locally; no subscription
  `git clone https://github.com/jamiepine/voicebox`

- **Kuku** (kuku.mom) — local-first macOS Markdown workspace; keeps notes on-device, no sync fees
  Download from kuku.mom

- **`unclecode/crawl4ai`** (76.1k★) — open-source LLM-friendly web crawler; returns clean structured Markdown from any URL; drop-in for scraping steps in agent pipelines
  Install: `pip install crawl4ai`

- **Bitwarden** — open-source 1Password alternative; self-hosted or cloud; free tier covers unlimited passwords across devices
  `git clone https://github.com/bitwarden/server` or download from bitwarden.com

- **`LibreTranslate/LibreTranslate`** — self-hosted open-source machine translation API; free DeepL alternative; runs on-device with no API costs
  `git clone https://github.com/LibreTranslate/LibreTranslate`

- **Baserow** — open-source Airtable alternative; no-code database and spreadsheet UI; self-hosted for $0
  `git clone https://github.com/bram2w/baserow`

- **Nextcloud** — open-source Dropbox/Google Drive alternative; file sync + calendar + contacts + video calls; self-hosted on any server
  `git clone https://github.com/nextcloud/server`

**Claude Code skills and tooling (from @trailofbits, @mattpocock, @microsoft, @melibuilds.io carousels):**

- **`trailofbits/skills`** (6.4k★) — Trail of Bits Claude Code skills collection; security-focused skills for code auditing, exploit research, and hardening
  `git clone https://github.com/trailofbits/skills`

- **`mattpocock/skills`** (203k★) — "Skills for Real Engineers" Claude Code skill collection from Matt Pocock (TypeScript guru); TypeScript, testing, and engineering workflow skills
  `git clone https://github.com/mattpocock/skills`

- **`microsoft/SkillOpt`** (15.6k★) — Microsoft research tool for skills that self-optimize for LLM agents; automatically improves skill prompts based on observed task performance
  `git clone https://github.com/microsoft/SkillOpt`

- **`pbakaus/impeccable`** (55.1k★) — already in README (51st addition); the design language that kills AI slop with 60 detectors

**Open-source AI coding agents and workspaces:**

- **Frontman** (frontman.ai) — open-source browser-based AI coding agent; runs entirely in the browser; no local install required
  Available at frontman.ai

- **Nimbalyst** — open-source integrated visual workspace for Claude Code and Codex; orchestrates parallel AI coding sessions, streams agent edits into editors, manages local projects, worktrees, and files; free for individuals
  Download at nimbalyst.com (Apple Silicon Mac / Intel Mac / Windows / Linux)

**Self-training open-source AI model:**

- **Ornith-1.5** (@aigenesis.official) — 1.5GB open-source AI model that trains itself on increasingly difficult coding tasks; generates its own tools and task scaffolds; learns from successful and failed attempts; available in 9B, 35B, and 397B variants; designed to improve coding and agentic performance through self-training

**Skills created:**

- `.claude/skills/ai-video-prompts-viral/SKILL.md` — 5 viral AI video prompts from @productester11 (Before/After Morph, City Hyperlapse, Found-Footage Walk, Dreamy Loop, Unexpected Job Swap) — copy-paste ready for Sora, Veo, and Kling
- `.claude/skills/overwhelm-to-action-prompts/SKILL.md` — 6 productivity prompts from @the21.i: Empty Your Brain, Plan the Week, Just Tell Me What to Do Next, Find What AI Can Do For Me, Turn Notes Into Action, Find the Bottleneck
- `.claude/skills/perplexity-research-workflow/SKILL.md` — 3 Perplexity + Claude research workflows from @earchoe: Research-to-Content, Client Research Before a Pitch, Competitor Analysis + Positioning Gap

Most other content in this batch was informational: @buildwithmuj "Local AI hardware tiers" (Strix Halo mini PC $2K, RTX 4090/5090 $1.6-5K, DGX Spark/Mac Studio $4.7-10K, H100/H200 clusters $250-400K — informational); @melibuilds.io "10 GitHub repositories that will change your life" (title + impeccable slides; impeccable already in README); @mydlytracker "Writing Automations 15-21" (Transcript to Article, Meeting Notes to Draft, Long Post to Thread, SEO Refresh, Proofreading Pass, FAQ Generator, Old Content Updater — informational); @clicksandranks "3 apps behind my 6 figure business" (title slide only, no apps visible); @replace.so "5 open-source website builders" + Crystal/Nimbalyst carousel (Nimbalyst captured above); @easyclaw6 "AI Chatbots" + commentary slides (ChatGPT/Gemini/Claude — informational); @emmadroid "Paid vs Free" carousel (Notes: Notion vs Obsidian; Cloud: Dropbox vs Nextcloud; Databases: Airtable vs Baserow; Forms: Typeform vs Google Forms; Tasks: Todoist vs Vikunja — open-source alternatives captured above, commercial tools informational); @dk.mindset15 FoundersDB.net promo (1,500+ real founder case studies at foundersdb.net — commercial service, no repo); @imma.uiux COMMANDS.md Claude Code orchestration slide (informational, part of ongoing carousel); @productester11 slide 1/7 title and 5/7 Dreamy Loop (captured in skill above); @the21.i slides 03/08 Plan the Week and 06/08 Turn Notes Into Action (captured in skill above).

---

### 53rd addition — all three images confirmed duplicates, no new installs

Batch of 3 images reviewed. Duplicate check run against README and existing skills before any action taken. All content already covered:

- **"The New SEO Playbook: AEO. GEO. AIO. SXO."** (@TheBestOfAI) — the four-quadrant breakdown (AEO = Answer Engine Optimization, GEO = Generative Engine Optimization, AIO = AI Integration Optimization, SXO = Search Experience Optimization) is already captured in full in `.claude/skills/ai-search-marketing-2026/SKILL.md` (added in an earlier batch, cross-referenced on line 22 of this README). Skipped.

- **"6 Storytelling Frameworks That Help You Lead Inspiringly"** (Kelly Knight) — Pixar's Story Spine, The Golden Circle (Simon Sinek), Duarte's Sparkline, The Hero's Journey (Joseph Campbell), And-But-Therefore (Randy Olson), What/So-What/Now-What — already added in the 28th batch as `references/leadership-storytelling-frameworks.md` inside `.claude/skills/business-decision-frameworks/`. Skipped.

- **"How to Build a LinkedIn Presence and Not Get Lost in the Noise?"** — 15-day course outline (Day 1–15 topic titles) — already noted in the 28th batch as informational-only (curriculum titles with no per-day content shown); its topics are already covered by `.claude/skills/linkedin-virality-playbook/` and `.claude/skills/inbound-content-playbook/`. Skipped.

No new repos, skills, commands, or tools installed this batch. No copy-paste prompts — the batch contained frameworks and course outlines, not AI prompts.

---

### 54th addition — Claude Code skill repos, dev/QA tools, and two prompt skills

**Batch:** 93 images from iCloud Photos (`a26ae912-iCloud_Photos.zip`). 22 repos identified; all checked against existing README — zero duplicates. Two new skills created from prompt content.

**Claude Code skill repos (installable with `npx skills add`):**

- **`lmbad0202/academic-research-skills`** (43k★, 3k forks) — Academic Research Skills for Claude Code; covers literature review, citation management, hypothesis formation, and research methodology
  `npx skills add lmbad0202/academic-research-skills`

- **`emilkowalski/skills`** (32k★, 2k forks) — Skills for Designers and Engineers from Emil Kowalski; covers component design, animation, and engineering workflow
  `npx skills add emilkowalski/skills`

- **`phuryn/pm-skills`** (26k★) — Product Management skills for Claude Code; PRD writing, roadmapping, stakeholder communication, sprint planning
  `npx skills add phuryn/pm-skills`

- **`cathrynlavery/diagram-design`** (26k★) — Diagram and visual design skills for Claude Code
  `npx skills add cathrynlavery/diagram-design`

- **`virgiliojr94/book-to-skill`** (24k★, 3k forks) — Converts a book's key insights into a Claude Code skill; structured methodology for extracting and packaging book knowledge
  `npx skills add virgiliojr94/book-to-skill`

- **`mukul975/Anthropic-Cybersecurity-Skills`** (31k★, 4k forks) — Cybersecurity skills for Claude Code; threat modeling, penetration testing methodology, vulnerability assessment
  `npx skills add mukul975/Anthropic-Cybersecurity-Skills`

- **`msitarzewski/agency-agents`** (125k★, 20.2k forks, MIT) — 200+ specialist subagents for running an AI agency; client communication, project management, content creation, and technical delivery roles
  `npx skills add msitarzewski/agency-agents`

- **`browser-use/video-use`** (13.5k★, 1.7k forks, MIT) — Edit videos with coding agents; ships a SKILL.md; companion to the `browser-use` browser automation framework; video editing via natural language instructions
  `npx skills add browser-use/video-use`

**Codebase knowledge graph:**

- **`safishamsi/graphify`** (75.6k★, 7.5k forks, MIT) — Turns any repository into a queryable knowledge graph for Claude Code, Codex, and Cursor; agents navigate the graph for context rather than reading every file; overlaps in goal with the existing `zzet/gortex` (50th batch, batch 50) — compare before installing both
  `git clone https://github.com/safishamsi/graphify`

**Self-hosted personal AI assistant:**

- **`leon-ai/leon`** (17k★) — Open-source self-hosted personal AI assistant; server/client architecture; modular skill system; runs locally with no API costs
  `git clone https://github.com/leon-ai/leon`

**Collaborative AI agent workspace:**

- **Sim** (simstudio.ai, 29.4k★) — Open-source collaborative workspace for building and running AI agent workflows; visual pipeline builder; supports Claude, GPT-4, and local models; available at simstudio.ai

**Desktop RPA (Windows):**

- **Astron-rpa** (5.8k★) — Open-source desktop RPA for Windows; automates repetitive UI tasks at the OS level without browser limitations
  `git clone https://github.com/Astron-rpa/Astron`

**Multi-agent orchestration:**

- **ORCA** (from @lunktech) — Manages and runs multiple coding agents in parallel; referenced alongside `manaflow-ai/cmux` (batch 34); no GitHub slug captured — check @lunktech's profile for the current repo path

**Workflow orchestration engine:**

- **`conductor-oss/conductor`** (32.1k★, Apache-2.0) — Netflix's open-source workflow orchestration engine; runs multi-step workflows as code with retry, timeout, and branching; language-agnostic; complements the visual-pipeline tools (Dify/Flowise/Langflow) already in `claude-code-tooling`
  `npm install -g @conductor-oss/conductor-cli`

**Developer tooling and UI frameworks:**

- **`ChromeDevTools/chrome-devtools-mcp`** (44.9k★, Apache-2.0) — Official Chrome DevTools MCP server; exposes the DevTools Protocol as MCP tools for debugging, performance profiling, and DOM inspection from within an agent session; requires Chrome/Chromium running locally; add via `claude mcp add` per the repo README

- **Arwes** (7.5k★) — Science-fiction UI design system and React framework; animated, cosmic-themed components for futuristic interfaces; complements `ui-motion-design` for stylized/branded builds
  `npm i @arwes/react`

**Validation and QA tools:**

- **Nu Html Checker (`validator/validator`)** — Official W3C HTML/CSS/SVG validator; batch-validates HTML files locally without a network roundtrip to validator.w3.org; download `vnu.jar` from validator.github.io
  `java -jar vnu.jar index.html` (or `--format json` for machine-readable output)

- **`argos-ci/argos`** — Open-source visual regression testing; captures and compares screenshots across deploys; integrates with CI/CD pipelines; catches layout regressions the unit tests miss
  `npm i @argos-ci/core`

- **Lychee** — Fast link checker in Rust; validates internal and external links in Markdown and HTML; a CI step before publishing to catch broken URLs
  `lychee README.md public/**/*.html` (install: `cargo install lychee`)

- **sitespeed.io** — Open-source Web Vitals and performance testing suite; measures TTFB, render time, and Core Web Vitals against real or synthetic traffic; complements `seo-audit-skill`
  `sitespeed.io https://site -n 5` (install: `npm install -g sitespeed.io`)

- **ZAP by Checkmarx** (Apache-2.0) — Open-source DAST security scanner; automated web application security testing in CI/CD; pairs with `npm-supply-chain-security` for a defense-in-depth QA pipeline
  `zap-baseline.py -t https://site` (install per checkmarx.github.io/zaproxy)

**Speech recognition:**

- **OpenWhisper (`openai/whisper`)** — Open-source speech recognition model from OpenAI; runs locally; converts audio to text across 99 languages; no API costs, no data leaves the machine; complements `ai-voice-tools` (batch 35) for transcription use cases
  `pip install openai-whisper`

**Skills created:**

- **`weekly-planning-workflow`** — 4-step (of a 7-step series) structured weekly planning methodology: (1) connect Google Calendar and verify read access before prompting; (2) brain-dump every deadline and half-finished item in one messy paragraph — the mess is the input; (3) ask Claude to ask you questions before planning anything — energy, hard deadlines, what cannot move; (4) request calendar blocks with specific start/finish times and buffers. Steps 5–7 were not visible in the batch.

- **`/clarify-first` command** — from the "6 Claude Formulas" infographic (Formula 4): `I want [task] to [goal]. Ask me questions with AskUserQuestion first.` A lightweight pre-prompt that forces clarification before any output; pairs with `/plan-then-answer` and the `claude-clean-audit-prompts` three-layer audit pattern.

**Reviewed and not added (confirmed duplicates against existing README):**

- `D4Vinci/Scrapling` — already in batch 34; skipped
- `Skyvern-AutoGPT/skyvern` — already in batch 49; skipped
- `MadsLorentzen/ai-job-search` — already in batch 34 "reviewed and not added" section; skipped
- `Panniantong/Agent-Reach` — already in batch 34; skipped
- ElevenLabs references — already covered in `ai-voice-tools` (batch 35); skipped

**Note on repo verification:** All repos above were seen in batch screenshots but not independently web-verified during this session (same approach as batches 34, 51, 52). Star counts are as shown in screenshots; actual counts may differ. `npx skills add` commands are the standard install path for Claude Code skill repos but will fail silently if the repo doesn't exist or isn't structured as a skills package — run `npx skills add --dry-run` first when uncertain.

Paste-ready prompts from this batch are below.

---

**Weekly planning with Claude (4 of 7 steps, from batch 54):**

> Step 1: Connect Google Calendar and verify you can see my events for this week before I give you any planning prompt.

> Step 2: Here is everything I'm carrying this week: [brain dump — one long paragraph, every deadline and half-finished thing, no organizing yet]

> Step 3: Before you make any plan, ask me questions. I need you to surface my energy levels for each day, any hard deadlines that cannot move, and what is optional vs. required.

> Step 4: Now give me a calendar plan with specific start and finish times for each block, and at least 15 minutes of buffer between blocks.

**"6 Claude Formulas" — Formula 4:**

> I want [task] to [goal]. Ask me questions with AskUserQuestion on first.

---

### 55th addition — JetroExtension/Jetro, LinkedIn Profile Auditor skill, and AI tools from the 2026 pyramid

**Batch:** 4 images — Marketing Strategy vs Plan infographic (Alec Rickard), The Claude Profile Auditor LinkedIn workflow, Best AI Tools of 2026 pyramid (Anastasiia Shapovalova), B2B vs B2C Marketing comparison (Pierre Herubel). Also: explicit user request to document `JetroExtension/Jetro`.

**New repo:**

- **`JetroExtension/Jetro`** — browser extension; clone per the repo README
  `git clone https://github.com/JetroExtension/Jetro`

**New tools from the Best AI Tools of 2026 pyramid not previously in README:**

- **Base44** — no-code/AI-assisted app builder; builds functional web apps from a prompt; competes with Lovable and Replit in the vibe-coding space; commercial (base44.com), no open-source repo
- **Manus AI** — autonomous AI agent for complex multi-step tasks (research, coding, spreadsheet automation); Chinese-developed, accessed via manus.im; no public GitHub repo
- **Otio AI** — AI reading and research tool; uploads PDFs, URLs, and YouTube videos then chats with the content; replaces manual literature review for research workflows; commercial (otio.com), no open-source repo
- **Read AI** — AI meeting intelligence: auto-joins calls, generates summaries, transcripts, and action items; integrates with Google Meet, Zoom, Teams; commercial (read.ai), no open-source repo
- **Softr** — no-code web app builder (client portals, internal tools, member sites) on top of Airtable or Google Sheets; no open-source repo; complements the existing `outreach-automation` and `waitlist-app-builder` skills for lightweight front-ends without code

**Already in README — skipped from pyramid:**
Claude, ChatGPT, Perplexity, Cursor, Lovable, Replit, HeyGen, Synthesia, Descript, Opus Clip, Beehiiv, Grammarly, NotebookLM, Gamma, Granola, Wispr Flow, ElevenLabs, Suno, Midjourney, Runway, Kling, Pika Labs, Figma, Canva, Google Veo, Higgsfield, Softr (noted above), n8n, Zapier, Lindy AI, Claude Code, Gemini, Notion AI, Apify, Clay

**Skill created:**

- **`linkedin-profile-auditor`** — 4-step Claude Projects setup for auditing LinkedIn profiles section by section. Create a dedicated project named "LinkedIn Profile Audit"; paste the full system prompt (get it by commenting "AUDIT" on the original creator's post) into Project Instructions; upload your voice guide + example audits to Project Knowledge; then introduce yourself in a new chat — Claude asks 3 quick questions (whose profile, audit goal, target audience), then reviews each section: headline, about, experience, featured, skills, positioning, CTA.

**Educational frameworks documented (reference, no tool/repo):**

- **Marketing Strategy vs Marketing Plan** (Alec Rickard) — 11 strategy→tactic pairings: authority content → publish blogs/case studies/whitepapers; high-intent conversions → targeted campaigns optimised weekly; relationship + lead gen → quarterly events; organic visibility → keyword research + on-page SEO; PR → pitch media; customer retention → personalised behavioural email; affiliate/partner distribution → recruit affiliates + provide assets; OKR-aligned marketing → track performance + adjust; influencer reach → partner + track results; personalised comms → targeted direct mail; brand awareness + community → consistent cross-platform content.

- **B2B vs B2C Marketing** (Pierre Herubel) — key differences across audience (businesses + firmographic vs. consumers + demographic), buying cycles (multiple stakeholders + touchpoints vs. single buyer + quick decision), content focus (case studies/thought leadership/webinars vs. UGC/influencer/social), decision drivers (ROI + efficiency + risk mitigation vs. price + emotion + convenience), and success factors (positioning + segmentation + working proof vs. brand identity + storytelling + social proof). Shared foundations: attract/engage/convert, clear value proposition, brand trust, digital channels.

**Paste-ready prompts:**

**LinkedIn Profile Auditor intro:**

> Hi. I'd like to audit a LinkedIn profile. Let's begin.

**Marketing strategy audit (derived from the Strategy vs Plan framework):**

> Map my current marketing activities to the Marketing Strategy vs Plan framework. For each strategic goal I have, identify the tactical execution it maps to and flag any goals with no active tactic, or tactics with no clear strategic goal behind them.

**B2B vs B2C alignment check (derived from the comparison framework):**

> Using the B2B vs B2C marketing framework, analyse my current marketing approach. Am I marketing like a B2B business (ROI-driven, multi-stakeholder, case study content) or a B2C business (emotion-driven, mass appeal, social content)? Where am I misaligned for the buyers I'm actually selling to?

---

### 56th addition — 15 open-source tools and 13 commands from @theusefulshift

**Batch:** 94 images from iCloud Photos (`632c5b24-iCloud_Photos_3.zip`). 16 repos identified; duplicate check confirmed `conductor-oss/conductor` already added in the 54th batch — 15 are new. One 12-slide carousel from @theusefulshift ("20 Claude Commands That Feel Illegal") provided 14 of the 20 commands; slides 05-07 and 13-16 and 19-20 were not captured in this batch.

**New open-source repos and tools:**

**Self-hosted wikis and knowledge bases:**

- **LeafWiki** — self-hosted personal wiki, single Go binary, Markdown files on disk; no database required; lightweight alternative to Notion or Obsidian Publish for teams wanting full data ownership
  `git clone https://github.com/nicholasgasior/leafwiki` (check repo for current path — captured from screenshot)

- **SilverBullet** — self-hosted Markdown knowledge database with a Lua scripting engine; supports slash commands, widgets, and page queries from within Markdown; a more programmable alternative to Obsidian for structured notes
  `npx @silverbulletmd/silverbullet` (or self-host via Docker)

**Self-hosted CRM:**

- **Relaticle** — open-source self-hosted CRM with built-in AI agents and 30+ MCP tools; contacts, deals, pipeline management, and AI-assisted relationship intelligence; 1.5k stars
  `git clone https://github.com/Relaticle/relaticle`

**Self-hosted eCommerce:**

- **Spree** (`spree/spree`) — open-source B2B and marketplace eCommerce platform (Ruby/Rails); powers headless storefronts and multi-vendor marketplaces; 15k stars
  `npx create-spree-app@latest my-store`

**Self-hosted project management:**

- **DooTask** — open-source self-hostable project and task management; kanban boards, Gantt charts, team collaboration; alternative to Jira/Linear for fully self-hosted setups
  `git clone https://github.com/kuaifan/dootask`

**Open-source SEO platform:**

- **OpenSEO** — open-source SEO platform for technical audits, keyword tracking, and backlink analysis; 9.9k stars; self-hostable alternative to Ahrefs/SEMrush for teams controlling their own data
  `git clone https://github.com/openseo-org/openseo` (check for current repo path)

**AI video / lip sync:**

- **LatentSync** (`bytedance/LatentSync`) — ByteDance's open-source lip sync generation model; takes an audio track and a reference video and generates matched mouth movement; 5.8k stars; complements the existing `ai-video-image-prompt-structure` skill and the `hyperframes` skill for post-production pipelines
  `git clone https://github.com/bytedance/LatentSync`

**Self-hosted monitoring:**

- **Uptime Kuma** — self-hosted website, API, port, and container uptime monitor with status pages; push/pull/ping monitoring; rich notification channels (Slack, Discord, Telegram, email, and many more); no cloud dependency
  `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data louislam/uptime-kuma:1`

**LLM-ready repo digests:**

- **Gitingest** — converts any public Git repo into a single LLM-friendly plain-text digest (file tree + concatenated source); paste the digest into a long-context model to ask codebase-wide questions without a local clone; available at gitingest.com or self-hostable
  `pip install gitingest` (CLI: `gitingest https://github.com/owner/repo`)

**Open-source API client:**

- **Bruno** (`usebruno/bruno`) — open-source API client with plain-text, Git-friendly collections (no proprietary binary format, no cloud sync required); drop-in alternative to Postman/Insomnia for teams that want API collections in version control
  `npm install -g @usebruno/cli` (or download the desktop app from usebruno.com)

**Open-source Go backend:**

- **PocketBase** — open-source backend in a single Go binary: SQLite database, realtime subscriptions, auth (email/OAuth/OTP), file storage, and an admin dashboard; no separate database setup; a fast foundation for side-projects and internal tools
  `go install github.com/pocketbase/pocketbase@latest`

**Self-hostable PaaS:**

- **Coolify** (`coollabsio/coolify`) — open-source self-hostable alternative to Heroku, Netlify, and Vercel; deploys apps, databases, and services from Git repos or Docker Compose; runs on a single VPS; pairs with the existing `waitlist-app-builder` skill for a fully self-hosted launch stack
  `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`

**Developer utilities:**

- **IT-Tools** (`CorentinTh/it-tools`) — collection of everyday developer utilities (token decoder, base64, cron parser, color converter, regex tester, and 100+ more) as a self-hostable web app; no telemetry; useful as a localhost toolbelt
  `docker run -d --name it-tools --restart unless-stopped -p 8080:80 corentinth/it-tools:latest`

**Self-hosted survey platform:**

- **Formbricks** (`formbricks/formbricks`) — open-source self-hosted survey platform; supports in-app, website, link, and email surveys; GDPR-compliant by default with full data ownership; a self-hosted alternative to Typeform/SurveyMonkey for privacy-sensitive contexts
  `npx create-formbricks-app@latest`

**TypeScript AI background jobs:**

- **Trigger.dev** (`triggerdotdev/trigger.dev`) — open-source platform for TypeScript AI workflows and long-running background jobs; built-in retries, queues, real-time observability, and scheduled runs; lets async/AI-heavy jobs run for minutes or hours without serverless timeouts; 16k stars; complements the existing `outreach-automation` and `self-healing-automation` command for production-grade async pipelines
  `npx trigger.dev@latest init`

**Already in README — skipped from this batch:**

- `conductor-oss/conductor` — already added in the 54th batch

**Commands created from @theusefulshift "20 Claude Commands That Feel Illegal" (14 of 20 captured; slides 05-07, 13-16, 19-20 not in this batch):**

- `/redteam` — attack the plan and rank its three most likely failure modes (numbered 02)
- `/researchmap` — separate what we know, assume, and still need to verify (numbered 03)
- `/sourcecheck` — source every factual claim; flag anything unsupported (numbered 04)
- `/meeting` — extract decisions, owners, deadlines, and open questions from a transcript (numbered 08)
- `/handoff` — package work so another person can continue without asking questions (numbered 08)
- `/sop` — convert a process into inputs, steps, quality checks, and outputs (numbered 09)
- `/qa` — test a result against every requirement; show failures first (numbered 09)
- `/decision` — compare three options by upside, cost, reversibility, and risk (numbered 09); distinct from the existing `/decision-matrix` (2-option budget/timeline/strategic-value comparison)
- `/nextmove` — choose the smallest action that removes the most uncertainty (numbered 10)
- `/offer-frame` — turn an idea into audience, problem, outcome, and proof (numbered 11); renamed from `/offer` since that command already exists as a priced-offer designer
- `/objection` — list why a skeptical buyer says no, then improve the offer (numbered 12)
- `/edgecases` — find ten realistic failures outside the happy path (numbered 17)
- `/teachback` — explain the idea back and expose what is still unclear (numbered 18)

**Skipped:**
- `/clarify` (numbered 01) — duplicate of the existing `/clarify-first` (batch 54), which already implements the same "ask only questions that would meaningfully change the output" pattern

**Paste-ready prompts (verbatim from @theusefulshift carousel):**

> 01 /clarify — Ask only the questions that would materially change the answer.

> 02 /redteam — Attack the plan and rank its three most likely failure modes.

> 03 /researchmap — Separate what we know, assume, and still need to verify.

> 04 /sourcecheck — Source every factual claim and flag anything unsupported.

> 08 /meeting — Extract decisions, owners, deadlines, and open questions.

> 08 /handoff — Package the work so another person can continue without me.

> 09 /sop — Convert the process into inputs, steps, checks, and outputs.

> 09 /qa — Test the result against every requirement. Show failures first.

> 09 /decision — Compare three options by upside, cost, reversibility, and risk.

> 10 /nextmove — Choose the smallest action that removes the most uncertainty.

> 11 /offer — Turn the idea into an audience, problem, outcome, and proof.

> 12 /objection — List why a skeptical buyer says no, then improve the offer.

> 17 /edgecases — Find ten realistic failures outside the happy path.

> 18 /teachback — Explain the idea back to me and expose what is still unclear.

**Note on repo verification:** All repos above were seen in batch screenshots. Star counts are as shown in screenshots; actual counts may differ. Install commands are the standard paths for each tool's type but should be verified against the current repo README before use — project names and namespaces occasionally change. `conductor-oss/conductor` (54th batch), `Remotion`, `MoneyPrinterTurbo`, `AI-Shorts-Generator`, and `WhisperX` (seen in this batch's "5 repos that make viral content" slide) are all already covered in earlier additions and were skipped.

---

### 57th addition — 11 open-source repos, 2 commands, and a brand-building skill

**Batch:** 101 images from iCloud Photos (`e2be2e26-iCloud_Photos_4.zip`). 17 repos/tools identified; 6 confirmed duplicates — 11 are new. Two new commands created from @ai.blueprint prompts; one new skill from @martiendejong_dev's 8-prompt brand+website series.

**Duplicate-check (skip):**

| Repo | First documented |
|---|---|
| `cline/cline` | 39th addition |
| `opf/openproject` | 47th addition |
| `makeplane/plane` | 47th addition |
| Nimbalyst | 52nd addition |
| `virgiliojr94/book-to-skill` | 54th addition |
| `zhaoxuya520/reverse-skill` | 34th addition (listed as `reverse-skill`) |

**New repos and tools:**

**Open-source .NET CMS:**

- **Umbraco** (`umbraco/Umbraco-CMS`) — the leading open-source .NET CMS; flexible headless and traditional content management; MIT
  `git clone https://github.com/umbraco/Umbraco-CMS`

**AI-native IDEs and agentic development environments (from @replace.so carousel):**

- **Neuralinverse** — open-source AI-native IDE; designed for agentic coding workflows; check @replace.so for current GitHub path
- **Jat** — open-source self-hosted agentic development environment; check @replace.so for current GitHub path

**DeepSeek-native coding agent:**

- **`esengine/DeepSeek-Reasonix`** (34.3k★) — terminal coding agent built natively on DeepSeek's reasoning model; CLI-native, fast reasoning loop; drop-in for terminal workflows where Claude Code or Codex is used today
  `git clone https://github.com/esengine/DeepSeek-Reasonix`

**Fast Rust PDF inspection library:**

- **`firecrawl/pdf-inspector`** (15.1k★, MIT, Rust) — fast PDF inspection library from the Firecrawl team; extracts structure, metadata, and text from PDFs at high speed; distinct from `firecrawl/firecrawl` (the web-scraping tool, already in README)
  `git clone https://github.com/firecrawl/pdf-inspector`

**Open-source desktop console for AI coding agents:**

- **BossConsole (BOSS)** — open-source desktop console for managing and orchestrating AI coding agents (Claude Code, Codex, and others); visual dashboard for agent sessions; check GitHub for current repo path

**RAG for monorepos using knowledge graphs:**

- **`vitali87/code-graph-rag`** (4.1k★) — RAG system for monorepos that builds a knowledge graph of the codebase and answers agent queries through graph traversal; reduces hallucination on large codebases; complements `zzet/gortex` (50th batch) and `safishamsi/graphify` (54th batch) for code-intelligence use cases
  `git clone https://github.com/vitali87/code-graph-rag`

**Open-source all-in-one business platform:**

- **Huly** (`hcengineering/huly`) — open-source all-in-one business platform that replaces Linear, Jira, Slack, and Notion in a single self-hosted install; project management, issue tracking, team chat, and docs in one place
  `git clone https://github.com/hcengineering/huly`

**Claude Code skill repos (installable with `npx skills add`):**

- **`addyosmani/agent-skills`** (86.7k★) — production-grade engineering skills for AI coding agents from Addy Osmani; performance engineering, accessibility, code review, and modern web development practices
  `npx skills add addyosmani/agent-skills`

- **`google/skills`** (18k★, Apache-2.0) — official Google agent skills for Claude Code; Google engineering best practices packaged as Claude Code skills
  `npx skills add google/skills`

**Give your agent its own computer:**

- **`cloudflare/computer`** (7.9k★, MIT) — Cloudflare's open-source tool for giving AI agents their own isolated computer environment; the agent gets a full browser, filesystem, and shell without touching the user's machine
  `git clone https://github.com/cloudflare/computer`

**Skills and commands created:**

- **`brand-website-8-prompts`** — 8-prompt sequential workflow from @martiendejong_dev "8 prompts to build brand + website in one afternoon": (1) Lean Brand Consultant — minimum brand elements to go live; (2) Messaging Strategist — one core message readable in 5 seconds; (3) Lean Brand Designer — minimal visual identity (2 colors, 1 font pair, 1 logo concept in 15 minutes); (4) Lean Website Strategist — conversion-focused one-page structure with headline, proof, CTA; (5) Credibility Consultant — strongest authentic proof available today, no invented credibility; (6) Lean Copywriter — complete website copy, headline through CTA, publish-ready; (7) Launch Coordinator — go-live checklist, flags only critical blockers; (8) Growth Consultant — 2-week post-launch iteration plan on real signals. Stored at `.claude/skills/brand-website-8-prompts/SKILL.md`.

- **`/pressure-test-idea`** — @ai.blueprint Step 1: skeptical-advisor pressure test for a new business idea — 5 most likely failure reasons and what proof would be needed before believing the idea can work. Distinct from the existing `/pressure-test-options` (which compares two named alternatives) — this one stress-tests a described idea cold.

- **`/daily-brief`** — @ai.blueprint Step 8: 5-bullet morning brief from priorities file and CRM notes — top 3 priorities, most urgent follow-up, and one thing that's probably being forgotten. For use with a connected CRM or project-management connector (Notion, Linear, HubSpot, etc.).

### 58th addition — 11 open-source repos, 0 new commands

**Batch:** 70 images from iCloud Photos (`dc1830a5-iCloud_Photos_5.zip`). Five carousels identified with actionable repos. All @earchoe LinkedIn prompts (profile rewrite, post writer, outreach DM) already covered by existing commands — no new commands created.

**Duplicate-check (skip):**

| Repo / Tool | First documented |
|---|---|
| `twentyhq/twenty` | 29th addition |
| Dyad | 55th addition |
| Chatwoot | 53rd addition |
| Nextcloud | 46th addition |
| ORCA (multi-agent coding workspace) | 34th addition |

**New repos and tools:**

**Self-hosted homelab stack — @networkllama "How to start a homelab from zero" (8-step guide):**

- **Proxmox VE** — open-source bare-metal hypervisor; runs VMs and LXC containers on any old PC or mini PC; the foundation of most homelabs
  `https://www.proxmox.com/en/proxmox-virtual-environment`

- **Pi-hole** (`pi-hole/pi-hole`) — network-level ad and tracker blocker; runs on your LAN, blocks ads for every device without installing anything on them
  `git clone https://github.com/pi-hole/pi-hole`

- **Jellyfin** (`jellyfin/jellyfin`) — free open-source media server; turns your movie and show collection into a private Netflix — stream to phone, TV, or laptop with no subscription or algorithm
  `git clone https://github.com/jellyfin/jellyfin`

- **Home Assistant** (`home-assistant/core`) — open-source smart home hub; connects all smart devices into one local hub you control; automations run locally, not in the cloud; works offline
  `git clone https://github.com/home-assistant/core`

- **Portainer** (`portainer/portainer`) — Docker and Kubernetes container management UI; manage all containers visually from a browser dashboard
  `git clone https://github.com/portainer/portainer`

- **Nginx Proxy Manager** (`NginxProxyManager/nginx-proxy-manager`) — reverse proxy with a GUI; assign one clean URL per homelab service, with automatic SSL; no manual nginx config
  `git clone https://github.com/NginxProxyManager/nginx-proxy-manager`

**Open-source SaaS replacements — @quadri_folo carousel:**

- **Webstudio** (`webstudio-is/webstudio`) — open-source alternative to Webflow; visual website builder with full source-code access and self-hosting; no vendor lock-in
  `git clone https://github.com/webstudio-is/webstudio`

- **OpenSign** (`OpenSignLabs/OpenSign`) — free open-source alternative to DocuSign; send documents for e-signature, create reusable templates, multiple signers, audit trails; self-host your documents
  `git clone https://github.com/OpenSignLabs/OpenSign`

- **Dokploy** (`Dokploy/dokploy`) — open-source alternative to Vercel, Netlify, and Heroku; deploy and manage web apps, Docker containers, PostgreSQL, Redis, and multiple servers; includes SSL, monitoring, backups, and GitHub deployments
  `git clone https://github.com/Dokploy/dokploy`

- **Rybbit** (`rybbit-io/rybbit`) — privacy-friendly open-source alternative to Google Analytics; self-hostable, no cookies, GDPR-compliant; replaces GA without the tracking overhead
  `git clone https://github.com/rybbit-io/rybbit`

- **Paperless-ngx** (`paperless-ngx/paperless-ngx`) — open-source document management system; scan, index, and archive physical documents into a searchable digital library; self-hosted
  `git clone https://github.com/paperless-ngx/paperless-ngx`

Most other content in this batch was informational: @risenworks MCP configuration tips (MAX_MCP_OUTPUT_TOKENS=50000, ENABLE_TOOL_SEARCH=auto:5, timeout settings — informational); @aicareersuite "150 AI Agent Ideas for Local Businesses" across 10 industries (restaurants, salons, gyms, real estate, clinics, retail — informational); @toolradar8 carousel covering Perplexity, NotebookLM, and ElevenLabs (SaaS tools, no repos); @webnailed "7 security concepts every backend needs" (SQL injection, password hashing, rate limiting, JWT, input validation, webhook signature — educational); @inkaai Claude PDF tips (3,000 tokens/page; convert to Markdown to reduce token cost — informational); @earchoe LinkedIn client system (9-slide carousel on using LinkedIn to attract clients — prompts already covered by existing commands); @aiemergence Google Jitro (autonomous coding agent, goal-driven AI — informational/news).

### 59th addition — 3 open-source repos, 0 new commands

**Batch:** 6 TikTok videos (`f5a2ed33-____________.zip`). Frames extracted and analyzed across all 6 videos.

**Duplicate-check (skip):**

| Repo / Tool | First documented |
|---|---|
| OpenAI Codex | `codex-plugin-cc` plugin table + multiple entries |
| `MadsLorentzen/AI-JOB-SEARCH` | 34th addition "reviewed and not added" |
| Karpathy Skills (`forrestchang/andrej-karpathy-skills`) | 38th addition |
| `makeplane/plane` | 47th addition |
| `thedotmack/claude-mem` | Already documented (persistent memory for Claude Code) |

**New repos and tools:**

**Trending AI coding agents and dev tools — @simplec03 "Top 5 Trending Repos" + @github.signals:**

- **graff** (`justrach/codegraff`) — AI coding agent that actually does the work rather than just chatting about it; install via single binary (3.7MB, zero dependencies, built in Zig), sign in with your existing AI subscription, give it plain-English tasks; writes and runs code, automates boring work, digs through files, researches the web, and runs its own experiments on its own until the job is done; can spin up a whole team of sub-agents working in parallel; works on your real terminal with your real files and the real internet; 20× cheaper than Claude Code per-task ($0.022 vs $0.51 per task per benchmark); also has a desktop app
  `curl -fsSL https://github.com/justrach/codegraff/releases/latest/download/install.sh | sh`

- **FREE-CLAUDE-CODE** (`Alishahryar-one/FREE-CLAUDE-CODE`) — Python tool for accessing Claude Code without a paid subscription; #1 trending repo (GitHub) at time of video recording
  `git clone https://github.com/Alishahryar-one/FREE-CLAUDE-CODE`

**Free developer resources — @nate.volkov "Free API Goldmine":**

- **public-apis** (`public-apis/public-apis`) — massive curated list of free public APIs for developers and builders; organized by category (weather, finance, aviation, search, files, screenshots, forex, email validation, and hundreds more); the go-to resource when you need an API for a project and don't want to pay
  `git clone https://github.com/public-apis/public-apis`

**Informational / educational (no repos added):**
- @codenameposhan: Claude Code + CrewAI multi-agent orchestration tutorial — Orchestrator delegates to Researcher, Writer, Reviewer sub-agents; no new installable repo shown
- @justhitsend (Ep 231 — file access): Always start Claude Code inside the project folder (not ~/Desktop); run `pwd` first to check, then `cd` into the project; use `/permissions` to block secrets — educational tip, no new repo
- @jake.joker.crypto (5 Claude Code plugins): Overview of MCP plugins (Slack, Notion visible in setup screen); covered free-tier LLM token budget dashboard (Kiro: 50 credits, Qoder: unlimited, LongCat: 50M/day, Cerebras: 1M/day, NVIDIA: 40 rpm, Pollinations: no key) — the main featured repo `thedotmack/claude-mem` is already documented

### 60th addition — 0 repos, 2 new commands

**Batch:** 2 MedTech strategy markdown files (`fb72daec-medtech_brand_strategy_playbook.md`, `4ba7e819-medtech_commercialization_2026_playbook.md`). Both authored from the perspective of a high-end MedTech commercial portfolio leader (surgical robotics, cardiovascular, neurotech, advanced diagnostics).

**New commands installed:**

- **`/medtech-brand-strategy`** (`.claude/commands/medtech-brand-strategy.md`) — MedTech 3-Tier Commercial Architecture. Guides brand strategy work in strict top-down sequence: Tier 1 Clinical Brand Strategy (standard-of-care vision, clinical integrity, paradigm positioning, specialty-specific value prop) → Tier 2 Market & Economic Strategy (VAC stakeholder mapping, HEOR dossiers, TCO/DRG models, go-to-market route) → Tier 3 Execution (proctorship programs, KOL masterclasses, CME symposia, commercial marketing). Includes a strategic comparison table contrasting the "Tactical Rep" (feature-first, price-war outcome) vs. "Strategic Portfolio Leader" (brand-first, standard-of-care adoption outcome). Usage: `/medtech-brand-strategy [device or technology name]`

- **`/medtech-salesflow`** (`.claude/commands/medtech-salesflow.md`) — 2026 MedTech 5-Stage SalesFlow Architecture. Built around the 2026 healthcare buyer reality (81% of physicians use AI/LLMs; 90% of hospital decision-makers do ~12 online searches; 68% of searches end in zero-clicks; 90% of addressable buyers are out-of-market). Five stages: (1) Understand — persona journey maps for Surgeon, CFO, OR Director, IT/BioMed, VAC; (2) Amplify — convert 3-day congress into 60-day digital pipeline (pre/during/post); (3) Verify — AI/LLM citation share via Schema.org, LinkedIn long-form, Wikipedia/peer-review indexing; (4) Expand — LinkedIn B2B precision targeting with boolean AND, Thought Leader Ads via KOL surgeons, ICP tiering; (5) Nurture — 24-month persona-segmented automation, quarterly KOL masterclasses, RWE registry engine, trigger-based escalation. Includes pipeline health dashboard KPIs per stage. Usage: `/medtech-salesflow [device or technology name]`

### 61st addition — 0 repos cloned, 1 MCP server documented, 1 skill noted

**Batch:** 4 TikTok videos from `5ed1d53d-_____________2.zip`. Sources: @automatedintelligenceai (Spline AI demo), @bingley.ai (AI sales skills), @ivan.geoffreyy × 2 (AI coder plugins; Claude Code improvements). Frames extracted at 1/4s (61 frames total across v1–v4).

**Video 1 — @automatedintelligenceai — Spline (3D AI design):**

- **Spline** (spline.design) — browser-based 3D design tool with an embedded AI agent mode; the AI agent operates inside the Spline editor, accepting plain-English prompts to build full 3D scenes (castle with drawbridge and towers, voxel characters, floating tropical island, energy production facility with power lines); uses primitives, extrusions, and materials natively; free tier available; SaaS only, no open-source repo to clone
  Site: https://spline.design

**Video 2 — @bingley.ai — "5 AI Skills Every Salesperson Needs":**

- **Bingley** (bingley.ai) — AI-powered sales intelligence SaaS platform; features shown: (1) Lead Prospecting — AI builds targeted prospect lists by industry/title/geography with enriched contact data; (2) Competitive Intelligence — real-time competitor monitoring, battlecard generation, win/loss pattern analysis; (3) Reply Intelligence — trained on 90M+ email replies, scores cold outreach and suggests subject-line and opening-line improvements; (4) Daily Sales Digest — morning briefing on pipeline health, deal commitments, follow-up priorities with a "commitments tracker" view; (5) "The Sales Brain" — persistent fact store capturing product knowledge, objection responses, and deal context for instant retrieval; SaaS only, no open-source repo
  Site: https://bingley.ai

**Video 3 — @ivan.geoffreyy — "5 Plugins Every AI Coder Needs":**

- **Playwright** (`microsoft/playwright`) — already documented (see earlier additions); shown here as the browser-testing/automation plugin for AI coders: write E2E tests in natural language, screenshot capture, headless browser control from Claude Code
- **Context7** (Upstash / context7.com) — MCP server that injects real-time, version-accurate library documentation directly into LLM context; solves the hallucination problem where Claude generates code against outdated API signatures; add `use context7` to any prompt and the server fetches the current docs for whichever library you're working with (React, Next.js, Prisma, LangChain, etc.); maintained by Upstash; **new, not previously documented**
  Install as Claude Code MCP server:
  ```
  claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
  ```
  Or add to `.claude/mcp.json`:
  ```json
  {
    "mcpServers": {
      "context7": {
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp@latest"]
      }
    }
  }
  ```

**Video 4 — @ivan.geoffreyy — "Claude Code Just Got Better":**

- **Taste Skill** (`Leonxlnx/taste-skill`) — already documented (38th addition); shown here again as the anti-slop frontend framework; install: `npx skills add Leonxlnx/taste-skill`
- **Guideline Skill** (tasteskill.dev companion) — Claude Code skill that feeds curated UI/UX design references (typography scales, spacing systems, button styles, layout patterns) into Claude's context before generating frontend components; prevents generic/plain output by grounding the AI in a specific visual aesthetic; shown alongside the Taste Skill in the same video, suggesting it is part of the tasteskill.dev ecosystem; the video demonstrated it improving a smoothie app UI and a "Bluebird" security SaaS site from "ui/ux rusty" to polished output; **new, not previously documented** — exact install path at tasteskill.dev/guideline-skill or similar
  Likely install: `npx skills add Leonxlnx/guideline-skill` *(verify at tasteskill.dev)*

**Informational / already documented:**
- Chase AI website (localhost:3000) — demo project built live with Claude Code v2.1.70 (Opus 4.6, high-effort mode); shown as proof of output quality; not an installable tool
- Playwright — already documented; not re-added

---

### 62nd addition — privacy/surveillance tools, dev productivity repos, AI scrapers, self-hosted AI stack, and 3 new commands

**Batch:** 4 iCloud Photos zip files (`2297464f-iCloud_Photos_1.zip`, `44268f6c-iCloud_Photos_2.zip`, `ca99468f-iCloud_Photos_3.zip`, `fcb5d053-iCloud_Photos_6.zip`). Sources include @martiendejong_dev (7 personal finance prompts), @earchoe (YouTube niche + SEO), @ty.prompts.ai (5 surveillance-evasion repos), @baniascodes (6 dev tools), @appmillers (AI scrapers), @deans.lester.tech (n8n AI starter kit). 15 new repos/tools documented; 3 new commands created.

**Duplicate-check (skip):**

| Repo / Tool | First documented |
|---|---|
| Brightbean-studio | 46th addition |
| Nimbalyst | 52nd addition |
| Superpowers | Plugins table |
| Repomix | Plugin table |
| Claude HUD (`jarrodwatts/claude-hud`) | 34th addition |
| Scrapling (`D4Vinci/Scrapling`) | 34th addition |
| Agent Reach (`Panniantong/Agent-Reach`) | 34th addition |
| Karpathy Skills (`forrestchang/andrej-karpathy-skills`) | 38th addition |

**Privacy & digital-security repos — @ty.prompts.ai "5 free repos to avoid surveillance state" (7-slide carousel):**

- **[`EFForg/rayhunter`](https://github.com/EFForg/rayhunter)** — EFF's open-source Rust tool that runs on Orbic mobile hotspots to detect IMSI catchers (fake cell towers / "Stingrays") that intercept your calls and texts; logs suspicious network behaviour, generates a visual web dashboard, and flags anomalies in real time; no cloud, no account
  `git clone https://github.com/EFForg/rayhunter`

- **[`mvt-project/mvt`](https://github.com/mvt-project/mvt)** (13k★) — Mobile Verification Toolkit; forensic tool from Amnesty International's Security Lab for detecting stalkerware, spyware (Pegasus), and other malware on Android and iOS devices; scans device backups and filesystem images for indicators of compromise
  `pip install mvt`

- **[`mollyim/mollyim-android`](https://github.com/mollyim/mollyim-android)** (3.7k★) — Molly: hardened fork of Signal for Android; adds database encryption at rest, auto-lock with inactivity timeout, passphrase-protected backups, and UnifiedPush support so you don't need Google Play Services; same wire protocol as Signal, compatible with Signal contacts
  Install via F-Droid or download APK from GitHub Releases

- **[`guardianproject/orbot-android`](https://github.com/guardianproject/orbot-android)** (3.5k★) — Orbot: Tor for Android by Guardian Project; routes your phone's traffic through the Tor network to anonymise your IP and bypass censorship; supports per-app VPN mode so only selected apps use Tor
  Install via Google Play or F-Droid

- **[`TrackerControl/tracker-control-android`](https://github.com/TrackerControl/tracker-control-android)** — TrackerControl: open-source Android app that monitors and blocks hidden data collection by tracking companies embedded in other apps; shows which trackers each app contacts in real time; based on NetGuard, no root required
  Install via F-Droid or GitHub Releases

**Dev productivity tools — @baniascodes carousel:**

- **[`affaan-m/ECC`](https://github.com/affaan-m/ECC)** — Enhanced Claude Code (ECC): CLAUDE.md harness tuned for speed and reduced token consumption; pairs with the official Claude Code CLI; install by cloning and copying the CLAUDE.md into your project root (the 41st addition referenced this name without a verified GitHub path — this is the resolved repo)
  `git clone https://github.com/affaan-m/ECC`

- **[`langchain-ai/openwiki`](https://github.com/langchain-ai/openwiki)** — OpenWiki: open-source knowledge base and wiki system from LangChain AI; connect your docs, PDFs, and web pages, then query them with natural language; self-hostable
  `pip install openwiki`

- **[`Tencent/AI-Infra-Guard`](https://github.com/Tencent/AI-Infra-Guard)** — Tencent's AI Infrastructure Guard: security scanning tool for AI/ML pipelines and model deployments; detects misconfigurations, exposed model files, and supply-chain risks in AI infrastructure
  `pip install aig-skill-scan`

- **[`styler-ai/ProjectAtlas`](https://github.com/styler-ai/ProjectAtlas)** — ProjectAtlas: Rust CLI that maps a codebase into a structured, agent-navigable project atlas; reduces LLM token consumption by giving agents a compact map instead of raw file reads
  `cargo install project-atlas`

- **[`evo-hq/evo`](https://github.com/evo-hq/evo)** — Evo: agentic CLI tool for evolving codebases; runs iterative improvement loops on code quality, test coverage, and documentation; installed via `uv`
  `uv tool install evo-hq-cli`

- **[`oraios/serena`](https://github.com/oraios/serena)** — Serena: MCP server that gives Claude Code precise semantic code navigation (go-to-definition, find-all-references, rename symbol, class hierarchy) by connecting to language servers; bridges Claude Code to LSP for accurate code understanding without relying on fuzzy text search
  `pip install serena-mcp`

**AI web scrapers — @appmillers carousel:**

- **[`ScrapeGraphAI/Scrapegraph-ai`](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** — ScrapeGraphAI: AI-powered web scraper that uses LLMs to understand and extract structured data from any website; describe what you want in natural language and it handles the extraction — no XPath, no CSS selector maintenance; integrates with Claude, GPT-4, and local models
  `pip install scrapegraphai`

**Self-hosted AI automation stack — @deans.lester.tech:**

- **[`n8n-io/self-hosted-ai-starter-kit`](https://github.com/n8n-io/self-hosted-ai-starter-kit)** — n8n's official self-hosted AI starter kit: a Docker Compose bundle that spins up n8n (workflow automation) + Ollama (local LLMs) + Qdrant (vector store) + PostgreSQL in one command; the foundation for a fully local, no-API-cost AI automation stack; distinct from `n8n-io/n8n` (already in README) — this kit bundles the full AI stack
  ```
  git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
  cd self-hosted-ai-starter-kit
  docker compose --profile cpu up
  ```

**WhatsApp CRM — @fcb5d053 batch:**

- **Wacrm** (`getcodyai/wacrm`) — self-hostable WhatsApp CRM backed by Supabase; manage customer conversations, contacts, and pipeline from a unified inbox without a SaaS subscription; open-source
  `git clone https://github.com/getcodyai/wacrm`

**Markdown notes + MCP + CLI — @fcb5d053 batch:**

- **ZenNotes** (`nicholasleclerc1983/ZenNotes`) — open-source local-first Markdown note-taking app with an integrated MCP server (lets Claude Code read and write your notes) and a `zen` CLI for terminal-based capture; privacy-first, no cloud sync required
  `git clone https://github.com/nicholasleclerc1983/ZenNotes`

**Commands created:**

- **`/personal-finance-claude`** (`.claude/commands/personal-finance-claude.md`) — 7-prompt sequential wealth-building system from @martiendejong_dev: (1) Financial X-Ray — brutally honest 90-day action plan; (2) Build My Money System — paycheck allocation with exact percentages; (3) Destroy My Debt — avalanche vs snowball payoff strategy; (4) Build My First $10K — step-by-step savings plan; (5) Create My Investment Strategy — beginner investing roadmap; (6) Find My Extra Income — 10 ranked income streams with 30-day execution plans; (7) My 1-Year Wealth Blueprint — complete 12-month roadmap with weekly actions. Usage: `/personal-finance-claude [optional financial context]`

- **`/youtube-niche-finder`** (`.claude/commands/youtube-niche-finder.md`) — @earchoe faceless YouTube niche finder: inputs background, tools (ElevenLabs/Claude/Canva), weekly time, and income goal; outputs 5 niches with search volume but not max competition, each with channel ideas, 5 video titles, and reasoning for why it works faceless. Usage: `/youtube-niche-finder [background, skills, interests, time, income goal]`

- **`/youtube-seo-optimizer`** (`.claude/commands/youtube-seo-optimizer.md`) — @earchoe YouTube video SEO optimizer: inputs video topic, channel niche, and target viewer; outputs 5 keyword-first title options (≤60 chars), full description (with hook in the first 150 chars), 15 tags, 3 chapter timestamps, and thumbnail text (≤6 words). Usage: `/youtube-seo-optimizer [video topic, channel niche, target viewer]`

**Reviewed and not added (62nd batch):**

| Repo / Tool | Reason skipped |
|---|---|
| Brightbean-studio | Already in 46th addition |
| Nimbalyst | Already in 52nd addition |
| SERPtag (serptag.com) | SaaS only, no GitHub repo |

Paste-ready prompts from this batch:

**7 Personal Finance Prompts (@martiendejong_dev):**

> **Prompt 1 — Financial X-Ray:** Act as my brutally honest personal finance strategist. Analyze my entire financial situation from scratch. I'll give you my income, expenses, savings, debts, assets, subscriptions, investments, and financial goals. Identify exactly where my money is leaking, what I'm doing wrong, and what I should change first. Then create a prioritized action plan to improve my finances over the next 90 days.

> **Prompt 2 — Build My Money System:** Based on my income and expenses, build me a simple financial system that automatically divides every dollar I earn into spending, bills, emergency savings, investing, and wealth-building. Give me exact percentages and amounts, explain the reasoning, and create rules I can follow every payday without relying on willpower.

> **Prompt 3 — Destroy My Debt:** Act as a debt-elimination strategist. Analyze all my debts, including balances, interest rates, and minimum payments. Compare the avalanche and snowball methods, then create the fastest realistic payoff strategy for me. Show me exactly how much extra I need to pay each month and how much interest I could save.

> **Prompt 4 — Build My First $10K:** I want to build my first $10,000 in savings. Analyze my current income and expenses and create a realistic step-by-step plan to reach $10K as quickly as possible without destroying my quality of life. Find areas where I can cut expenses, suggest ways to increase income, and give me monthly and weekly targets.

> **Prompt 5 — Create My Investment Strategy:** Act as a long-term investing coach. Based on my age, income, financial goals, emergency fund, debt, risk tolerance, and investment timeline, create a beginner-friendly investment strategy. Explain what types of assets I should consider, how much I could invest each month, how to diversify, and what mistakes I absolutely need to avoid. Do not recommend anything until you've analyzed my situation.

> **Prompt 6 — Find My Extra Income:** Analyze my skills, experience, available time, interests, and current income. Find 10 realistic ways I could increase my monthly income. Rank them by startup cost, difficulty, time to first income, scalability, and potential monthly earnings. Then choose the top 3 and create a 30-day execution plan for each.

> **Prompt 7 — My 1-Year Wealth Blueprint:** Act as my personal wealth strategist. Take everything you know about my financial situation and build a complete 12-month wealth-building roadmap. Give me specific monthly targets for income, spending, debt repayment, emergency savings, investing, and additional income. Break each month into weekly actions and create measurable milestones so I know exactly whether I'm on track.

**YouTube Niche Finder (@earchoe):**

> Help me find the best niche for a faceless YouTube channel. About me: [your background, skills, interests] Tools I am using: ElevenLabs for voice, Claude for scripts, Canva for visuals Time available per week: [hours] Income goal: [£X/month within Y months] Suggest 5 niches that: 1. Have search volume but not maximum competition 2. Work well for faceless format (no personality required) 3. Have multiple monetisation paths beyond AdSense 4. I could create 50+ videos about without running out of ideas 5. Attract an audience with purchasing power For each: name the niche, example channel ideas, 5 video titles, and why it works for faceless content.

**YouTube SEO Optimizer (@earchoe):**

> Help me optimise this YouTube video for search. Video topic: [what the video is about] My channel niche: [your niche] Target viewer: [who searches for this] Give me: 1. 5 title options (keyword-first, under 60 chars, creates curiosity) 2. Video description (first 150 chars are crucial — hook + keyword here) 3. 15 tags (mix of broad and specific keywords) 4. 3 chapter timestamps and names for the video description 5. The thumbnail text (under 6 words — the hook in visual form)

---

### 63rd addition

**Batch:** 103 images from iCloud Photos (`3a11c455-iCloud_Photos.zip`). Sources include @joshualevi.ai (7 open-source tools to replace paid SaaS: plausible, caddy, searxng, NocoDB, and more), @replace.so (7 open-source Obsidian alternatives: Logseq, NoteGen already added), @iunlockedai (addyosmani/factory — Claude Code issue-triage factory), @your.aimentor (6 Claude Code skills including `swiftui-design-skill`), @earchoe (9-slide email list building series: lead magnet, landing page, welcome email prompts), @ty.prompts.ai (5 side-hustle automation repos), and @the.wealth.lab (AI agent frameworks for business). Note-gen already covered in 62nd addition.

**New repos:**

- **Plausible Analytics** (`plausible/analytics`) — open-source, privacy-first, cookie-free web analytics; lightweight Google Analytics alternative; no consent banner required; self-hosted or cloud; 29k★
  `git clone https://github.com/plausible/analytics`

- **Caddy** (`caddyserver/caddy`) — fast, extensible HTTP/1-2-3 web server with automatic HTTPS via Let's Encrypt; zero-config TLS; readable config files; 75k★
  `git clone https://github.com/caddyserver/caddy`

- **SearXNG** (`searxng/searxng`) — free, self-hostable internet metasearch engine that aggregates results from 70+ sources; tracks nobody; cheapest way to give an AI agent real web search without paid APIs; 36k★
  `git clone https://github.com/searxng/searxng`
  `docker run -d -p 8080:8080 searxng/searxng`

- **Addyosmani/Factory** (`addyosmani/factory`) — Claude Code Routine-based issue-triage factory: new GitHub issues trigger a fresh Claude Code session that triages, labels, and comments; ships an `ADVICE.md` explaining when stock Claude Code is already enough; MIT; 68★ (brand new, Aug 2026)
  `git clone https://github.com/addyosmani/factory.git`
  `cd /path/to/your/repo && /path/to/factory/install.sh --dry-run .`

- **Logseq** (`logseq/logseq`) — open-source, local-first knowledge-management app: outliner-based notes, tasks, and ideas organised in bidirectional graphs; desktop, web, and mobile; privacy-first, plain-text Markdown/Org storage
  `git clone https://github.com/logseq/logseq`

- **NocoDB** (`nocodb/nocodb`) — open-source Airtable alternative: turn any SQL database (Postgres, MySQL, SQLite, MariaDB) into a smart spreadsheet with API, forms, gallery, and Kanban views; 65k★
  `git clone https://github.com/nocodb/nocodb`
  `docker run -d -p 8080:8080 nocodb/nocodb:latest`

- **ERPNext** (`frappe/erpnext`) — open-source, full-stack ERP: accounting, inventory, manufacturing, HR, CRM, projects, and support in one self-hosted platform; 38k★
  `git clone https://github.com/frappe/erpnext`

- **Lago** (`getlago/lago`) — open-source usage-based billing and metering: Stripe-alternative for event-driven pricing; supports subscriptions, pay-as-you-go, hybrid models; 10k★
  `git clone https://github.com/getlago/lago`
  `docker compose up`

**Skills installed:**

- **`swiftui-design-skill`** (`Wholiver/swiftui-design-skill`) — Claude Code skill that teaches polished iOS/macOS SwiftUI UI design: spacing, typography, hierarchy, color, layout systems, brand integration, and design review; use when building SwiftUI views, choosing visual styles, or when UI looks generic; 165★
  `npx skills add Wholiver/swiftui-design-skill`

**Commands created:**

- **`/email-list-builder`** (`.claude/commands/email-list-builder.md`) — @earchoe 3-prompt email list building system: (1) Lead Magnet Builder — title, format, 10+ contents, landing page headline, opt-in copy, welcome email in one prompt; (2) Landing Page Copy — headline, subheadline, bullet points, button text, reassurance line; (3) Welcome Email — personal subject, downloaded-magnet acknowledgement, expectations para, one quick tip, CTA to reply. Usage: `/email-list-builder [your niche, audience, content topic, their biggest problem]`

**Reviewed and not added (63rd batch):**

| Repo / Tool | Reason skipped |
|---|---|
| `makeplane/plane` | Already in 47th addition |
| `uptime-kuma` | Already in recent addition |
| `trigger.dev` | Already in recent addition |
| `relaticle` | Already in recent addition |
| `openai/codex` | Covered via `codex-plugin-cc` (plugin table) |
| `multica-ai/andrej-karpathy-skills` | `forrestchang/andrej-karpathy-skills` already in 38th addition |
| `note-gen` | Already in 62nd addition |
| `mobile-app-ui-design` (6-skill pack) | No standalone GitHub repo identified — part of same @your.aimentor series as swiftui-design-skill |
| `addyosmani/factory` lead-magnet CTA | No content behind "Comment VAULT" CTA |

Paste-ready prompts from this batch:

**Lead Magnet Builder (@earchoe):**

> Build me a lead magnet I can create in 2 hours. My niche: [what you do] My audience: [who follows me] My content topic: [what your TikTok / content is about] Their biggest problem: [the thing they struggle with most] Give me: 1. Lead magnet title (specific, promise-driven, under 10 words) 2. Format (swipe file / checklist / mini guide / toolkit) 3. Exactly what is included (minimum 10 items) 4. Landing page headline and 3 bullet points 5. The opt-in form copy (headline + button text) 6. First email after they sign up (subject + 150-word welcome)

**Landing Page Copy (@earchoe):**

> Write the landing page copy for my free lead magnet. Lead magnet: [name of your magnet] What they get: [list the contents] Who it is for: [describe your audience] The one result they get from it: [specific outcome] Write: 1. Headline (under 10 words — the result they get) 2. Subheadline (who it is for and what is inside) 3. 3 bullet points (what they walk away knowing/having) 4. Email opt-in button text (not "Submit" — make it specific) 5. Below-button reassurance line ("No spam. Unsubscribe any time.")

**Welcome Email (@earchoe):**

> Write the welcome email for my new subscriber. Lead magnet they downloaded: [name] What they wanted when they signed up: [their goal] What my email list is about: [what I send regularly] My name and what I do: [brief intro] Email format: - Subject: make it personal, not promotional - Line 1: acknowledge what they just downloaded - Para 1: what they can expect from my emails - Para 2: one quick tip they can use today (from the magnet) - CTA: reply to this email with [specific question] — so I know what to focus on

### 64th addition — 0 new repos, 1 new command (6 MP4 TikTok videos)

**Batch:** 6 MP4 TikTok videos (`0bfce4fd-____________.zip`). 3 of 6 videos were unreadable (corrupt TikTok downloads with no valid duration). Actionable content extracted from 3 videos via ffmpeg frame extraction at multiple timestamps.

**Sources:**
- Video 1: @ai.honeycove — Graphly knowledge-graph visualiser + Claude Code security review demo
- Video 3: @automatedintelligenceai — Apodex 1.1 AI research agent (scientific work)
- Video 5: @promptbuilder.cc — FORGE, a 110-prompt 6-role marketing team system

**Informational only (no installable repos):**

- **Graphly** — web-based interactive knowledge graph that maps LLM/AI concepts and their relationships; nodes include agent frameworks, knowledge compilation paradigms, coding tools, model releases; communities visible include Claude Code Ecosystem, Agent Self-improvement, Knowledge Compilation, Claude Code Interfaces; web tool, no public GitHub repo identified
  `https://graphly.ai` (domain inferred from browser bar)

- **Apodex 1.1** — commercial AI research agent demonstrated doing complex scientific work (seawater carbonate system reconstruction, magnesium-alloy nanoindentation analysis); positioned as "frontier-level performance across Professional Work and Scientific Research — matching expert-level quality, leading complex open-ended research tasks"; not a self-hostable repo

**Command created:**

- **`/forge-marketing-team`** — @promptbuilder.cc FORGE system: 6 Claude marketing roles activated by slash command — `/seo` (search & rankings), `/social` (posts & reels), `/ads` (paid traffic), `/content` (copy & offers), `/inbound` (replies & leads), `/analytics` (numbers & decisions). Distilled from the 110-prompt FORGE file (MARKETING 45 prompts, SOCIAL 17, SMALL BUSINESS 31, FINANCE 8). Type `/[role] [task]` to activate a coworker.

**Paste-ready FORGE role activations:**

> /seo [task or URL] — activates SEO specialist for keyword research, on-page audits, content briefs, technical recommendations, SERP analysis

> /social [platform + topic] — activates social strategist for platform-native captions, reel scripts, content calendars, hashtag strategy, content repurposing

> /ads [platform + product/offer] — activates performance marketer for ad copy (Meta/Google/TikTok), audience targeting, A/B variants, landing page critique, budget allocation

> /content [format + product/topic] — activates conversion copywriter for sales pages, email sequences, offer positioning, VSL scripts, SEO blog posts

> /inbound [channel + scenario] — activates inbound specialist for DM reply scripts, comment templates, lead qualification questions, discovery call frameworks, warm-lead follow-ups

> /analytics [platform + question] — activates marketing analyst for KPI dashboards, campaign performance analysis, reporting structure, attribution models, ad manager/GA4 interpretation

---

## 65th Addition — 2026-08-27

**Batch:** 3 iCloud Photos zips (`1b56d730-iCloud_Photos.zip` [65a: 21 JPEGs + 1 MP4], `7d7b4faf-iCloud_Photos_1.zip` [65b: 6 JPEGs], `31da51a2-iCloud_Photos_2.zip` [65c: 30 JPEGs + 1 MP4]). Sources: @theromanknox Knox "120 Claude MCP" reference carousel (65a), @github.signals TikTok showcasing fathom-starmap (65a MP4), @junaid_jamel "Sites for Developers" (65b), @toolradar8 "5 hidden websites" (65c), @earchoe "AI Research System" (65c), @risenworks Claude review tips (65c), @tomm3hshipp GitHub Trending Aug 25 (65c), @github.signals TikTok showcasing Open Executive (65c MP4). 7 new repos, 1 new command, 9 paste-ready prompts.

**Repos added:**

- **[dryweather-2544/fathom-starmap](https://github.com/dryweather-2544/fathom-starmap)** — "Your Obsidian vault as a living 3D galaxy." Every note is a star; folders become colored constellations wrapped in nebula fog; links are threads of light; archived notes fall into a black hole. Real physics (notes repel, links attract, constellations form), galaxy shapes (spiral, disc, ring, shell, helix, torus, clusters), spaceship flight (W to take off, WASD thrusts). MIT license. Showcased by @github.signals.

- **[sentelabsai/openexecutive](https://github.com/SenteLabsAI/openexecutive)** — AI system that acts as your company's virtual executive team — a senior advisor with Harvard MBA-level knowledge customized for your business. Eight specialist AI agents: Chief Strategy Officer, Chief Financial Officer, CHRO/People Officer, General Counsel, Chief Operating Officer, Chief Marketing Officer, Chief Product Officer, Board Communications Director. Maintains episodic memory of decisions and initiatives across sessions; built-in scheduler surfaces follow-ups proactively. Apache 2.0, Python 3.11+, Next.js 15. Showcased by @github.signals.

- **[freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)** — Curated collection of 530 GPT-Image-2 prompts organized for rapid creative use. 17k stars, 1.8k forks. JavaScript. Source: @tomm3hshipp GitHub Trending Aug 25.

- **[anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)** — Community plugin marketplace for Claude Cowork and Claude Code. 1.6k stars. Python. Source: @tomm3hshipp GitHub Trending Aug 25.

- **[AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)** — Self-organizing AI second brain for Obsidian + Claude Code. 12k stars. Python. Source: @tomm3hshipp GitHub Trending Aug 25.

- **[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)** — Personal AI super intelligence, local-first memory. 38k stars, 3.7k forks. Rust. Source: @tomm3hshipp GitHub Trending Aug 25.

- **[marin-community/marin](https://github.com/marin-community/marin)** — Open-source framework for research and development of foundation models. 2.0k stars, 188 forks. Python. Source: @tomm3hshipp GitHub Trending Aug 25.

**Command created:**

- **`/ai-research-system`** (`.claude/commands/ai-research-system.md`) — @earchoe "The AI Research System: Learn Anything 10× Faster." Three-prompt learning system: `/feynman [topic]` (Feynman method — plain-language explanation, analogy, misconceptions, context, quiz), `/daily [work/challenges/goal]` (10-minute daily learning habit — one concept, 150-word explanation, weekly application, reflection question), `/content [notes + audience]` (research-to-content — turn Feynman notes into a 9-slide TikTok carousel with hook, six points, CTA, poll). Usage: `/ai-research-system [feynman | daily | content] [topic or context]`

**Informational only (no repo):**

- **@theromanknox "120 Claude MCP — Claude as Super Agent"** — reference carousel (skool.com/knox) mapping 120 MCP integrations across 12 categories of 10 each: Cat 01 Web & Browsing, Cat 02 Developer & Code, Cat 03 Databases & Data, Cat 04 Productivity & Work (Notion, Linear, Atlassian, Asana, ClickUp, Todoist, Obsidian, Monday.com, Trello, Airtable), Cat 05 Google & Microsoft, Cat 06 Communication, Cat 07 Marketing & Sales, Cat 08 Content & Creative, Cat 09 Automation & Workflows, Cat 10 AI Models & Memory, Cat 11 Cloud & DevOps, Cat 12 Finance & Business (Stripe, PayPal, Square, Plaid, Alpha Vantage, Polygon.io, Mixpanel, Amplitude, QuickBooks, Metabase)

- **@junaid_jamel "Sites for Developers"** — balsamiq.com (wireframing), codefronts.com, websiteprompts.ai, 3dicons.co (3D icons library)

- **@toolradar8 "The Internet Has A Hidden Side — 5 websites"** — radio.garden (live radio from anywhere on Earth), zoom.earth (real-time weather/satellite imagery), neal.fun (interactive experiments), 12ft.io (article paywall bypass)

- **@risenworks "6 ways to use Claude on work you did not write"** — built-in Claude Code `/code-review` workflow tips (targeting, noise level, bug tagging, REVIEW.md, neutral conclusion)

**Paste-ready AI Research System prompts:**

> **Feynman Method:** Teach me [topic/concept] using the Feynman method. Assume I am intelligent but know nothing about this topic. Step 1: Explain it in plain language — no jargon. Under 200 words. Step 2: Give me one real-world analogy that makes it click. Step 3: Tell me the 3 most common misconceptions people have about this. Step 4: Show me how this applies to [my specific context / business / niche]. Step 5: Give me 3 questions I should now be able to answer if I understood this. After I answer those questions, tell me what I missed or got wrong.

> **Daily Learning:** I have 10 minutes to learn something useful for my work today. My work: [what you do] Current challenges: [what you are struggling with] What I am trying to get better at: [skill or knowledge area] Give me: 1. One concept I should know that I probably do not yet 2. A 150-word explanation of that concept 3. How to apply it in my specific context this week 4. One question to reflect on before tomorrow Keep it tight. I need to be able to act on this today.

> **Research-to-Content:** I just learned this: [paste your Claude summary or Feynman notes] Turn it into a 9-slide TikTok carousel for my audience of [describe them]. Format: Slide 1: Hook (under 8 words — create curiosity without giving away the answer) Slides 2-7: One practical point per slide, explained simply Slide 8: The one action they should take today Slide 9: Poll — [suggest a relevant question] My tone: [direct / warm / educational] Do not use jargon. Assume they are smart but new to this topic.

---

## 66 — @earchoe AI Newsletter System · @__ai_slacker__ Vibecoding Prompts · @replace.so Analytics Repos · @datascibykas Claude Watermarks · @app.crafter Mobile Stack · @mydlytracker AI Projects · @structurewebworks AI Social OS

*Sources: 66a — 19 screenshots (TikTok carousels); 66b — 23 screenshots + 1 video (@structurewebworks)*

### Commands installed

**`/ai-newsletter-system`** — 2-prompt newsletter workflow from @earchoe "The AI Newsletter System: Build to 500 Paid Subscribers Without a Big Audience." Two sub-prompts:
- `/writer` — full weekly issue draft (subject line, hook, 300–400-word main section, quick win, CTA)
- `/subject` — generates 10 subject lines across 5 formulas, flags top 3 to A/B test
- Platform: Beehiiv (free to 2,500 subs, referral, paid subs, SEO-indexed)

**`/vibecoding-prompts`** — 5 structured prompts from @__ai_slacker__ "5 Prompts I Use While Vibecoding: From Blank Project → Polished UI." Five sub-prompts:
- `/build` — senior frontend engineer kickoff (structure, components, approach, then code)
- `/design` — visual system definition (layout, typography, colours, spacing, hierarchy)
- `/debug` — systematic root-cause fix (identify → explain → smallest fix → verify)
- `/modify` — minimal change protocol (list what changes, list what stays, make only that)
- `/think` — senior product designer critical review (weaknesses, gaps, 3 concrete improvements)

### Analytics repos (@replace.so "4 GitHub Analytics Repos That Shouldn't Be Free")

- **Plausible Analytics** — open-source, privacy-first, cookie-free web analytics; EU-hosted, self-hostable
- **Umami** — privacy-first web analytics, 38K+ GitHub stars, cookie-free, self-hosted
- **Talivia** — self-hosted revenue analytics; web tracking + session replay + payment integrations + attribution

### Carousels noted (no install action)

- **@datascibykas** — "How to Remove Claude Watermarks from Text, Code, and Files?" (7 slides): Claude uses SynthID-Text for text (statistical pattern in word choices), same for code (weaker — fewer arbitrary choices), and signed C2PA metadata for files (.png/.jpg/.svg). Text needs a full rewrite to remove; code needs real source transformation; files break with format conversion or re-save.
- **@app.crafter** — "Stop dreaming. Start building." mobile app stack guide (8 slides): framework (SwiftUI / Flutter / Expo+React Native), backend (on-device / Supabase / Appwrite+Firebase), shipping (TestFlight / EAS Build / App Store / Play Store), payments (RevenueCat / Adapty), AI copilots (Claude Code / Cursor / Codex / Antigravity), analytics (Firebase / Crashlytics / Microsoft Clarity / Sentry), distribution (TikTok+Reels / Instagram / Reddit / group chat).
- **@mydlytracker** — "4 AI Projects You Should Build in 2026": (1) AI data analyst — CSV in, plain-English questions, charts out; (2) Voice action assistant — speak naturally, AI asks when needed, uses tools; (3) MCP workspace agent — connects calendar/docs/tasks, suggests action, runs after approval; (4) Research agent — give it a messy question, it searches web + files, returns a cited brief.
- **@structurewebworks** — "AI Social Media Operating System" (video): 7-module pipeline — Research/Scraping Intelligence → Content Engine (write/narrate) → Production Studio (presenter/B-roll) → Distribution (auto cross-post) → Engagement (reply/capture) → Analytics (winning hooks fed back to research) → Monetization (leads convert to booked calls). Product demo, not open-source.

### Plain-text prompts to copy

**Weekly Newsletter Writer (@earchoe):**
> Write this week's newsletter for my [niche] audience. Newsletter name: [your name] This week's theme: [topic] Things that happened this week I can reference: [any news, personal events, learnings] Tool or resource to feature: [optional] Structure: 1. Subject line (under 50 chars — creates curiosity, not clickbait) 2. Opening hook (2-3 sentences — personal, relevant, conversational) 3. Main section (300-400 words — value, insight, or how-to) 4. Quick win (one thing they can do in under 10 minutes this week) 5. CTA (one action — reply, click, or share) Tone: [warm / direct / educational] — not corporate

**Subject Line Generator (@earchoe):**
> Write 10 subject line options for my newsletter this week. Topic: [what this issue covers] My audience: [who subscribes] Open rate goal: above 40% Formula options to use: - Curiosity gap: "Why I stopped doing X" - Number: "3 things I learned from X" - Personal: "I made a mistake last week" - Bold claim: "The AI tool everyone is sleeping on" - Question: "Are you making this mistake?" Flag which 3 you would A/B test first and why.

**BUILD — Start a New Project (@__ai_slacker__):**
> You are a senior frontend engineer. I'm building [PROJECT]. Goal: [WHAT IT DOES] Target users: [AUDIENCE] Tech stack: - [FRAMEWORK] - [STYLING] - [LIBRARIES] Core features: 1. [FEATURE] 2. [FEATURE] 3. [FEATURE] Before coding: 1. Propose the project structure. 2. Identify the key components. 3. Explain your implementation approach. 4. Then start building. Keep the architecture simple, scalable, and production-ready.

**DESIGN — Define the Visual System (@__ai_slacker__):**
> Design this interface with a [DESIGN STYLE] aesthetic. Design direction: - Layout: [DESCRIPTION] - Typography: [STYLE] - Colors: [PALETTE] - Spacing: [TIGHT / AIRY] - Components: [STYLE] - Visual hierarchy: [DESCRIPTION] Reference: [IMAGE / WEBSITE / DESIGN] Before implementing, explain: 1. The visual system 2. The layout hierarchy 3. The interaction patterns Then implement it. Do not add unnecessary elements. Prioritize clarity and consistency.

**DEBUG — Systematic Error Fix (@__ai_slacker__):**
> I have this error: [PASTE ERROR] Context: [WHAT I WAS DOING] Relevant code: [PASTE CODE] Debug this systematically. 1. Identify the root cause. 2. Explain why it is happening. 3. Identify the exact file/component responsible. 4. Propose the smallest correct fix. 5. Implement the fix. 6. Verify that the fix doesn't introduce another issue. Do not rewrite unrelated code.

**MODIFY — Change One Thing Without Breaking Others (@__ai_slacker__):**
> Modify the existing design. I want to change: [EXACT CHANGE] KEEP UNCHANGED: - Overall layout - Typography - Color system - Existing functionality - Responsive behavior - Component structure Before making changes: 1. Identify what needs to change. 2. Identify what must remain untouched. 3. Make the SMALLEST NECESSARY CHANGES. Do not redesign the page. Do not add new dependencies. Do not change unrelated components. Then verify the result across desktop and mobile.

**THINK — Senior Product Designer Review (@__ai_slacker__):**
> Act as a senior product designer reviewing this idea. My idea: [DESCRIBE IDEA] Target user: [TARGET USER] Current approach: [DESCRIBE APPROACH] Think critically about it. Tell me: 1. What's weak or unnecessary? 2. What's missing? 3. What would make it simpler? 4. What would make it more useful? 5. What would you change? Give me 3 CONCRETE IMPROVEMENTS I can implement immediately. Don't agree with me just to be helpful. Prioritize the best user experience.

---

## 67 — Tim Tsai New Team 30-Day Playbook · AIPlanetX Free Courses · Emilia Möller Claude Code Growth Marketing · Mo Bunnell Client Trust Model · McKinsey Agentic Change Levels

*Sources: 5 screenshots (LinkedIn/Twitter carousels)*

### Command installed

**`/new-team-30-days`** — 30-action leadership playbook from Tim Tsai "Your First 30 Days Leading a New Team." Six phases × 5 actions each:
- **Phase 1 — Listen Without an Agenda**: Open With a Question / Meet Everyone Once / Sit In as a Guest / Read Before You Ask / Track the Contradictions
- **Phase 2 — Learn How Work Actually Gets Done**: Follow the Handoffs / Learn the Workarounds / Find the Real Bottleneck / Watch the Actual Work / Name the Unwritten Rules
- **Phase 3 — Map the Team Behind the Org Chart**: Find the Informal Leader / Spot the Steady Contributor / Ask About the Last Leader / Watch Who People Follow / Learn What Changed Last Time
- **Phase 4 — Diagnose Before You Decide**: Separate People From Systems / Test Your First Theory / Ask What They'd Fix First / Follow the Recurring Complaint / Hold Your Verdict
- **Phase 5 — Build Trust Through Small Moves**: Fix One Small Thing Fast / Give Credit in Public / Deliver One Ask / Show Up on Time Every Time / Own Your Blind Spot
- **Phase 6 — Earn the Right to Change Something**: Name What You Learned / Pick One Change First / Explain the Why / Involve the Closest Person / Set the Next Checkpoint
- Usage: `/new-team-30-days [phase number or phase name]` — or run with no args for the full playbook

### Informational only (no install action)

- **AIPlanetX.com "9 Free Personal Development Courses"** — curated university courses: Improving Communication Skills (Wharton, 4.7★), Critical Thinking Fundamentals (Harvard, 4.8★), Rhetoric (Harvard, 4.9★), Negotiations (Wharton, 4.5★), The Nature of Genius (Yale, 4.8★), Managing Happiness (Harvard, 4.9★), The Psychology of Emotions (Cambridge, 4.6★), Finding Purpose and Meaning in Life (Michigan, 4.8★), The Science of Success (Michigan, 4.8★)

- **Emilia Möller "Claude Code for Growth Marketing"** — 9 marketing automations Claude Code can build without engineering: (1) Google Ads automation — BigQuery + Google Ads + GA4; (2) Figma creative plugin — Meta + Figma + Google Drive; (3) Meta Ads connection — Claude + Meta + GA4; (4) Ad testing system — PostHog + Meta + Google Ads; (5) Creative performance tracker — Figma + Meta + GA4; (6) Competitor monitor — Slack + Searchable + Firecrawl; (7) Programmatic SEO — DataForSEO + Webflow + GSC; (8) Landing page builder — Figma + GitHub + Vercel; (9) Marketing analytics — GA4 + BigQuery + Searchable

- **Mo Bunnell / BIG "Turn a Skeptical Client Into a Loyal One"** — U-curve trust model: clients start at "What's the catch?" → dip to "I don't think about them at all" → rise to "That was actually useful" → peak at "They're the first call I make." The lever is proactive giving: Expertise (insights they didn't ask for), Experiences (connecting them to events/people), Introductions (to the right person at the right moment), Insights (strategic observations about their world). Transition happens when giving shifts from transactional to genuinely other-focused.

- **McKinsey & Company "Agentic transformation is the next frontier of change"** — 4 agentic change levels (each builds on the prior):
  - **C1 — Execute**: Manage tactical change — OKRs, stakeholder analysis, communications plans, training
  - **C2 — Mobilize**: Win hearts and minds — address root mindsets, craft change story via inspiration and emotion, build capability
  - **C3 — Transform**: Drive performance and health — set bold goals, maintain a portfolio of initiatives, apply execution rigor, shift behaviors
  - **C4 — Reinvent**: Create value with new identity — address new customer needs, shift organizational identity, let go of the past, redefine leading as learning

### Plain-text prompt to copy

**New Team 30-Day Phase Coaching (Tim Tsai):**
> I'm in [PHASE NAME / PHASE NUMBER] of leading a new team. Current situation: [what you're observing or struggling with] Team size: [number] Industry/context: [brief description] Help me: 1. Identify which of the 5 actions in this phase I should prioritize. 2. Give me a specific script or question I can use today. 3. Flag any risk I should watch for in this phase. 4. Suggest the one thing I should NOT do right now.

---

## 68 — "How to Build an AI Agent" Aug 2026 Framework · @ajsilber Decision Making Frameworks · Anastasiia Shapovalova Claude Power User Guide · smarterwithai.news AI PowerPoint Alternatives · Hustle Badger Product Ops for AI-Native Teams

*Sources: 5 screenshots (LinkedIn/Twitter carousels and infographics)*

### Commands installed

**`/build-ai-agent-guide`** — 8-step AI agent building checklist from the Aug 2026 "How to Build an AI Agent" framework. Each step includes a focused prompt:
- **Step 1 — Define Purpose & Scope**: use case / user needs / success criteria / constraints
- **Step 2 — System Prompt Design**: goals / role-persona / instructions / guardrails
- **Step 3 — Choose LLM**: base model / reasoning effort level / context window / cost-latency tradeoff; includes Aug 2026 tool comparison table (ChatGPT GPT-5.6, Claude Opus 5, Perplexity, Cursor, Windsurf SWE-1.6, Claude Code Claude 5, Lindy, Zapier Agents, n8n, LangGraph, CrewAI, LlamaIndex)
- **Step 4 — Tools & Integrations**: simple/local / API / MCP server / AI-agent-as-tool / custom functions
- **Step 5 — Memory Systems**: episodic (conversation) / working memory / vector database / SQL-structured DB / file storage
- **Step 6 — Orchestration**: routes-workflows / triggers / parameters / message queues / Agent2Agent / error handling
- **Step 7 — User Interface**: chat / web app / API endpoint / Slack-Discord bot
- **Step 8 — Testing & Evals**: unit tests / latency testing / quality metrics / iterate-and-improve
- Includes a quick 8-item checklist at the end

**`/decision-frameworks`** — 6 decision-making frameworks from @ajsilber "Unlock the Power of Decision Making," each with an embedded paste-ready prompt:
- **RAPID**: Responsible / Accountable / Power to Decide / Informed / Deliver — clarifies accountability when multiple stakeholders are involved
- **DACI**: Driver / Approver / Contributors / Informed — streamlined role assignment for project decisions
- **Cynefin**: Simple (Clear) / Complicated / Complex / Chaotic / Disorder — matches the response approach to the problem's complexity domain
- **Decision Matrix**: weighted scoring grid — list options as columns, criteria as rows, weight × score, highest total wins
- **Pareto Principle (80/20)**: find the 20% of actions that drive 80% of outcomes; stop doing the 80% that produces 20%
- **SWOT Analysis**: Strengths / Weaknesses / Opportunities / Threats — strategic positioning for projects, products, or career moves
- Usage: `/decision-frameworks [rapid | daci | cynefin | matrix | pareto | swot] [decision or situation]`

### Informational only (no install action)

- **Anastasiia Shapovalova "Claude Power User Guide"** — comprehensive reference covering all five Claude capabilities: Artifacts (docs/dashboards/charts/code/spreadsheets/web pages; ask Claude to create, then edit, refine, download/publish); Skills (custom instructions/workflows/templates Claude can follow on demand — define in Claude Settings → Create Skill with name/description/instructions/examples); Connectors (Google Drive, Gmail, Slack, Notion, Salesforce, Web Search, MCP, Database, API, Calendar); Claude Code (generate/refactor code, explain codebases, write tests, debug, terminal/IDE, multi-file edits, run scripts, review PRs, security scan — slash commands: /explain, /refactor, /test, /fix, /doc, /review, /pr, /optimize, /security); Automation (Trigger → Scheduled Task → Action → Condition → Output → Integrate). Power Use Cases: Content Creation (Research → Outline → Draft → Refine → Publish), Research & Intelligence (Deep research → Analyze → Report → Share), Business Operations (Reports → Dashboards → Insights → Automate), Developer Workflow (Code → Test → Document → Deploy). Success Formula: Knowledge + Tools + Automation + Consistency = Freedom.

- **smarterwithai.news "AI-Powered Alternatives to PowerPoint"** — 9 tools with quick-compare picks:
  - **Gamma** — AI-first, prompt-to-deck, strong layout automation, web-based
  - **Decktopus AI** — guided creation, speed, templates
  - **Pitch** — collaborative, team workflows, brand consistency
  - **SlideSpeak** — doc-to-slides, summarizes uploaded documents, extracts insights
  - **Simplified** — all-in-one content suite with fast slide generation
  - **Plus AI** — in-slide assistant, works inside existing tools
  - **Designs.ai** — presentations + visuals + video + branding assets
  - **Haiku Deck** — visual storytelling, AI-assisted layout, simplicity focus
  - **Slidebean** — pitch decks, investor storytelling, structure-focused
  - Quick Compare: Fastest prompt-to-deck → Gamma, Decktopus AI; Best for teams → Pitch, Plus AI; Best for investors → Slidebean
  - Workflow: Prompt/Doc → Outline → Draft Slides → Design Polish → Present/Share

- **Hustle Badger "Why Product Ops is the key to an AI-Native Product Team"** — five-part framework for building an AI-native team layer:
  - The rationale: "team layer" = shared context, skills, tools, permissions that let each person's work make everyone else better; without it, the best workflow dies on one person's laptop
  - Job description: (1) Own the team's shared context (strategy, ICP, metric definitions, past decisions, insights); (2) Build internal tooling (feedback triage, research synthesis, competitor monitoring, exec updates); (3) Own quality — use evals to make sure automations actually work; (4) Own access — decide what agents can read/write and where humans get involved; (5) Drive adoption and prove the return
  - The proof: Anthropic pays $240–325K for Product Ops who "build the tools you need yourself" and have "written the prompts, built the evals"; Meta has Product Ops roles building autonomous agents for bug triage and running a model evals programme, open in five locations
  - Ideal candidate: shipped an AI workflow others use / systems thinker / technical enough to build and debug without being an engineer / sees process as a product / knows what good product work looks like
  - Key decisions: Context engineering (system prompt vs. skill vs. file vs. retrieval) / Agent architecture (deterministic workflow vs. agent loop) / Evals (define good quantitatively) / Observability (agents aren't black boxes) / Tool design (effective tool descriptions + which MCPs the team gets)

### Plain-text prompts to copy

**AI Agent Step 1 — Define Purpose & Scope:**
> My agent's use case is [X]. Its users are [Y]. I'll know it's working when [Z]. It must never [constraints]. Help me tighten this scope before I build.

**AI Agent Step 2 — System Prompt Design:**
> Help me write a system prompt for an agent that [use case]. It should act as [persona], always [positive behaviors], and never [negative behaviors]. Include guardrails for [edge cases].

**AI Agent Step 5 — Memory Architecture:**
> My agent needs to remember [X across sessions / Y within a session / Z about the user]. What memory architecture fits? Give me the tradeoffs between vector vs. SQL for my use case.

**AI Agent Step 8 — Evals:**
> Help me design an eval suite for my agent that [use case]. What should I test? What's a good golden dataset? How do I measure quality without human review on every output?

**RAPID Framework:**
> I need to make a decision about [DECISION]. The people involved are [LIST PEOPLE/ROLES]. Apply the RAPID framework: 1. Assign each role (R/A/P/I/D) to the right person. 2. Flag any gaps or conflicts in accountability. 3. Tell me what could go wrong if any role is unclear.

**Cynefin Framework:**
> I'm facing this challenge: [DESCRIBE SITUATION] Apply the Cynefin framework: 1. Which domain does this fall into (Simple, Complicated, Complex, Chaotic, Disorder)? 2. Why — what's the evidence for that classification? 3. What's the right response strategy for this domain? 4. What would make me reclassify it to a different domain?

**Decision Matrix:**
> I'm choosing between: [LIST OPTIONS] My decision criteria are: [LIST CRITERIA] Build a decision matrix: 1. Suggest weights for each criterion (1–3) based on my priorities. 2. Score each option on each criterion (1–10). 3. Show the weighted totals. 4. Recommend the winner and explain any caveats.

**Pareto Principle:**
> I'm trying to [GOAL] but have limited time/resources. Apply the Pareto Principle: 1. List all the possible actions/inputs I could take. 2. Identify the 20% that are likely to drive 80% of the outcome. 3. What should I stop doing (the 80% of effort with 20% of results)? 4. How do I validate my Pareto analysis — what data should I look at?

**SWOT Analysis:**
> I'm evaluating [PROJECT / PRODUCT / DECISION / CAREER MOVE]. Run a SWOT analysis: 1. Strengths: What internal advantages do I have? 2. Weaknesses: What internal gaps or limitations do I have? 3. Opportunities: What external trends or conditions could I exploit? 4. Threats: What external risks could hurt me? Then: Give me 2 strategic recommendations based on the SWOT.

---

## 69 — GitHub Trending Repos · Claude Code Setup Prompts · Multi-Agent Tools · Dev Utilities · Email Verification · AirPods on Linux · Windows 95

*Sources: 4 iCloud Photos zip files (`batch69a`: 28 JPEGs, `batch69b`: 12 JPEGs, `batch69c`: 60 JPEGs + 2 MP4 videos, `batch69d`: 9 JPEGs). Sources include GitHub Trending screenshots (@tomm3hshipp-style), @appmillers (Elshad Karimov), @jackroberts__, @structurewebworks, @freedombuilderai, @aicareersuite. 21 new repos documented; 1 new command created.*

**Duplicate-check (skip):**

| Repo / Tool | First documented |
|---|---|
| garrytan/gstack | 39th addition |
| wshobson/agents | 40th addition |
| affaan-m/ECC | 62nd addition |
| Alishahryar1/free-claude-code | 62nd addition (as Alishahryar-one/FREE-CLAUDE-CODE) |
| HKUDS/ViMax | 65th addition area |

### Command installed

**`/claude-power-prompts`** — 4 power prompts for Claude Code environment setup from @appmillers (Elshad Karimov) and @jackroberts__:
- **`claudemd`** — interactive CLAUDE.md builder: Claude asks about your business, voice, banned words, output defaults, and working style, then writes to `~/.CLAUDE.md`
- **`memory`** — persistent memory for corrections: every correction you make is saved as a dedicated `.md` file at `~/.claude/projects/{project}/memory/` and indexed in `MEMORY.md` for future sessions
- **`routine`** — schedule any Claude skill or sub-agent on Anthropic's cloud on a repeating schedule; output drops into a folder, Notion page, or connected tool
- **`dashboard`** — Jarvis OS one-screen dark dashboard: laptop health, list of Claude commands, today's schedule, live Obsidian vault notes (no tabs, no scrolling) — from @jackroberts__ Jarvis OS setup

### Repos added

**From batch69a — GitHub Trending / tool carousels:**

- **[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)** — AI tutoring system from the HKUDS lab (same org as ViMax); interactive learning agent that explains concepts at multiple depth levels
  `git clone https://github.com/HKUDS/DeepTutor`

- **[`Fincept-Corporation/FinceptTerminal`](https://github.com/Fincept-Corporation/FinceptTerminal)** — open-source financial terminal CLI; real-time market data, portfolio tracking, and financial analysis from the command line; Python-based
  `git clone https://github.com/Fincept-Corporation/FinceptTerminal`

- **[`CJackHwang/ds2api`](https://github.com/CJackHwang/ds2api)** — wraps DeepSeek models as an OpenAI-compatible REST API; lets any OpenAI SDK client (Python, JS, Claude Code, etc.) call DeepSeek without changing client code
  `git clone https://github.com/CJackHwang/ds2api`

- **[`siddharthvaddem/openscreen`](https://github.com/siddharthvaddem/openscreen)** — browser-based open screen sharing / screen broadcasting tool; no install required for viewers
  `git clone https://github.com/siddharthvaddem/openscreen`

- **[`Z4nzu/hackingtool`](https://github.com/Z4nzu/hackingtool)** — collection of ethical hacking tools for Linux organized by category (web, network, OSINT, forensics, cracking, etc.); Python-based menu installer
  `git clone https://github.com/Z4nzu/hackingtool`

- **[`AIDC-AI/Pixelle-Video`](https://github.com/AIDC-AI/Pixelle-Video)** — AI video generation model from Alibaba AIDC-AI; text-to-video and image-to-video generation
  `git clone https://github.com/AIDC-AI/Pixelle-Video`

- **[`google-ai-edge/LiteRT-LM`](https://github.com/google-ai-edge/LiteRT-LM)** — Google's on-device LLM inference runtime (successor to TensorFlow Lite); runs large language models locally on mobile/edge devices; powers Gemma on-device
  `git clone https://github.com/google-ai-edge/LiteRT-LM`

- **[`trycua/cua`](https://github.com/trycua/cua)** — computer-use agent framework; gives AI agents the ability to control a computer (cursor, keyboard, screen) similar to Anthropic's computer-use but as a self-hostable open-source system
  `git clone https://github.com/trycua/cua`

- **[`huggingface/ml-intern`](https://github.com/huggingface/ml-intern)** — Hugging Face's ML intern utilities: tooling and scaffolding for ML tasks, experiments, and model work; used internally and released as open-source
  `git clone https://github.com/huggingface/ml-intern`

- **[`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail)** — AI agent code output minimizer; forces coding agents to produce short, focused, minimal responses; resolves the incomplete README entry at batch 41 ("no verified repo found") — 115k★
  `git clone https://github.com/DietrichGebert/ponytail`

**From batch69b/69c — tool carousels and GitHub Trending:**

- **[`kavishdevar/librepods`](https://github.com/kavishdevar/librepods)** (26.8k★) — LibrePods: use AirPods on Android and Linux with full feature support (ear detection, battery, noise control); no iOS required; Kotlin/Python
  `git clone https://github.com/kavishdevar/librepods`

- **[`felixrieseberg/windows95`](https://github.com/felixrieseberg/windows95)** (24.1k★) — Windows 95 running inside an Electron app; runs on Mac, Windows, Linux; the actual Windows 95 OS in a desktop window for nostalgia, demos, and retro computing; MIT
  `git clone https://github.com/felixrieseberg/windows95`

- **[`pinchtab/pinchtab`](https://github.com/pinchtab/pinchtab)** (8.9k★) — Browser Control for AI Agents: MCP-compatible browser automation tool that lets Claude and other agents control Chrome/Firefox tabs programmatically; TypeScript
  `git clone https://github.com/pinchtab/pinchtab`

- **[`pranshuparmar/witr`](https://github.com/pranshuparmar/witr)** (14.7k★) — `witr`: CLI that explains why a process is running — shows the reason, parent chain, and resource usage for any PID; useful for debugging mystery processes; Rust
  `cargo install witr`

- **[`reacherhq/check-if-email-exists`](https://github.com/reacherhq/check-if-email-exists)** (8.6k★) — Rust library and self-hostable API to verify whether an email address exists without sending an email; checks MX records, SMTP handshake, and mailbox existence; powers Reacher
  `git clone https://github.com/reacherhq/check-if-email-exists`

- **[`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)** (33.2k★) — generates a full CLI interface for any program so AI agents can drive it; converts any tool (GUI app, web service, Python script) into a command-line interface that agents can invoke; install as a Claude Code skill:
  `npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`

- **[`DigitalPlatDev/FreeDomain`](https://github.com/DigitalPlatDev/FreeDomain)** (160k★) — nonprofit project offering free domain registration for individuals and small projects; register a real domain at no cost; sponsored by community
  `git clone https://github.com/DigitalPlatDev/FreeDomain`

- **[`ayghri/i-have-adhd`](https://github.com/ayghri/i-have-adhd)** (25k★, 1.6k forks) — ADHD-friendly output skill for coding agents; instructs Claude Code, Cursor, and Codex to structure responses in short, clearly chunked, distraction-minimizing format; install as a skill:
  `npx skills add ayghri/i-have-adhd`

- **[`VERT-sh/VERT`](https://github.com/VERT-sh/VERT)** (14.7k★) — VERT: web-based file converter supporting 250+ formats (audio, video, image, documents, fonts) entirely via WebAssembly — no server, no upload, everything runs in the browser; self-hostable
  `git clone https://github.com/VERT-sh/VERT`

- **[`pear-devs/pear-desktop`](https://github.com/pear-devs/pear-desktop)** (31.5k★) — Pear Desktop: open-source desktop client for YouTube Music; native-feeling app with offline support, playlist management, and no ads; Electron/TypeScript
  `git clone https://github.com/pear-devs/pear-desktop`

- **[`stab1yai/orca`](https://github.com/stab1yai/orca)** (56k★, 3.8k forks) — Orca: Agent Development Environment (ADE) for running multiple coding agents in parallel side by side — Codex, Claude Code, OpenCode, and Pi in one workspace; resolves the incomplete ORCA entry from batch 34 ("from @lunktech, no GitHub slug captured") — this is the specific repo
  `git clone https://github.com/stab1yai/orca`

### Informational only (no install action)

- **@structurewebworks MP4 — "55 AI Agents Run an Entire Automotive Company"** — TikTok video showing a multi-agent orchestration system where 55 specialized AI agents handle all functions of an automotive company (sales, supply chain, customer service, quality control, etc.); architecture demo, no public repo
- **@structurewebworks MP4 — "Claude AI Sales System"** — demonstration of a Claude-powered sales system managing the full pipeline from lead capture through close; informational
- **@aicareersuite "Build Your Own CRM" (9 slides, batch69d)** — step-by-step guide: (1) Capture leads automatically from Forms/Website/WhatsApp/Social DMs, (2) Organise every lead with Name/Source/Status/Notes/Owner fields, (3) Automate follow-ups (new lead → CRM → send email + WhatsApp + create task), 4 core parts: Lead Capture / Contact Records / Sales Pipeline / Tasks & Reminders; simple stack: Forms → n8n Automation → CRM Database → Email & WhatsApp → Dashboard; informational

### Plain-text prompts to copy

**Build your CLAUDE.md:**
> Help me build my CLAUDE.md from scratch. Ask me about my business, my voice, my banned words, my output defaults, and how I want you to work. Save it to ~/.CLAUDE.md.

**Enable persistent memory for corrections:**
> From now on, whenever I correct you, save it as its own .md file at ~/.claude/projects/{project}/memory/. Index everything in MEMORY.md.

**Schedule a Claude Routine on the cloud:**
> Create a Claude Routine that runs my [skill or sub-agent] every [schedule]. Run it on Anthropic's cloud, not my laptop. Drop the output into [folder, Notion page, or tool].

**Jarvis OS dark dashboard:**
> Build me a dark dashboard on one screen: how my laptop is doing, my list of commands, today's schedule, and live notes from my Obsidian vault. No tabs, no scrolling.

---

## 70. GitHub Trending, AI Courses, Team Tools & Product Frameworks (Batch 70)

*Sources: batch70a (8 images + TikTok MP4) and batch70b (44 images) — frameworks, trending repos, AI courses, messaging tools, and ML resources*

### New commands installed

- **`/product-execution-pillars`** — 5 Pillars of Product Execution framework: **Docs**, **Prioritisation**, **Team Rhythm**, **Velocity**, **Projects**; each pillar has a structured prompt template for coaching yourself or your team through it; run with no args for the full checklist, or name a pillar to dive in
  `File: .claude/commands/product-execution-pillars.md`

- **`/strategic-thinking`** — Natan Mohart's 8 Elements of Strategic Thinking: **Vision**, **Analysis**, **Problem Solving**, **Focus**, **Synthesis**, **Storytelling**, **Decisiveness**, **Adaptability**; each element has a coaching prompt; run with no args to see all 8, or name an element
  `File: .claude/commands/strategic-thinking.md`

### New repos to clone

- **[`Shubham-Saboo/awesome-llm-apps`](https://github.com/Shubham-Saboo/awesome-llm-apps)** — Awesome LLM Apps: curated collection of LLM-powered apps and examples built with Retrieval-Augmented Generation (RAG), multi-agent systems, and fine-tuning; was #1 on GitHub Trending
  `git clone https://github.com/Shubham-Saboo/awesome-llm-apps`

- **[`x1xhlol/system-prompts-and-models-of-ai-tools`](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** (135k★, 33.9k forks) — comprehensive collection of leaked and reverse-engineered system prompts for Claude Code, Cursor, Devin AI, Windsurf, v0, Bolt, Perplexity, and 20+ other AI tools; reveals model identities and operational instructions
  `git clone https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools`

- **[`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners)** — Microsoft Learn course: building AI agents from scratch; covers agent architectures, tool use, multi-agent systems, and evaluation; also available at `aka.ms/ai-agents-beginners`
  `git clone https://github.com/microsoft/ai-agents-for-beginners`

- **[`microsoft/AI-For-Beginners`](https://github.com/microsoft/AI-For-Beginners)** — Microsoft AI curriculum (Microsoft Foundry); full AI course covering classical AI, neural networks, NLP, CV, and modern LLMs; also at `aka.ms/ml-beginners`
  `git clone https://github.com/microsoft/AI-For-Beginners`

- **[`frappe/raven`](https://github.com/frappe/raven)** — Raven: open-source team messaging app with built-in AI (Chat + AI); Frappe-based, self-hostable, 350+ active sites; replaces Slack for teams on the Frappe ecosystem
  `git clone https://github.com/frappe/raven`

- **[`Avik-Jain/100-Days-Of-ML-Code`](https://github.com/Avik-Jain/100-Days-Of-ML-Code)** (11.4k forks) — 100 Days of ML Code: Siraj Raval challenge; structured day-by-day ML learning with code, infographics, and practical implementations; covers supervised/unsupervised learning, deep learning, NLP
  `git clone https://github.com/Avik-Jain/100-Days-Of-ML-Code`

- **[`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli)** — Gemini CLI: Google's official command-line AI agent powered by Gemini; runs in the terminal similar to Claude Code; part of Google's full-stack AI ecosystem (alongside Stitch, Google ADK, Agent2Agent protocol, Jules, Veo)
  `git clone https://github.com/google-gemini/gemini-cli`

### Self-hosted tools noted (repo slugs not confirmed in images)

- **Atomic** — self-hosted AI knowledge base (1.6k★); converts Markdown into linked articles with semantic search and a visual knowledge graph; local-first; no public repo slug confirmed in images — search GitHub for "atomic knowledge base"

- **Haptic** — open-source local-first Markdown note-taking app; available as both a desktop client and self-hosted web app; no public repo slug confirmed in images — search GitHub for "haptic notes"

- **Panaversity Learn Agentic AI (DACA)** — "Learn Agentic AI using Dapr Agentic Cloud Ascent Design Pattern"; full learning path for production-grade agentic AI systems; no public repo slug confirmed in images — search GitHub for "panaversity agentic ai"

### Skipped (already in README)

- `mukul975/Anthropic-Cybersecurity-Skills` — already indexed in a prior batch
- `excalidraw/excalidraw` — already indexed in a prior batch

### Informational only (no install action)

- **Google Full-Stack AI Ecosystem (@aigenesis.official)** — carousel covering Gemini family (Flash/Pro/Ultra/Nano/Exp), Stitch (AI UI generator), Google ADK (Agent Development Kit), Agent2Agent (A2A) protocol, Gemini CLI, Jules (autonomous coding agent), NotebookLM, Veo 3.1; informational overview
- **@nateherkai TikTok — "Claude Automations"** — overview of Claude Code automation capabilities; informational
- **Ninja AI Tools carousel (Brad Gaines, @ninjaaitools)** — 7-category AI tool overview: AI Video, AI Writing, AI Voice, AI Research, AI Coding, AI Presentations, AI Meetings, Image Generation; informational
- **@martiendejong_dev slides** — "What Will Businesses Look Like By 2050?" business futures series; informational
- **@user5672829910 AI tools** — Otter.ai (transcription), Humata AI (PDF Q&A), Remove.bg (background removal), Glasp.co (web highlighter/summarizer), Eightfold.ai (HR/talent AI), PIXAI.ART (AI image gen, "better than DALL-E"); informational web tools

### Plain-text prompts to copy

**Run the 5 Pillars of Product Execution framework:**
> I want to improve my team's execution. Walk me through the 5 Pillars framework: Docs, Prioritisation, Team Rhythm, Velocity, and Projects. Start by asking me which pillar hurts the most right now.

**Run the Strategic Thinking 8 Elements:**
> Help me think more strategically. Use the 8 Elements of Strategic Thinking framework: Vision, Analysis, Problem Solving, Focus, Synthesis, Storytelling, Decisiveness, and Adaptability. Ask me about the challenge I'm facing and which element I want to strengthen.

**Explore system prompts of AI tools:**
> I want to understand how [Claude Code / Cursor / Devin / Windsurf / v0] works under the hood. Pull from the system-prompts-and-models-of-ai-tools repo and summarize what the system prompt reveals about its design philosophy, persona, and key rules.

**Build a Gemini CLI workflow:**
> Set up Gemini CLI and help me create a workflow that does [task]. Compare it to how I'd do the same thing in Claude Code.

## 71. Claude Code 301, Hermes Content Factory, YouTube→Skill & Career Tools (Batch 71)

*Sources: 8 MP4 TikTok videos — advanced Claude Code features, multi-agent content pipeline, skill-building technique, resume gap analysis*

### New commands installed

- **`/claude-code-301`** — @hackproduct9's 9 advanced Claude Code features: **Monorepo Skills** (package-scoped skill loading), **Path Rules** (`paths:` frontmatter scopes rules to file globs), **Context Budget** (CLAUDE.md always / rules on match / skills on demand), **Marketplaces** (`/plugin marketplace add`), **Managed Policy** (`managed-settings.json` — org rules nobody skips), **Symlinked Rules** (`ln -s ~/.standards .claude/rules`), **Headless** (`claude -p "..."` for CI), **Agent SDK** (TS/Python/Go/C# — Claude inside your product), **Permission Layers** (deny anywhere beats allow everywhere)
  `File: .claude/commands/claude-code-301.md`

- **`/hermes-content-factory`** — @hackproduct9's Mental Model 03: ONE BRIEF → LOCAL AGENT TEAM → SIX CHANNELS multi-agent content pipeline; architecture: Weekly Trend Brief → Hermes Orchestrator → Claude (reason+write) + Codex (build+validate) + Capability Dock (Skills/Plugins/Tools) → 3 parallel researchers (Primary Sources / Trends+News / User Questions, top 5 each) → Synthesis Agent (Merge→Rank→Verify→Cite) → 6 channel outputs (Telegram, WhatsApp, Slack, Twitter, LinkedIn, Newsletter); principle: "Evidence merges before anything is created."
  `File: .claude/commands/hermes-content-factory.md`

- **`/youtube-to-skill`** — @bengusberg's technique for converting any YouTube video transcript into a reusable Claude Skill; 5-step process: get transcript (YouTube UI / yt-dlp / Claude) → extract methodology → structure as SKILL.md → install → test; includes full one-shot prompt; works best with framework videos, prompt engineering guides, productivity systems, technical tutorials
  `File: .claude/commands/youtube-to-skill.md`

- **`/resume-gap-analysis`** — @nathanhodgson.ai's 4-part career workflow: paste resume + job description → Claude acts as a strict corporate recruiter → (1) Gap Analysis: hard skills comparison + top 5 missing keywords + 3 experience red flags, (2) Tailored CV: keyword-optimized rewrite, (3) Cover Letter: 3-paragraph targeted letter, (4) ATS Score: 0–100 match score + formatting flags; includes full one-shot prompt for all four outputs at once
  `File: .claude/commands/resume-gap-analysis.md`

### Informational only (no install action)

- **AI2UI / Verdent.ai (@verdent.ai)** — "One image. Working UI." — Verdent.ai is a commercial agentic coding product (parallel agents, Plan Mode, BYOK, Eco Mode; VS Code + JetBrains + Mac + Windows); turns screenshots/images into working UI code; no public open-source repo; website: verdent.ai; GitHub org: `github.com/verdentAI` (docs only), `github.com/verdent-ai` (demo projects)

- **@nutressniftt — innerbody.com health content** — health information platform; not relevant to development tooling

- **@valeridoesai — AI Motion Tool** — "This site replaced motion designers"; AI-generated motion graphics/animation tool; informational

- **@anastasia.crypto.analyst — 15 Tools for Working with AI** — intro frame only; insufficient detail

### Plain-text prompts to copy

**Claude Code 301 — run all 9 advanced features:**
> Walk me through the 9 advanced Claude Code features from the 301 guide: Monorepo Skills, Path Rules, Context Budget, Marketplaces, Managed Policy, Symlinked Rules, Headless mode, the Agent SDK, and Permission Layers. For each one, show me the exact config or command I need to set it up.

**Hermes Content Factory — run the full pipeline:**
> Run the Hermes Content Factory pipeline on this brief: [PASTE BRIEF]. 1) Dispatch three parallel researchers: primary sources, trends+news, user questions (top 5 each). 2) Run the synthesis agent: merge → rank → verify → cite all findings. 3) Generate content for each channel: Telegram, WhatsApp, Slack, Twitter, LinkedIn, Newsletter. Return all six channel outputs, each formatted for that platform.

**YouTube → Claude Skill:**
> I want to turn this YouTube video into a Claude Code skill. Here is the transcript: [PASTE TRANSCRIPT]. 1) Extract the core methodology, steps, principles, and any templates shown. 2) Write the full SKILL.md file with proper YAML frontmatter. 3) Save it to .claude/skills/[skill-name]/SKILL.md. 4) Tell me how to invoke it.

**Resume gap analysis (one-shot):**
> Act as a meticulous corporate recruiter. Analyze my attached resume against this job description [Insert Job Description]. Perform a strict gap analysis and provide: 1. A hard comparison of required skills vs. my stated experience. 2. The top 5 technical and soft keywords missing from my resume. 3. Three specific professional gaps or experience red flags.

**Full resume → tailored CV + cover letter + ATS score:**
> Act as a meticulous corporate recruiter and career strategist. MY RESUME: [PASTE]. JOB DESCRIPTION: [PASTE]. PART 1 — Gap Analysis: hard skills comparison, top 5 missing keywords, 3 red flags. PART 2 — Tailored Resume: rewrite with missing keywords, reframe experience, reorder sections. PART 3 — Cover Letter: 3 paragraphs, under 300 words, specific opening hook, address top gaps, clear CTA. PART 4 — ATS Score: 0–100 score, keyword match/gap list, formatting flags, 3 improvements.

## 72. Marketing Frameworks, LinkedIn Brand, Critical Thinking & WolfCut (Batch 72)

*Sources: 4 images + 1 MP4 TikTok video — psychology-backed marketing frameworks, LinkedIn personal brand system, 48 critical thinking questions, 20 business prompts, open-source video editor*

### New commands installed

- **`/marketing-frameworks-7`** — 7 psychology-backed marketing frameworks: **Jobs To Be Done** (hire products for a job), **95-5 Rule** (only 5% ready to buy today — build brand for the 95%), **Peak-End Rule** (memory = peak + ending), **Anchoring** (first impression = reference point), **Information Gap Theory** (curiosity = gap in knowledge → hooks go viral), **Growth Loops vs Funnels** (loops compound; funnels leak), **Memory Structure** (situational cues beat feature lists); each framework has a why + how-to-apply + coaching prompt
  `File: .claude/commands/marketing-frameworks-7.md`

- **`/linkedin-personal-brand-2026`** — Josh Sanders' 9-element LinkedIn system: (1) **North Star** (one direction, 90 days), (2) **Positioning Triangle** (skills × market problem × unique take), (3) **Audience Clarity Map** (Buyers / Aspirational Followers / Learners), (4) **Content OS** (Teach / Think / Build / Sell lanes), (5) **Attention Engine** (60+120+15+20 min weekly rhythm), (6) **Trust Ladder** (Awareness→Relevance→Authority→Proof→Action), (7) **Content Feedback Loop** (Measure→Learn→Improve weekly), (8) **3-Level Brand Funnel** (reach / trust / proof), (9) **Growth Scorecard** (5 metrics: views, followers, engagement, inbound leads, newsletter signups)
  `File: .claude/commands/linkedin-personal-brand-2026.md`

- **`/critical-thinking-48`** — Justin Wright's 48 critical thinking questions across 6 categories (8 per category): **Who**, **What**, **Where**, **When**, **Why**, **How**; covers stakeholder mapping, evidence analysis, root cause, timing, significance, implementation; includes full-analysis, single-category, assumption-challenge, and decision-review prompt modes
  `File: .claude/commands/critical-thinking-48.md`

- **`/business-prompts-20`** — 20 fill-in-the-bracket business prompts from smarterwithai.news: Content Calendar, Press Release, Email Sequence, Social Media Copy, Competitor Analysis, Customer Objections, Follow-Up Emails, Customer Survey, Support Responses, Sales Pitch, SWOT, Onboarding Checklist, PM Framework, Meeting Agenda, Business Continuity Plan, Financial Forecast, Pricing Strategy, Fundraising Pitch, Cost-Cutting Framework, Market Expansion Strategy
  `File: .claude/commands/business-prompts-20.md`

### New repos to clone

- **[`jub0t/WolfCut`](https://github.com/jub0t/wolfcut)** — WolfCut: free, open-source CapCut replacement; native Rust engine + React UI, runs on macOS/Windows/Linux via Tauri; no account, no watermarks, no paywalls; features: multi-track timeline, free voice filters, free local auto-captions (transcription); v0.1.0, MPL-2.0 license; from @github.signals
  `git clone https://github.com/jub0t/wolfcut`

### Informational only (no install action)

- No additional informational-only items in this batch

### Plain-text prompts to copy

**Apply 7 Marketing Frameworks to your business:**
> I want to analyze my marketing using all 7 psychology-backed frameworks. My business is [DESCRIBE]. Walk me through: Jobs To Be Done, the 95-5 Rule, Peak-End Rule, Anchoring, Information Gap Theory, Growth Loops vs Funnels, and Memory Structure. For each one, tell me what I'm doing well and what I should change.

**Build LinkedIn Personal Brand (9-element system):**
> Help me build my LinkedIn personal brand using Josh Sanders' 9-element system. Start with my North Star: my background is [DESCRIBE], my current goals are [DESCRIBE]. Walk me through all 9 elements and help me complete each one.

**Run 48 Critical Thinking Questions on a problem:**
> I'm facing this situation: [DESCRIBE SITUATION]. Walk me through all 6 categories of the 48 critical thinking questions (Who, What, Where, When, Why, How). For each question, answer it based on what I've described or flag what information I'd need to answer it. At the end, tell me the top 5 questions I most need to resolve.

**Use the 20 Business Prompts (pick one):**
> Run prompt #[NUMBER] for my business: [YOUR BUSINESS/PRODUCT/SERVICE]. Fill in the template with details about [RELEVANT CONTEXT].

---

## Batch 73

### New commands / skills installed

- **`/seo-prompts-10`** — 10 fill-in-the-bracket SEO prompts: SEO Audit (comprehensive site analysis + action plan), TASM (Total Addressable Search Market mapping), Search Intent Reverse Engineering, Programmatic SEO Template Generator, Entity-Optimised Article Creator, Topical Authority Builder (pillar + cluster plan), SERP Competitor Teardown, BOFU Content Finder (comparison/review/price keywords), LLM SEO (optimise for ChatGPT/Perplexity/AI Overviews), Untapped Demand (low-competition keyword finder)
  `File: .claude/commands/seo-prompts-10.md`

- **`/time-management-leaders`** — Tim Tsai's 9 time management techniques for leaders, each with coaching prompt: Not-To-Do List (Tim Ferriss — eliminate before optimising), Focusing Question (Gary Keller — one thing that unlocks everything), Ivy Lee Method (6 tasks in order every day), Deep Work Blocks (Cal Newport — protect uninterrupted focus), Two-Minute Rule (David Allen — do it now or schedule it), Task Batching (Cal Newport — group similar work), Parkinson's Law (shorter deadlines force focus), Weekly Review (David Allen — weekly maintenance ritual), Calendar Audit (David Allen — reclaim time from dead meetings)
  `File: .claude/commands/time-management-leaders.md`

- **`/linkedin-lead-post-types`** — 5 LinkedIn post types that generate leads, each with structure and coaching prompt: Storytelling Post (problem → feeling → frustration → lesson → life after), Framework Share (process → steps → stack frameworks → hold nothing back), Contrarian Take (position → accepted wisdom → proof → unspoken truth; avoid controversy for its own sake), Case Study (starting numbers → process → outcome with figures → client quote), Direct Offer (earn right first → announce explicitly → one CTA; ~1 in 4–5 posts)
  `File: .claude/commands/linkedin-lead-post-types.md`

### New repos to clone

- No new repos in this batch

### Informational only (no install action)

- No additional informational-only items in this batch

### Plain-text prompts to copy

**Run the 10 SEO Prompts (pick one):**
> Run SEO prompt #[NUMBER] for my website/niche: [YOUR URL OR NICHE]. Fill in all brackets with my specifics and give me a complete, actionable output.

**Full SEO audit prompt:**
> You are an SEO expert. Conduct a comprehensive SEO audit of [website URL]. Analyse the following areas and provide specific, actionable recommendations: Technical SEO: Site speed, mobile-friendliness, crawlability, indexing issues, Core Web Vitals, and HTTPS security. On-Page SEO: Title tags, meta descriptions, header structure, keyword usage, internal linking, and content quality. Content Strategy: Identify content gaps, thin content, and opportunities for new, high-ranking content. Backlink Profile: Assess the quality and quantity of backlinks, identify toxic links, and suggest link-building opportunities. User Experience: Evaluate site navigation, design, and how it impacts SEO performance. Create a prioritised action plan with specific solutions for each issue found.

**Apply the Focusing Question (Gary Keller):**
> My current priorities are: [LIST YOUR PRIORITIES OR PROJECTS]. Apply the Focusing Question: What is the ONE thing I can do this week such that by doing it, everything else becomes easier or unnecessary? Then tell me the ONE thing for today, what's blocking me from doing only that, and how I should restructure my schedule around it.

**Run the Ivy Lee Method:**
> Here is my full task list for tomorrow: [LIST ALL TASKS]. Apply the Ivy Lee Method: select the 6 most important tasks, rank them 1–6 by importance and impact, explain your ordering, and tell me what to do with everything that didn't make the top 6.

**Write a LinkedIn Storytelling Post:**
> I want to write a Storytelling Post on LinkedIn about: [YOUR STORY]. My audience is [WHO READS YOUR CONTENT]. My offer/expertise is [WHAT YOU DO]. Write the post using this structure: (1) Hook — 1 line that names the problem and stops the scroll, (2) Day-to-day feeling — 2–3 lines, (3) Frustration — the breaking point, (4) Lesson — the insight or decision, (5) Life after — what changed, (6) Closing question or CTA. Write 2 versions: one more vulnerable, one more professional. Keep each under 200 words.

**Write a LinkedIn Framework Share post:**
> I want to write a Framework Share post on LinkedIn. My process: [DESCRIBE THE PROCESS OR SYSTEM YOU USE]. My audience: [WHO NEEDS THIS]. Write the post with a hook, brief context, numbered steps (each named and explained), and a closing save-this line. Also give me 3 hook variations to test.

**Write a LinkedIn Case Study post:**
> I want to write a Case Study post on LinkedIn. Client situation before: [STARTING NUMBERS AND CONTEXT]. What we did: [THE PROCESS — be specific]. Results: [OUTCOME IN REAL NUMBERS]. Client quote: [QUOTE IF AVAILABLE]. Write the post with hook, starting situation, process, outcome, quote, and a soft CTA. Keep it under 250 words. Make the numbers the star.

---

## 74. Open-Source App Alternatives + Claude Code Commands Reference (Batch 74)

**Sources:** @joshualevi.ai (7 paid-app alternatives carousel), @korolev.timm (Claude Code commands), plus b74a/b74b tool carousels

### Repos to Clone

**Self-hosted & privacy tools:**
- [`immich-app/immich`](https://github.com/immich-app/immich) (113K★) — self-hosted photo and video backup; open-source Google Photos alternative with mobile apps, face recognition, and albums
- [`mattermost/mattermost`](https://github.com/mattermost/mattermost) (39K★) — open-source, self-hostable team messaging; Slack alternative with channels, threads, and integrations

**Browser extensions & dev tools:**
- [`petergyang/no-ai-slop`](https://github.com/petergyang/no-ai-slop) — browser extension that flags and filters AI-generated ("slop") content on the web
- [`Comfy-Org/ComfyUI`](https://github.com/Comfy-Org/ComfyUI) — node-based GPU interface for Stable Diffusion and other image/video generation models; highly extensible workflow builder

**Analytics & monitoring:**
- [`OpenLabs-so/openanalytics`](https://github.com/OpenLabs-so/openanalytics) — privacy-first, open-source web analytics platform with built-in MCP support for querying your own traffic data in Claude

**Productivity & workflow:**
- [`usestrix/strix`](https://github.com/usestrix/strix) — AI-powered browser extension for reading, summarising, and acting on web content without leaving the page
- [`superplanehq/superplane`](https://github.com/superplanehq/superplane) — open-source release pipeline and feature-flag orchestration tool for coordinating complex deployments
- [`diwenne/openreply`](https://github.com/diwenne/openreply) — open-source AI reply tool for generating contextual responses across social platforms and email

### Command Installed

- **`/claude-code-commands-reference`** — full reference card for all 15 Claude Code slash commands (12 core + 3 bonus)

  **12 core:** `/init` `/compact` `/clear` `/rewind` `/plan` `/model` `/context` `/mcp` `/agents` `/doctor` `/review` `/batch`
  **Bonus:** `/btw` `/usage` `/loop`

### Plain-Text Prompts

**Look up a Claude Code slash command:**
> What does the /[COMMAND] slash command do in Claude Code? Give me a detailed explanation with usage examples and when to use it versus alternatives.

**Discover open-source alternatives to a paid tool:**
> I currently pay for [TOOL NAME]. What is the best open-source, self-hostable alternative? Give me: (1) the top repo with stars and a one-line description, (2) how close the feature parity is, (3) the main trade-off vs the paid version, (4) the docker-compose or quickstart command to run it locally.

**Evaluate a repo before cloning:**
> I'm considering self-hosting [REPO NAME / URL]. Analyse it for: (1) activity — last commit, open issues, PR merge rate; (2) deployment complexity — Docker support, required env vars, infra needs; (3) community — Discord, docs quality, contributor count; (4) security posture — known CVEs, secret scanning, dependency freshness. Give me a go / no-go recommendation.

---

## 75. Second Brain Weekly Review & Idea Connection Commands (Batch 75)

**Batch:** 77 iCloud Photos (`d3e471d9-iCloud_Photos_2.zip`). Sources include @earchoe (second brain system + weekly review prompt + idea connection prompt), @ty.prompts.ai (NOMAD local AI tool carousel), SkillDrop AI (browser use cases), @aicareersuite (NotebookLM+Claude workflow), @emmadroid (full stack project ideas), @clicksandrank (business platforms), @byblotech (AI email tips), AI Unlocked (GitLab v2.1.232-234 changelog), and @AIEMERGENCE (AI app alternatives). All repos confirmed already in README; two new commands created from @earchoe prompts.

**New Commands:**

- **`/idea-connection`** (`.claude/commands/idea-connection.md`) — Monthly idea connection prompt from @earchoe: paste a selection of notes from the last month; Claude finds recurring themes, cross-domain applications, collective questions, contradictions, and the one big idea tying 3+ notes together. Usage: `/idea-connection [paste your monthly notes]`

- **`/second-brain-weekly`** (`.claude/commands/second-brain-weekly.md`) — Weekly Second Brain Review from @earchoe: paste your Notion inbox every Friday; Claude returns the 3 most important ideas, missed connections between notes, which notes should become content (carousel/video/newsletter), which become actions, what to archive, and one insight to apply immediately — formatted as a clean list to paste back into Notion. Usage: `/second-brain-weekly [paste your Notion inbox / this week's notes]`

**Prompts (plain text to copy):**

**Monthly Idea Connection (@earchoe):**
```
Here are notes I have collected over the last month on various topics:

[paste a selection of your notes]

Find connections I might have missed:
1. What themes keep appearing across different notes?
2. What idea from one area could apply to a completely different area?
3. What question do these notes collectively seem to be asking?
4. What have I learned this month that contradicts something I believed before?
5. What is the one big idea that ties 3+ of these notes together?

This will help me generate original content and make better decisions.
```

**Weekly Second Brain Review (@earchoe):**
```
// WEEKLY SECOND BRAIN REVIEW – PASTE EVERY FRIDAY

Here are my raw notes and ideas from this week: [paste your Notion inbox]

Process them and give me:
1. A summary of the 3 most important ideas I captured
2. Any connections between different notes I might have missed
3. Which notes should become content (carousel / video / newsletter)
4. Which notes should become actions (add to my project tracker)
5. Which notes can be archived or deleted – they are not useful
6. One insight from this week's reading that I should apply immediately

Format as a clean organised list I can paste back into Notion.

---

## 76. Storytelling Frameworks Reference

**Source:** Will McTighe infographic — "6 Storytelling Frameworks Everybody Must Know"
**Type:** Claude Code command (`/storytelling-frameworks`)
**File:** `.claude/commands/storytelling-frameworks.md`

Six structured storytelling frameworks, each with a step-by-step structure and a specific "use when" scenario. Use `/storytelling-frameworks [your topic]` to get a framework applied to your situation, or run with no args to see the full reference.

### Frameworks included

| # | Framework | Use when |
|---|-----------|---------|
| 1 | **Hero's Journey** (12 steps) | Interview pitches, founder stories |
| 2 | **The Golden Circle** (Why → How → What) | Explaining your company's purpose |
| 3 | **The Mountain Structure** | Talks and dinner stories with a big payoff |
| 4 | **Pixar's Story Framework** | Making someone care before you ask for something |
| 5 | **The 3-Act Play** | Case studies, client problem walkthroughs |
| 6 | **What, So What, Now What** | Exec presentations, budget requests |

### Plain-text prompts

**Hero's Journey prompt:**
```
Tell my story using the Hero's Journey framework:
1. Ordinary World — [your life before]
2. Call to Adventure — [the opportunity]
3. Refuse the Call — [initial hesitation]
4. Meet the Mentor — [who/what helped]
5. Cross the First Threshold — [first step]
6. Tests, Allies, Enemies — [obstacles]
7. Innermost Cave — [hardest moment]
8. Ordeal — [crisis point]
9. Reward — [what you gained]
10. The Road Back — [applying the lesson]
11. Resurrection — [final challenge]
12. Return with the Elixir — [what you offer now]
```

**Pixar's Story Framework prompt:**
```
Tell my story using Pixar's framework:
Once upon a time… [who you are]
And every day… [familiar situation before the problem]
Until one day… [the disruption / problem]
And because of this… [solutions you tried]
And because of this… [consequences / stakes]
Until finally… [your solution / offer]
And ever since that day… [results / success story]
```

**What, So What, Now What prompt:**
```
Structure my presentation using What / So What / Now What:
WHAT: [the background — what happened, what the data shows]
SO WHAT: [the consequences — why it matters, what's at risk]
NOW WHAT: [the recommendation — what to do next]
```

> **Note:** Four MP4 video files were uploaded alongside this image. Video content cannot be read or analyzed with currently available tools — no command was created from them.
```

---

## 77. AI Tool Finder — 250+ Curated Tools by Category

**Source:** User-curated link collection (dmavridi@gmail.com)
**Type:** Claude Code command (`/ai-tool-finder`)
**File:** `.claude/commands/ai-tool-finder.md`

Comprehensive, categorized reference of 250+ AI and productivity tools saved over time. Use `/ai-tool-finder [use case]` to get the best tools for a specific task, or run with no args for the full directory.

### Categories covered

| Category | Example tools |
|----------|--------------|
| AI Video Creation | invideo, zebracat, klingai, lumalabs, runwayml, pika, heygen |
| AI Image Generation | midjourney, leonardo, krea, ideogram, openart, flux1 |
| Website/App Builders | bolt.new, lovable.dev, dora.run, wegic, relume, emergent.sh |
| PDF & Document Tools | simplepdf, lightpdf, hipdf, stirlingpdf, cloudconvert |
| Infographics & Data Viz | napkin.ai, flourish.studio, julius, venngage, text2infographic |
| AI Writing & Content | writesonic, hix.ai, simplified, undetectable, type.ai |
| Learning Platforms | learnanything.xyz, roadmap.sh, shepherd.study, mindgraspai |
| Automation & Workflow | n8n.io, zapier, lindy.ai, reply.io, string.com |
| Voice & Audio AI | elevenlabs, podcastle, notta, musicgpt, freetts |
| Presentation Tools | gamma, magicslides, slideteam, beautiful.ai |
| Mind Mapping & Notes | mymind, xtiles, notebooklm, map-this |
| Free AI Multi-Tool Hubs | tinywow, 10015.io, bestofai, futurepedia |
| SEO & Marketing | similarweb, semrush, seostudio, validea, particl |
| Avatar & Training Video | humva, heygen, akool, thetwinai, apob.ai |
| 3D, Maps & Specialty | Google Earth Studio, backflip.ai, spline, zoo.dev |

### Solo entrepreneur app ideas from this tool landscape

Patterns in these tools reveal clear gaps and opportunities for a solo builder:

1. **Niche AI tool directory** — bestfreeaiwebsites.com and futurepedia are generic; a vertical-specific directory (e.g. "AI tools for real estate agents" or "AI tools for course creators") built on an Airtable/Notion CMS + bolt.new frontend is fast to ship and monetizable via affiliate or a $9/mo membership.

2. **AI infographic-as-a-service** — text2infographic.com exists but is generic. A niche service (financial summaries → infographics, research papers → one-pagers) using napkin.ai + Claude + Canva API as the backend, sold on Gumroad or as a subscription.

3. **Automation workflow templates shop** — n8n.io and Zapier templates for specific industries. Sell pre-built automation bundles on Gumroad or a Notion storefront: "$29 — 10 n8n workflows for content creators." Low build cost, recurring revenue from updates.

4. **AI-generated training video service** — use humva + heygen + elevenlabs to produce corporate training/onboarding videos on demand. Solo service: client provides script + brand → you deliver avatar video in 48h. $300–$800/video with nearly $0 marginal cost.

5. **Competitor intelligence report service** — combine similarweb + semrush + Claude to produce weekly competitor analysis reports for small brands. $99–$299/mo subscription. Build the pipeline once in n8n, sell to 20 clients.

6. **AI-powered PDF/document service** — niche document transformation: "upload your research, get an executive brief + infographic." Use stirlingpdf + Claude + napkin.ai. Sell to consultants, analysts.

7. **Learning curriculum builder** — learnanything.xyz-style tool but for custom company onboarding. Client provides their product docs → Claude generates a structured learning path. SaaS on top of Supabase + lovable.dev frontend.

> **Note:** 30 TikTok short-form video links were included in this batch. TikTok video content cannot be fetched or analyzed with available tools — no commands were created from those links.
