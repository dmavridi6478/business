# Batch 113 action plan (files numbered 117)

## Do first
1. Run `/eda-plan` on one real CSV before you model it. Check missing values, duplicates and outliers first.
2. If you test against AWS and use Docker, read Floci's README and compare its service list with yours.
3. Treat "trending" lists as attention, not safety: read any skill repo (for example `cloudflare/security-audit-skill`) before it runs with your agent's permissions.

## Careful
- kimi-k3-in-c needs a 1.56 TB checkpoint and is slow at small RAM: it is a research demonstration, not a GPU replacement.
- Worktrunk's shell install changes your shell config: read what it adds.
- Sherlock finds a username across sites: use it on yourself or with consent.

## Not done
No connector, agent or workflow (none in the files). Nothing cloned or run. `.mcp.json` unchanged.
