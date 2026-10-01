# Tool stack and connector status

Checked against this workspace's connector list on 2026-10-01. A connector that is not **connected** cannot be used by an agent until you authorise it in claude.ai → Settings → Connectors. Agents work from pasted exports when a connector is missing.

## Stack named in the source videos

| Tool (as shown) | Role | Connector status | Connected alternative |
|---|---|---|---|
| Claude (orchestrator, shown as "Opus 5.5") | reasoning, routing | this session | — |
| Codex, "Groq" (spelled so on screen; likely Grok) | builders / implementers | no connector here | use Claude subagents (`model: sonnet/haiku`) |
| Fathom, Granola | meeting notes | **not installed** (both exist in the connector directory) | **Fireflies — connected** |
| Wispr Flow | voice to text | **connect_incomplete** — finish OAuth | — |
| Spark Email | email client | no connector | **Gmail — connected** |
| 1Password | secrets | no connector; never give agents secrets | — |
| Orca | agent workspace | no connector (see `orca-cli` skills) | — |
| Notion | SOPs, tasks | **connected** | — |
| Slack | approvals | **connected** | — |
| Google Calendar | scheduling | **connected** | — |
| Canva | lead-magnet design | **connected** | Gamma, Figma also connected |
| Meta Ads | ads data | via **Motion Creative Analytics** and **Supermetrics** (connected) | Adspirer not installed |
| Semrush / Ahrefs | SEO | **connected** | — |
| Klaviyo | email/SMS | **connected** | MailerLite needs reconnect |
| Pipedrive | CRM | **not installed** | **HubSpot — connected** |
| QuickBooks | books | Meridian: **connect_incomplete**; Intuit QuickBooks: not installed | — |
| Stripe | invoices/payments | **needs_reconnect** | — |

## OWNER MUST FILL IN

- Business name and one-line offer:
- Ideal customer profile and exclusions:
- Service area / languages:
- Where leads arrive (form, email, DM, phone):
- Where the books live:
- Who is the human approver and the backup:
