---
title: "PostgreSQL: Documentation: 18: 53.22. pg_rules"
source: "https://www.postgresql.org/docs/current/view-pg-rules.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-rules.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:42:48.558Z"
content_hash: "d92952bbff06c1d5cacbcc74e5fdd27706efdeb1ca8a250f2cde7f017d4ec044"
menu_path: ["PostgreSQL: Documentation: 18: 53.22. pg_rules"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-roles.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.21.\u00a0pg_roles"}
nav_next: {"path": "../view-pg-timezone-abbrevs.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.33.\u00a0pg_timezone_abbrevs"}
---

The view `pg_rules` provides access to useful information about query rewrite rules.

**Table 53.22. `pg_rules` Columns**

| 
Column Type

Description

 |
| --- |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table

 |
| 

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table the rule is for

 |
| 

`rulename` `name` (references [`pg_rewrite`](https://www.postgresql.org/docs/current/catalog-pg-rewrite.html "52.45. pg_rewrite").`rulename`)

Name of rule

 |
| 

`definition` `text`

Rule definition (a reconstructed creation command)

 |

The `pg_rules` view excludes the `ON SELECT` rules of views and materialized views; those can be seen in [`pg_views`](https://www.postgresql.org/docs/current/view-pg-views.html "53.37. pg_views") and [`pg_matviews`](https://www.postgresql.org/docs/current/view-pg-matviews.html "53.14. pg_matviews").
