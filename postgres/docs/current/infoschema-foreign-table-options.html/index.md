---
title: "PostgreSQL: Documentation: 18: 35.30. foreign_table_options"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-table-options.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-table-options.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:35.847Z"
content_hash: "8f400d02dc766b4e4821c8271e56aee18e110034d402786612b7d546e1c5f6ae"
menu_path: ["PostgreSQL: Documentation: 18: 35.30. foreign_table_options"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-createtstemplate.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TEXT SEARCH TEMPLATE"}
nav_next: {"path": "postgres/docs/current/app-pgresetxlog.html/index.md", "title": "PostgreSQL: Documentation: 18: O.4.\u00a0pg_resetxlog renamed to pg_resetwal"}
---

The view `foreign_table_options` contains all the options defined for foreign tables in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.28. `foreign_table_options` Columns**

Column Type

Description

`foreign_table_catalog` `sql_identifier`

Name of the database that contains the foreign table (always the current database)

`foreign_table_schema` `sql_identifier`

Name of the schema that contains the foreign table

`foreign_table_name` `sql_identifier`

Name of the foreign table

`option_name` `sql_identifier`

Name of an option

`option_value` `character_data`

Value of the option
