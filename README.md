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
