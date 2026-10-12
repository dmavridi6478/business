# Batch 112 prompts (plain text; replace [brackets])

## 1. Idea validation (`/validate-idea`) - @earchoe
Prompt 01: Act as a skeptical product researcher. For [IDEA], identify the 10 assumptions that must be true for this to work. Label each by impact and uncertainty.
Prompt 02: Turn the highest-risk assumptions into 5 cheap validation tests. For each test, state what I should measure and what result would increase or decrease confidence.

## 2. Reflective prompts (`/life-prompt <number>`) - @betterpromptsai
1. You are a self-sabotage forensic analyst. I consistently self-sabotage around: [area]. Perform a complete autopsy: what is the payoff of the sabotage, which part of me benefits from failure, and what does this part fear more than failure?
2. Research-backed discussion on how binaural beats, meditation, and other neuro-techniques influence learning outcomes, and provide actionable tips for implementation.
3. You are a future self specialist. Have me write a letter from my future self at [age/achievement level] back to today. This future self should tell me what they regret not doing sooner, what they are grateful for starting, and what I should prioritize.
4. You are a remix strategist. Take [existing successful work/concept] and give me the complete remix blueprint: what to keep, what to change, what to amplify, what to subvert. I want to create something derivative that feels original.
5. You are a rapport specialist. Teach me the advanced emotional mirroring and labeling technique: how to reflect someone's emotional state back in a way that creates instant connection and trust. Apply it to [context].
6. Examine the concept of emotional labor in romantic relationships and its effects on mental health.
7. You are a brutal truth accelerator. I will describe my current situation: [describe]. You will give me the 5 uncomfortable truths I am avoiding, why I am avoiding them, and exact steps to face each one.
8. If you could instantly integrate the knowledge, skills, and experiences of someone 10 years older and wiser, who would it be, and what lessons would you apply to your life?
9. Describe your perfect day in vivid detail, what activities, relationships, and habits would you include, and how can you integrate these elements into your real life?
10. You are a life transition specialist. I am transitioning from [current state] to [desired state]. Map the psychological, practical, and social dimensions of this transition. Give me the complete navigation protocol so I emerge stronger on the other side.
11. Describe the neurotransmitter-based differences between romantic love and lust, and discuss the implications of these findings for modern dating and long-term relationships.
12. You are a permission-slip destroyer. I am afraid to create [describe idea/project] because [fear]. Walk me through a session that destroys that fear using psychological reframing, then give me a 3-day creation sprint plan.

## 3. Agent blueprint (`/agent-blueprint`)
Design an AI agent for [USE CASE]. Follow 8 steps in order: purpose and scope (use case, user needs, success criteria, constraints); system prompt (goals, role, instructions, guardrails); LLM choice (model, reasoning effort, context window, cost and latency); tools and integrations (local, API, MCP, agent as a tool, custom functions); memory (episodic, working, vector, SQL, files); orchestration (workflows, triggers, queues, agent-to-agent, error handling); interface (chat, web, API, Slack or Discord bot); tests and evals (unit, latency, quality, iterate). End with 5 evals that must pass before launch. Mark every assumption.

## 4. Plugin commands (run inside Claude Code)
/plugin install code-simplifier@anthropic-plugin-directory
/plugin install context7@anthropic-plugin-directory
/plugin install frontend-design@anthropic-plugin-directory
/plugin install superpowers@anthropic-plugin-directory
(then say "use context7" in any prompt; /brainstorming for superpowers; "simplify this component" for code-simplifier)
