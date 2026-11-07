# Batch 112 prompts (files numbered 116)

Plain-text prompts from this batch. Nothing here installs, publishes or messages anyone.

## 1. Audit a vibe-coded app for five holes (read-only)

```
Audit this app for five issues, read-only, and do not change anything until I approve:
1. Secrets or API keys reachable from the frontend bundle or committed to git (including history).
2. Database tables or storage buckets readable without authentication (for Supabase: row level security off).
3. Admin or write endpoints that rely on hidden UI instead of a server-side role check.
4. AI or expensive endpoints with no per-user rate limit or spending cap.
5. A .env file or other secrets tracked in git, and whether .gitignore covers them.
For each: file and line, how an outsider could abuse it, the smallest fix, and how I verify the fix. Never print secret values; show only the first four characters. List what you could not check.
```

Command: `/vibe-check [path or stack]`.

## 2. Explain a mechanism as an interactive illustration (anatomy skill)

After you have read and installed the skill yourself (`npx skills add wheresryan22/anatomy -g -a claude-code`, Node 20.10 or later), type:

```
/anatomy explain how a token bucket rate limiter works, interactive
```

The skill's own limits: no charts, no people or exact maps, weaker on ideas with no moving parts.

## 3. Pick a free app for a job

```
Job: [what I need to do] on [Windows / macOS / Linux].
From Upscayl, Ventoy, Czkawka, Espanso, Syncthing, KDE Connect, HandBrake, Excalidraw, Penpot, Stirling PDF, RustDesk, pick one or two. For each give the licence, the platform as its README states it, the install route and the one risk. Tell me what to back up first. Do not install or run anything.
```

Command: `/free-app-pick [job]`.

## 4. Freelance first-client prompt (replaces "undercut the designers")

```
I am a [skill] freelancer. Help me find one narrow client type and one measurable outcome I can promise, then draft a three-line message to ten people of that type. Use AI tools to speed up delivery, not to compete on price. Ask me for proof I can show before you write any claim.
```
