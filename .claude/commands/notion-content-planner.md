---
description: Add pre-approved content ideas to an existing Notion content planner (Claude content-workflow skill 8/9, socialblueprint.ca)
argument-hint: [content idea(s) to add, or "list" to review the current planner]
---

# /notion-content-planner

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 08 of 9.
This repo's `content-manager` agent already owns scheduling/pipeline-state
for the `/content-pipeline` workflow (Read/Write/TaskCreate/TaskUpdate/
TaskList) — use that agent when the job is managing this repo's own
content calendar. Use this command specifically when the destination is an
actual external Notion content planner database via the Notion connector.

## What it does

Takes an approved content idea and adds it to a Notion content-planner
database as a new row with the right properties — Title, Type, Status —
rather than dumping it in as unstructured text.

## Instructions

1. Confirm the Notion connector is available (check `ListConnectors` / the
   MCP tool list for `mcp__Notion__*` tools). If not connected, say so and
   stop — don't fabricate a database write.
2. If adding an idea: ask for (or infer) Title, Type (Infographic / Video
   / Image / Idea / Q&A roundup, matching the source's own status values),
   and Status (default `Idea` unless told otherwise).
3. Use `notion-search` to locate the content-planner database, then
   `notion-create-pages` (or the appropriate Notion MCP write tool) to add
   the row with those properties.
4. If asked to "list" or review, query the database and return it as a
   table: Title | Type | Status — sorted by Status (Posted → Draft →
   Idea → New) matching the source's own ordering.

## Plain-text prompt

```
Add this content idea to my Notion content planner: Title: [TITLE],
Type: [Infographic/Video/Image/Idea/Q&A], Status: Idea.
```

```
Show me my current Notion content planner as a table — Title, Type,
Status — sorted by status.
```
