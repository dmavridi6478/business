# Source

- Repo: https://github.com/goodnight000/api-anything (`skills/api-anything/` only)
- Commit: cd8d773d6617df07dc473598b67dec4d612276bc (package version 0.4.0)
- License: MIT (see LICENSE.txt)
- Not copied: the npm package source (`src/`), the plugin manifest and the MCP server entry.

## Read before using
- The skill is only instructions. The tools it calls (`find_sites`, `call_operation`, `learn_site`) come from the `api-anything` npm package. That package is NOT installed or registered here, and the MCP server entry was deliberately left out of `.claude/settings.json` so nothing runs `npx` automatically at session start.
- Without the MCP server the skill falls back to `npx -y api-anything <command>`, which downloads and runs code from npm on first use. Review the package before the first run.
- By default it talks to a shared public catalog. Run it in local-only mode (`--local-only`, or `API_ANYTHING_LOCAL_ONLY=1`) unless you want it to share anything.
- Never let it learn or share an operation that contains patient data, customer data, or the business's own logins. It stores site sessions and cookies on the machine it runs on.
- Third-party catalog entries are other people's words, not vetted code. Check that an operation's domain is the site you mean.
- Calling sites through undocumented requests can breach their terms of service. Read-only, public data, low volume.
