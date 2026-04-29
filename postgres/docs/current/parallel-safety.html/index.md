---
title: "PostgreSQL: Documentation: 18: 15.4. Parallel Safety"
source: "https://www.postgresql.org/docs/current/parallel-safety.html"
canonical_url: "https://www.postgresql.org/docs/current/parallel-safety.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:43.631Z"
content_hash: "7ca037e0b0aa003ab1e70f781150776a18e9f388b5c1358f1d3204d3162ea916"
menu_path: ["PostgreSQL: Documentation: 18: 15.4. Parallel Safety"]
section_path: []
nav_prev: {"path": "../parallel-plans.html/index.md", "title": "PostgreSQL: Documentation: 18: 15.3.\u00a0Parallel Plans"}
nav_next: {"path": "../parser-stage.html/index.md", "title": "PostgreSQL: Documentation: 18: 51.3.\u00a0The Parser Stage"}
---

The planner classifies operations involved in a query as either _parallel safe_, _parallel restricted_, or _parallel unsafe_. A parallel safe operation is one that does not conflict with the use of parallel query. A parallel restricted operation is one that cannot be performed in a parallel worker, but that can be performed in the leader while parallel query is in use. Therefore, parallel restricted operations can never occur below a `Gather` or `Gather Merge` node, but can occur elsewhere in a plan that contains such a node. A parallel unsafe operation is one that cannot be performed while parallel query is in use, not even in the leader. When a query contains anything that is parallel unsafe, parallel query is completely disabled for that query.

### 15.4.1. Parallel Labeling for Functions and Aggregates [#](#PARALLEL-LABELING)

The planner cannot automatically determine whether a user-defined function or aggregate is parallel safe, parallel restricted, or parallel unsafe, because this would require predicting every operation that the function could possibly perform. In general, this is equivalent to the Halting Problem and therefore impossible. Even for simple functions where it could conceivably be done, we do not try, since this would be expensive and error-prone. Instead, all user-defined functions are assumed to be parallel unsafe unless otherwise marked. When using [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION") or [ALTER FUNCTION](https://www.postgresql.org/docs/current/sql-alterfunction.html "ALTER FUNCTION"), markings can be set by specifying `PARALLEL SAFE`, `PARALLEL RESTRICTED`, or `PARALLEL UNSAFE` as appropriate. When using [CREATE AGGREGATE](https://www.postgresql.org/docs/current/sql-createaggregate.html "CREATE AGGREGATE"), the `PARALLEL` option can be specified with `SAFE`, `RESTRICTED`, or `UNSAFE` as the corresponding value.

Functions and aggregates must be marked `PARALLEL UNSAFE` if they write to the database, change the transaction state (other than by using a subtransaction for error recovery), access sequences, or make persistent changes to settings. Similarly, functions must be marked `PARALLEL RESTRICTED` if they access temporary tables, client connection state, cursors, prepared statements, or miscellaneous backend-local state that the system cannot synchronize across workers. For example, `setseed` and `random` are parallel restricted for this last reason.

In general, if a function is labeled as being safe when it is restricted or unsafe, or if it is labeled as being restricted when it is in fact unsafe, it may throw errors or produce wrong answers when used in a parallel query. C-language functions could in theory exhibit totally undefined behavior if mislabeled, since there is no way for the system to protect itself against arbitrary C code, but in most likely cases the result will be no worse than for any other function. If in doubt, it is probably best to label functions as `UNSAFE`.

If a function executed within a parallel worker acquires locks that are not held by the leader, for example by querying a table not referenced in the query, those locks will be released at worker exit, not end of transaction. If you write a function that does this, and this behavior difference is important to you, mark such functions as `PARALLEL RESTRICTED` to ensure that they execute only in the leader.

Note that the query planner does not consider deferring the evaluation of parallel-restricted functions or aggregates involved in the query in order to obtain a superior plan. So, for example, if a `WHERE` clause applied to a particular table is parallel restricted, the query planner will not consider performing a scan of that table in the parallel portion of a plan. In some cases, it would be possible (and perhaps even efficient) to include the scan of that table in the parallel portion of the query and defer the evaluation of the `WHERE` clause so that it happens above the `Gather` node. However, the planner does not do this.
