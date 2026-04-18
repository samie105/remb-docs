---
title: "PostgreSQL: Documentation: 18: 53.14. pg_matviews"
source: "https://www.postgresql.org/docs/current/view-pg-matviews.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-matviews.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:30.088Z"
content_hash: "8b30e59c4e7ee1cd13dbe13b5bd34f1f22b1233202467a82225ca3c19e74a928"
menu_path: ["PostgreSQL: Documentation: 18: 53.14. pg_matviews"]
section_path: []
nav_prev: {"path": "postgres/docs/current/locking-indexes.html/index.md", "title": "PostgreSQL: Documentation: 18: 13.7.\u00a0Locking and Indexes"}
nav_next: {"path": "postgres/docs/current/functions-info.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.27.\u00a0System Information Functions and Operators"}
---

The view `pg_matviews` provides access to useful information about each materialized view in the database.

**Table 53.14. `pg_matviews` Columns**

Column Type

Description

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing materialized view

`matviewname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of materialized view

`matviewowner` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of materialized view's owner

`tablespace` `name` (references [`pg_tablespace`](https://www.postgresql.org/docs/current/catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)

Name of tablespace containing materialized view (null if default for database)

`hasindexes` `bool`

True if materialized view has (or recently had) any indexes

`ispopulated` `bool`

True if materialized view is currently populated

`definition` `text`

Materialized view definition (a reconstructed [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") query)
