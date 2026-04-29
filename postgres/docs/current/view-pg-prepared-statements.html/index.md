---
title: "PostgreSQL: Documentation: 18: 53.16. pg_prepared_statements"
source: "https://www.postgresql.org/docs/current/view-pg-prepared-statements.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-prepared-statements.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:45:26.183Z"
content_hash: "608538f7d6d60e45ade03027a2b125b535add8a3f768e0f5cc7f7a3c63b97d99"
menu_path: ["PostgreSQL: Documentation: 18: 53.16. pg_prepared_statements"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-policies.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.15.\u00a0pg_policies"}
nav_next: {"path": "postgres/docs/current/view-pg-prepared-xacts.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.17.\u00a0pg_prepared_xacts"}
---

The `pg_prepared_statements` view displays all the prepared statements that are available in the current session. See [PREPARE](https://www.postgresql.org/docs/current/sql-prepare.html "PREPARE") for more information about prepared statements.

`pg_prepared_statements` contains one row for each prepared statement. Rows are added to the view when a new prepared statement is created and removed when a prepared statement is released (for example, via the [`DEALLOCATE`](https://www.postgresql.org/docs/current/sql-deallocate.html "DEALLOCATE") command).

**Table 53.16. `pg_prepared_statements` Columns**

| 
Column Type

Description

 |
| --- |
| 

`name` `text`

The identifier of the prepared statement

 |
| 

`statement` `text`

The query string submitted by the client to create this prepared statement. For prepared statements created via SQL, this is the `PREPARE` statement submitted by the client. For prepared statements created via the frontend/backend protocol, this is the text of the prepared statement itself.

 |
| 

`prepare_time` `timestamptz`

The time at which the prepared statement was created

 |
| 

`parameter_types` `regtype[]`

The expected parameter types for the prepared statement in the form of an array of `regtype`. The OID corresponding to an element of this array can be obtained by casting the `regtype` value to `oid`.

 |
| 

`result_types` `regtype[]`

The types of the columns returned by the prepared statement in the form of an array of `regtype`. The OID corresponding to an element of this array can be obtained by casting the `regtype` value to `oid`. If the prepared statement does not provide a result (e.g., a DML statement), then this field will be null.

 |
| 

`from_sql` `bool`

`true` if the prepared statement was created via the `PREPARE` SQL command; `false` if the statement was prepared via the frontend/backend protocol

 |
| 

`generic_plans` `int8`

Number of times generic plan was chosen

 |
| 

`custom_plans` `int8`

Number of times custom plan was chosen

 |

The `pg_prepared_statements` view is read-only.
