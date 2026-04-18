---
title: "PostgreSQL: Documentation: 18: 35.32. key_column_usage"
source: "https://www.postgresql.org/docs/current/infoschema-key-column-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-key-column-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:07.014Z"
content_hash: "2108691f8aa55f97d65f6b9e5c0db70b4e571b20bf36f826b60ddb2c1513a5ce"
menu_path: ["PostgreSQL: Documentation: 18: 35.32. key_column_usage"]
section_path: []
nav_prev: {"path": "postgres/docs/current/recovery-config.html/index.md", "title": "PostgreSQL: Documentation: 18: O.1.\u00a0recovery.conf file merged into postgresql.conf"}
nav_next: {"path": "postgres/docs/current/rules-update.html/index.md", "title": "PostgreSQL: Documentation: 18: 39.4.\u00a0Rules on INSERT, UPDATE, and DELETE"}
---

The view `key_column_usage` identifies all columns in the current database that are restricted by some unique, primary key, or foreign key constraint. Check constraints are not included in this view. Only those columns are shown that the current user has access to, by way of being the owner or having some privilege.

**Table 35.30. `key_column_usage` Columns**

Column Type

Description

`constraint_catalog` `sql_identifier`

Name of the database that contains the constraint (always the current database)

`constraint_schema` `sql_identifier`

Name of the schema that contains the constraint

`constraint_name` `sql_identifier`

Name of the constraint

`table_catalog` `sql_identifier`

Name of the database that contains the table that contains the column that is restricted by this constraint (always the current database)

`table_schema` `sql_identifier`

Name of the schema that contains the table that contains the column that is restricted by this constraint

`table_name` `sql_identifier`

Name of the table that contains the column that is restricted by this constraint

`column_name` `sql_identifier`

Name of the column that is restricted by this constraint

`ordinal_position` `cardinal_number`

Ordinal position of the column within the constraint key (count starts at 1)

`position_in_unique_constraint` `cardinal_number`

For a foreign-key constraint, ordinal position of the referenced column within its unique constraint (count starts at 1); otherwise null

