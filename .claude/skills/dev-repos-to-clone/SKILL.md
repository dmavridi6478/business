---
name: dev-repos-to-clone
description: Five open-source repos worth cloning as a starting point before building common product infrastructure from scratch — self-hosted analytics (plausible/analytics), a scheduling/booking system (calcom/cal.diy), a copy-into-your-repo UI component library (shadcn-ui/ui), a Postgres/auth/storage backend (supabase/supabase), and a virtual whiteboard/diagramming tool (excalidraw/excalidraw). Use when scoping a new product build and deciding whether to write analytics, scheduling, a component library, backend auth/storage, or diagramming from zero versus forking a mature, actively-maintained OSS project.
---

# Dev Repos Worth Cloning Before Writing Code

Five categories of infrastructure that almost never need a from-scratch build.
Each repo below is real, actively maintained, and was live-verified (star
count, commit recency) at the time this skill was written — check current
numbers before quoting them, they move fast.

| Repo | Category | What it replaces building | Clone |
|---|---|---|---|
| [`plausible/analytics`](https://github.com/plausible/analytics) | Web analytics | A cookie-free, GDPR-friendly Google Analytics alternative — one clean dashboard, no cookie banner, no vanity-metric bloat. Elixir/Phoenix. AGPL-3.0 | `git clone https://github.com/plausible/analytics` |
| [`calcom/cal.diy`](https://github.com/calcom/cal.diy) | Scheduling / booking | A complete booking system you host and control (the open-source core behind Cal.com), instead of building calendar-sync + availability + booking-page logic from zero. Next.js/Prisma. MIT | `git clone https://github.com/calcom/cal.diy` |
| [`shadcn-ui/ui`](https://github.com/shadcn-ui/ui) | UI component library | Accessible, beautifully-designed components you copy directly into your repo (not an npm dependency) — you own and can edit every line instead of fighting a component library's API. React/Tailwind/Radix | `npx shadcn@latest init` (or `git clone https://github.com/shadcn-ui/ui` to browse source) |
| [`supabase/supabase`](https://github.com/supabase/supabase) | Backend (DB/auth/storage) | Postgres database, authentication, storage, and realtime subscriptions as one dedicated backend, instead of hand-rolling auth and file storage around a raw database. Apache-2.0 | `git clone https://github.com/supabase/supabase` |
| [`excalidraw/excalidraw`](https://github.com/excalidraw/excalidraw) | Diagramming / whiteboard | A hand-drawn-style virtual whiteboard with real-time collaboration and one-link sharing, for embedding diagram/sketch capability instead of building a canvas editor. MIT | `git clone https://github.com/excalidraw/excalidraw` |

## When to reach for one instead of building

- Need analytics but don't want to hand Google a copy of your traffic data or make visitors click a cookie banner → `plausible/analytics` (self-host or use their cloud).
- Need "book a call" / appointment scheduling on your own domain, not an embedded third-party widget → `calcom/cal.diy`.
- Starting a new frontend and don't want to be locked into a component library's theming API → `shadcn-ui/ui` (copy components in, they become your code).
- Need a Postgres database with auth and file storage wired together, fast, without standing up three separate services → `supabase/supabase` (self-host or their managed cloud).
- Need users to sketch a flow, wireframe, or diagram together in the browser → `excalidraw/excalidraw` (also embeddable as a React component: `@excalidraw/excalidraw`).

## Before adopting any of them

Check current license terms and hosting costs (self-hosted vs. the vendor's
paid cloud tier) against the project's actual requirements — a mature repo
being free and open-source doesn't mean self-hosting it is free in
infrastructure/ops time. Read each project's own `CONTRIBUTING.md`/deployment
docs before going to production with it, since setup steps and dependencies
(Elixir/Phoenix for Plausible, a Postgres instance for Supabase and Cal.diy)
vary a lot from a typical Node/Python app.
