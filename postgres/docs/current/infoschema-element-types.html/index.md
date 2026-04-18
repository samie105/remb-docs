---
title: "PostgreSQL: Documentation: 18: 35.24. element_types"
source: "https://www.postgresql.org/docs/current/infoschema-element-types.html"
canonical_url: "https://www.postgresql.org/docs/current/infoschema-element-types.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:58.204Z"
content_hash: "d7ea868c3e47c32f9d882f544438977b05f8d60966b43a14b86f5eb6958cfe1e"
menu_path: ["PostgreSQL: Documentation: 18: 35.24. element_types"]
section_path: []
---
Column Type

Description

`object_catalog` `sql_identifier`

Name of the database that contains the object that uses the array being described (always the current database)

`object_schema` `sql_identifier`

Name of the schema that contains the object that uses the array being described

`object_name` `sql_identifier`

Name of the object that uses the array being described

`object_type` `character_data`

The type of the object that uses the array being described: one of `TABLE` (the array is used by a column of that table), `USER-DEFINED TYPE` (the array is used by an attribute of that composite type), `DOMAIN` (the array is used by that domain), `ROUTINE` (the array is used by a parameter or the return data type of that function).

`collection_type_identifier` `sql_identifier`

The identifier of the data type descriptor of the array being described. Use this to join with the `dtd_identifier` columns of other information schema views.

`data_type` `character_data`

Data type of the array elements, if it is a built-in type, else `USER-DEFINED` (in that case, the type is identified in `udt_name` and associated columns).

`character_maximum_length` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`character_octet_length` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`character_set_catalog` `sql_identifier`

Applies to a feature not available in PostgreSQL

`character_set_schema` `sql_identifier`

Applies to a feature not available in PostgreSQL

`character_set_name` `sql_identifier`

Applies to a feature not available in PostgreSQL

`collation_catalog` `sql_identifier`

Name of the database containing the collation of the element type (always the current database), null if default or the data type of the element is not collatable

`collation_schema` `sql_identifier`

Name of the schema containing the collation of the element type, null if default or the data type of the element is not collatable

`collation_name` `sql_identifier`

Name of the collation of the element type, null if default or the data type of the element is not collatable

`numeric_precision` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`numeric_precision_radix` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`numeric_scale` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`datetime_precision` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`interval_type` `character_data`

Always null, since this information is not applied to array element data types in PostgreSQL

`interval_precision` `cardinal_number`

Always null, since this information is not applied to array element data types in PostgreSQL

`udt_catalog` `sql_identifier`

Name of the database that the data type of the elements is defined in (always the current database)

`udt_schema` `sql_identifier`

Name of the schema that the data type of the elements is defined in

`udt_name` `sql_identifier`

Name of the data type of the elements

`scope_catalog` `sql_identifier`

Applies to a feature not available in PostgreSQL

`scope_schema` `sql_identifier`

Applies to a feature not available in PostgreSQL

`scope_name` `sql_identifier`

Applies to a feature not available in PostgreSQL

`maximum_cardinality` `cardinal_number`

Always null, because arrays always have unlimited maximum cardinality in PostgreSQL

`dtd_identifier` `sql_identifier`

An identifier of the data type descriptor of the element. This is currently not useful.
