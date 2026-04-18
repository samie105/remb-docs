---
title: "PostgreSQL: Documentation: 18: 35.47. sequences"
source: "https://www.postgresql.org/docs/current/infoschema-sequences.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-sequences.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:51.526Z"
content_hash: "16383ebb364f3658d22589d107062bcbc52ae07cd43766c4291ca6e93fdcebe4"
menu_path: ["PostgreSQL: Documentation: 18: 35.47. sequences"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-checkpoint.html/index.md", "title": "PostgreSQL: Documentation: 18: CHECKPOINT"}
nav_next: {"path": "postgres/docs/current/vacuumlo.html/index.md", "title": "PostgreSQL: Documentation: 18: vacuumlo"}
---

The view `sequences` contains all sequences defined in the current database. Only those sequences are shown that the current user has access to (by way of being the owner or having some privilege).

**Table 35.45. `sequences` Columns**

Column Type

Description

`sequence_catalog` `sql_identifier`

Name of the database that contains the sequence (always the current database)

`sequence_schema` `sql_identifier`

Name of the schema that contains the sequence

`sequence_name` `sql_identifier`

Name of the sequence

`data_type` `character_data`

The data type of the sequence.

`numeric_precision` `cardinal_number`

This column contains the (declared or implicit) precision of the sequence data type (see above). The precision indicates the number of significant digits. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column `numeric_precision_radix`.

`numeric_precision_radix` `cardinal_number`

This column indicates in which base the values in the columns `numeric_precision` and `numeric_scale` are expressed. The value is either 2 or 10.

`numeric_scale` `cardinal_number`

This column contains the (declared or implicit) scale of the sequence data type (see above). The scale indicates the number of significant digits to the right of the decimal point. It can be expressed in decimal (base 10) or binary (base 2) terms, as specified in the column `numeric_precision_radix`.

`start_value` `character_data`

The start value of the sequence

`minimum_value` `character_data`

The minimum value of the sequence

`maximum_value` `character_data`

The maximum value of the sequence

`increment` `character_data`

The increment of the sequence

`cycle_option` `yes_or_no`

`YES` if the sequence cycles, else `NO`

Note that in accordance with the SQL standard, the start, minimum, maximum, and increment values are returned as character strings.
