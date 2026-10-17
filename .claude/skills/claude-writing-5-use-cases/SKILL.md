---
name: claude-writing-5-use-cases
description: Five Claude writing use cases beyond "write this for me" from a @your.aimentor infographic (executive compression, audience translation, argument strengthening, voice consistency, objection anticipation) and its five-step writing flow, with a ready prompt for each. Use when improving a draft you already have.
---

# 5 Claude writing use cases beyond "write this for me"

Source: one infographic (@your.aimentor): "Same ideas. Better thinking. Stronger writing." The prompts below were **written for this repo from the graphic's headings**; they are not the author's wording.

| # | Use case | The graphic says | Prompt |
|---|---|---|---|
| 01 | Executive compression | 20 pages become one decision memo | Turn the document below into a one-page decision memo for [decision maker]. State the decision needed, the recommendation, the three facts that drive it, the main risk and what happens if we do nothing. Do not add facts that are not in the document. Document: [paste] |
| 02 | Audience translation | One idea, different audiences (Executive, Technical, General) | Rewrite the idea below three times: for an executive (outcome and cost), for a technical reader (how it works and constraints) and for a general reader (plain language, no jargon). Keep the facts identical in all three. Idea: [paste] |
| 03 | Argument strengthening | Find the weakest premise | Read my argument below. List its premises, name the weakest one and explain why, say what evidence would support it, then suggest a stronger version. Do not flatter the argument. Argument: [paste] |
| 04 | Voice consistency | Compare writing against a defined voice (tone, style, vocabulary, consistency) | Here is my voice guide: [paste]. Compare the draft below against it on tone, style, vocabulary and consistency. Quote each place it drifts and give a fix. Draft: [paste] |
| 05 | Objection anticipation | Predict what skeptical readers will challenge | For the proposal below, list what a skeptical reader could doubt, what evidence they will want, what alternative they might suggest, and how to address each upfront. Proposal: [paste] |

## The flow in the footer
Draft (get ideas down) then Critique (find the gaps) then Strengthen (make it stronger) then Compress (say more with less) then Publish (create impact). The closing line is "Better writing builds better thinking."

## Use
- Run `/writing-lab <mode> <text or path>` with mode `compress`, `translate`, `strengthen`, `voice` or `objections`.
- The `writing-reviewer` agent applies checks 03, 04 and 05 to a file read-only.
- Never paste confidential documents into a tool you have not cleared for that data.
