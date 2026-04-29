---
title: "PostgreSQL: Documentation: 18: 53.12. pg_indexes"
source: "https://www.postgresql.org/docs/current/view-pg-indexes.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-indexes.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:29.741Z"
content_hash: "bd4700dd8a87f02757b19a07a09b1e43cd2085f99e57d6e68ceda6b5154caad4"
menu_path: ["PostgreSQL: Documentation: 18: 53.12. pg_indexes"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-ident-file-mappings.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.11.\u00a0pg_ident_file_mappings"}
nav_next: {"path": "../view-pg-locks.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.13.\u00a0pg_locks"}
---

The view `pg_indexes` provides access to useful information about each index in the database.

**Table 53.12. `pg_indexes` Columns**

| 
Column Type

Description

 |
| --- |
| 

`schemaname` `name` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`nspname`)

Name of schema containing table and index

 |
| 

`tablename` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of table the index is for

 |
| 

`indexname` `name` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`relname`)

Name of index

 |
| 

`tablespace` `name` (references [`pg_tablespace`](https://www.postgresql.org/docs/current/catalog-pg-tablespace.html "52.56. pg_tablespace").`spcname`)

Name of tablespace containing index (null if default for database)

 |
| 

`indexdef` `text`

Index definition (a reconstructed [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html "CREATE INDEX") command)

 |
