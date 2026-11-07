---
name: game-studio-chain-of-command
description: How the Claude Code Game Studios template organises one Claude Code session as a studio - three tiers (directors, department leads, specialists), engine sets for Godot, Unity and Unreal, the `modes.rigor` dial whose default `minimal` beat the 30-document build in the authors' own test, and the rule that anything the player sees must be launched and looked at. Use when planning a game project in Claude Code, deciding how much process to impose, or choosing which roles a task needs.
---

# Game studio chain of command

Source: the carousel's cards 01 and detail slides, checked against the README of `Donchitos/Claude-Code-Game-Studios` (MIT) on 7 November 2026. README counts: 49 agents, 74 skills, 14 path-scoped rules, 62 document templates.

## Three tiers

| Tier | Roles |
|---|---|
| 1. Directors | `creative-director`, `technical-director`, `producer` |
| 2. Department leads | `game-designer`, `lead-programmer`, `art-director`, `audio-director`, `narrative-director`, `qa-lead`, `release-manager`, `localization-lead` |
| 3. Specialists | `gameplay-programmer`, `engine-programmer`, `ai-programmer`, `network-programmer`, `tools-programmer`, `ui-programmer`, `systems-designer`, `level-designer`, `economy-designer`, `technical-artist`, `sound-designer`, `writer`, `world-builder`, `ux-designer`, `prototyper`, `performance-analyst`, `devops-engineer`, `analytics-engineer`, `security-engineer`, `qa-tester`, `accessibility-specialist`, `live-ops-designer`, `community-manager` |

Engine sets: Godot 4 (`godot-specialist` with GDScript, shaders, GDExtension), Unity (`unity-specialist` with DOTS/ECS, shaders and VFX, Addressables, UI Toolkit), Unreal Engine 5 (`unreal-specialist` with GAS, Blueprints, replication, UMG and CommonUI). The README says the three directors ask for Opus, one lead and fifteen specialists name Sonnet, and the rest inherit your session's model, so the tiers are seniority of role, not a billing plan.

## The process dial

`project.yaml` holds `modes.rigor`: `minimal` (default; no design docs required, solo review), `standard` (5 required design-doc sections, lean review) or `full` (all 8 sections, full director review). The README's own measurement: `minimal` wrote one document before the first line of game code; `standard` wrote 30 and took 58 minutes; reviewers and a playtest ranked the `standard` build last. It is the authors' test and has not been reproduced here. Start on `minimal` and raise it when the project grows.

## The evidence rule

A story that changes anything the player sees is not done until the game has been launched, observed and a screenshot kept in `production/qa/evidence/`. A parse check or passing test is not a run. This holds at every rigor level.

## Main commands (from the README)

`/start`, `/setup-engine`, `/brainstorm`, `/create-stories`, `/dev-story`, `/story-done`, `/gate-check`, `/settings`. On `minimal` the path is `/start`, `/setup-engine`, `/brainstorm` (a one-page brief), `/create-stories`, then `/dev-story` and `/story-done` in a loop.

## Use here

- To get the template: `git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game` on your own machine, open Claude Code in that folder, run `/start`. Do not clone it inside this repository; its `.claude/` folder would mix with ours.
- `/studio-plan [engine] [idea]` makes a lighter plan without installing anything, using the `game-studio-planner` agent.
- `unity-developer` is the existing single-agent option for Unity work.
