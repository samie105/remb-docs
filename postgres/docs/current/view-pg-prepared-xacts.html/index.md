---
title: "PostgreSQL: Documentation: 18: 53.17. pg_prepared_xacts"
source: "https://www.postgresql.org/docs/current/view-pg-prepared-xacts.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-prepared-xacts.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:59.525Z"
content_hash: "f3941a3b11378a74fdbd87113cd86a0e3559c8830a96d96677cc091e7ba659e9"
menu_path: ["PostgreSQL: Documentation: 18: 53.17. pg_prepared_xacts"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-prepared-xacts.html "PostgreSQL devel - 53.17. pg_prepared_xacts")

The view `pg_prepared_xacts` displays information about transactions that are currently prepared for two-phase commit (see [PREPARE TRANSACTION](https://www.postgresql.org/docs/current/sql-prepare-transaction.html "PREPARE TRANSACTION") for details).

`pg_prepared_xacts` contains one row per prepared transaction. An entry is removed when the transaction is committed or rolled back.

**Table 53.17. `pg_prepared_xacts` Columns**

| 
Column Type

Description

 |
| --- |
| 

`transaction` `xid`

Numeric transaction identifier of the prepared transaction

 |
| 

`gid` `text`

Global transaction identifier that was assigned to the transaction

 |
| 

`prepared` `timestamptz`

Time at which the transaction was prepared for commit

 |
| 

`owner` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of the user that executed the transaction

 |
| 

`database` `name` (references [`pg_database`](https://www.postgresql.org/docs/current/catalog-pg-database.html "52.15. pg_database").`datname`)

Name of the database in which the transaction was executed

 |

When the `pg_prepared_xacts` view is accessed, the internal transaction manager data structures are momentarily locked, and a copy is made for the view to display. This ensures that the view produces a consistent set of results, while not blocking normal operations longer than necessary. Nonetheless there could be some impact on database performance if this view is frequently accessed.
