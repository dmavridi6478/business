#!/usr/bin/env bash
# Batch 125 - optional steps. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell and no key is stored.
# Done in the cloud session: 3 skills, 3 commands, 3 design templates, 2 themes, a workflows page and a prompts file; nothing was installed or connected.
# Facts read on 31 October 2026: nateherkai/roast-room (1,271 stars, created 10 Oct 2026, licence "Other"); Blotato docs (paid plan needed for MCP).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Read-only look at the advisor-room repository (licence shown as 'Other': read LICENSE first) =="
if ask "git clone nateherkai/roast-room into ~/src (look only; do not run npm start until you have read package.json)?"; then
  clone nateherkai/roast-room
  echo "   Next: read ~/src/roast-room/LICENSE and package.json. Needs Node 20+. Start with: npm start (then http://localhost:4730) and run 'claude' in that folder."
fi

echo "== 2. Blotato connector (needs YOUR paid Blotato account; MCP is not in the free trial) =="
echo "   Review first: https://help.blotato.com/start-with-an-ai-agent/mcp/setup"
echo "   It gives a third party posting rights on every account you connect. Test with one low-stakes account."
if ask "Show the Claude Code command to add Blotato (this script will NOT run it)?"; then
  echo "   claude mcp add --transport http blotato https://mcp.blotato.com/mcp"
  echo "   Then open Claude Code, run /mcp, select Blotato, authenticate in the browser, and ask:"
  echo "   List my connected Blotato accounts using blotato_list_accounts."
  echo "   Prefer OAuth over an API key; if you use a key, keep it out of any shared project config."
fi

echo "== 3. Not offered =="
echo "   Uploading a seller's data room to any AI service: check the NDA and data-room terms first and use a plan with no-training terms."
echo "   Any pack received by commenting a keyword (e.g. 'AGENTS', 'CMO', 'Link in my Community'): read every file before installing."
echo "Done. Restart Claude Code so the new commands appear."
