---
title: "PostgreSQL: Documentation: 18: 35.27. foreign_data_wrappers"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrappers.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrappers.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:23.943Z"
content_hash: "93d6a6b487e55dc44bd2e94a3107a8e8767ca2c3dc07f0cf33aab96f19ffcd8b"
menu_path: ["PostgreSQL: Documentation: 18: 35.27. foreign_data_wrappers"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-foreign-data-wrapper-options.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.26.\u00a0foreign_data_wrapper_options"}
nav_next: {"path": "postgres/docs/current/infoschema-foreign-server-options.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.28.\u00a0foreign_server_options"}
---

The view `foreign_data_wrappers` contains all foreign-data wrappers defined in the current database. Only those foreign-data wrappers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.25. `foreign_data_wrappers` Columns**

| 
Column Type

Description

 |
| --- |
| 

`foreign_data_wrapper_catalog` `sql_identifier`

Name of the database that contains the foreign-data wrapper (always the current database)

 |
| 

`foreign_data_wrapper_name` `sql_identifier`

Name of the foreign-data wrapper

 |
| 

`authorization_identifier` `sql_identifier`

Name of the owner of the foreign server

 |
| 

`library_name` `character_data`

File name of the library that implementing this foreign-data wrapper

 |
| 

`foreign_data_wrapper_language` `character_data`

Language used to implement this foreign-data wrapper

 |
