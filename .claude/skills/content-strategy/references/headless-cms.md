# Headless CMS Guide

*Authored directly for this repo — the parent skill's References section pointed here, but no source content shipped with the install. This fills that gap.*

## When this decision comes up

Once a content strategy is producing enough content pillars/clusters to need real editorial workflow (multiple authors, review steps, scheduled publishing, content reused across channels), the question of *where the content lives* becomes a real infrastructure decision — not just "which blog platform."

## Headless vs. traditional CMS

| | Traditional CMS (e.g. WordPress default setup) | Headless CMS |
|---|---|---|
| Content + presentation | Coupled — the CMS renders the page | Decoupled — CMS stores content, a separate frontend renders it |
| Best for | A single website, fast setup, non-technical editing | Content reused across multiple channels (web, app, marketing site, email) |
| Frontend flexibility | Limited to the CMS's templating | Full control — frontend can be any framework |
| Setup cost | Low | Higher — requires building/maintaining the frontend separately |

**Decision rule**: if content only ever needs to become one webpage, a traditional CMS is usually simpler and cheaper. Reach for headless when the same content needs to reach more than one surface (site + app, site + newsletter, site + partner syndication) or when the frontend needs to be something the CMS's own templating can't produce.

## Platform comparison

| Platform | Strengths | Trade-offs | Best fit |
|---|---|---|---|
| **Sanity** | Highly customizable structured content (Portable Text), real-time collaborative editing, strong developer experience, generous free tier | Requires more setup/schema design work upfront than a turnkey CMS | Teams with developer resources who want deep content modeling flexibility |
| **Contentful** | Mature enterprise features (roles/permissions, localization, workflow approvals), large ecosystem/integrations | Pricing scales up quickly past the free tier; less flexible content modeling than Sanity for complex nested content | Larger orgs needing enterprise governance, multi-locale content, and established integrations |
| **Strapi** | Open-source, self-hostable (full control over data/infra), no vendor lock-in, free at the core | Self-hosting means you own uptime/scaling/security; hosted version (Strapi Cloud) trades that back for cost | Teams wanting to avoid per-record/per-seat SaaS pricing, or with existing infra to self-host on |

## Content modeling for marketing use

When designing the content model (schema) in a headless CMS for a marketing content strategy specifically:

- **Model by content type, not by page.** A "blog post" type, a "case study" type, a "landing page" type — each with fields matching what that content actually needs (a case study needs a "results" field structure; a blog post doesn't).
- **Separate reusable content blocks from page-specific content** — a CTA block, an author bio, a related-posts block should be modeled once and referenced, not copy-pasted into every content type.
- **Model for the content pillars/clusters structure**, not just flat posts — a "pillar" reference field on cluster content lets the CMS itself enforce and query the hub-and-spoke structure this skill's Content Pillars section describes, rather than relying on manual tagging discipline alone.
- **Plan localization fields early** if any non-English output is anticipated (per this repo's Greek-language conventions elsewhere) — retrofitting localization into an existing content model is significantly more painful than designing for it from the start.

## Editorial workflow patterns

- **Draft → Review → Scheduled → Published** as a minimum status pipeline — most headless CMS platforms support custom workflow states; use them rather than relying on a spreadsheet or Slack thread to track review status.
- **Assign an explicit reviewer per content type**, not just "someone on the team" — unowned review steps are where publishing pipelines stall.
- **Use scheduled publishing** for coordinated launches (aligning a blog post with a product announcement) rather than manual publish-day coordination.

## Related skills in this repo

- **content-strategy**: This file is that skill's CMS/infrastructure companion — use once pillars and clusters exist and need a real home, not before.
- **doc-coauthoring**: Drafting still happens there; this guide covers where the finished draft lives and how it moves through review to publish.
