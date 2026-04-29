---
title: "PostgreSQL: Documentation: 18: 35.42. routine_routine_usage"
source: "https://www.postgresql.org/docs/current/infoschema-routine-routine-usage.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-routine-routine-usage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:26.281Z"
content_hash: "0244844b4827a2d028108b929677686e6ec422f004f2d58707e2fce3d10f0e86"
menu_path: ["PostgreSQL: Documentation: 18: 35.42. routine_routine_usage"]
section_path: []
content_language: "en"
nav_prev: {"path": "../infoschema-routine-privileges.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.41.\u00a0routine_privileges"}
nav_next: {"path": "../infoschema-routine-sequence-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.43.\u00a0routine_sequence_usage"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/infoschema-routine-routine-usage.html "PostgreSQL devel - 35.42. routine_routine_usage")

The view `routine_routine_usage` identifies all functions or procedures that are used by another (or the same) function or procedure, either in the SQL body or in parameter default expressions. (This only works for unquoted SQL bodies, not quoted bodies or functions in other languages.) An entry is included here only if the used function is owned by a currently enabled role. (There is no such restriction on the using function.)

Note that the entries for both functions in the view refer to the “specific” name of the routine, even though the column names are used in a way that is inconsistent with other information schema views about routines. This is per SQL standard, although it is arguably a misdesign. See [Section 35.45](https://www.postgresql.org/docs/current/infoschema-routines.html "35.45. routines") for more information about specific names.

**Table 35.40. `routine_routine_usage` Columns**

| 
Column Type

Description

 |
| --- |
| 

`specific_catalog` `sql_identifier`

Name of the database containing the using function (always the current database)

 |
| 

`specific_schema` `sql_identifier`

Name of the schema containing the using function

 |
| 

`specific_name` `sql_identifier`

The “specific name” of the using function.

 |
| 

`routine_catalog` `sql_identifier`

Name of the database that contains the function that is used by the first function (always the current database)

 |
| 

`routine_schema` `sql_identifier`

Name of the schema that contains the function that is used by the first function

 |
| 

`routine_name` `sql_identifier`

The “specific name” of the function that is used by the first function.

 |
