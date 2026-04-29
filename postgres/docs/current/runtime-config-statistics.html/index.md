---
title: "PostgreSQL: Documentation: 18: 19.9. Run-time Statistics"
source: "https://www.postgresql.org/docs/current/runtime-config-statistics.html"
canonical_url: "https://www.postgresql.org/docs/current/runtime-config-statistics.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:09.394Z"
content_hash: "3db91bee6f493c51be630e7c5670985ed5ad858550146c73f41ad4ad67afeca6"
menu_path: ["PostgreSQL: Documentation: 18: 19.9. Run-time Statistics"]
section_path: []
nav_prev: {"path": "../runtime-config-short.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.18.\u00a0Short Options"}
nav_next: {"path": "../runtime-config-vacuum.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.10.\u00a0Vacuuming"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/runtime-config-statistics.html "PostgreSQL devel - 19.9. Run-time Statistics")

### 19.9.1. Cumulative Query and Index Statistics [#](#RUNTIME-CONFIG-CUMULATIVE-STATISTICS)

These parameters control the server-wide cumulative statistics system. When enabled, the data that is collected can be accessed via the `pg_stat` and `pg_statio` family of system views. Refer to [Chapter 27](https://www.postgresql.org/docs/current/monitoring.html "Chapter 27. Monitoring Database Activity") for more information.

`track_activities` (`boolean`) [#](#GUC-TRACK-ACTIVITIES)

Enables the collection of information on the currently executing command of each session, along with its identifier and the time when that command began execution. This parameter is on by default. Note that even when enabled, this information is only visible to superusers, roles with privileges of the `pg_read_all_stats` role and the user owning the sessions being reported on (including sessions belonging to a role they have the privileges of), so it should not represent a security risk. Only superusers and users with the appropriate `SET` privilege can change this setting.

`track_activity_query_size` (`integer`) [#](#GUC-TRACK-ACTIVITY-QUERY-SIZE)

Specifies the amount of memory reserved to store the text of the currently executing command for each active session, for the `pg_stat_activity`.`query` field. If this value is specified without units, it is taken as bytes. The default value is 1024 bytes. This parameter can only be set at server start.

`track_counts` (`boolean`) [#](#GUC-TRACK-COUNTS)

Enables collection of statistics on database activity. This parameter is on by default, because the autovacuum daemon needs the collected information. Only superusers and users with the appropriate `SET` privilege can change this setting.

`track_cost_delay_timing` (`boolean`) [#](#GUC-TRACK-COST-DELAY-TIMING)

Enables timing of cost-based vacuum delay (see [Section 19.10.2](https://www.postgresql.org/docs/current/runtime-config-vacuum.html#RUNTIME-CONFIG-RESOURCE-VACUUM-COST "19.10.2. Cost-based Vacuum Delay")). This parameter is off by default, as it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms. You can use the [pg\_test\_timing](https://www.postgresql.org/docs/current/pgtesttiming.html "pg_test_timing") tool to measure the overhead of timing on your system. Cost-based vacuum delay timing information is displayed in [`pg_stat_progress_vacuum`](https://www.postgresql.org/docs/current/progress-reporting.html#VACUUM-PROGRESS-REPORTING "27.4.5. VACUUM Progress Reporting"), [`pg_stat_progress_analyze`](https://www.postgresql.org/docs/current/progress-reporting.html#ANALYZE-PROGRESS-REPORTING "27.4.1. ANALYZE Progress Reporting"), in the output of [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") and [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") when the `VERBOSE` option is used, and by autovacuum for auto-vacuums and auto-analyzes when [log\_autovacuum\_min\_duration](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-AUTOVACUUM-MIN-DURATION) is set. Only superusers and users with the appropriate `SET` privilege can change this setting.

`track_io_timing` (`boolean`) [#](#GUC-TRACK-IO-TIMING)

Enables timing of database I/O waits. This parameter is off by default, as it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms. You can use the [pg\_test\_timing](https://www.postgresql.org/docs/current/pgtesttiming.html "pg_test_timing") tool to measure the overhead of timing on your system. I/O timing information is displayed in [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW "27.2.17. pg_stat_database"), [`pg_stat_io`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-IO-VIEW "27.2.13. pg_stat_io") (if `object` is not `wal`), in the output of the [`pg_stat_get_backend_io()`](https://www.postgresql.org/docs/current/monitoring-stats.html#PG-STAT-GET-BACKEND-IO) function (if `object` is not `wal`), in the output of [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html "EXPLAIN") when the `BUFFERS` option is used, in the output of [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") when the `VERBOSE` option is used, by autovacuum for auto-vacuums and auto-analyzes, when [log\_autovacuum\_min\_duration](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-AUTOVACUUM-MIN-DURATION) is set and by [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "F.32. pg_stat_statements — track statistics of SQL planning and execution"). Only superusers and users with the appropriate `SET` privilege can change this setting.

`track_wal_io_timing` (`boolean`) [#](#GUC-TRACK-WAL-IO-TIMING)

Enables timing of WAL I/O waits. This parameter is off by default, as it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms. You can use the pg\_test\_timing tool to measure the overhead of timing on your system. I/O timing information is displayed in [`pg_stat_io`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-IO-VIEW "27.2.13. pg_stat_io") for the `object` `wal` and in the output of the [`pg_stat_get_backend_io()`](https://www.postgresql.org/docs/current/monitoring-stats.html#PG-STAT-GET-BACKEND-IO) function for the `object` `wal`. Only superusers and users with the appropriate `SET` privilege can change this setting.

`track_functions` (`enum`) [#](#GUC-TRACK-FUNCTIONS)

Enables tracking of function call counts and time used. Specify `pl` to track only procedural-language functions, `all` to also track SQL and C language functions. The default is `none`, which disables function statistics tracking. Only superusers and users with the appropriate `SET` privilege can change this setting.

### Note

SQL-language functions that are simple enough to be “inlined” into the calling query will not be tracked, regardless of this setting.

`stats_fetch_consistency` (`enum`) [#](#GUC-STATS-FETCH-CONSISTENCY)

Determines the behavior when cumulative statistics are accessed multiple times within a transaction. When set to `none`, each access re-fetches counters from shared memory. When set to `cache`, the first access to statistics for an object caches those statistics until the end of the transaction unless `pg_stat_clear_snapshot()` is called. When set to `snapshot`, the first statistics access caches all statistics accessible in the current database, until the end of the transaction unless `pg_stat_clear_snapshot()` is called. Changing this parameter in a transaction discards the statistics snapshot. The default is `cache`.

### Note

`none` is most suitable for monitoring systems. If values are only accessed once, it is the most efficient. `cache` ensures repeat accesses yield the same values, which is important for queries involving e.g. self-joins. `snapshot` can be useful when interactively inspecting statistics, but has higher overhead, particularly if many database objects exist.

### 19.9.2. Statistics Monitoring [#](#RUNTIME-CONFIG-STATISTICS-MONITOR)

`compute_query_id` (`enum`) [#](#GUC-COMPUTE-QUERY-ID)

Enables in-core computation of a query identifier. Query identifiers can be displayed in the [`pg_stat_activity`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW "27.2.3. pg_stat_activity") view, using `EXPLAIN`, or emitted in the log if configured via the [log\_line\_prefix](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-LINE-PREFIX) parameter. The [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "F.32. pg_stat_statements — track statistics of SQL planning and execution") extension also requires a query identifier to be computed. Note that an external module can alternatively be used if the in-core query identifier computation method is not acceptable. In this case, in-core computation must be always disabled. Valid values are `off` (always disabled), `on` (always enabled), `auto`, which lets modules such as [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "F.32. pg_stat_statements — track statistics of SQL planning and execution") automatically enable it, and `regress` which has the same effect as `auto`, except that the query identifier is not shown in the `EXPLAIN` output in order to facilitate automated regression testing. The default is `auto`.

### Note

To ensure that only one query identifier is calculated and displayed, extensions that calculate query identifiers should throw an error if a query identifier has already been computed.

`log_statement_stats` (`boolean`)  
`log_parser_stats` (`boolean`)  
`log_planner_stats` (`boolean`)  
`log_executor_stats` (`boolean`) [#](#GUC-LOG-STATEMENT-STATS)

For each query, output performance statistics of the respective module to the server log. This is a crude profiling instrument, similar to the Unix `getrusage()` operating system facility. `log_statement_stats` reports total statement statistics, while the others report per-module statistics. `log_statement_stats` cannot be enabled together with any of the per-module options. All of these options are disabled by default. Only superusers and users with the appropriate `SET` privilege can change these settings.
