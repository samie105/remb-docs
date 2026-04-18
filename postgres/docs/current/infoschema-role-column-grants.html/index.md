---
title: "PostgreSQL: Documentation: 18: 35.35. role_column_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-column-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-column-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:27.340Z"
content_hash: "5c3c7a9bdd384c93fa1af936603386eb7c65e6b3aab4447f2fbec849d71dd434"
menu_path: ["PostgreSQL: Documentation: 18: 35.35. role_column_grants"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-alterindex.html/index.md", "title": "PostgreSQL: Documentation: 18: ALTER INDEX"}
nav_next: {"path": "postgres/docs/current/external-extensions.html/index.md", "title": "PostgreSQL: Documentation: 18: H.4.\u00a0Extensions"}
---

The view `role_column_grants` identifies all privileges granted on columns where the grantor or grantee is a currently enabled role. Further information can be found under `column_privileges`. The only effective difference between this view and `column_privileges` is that this view omits columns that have been made accessible to the current user by way of a grant to `PUBLIC`.

**Table 35.33. `role_column_grants` Columns**

Column Type

Description

`grantor` `sql_identifier`

Name of the role that granted the privilege

`grantee` `sql_identifier`

Name of the role that the privilege was granted to

`table_catalog` `sql_identifier`

Name of the database that contains the table that contains the column (always the current database)

`table_schema` `sql_identifier`

Name of the schema that contains the table that contains the column

`table_name` `sql_identifier`

Name of the table that contains the column

`column_name` `sql_identifier`

Name of the column

`privilege_type` `character_data`

Type of the privilege: `SELECT`, `INSERT`, `UPDATE`, or `REFERENCES`

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not

