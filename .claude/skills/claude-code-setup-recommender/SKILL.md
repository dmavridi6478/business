---
name: claude-code-setup-recommender
description: Notes from the @sadie.ontech video on the Claude Code Setup plugin (claude-automation-recommender) that scans a codebase and recommends the top 1-2 automations in each of five categories - MCP servers, skills, hooks, subagents, slash commands - read-only. Also lists the other tools the video flashes (Superpowers plugin, an LLM router with cheap/expensive tiers, a code-security scan). Use when someone asks what to install for a project or how to find the right Claude Code automations. Run via /setup-recommend.
---

# Claude Code Setup recommender

Source: ~70-second video (@sadie.ontech). Spoken captions are fragments; the screen text is the reliable part.

## From the screen

- **Claude Code Setup Plugin** - "Analyze codebases and recommend tailored Claude Code automations - hooks, skills, MCP servers, and more." Scans your codebase and recommends the top 1-2 automations in each category:
  1. MCP servers - external integrations (context7 for docs, Playwright for frontend)
  2. Skills - packaged expertise (Plan agent, frontend-design)
  3. Hooks - automatic actions (auto-format, auto-lint, block sensitive files)
  4. Subagents - specialised reviewers (security, performance, accessibility)
  5. Slash commands - quick workflows (/test, /pr-review, /explain)
- "This skill is read-only - it analyzes but doesn't modify files."
- Usage prompts shown: "recommend automations for this project", "help me set up Claude Code", "what hooks should I use?"
- Also flashed: "#2 Superpowers" (a plugin of workflow skills), a local router sketch ("IDE / CLI -> Route - smart ... tiers: cheap vs strong models, circuit breakers"), and a GitHub-repo security scan ("Claude analyzes your GitHub repository ... misconfigurations ...").

## How to use it here

1. Run the plugin's recommendation prompt on a repo; treat the output as suggestions.
2. Compare each suggestion with what already exists: this repo has 1,000+ skills, 700+ commands and many agents, so the answer to "what should I add" is usually **nothing or one hook**. Use `capability-scout` first.
3. Prefer hooks that block (secrets, destructive commands) over new skills.
4. Do not install the plugins listed from a video without reading their source and permissions.

Overlap: `claude-code-tooling` covers general tooling.
