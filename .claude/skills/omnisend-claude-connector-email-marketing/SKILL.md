---
name: omnisend-claude-connector-email-marketing
description: Reference for the "5 minutes to smarter email marketing with Claude" Omnisend vendor infographic, covering the connector setup steps (Customize, Add, Browse connectors, search Omnisend MCP, approve), four sample prompts, and what could not be verified. Use when an Omnisend account owner wants Claude to read their email stats. No connector was authorized in this session.
---

# Omnisend connector in Claude (vendor infographic, Batch 111)

Source: one Omnisend marketing infographic, "5 minutes to smarter email marketing with Claude". It is a **vendor advertisement**, so its numbers (for example "150,000+ brands" and "$79 back per $1") are unverified claims by the seller.

## Setup steps as drawn
1. In Claude open Customize.
2. Choose Add, then Browse connectors.
3. Search "Omnisend MCP" and approve the connection.
4. Start a chat and ask a question.

**Not done here:** a connector needs your own Omnisend account and your authorization in claude.ai settings. This session cannot start that sign-in, so nothing was connected. Only approve a connector listed under your own claude.ai connectors, and read which permissions it asks for (read only versus write).

## Four sample prompts (plain text)
1. "Give me a snapshot of my Omnisend account: list size, recent campaigns, and anything that looks off."
2. "Show my top 5 campaigns by revenue and what they have in common."
3. "Check my deliverability: open and click trends, bounces and complaints, and what to fix first."
4. "Recommend 3 segments that would move revenue and explain the data behind each."

## Use it safely
- **[Certain]** Prompts 1 to 4 are read-only questions; keep the connector read-only if the option exists and never let Claude send or schedule a campaign without a human reading the final copy and the audience.
- **[Likely]** Revenue attribution in any email platform depends on its tracking window; ask Claude to state the window it used.
- Customer emails are personal data (GDPR); do not paste exports into chats outside your approved tools.
- Related: `claude-marketing-50-ways`, `one-person-content-system`.
