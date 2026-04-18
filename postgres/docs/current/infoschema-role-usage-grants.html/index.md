---
title: "PostgreSQL: Documentation: 18: 35.39. role_usage_grants"
source: "https://www.postgresql.org/docs/current/infoschema-role-usage-grants.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-role-usage-grants.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:47.954Z"
content_hash: "8e50e434565dcb93222cef45da75406078cc0a2ec6e0bc2a7f03f1b051a28896"
menu_path: ["PostgreSQL: Documentation: 18: 35.39. role_usage_grants"]
section_path: []
---
The view `role_usage_grants` identifies `USAGE` privileges granted on various kinds of objects where the grantor or grantee is a currently enabled role. Further information can be found under `usage_privileges`. The only effective difference between this view and `usage_privileges` is that this view omits objects that have been made accessible to the current user by way of a grant to `PUBLIC`.

**Table 35.37. `role_usage_grants` Columns**

Column Type

Description

`grantor` `sql_identifier`

The name of the role that granted the privilege

`grantee` `sql_identifier`

The name of the role that the privilege was granted to

`object_catalog` `sql_identifier`

Name of the database containing the object (always the current database)

`object_schema` `sql_identifier`

Name of the schema containing the object, if applicable, else an empty string

`object_name` `sql_identifier`

Name of the object

`object_type` `character_data`

`COLLATION` or `DOMAIN` or `FOREIGN DATA WRAPPER` or `FOREIGN SERVER` or `SEQUENCE`

`privilege_type` `character_data`

Always `USAGE`

`is_grantable` `yes_or_no`

`YES` if the privilege is grantable, `NO` if not
