#!/usr/bin/env bash
# Batch 104 - RUN ON YOUR OWN MACHINE from the repo root. Every step asks first. Nothing pipes a download into a shell.
# Why this exists: the cloud session was blocked from writing .claude/ and .mcp.json, so the skills, commands and agents
# are staged in docs/batch104/install-pack/ and copied in here.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
P=docs/batch104/install-pack
ask "Copy 26 LinkedIn skills + 7 new skills into .claude/skills (skips existing)?" && for d in $P/skills/*/; do n=$(basename "$d"); [ -e ".claude/skills/$n" ] && echo "  skip $n" || cp -r "$d" ".claude/skills/$n"; done
ask "Copy 11 commands into .claude/commands?" && for f in $P/commands/*.md; do [ -e ".claude/commands/$(basename $f)" ] && echo "  skip $f" || cp "$f" .claude/commands/; done
ask "Copy 5 agents into .claude/agents?" && for f in $P/agents/*.md; do [ -e ".claude/agents/$(basename $f)" ] && echo "  skip $f" || cp "$f" .claude/agents/; done
ask "Add the Taplio MCP (https://mcp.taplio.com) to this project?" && claude mcp add --transport http taplio https://mcp.taplio.com
echo "Then run /mcp and authenticate Taplio (it shows 'needs reconnect' in your claude.ai connectors)."
ask "Shallow-clone the 5 free coding agents into ~/src (read first, install later)?" && for r in cline/cline anomalyco/opencode OpenHands/OpenHands Aider-AI/aider continuedev/continue; do
  [ -d "$HOME/src/${r#*/}" ] || { mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$r.git" "$HOME/src/${r#*/}"; }; done
echo "Installs (run yourself after reading): npm i -g cline | npm i -g opencode-ai@latest | npm i -g @openhands/agent-canvas | python -m pip install aider-install && aider-install"
echo "Continue's README says 2.0.0 was its final release - consider skipping it."
ask "Copy the Obsidian vault scaffold to ~/Obsidian/FITNESS SECOND BRAIN?" && mkdir -p "$HOME/Obsidian" && cp -r docs/ai-coach/FITNESS-SECOND-BRAIN "$HOME/Obsidian/FITNESS SECOND BRAIN"
echo "Supabase: review docs/ai-coach/supabase-schema.sql, then run it in a NEW project named FITNESS DATA. Telegram: BotFather /newbot (manual)."
