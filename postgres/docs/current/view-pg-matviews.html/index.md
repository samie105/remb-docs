---
title: "PostgreSQL: Documentation: 18: 53.14. pg_matviews"
source: "https://www.postgresql.org/docs/current/view-pg-matviews.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-matviews.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:43.663Z"
content_hash: "6806127641b72a9223f2c2de18d71e13d6d63d85295a731c8f8cf60cc55fecd6"
menu_path: ["PostgreSQL: Documentation: 18: 53.14. pg_matviews"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-locks.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.13.\u00a0pg_locks"}
nav_next: {"path": "../view-pg-policies.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.15.\u00a0pg_policies"}
---

The view `pg_matviews` provides access to useful information about each materialized view in the database.

**Table 53.14. `pg_matviews` Columns**

| 
Column Type

Description

 |
| --- |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing materialized view

 |
| 

`matviewname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of materialized view

 |
| 

`matviewowner` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of materialized view's owner

 |
| 

`tablespace` `name` (references [`pg_tablespace`](https://www.postgresql.org/docs/current/catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)

Name of tablespace containing materialized view (null if default for database)

 |
| 

`hasindexes` `bool`

True if materialized view has (or recently had) any indexes

 |
| 

`ispopulated` `bool`

True if materialized view is currently populated

 |
| 

`definition` `text`

Materialized view definition (a reconstructed [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") query)

 |
