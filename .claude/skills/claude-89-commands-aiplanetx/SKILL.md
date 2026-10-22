---
name: claude-89-commands-aiplanetx
description: The AIPlanetX "89 Claude commands" graphic, a list of 89 short slash-style prompts in 11 groups (start, focus, think, write, organize, code, data, automate, personalize, learn, collaborate) with a warning that most are not built-in Claude commands. Use as a prompt-shortcut checklist, and see claude-code-commands-reference for the real Claude Code commands.
---

# 89 "Claude commands" (AIPlanetX graphic)

Source: one infographic. **[Certain] Most of these are not built-in Claude or Claude Code commands.** In the claude.ai chat you cannot type `/workflow` or `/forecast` and get a feature; they work only as a convention (you type the word and Claude interprets it) or if you save each as your own command or skill. Real Claude Code commands are in `claude-code-commands-reference`. The graphic ends with a comment-for-database sales funnel ("38,000+ AI tools"); nothing was commented.

| Group | Commands as printed |
|---|---|
| 1 Start and create (1-8) | /new /project /upload /paste /template /import /scan /voice |
| 2 Focus and context (9-17) | /focus /context /details /examples /clarify /define /assumptions /priorities /constraints |
| 3 Think and solve (18-25) | /analyze /compare /pros-cons /evaluate /recommend /brainstorm /solve /challenge |
| 4 Write and edit (26-34) | /write /edit /rewrite /shorten /expand /improve /summarize /paraphrase /proofread |
| 5 Organize and structure (35-43) | /outline /structure /bullet /numbered /table /summary /key-points /mindmap /flowchart |
| 6 Code and tech (44-52) | /code /debug /explain /optimize /refactor /test /convert /documentation /review |
| 7 Data and analysis (53-59) | /analyze-data /visualize /insights /forecast /report /stats /clean |
| 8 Automate and integrate (60-67) | /workflow /automate /api /integrate /schedule /trigger /tasklist /checklist |
| 9 Personalize and control (68-75) | /preferences /memory /tone /style /length /format /reset /clear |
| 10 Learn and research (76-82) | /search /research /learn /tl;dr /sources /fact-check /explore |
| 11 Collaborate and share (83-89) | /share /export /download /copy /email /publish /feedback |

Bonus tips on the graphic: use "/" for quick access, combine commands, add context early, be specific, iterate, save what works.

## How to make them real
- Save the ones you use as commands or skills in `.claude/commands` (see `task-to-reusable-skill`, `write-a-skill`). This repo already ships working equivalents such as `/brainstorm`, `/compare`, `/proscons`, `/summary`, `/checklist`, `/sourcecheck`, `/teachback` and `/decision-matrix`.
- **[Likely]** Commands that imply actions on your accounts (/email, /publish, /schedule, /api, /trigger) only work if a connector or tool is connected; without it Claude just writes text.
- Several verbs overlap (/summary, /summarize, /tl;dr, /key-points); keep one per job.
