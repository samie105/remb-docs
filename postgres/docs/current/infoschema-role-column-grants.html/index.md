---
title: "PostgreSQL: Documentation: 18: 35.35. role_column_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-column-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-column-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:47:31.191Z"
content_hash: "0f49a75d32d8ceb55efd4e1444a7c1de62a02f1ebb94e7b21338219d2efab86d"
menu_path: ["PostgreSQL: Documentation: 18: 35.35. role_column_grants"]
section_path: []
content_language: "en"
---
The view `role_column_grants` identifies all privileges granted on columns where the grantor or grantee is a currently enabled role. Further information can be found under `column_privileges`. The only effective difference between this view and `column_privileges` is that this view omits columns that have been made accessible to the current user by way of a grant to `PUBLIC`.

**Table 35.33. `role_column_grants` Columns**

| 
Column Type

Description

 |
| --- |
| 

`grantor` `sql_identifier`

Name of the role that granted the privilege

 |
| 

`grantee` `sql_identifier`

Name of the role that the privilege was granted to

 |
| 

`table_catalog` `sql_identifier`

Name of the database that contains the table that contains the column (always the current database)

 |
| 

`table_schema` `sql_identifier`

Name of the schema that contains the table that contains the column

 |
| 

`table_name` `sql_identifier`

Name of the table that contains the column

 |
| 

`column_name` `sql_identifier`

Name of the column

 |
| 

`privilege_type` `character_data`

Type of the privilege: `SELECT`, `INSERT`, `UPDATE`, or `REFERENCES`

 |
| 

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not

 |
