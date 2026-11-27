---
name: claude-automation-skills-8
description: Eight automation skills from a carousel (file automation, design automation, research agent, data analysis, automation master, browser automation, content writer, social media), each described as a three-step flow and saved as .claude/skills/<name>/SKILL.md, mapped to what already exists in this repo and to the risks of skills that run automatically. Use when someone asks which skills to build first, how to install a skill by saving a SKILL.md, or what "Claude runs it automatically, no commands required" means. Source @theromanknox "8 Claude Automations Skills" (Batch 116). The carousel shows no SKILL.md contents.
---

# 8 Claude automation skills

Source: @theromanknox carousel. Each slide gives a one-paragraph description, a three-step "how it flows", and one setup line: save as `.claude/skills/<name>/SKILL.md`, "Claude runs it automatically, no commands required." **The slides do not show any skill file contents**, so nothing here was copied; the table maps each idea to what this repo already has. The author's pitch points to a paid community.

| # | Skill on the card | Flow on the card | Already here |
|---|---|---|---|
| 1 | File Automation | Files, Process, Organised (bulk rename, sort, convert) | `file-conversion`, `pdf`, `docx`; plugin `playbook:organize-assets` |
| 2 | Design Automation | Idea, Spec out, Design brief | `design-templates`, `design-token-extractor`, `the-design-system-prompt` |
| 3 | Research Agent | Topic, Gather sources, Summary | `deep-research`, `claude-research-employee`, `verified-research` |
| 4 | Data Analysis | Raw data, Clean and analyse, Report | `data:analyze`, `xlsx`, `data-storytelling` |
| 5 | Automation Master | Task, Automate, Done | `workflow-orchestration-patterns`, `/workflow-automate`, `n8n-workflow-patterns` |
| 6 | Browser Automation | URL, Click and fill, Data | `browser`, `playwright-skill`, `safe-browser` |
| 7 | Content Writer | Research, Draft, Published | `content-engine`, `article-writing` |
| 8 | Social Media | One idea, Adapt, All platforms | `social-publisher`, `/content-repurpose` |

## What "runs automatically" really means
A skill loads when its **description** matches your request, not by magic. A broad description ("automates anything") fires on the wrong tasks and burns context; a narrow one never fires. Write the description as "use when ..." with concrete triggers, and test it with three real prompts that should trigger it and three that should not.

## Risks
- **Browser automation** acts as you on real sites: keep it read-only first, off logged-in banking and admin pages, and inside the site's terms.
- **File automation** that renames or deletes at scale is irreversible without a backup: run it on a copy and show the plan before it executes.
- **Social media** automation posts in your name: drafts only until you approve.

Build your own with `skill-creator` (see `claude-5-official-skills`).
