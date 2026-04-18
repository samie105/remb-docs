---
title: "PostgreSQL: Documentation: 18: 35.41. routine_privileges"
source: "https://www.postgresql.org/docs/current/infoschema-routine-privileges.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-routine-privileges.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:33.742Z"
content_hash: "55aa184afe29732033e2acddefa7b61fa142d60e623962953cc8c93e78deeef8"
menu_path: ["PostgreSQL: Documentation: 18: 35.41. routine_privileges"]
section_path: []
nav_prev: {"path": "postgres/docs/current/functions-array.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.19.\u00a0Array Functions and Operators"}
nav_next: {"path": "postgres/docs/current/dynamic-trace.html/index.md", "title": "PostgreSQL: Documentation: 18: 27.5.\u00a0Dynamic Tracing"}
---

The view `routine_privileges` identifies all privileges granted on functions to a currently enabled role or by a currently enabled role. There is one row for each combination of function, grantor, and grantee.

**Table 35.39. `routine_privileges` Columns**

Column Type

Description

`grantor` `sql_identifier`

Name of the role that granted the privilege

`grantee` `sql_identifier`

Name of the role that the privilege was granted to

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

`privilege_type` `character_data`

Always `EXECUTE` (the only privilege type for functions)

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not


