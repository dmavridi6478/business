---
name: build-ai-coach
description: Nine-step build guide for a personal AI Coach: Claude Project, athlete profile, wearable data via Intervals.icu, Obsidian second brain, weekly plan, adaptive daily plan, dashboard, Supabase, Telegram.
---

# Build your own AI Coach (@usamaakrm, 9 steps) - not medical advice
Scaffolds in this repo: `docs/ai-coach/FITNESS-SECOND-BRAIN/` (vault), `docs/ai-coach/supabase-schema.sql`, agent `ai-coach`, command `/ai-coach-daily`.

1. **Create the coach** - Claude > Projects > New Project, name `AI COACH`, Set project instructions:
   "You are my personal fitness coach. Use my workout, sleep, recovery and training data before giving advice. Track my goals, training history and progress. Every day tell me what I should do and why. Never invent missing health data."
2. **Teach it about you** - paste: "Interview me to build my athlete profile. Ask my goal, race date, current fitness, injuries, weekly training style. Ask one question at a time." Then: "Create my Athlete Profile.md" and save it to project knowledge.
3. **Connect your gear** - free account at intervals.icu > Settings > Connections: Garmin, Strava, Apple Health, WHOOP, Oura, COROS, Zwift, Withings, Hevy. (Claude has no intervals.icu connector in the registry; use exports or a script.)
4. **Second brain in Obsidian** - vault `FITNESS SECOND BRAIN`, folders profile/ workouts/ recovery/ strength/ habits/ weekly-reviews/. Add to project instructions: "Before coaching me, read the relevant notes from my Obsidian fitness Second Brain. Never treat every chat like a fresh conversation. Update the correct note when you learn something important." (The slide shows a "Connect Obsidian" menu; not verified to exist - upload the notes if it is absent.)
5. **Plan** - "Build me a simple weekly plan for strength, cardio, walking and recovery. Keep workouts under 60 minutes and realistic for a busy founder."
6. **Adapt** - "Every day check my sleep, recovery, soreness, work stress and available time. Then decide if I should train, train easy, walk or recover. Bad sleep? Lighter workout. Busy day? 20-minute version."
7. **Dashboard** - "Build a premium founder fitness dashboard. Style: minimal Apple + WHOOP, white background, clean typography, premium spacing, mobile responsive, no clutter. Top section: greeting, readiness score, today's plan. Metrics: sleep, HRV, resting HR, steps, training, recovery. 7-day and 30-day trend charts. COACH SAYS with three cards: what's working, what needs attention, what to do today. Add weekly workout calendar, recent workouts, strength PRs, habit streaks, weekly fitness score. Make it look like a premium $10,000 health dashboard, not a generic admin template."
8. **Supabase** - project `FITNESS DATA`; run `docs/ai-coach/supabase-schema.sql`; keep the service_role key secret, use the anon key plus row level security in the dashboard (`createClient` from `@supabase/supabase-js`).
9. **Telegram** - BotFather > /newbot, keep the token private, connect it to the coach, schedule a daily update.
Data flow: wearables > Supabase > Obsidian notes > Claude > dashboard > Telegram.
