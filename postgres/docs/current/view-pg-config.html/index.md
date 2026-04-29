---
title: "PostgreSQL: Documentation: 18: 53.6. pg_config"
source: "https://www.postgresql.org/docs/current/view-pg-config.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-config.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:50:37.257Z"
content_hash: "84f979f449f61e5603ee394a4ab4fcbb8ec37637bceca19f7eab3b3d9ef62db4"
menu_path: ["PostgreSQL: Documentation: 18: 53.6. pg_config"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/view-pg-backend-memory-contexts.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.5.\u00a0pg_backend_memory_contexts"}
nav_next: {"path": "postgres/docs/current/view-pg-cursors.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.7.\u00a0pg_cursors"}
---

The view `pg_config` describes the compile-time configuration parameters of the currently installed version of PostgreSQL. It is intended, for example, to be used by software packages that want to interface to PostgreSQL to facilitate finding the required header files and libraries. It provides the same basic information as the [pg\_config](https://www.postgresql.org/docs/current/app-pgconfig.html "pg_config") PostgreSQL client application.

By default, the `pg_config` view can be read only by superusers.

**Table 53.6. `pg_config` Columns**

| 
Column Type

Description

 |
| --- |
| 

`name` `text`

The parameter name

 |
| 

`setting` `text`

The parameter value

 |
