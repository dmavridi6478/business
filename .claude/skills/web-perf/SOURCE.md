# Source

- Repo: https://github.com/cloudflare/skills (`skills/web-perf/` only)
- Commit: 5108325ecceabc899c761e07aa617b09c02445ee
- License: Apache-2.0 (see LICENSE.txt)
- Why only this one: the other 21 skills in the repo are Cloudflare developer and infrastructure skills (Workers, Durable Objects, Wrangler, Zero Trust, Sandbox and so on). They were reviewed and not installed.
- Optional dependency: the skill suggests the Chrome DevTools MCP (`npx -y chrome-devtools-mcp@latest`) for live audits. It is not registered here. Without it, use Lighthouse or PageSpeed Insights output as input.
