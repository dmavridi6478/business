#!/usr/bin/env bash
# Optional: clone the PM repos into ~/pm-repos for READING only. Verifies each repo exists first.
# Handles come from an AI-looking infographic and may be wrong. Nothing is installed or executed.
set -u
REPOS="erikholmberg/ai-pm-toolkit dend/awesome-product-management aakashg/pm-prompt-library yuhenobi/awesome-product-manager ryancproduct/product-ai-toolkit Dher10/pm-ai-playbook aza-ali/awesome-ai-product-management wwwazzz/senior-pm-prompt deanpeters/product-manager-prompts lukesw55/ai-pm-toolkit"
DEST="${HOME}/pm-repos"; mkdir -p "$DEST"
for r in $REPOS; do
  if ! git ls-remote "https://github.com/$r" >/dev/null 2>&1; then echo "MISSING or private: $r"; continue; fi
  read -r -p "Clone $r for reading? [y/N] " a
  [ "$a" = "y" ] && git clone --depth 1 "https://github.com/$r" "$DEST/${r//\//__}"
done
echo "Read before using. Do not copy hooks or scripts into .claude/ unreviewed."
