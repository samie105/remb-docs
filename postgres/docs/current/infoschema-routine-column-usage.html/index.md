---
title: "PostgreSQL: Documentation: 18: 35.40. routine_column_usage"
source: "https://www.postgresql.org/docs/current/infoschema-routine-column-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-routine-column-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:04.070Z"
content_hash: "783dcb7cc41c3b3e8daec0bbfdb11fe5750d11d078b8eaeb0c5c1bdc0e2b106f"
menu_path: ["PostgreSQL: Documentation: 18: 35.40. routine_column_usage"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-role-usage-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.39.\u00a0role_usage_grants"}
nav_next: {"path": "postgres/docs/current/infoschema-routine-privileges.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.41.\u00a0routine_privileges"}
---

The view `routine_column_usage` identifies all columns that are used by a function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) A column is only included if its table is owned by a currently enabled role.

**Table 35.38. `routine_column_usage` Columns**

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

`column_name` `sql_identifier`

Name of the column that is used by the function
