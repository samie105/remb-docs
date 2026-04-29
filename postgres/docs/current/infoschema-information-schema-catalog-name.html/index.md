---
title: "PostgreSQL: Documentation: 18: 35.3. information_schema_catalog_name"
source: "https://www.postgresql.org/docs/current/infoschema-information-schema-catalog-name.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-information-schema-catalog-name.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:45:25.650Z"
content_hash: "245d496fb1982181451ed29f79f5c04323e16bf6087ded84d8e3ac3051de86d1"
menu_path: ["PostgreSQL: Documentation: 18: 35.3. information_schema_catalog_name"]
section_path: []
content_language: "en"
nav_prev: {"path": "../infoschema-foreign-tables.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.31.\u00a0foreign_tables"}
nav_next: {"path": "../infoschema-key-column-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.32.\u00a0key_column_usage"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/infoschema-information-schema-catalog-name.html "PostgreSQL devel - 35.3. information_schema_catalog_name")

| 35.3. `information_schema_catalog_name` |
| --- |
| [Prev](https://www.postgresql.org/docs/current/infoschema-datatypes.html "35.2. Data Types")  | [Up](https://www.postgresql.org/docs/current/information-schema.html "Chapter 35. The Information Schema") | Chapter 35. The Information Schema | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/infoschema-administrable-role-authorizations.html "35.4. administrable_role_​authorizations") |

* * *

`information_schema_catalog_name` is a table that always contains one row and one column containing the name of the current database (current catalog, in SQL terminology).

**Table 35.1. `information_schema_catalog_name` Columns**

| 
Column Type

Description

 |
| --- |
| 

`catalog_name` `sql_identifier`

Name of the database that contains this information schema

 |
