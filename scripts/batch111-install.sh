#!/usr/bin/env bash
# Batch 111 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: skills, commands, prompts and a Blotato entry in .mcp.json were added; nothing was installed or authenticated.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Claude Code plugins (official marketplace) =="
for p in modern-web-guidance browser-use lovable; do
  ask "run '/plugin install $p@anthropic-plugin-directory' inside Claude Code yourself? (prints the command)" && echo "   /plugin install $p@anthropic-plugin-directory"
done

echo "== 2. Blotato connector (needs a PAID Blotato plan; OAuth in the browser) =="
ask "add the Blotato MCP server to Claude Code?" && claude mcp add --transport http Blotato https://mcp.blotato.com/mcp && echo "   Now run /mcp -> Blotato -> Authenticate. Ask for drafts first; it posts live."

echo "== 3. Clone for reading (shallow; no install) =="
for r in OpenClaudia/openclaudia-skills obra/superpowers vectorize-io/hindsight upstash/context7 microsoft/playwright-mcp github/github-mcp-server; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 4. Read first, not automated =="
echo "   Swaps (Void, Hyprnote, Perplexica, ComfyUI, Open WebUI+Ollama, Handy, LanguageTool, Activepieces): check each repo's licence and hardware needs; see ai-tool-swaps-8."
echo "   Install-list items (claude-install-list-40): repo owners were not on the image; resolve and read before installing."
echo "Done. Restart Claude Code so new commands appear."
