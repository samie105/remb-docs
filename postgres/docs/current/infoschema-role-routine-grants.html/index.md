---
title: "PostgreSQL: Documentation: 18: 35.36. role_routine_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-routine-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-routine-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:57.252Z"
content_hash: "f20233f688d7d47e076ebf6d9605f50f3b21efa72cdc55a5b824d476a8020cd9"
menu_path: ["PostgreSQL: Documentation: 18: 35.36. role_routine_grants"]
section_path: []
nav_prev: {"path": "postgres/docs/current/lo-examplesect.html/index.md", "title": "PostgreSQL: Documentation: 18: 33.5.\u00a0Example Program"}
nav_next: {"path": "postgres/docs/current/sql-commit.html/index.md", "title": "PostgreSQL: Documentation: 18: COMMIT"}
---

The view `role_routine_grants` identifies all privileges granted on functions where the grantor or grantee is a currently enabled role. Further information can be found under `routine_privileges`. The only effective difference between this view and `routine_privileges` is that this view omits functions that have been made accessible to the current user by way of a grant to `PUBLIC`.

**Table 35.34. `role_routine_grants` Columns**

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


