---
title: "PostgreSQL: Documentation: 18: 35.44. routine_table_usage"
source: "https://www.postgresql.org/docs/current/infoschema-routine-table-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-routine-table-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:59.233Z"
content_hash: "dc689bd6cc68bb3ce519c9fcd90405308c36c964fd52c2d2231dc00f0f8f7a9e"
menu_path: ["PostgreSQL: Documentation: 18: 35.44. routine_table_usage"]
section_path: []
---
The view `routine_table_usage` is meant to identify all tables that are used by a function or procedure. This information is currently not tracked by PostgreSQL.

**Table 35.42. `routine_table_usage` Columns**

Column Type

Description

`specific_catalog` `sql_identifier`

Name of the database containing the function (always the current database)

`specific_schema` `sql_identifier`

Name of the schema containing the function

`specific_name` `sql_identifier`

The “specific name” of the function. See [Section 35.45](https://www.postgresql.org/docs/current/infoschema-routines.html "35.45. routines") for more information.

`routine_catalog` `sql_identifier`

Name of the database containing the function (always the current database)

`routine_schema` `sql_identifier`

Name of the schema containing the function

`routine_name` `sql_identifier`

Name of the function (might be duplicated in case of overloading)

`table_catalog` `sql_identifier`

Name of the database that contains the table that is used by the function (always the current database)

`table_schema` `sql_identifier`

Name of the schema that contains the table that is used by the function

`table_name` `sql_identifier`

Name of the table that is used by the function
