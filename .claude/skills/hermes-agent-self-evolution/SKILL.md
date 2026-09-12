---
name: hermes-agent-self-evolution
description: Research framework for automatic self-improvement of AI agents using DSPy + GEPA (Generative Evolutionary Prompt Adaptation) — reads execution traces to understand WHY failures occur, then proposes targeted prompt/tool improvements. ICLR 2026 Oral. Use when studying or implementing self-correcting agents that improve autonomously from failure traces rather than requiring human-written examples.
---

# Hermes Agent Self-Evolution (NousResearch)

A research-grade framework for agents that improve themselves by analysing execution traces — ICLR 2026 Oral.

## What it does

Traditional prompt engineering requires humans to study failures and hand-write better examples. Hermes automates this loop:

1. **Trace collection**: Captures full agent execution traces (inputs, tool calls, outputs, errors)
2. **Failure analysis (GEPA)**: Generative Evolutionary Prompt Adaptation — reads traces to understand root cause of failures
3. **Targeted improvement**: Proposes new prompts/few-shot examples that fix the observed failure modes
4. **Evaluation**: Runs the improved agent on a held-out set and keeps only improvements that generalise

## Key concepts

- **GEPA** (Generative Evolutionary Prompt Adaptation): trace-driven prompt evolution without human-labelled correction examples
- **DSPy integration**: Built on DSPy's optimizer infrastructure for structured prompt optimization
- **Execution trace format**: Structured JSON logs capturing every agent step for retrospective analysis

## When to reach for it

- Building self-improving agents and want a battle-tested trace-analysis scaffold
- Studying the ICLR 2026 paper's methodology to reproduce or extend it
- You want automatic prompt tuning that uses *failure reasons*, not just performance metrics

## Stack

Python 3.10+ · DSPy · Nous-Hermes model family (works with any OpenAI-compatible API)

## Clone

```bash
git clone https://github.com/NousResearch/hermes-agent-self-evolution
```

## Quickstart

```bash
pip install -e .
python generate_report.py --config datasets/your_config.yaml
```

See `PLAN.md` for the full experimental pipeline.

## Paper

ICLR 2026 Oral — "Hermes: Self-Evolving LLM Agents via Execution Trace Analysis"
