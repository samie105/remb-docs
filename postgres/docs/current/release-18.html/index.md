---
title: "PostgreSQL: Documentation: 18: E.4. Release 18"
source: "https://www.postgresql.org/docs/current/release-18.html"
canonical_url: "https://www.postgresql.org/docs/current/release-18.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:25.466Z"
content_hash: "bda02bd7974b7d1b8e15e082ac49ba3d6640e0170026a1184e234019fb51aa44"
menu_path: ["PostgreSQL: Documentation: 18: E.4. Release 18"]
section_path: []
nav_prev: {"path": "postgres/docs/current/release-18-3.html/index.md", "title": "PostgreSQL: Documentation: 18: E.1.\u00a0Release 18.3"}
nav_next: {"path": "postgres/docs/current/release-prior.html/index.md", "title": "PostgreSQL: Documentation: 18: E.5.\u00a0Prior Releases"}
---

*   Increase the logging granularity of server variable [log\_connections](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-CONNECTIONS) (Melanie Plageman) [§](https://postgr.es/c/9219093ca)
    
    This server variable was previously only boolean, which is still supported.
    
*   Add `log_connections` option to report the duration of connection stages (Melanie Plageman) [§](https://postgr.es/c/18cd15e70)
    
*   Add [log\_line\_prefix](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-LINE-PREFIX) escape `%L` to output the client IP address (Greg Sabino Mullane) [§](https://postgr.es/c/3516ea768)
    
*   Add server variable [log\_lock\_failures](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-LOCK-FAILURES) to log lock acquisition failures (Yuki Seino, Fujii Masao) [§](https://postgr.es/c/6d376c3b0) [§](https://postgr.es/c/73bdcfab3)
    
    Specifically it reports [`SELECT ... NOWAIT`](https://www.postgresql.org/docs/current/sql-select.html#SQL-FOR-UPDATE-SHARE "The Locking Clause") lock failures.
    
*   Modify [`pg_stat_all_tables`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW "27.2.19. pg_stat_all_tables") and its variants to report the time spent in [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM"), [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE"), and their [automatic](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM "24.1.6. The Autovacuum Daemon") variants (Sami Imseih) [§](https://postgr.es/c/30a6ed0ce)
    
    The new columns are `total_vacuum_time`, `total_autovacuum_time`, `total_analyze_time`, and `total_autoanalyze_time`.
    
*   Add delay time reporting to [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") and [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") (Bertrand Drouvot, Nathan Bossart) [§](https://postgr.es/c/bb8dff999) [§](https://postgr.es/c/7720082ae)
    
    This information appears in the server log, the system views [`pg_stat_progress_vacuum`](https://www.postgresql.org/docs/current/progress-reporting.html#VACUUM-PROGRESS-REPORTING "27.4.5. VACUUM Progress Reporting") and [`pg_stat_progress_analyze`](https://www.postgresql.org/docs/current/progress-reporting.html#PG-STAT-PROGRESS-ANALYZE-VIEW "Table 27.38. pg_stat_progress_analyze View"), and the output of [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") and [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") when in `VERBOSE` mode; tracking must be enabled with the server variable [track\_cost\_delay\_timing](postgres/docs/current/runtime-config-statistics.html/index.md#GUC-TRACK-COST-DELAY-TIMING).
    
*   Add WAL, CPU, and average read statistics output to `ANALYZE VERBOSE` (Anthonin Bonnefoy) [§](https://postgr.es/c/4c1b4cdb8) [§](https://postgr.es/c/bb7775234)
    
*   Add full WAL buffer count to `VACUUM`/`ANALYZE (VERBOSE)` and autovacuum log output (Bertrand Drouvot) [§](https://postgr.es/c/6a8a7ce47)
    
*   Add per-backend I/O statistics reporting (Bertrand Drouvot) [§](https://postgr.es/c/9aea73fc6) [§](https://postgr.es/c/3f1db99bf)
    
    The statistics are accessed via [`pg_stat_get_backend_io()`](https://www.postgresql.org/docs/current/monitoring-stats.html#PG-STAT-GET-BACKEND-IO). Per-backend I/O statistics can be cleared via [`pg_stat_reset_backend_stats()`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-FUNCS-TABLE "Table 27.36. Additional Statistics Functions").
    
*   Add [`pg_stat_io`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-IO-VIEW "27.2.13. pg_stat_io") columns to report I/O activity in bytes (Nazir Bilal Yavuz) [§](https://postgr.es/c/f92c854cf)
    
    The new columns are `read_bytes`, `write_bytes`, and `extend_bytes`. The `op_bytes` column, which always equaled [`BLCKSZ`](postgres/docs/current/runtime-config-preset.html/index.md#GUC-BLOCK-SIZE), has been removed.
    
*   Add WAL I/O activity rows to `pg_stat_io` (Nazir Bilal Yavuz, Bertrand Drouvot, Michael Paquier) [§](https://postgr.es/c/a051e71e2) [§](https://postgr.es/c/4538bd3f1) [§](https://postgr.es/c/7f7f324eb)
    
    This includes WAL receiver activity and a wait event for such writes.
    
*   Change server variable [track\_wal\_io\_timing](postgres/docs/current/runtime-config-statistics.html/index.md#GUC-TRACK-WAL-IO-TIMING) to control tracking WAL timing in `pg_stat_io` instead of [`pg_stat_wal`](https://www.postgresql.org/docs/current/monitoring-stats.html#PG-STAT-WAL-VIEW "Table 27.26. pg_stat_wal View") (Bertrand Drouvot) [§](https://postgr.es/c/6c349d83b)
    
*   Remove read/sync columns from `pg_stat_wal` (Bertrand Drouvot) [§](https://postgr.es/c/2421e9a51) [§](https://postgr.es/c/6c349d83b)
    
    This removes columns `wal_write`, `wal_sync`, `wal_write_time`, and `wal_sync_time`.
    
*   Add function [`pg_stat_get_backend_wal()`](https://www.postgresql.org/docs/current/monitoring-stats.html#PG-STAT-GET-BACKEND-WAL) to return per-backend WAL statistics (Bertrand Drouvot) [§](https://postgr.es/c/76def4cdd)
    
    Per-backend WAL statistics can be cleared via [`pg_stat_reset_backend_stats()`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-FUNCS-TABLE "Table 27.36. Additional Statistics Functions").
    
*   Add function [`pg_ls_summariesdir()`](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-GENFILE-TABLE "Table 9.108. Generic File Access Functions") to specifically list the contents of [`PGDATA`](https://www.postgresql.org/docs/current/storage-file-layout.html "66.1. Database File Layout")/[`pg_wal/summaries`](postgres/docs/current/runtime-config-wal.html/index.md#GUC-WAL-SUMMARY-KEEP-TIME) (Yushi Ogiwara) [§](https://postgr.es/c/4e1fad378)
    
*   Add column [`pg_stat_checkpointer`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-CHECKPOINTER-VIEW "27.2.15. pg_stat_checkpointer").`num_done` to report the number of completed checkpoints (Anton A. Melnikov) [§](https://postgr.es/c/559efce1d)
    
    Columns `num_timed` and `num_requested` count both completed and skipped checkpoints.
    
*   Add column `pg_stat_checkpointer`.`slru_written` to report SLRU buffers written (Nitin Jadhav) [§](https://postgr.es/c/17cc5f666)
    
    Also, modify the checkpoint server log message to report separate shared buffer and SLRU buffer values.
    
*   Add columns to [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW "27.2.17. pg_stat_database") to report parallel worker activity (Benoit Lobréau) [§](https://postgr.es/c/e7a9496de)
    
    The new columns are `parallel_workers_to_launch` and `parallel_workers_launched`.
    
*   Have [query id](postgres/docs/current/runtime-config-statistics.html/index.md#GUC-COMPUTE-QUERY-ID) computation of constant lists consider only the first and last constants (Dmitry Dolgov, Sami Imseih) [§](https://postgr.es/c/62d712ecf) [§](https://postgr.es/c/9fbd53dea) [§](https://postgr.es/c/c2da1a5d6)
    
    Jumbling is used by [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "F.32. pg_stat_statements — track statistics of SQL planning and execution").
    
*   Adjust query id computations to group together queries using the same relation name (Michael Paquier, Sami Imseih) [§](https://postgr.es/c/787514b30)
    
    This is true even if the tables in different schemas have different column names.
    
*   Add column [`pg_backend_memory_contexts`](https://www.postgresql.org/docs/current/view-pg-backend-memory-contexts.html "53.5. pg_backend_memory_contexts").`type` to report the type of memory context (David Rowley) [§](https://postgr.es/c/12227a1d5)
    
*   Add column `pg_backend_memory_contexts`.`path` to show memory context parents (Melih Mutlu) [§](https://postgr.es/c/32d3ed816)
