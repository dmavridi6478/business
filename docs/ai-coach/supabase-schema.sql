-- AI Coach "FITNESS DATA" schema. The slide shows daily_metrics exactly; the other five tables are
-- reconstructed from a partly illegible image - review before running. Not applied to any project.
create table daily_metrics (id uuid primary key default gen_random_uuid(), date date unique not null,
  sleep_hours numeric, hrv integer, resting_hr integer, steps integer, weight numeric,
  recovery_score integer, created_at timestamp default now());
create table workouts (id uuid primary key default gen_random_uuid(), date date, title text, type text,
  duration_minutes integer, calories integer, notes text, created_at timestamp default now());
create table recovery (id uuid primary key default gen_random_uuid(), date date, sleep_score integer,
  hrv integer, resting_hr integer, stress_level integer, soreness text, notes text, created_at timestamp default now());
create table strength (id uuid primary key default gen_random_uuid(), date date, exercise text, weight numeric,
  reps integer, sets integer, volume numeric, is_pr boolean default false, created_at timestamp default now());
create table habits (id uuid primary key default gen_random_uuid(), date date, steps_target integer,
  steps_actual integer, water_target integer, water_actual integer, sleep_target numeric, sleep_actual numeric,
  training_done boolean, created_at timestamp default now());
create table coach_insights (id uuid primary key default gen_random_uuid(), date date, insight_type text,
  message text, priority text, action text, created_at timestamp default now());
-- Personal health data: enable row level security and add policies before exposing the anon key.
alter table daily_metrics enable row level security; alter table workouts enable row level security;
alter table recovery enable row level security; alter table strength enable row level security;
alter table habits enable row level security; alter table coach_insights enable row level security;
