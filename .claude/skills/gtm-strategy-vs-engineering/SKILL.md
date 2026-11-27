---
name: gtm-strategy-vs-engineering
description: Side-by-side comparison of GTM strategy (what, to whom, why us) and GTM engineering (how you reach them every week) across eleven dimensions, with the two copy formulas, the hand-off between them, and the limits and privacy checks the graphic omits (vendor-built tool list, lookalike-account targeting, case-study proof, outreach law). Use when deciding what to settle in strategy before building a data and outreach system, or when explaining the two roles.
---

# GTM strategy versus GTM engineering

Source: an infographic by Margaret Sikora, CEO of an outreach-tool vendor (Batch 124). The tools it lists for engineering (Clay, Zapier, Woodpecker, HubSpot) include the author's own product; read the tool column as examples, not a recommendation.

| Dimension | GTM strategy ("what") | GTM engineering ("how") |
|---|---|---|
| Core question | What do we offer, to whom and why us? | How do we reach them every week? |
| Key decisions | Offer, price, positioning, brand, channel | Data, integrations, automation, sending setup |
| Who to target first | Early customer profile: pays now, will refer you, reachable fast | List filters for that profile; the dream ICP comes later |
| Learn from current customers | Map how similar customers bought: where they came from, what convinced them, what they said on calls | Pull CRM sources and call transcripts, analyse them with Claude, rebuild that path for lookalike accounts |
| When it matters | From day one | After one motion works, then scale it |
| Proof | Which evidence buyers need: case studies, references, certifications | Each prospect sees a case study from their own industry; tag industry in the data tool and pull the matching story into email two |
| Example tools | Call recording and notes (Fireflies, Notion on the graphic) | Enrichment, workflow automation, outreach, CRM (Clay, Zapier, Woodpecker, HubSpot) |
| Easy to copy? | No: your customers' words are yours | Yes: anyone can rebuild your table |
| Where buyers judge you | Website, tone of voice, social presence | Every email and follow-up you send |
| Copy this formula | "We help [customer] get [outcome] with [offer]. Unlike [alternative], we [difference]." | "[Target criteria] → enrich and verify → send and follow up → log outcomes" |
| How they work together | Sets the direction | Runs it and sends results back |

## How to use the split
1. **Do strategy first, but small.** Write the positioning sentence and the early-customer profile before you build tables and sequences. Engineering a motion for an unclear offer only automates a miss.
2. **Engineer one motion.** One segment, one channel, one proof asset. Scale only after replies and meetings are real.
3. **Close the loop.** Engineering reports back (reply rate, meetings, cost per meeting, objections) and strategy changes the offer or the profile on that evidence.
4. **Keep the strategic parts human.** The customer's own words from calls are the asset; summarise them with a model but read a sample yourself.

## Checks the graphic omits
- **"Anyone can rebuild your table" cuts both ways.** If engineering is the easy-to-copy layer, the moat is proof, offer and speed of learning, not the stack.
- **Lookalike accounts from call transcripts.** Transcripts and CRM data contain personal data. Confirm you may process them for this purpose, tell participants what recordings are used for, and keep retention short. In the UK and EU this is regulated; take advice.
- **Industry-matched case studies need real consent and real results.** Do not stretch a case study from a different industry, and do not name a customer without permission.
- **Enrich and verify** costs money per record and still returns stale data. Sample 50 records by hand per segment before sending.
- **Sending setup is a compliance matter.** Domains, warm-up, opt-out and suppression lists, and per-country rules on cold email apply. [Likely] B2B cold email is not consent-free everywhere.
- **Tools are not the strategy.** Choose a stack after the motion is defined; two or three tools are enough to start.

Overlap in this library: `gtm-team-roles-revops-boundary` (who owns the CRM), `gtm-strategy`, `gtm-engineer-skills` (command), `tam-mapping-6-steps`, `icp-builder`, `list-architect`, `data-enrichment`, `trigger-based-outbound`, `give-first-cold-email`, `outbound-campaign-brief`. This skill is the one-page comparison and the hand-off rule.

Run with `/gtm-vs-engineering <your offer, target customer, current motion>`.
