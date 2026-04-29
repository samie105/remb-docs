---
title: "PostgreSQL: Documentation: 18: 53.3. pg_available_extensions"
source: "https://www.postgresql.org/docs/current/view-pg-available-extensions.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-available-extensions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:51:14.563Z"
content_hash: "00973838007a66d48899cf334fe5a5c7cae9e9b7a75be640c78ee1f1e75a48c8"
menu_path: ["PostgreSQL: Documentation: 18: 53.3. pg_available_extensions"]
section_path: []
content_language: "en"
nav_prev: {"path": "../view-pg-available-extension-versions.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.4.\u00a0pg_available_extension_versions"}
nav_next: {"path": "../view-pg-backend-memory-contexts.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.5.\u00a0pg_backend_memory_contexts"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-available-extensions.html "PostgreSQL devel - 53.3. pg_available_extensions")

The `pg_available_extensions` view lists the extensions that are available for installation. See also the [`pg_extension`](https://www.postgresql.org/docs/current/catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.3. `pg_available_extensions` Columns**

| 
Column Type

Description

 |
| --- |
| 

`name` `name`

Extension name

 |
| 

`default_version` `text`

Name of default version, or `NULL` if none is specified

 |
| 

`installed_version` `text`

Currently installed version of the extension, or `NULL` if not installed

 |
| 

`comment` `text`

Comment string from the extension's control file

 |

The `pg_available_extensions` view is read-only.
