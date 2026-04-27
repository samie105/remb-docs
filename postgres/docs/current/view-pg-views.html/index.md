---
title: "PostgreSQL: Documentation: 18: 53.37. pg_views"
source: "https://www.postgresql.org/docs/current/view-pg-views.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-views.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:30.490Z"
content_hash: "1793c4d20f8b8407ba132a74f1fbf425f69f48ab579c3307d04ce6317ec5ec6f"
menu_path: ["PostgreSQL: Documentation: 18: 53.37. pg_views"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-views.html "PostgreSQL devel - 53.37. pg_views")

The view `pg_views` provides access to useful information about each view in the database.

**Table 53.37. `pg_views` Columns**

| 
Column Type

Description

 |
| --- |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing view

 |
| 

`viewname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of view

 |
| 

`viewowner` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of view's owner

 |
| 

`definition` `text`

View definition (a reconstructed [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") query)

 |
