---
title: "PostgreSQL: Documentation: 18: 35.27. foreign_data_wrappers"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrappers.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrappers.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:38.574Z"
content_hash: "e6400a9f618c85381e8943e5c7b15e40289c522db3286e88c454c23a050b8b9a"
menu_path: ["PostgreSQL: Documentation: 18: 35.27. foreign_data_wrappers"]
section_path: []
nav_prev: {"path": "postgres/docs/current/textsearch-limitations.html/index.md", "title": "PostgreSQL: Documentation: 18: 12.11.\u00a0Limitations"}
nav_next: {"path": "postgres/docs/current/wal-configuration.html/index.md", "title": "PostgreSQL: Documentation: 18: 28.5.\u00a0WAL Configuration"}
---

The view `foreign_data_wrappers` contains all foreign-data wrappers defined in the current database. Only those foreign-data wrappers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.25. `foreign_data_wrappers` Columns**

Column Type

Description

`foreign_data_wrapper_catalog` `sql_identifier`

Name of the database that contains the foreign-data wrapper (always the current database)

`foreign_data_wrapper_name` `sql_identifier`

Name of the foreign-data wrapper

`authorization_identifier` `sql_identifier`

Name of the owner of the foreign server

`library_name` `character_data`

File name of the library that implementing this foreign-data wrapper

`foreign_data_wrapper_language` `character_data`

Language used to implement this foreign-data wrapper

