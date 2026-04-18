---
title: "PostgreSQL: Documentation: 18: 67.2. Transactions and Locking"
source: "https://www.postgresql.org/docs/current/xact-locking.html"
canonical_url: "https://www.postgresql.org/docs/current/xact-locking.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:14.624Z"
content_hash: "153be672168f2ed9f6bc8f9df3e9205acd33f1d4c08c3370cfe3a04bf4cfb445"
menu_path: ["PostgreSQL: Documentation: 18: 67.2. Transactions and Locking"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-do.html/index.md", "title": "PostgreSQL: Documentation: 18: DO"}
nav_next: {"path": "postgres/docs/current/view-pg-hba-file-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.10.\u00a0pg_hba_file_rules"}
---

The transaction IDs of currently executing transactions are shown in [`pg_locks`](https://www.postgresql.org/docs/current/view-pg-locks.html "53.13. pg_locks") in columns `virtualxid` and `transactionid`. Read-only transactions will have `virtualxid`s but NULL `transactionid`s, while both columns will be set in read-write transactions.

Some lock types wait on `virtualxid`, while other types wait on `transactionid`. Row-level read and write locks are recorded directly in the locked rows and can be inspected using the [pgrowlocks](https://www.postgresql.org/docs/current/pgrowlocks.html "F.31. pgrowlocks — show a table's row locking information") extension. Row-level read locks might also require the assignment of multixact IDs (`mxid`; see [Section 24.1.5.1](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-MULTIXACT-WRAPAROUND "24.1.5.1. Multixacts and Wraparound")).
