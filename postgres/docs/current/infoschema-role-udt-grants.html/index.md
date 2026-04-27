---
title: "PostgreSQL: Documentation: 18: 35.38. role_udt_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-udt-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-udt-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:21.042Z"
content_hash: "d67285407d2a27c36a31f6bdfac45478e1ff0591cd271e3dd73a8b2650dd3c6c"
menu_path: ["PostgreSQL: Documentation: 18: 35.38. role_udt_grants"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/infoschema-role-udt-grants.html "PostgreSQL devel - 35.38. role_udt_grants")

The view `role_udt_grants` is intended to identify `USAGE` privileges granted on user-defined types where the grantor or grantee is a currently enabled role. Further information can be found under `udt_privileges`. The only effective difference between this view and `udt_privileges` is that this view omits objects that have been made accessible to the current user by way of a grant to `PUBLIC`. Since data types do not have real privileges in PostgreSQL, but only an implicit grant to `PUBLIC`, this view is empty.

**Table 35.36. `role_udt_grants` Columns**

| 
Column Type

Description

 |
| --- |
| 

`grantor` `sql_identifier`

The name of the role that granted the privilege

 |
| 

`grantee` `sql_identifier`

The name of the role that the privilege was granted to

 |
| 

`udt_catalog` `sql_identifier`

Name of the database containing the type (always the current database)

 |
| 

`udt_schema` `sql_identifier`

Name of the schema containing the type

 |
| 

`udt_name` `sql_identifier`

Name of the type

 |
| 

`privilege_type` `character_data`

Always `TYPE USAGE`

 |
| 

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not

 |
