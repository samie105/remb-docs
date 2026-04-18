---
title: "PostgreSQL: Documentation: 18: 35.49. sql_implementation_info"
source: "https://www.postgresql.org/docs/current/infoschema-sql-implementation-info.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-sql-implementation-info.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:53.406Z"
content_hash: "b5b3f082baf50c1d822bf8da32e24e36f793aac379787fc7adf81a1617e09a73"
menu_path: ["PostgreSQL: Documentation: 18: 35.49. sql_implementation_info"]
section_path: []
nav_prev: {"path": "postgres/docs/current/runtime-config-connection.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.3.\u00a0Connections and Authentication"}
nav_next: {"path": "postgres/docs/current/pageinspect.html/index.md", "title": "PostgreSQL: Documentation: 18: F.23.\u00a0pageinspect \u2014 low-level inspection of database pages"}
---

The table `sql_implementation_info` contains information about various aspects that are left implementation-defined by the SQL standard. This information is primarily intended for use in the context of the ODBC interface; users of other interfaces will probably find this information to be of little use. For this reason, the individual implementation information items are not described here; you will find them in the description of the ODBC interface.

**Table 35.47. `sql_implementation_info` Columns**

Column Type

Description

`implementation_info_id` `character_data`

Identifier string of the implementation information item

`implementation_info_name` `character_data`

Descriptive name of the implementation information item

`integer_value` `cardinal_number`

Value of the implementation information item, or null if the value is contained in the column `character_value`

`character_value` `character_data`

Value of the implementation information item, or null if the value is contained in the column `integer_value`

`comments` `character_data`

Possibly a comment pertaining to the implementation information item


