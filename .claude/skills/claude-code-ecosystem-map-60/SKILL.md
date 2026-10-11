---
name: claude-code-ecosystem-map-60
description: The @aisimplified23 "Claude Code Ecosystem Map" cheat sheet transcribed as a lookup - 60 names in 12 sections across 4 layers (Start here, Teach it, Extend it, Run it): getting started, models, commands, memory, skills, subagents, hooks, MCP, plugins, permissions, surfaces, automation. Use when someone asks "what does X do in Claude Code", wants to know where a feature lives, or when auditing a repo's Claude Code setup (/ecosystem-audit). Model names and features are as printed on the image (Aug-Oct 2026) and may drift.
---

# Layer 1 - START HERE (15 names)
- **Get started:** `claude` (start a session in this folder) · `/init` (writes your first CLAUDE.md) · `claude -c` (picks up your last session) · `claude update` (pulls latest version) · `/doctor` (checks your install and fixes it)
- **Models:** `/model opus` (Opus 5.5, deep reasoning) · `/model sonnet` (Sonnet 5.5, everyday code) · `/model fable` (Fable 5.1, "the top model") · `opusplan` (Opus plans, Sonnet builds) · `/effort` (sets how hard it thinks)
- **Commands:** `/plan` (plans before it edits) · `/compact` (shrinks a long chat to a summary) · `/clear` (fresh context, same folder) · `/rewind` (rolls back to an earlier point) · `/context` (shows what fills the window)
# Layer 2 - TEACH IT (15)
- **Memory:** `CLAUDE.md` (rules read every session) · `CLAUDE.local.md` (private project notes) · `.claude/rules/` (rules split by topic) · `AGENTS.md` (read if there is no CLAUDE.md) · Auto memory (saves what it learns as it works)
- **Skills:** `SKILL.md` (one job, plain words) · `.claude/skills/` (where skills live) · `/skill-name` (runs any skill by name) · `/skills` (lists every skill) · `/code-review` (built-in skill that reviews code)
- **Subagents:** Explore (fast read-only code search) · Plan (researches for plan mode) · General-purpose (explores and edits on long jobs) · `.claude/agents/` (your own specialists) · `Ctrl+B` (sends a task to the background)
# Layer 3 - EXTEND IT (15)
- **Hooks:** PreToolUse (checks a tool call before it runs) · PostToolUse (acts after a tool runs) · UserPromptSubmit (adds context to every prompt) · SessionStart (loads context as you open) · Stop (runs when Claude finishes)
- **MCP:** `claude mcp add` (connects a tool server) · `claude mcp list` (lists every server) · `.mcp.json` (shares servers with your team) · `/mcp` (checks and reconnects servers) · `claude mcp serve` (runs Claude Code as a server)
- **Plugins:** `/plugin` (browse and install) · Marketplaces (catalogues you add plugins from) · `plugin.json` (bundles skills, agents, hooks, MCP) · Mods (change how the app looks and acts) · `/reload-plugins` (apply changes without a restart)
# Layer 4 - RUN IT (15)
- **Permissions:** `Shift+Tab` (cycles permission modes) · Auto mode (a second model checks each step) · Plan mode (reads and plans, never edits) · `/permissions` (allow, ask and deny rules) · `settings.json` (project, user and local scopes)
- **Surfaces:** `/desktop` (moves a session to the app) · `claude.ai/code` (runs in the cloud, in a browser) · VS Code (plus JetBrains, in your editor) · Remote Control (steer a session from your phone) · `/install-slack-app` (adds Claude to your Slack)
- **Automation:** `claude -p` (one shot, no chat, for scripts) · `/goal` (keeps going until it is met) · `/loop` (repeats a prompt on a timer) · Routines (cloud runs on a schedule or event) · Agent SDK (build your own agent on it)

# Using it
- Audit a repo against the four layers with `/ecosystem-audit` (agent `claude-code-setup-coach`).
- Verify any command in your installed version (`/help`, `claude --help`); the image is a cheat sheet, not documentation. In this environment `claude plugin install` uses the marketplace `anthropic-plugin-directory`, not `claude-plugins-official`.
- Related: `claude-cheat-sheet`, `claude-code-superpowers`, `harness-audit` (command).
