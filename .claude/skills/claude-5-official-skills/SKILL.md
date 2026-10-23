---
name: claude-5-official-skills
description: The five Claude skills from the @ai.easily carousel mapped to what is installed here - ELI5 picture explainer, Frontend Design, Document skills (Word, PowerPoint, Excel, PDF), Skill Creator and Doc Co-authoring - with one trigger prompt each. Use when the user asks which skills to install first, how to make Claude produce real files, avoid generic-looking pages, build their own skill, or plan a document before writing it. Source @ai.easily "5 Claude skills" (Batch 100); the official ones come from github.com/anthropics/skills.
---

# 5 Claude skills to install first

Slide 7 of the carousel: "Pick one. Install it today." All five are already installed in this repo, so nothing needs adding.

| # | Skill | What the slide says | Here | Trigger prompt |
|---|---|---|---|---|
| 1 | ELI5 | Turns any topic into a picture explainer with very few words; built by the Claude Code team; from the community plugins | `/eli5` command (text version) | `/eli5 how a vector database works` |
| 2 | Frontend Design | Stops Claude making generic-looking pages; avoids overused fonts like Inter; picks one bold look and commits | `frontend-design` | "Build a landing page for [X] with the frontend-design skill; pick one bold direction and commit." |
| 3 | Document skills | Real Word, PowerPoint, Excel and PDF files; create and edit, not just read | `docx`, `pptx`, `xlsx`, `pdf` | "Make a 6-slide deck from this outline as a .pptx." |
| 4 | Skill Creator | Describe a task you repeat and it writes the skill file | `skill-creator` | "Use skill-creator to turn my weekly client report process into a skill." |
| 5 | Doc Co-authoring | Gathers your context, agrees an outline, then drafts section by section | `doc-coauthoring` | "Use doc-coauthoring to write [document]. Start by asking what you need." |

Notes: the picture-explainer ELI5 in the carousel is a community plugin and produces images; the local `/eli5` command only explains in plain words. The carousel's own dates ("checked 2026-10-01") are the creator's, not verified here.


## Batch 114: install cards (@atlasgrowth.co "Lvl", "7 top Claude skills to install today")

The seven named skills are `frontend-design`, `skill-creator`, `pptx`, `pdf`, `webapp-testing`, `theme-factory`, `mcp-builder`. All seven are installed in this repo already. The install route on the cards matches the `anthropics/skills` README (182,875 stars, checked 22 October 2026):

```
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
/plugin install document-skills@anthropic-agent-skills
```

`example-skills` carries the creative and development skills; `document-skills` carries `docx`, `pdf`, `pptx`, `xlsx`. The README states that the document skills are source-available, not open source, and that the skills are demonstrations: test them before relying on them.

Slide 9 prompt, usable as is: "What task do you repeat every week? Turn the best one into a skill." Run it with `/task-to-reusable-skill <the task>`; it should list candidates, pick one, and build the skill with `skill-creator`.
