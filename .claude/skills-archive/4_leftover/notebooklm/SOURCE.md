# Source

- Repo: https://github.com/PleasePrompto/notebooklm-skill (SKILL.md, scripts/, references/, requirements.txt, AUTHENTICATION.md)
- Commit: c80722d3f27d65e06b6579add201bf69b99101d0
- License: MIT (see LICENSE.txt)
- Not copied: README, CHANGELOG, images/.
- Added here: `.gitignore`, so `data/` (Google session cookies in `data/browser_state/`, the notebook library) and `.venv/` can never be committed.

## Read before using
- Runs on the owner's own machine, not in the cloud sandbox: it opens a real Chrome window, and the first run needs a manual Google login.
- That login is stored locally under `data/browser_state/`. Use a dedicated Google account, not the main business account.
- Automates the NotebookLM web UI with anti-detection flags (`--disable-blink-features=AutomationControlled`). Google can break it or restrict the account, and it may conflict with Google's terms.
- On first run `scripts/__init__.py` creates a `.venv` and pip-installs `patchright` and `python-dotenv` from PyPI. Nothing else is fetched at runtime.
- Do not feed it notebooks that hold patient or personal data (GDPR).
- Sibling skill: `notebooklm-skill` (claude-world, MCP-based, skill name `notebooklm-research`). The two overlap, so use one.
