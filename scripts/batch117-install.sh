#!/usr/bin/env bash
# Batch 117 - nothing to install. Optional: run the trained-attention demo locally in a virtualenv.
set -euo pipefail
read -r -p "Create ~/.venvs/attn with numpy and run the part-31 attention demo? [y/N] " a
if [[ "$a" =~ ^[Yy]$ ]]; then
  python3 -m venv "$HOME/.venvs/attn" && "$HOME/.venvs/attn/bin/pip" install numpy
  "$HOME/.venvs/attn/bin/python" .claude/skills/ml-transformer-part31/scripts/attention_train_from_scratch.py
fi
echo "No plugins, connectors or repos were added for batch 117."
