---
title: "PostgreSQL: Documentation: 18: 35.31. foreign_tables"
source: "https://www.postgresql.org/docs/current/infoschema-foreign-tables.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-foreign-tables.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:13.407Z"
content_hash: "9abcac0a96de659eaa2663b4e5cf9b5c442d7eaa5f2c8f3531b0e6088b88b17f"
menu_path: ["PostgreSQL: Documentation: 18: 35.31. foreign_tables"]
section_path: []
---
The view `foreign_tables` contains all foreign tables defined in the current database. Only those foreign tables are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.29. `foreign_tables` Columns**

Column Type

Description

`foreign_table_catalog` `sql_identifier`

Name of the database that the foreign table is defined in (always the current database)

`foreign_table_schema` `sql_identifier`

Name of the schema that contains the foreign table

`foreign_table_name` `sql_identifier`

Name of the foreign table

`foreign_server_catalog` `sql_identifier`

Name of the database that the foreign server is defined in (always the current database)

`foreign_server_name` `sql_identifier`

Name of the foreign server
