---
title: "PostgreSQL: Documentation: 18: 35.30. foreign_table_options"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-table-options.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-table-options.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:45:03.447Z"
content_hash: "89f6ac5d02f37a5e74daa2cc434efd1f06828f64fe72f13894f82172a4470da9"
menu_path: ["PostgreSQL: Documentation: 18: 35.30. foreign_table_options"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-foreign-servers.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.29.\u00a0foreign_servers"}
nav_next: {"path": "postgres/docs/current/infoschema-foreign-tables.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.31.\u00a0foreign_tables"}
---

The view `foreign_table_options` contains all the options defined for foreign tables in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.28. `foreign_table_options` Columns**

| 
Column Type

Description

 |
| --- |
| 

`foreign_table_catalog` `sql_identifier`

Name of the database that contains the foreign table (always the current database)

 |
| 

`foreign_table_schema` `sql_identifier`

Name of the schema that contains the foreign table

 |
| 

`foreign_table_name` `sql_identifier`

Name of the foreign table

 |
| 

`option_name` `sql_identifier`

Name of an option

 |
| 

`option_value` `character_data`

Value of the option

 |
