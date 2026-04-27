---
title: "PostgreSQL: Documentation: 18: 35.37. role_table_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-table-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-table-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:16.879Z"
content_hash: "064f451139b9bb7c4713fc5f215b2f21e6dcd26778eab85d52e9abebf5beae98"
menu_path: ["PostgreSQL: Documentation: 18: 35.37. role_table_grants"]
section_path: []
content_language: "en"
---
The view `role_table_grants` identifies all privileges granted on tables or views where the grantor or grantee is a currently enabled role. Further information can be found under `table_privileges`. The only effective difference between this view and `table_privileges` is that this view omits tables that have been made accessible to the current user by way of a grant to `PUBLIC`.

**Table 35.35. `role_table_grants` Columns**

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

Name of the database that contains the table (always the current database)

 |
| 

`table_schema` `sql_identifier`

Name of the schema that contains the table

 |
| 

`table_name` `sql_identifier`

Name of the table

 |
| 

`privilege_type` `character_data`

Type of the privilege: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES`, or `TRIGGER`

 |
| 

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not

 |
| 

`with_hierarchy` `yes_or_no`

In the SQL standard, `WITH HIERARCHY OPTION` is a separate (sub-)privilege allowing certain operations on table inheritance hierarchies. In PostgreSQL, this is included in the `SELECT` privilege, so this column shows `YES` if the privilege is `SELECT`, else `NO`.

 |
