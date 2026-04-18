---
title: "PostgreSQL: Documentation: 18: 53.12. pg_indexes"
source: "https://www.postgresql.org/docs/current/view-pg-indexes.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-indexes.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:48.022Z"
content_hash: "4354504a03bba4383fe80048ba30b93daa155f5a2fbad3ee6c3e55190eec3c59"
menu_path: ["PostgreSQL: Documentation: 18: 53.12. pg_indexes"]
section_path: []
nav_prev: {"path": "postgres/docs/current/libpq-envars.html/index.md", "title": "PostgreSQL: Documentation: 18: 32.15.\u00a0Environment Variables"}
nav_next: {"path": "postgres/docs/current/sql-reassign-owned.html/index.md", "title": "PostgreSQL: Documentation: 18: REASSIGN OWNED"}
---

The view `pg_indexes` provides access to useful information about each index in the database.

**Table 53.12. `pg_indexes` Columns**

Column Type

Description

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table and index

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table the index is for

`indexname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of index

`tablespace` `name` (references [`pg_tablespace`](https://www.postgresql.org/docs/current/catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)

Name of tablespace containing index (null if default for database)

`indexdef` `text`

Index definition (a reconstructed [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html "CREATE INDEX") command)


