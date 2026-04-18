---
title: "pg_stat_statements: Query Performance Monitoring"
source: "https://supabase.com/docs/guides/database/extensions/pg_stat_statements"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pg_stat_statements"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:55:52.355Z"
content_hash: "05cd40c4d57e2b29cabb202f50c7921dc1f5085fd460dc8244693ea447351909"
menu_path: ["Database","Database","Extensions","Extensions","pg_stat_statements: SQL Planning and Execution Statistics","pg_stat_statements: SQL Planning and Execution Statistics"]
section_path: ["Database","Database","Extensions","Extensions","pg_stat_statements: SQL Planning and Execution Statistics","pg_stat_statements: SQL Planning and Execution Statistics"]
---
# 

pg\_stat\_statements: Query Performance Monitoring

* * *

`pg_stat_statements` is a database extension that exposes a view, of the same name, to track statistics about SQL statements executed on the database. The following table shows some of the available statistics and metadata:

Column Name

Column Type

Description

`userid`

`oid` (references `pg_authid.oid`)

OID of user who executed the statement

`dbid`

`oid` (references `pg_database.oid`)

OID of database in which the statement was executed

`toplevel`

`bool`

True if the query was executed as a top-level statement (always true if pg\_stat\_statements.track is set to top)

`queryid`

`bigint`

Hash code to identify identical normalized queries.

`query`

`text`

Text of a representative statement

`plans`

`bigint`

Number of times the statement was planned (if pg\_stat\_statements.track\_planning is enabled, otherwise zero)

`total_plan_time`

`double precision`

Total time spent planning the statement, in milliseconds (if pg\_stat\_statements.track\_planning is enabled, otherwise zero)

`min_plan_time`

`double precision`

Minimum time spent planning the statement, in milliseconds (if pg\_stat\_statements.track\_planning is enabled, otherwise zero)

A full list of statistics is available in the [pg\_stat\_statements docs](https://www.postgresql.org/docs/current/pgstatstatements.html).

For more information on query optimization, check out the [query performance guide](/docs/guides/platform/performance#examining-query-performance).

## Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "pg\_stat\_statements" and enable the extension.

## Inspecting activity[#](#inspecting-activity)

A common use for `pg_stat_statements` is to track down expensive or slow queries. The `pg_stat_statements` view contains a row for each executed query with statistics inlined. For example, you can leverage the statistics to identify frequently executed and slow queries against a given table.

```
1select2	calls,3	mean_exec_time,4	max_exec_time,5	total_exec_time,6	stddev_exec_time,7	query8from9	pg_stat_statements10where11    calls > 50                   -- at least 50 calls12    and mean_exec_time > 2.0     -- averaging at least 2ms/call13    and total_exec_time > 60000  -- at least one minute total server time spent14    and query ilike '%user_in_organization%' -- filter to queries that touch the user_in_organization table15order by16	calls desc
```

From the results, we can make an informed decision about which queries to optimize or index.

## Resources[#](#resources)

*   Official [pg\_stat\_statements documentation](https://www.postgresql.org/docs/current/pgstatstatements.html)
