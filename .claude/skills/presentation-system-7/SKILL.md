---
name: presentation-system-7
description: The Wealth Lab "7 ChatGPT prompts to build a complete presentation" workflow - Blueprint, Storytelling and slide flow, Complete slide content generator, Slide clarity editor, Visual direction and design, Speaker notes, Final quality check - with the Plan-Structure-Write-Simplify-Design-Prepare-Polish order. Use when building any slide deck from a topic with ChatGPT or Claude. Complements claude-presentation-prompts (a different six-prompt set).
---

# 7 Prompts, One Presentation Workflow

Source: @the.wealth.lab carousel. Order: Plan, Structure, Write, Simplify, Design, Prepare, Polish. Replace every [BRACKET]. Prompts are reproduced from the slides; the "why it works" lines are paraphrased.

## 1 Presentation Blueprint
"Act as a professional presentation consultant. Create a complete blueprint for a presentation about [TOPIC]. Define the main goal, target audience, core message, ideal number of slides, and overall narrative. Make sure the structure is logical, engaging, and designed to achieve the presentation's objective."
Why: gives the model the big picture before any slide is written.

## 2 Storytelling and Slide Flow Architect
"Turn [TOPIC] into a compelling slide-by-slide presentation using a strong storytelling structure: Hook -> Problem -> Insight -> Solution -> Conclusion. For each slide, provide a clear title, its purpose, and the key message it should communicate. Ensure the presentation flows naturally from beginning to end."

## 3 Complete Slide Content Generator
"Create presentation-ready content for every slide based on the structure above. Keep each slide concise and focused on one clear idea. Use strong headlines, short bullet points, relevant examples, statistics, or key takeaways where appropriate. Audience: [DESCRIBE AUDIENCE]."
Rule: do not invent statistics. Mark any figure you cannot source as [VERIFY].

## 4 Slide Clarity and Simplification Editor
"Review the following presentation content as an expert presentation editor. Remove unnecessary text, simplify complex ideas, strengthen weak points, and rewrite each slide for maximum clarity and impact. Make sure every slide communicates one clear idea without becoming overcrowded. Content: [PASTE CONTENT]."

## 5 Visual Direction and Design
"Act as a professional presentation designer. Create a visual direction guide for every slide in a presentation about [TOPIC]. For each slide, recommend the ideal layout, visual hierarchy, charts, diagrams, icons, images, and other visuals. Keep the design clean, modern, professional, and visually engaging while ensuring every visual supports the message."
Output feeds PowerPoint, Canva, Google Slides or `premium-html-presentation`.

## 6 Speaker Notes and Presentation Delivery
"Create concise speaker notes for every slide. Make them conversational, informative, and engaging without simply repeating the slide text. Add useful explanations, examples, transitions, and emphasis points that help the presenter deliver the presentation confidently."

## 7 Final Presentation Quality Check
"Act as a senior presentation editor and quality reviewer. Review the complete presentation for logical flow, clarity, storytelling, repetition, unsupported claims, slide overcrowding, visual consistency, and audience engagement. Identify anything that weakens the presentation and provide specific improvements. Then present the final recommended slide order and key revisions."

## Usage

Run in one chat so each step sees the previous output. Slash command: `/presentation-system <topic and audience>`. Agent: `presentation-director`.
