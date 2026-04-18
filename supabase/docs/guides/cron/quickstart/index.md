---
title: "Quickstart"
source: "https://supabase.com/docs/guides/cron/quickstart"
canonical_url: "https://supabase.com/docs/guides/cron/quickstart"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:42.215Z"
content_hash: "b1ef437bdfe5b3bc935bce74f8faeea496fdaac662a8a615b017fbf537474257"
menu_path: ["Cron","Cron","Getting Started","Getting Started","Quickstart","Quickstart"]
section_path: ["Cron","Cron","Getting Started","Getting Started","Quickstart","Quickstart"]
nav_prev: {"path": "supabase/docs/guides/cron/install/index.md", "title": "Install"}
nav_next: {"path": "supabase/docs/guides/database/beekeeper-studio/index.md", "title": "Connecting with Beekeeper Studio"}
---

# 

Quickstart

* * *

Job names are case sensitive and cannot be edited once created.

Attempting to create a second Job with the same name (and case) will overwrite the first Job.

## Schedule a job[#](#schedule-a-job)

1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section to schedule your first Job.
2.  Click on `Create job` button or navigate to the new Cron Job form [here](/dashboard/project/_/integrations/cron/jobs?new=true).
3.  Name your Cron Job.
4.  Choose a schedule for your Job by inputting cron syntax (refer to the syntax chart in the form) or natural language.
5.  Input SQL snippet or select a Database function, HTTP request, or Supabase Edge Function.

You can input seconds for your Job schedule interval as long as you're on Postgres version 15.1.1.61 or later.

## Edit a job[#](#edit-a-job)

1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to edit.
2.  Click on the three vertical dots menu on the right side of the Job and click `Edit cron job`.
3.  Make your changes and then click `Save cron job`.

## Activate/Deactivate a job[#](#activatedeactivate-a-job)

1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to unschedule.
2.  Toggle the `Active`/`Inactive` switch next to Job name.

## Unschedule a job[#](#unschedule-a-job)

1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to delete.
2.  Click on the three vertical dots menu on the right side of the Job and click `Delete cron job`.
3.  Confirm deletion by entering the Job name.

## Inspecting job runs[#](#inspecting-job-runs)

1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you want to see the runs of.
2.  Click on the `History` button next to the Job name.

## Examples[#](#examples)

### Delete data every week[#](#delete-data-every-week)

Delete old data every Saturday at 3:30AM (GMT):

```
1select cron.schedule (2  'saturday-cleanup', -- name of the cron job3  '30 3 * * 6', -- Saturday at 3:30AM (GMT)4  $$ delete from events where event_time < now() - interval '1 week' $$5);
```

### Run a vacuum every day[#](#run-a-vacuum-every-day)

Vacuum every day at 3:00AM (GMT):

```
1select cron.schedule('nightly-vacuum', '0 3 * * *', 'VACUUM');
```

### Call a database function every 5 minutes[#](#call-a-database-function-every-5-minutes)

Create a [`hello_world()`](/docs/guides/database/functions?language=sql#simple-functions) database function and then call it every 5 minutes:

```
1select cron.schedule('call-db-function', '*/5 * * * *', 'SELECT hello_world()');
```

### Call a database stored procedure[#](#call-a-database-stored-procedure)

To use a stored procedure, you can call it like this:

```
1select cron.schedule('call-db-procedure', '*/5 * * * *', 'CALL my_procedure()');
```

### Invoke Supabase Edge Function every 30 seconds[#](#invoke-supabase-edge-function-every-30-seconds)

Make a POST request to a Supabase Edge Function every 30 seconds:

```
1select2  cron.schedule(3    'invoke-function-every-half-minute',4    '30 seconds',5    $$6    select7      net.http_post(8          url:='https://project-ref.supabase.co/functions/v1/function-name',9          headers:=jsonb_build_object('Content-Type','application/json', 'Authorization', 'Bearer ' || 'YOUR_ANON_KEY'),10          body:=jsonb_build_object('time', now() ),11          timeout_milliseconds:=500012      ) as request_id;13    $$14  );
```

This requires the [`pg_net` extension](/docs/guides/database/extensions/pg_net) to be enabled.

## Caution: Scheduling system maintenance[#](#caution-scheduling-system-maintenance)

Be extremely careful when setting up Jobs for system maintenance tasks as they can have unintended consequences.

For instance, scheduling a command to terminate idle connections with `pg_terminate_backend(pid)` can disrupt critical background processes like nightly backups. Often, there is an existing Postgres setting, such as `idle_session_timeout`, that can perform these common maintenance tasks without the risk.

Reach out to [Supabase Support](/support) if you're unsure if that applies to your use case.

