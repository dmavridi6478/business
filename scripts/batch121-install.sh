#!/usr/bin/env bash
# Optional, user-run. Checks that each repo exists and asks before each shallow clone into ~/batch121-repos (READ ONLY; nothing is installed or run).
# Excluded on purpose: boykopovar/AnyPS5 (DRM/copyright). Owner/name pairs come from slides and may be wrong.
set -u
REPOS="NVIDIA/OpenShell flutter/flutter EpicGames/raddebugger anthropics/claude-code tashfeenahmed/freellmapi Shubhamsaboo/awesome-llm-apps JCodesMore/ai-website-cloner-template momenbasel/PureMac ShawnPana/phone-harness conductor-oss/conductor langflow-ai/langflow triggerdotdev/trigger.dev"
DEST="${HOME}/batch121-repos"; mkdir -p "$DEST"
for r in $REPOS; do
  if ! git ls-remote "https://github.com/$r" >/dev/null 2>&1; then echo "MISSING or private: $r"; continue; fi
  read -r -p "Clone $r for reading? [y/N] " a
  [ "$a" = "y" ] && git clone --depth 1 "https://github.com/$r" "$DEST/${r//\//__}"
done
echo "Read the code before running anything. Never put real API keys into an unreviewed tool."
