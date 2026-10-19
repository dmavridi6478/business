---
name: customer-research-stack
description: Six free-or-freemium tools for finding and tracking your first customer conversations from the @dotdevs series - Tally forms, F5Bot mention alerts, SparkToro audience research, Twenty CRM, DocuSeal PDF signing, Fider feature voting - each with its one-line job and first test. Use when a founder asks where to find first customers, how to collect answers before building, or which lightweight stack replaces a spreadsheet of DMs. Run via /research-stack. Extends the customer-research skill with a tool layer; it does not replace its methods.
---

# First-customer tool stack (@dotdevs)

Slides: Tally, F5Bot, SparkToro, Twenty, DocuSeal, Fider. Pricing and free limits were not on the slides; check each site before relying on them.

| Tool | Site | Job | First test (from the slide) | Stage |
|---|---|---|---|---|
| Tally | tally.so | Collect answers before building another feature | Ask what people tried before your app, then why it failed | Find |
| F5Bot | f5bot.com | Hear when people mention your product category | Add a specific problem keyword; review matching discussions | Find |
| SparkToro | sparktoro.com | Find websites and communities your audience already visits | Describe one customer group; inspect its audience report | Find |
| Twenty | twenty.com | Keep customer conversations out of scattered DMs | Add one contact, one opportunity and the next follow-up | Track |
| DocuSeal | docuseal.com | Turn a PDF into a signing workflow | Upload a sample PDF, add signature fields, preview | Close |
| Fider | fider.io | Put repeated feature requests in one place | Post one request, let users vote and add context | Learn |

Flow: **Find** (Tally + F5Bot + SparkToro) -> **Track** (Twenty) -> **Close** (DocuSeal) -> **Learn** (Fider).

## Rules

- Mine public signal first, then ask (see `customer-research`, modes 2 and 3).
- F5Bot and any scraping-adjacent tool: stay inside each site's terms; reply as a human, never auto-post.
- Contacts are personal data: record the lawful basis before they go into a CRM.
- Connectors: `n8n` and `Tally` exist as claude.ai connectors (not installed in this session; the user authorises them). No connector was found for SparkToro, Twenty, F5Bot, DocuSeal or Fider; Docusign is a different product from DocuSeal.
