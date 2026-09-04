# Procedure: Research Synthesis (Knowledge Map → Literature Review → Gap Finder → Contradiction Detector → Methodology Auditor → Executive Brief)

## When this applies

Synthesizing a pile of sources — academic papers, market research, news
coverage, analyst reports — into something a person can actually act on.
Distinct from `agentic-researcher` (which goes out and *finds* sources):
this procedure assumes the sources are already in hand and need to be
turned into consensus, gaps, disagreements, and a decision-ready brief.

Run all six stages against the *same* source set, in order — each stage
builds on what the previous one surfaced. Don't skip stages or merge them;
each one is deliberately narrow so it catches something the others miss.

## The six prompts

Paste the sources once, then run these in sequence (each is a standalone
copy-paste prompt if you're running this by hand rather than via
`/research-synthesis`):

**1. Knowledge Map Builder** — orient in the field first, before synthesizing anything:
```
Based on the research I shared — build a knowledge map of this field.

Show me:
- The core concepts and how they connect
- The sub-fields and what each focuses on
- The key researchers or schools of thought
- How understanding has evolved over time
- Where the field is heading based on recent work

Present as a structured map I can use to orient myself quickly.
```

**2. Literature Review Engine** — synthesize across sources by theme, not paper-by-paper:
```
I am going to paste multiple research abstracts. After all of them —
synthesise into a structured literature review.

For each theme:
- What the consensus is across papers
- Where researchers disagree and why
- What methodology is most common
- What the most cited finding is

Do not summarise each paper individually. Synthesise across ALL of them.

Here are the papers: [paste all abstracts]
```

**3. Research Gap Finder** — find what's missing, not what's covered:
```
Read through all the research I shared. Find what is MISSING — not what
has been studied.

Tell me:
1. Questions researchers keep asking but never answering
2. Populations or contexts consistently understudied
3. Methodological limitations appearing across studies
4. Assumptions nobody has tested
5. The most promising unexplored direction

This is for identifying where original contribution is possible.
```

**4. Contradiction Detector** — surface disagreements instead of smoothing them over:
```
Analyse the research I shared and find where studies contradict each
other.

For each contradiction:
- What exactly is being disputed
- Which studies are on each side
- Why the contradiction might exist
- Different populations, methods, or definitions
- Which position has stronger evidence and why

Do not smooth over disagreements. Surface them clearly.
```

**5. Methodology Auditor** — check whether the evidence actually supports the claims:
```
Review the research methods used across all the papers I shared.

Tell me:
- What research designs are most common and why
- What the methodological weaknesses are
- What a stronger study design would look like
- What data nobody has collected yet
- Whether conclusions drawn are justified by the methods used

Be specific. Name the weakness. Name the paper.
```

**6. Executive Research Brief** — run this last, after the other five have done their work:
```
Synthesise everything into a one-page executive research brief.

Format:
- What this field is about in 2 sentences
- The 3 most important findings a decision-maker needs
- The 2 biggest uncertainties that remain
- What the practical implications are right now
- What we will likely know in 5 years that we don't today

Write for a smart non-expert who needs to make decisions based on this
research. Plain language. No jargon.
```

## Notes

- Stage 6's brief is the only stage meant to stand alone and be shared —
  the other five are working documents that feed it.
- Works on any topic, not just academic papers: market research, news
  coverage, competitor analysis, internal reports.
- In this repo, `/research-synthesis [sources]` runs all six stages in one
  invocation instead of pasting each prompt by hand.

## Source

Synthesized from an 8-slide "Claude Now Researches Like a Stanford PhD
Student" carousel (@claude.with.christelle).
