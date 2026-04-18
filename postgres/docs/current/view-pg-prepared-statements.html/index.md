---
title: "PostgreSQL: Documentation: 18: 53.16. pg_prepared_statements"
source: "https://www.postgresql.org/docs/current/view-pg-prepared-statements.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-prepared-statements.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:37.593Z"
content_hash: "fa71c07b1003187f0187d5ea2440df287c212368cfe4265ea7ab75ad49fea281"
menu_path: ["PostgreSQL: Documentation: 18: 53.16. pg_prepared_statements"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-information-schema-catalog-name.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.3.\u00a0information_schema_catalog_name"}
nav_next: {"path": "postgres/docs/current/sql-createsequence.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE SEQUENCE"}
---

The `pg_prepared_statements` view displays all the prepared statements that are available in the current session. See [PREPARE](https://www.postgresql.org/docs/current/sql-prepare.html "PREPARE") for more information about prepared statements.

`pg_prepared_statements` contains one row for each prepared statement. Rows are added to the view when a new prepared statement is created and removed when a prepared statement is released (for example, via the [`DEALLOCATE`](https://www.postgresql.org/docs/current/sql-deallocate.html "DEALLOCATE") command).

**Table 53.16. `pg_prepared_statements` Columns**

Column Type

Description

`name` `text`

The identifier of the prepared statement

`statement` `text`

The query string submitted by the client to create this prepared statement. For prepared statements created via SQL, this is the `PREPARE` statement submitted by the client. For prepared statements created via the frontend/backend protocol, this is the text of the prepared statement itself.

`prepare_time` `timestamptz`

The time at which the prepared statement was created

`parameter_types` `regtype[]`

The expected parameter types for the prepared statement in the form of an array of `regtype`. The OID corresponding to an element of this array can be obtained by casting the `regtype` value to `oid`.

`result_types` `regtype[]`

The types of the columns returned by the prepared statement in the form of an array of `regtype`. The OID corresponding to an element of this array can be obtained by casting the `regtype` value to `oid`. If the prepared statement does not provide a result (e.g., a DML statement), then this field will be null.

`from_sql` `bool`

`true` if the prepared statement was created via the `PREPARE` SQL command; `false` if the statement was prepared via the frontend/backend protocol

`generic_plans` `int8`

Number of times generic plan was chosen

`custom_plans` `int8`

Number of times custom plan was chosen

The `pg_prepared_statements` view is read-only.

