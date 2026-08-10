# Procedure: Free/Open-Source Tool vs. Paid SaaS Decision

## When this applies

Choosing between a free/open-source desktop tool (e.g. one from
`lean-software-stack`) and a paid SaaS subscription for a business function —
notes, workspace, passwords, streaming, video editing, team chat, PDFs, or
file transfer.

## Steps

1. **Count the actual users, not just the founder.** A solo founder or a
   two-person team can usually run entirely on the free/local tool. Once a
   team needs shared real-time access, permissions, or admin controls across
   many people, the free tool's local-first/offline design starts costing
   more in coordination overhead than the subscription would cost in cash.

2. **Check for a hard sync/collaboration requirement.** If the workflow needs
   real-time multi-user editing, cross-device sync without manual setup, or
   mobile apps with parity to desktop, verify the free tool actually covers
   it (some do — Joplin has sync options; most don't have real-time
   co-editing). Don't assume feature parity with the paid tool it replaces.

3. **Weigh data portability against support.** Free/open-source tools
   generally win on data portability (local files, open formats, no vendor
   lock-in) and lose on support (no vendor SLA, community forums instead of a
   support line). For anything client-facing or revenue-critical, missing
   support is a real cost — weigh it explicitly, don't ignore it.

4. **Flag security/compliance-sensitive data before defaulting to local.**
   Password vaults (KeePassXC) and file transfers (LocalSend) keep data on
   the user's own machine/network by design — that's a feature for
   sensitive data, but confirm the maintenance burden (who backs up the
   vault file, who patches the app) is actually owned by someone.

5. **Re-run this decision when the business's shape changes.** A tool chosen
   correctly for a solo founder can become the wrong choice once a team
   forms, or once compliance/support requirements appear (a client contract
   requiring an SLA, a hire who needs shared real-time access). Don't treat
   the initial choice as permanent — revisit it at each stage change,
   not only when something breaks.

6. **Default recommendation for pre-revenue/solo stage:** favor the free tool
   from `lean-software-stack` unless step 2 or 3 above surfaces a concrete
   blocker — cost control matters most before the business has revenue to
   validate spending against.
