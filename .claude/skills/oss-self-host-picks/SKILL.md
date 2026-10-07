---
name: oss-self-host-picks
description: Open-source self-hostable tools from @replace.so cards - RustDesk (remote desktop), Listmonk (newsletters and mailing lists), Dify (agentic workflow and RAG platform) and Tolgee (translation and localisation platform) - with what each replaces and verification status. Use when looking for a self-hosted alternative to TeamViewer, Mailchimp, a hosted LLM-app builder or a translation SaaS.
---

# Open-Source Picks (self-host)

Source: @replace.so carousels "I searched GitHub for you, these 5 repos are worth trying". Four of the five were readable; the fifth card was not.

| Tool | Replaces | Card description | Repo | Check |
|---|---|---|---|---|
| RustDesk | TeamViewer, AnyDesk | Open-source remote desktop written in Rust; self-host servers or use rendezvous and relay services | rustdesk/rustdesk | exists |
| Listmonk | Mailchimp-style tools | Self-hosted newsletter and mailing-list manager, single binary, modern dashboard | knadh/listmonk | exists |
| Dify | Hosted LLM app builders | Platform for agentic workflows, RAG pipelines, agents and LLM apps with model management | langgenius/dify | exists |
| Tolgee | Lokalise, Crowdin | Localisation platform: in-context editing, screenshots, machine translation, translation memory | tolgee/tolgee-platform | exists |

Warnings

- The RustDesk card shows a scam warning: only download from the official site and never install it for someone who phones you. Remote-desktop tools are a common scam vector.
- Listmonk sends email: check consent rules (GDPR, CAN-SPAM), set SPF, DKIM and DMARC, and warm up the sending domain.
- Self-hosting means you own updates, backups and security. Licences were not checked this batch.
