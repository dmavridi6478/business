# claude-code-setup Plugin

Official Claude plugin that scans your project and recommends exactly which hooks, skills, MCPs, and subagents to configure — so you don't have to figure it out manually. By @codenameposhan.

## Install

Inside Claude Code, run:

```
/plugin install claude-code-setup@claude-plugins-official
```

## What It Does

Analyzes your codebase and produces a personalized recommendation for:

| Component | What It Recommends |
|-----------|-------------------|
| **Hooks** | Pre/post-tool hooks for your workflow |
| **Skills** | Skills that match your project type |
| **MCPs** | MCP servers for your tech stack |
| **Subagents** | Specialized agents for your tasks |

## Usage

After installing, ask Claude:

```
recommend automation for this project
```

Claude will scan the repo structure, stack, and existing config, then output a full setup plan.

## Package as a Plugin (Team Sharing)

To share your `.claude/` config with teammates without committing it to the repo:

```
/plugin marketplace add .
```

This packages your `skills/agents/hooks` into a versioned plugin anyone on the team can install — keeps personal settings out of git while making team settings installable.

## Full Workflow

```
1. /plugin install claude-code-setup@claude-plugins-official
2. recommend automation for this project
3. Review recommendations → apply ones that fit
4. /plugin marketplace add .   (optional — share with team)
```

## Notes

- The plugin runs on **Claude Opus 5** with 1M context by default
- It reads your existing CLAUDE.md, package.json, directory structure, and current `.claude/` config
- Particularly good at spotting missing MCP servers for your tech stack (Supabase, GitHub, Linear, etc.)
- Works alongside DevSwarm.ai for multi-agent team workflows

## Video notes (@sadie.ontech, 19 Oct 2026)

Screen text from a ~70-second video; the spoken captions are fragments, so only on-screen text is recorded.

- **Claude Code Setup Plugin** - "Analyze codebases and recommend tailored Claude Code automations - hooks, skills, MCP servers, and more." Scans your codebase and recommends the top 1-2 automations in each category:
  1. MCP servers - external integrations (context7 for docs, Playwright for frontend)
  2. Skills - packaged expertise (Plan agent, frontend-design)
  3. Hooks - automatic actions (auto-format, auto-lint, block sensitive files)
  4. Subagents - specialised reviewers (security, performance, accessibility)
  5. Slash commands - quick workflows (/test, /pr-review, /explain)
- "This skill is read-only - it analyzes but doesn't modify files."
- Usage prompts shown: "recommend automations for this project", "help me set up Claude Code", "what hooks should I use?"
- Also flashed: "#2 Superpowers" (a plugin of workflow skills), a local router sketch ("IDE / CLI -> Route - smart ... tiers: cheap vs strong models, circuit breakers"), and a GitHub-repo security scan ("Claude analyzes your GitHub repository ... misconfigurations ...").

### Using it in this repository

1. Run the plugin's recommendation prompt on a repo; treat the output as suggestions.
2. Compare each suggestion with what already exists: this repo has 1,000+ skills, 700+ commands and many agents, so the answer to "what should I add" is usually **nothing or one hook**. Use `capability-scout` first.
3. Prefer hooks that block (secrets, destructive commands) over new skills.
4. Do not install the plugins listed from a video without reading their source and permissions.

Overlap: `claude-code-tooling` covers general tooling.
