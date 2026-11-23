---
name: multi-agent-debate
description: Run a structured three-agent debate system (Researcher, Critic, Synthesizer) to produce higher-quality analysis than a single-pass response can achieve. Use when the question is important enough to warrant adversarial checking — a business decision, investment thesis, strategy choice, research question, or any claim where a wrong answer has real cost. Source: @ai_slacker "25 Powerful AI Skills, Agents & Automations You Can Build Today."
---

# Multi-Agent Debate System

Source: @ai_slacker "25 Powerful AI Skills, Agents & Automations You Can Build Today" (Advanced Tier, #20).

> Three agents (researcher, critic, synthesizer) produce higher-quality analysis than one.

## Why this beats a single prompt

A single Claude response optimizes for coherence and completeness — it surfaces the best case for whatever direction the initial framing implied. The debate system forces:
- The **Researcher** to build the strongest possible case
- The **Critic** to attack that case without holding back
- The **Synthesizer** to integrate both and produce a position the criticism couldn't break

The result is a stress-tested conclusion, not a confident-sounding first draft.

## When to use it

- High-stakes decisions (hiring, pricing, entering a market, pivoting)
- Investment or financial theses where a wrong call has cost
- Strategy questions where there are real competing approaches
- Any claim you're about to act on that deserves adversarial checking
- Research where you need to surface what you don't know, not just what you do

## The three-round protocol

Run each round as a separate Claude conversation or in sequence in one session.

---

### Round 1 — Researcher

```
You are the Researcher in a three-agent analysis system. Your job in this round is to build the strongest possible case FOR the following position, backed by the best available evidence and reasoning.

Topic / question: [STATE THE DECISION OR QUESTION]
Position to argue: [STATE THE AFFIRMATIVE POSITION]

Produce:
1. The 5 strongest arguments in favor of this position
2. The most compelling evidence or data points (cite sources if you know them; flag when you're estimating)
3. The key assumptions this position depends on
4. Examples where this position has worked in practice
5. Why the opposing view underestimates the strength of this position

Be rigorous and specific. Weak, vague arguments make the subsequent critique useless.
```

---

### Round 2 — Critic

```
You are the Critic in a three-agent analysis system. Your job is to attack the Researcher's case as forcefully and specifically as possible. You are NOT trying to balance — you are trying to break the argument.

Topic / question: [STATE THE DECISION OR QUESTION]

The Researcher argued:
[PASTE ROUND 1 OUTPUT HERE]

Your task:
1. Identify the 3 weakest points in the Researcher's case — explain specifically why they fail
2. Find the assumptions that, if wrong, collapse the entire argument
3. Present the strongest counterevidence or counterexamples
4. Name what the Researcher conveniently ignored or underweighted
5. State what a rational opponent would say if they had 60 seconds to rebut this case

Be adversarial, not balanced. Good criticism feels uncomfortable.
```

---

### Round 3 — Synthesizer

```
You are the Synthesizer in a three-agent analysis system. You have read both the Researcher's case and the Critic's attack. Your job is to produce the most accurate, actionable conclusion possible — one that survives the criticism.

Topic / question: [STATE THE DECISION OR QUESTION]

Researcher's case:
[PASTE ROUND 1 OUTPUT]

Critic's attack:
[PASTE ROUND 2 OUTPUT]

Produce:
1. Which of the Researcher's arguments survived the criticism (and why)
2. Which arguments the Critic broke (and what that means)
3. What the actual answer or recommendation is, given both rounds
4. The key conditions under which the answer changes
5. The 2–3 things you'd want to know before acting with high confidence
6. Your final verdict in one sentence

Be decisive. "It depends" without a condition is not a verdict.
```

## Shortcut: single-session version

If you don't want to run three separate conversations, use this combined prompt:

```
Run a three-round debate on the following question, playing all three roles in sequence.

Question: [STATE THE QUESTION]

Round 1 — Researcher: Build the strongest case FOR [POSITION A]
Round 2 — Critic: Attack that case without holding back
Round 3 — Synthesizer: Integrate both and deliver a verdict that survives the criticism

Label each round clearly. Be adversarial in Round 2 — don't soften the critique to seem balanced.
```

## Related skills

- **analytical-prompts**: 8 deeper thinking frameworks to apply before or after a debate round
- **business-decision-frameworks**: Structured decision tools that pair with the Synthesizer's output
- **ai-research-analyst**: Use for sourcing evidence in Round 1 before running the debate
- **competitor-profiling**: Run this debate on a competitor's strategy before deciding how to respond
