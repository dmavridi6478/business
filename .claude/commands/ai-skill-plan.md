# /ai-skill-plan

Build a detailed, week-by-week learning plan for one of the 12 AI Skills for 2026, tailored to your role and current level.

## Usage
```
/ai-skill-plan [skill name] [optional: role and current level]
```

## Examples
```
/ai-skill-plan Prompt Engineering, marketing manager, beginner
/ai-skill-plan AI Agents, software developer, intermediate
/ai-skill-plan RAG, startup CTO, know Python but no ML background
/ai-skill-plan AI Workflow Automation, operations lead, using Zapier already
```

## What You Get
- Skill level assessment (current → target)
- 4-week structured learning plan with daily/weekly actions
- Curated resources: one free + one paid per week
- Practical exercises you can do today
- Milestone checkpoints to measure progress
- "First win" project to prove the skill in 48 hours

$ARGUMENTS

---

## Prompt (executed internally)

Act as an expert AI skills coach. The user wants to master this skill: **$ARGUMENTS**

Design a rigorous, practical 4-week learning plan. Use the 12 AI Skills for 2026 framework.

**SKILL CONTEXT** (reference only — apply to the user's stated skill):
1. Prompt Engineering — Goal → Context → Format → Precise AI Output
2. AI Workflow Automation — Trigger → Action → Process → Result (no-code)
3. AI Agents — Plan → Reason → Execute → Better Results
4. RAG — Knowledge Sources → Retrieve → Augment → Grounded Answer
5. Staying Updated — Curate → Synthesize → Apply → Share
6. Multimodal AI — Text + Image + Audio + Code → ONE MODEL
7. Fine-Tuning & AI Assistants — General → Fine-Tuned → Domain Expert
8. Voice AI & Avatars — Voice Input → AI Processing → Talking Avatar
9. AI Tool Stacking — Plan → Build → Execute → Scale
10. AI Video Content — Script → Scenes → Voiceover → Publish
11. AI-Powered SaaS Dev — Idea → Build → Iterate → Launch
12. LLM Management — Accuracy ↑ · Latency ↓ · Cost ↓

**DELIVER:**

### Current Level Assessment
- Infer current proficiency (0–4) from context provided
- State what they already know vs. what they are missing
- Define the target state at plan completion

### 48-Hour First Win
- One specific project they can complete in 2 days
- Exact steps (not vague instructions)
- Expected output they can show someone

### 4-Week Learning Plan

**Week 1 — Foundation**
- Goal for the week
- 3 daily actions (15–30 min each)
- One free resource (name + URL if known)
- One paid resource or course (name + estimated cost)
- End-of-week checkpoint: what can you do that you couldn't before?

**Week 2 — Core Skills**
- Same structure as Week 1
- First hands-on build exercise

**Week 3 — Applied Practice**
- Same structure
- Real-world project tied to their role

**Week 4 — Ship & Share**
- Same structure
- A deliverable they can publish or demonstrate

### Tool Ladder
List the 3–5 tools to learn in sequence: start simple → go deeper

### Common Mistakes
Top 3 mistakes beginners make with this skill and how to avoid them

Format as a clean, scannable plan. Be specific — name actual tools, name actual resources. No generic advice.
