# iCloud Photos — Full Action Plan & Reference

Extracted from 37 TikTok content cards (Sep 2026).
Sources: @replace.so, @unifybrowse, @aigenesis.official, @woodwchbp5j (Tech With Zia), @your.aimentor

---

## 1. GitHub Repositories to Explore / Clone

| Repo | Stars | What It Does | Get It |
|------|-------|-------------|--------|
| `LingyiChen-AI/DeepDiagram` | 930 | AI-powered interactive architecture diagrams from codebases | `git clone github.com/LingyiChen-AI/DeepDiagram` |
| `syi0808/screenize` | 605 | Screen recording → polished shareable format | `git clone github.com/syi0808/screenize` |
| `appwrite/appwrite` | 57,424 | Open-source Firebase alternative (backend-as-a-service) | `git clone github.com/appwrite/appwrite` |
| `pocketbase/pocketbase` | 61,119 | Single-file self-hosted backend + realtime DB | `git clone github.com/pocketbase/pocketbase` |
| `polarsource/polar` | 10,273 | Open-source billing & subscription platform for developers | `git clone github.com/polarsource/polar` |
| `oblien/openship` | 12,389 | Open-source multi-vendor order management & fulfillment | `git clone github.com/oblien/openship` |
| `salarzeidanlou/todofy` | — | Beautiful minimal todo app (Todofy) | `git clone github.com/salarzeidanlou/todofy` |
| `tt-a1i/archify` | 26,400 | Plain English → self-validating architecture diagrams | `npx skills add tt-a1i/archify -g` |
| `freestylefly/awesome-gpt-image-2` | 24,104 | 544 reverse-engineered GPT-Image-2 prompts in 13 categories | `npx skills add freestylefly/awesome-gpt-image-2` |
| `anthropics/claude-plugins-community` | 2,514 | 2,282 community plugins for Claude Code | `claude plugin marketplace add anthropics/claude-plugins-community` |
| `bilawalsidhu/gods-eye-view` | 10,475 | 3D globe with live aircraft, ships, satellites, 800 public cameras | `git clone bilawalsidhu/gods-eye-view && npm install && npm run dev` |
| `MadsLorentzen/ai-job-search` | 37,529 | AI job application framework on Claude Code (/scrape /rank /apply) | `gh repo fork MadsLorentzen/ai-job-search` |

---

## 2. Commands / Skills to Install

### Claude Plugins Marketplace
```bash
claude plugin marketplace add anthropics/claude-plugins-community
```
Then install specific plugins, e.g.:
```bash
claude plugin install eli5@claude-community
```

### NPX Skills
```bash
# GPT-Image-2 style library (544 reverse-engineered prompts)
npx skills add freestylefly/awesome-gpt-image-2

# Archify — plain English → architecture diagrams (global install)
npx skills add tt-a1i/archify -g
```

---

## 3. Claude Skills Created (from Tech With Zia Prompts)

All 4 skills are installed under `.claude/skills/`:

| Skill | Invoke With | File |
|-------|------------|------|
| AI Content Workflow Designer | `/ai-workflow-designer` | `.claude/skills/ai-workflow-designer/SKILL.md` |
| AI Content Production Engine | `/ai-content-production-engine` | `.claude/skills/ai-content-production-engine/SKILL.md` |
| AI Smart Publishing Planner | `/ai-smart-publishing-planner` | `.claude/skills/ai-smart-publishing-planner/SKILL.md` |
| AI Content Improvement Loop | `/ai-content-improvement-loop` | `.claude/skills/ai-content-improvement-loop/SKILL.md` |

---

## 4. The 4 Prompts — Plain Text (Copy-Paste Ready)

### PROMPT 01 — WORKFLOW DESIGNER

```
You are an AI workflow architect specializing in content systems for creators and businesses. Help me design a complete content creation workflow by first asking me these questions: 1) What type of content do I create? (video, blog, social posts, newsletters, podcasts, etc.) 2) Who is my target audience and what platforms do they use? 3) How many pieces of content do I need to produce per week? 4) What AI tools do I currently use or have access to? 5) What is my biggest bottleneck right now? (ideas, production, consistency, distribution). After gathering my answers, design a custom workflow with these phases: IDEA → RESEARCH → CREATE → REVIEW → PUBLISH → ANALYZE. For each phase provide: specific actions to take, recommended AI tools and how to prompt them, time estimate, output/deliverable for that phase, and handoff notes to the next phase. Also create a visual text diagram of the full workflow, and identify the 2-3 steps where AI can save the most time. End with a Quick Start — the 3 things I should implement TODAY to see immediate results.
```

---

### PROMPT 02 — CONTENT PRODUCTION ENGINE

```
You are a content production specialist and creative director with expertise in viral social media content. I'm going to give you a single content idea. Your job is to expand it into a COMPLETE PRODUCTION BRIEF that any creator or AI tool can immediately execute without additional clarification. The brief must include: 1) HOOK (First 3-5 seconds) — primary hook option, 2 alternative hook variations, pattern interrupt technique to use; 2) NARRATIVE ARC — opening setup (problem/tension/curiosity gap), middle development (insight/proof/story), closing resolution (solution/transformation/CTA); 3) KEY TALKING POINTS — 5 core points with supporting data, examples, or stories for each; 4) VISUAL & AUDIO NOTES — b-roll suggestions/visual transitions, on-screen text overlays, music mood and energy arc, any text animations or effects; 5) CALL TO ACTION — primary CTA, secondary CTA (for engagement), where to place each CTA in the content; 6) REPURPOSING PLAN — how to adapt this for 3 other platforms (e.g., TikTok → LinkedIn → Newsletter → YouTube Short), what to cut, keep, or add for each platform. My content idea is: [INSERT YOUR IDEA HERE]
```

---

### PROMPT 03 — SMART PUBLISHING PLANNER

```
You are a social media strategist and publishing scheduler who specializes in building sustainable content calendars for solo creators and small teams. I need a 30-day publishing calendar. First, ask me: 1) Which platforms am I publishing on? 2) How many pieces of content do I have ready or in production right now? 3) What content categories do I post in? (educational, behind-the-scenes, product, entertainment, personal) 4) What is my main content goal for this month? (growth, engagement, sales, brand awareness) 5) Are there any key dates, launches, or events in the next 30 days I should plan around? Once you have my answers, create a 30-day calendar that respects these rules: no more than 2 promotional posts per week (the rest should deliver value), alternate content types to prevent audience fatigue, place educational/high-value content on high-traffic days for each platform, build in 20% buffer slots for trending/reactive content. For each week, show: day-by-day schedule (date, platform, content type, topic/title), weekly theme or arc, expected best-performing post of the week and why. End with: 3 evergreen pieces I should always have in reserve, the optimal posting time for each platform, and a checklist to prep content one week ahead.
```

---

### PROMPT 04 — AI CONTENT IMPROVEMENT LOOP

```
You are a content optimization expert and data analyst who specializes in iterative creative improvement for digital creators. I'm going to share my recent content performance data. Your job is to run a FULL IMPROVEMENT LOOP ANALYSIS and give me actionable outputs I can immediately feed back into my content workflow. Please analyze: 1) WHAT WORKED (Top Performers) — identify the top 20% of content and extract the common patterns; what hook style, content format, topic, length, or posting time drove results?; what specific words, phrases, or visuals seem to trigger engagement?; 2) WHAT UNDERPERFORMED (Bottom Performers) — identify the bottom 20% and diagnose WHY each underperformed; was it the hook, the topic, the format, the timing, or the CTA?; what ONE change would most likely fix each piece?; 3) 3 SPECIFIC IMPROVEMENTS FOR MY NEXT BATCH — based on patterns above, give me 3 concrete, implementable changes; each improvement must be specific enough to act on TODAY; rank by expected impact (highest first); 4) A/B TEST IDEAS — suggest 3 A/B tests for my next 2 weeks; each test must isolate ONE variable (hook, format, CTA, or length); define success metric for each test before running it; 5) REFINED WORKFLOW PROMPTS — based on this analysis, rewrite the 3 prompts I should use in my next content cycle: a) a better HOOK FORMULA for my audience, b) a better TOPIC SELECTION filter, c) a better CTA for my current engagement level. My performance data: [PASTE YOUR ANALYTICS DATA HERE]
```

---

## 5. AI Tool Stack (from @aigenesis.official)

### For Image Generation
- ChatGPT (GPT-Image-2) — photorealistic generation
- Ideogram — best for text-in-image accuracy
- Nano Banana — rapid product mock-up generation

### For Upscaling Images
- Krea AI
- Stable Diffusion
- Magnific AI — 4× detail enhancement

### For Text & Titles
- Jasper AI
- Copy AI
- Claude

### For Image Mockups
- Midjourney
- Smart Mockups
- Artboard Studio

### For Visuals & Depth
- Higgsfield
- Freepik
- Night Cafe AI

---

## 6. Design Templates Created

All 4 templates are in `Artifacts/templates/`:

| Template | File | Style | Based On |
|----------|------|-------|----------|
| Dark Tool Showcase Card | `social-card-dark-tool-showcase.html` | Black bg, dot-grid, 3D glossy objects, large white type | @replace.so |
| Light Editorial Slide | `social-card-light-editorial-slide.html` | Cream/white, large bold serif, device mockups, numbered | @unifybrowse |
| Dark AI Tools List | `social-card-dark-ai-tools-list.html` | Black bg, bold white header, icon + name vertical list | @aigenesis.official |
| AI Prompt Card | `social-card-prompt-card.html` | Light gradient, red/coloured badge, white prompt card | Tech With Zia |

---

## 7. Recommended Priority Order (@your.aimentor "Which Ones I Would Use")

1. **Install TODAY**: gpt-image-2 skill (`npx skills add freestylefly/awesome-gpt-image-2`)
2. **Install TODAY**: claude-plugins-community (`claude plugin marketplace add anthropics/claude-plugins-community`)
3. **If you ship diagrams**: archify (`npx skills add tt-a1i/archify -g`)
4. **Weekend project**: gods-eye-view (`git clone bilawalsidhu/gods-eye-view`)
5. **If job searching**: ai-job-search (`gh repo fork MadsLorentzen/ai-job-search`)
