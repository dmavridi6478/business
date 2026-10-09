---
description: 10-component Claude prompt formula (Role → Objective → Context → Task → Constraints → Workflow → Validation → Stop Conditions → Output Format → Quality Control) with a worked SaaS-launch example
argument-hint: [what you're trying to get Claude to do — "simple" or "complex"]
---

# The Perfect Claude Prompt Structure

Source: @the.wealth.lab, "The Perfect Claude Prompt Structure." A 10-component formula for structuring prompts, distinct from this repo's other prompt-technique skills (`claude-founder-prompts` is 11 one-line meta-techniques like "argue the other side"; `prompt-engineering-patterns` covers chain-of-thought/few-shot/production patterns) — this one is a **prompt-assembly checklist**, the order to write the components in.

## The simple formula

```
ROLE → OBJECTIVE → CONTEXT → TASK → CONSTRAINTS → WORKFLOW →
VALIDATION → STOP CONDITIONS → OUTPUT FORMAT → QUALITY CONTROL
```

- **For simple prompts:** ROLE + CONTEXT + TASK + OUTPUT (4 components)
- **For complex prompts:** use all 10

## The 10 components, each with its purpose

1. **ROLE** — define who Claude should act as. *Purpose: sets the expertise and perspective.*
2. **OBJECTIVE** — define the desired outcome. *Purpose: gives Claude a clear destination.*
3. **CONTEXT** — provide the information Claude needs. *Purpose: prevents generic answers.*
4. **TASK** — state exactly what Claude needs to do. *Purpose: converts the objective into specific work.*
5. **CONSTRAINTS** — set the boundaries. *Purpose: prevents impractical solutions.*
6. **WORKFLOW** — tell Claude how to approach the problem. *Purpose: creates a structured problem-solving process.*
7. **VALIDATION** — tell Claude how ideas should be tested. *Purpose: turns opinions into measurable experiments.*
8. **STOP CONDITIONS** — define when the task is complete. *Purpose: prevents incomplete outputs.*
9. **OUTPUT FORMAT** — tell Claude exactly how to present the answer. *Purpose: produces consistent, usable results.*
10. **QUALITY CONTROL** — make Claude check the work before delivering it. *Purpose: catches omissions and weak spots.*

## Worked example (all 10 components, a SaaS launch plan)

```
<role>Act as a senior go-to-market strategist specializing in early-stage SaaS.</role>

<objective>Create a launch strategy that validates positioning and drives traction.</objective>

<context>
Product: AI task manager.
Audience: Founders aged 25-40.
Team: Founder + Growth Marketer.
Resources: Lean budget, 15-20 beta users.
</context>

<task>Build a 12-week launch plan with weekly experiments and measurable outcomes.</task>

<constraints>Keep recommendations realistic for a two-person team and lean budget.</constraints>

<workflow>Diagnose → Prioritize → Build → Test → Measure → Decide.</workflow>

<validation>For each major assumption, define the test, success signal, failure signal, and next action.</validation>

<stop_conditions>Do not stop until all 12 weeks are covered, every action has an owner and risk, and a final decision gate is included.</stop_conditions>

<output_format>For each action include: Action, Owner, Risk, Rationale, Deliverable, and Success Metric.</output_format>

<quality_control>Before finalizing, verify that every requirement is satisfied, assumptions are identified, metrics are measurable, and no major constraint was ignored.</quality_control>
```

## Pro tip — XML tags for complex prompts

For complex Claude prompts, XML tags make instructions easier to separate:

```
<role>...</role>
<context>...</context>
<task>...</task>
<constraints>...</constraints>
```

You don't need a massive prompt. Clear instructions beat unnecessary complexity.

## Plain-text prompt to build your own 10-part prompt

```
Help me write a complete 10-component prompt for this task: [DESCRIBE YOUR TASK].
Walk through each component with me — Role, Objective, Context, Task,
Constraints, Workflow, Validation, Stop Conditions, Output Format, Quality
Control — asking me one question at a time for whatever you don't already
know, then assemble the final prompt in XML tags.
```
