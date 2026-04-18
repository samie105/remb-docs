---
title: "PostgreSQL: Documentation: 18: 53.37. pg_views"
source: "https://www.postgresql.org/docs/current/view-pg-views.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-views.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:03.773Z"
content_hash: "650eab8ef7672817128351a8c11bd938d7ce4e4fe4a41ce636c2dff7cdfa4a3d"
menu_path: ["PostgreSQL: Documentation: 18: 53.37. pg_views"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-postgres.html/index.md", "title": "PostgreSQL: Documentation: 18: postgres"}
nav_next: {"path": "postgres/docs/current/sql-unlisten.html/index.md", "title": "PostgreSQL: Documentation: 18: UNLISTEN"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-views.html "PostgreSQL devel - 53.37. pg_views")

53.37. `pg_views`

[Prev](https://www.postgresql.org/docs/current/view-pg-user-mappings.html "53.36. pg_user_mappings") 

[Up](https://www.postgresql.org/docs/current/views.html "Chapter 53. System Views")

Chapter 53. System Views

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/view-pg-wait-events.html "53.38. pg_wait_events")

* * *

The view `pg_views` provides access to useful information about each view in the database.

**Table 53.37. `pg_views` Columns**

Column Type

Description

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing view

`viewname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of view

`viewowner` `name` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`rolname`)

Name of view's owner

`definition` `text`

View definition (a reconstructed [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") query)

  

* * *

[Prev](https://www.postgresql.org/docs/current/view-pg-user-mappings.html "53.36. pg_user_mappings") 

[Up](https://www.postgresql.org/docs/current/views.html "Chapter 53. System Views")

 [Next](https://www.postgresql.org/docs/current/view-pg-wait-events.html "53.38. pg_wait_events")

53.36. `pg_user_mappings` 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 53.38. `pg_wait_events`

