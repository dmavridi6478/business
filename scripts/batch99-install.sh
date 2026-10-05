#!/usr/bin/env bash
# Batch 99 - optional third-party installs. RUN ON YOUR OWN MACHINE from the repo root, after reading it. Every step asks first.
# Nothing here was executed by Claude: the repos were verified to exist (git ls-remote / npm view) and four were cloned
# shallowly into repos/ for reading. Licences were read from the cloned LICENSE files (all MIT).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }

echo "== 1. Hindsight - agent memory (MIT) =="
ask "pip install hindsight-client (Python client only; the server is Docker or 'pip install hindsight-api')?" && python3 -m pip install -U hindsight-client
echo "   Server (optional): see https://github.com/vectorize-io/hindsight#quick-start - it needs an LLM key in YOUR shell, never in a file."

echo "== 2. Brigade - self-hosted agent ecosystem (MIT) =="
echo "   It runs a gateway and can open public tunnels. Try it in a VM or container, not on a machine holding client data."
ask "npm i -g @spinabot/brigade (1.39.0 on npm)?" && npm i -g @spinabot/brigade

echo "== 3. Skyvern MCP for Claude Code (browser automation) =="
echo "   Skyvern fills forms and clicks on real websites. It breaks the OS rule 'agents never touch the web beyond a read-only fetch':"
echo "   never connect it to an os-* agent, and use it only for tasks you supervise. You need a Skyvern account/API key (free tier per the video)."
echo "   Follow https://www.skyvern.com/docs (the video shows Settings > Integrations > MCP > Claude Code) and run the exact 'claude mcp add' command shown there."

echo "== 4. CodeGraph - code index for agents (MIT) - NOT automated =="
echo "   The README installs with: curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh"
echo "   Download install.sh, read it, then run it yourself; then 'codegraph install' configures your agents (it edits their configs: review the diff)."

echo "== 5. Local models and the app stack (documented only) =="
echo "   Ollama: https://github.com/ollama/ollama  | Langfuse: self-host with Docker  | Supabase / Expo: per their docs."
echo "   Check each model licence and your hardware before choosing a local model."

echo "== 6. Courses to clone for offline reading (large; optional) =="
ask "git clone --depth 1 the four course repos into ~/courses?" && {
  mkdir -p ~/courses && cd ~/courses
  for r in microsoft/mcp-for-beginners microsoft/generative-ai-for-beginners huggingface/agents-course anthropics/courses; do
    git clone --depth 1 "https://github.com/$r.git"
  done
}

echo "== 7. Connectors that need YOUR login (cannot be done by Claude) =="
echo "   Already connected in the cloud session: Notion, Calendly, Gmail, Google Calendar, Google Drive."
echo "   Reconnect when you need them: Stripe, MailerLite, Meridian QuickBooks, Wispr Flow. Not available: SERPtag, Loom."
echo "Done."
