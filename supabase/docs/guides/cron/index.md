---
title: "Cron"
source: "https://supabase.com/docs/guides/cron"
canonical_url: "https://supabase.com/docs/guides/cron"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:00.481Z"
content_hash: "cbbe4e1bfa2f00cdbca9b08f211738bb5613ed8ed58d2b651865cc7423d98332"
menu_path: ["Cron","Cron","Overview","Overview"]
section_path: ["Cron","Cron","Overview","Overview"]
---
# 

Cron

## 

Schedule Recurring Jobs with Cron Syntax in Postgres

* * *

Supabase Cron is a Postgres Module that simplifies scheduling recurring Jobs with cron syntax and monitoring Job runs inside Postgres.

Cron Jobs can be created via SQL or the [Integrations -> Cron](/dashboard/project/_/integrations) interface inside the Dashboard, and can run anywhere from every second to once a year depending on your use case.

![Manage cron jobs via the Dashboard](/docs/img/guides/cron/cron--light.jpg)

Every Job can run SQL snippets or database functions with zero network latency or make an HTTP request, such as invoking a Supabase Edge Function, with ease.

For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes.

## How does Cron work?[#](#how-does-cron-work)

Under the hood, Supabase Cron uses the [`pg_cron`](https://github.com/citusdata/pg_cron) Postgres database extension which is the scheduling and execution engine for your Jobs.

The extension creates a `cron` schema in your database and all Jobs are stored on the `cron.job` table. Every Job's run and its status is recorded on the `cron.job_run_details` table.

The Supabase Dashboard provides an interface for you to schedule Jobs and monitor Job runs. You can also do the same with SQL.

## Resources[#](#resources)

*   [`pg_cron` GitHub Repository](https://github.com/citusdata/pg_cron)
