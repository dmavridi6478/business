---
name: salesdaily-claude-10-sales-tools-connectors
description: The SalesDaily "Let Claude work inside these 10 sales tools" graphic (lemlist, Prospeo, Lusha, G2, FullEnrich, Gmail, Google Calendar, Google Drive, Slack, Loom) with the three-step connection method, one sample ask per tool, the three custom connector URLs shown, and security cautions. Use when connecting sales tools to Claude. No connector was added in this session.
---

# Let Claude work inside 10 sales tools (SalesDaily graphic)

Source: one infographic (salesdaily.co). Vendor and newsletter content, so claims such as "Claude only sees what you connect" are the publisher's, not verified.

## Connection method as drawn
1. In Claude open Settings, then Connectors, then Browse connectors.
2. Pick a tool and log in with your own account. Each tool needs its own account.
3. Ask in plain words.
Tip on the graphic: start with Gmail and Calendar. Three tools are "not in the directory yet": add them through "Add custom connector" using the URLs on the graphic (`https://app.lemlist.com/mcp`, `https://mcp.prospeo.io`, `https://mcp.fullenrich.com/mcp`).

## The ten tools and the sample ask
| # | Tool | Does | Sample ask on the graphic |
|---|---|---|---|
| 1 | lemlist | Runs sequences and inbox | "Add these leads to my [campaign] and show me who replied." |
| 2 | Prospeo | Builds lists with verified emails | "Find Heads of Sales at [your ICP] with verified emails." |
| 3 | Lusha | Buying signals on your accounts | "Which of my target accounts are hiring salespeople?" |
| 4 | G2 | Reviews and buyer intent | "What do reviewers complain about in [competitor]?" |
| 5 | FullEnrich | Enriches lists from 20+ providers | "Find mobile numbers for the 50 leads in this list." |
| 6 | Gmail | Reads threads, drafts replies | "Who's still waiting on a reply from me?" |
| 7 | Google Calendar | Sees meetings and free time | "Prep me for every external meeting tomorrow." |
| 8 | Google Drive | Searches docs and files | "Find the last proposal we sent [company]." |
| 9 | Slack | Searches channels and threads | "What did my team say about [account] this month?" |
| 10 | Loom | Your videos, via the Atlassian connector | "Find the Loom I sent [prospect] and draft my follow-up from it." |

## Cautions
- **[Certain]** A custom connector URL gives that server a path into your Claude session. Add only URLs you have verified on the vendor's own documentation, not from an image, and prefer read-only scopes.
- **[Certain]** Prompts 1, 2 and 5 touch personal data (emails, phone numbers). Mobile-number enrichment and cold outreach carry GDPR, ePrivacy and telemarketing rules; confirm a lawful basis first.
- **[Likely]** Letting Claude write to lemlist or send from Gmail without review risks mass-sending errors; keep drafts as drafts.
- Not done here: no connector added, no sign-in, nothing sent. See also `claude-connectors-by-category`, `connector-stack`, `claude-sales-prompts-20`.
