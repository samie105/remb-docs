---
title: "PostgreSQL: Documentation: 18: 35.43. routine_sequence_usage"
source: "https://www.postgresql.org/docs/current/infoschema-routine-sequence-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-routine-sequence-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:34.493Z"
content_hash: "b2d977e6c6cbe8bf15cbfa63f1162b6f89c80d67c07eb103d22647ec39bd71a1"
menu_path: ["PostgreSQL: Documentation: 18: 35.43. routine_sequence_usage"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/infoschema-routine-routine-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.42.\u00a0routine_routine_usage"}
nav_next: {"path": "postgres/docs/current/infoschema-routine-table-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.44.\u00a0routine_table_usage"}
---

The view `routine_sequence_usage` identifies all sequences that are used by a function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) A sequence is only included if that sequence is owned by a currently enabled role.

**Table 35.41. `routine_sequence_usage` Columns**

| 
Column Type

Description

 |
| --- |
| 

`specific_catalog` `sql_identifier`

Name of the database containing the function (always the current database)

 |
| 

`specific_schema` `sql_identifier`

Name of the schema containing the function

 |
| 

`specific_name` `sql_identifier`

The “specific name” of the function. See [Section 35.45](https://www.postgresql.org/docs/current/infoschema-routines.html "35.45. routines") for more information.

 |
| 

`routine_catalog` `sql_identifier`

Name of the database containing the function (always the current database)

 |
| 

`routine_schema` `sql_identifier`

Name of the schema containing the function

 |
| 

`routine_name` `sql_identifier`

Name of the function (might be duplicated in case of overloading)

 |
| 

`schema_catalog` `sql_identifier`

Name of the database that contains the sequence that is used by the function (always the current database)

 |
| 

`sequence_schema` `sql_identifier`

Name of the schema that contains the sequence that is used by the function

 |
| 

`sequence_name` `sql_identifier`

Name of the sequence that is used by the function

 |
