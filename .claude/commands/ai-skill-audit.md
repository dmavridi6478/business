# /ai-skill-audit

Audit your current AI capability level against the 12 AI Skills for 2026 framework and produce a prioritised gap analysis with a 90-day action plan.

## Usage
```
/ai-skill-audit [role] [optional: context about current stack or constraints]
```

## Examples
```
/ai-skill-audit Marketing Director, currently using ChatGPT for copywriting only
/ai-skill-audit Freelance consultant, comfortable with Zapier and Notion
/ai-skill-audit Startup founder, building B2B SaaS, team of 3
```

## What You Get
- Self-assessment scorecard across all 12 skills (0–4 scale)
- Top 3 skills with the highest leverage for your role
- 90-day learning roadmap with weekly milestones
- One starter resource per priority skill
- Recommended first tool to try for each gap

$ARGUMENTS

---

## Prompt (executed internally)

Act as an AI skills coach and career strategist. The user's role and context: **$ARGUMENTS**

Run a structured audit against the 12 AI Skills for 2026:

1. Prompt Engineering
2. AI Workflow Automation
3. AI Agents
4. Retrieval-Augmented Generation (RAG)
5. Staying Updated
6. Multimodal AI
7. Fine-Tuning & AI Assistants
8. Voice AI & Avatars
9. AI Tool Stacking
10. AI Video Content Generation
11. AI-Powered SaaS Development
12. LLM Management

For each skill, infer a likely proficiency level (0 = unaware, 1 = aware, 2 = experimenting, 3 = applying, 4 = building) based on the user's stated role and context. Flag assumptions clearly.

Then:
- Rank the top 3 skills by leverage for this specific role
- Write a 90-day action plan with Month 1 / Month 2 / Month 3 milestones
- Suggest the single best starter tool and one starter prompt for each priority skill

Format as a clean, scannable report.
