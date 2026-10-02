#!/usr/bin/env bash
# Batch 98 — installs the third-party pieces that Claude Code would not install for you in the cloud session.
# RUN THIS ON YOUR OWN MACHINE, from the repo root, after reading it. Every step asks first.
# Why this exists: in the cloud session the auto-mode classifier blocked `npx skills add` for these repos as
# "untrusted code integration", so nothing below has been executed by Claude. The repos were verified to exist
# and were cloned shallowly for reading; licences are noted per step.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }

echo "== 1. Agent skills (writes .agents/skills/* and updates skills-lock.json) =="
echo "   Review each skill's SKILL.md after install — skills are prompts that steer your agent."
ask "Install NVIDIA/OpenShell skills (4: openshell-cli, generate-sandbox-policy, debug-openshell-cluster, debug-inference; Apache-2.0)?" \
  && npx skills add NVIDIA/OpenShell -a claude-code -s '*' -y
ask "Install longbridge/gpui-kit skills (2: gpui-kit, gpui-kit-design-guides; Apache-2.0 + docs licence)?" \
  && npx skills add longbridge/gpui-kit -a claude-code -s '*' -y
ask "Install t8y2/dbx skill (1: dbx; Apache-2.0)?" \
  && npx skills add t8y2/dbx -a claude-code -s '*' -y

echo "== 2. PageIndex SDK (MIT) — needed by /pageindex-ask =="
ask "pip install -U pageindex (verified on PyPI: 0.2.20)?" && python3 -m pip install -U pageindex
echo "   Then export your LLM key in the shell (never in a file):  export OPENAI_API_KEY=..."

echo "== 3. hey — HTTP load generator (Apache-2.0) — needed by /loadtest =="
ask "go install github.com/rakyll/hey@latest?" && go install github.com/rakyll/hey@latest
echo "   (macOS alternative: brew install hey)"

echo "== 4. dbx MCP server — lets Claude query databases you configured in DBX (Apache-2.0) =="
echo "   Prerequisite: the DBX desktop app with connections set up. Set the mode in DBX Settings → MCP"
echo "   (Read only / Data read-write / Full access). START WITH READ ONLY."
ask "claude mcp add dbx -- npx -y @dbx-app/mcp-server (npm: 0.4.102)?" && claude mcp add dbx -- npx -y @dbx-app/mcp-server

echo "== 5. NVIDIA OpenShell runtime — NOT automated =="
echo "   The README installs with:  curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh"
echo "   Download install.sh, read it, then run it yourself. Needs Linux, or macOS on Apple Silicon, plus Docker/Podman."

echo "== 6. Connectors that need YOUR login (cannot be done by Claude) =="
echo "   claude.ai → Settings → Connectors: reconnect Stripe, Wispr Flow, MailerLite, Meridian QuickBooks;"
echo "   add Fathom, Granola, Pipedrive, Intuit QuickBooks if you use them."
echo "Done."
