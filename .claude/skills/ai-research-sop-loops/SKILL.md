---
name: ai-research-sop-loops
description: Two 9-slide @earchoe prompt series - "AI research that turns sources into a brief" (source pack -> brief -> decision memo) and "AI SOP builder for any repeatable task" (process -> SOP -> test -> improve), with the exact two-pass prompts, the human-check rules and the "save the recipe" method. Use when asked to turn 3-10 sources into a cited research brief or decision memo, or to write an SOP from how someone already does a task.
---

# Research loop and SOP builder (@earchoe, AI Playbook 08/21)

Shared method: Context (give AI the real material) -> Structure (define the job) -> Check (review before action). "Do not start with a clever prompt. Start with the outcome, the inputs and the quality check." Workflow: open ChatGPT / Claude / Gemini -> copy -> replace [BRACKETS] -> attach the source -> send -> read the output before using it.

## A. Research loop (inputs: a question, 3-10 trustworthy sources, the decision the research supports)
Prompt 01: Turn these sources into a structured research brief on [TOPIC]. Separate established facts, source claims, disagreements and unanswered questions. Cite each important claim to its source.
Prompt 02: Now convert the brief into a one-page decision memo for [AUDIENCE]. Include: what we know, what we do not know, implications, options and the next 3 questions worth researching.
Quality loop: two-pass (extract first, interpret second). If sources disagree, keep the disagreement visible instead of forcing one answer. AI accelerates; you own the decision, the facts and the final output.
Value: source -> extract -> compare -> decide; a sellable "research service" (source pack -> brief -> decision memo) for founders, students, analysts, content teams.

## B. SOP builder (inputs: one task you repeat; your current steps, tools, decisions, exceptions, final output)
Prompt 01: Turn this process description [PROCESS] into an SOP. Include purpose, trigger, prerequisites, numbered steps, decision points, quality checks and completion criteria. Do not invent steps.
Prompt 02: Now identify where a new person is most likely to make a mistake. Add short warnings and examples without changing the underlying process.
Quality loop: run the SOP yourself once using only the document; every point where you still need to ask a question is a documentation gap.
Value: SOP creation can be sold to small businesses whose processes live in people's heads. Process -> SOP -> test -> improve.

## C. Save the recipe (both series)
Keep the original input/source; keep the prompt that produced the useful result; add your own quality check before publishing or acting; turn the finished workflow into a reusable template.

Use `/research-brief` and `/sop-from-process`. Related: `sop-builder`, `research-synthesis`, `verified-research`, `source-verification`.
