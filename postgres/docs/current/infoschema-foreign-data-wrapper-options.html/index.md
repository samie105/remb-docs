---
title: "PostgreSQL: Documentation: 18: 35.26. foreign_data_wrapper_options"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrapper-options.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-data-wrapper-options.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:09.503Z"
content_hash: "cca9f7332757b60cad1ed62ee335a7c84f1178403c6176aa282dc531481ff8ee"
menu_path: ["PostgreSQL: Documentation: 18: 35.26. foreign_data_wrapper_options"]
section_path: []
content_language: "en"
nav_prev: {"path": "../infoschema-enabled-roles.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.25.\u00a0enabled_roles"}
nav_next: {"path": "../infoschema-foreign-data-wrappers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.27.\u00a0foreign_data_wrappers"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/infoschema-foreign-data-wrapper-options.html "PostgreSQL devel - 35.26. foreign_data_wrapper_options")

The view `foreign_data_wrapper_options` contains all the options defined for foreign-data wrappers in the current database. Only those foreign-data wrappers are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.24. `foreign_data_wrapper_options` Columns**

| 
Column Type

Description

 |
| --- |
| 

`foreign_data_wrapper_catalog` `sql_identifier`

Name of the database that the foreign-data wrapper is defined in (always the current database)

 |
| 

`foreign_data_wrapper_name` `sql_identifier`

Name of the foreign-data wrapper

 |
| 

`option_name` `sql_identifier`

Name of an option

 |
| 

`option_value` `character_data`

Value of the option

 |
