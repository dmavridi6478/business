---
name: b2b-sales-32-technical-validation
description: Map a buyer's technical, security and integration requirements to product evidence the user supplies, mark each met, partial, not met or unknown with its source, list risks and draft answers for the product or security owner to review. Use for security questionnaires and technical evaluations.
---

# 32. Technical Validation

Stage 5 of 7: Demo and evaluation. Skill 32 of 50 in the B2B sales set. The title comes from the Prosp "Claude Skills for B2B Sales" graphic; the method below is original to this repository (the graphic's own skill file was not obtained). Follow `b2b-sales-standard` for evidence tags, drafts-only and privacy rules.

## When to use

Use when the buyer has sent requirements or a questionnaire and the user has product documentation to answer from.

## Inputs

- Required: the buyer's technical requirements or questionnaire
- Required: the product documents the user confirms are current (architecture, security, integrations, compliance)
- Optional: the buyer's environment (systems, hosting, identity provider)
- Optional: previous completed questionnaires
- If a required input is missing, ask for it. Do not guess or fill it with an example.

## Method

1. List each requirement exactly as written.
2. For each, find the evidence in the supplied documents and cite the document and section. Mark met, partial, not met or unknown.
3. Do not claim a certification, control or integration that the documents do not state. Unknown stays unknown.
4. For partial and not met, state the gap and any workaround the documents support.
5. List technical risks to the deal and who on the buyer's side owns each.
6. Draft the answers in plain language. Label them "draft, needs review by the product or security owner before sending".
7. List questions to ask the buyer's technical team to clear unknowns.

## Output

Use these headings, in this order:

- `## Requirements`
- `## Evidence matrix`
- `## Gaps and risks`
- `## Questions for the buyer`
- `## Draft answers`
- `## Assumptions and what could be wrong`

## Quality checks

The output fails if any of these is false:

- Every "met" cites a document and section.
- No certification or control is claimed without a source.
- Unknowns are shown as unknown.
- The draft answers carry the review label.
- Every number not taken from the inputs carries a `[calc: ...]` or `[assumption]` tag (see `b2b-sales-standard`).
- Nothing is sent, posted, priced or signed; anything outward is labelled "draft, needs approval".

## Do not

- Do not answer from memory or from the competitor's documents.
- Do not state compliance as fact on a guess.
- Do not send answers without owner review.

## Related

- `b2b-sales-33-poc-scoper` (skill 33, POC Scoper)
- `b2b-sales-30-demo-script-builder` (skill 30, Demo Script Builder)
- `security-review`
