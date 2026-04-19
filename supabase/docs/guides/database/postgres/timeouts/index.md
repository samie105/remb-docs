---
title: "Timeouts"
source: "https://supabase.com/docs/guides/database/postgres/timeouts"
canonical_url: "https://supabase.com/docs/guides/database/postgres/timeouts"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:47.329Z"
content_hash: "03492ac409f9427fe4065426eacbc4b8b4e261602be5817fbaf8fce140904d65"
menu_path: ["Database","Database","Debugging","Debugging","Timeouts","Timeouts"]
section_path: ["Database","Database","Debugging","Debugging","Timeouts","Timeouts"]
nav_prev: {"path": "supabase/docs/guides/database/postgres/setup-replication-external/index.md", "title": "Replicate to another Postgres database using Logical Replication"}
nav_next: {"path": "supabase/docs/guides/database/postgres/triggers/index.md", "title": "Postgres Triggers"}
---

# 

Timeouts

## 

Extend database timeouts to execute longer transactions

* * *

Dashboard and [Client](/docs/guides/api/rest/client-libs) queries have a max-configurable timeout of 60 seconds. For longer transactions, use [Supavisor or direct connections](/docs/guides/database/connecting-to-postgres#quick-summary).

## Change Postgres timeout[#](#change-postgres-timeout)

You can change the Postgres timeout at the:

1.  [Session level](#session-level)
2.  [Function level](#function-level)
3.  [Global level](#global-level)
4.  [Role level](#role-level)

### Session level[#](#session-level)

Session level settings persist only for the duration of the connection.

Set the session timeout by running:

```
1set statement_timeout = '10min';
```

Because it applies to sessions only, it can only be used with connections through Supavisor in session mode (port 5432) or a direct connection. It cannot be used in the Dashboard, with the Supabase Client API, nor with Supavisor in Transaction mode (port 6543).

This is most often used for single, long running, administrative tasks, such as creating an HSNW index. Once the setting is implemented, you can view it by executing:

```
1SHOW statement_timeout;
```

See the full guide on [changing session timeouts](https://github.com/orgs/supabase/discussions/21133).

### Function level[#](#function-level)

This works with the Database REST API when called from the Supabase client libraries:

```
1create or replace function myfunc()2returns void as $$3 select pg_sleep(3); -- simulating some long-running process4$$5language sql6set statement_timeout TO '4s'; -- set custom timeout
```

This is mostly for recurring functions that need a special exemption for runtimes.

### Role level[#](#role-level)

This sets the timeout for a specific role.

The default role timeouts are:

*   `anon`: 3s
*   `authenticated`: 8s
*   `service_role`: none (defaults to the `authenticator` role's 8s timeout if unset)
*   `postgres`: none (capped by default global timeout to be 2min)

Run the following query to change a role's timeout:

```
1alter role example_role set statement_timeout = '10min'; -- could also use seconds '10s'
```

If you are changing the timeout for the Supabase Client API calls, you will need to reload PostgREST to reflect the timeout changes by running the following script:

```
1NOTIFY pgrst, 'reload config';
```

Unlike global settings, the result cannot be checked with `SHOW statement_timeout`. Instead, run:

```
1select2  rolname,3  rolconfig4from pg_roles5where6  rolname in (7    'anon',8    'authenticated',9    'postgres',10    'service_role'11    -- ,<ANY CUSTOM ROLES>12  );
```

### Global level[#](#global-level)

This changes the statement timeout for all roles and sessions without an explicit timeout already set.

```
1alter database postgres set statement_timeout TO '4s';
```

Check if your changes took effect:

```
1show statement_timeout;
```

Although not necessary, if you are uncertain if a timeout has been applied, you can run a quick test:

```
1create or replace function myfunc()2returns void as $$3  select pg_sleep(601); -- simulating some long-running process4$$5language sql;
```

## Identifying timeouts[#](#identifying-timeouts)

The Supabase Dashboard contains tools to help you identify timed-out and long-running queries.

### Using the Logs Explorer[#](#using-the-logs-explorer)

Go to the [Logs Explorer](/dashboard/project/_/logs/explorer), and run the following query to identify timed-out events (`statement timeout`) and queries that successfully run for longer than 10 seconds (`duration`).

```
1select2  cast(postgres_logs.timestamp as datetime) as timestamp,3  event_message,4  parsed.error_severity,5  parsed.user_name,6  parsed.query,7  parsed.detail,8  parsed.hint,9  parsed.sql_state_code,10  parsed.backend_type11from12  postgres_logs13  cross join unnest(metadata) as metadata14  cross join unnest(metadata.parsed) as parsed15where16  regexp_contains(event_message, 'duration|statement timeout')17  -- (OPTIONAL) MODIFY OR REMOVE18  and parsed.user_name = 'authenticator' -- <--------CHANGE19order by timestamp desc20limit 100;
```

### Using the Query Performance page[#](#using-the-query-performance-page)

Go to the [Query Performance page](/dashboard/project/_/advisors/query-performance?preset=slowest_execution) and filter by relevant role and query speeds. This only identifies slow-running but successful queries. Unlike the Log Explorer, it does not show you timed-out queries.

### Understanding roles in logs[#](#understanding-roles-in-logs)

Each API server uses a designated user for connecting to the database:

Role

API/Tool

`supabase_admin`

Used by Realtime and for project configuration

`authenticator`

PostgREST

`supabase_auth_admin`

Auth

`supabase_storage_admin`

Storage

`supabase_replication_admin`

Synchronizes Read Replicas

`postgres`

Supabase Dashboard and External Tools (e.g., Prisma, SQLAlchemy, PSQL...)

Custom roles

External Tools (e.g., Prisma, SQLAlchemy, PSQL...)

Filter by the `parsed.user_name` field to only retrieve logs made by specific users:

```
1-- find events based on role/server2... query3where4  -- find events from the relevant role5  parsed.user_name = '<ROLE>'
```
