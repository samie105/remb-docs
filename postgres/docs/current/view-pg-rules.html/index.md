---
title: "PostgreSQL: Documentation: 18: 53.22. pg_rules"
source: "https://www.postgresql.org/docs/current/view-pg-rules.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-rules.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:16.310Z"
content_hash: "1d9fe36b01d17a415915ed23829aa610691afbd5a6808c3c88deae853c4b2d8f"
menu_path: ["PostgreSQL: Documentation: 18: 53.22. pg_rules"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-dropview.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP VIEW"}
nav_next: {"path": "postgres/docs/current/sql-droptsparser.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP TEXT SEARCH PARSER"}
---

The view `pg_rules` provides access to useful information about query rewrite rules.

**Table 53.22. `pg_rules` Columns**

Column Type

Description

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table the rule is for

`rulename` `name` (references [`pg_rewrite`](https://www.postgresql.org/docs/current/catalog-pg-rewrite.html "52.45. pg_rewrite").`rulename`)

Name of rule

`definition` `text`

Rule definition (a reconstructed creation command)

The `pg_rules` view excludes the `ON SELECT` rules of views and materialized views; those can be seen in [`pg_views`](https://www.postgresql.org/docs/current/view-pg-views.html "53.37. pg_views") and [`pg_matviews`](https://www.postgresql.org/docs/current/view-pg-matviews.html "53.14. pg_matviews").


