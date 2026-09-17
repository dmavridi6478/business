# Hidden SEO Tools

Three professional SEO tools that rarely make the lists — each solves a specific problem that the popular tools miss.

---

## 1. Sitebulb

**What it does:** Desktop website crawler with deep technical SEO auditing. Runs on your machine, so no data leaves your environment.

**Why it's underrated:**
- Generates visual site architecture maps — not just a flat list of URLs
- Prioritises issues by impact, not just count (so you know what to fix first)
- Has a **native MCP server**, meaning Claude can query your crawl data directly

**Install & use:**
```
Download: https://sitebulb.com
Pricing: paid (desktop app, one-time or subscription)

MCP setup:
1. Run a crawl in Sitebulb
2. Enable the Sitebulb MCP server in app settings
3. Add the MCP server to Claude Code via /mcp
4. Ask Claude: "What are the top technical SEO issues in my crawl?"
```

**Best for:** Technical SEO audits, crawl budget analysis, internal link architecture, identifying orphaned pages.

---

## 2. SERPtag

**What it does:** Lightweight rank tracker that focuses on SERP feature tracking, not just position numbers.

**Why it's underrated:**
- Tracks whether you're appearing in featured snippets, People Also Ask, image packs, local packs — not just blue links
- Shows SERP volatility alongside your rankings (so you know if a ranking drop is your fault or Google's)
- Much cheaper than Semrush/Ahrefs for rank tracking only

**Use:**
```
Access: https://serptag.com
Add your domain and target keywords
Set up daily or weekly tracking
Review the SERP feature column — that's where the real insight is
```

**Best for:** Monitoring SERP feature gains/losses, understanding why traffic dropped when rankings didn't, lightweight rank tracking without paying for a full suite.

---

## 3. Detailed SEO Extension

**What it does:** Browser extension that overlays SEO data on any page you visit — no separate tool window needed.

**Why it's underrated:**
- Shows on-page structure (H1-H6 hierarchy, meta tags, canonical, hreflang) at a glance
- Schema markup viewer built in — see exactly what structured data is implemented
- Checks internal/external link counts, noindex/nofollow signals, and page speed indicators without leaving the page
- Free

**Install:**
```
Chrome: search "Detailed SEO Extension" in Chrome Web Store
Firefox: search same in Firefox Add-ons

Usage: visit any page → click the extension icon → full on-page SEO audit appears inline
```

**Best for:** Quick competitive analysis while browsing, on-page audits during content reviews, verifying schema implementation without a separate tool.

---

## Claude + SEO workflow

```
1. Run Sitebulb crawl → connect via MCP → ask Claude to prioritise the top 10 technical issues and draft fix tickets

2. Pull SERPtag rank data → paste weekly report into Claude → ask "What dropped this week and why?"

3. Use Detailed SEO Extension on a competitor page → screenshot the schema panel → ask Claude "How does their schema compare to mine and what should I add?"
```

---

## Why these three

| Tool | Gap it fills | Cost |
|------|-------------|------|
| Sitebulb | Deep technical crawl + MCP integration | Paid |
| SERPtag | SERP feature tracking (not just positions) | Freemium |
| Detailed SEO | On-page audit without leaving the browser | Free |

Together they cover technical, SERP intelligence, and on-page — without duplicating what Ahrefs or Semrush already do well.
