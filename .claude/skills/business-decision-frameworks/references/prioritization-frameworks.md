# Prioritization Frameworks

*Authored directly for this repo — the parent skill's routing table pointed here, but no source content shipped with the install. This fills that gap, at the same "accurate but shallow scaffold" depth the parent skill's caveat describes — verify against primary sources before high-stakes use.*

## Choosing between frameworks

| Situation | Framework |
|---|---|
| Small backlog, need a fast yes/no/later cut | MoSCoW |
| Need a defensible numeric score across many initiatives | RICE |
| Setting/tracking measurable goals, not ranking a backlog | OKRs (not really a prioritization tool — see note below) |
| Deciding what makes users *delighted* vs. merely satisfied | Kano |
| Quick visual triage with a small group in a workshop | Value vs. Effort (2x2) |
| Continuous product discovery, connecting opportunities to solutions | Opportunity Solution Tree |

Don't apply all six to the same decision — they solve different problems and picking the wrong one is a common, correctable mistake (per the parent skill).

## MoSCoW

Buckets: **M**ust have, **S**hould have, **C**ould have, **W**on't have (this time).

- **Must have**: the release fails without it — not "important," but "non-negotiable."
- **Should have**: important but not vital; painful to cut, but the release still ships without it.
- **Could have**: desirable, small impact if cut.
- **Won't have**: explicitly out of scope for this round — stated to prevent scope creep, not forgotten.

**How to use it**: force every stakeholder to justify a "Must" with a consequence of not shipping it, not just enthusiasm. A common failure mode is everything ending up in "Must" — cap Must-haves at a hard percentage of the list (e.g. no more than 20%) to force real triage.

## RICE

Score = (Reach × Impact × Confidence) / Effort

| Factor | What it measures | Typical scale |
|---|---|---|
| Reach | How many people/customers this affects in a given period | Raw number (e.g. users/quarter) |
| Impact | How much it moves the needle per person affected | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| Confidence | How sure you are about the Reach/Impact estimates | 100% = high, 80% = medium, 50% = low |
| Effort | Person-months to build | Raw number |

**How to use it**: RICE's value is forcing explicit numbers instead of gut-feel ranking — the exact score matters less than making the team defend each input. Recalculate when a key assumption (reach estimate, effort estimate) turns out wrong; don't treat the first score as permanent.

## OKRs (as a prioritization signal, not a scoring method)

OKRs aren't a ranking framework — they're a goal-setting one. Use them for prioritization only indirectly: once Objectives and Key Results are set, an initiative's priority follows from how directly it moves a Key Result. An initiative that doesn't visibly move any current KR is a candidate to deprioritize, regardless of how good it sounds in isolation.

## Kano Model

Classifies features by the *shape* of the relationship between how much you invest and how satisfied users are:

| Category | Effect |
|---|---|
| Basic/threshold | Expected — absence causes dissatisfaction, presence doesn't create delight (e.g. "it doesn't crash") |
| Performance | Linear — more is better, less is worse (e.g. faster load times) |
| Delighters | Unexpected — absence isn't noticed, presence creates disproportionate satisfaction |
| Indifferent | Users don't care either way |
| Reverse | Presence actively annoys some users |

**How to use it**: rigorous Kano classification requires a structured survey (functional/dysfunctional question pairs per feature) — a team guessing at categories in a meeting is doing a lighter, less reliable version. Use it to catch the trap of over-investing in Basic features past the threshold where more investment stops paying off, and to protect budget for at least one Delighter per cycle.

## Value vs. Effort (2x2)

A fast visual triage: plot each initiative on a 2x2 of Value (low/high) vs. Effort (low/high).

| Quadrant | Label | Action |
|---|---|---|
| High value, low effort | Quick wins | Do first |
| High value, high effort | Major projects | Plan deliberately, don't rush |
| Low value, low effort | Fill-ins | Do if there's slack, not a priority |
| Low value, high effort | Time sinks | Cut or heavily question |

**How to use it**: fast for workshops with a group in the room, but the axes are subjective unless grounded in the same estimation discipline as RICE — use Value vs. Effort for quick triage, then RICE for the initiatives that need a defensible ranking beyond "it's in the top-right quadrant."

## Opportunity Solution Tree

A visual structure (associated with Teresa Torres — verify her actual published rules before formal use, per the parent skill's caveat) connecting:

```
Desired Outcome
├── Opportunity 1 (a customer need/pain/desire, from research)
│   ├── Solution A
│   └── Solution B
├── Opportunity 2
│   ├── Solution C
│   └── Solution D
```

**How to use it**: start from the outcome, surface opportunities from continuous customer research (not brainstorming), then generate multiple candidate solutions per opportunity before committing to build any one of them. The discipline is in resisting the jump straight from Outcome to Solution without surfacing the Opportunity layer — that's the step teams skip under deadline pressure, and it's the step that prevents building the wrong thing well.
