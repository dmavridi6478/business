---
description: Build an interactive HTML dashboard from a meeting's notes: decisions, actions by owner, timeline and risks
argument-hint: [meeting notes, transcript or Granola meeting reference]
---

Input: $ARGUMENTS

Use `dashboard-builder`, `dataviz` guidance and the Granola connector only if it is connected and I named the meeting.

1. Extract decisions, action items (owner, date, status), topics with time spent if known, and risks. Use only what the notes say.
2. Build one self-contained HTML file: summary strip, actions table filterable by owner, timeline, risks list. Readable on a phone, light and dark.
3. Publish it as an Artifact per the repository rule. Mark anything inferred.
