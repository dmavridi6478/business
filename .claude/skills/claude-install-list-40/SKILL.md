---
name: claude-install-list-40
description: Charlie Hills' "40 Things to Install in Claude" list (Workflows 8, Skills 8, Memory & context 7, Tools & connectors 10, Prompts & usage 7) transcribed from the infographic with what each item does, plus which ones this repo already has and how to vet before installing. Use when asked what to install for Claude Code, which workflow/skill/memory/tool packs exist, or to build a vetted install shortlist.
---

# 40 things to install in Claude (source: charliehills.substack.com infographic)
Names are as printed; **repo owners/URLs were not on the image** - resolve each by search and read its README and LICENSE before installing. Star counts and "gift" framing are the author's; none verified.

**Workflows (8):** learn-claude-code (agent basics, one building block at a time) - karpathy-skills (CLAUDE.md rules to reduce coding mistakes) - superpowers (plan, build, test; repeatable workflow; installed here) - ponytail (keep code simple, reuse what exists; installed) - gstack (planning/review/testing tools) - ECC (skills, memory, security, research checks; installed) - oh-my-claudecode (several agents as a team) - Archon (repeatable coding workflows).
**Skills (8):** taste-skill (stronger visual design; installed) - anthropics skills (official collection; installed) - mattpocock skills (engineering skills) - wshobson agents (specialist agents; many installed) - claude-plugins (official plugin directory) - addyosmani skills (production engineering) - ui-ux-pro-max (interfaces for different platforms) - awesome-claude-skills (curated list).
**Memory & context (7):** planning-with-files (plans in files across sessions) - claude-mem (relevant context back into future sessions) - codegraph (code connections index) - graphify (code, documents, schemas) - repomix (repo into one AI-friendly file) - agentmemory (memory between runs) - beads (task/progress tracking across sessions).
**Tools & connectors (10):** multica (assign work to coding agents) - firecrawl (website to usable text) - cc-switch (manage coding tools from one app) - context7 (current library docs; in `.mcp.json`) - vibe-kanban (agent tasks on a board) - github-mcp (GitHub via Claude) - playwright-mcp (browser; in `.mcp.json`) - serena (find code, targeted edits) - claude-code-router (route model requests) - awesome-mcp-servers (directory).
**Prompts & usage (7):** system-prompts-ai (system prompts of popular AI tools) - best-practice (Claude Code guidance) - codex-plugin-cc (Codex review/delegate) - claude-hud (context usage, tools, agents) - rtk (trim command output) - headroom (compress tool output/logs/files) - caveman (shorter replies; installed).

## Vet before installing
Official/publisher source only; read the code of anything with shell hooks; prefer read-only first; one pack at a time and measure token cost (`context-budget`, `token-audit`). Do not install 40 things: pick 3-5 for the job at hand. See `claude-skill-directories-12`, `dev-repos-to-clone`.
