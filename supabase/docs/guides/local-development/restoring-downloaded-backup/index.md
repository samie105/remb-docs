---
title: "Restoring a downloaded backup locally"
source: "https://supabase.com/docs/guides/local-development/restoring-downloaded-backup"
canonical_url: "https://supabase.com/docs/guides/local-development/restoring-downloaded-backup"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:46.420Z"
content_hash: "11f328c1016c7f27377b4fc7c9a921d52ce663362830660a03265647d8178713"
menu_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Restoring downloaded backup","Restoring downloaded backup"]
section_path: ["Local Dev / CLI","Local Dev / CLI","Local development","Local development","Restoring downloaded backup","Restoring downloaded backup"]
nav_prev: {"path": "supabase/docs/guides/local-development/overview/index.md", "title": "Local development with schema migrations"}
nav_next: {"path": "supabase/docs/guides/local-development/seeding-your-database/index.md", "title": "Seeding your database"}
---

# 

Restoring a downloaded backup locally

## 

Restore a backup of a remote database on a local instance to inspect and extract data

* * *

If your paused project has exceeded its [restoring time limit](../../platform/upgrading/index.md#time-limits), you can download a backup from the dashboard and restore it to your local development environment. This might be useful for inspecting and extracting data from your paused project.

If you want to restore your backup to a hosted Supabase project, follow the [Migrating within Supabase guide](../../platform/migrating-within-supabase/index.md) instead.

## Downloading your backup[#](#downloading-your-backup)

First, download your project's backup file from dashboard and identify its backup image version (following the `PG:` prefix):

![Project Paused: 90 Days Remaining](/docs/img/guides/platform/paused-dl-image-version.png)

## Restoring your backup[#](#restoring-your-backup)

Given Postgres version `15.6.1.115`, start Postgres locally with `db_cluster.backup` being the path to your backup file.

```
1supabase init2echo '15.6.1.115' > supabase/.temp/postgres-version3supabase db start --from-backup db_cluster.backup
```

Note that the earliest Supabase Postgres version that supports a local restore is `15.1.0.55`. If your hosted project was running on earlier versions, you will likely run into errors during restore. Before submitting any support ticket, make sure you have attached the error logs from `supabase_db_*` docker container.

Once your local database starts up successfully, you can connect using psql to verify that all your data is restored.

```
1psql 'postgresql://postgres:postgres@localhost:54322/postgres'
```

If you want to use other services like Auth, Storage, and Studio dashboard together with your restored database, restart the local development stack.

```
1supabase stop2supabase start
```

A Postgres database started with Supabase CLI is not production ready and should not be used outside of local development.
