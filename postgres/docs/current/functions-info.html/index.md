---
title: "PostgreSQL: Documentation: 18: 9.27. System Information Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions-info.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-info.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:46.261Z"
content_hash: "a6f186f8157ea9cb113d584154f13bfd945fbbb130daf52d93b3193c7386c527"
menu_path: ["PostgreSQL: Documentation: 18: 9.27. System Information Functions and Operators"]
section_path: []
content_language: "en"
---
| 
Function

Description

 |
| --- |
| 

`format_type` ( _`type`_ `oid`, _`typemod`_ `integer` ) → `text`

Returns the SQL name for a data type that is identified by its type OID and possibly a type modifier. Pass NULL for the type modifier if no specific modifier is known.

 |
| 

`pg_basetype` ( `regtype` ) → `regtype`

Returns the OID of the base type of a domain identified by its type OID. If the argument is the OID of a non-domain type, returns the argument as-is. Returns NULL if the argument is not a valid type OID. If there's a chain of domain dependencies, it will recurse until finding the base type.

Assuming `CREATE DOMAIN mytext AS text`:

`pg_basetype('mytext'::regtype)` → `text`

 |
| 

`pg_char_to_encoding` ( _`encoding`_ `name` ) → `integer`

Converts the supplied encoding name into an integer representing the internal identifier used in some system catalog tables. Returns `-1` if an unknown encoding name is provided.

 |
| 

`pg_encoding_to_char` ( _`encoding`_ `integer` ) → `name`

Converts the integer used as the internal identifier of an encoding in some system catalog tables into a human-readable string. Returns an empty string if an invalid encoding number is provided.

 |
| 

`pg_get_catalog_foreign_keys` () → `setof record` ( _`fktable`_ `regclass`, _`fkcols`_ `text[]`, _`pktable`_ `regclass`, _`pkcols`_ `text[]`, _`is_array`_ `boolean`, _`is_opt`_ `boolean` )

Returns a set of records describing the foreign key relationships that exist within the PostgreSQL system catalogs. The _`fktable`_ column contains the name of the referencing catalog, and the _`fkcols`_ column contains the name(s) of the referencing column(s). Similarly, the _`pktable`_ column contains the name of the referenced catalog, and the _`pkcols`_ column contains the name(s) of the referenced column(s). If _`is_array`_ is true, the last referencing column is an array, each of whose elements should match some entry in the referenced catalog. If _`is_opt`_ is true, the referencing column(s) are allowed to contain zeroes instead of a valid reference.

 |
| 

`pg_get_constraintdef` ( _`constraint`_ `oid` \[, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the creating command for a constraint. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_expr` ( _`expr`_ `pg_node_tree`, _`relation`_ `oid` \[, _`pretty`_ `boolean` \] ) → `text`

Decompiles the internal form of an expression stored in the system catalogs, such as the default value for a column. If the expression might contain Vars, specify the OID of the relation they refer to as the second parameter; if no Vars are expected, passing zero is sufficient.

 |
| 

`pg_get_functiondef` ( _`func`_ `oid` ) → `text`

Reconstructs the creating command for a function or procedure. (This is a decompiled reconstruction, not the original text of the command.) The result is a complete `CREATE OR REPLACE FUNCTION` or `CREATE OR REPLACE PROCEDURE` statement.

 |
| 

`pg_get_function_arguments` ( _`func`_ `oid` ) → `text`

Reconstructs the argument list of a function or procedure, in the form it would need to appear in within `CREATE FUNCTION` (including default values).

 |
| 

`pg_get_function_identity_arguments` ( _`func`_ `oid` ) → `text`

Reconstructs the argument list necessary to identify a function or procedure, in the form it would need to appear in within commands such as `ALTER FUNCTION`. This form omits default values.

 |
| 

`pg_get_function_result` ( _`func`_ `oid` ) → `text`

Reconstructs the `RETURNS` clause of a function, in the form it would need to appear in within `CREATE FUNCTION`. Returns `NULL` for a procedure.

 |
| 

`pg_get_indexdef` ( _`index`_ `oid` \[, _`column`_ `integer`, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the creating command for an index. (This is a decompiled reconstruction, not the original text of the command.) If _`column`_ is supplied and is not zero, only the definition of that column is reconstructed.

 |
| 

`pg_get_keywords` () → `setof record` ( _`word`_ `text`, _`catcode`_ `"char"`, _`barelabel`_ `boolean`, _`catdesc`_ `text`, _`baredesc`_ `text` )

Returns a set of records describing the SQL keywords recognized by the server. The _`word`_ column contains the keyword. The _`catcode`_ column contains a category code: `U` for an unreserved keyword, `C` for a keyword that can be a column name, `T` for a keyword that can be a type or function name, or `R` for a fully reserved keyword. The _`barelabel`_ column contains `true` if the keyword can be used as a “bare” column label in `SELECT` lists, or `false` if it can only be used after `AS`. The _`catdesc`_ column contains a possibly-localized string describing the keyword's category. The _`baredesc`_ column contains a possibly-localized string describing the keyword's column label status.

 |
| 

`pg_get_partition_constraintdef` ( _`table`_ `oid` ) → `text`

Reconstructs the definition of a partition constraint. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_partkeydef` ( _`table`_ `oid` ) → `text`

Reconstructs the definition of a partitioned table's partition key, in the form it would have in the `PARTITION BY` clause of `CREATE TABLE`. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_ruledef` ( _`rule`_ `oid` \[, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the creating command for a rule. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_serial_sequence` ( _`table`_ `text`, _`column`_ `text` ) → `text`

Returns the name of the sequence associated with a column, or NULL if no sequence is associated with the column. If the column is an identity column, the associated sequence is the sequence internally created for that column. For columns created using one of the serial types (`serial`, `smallserial`, `bigserial`), it is the sequence created for that serial column definition. In the latter case, the association can be modified or removed with `ALTER SEQUENCE OWNED BY`. (This function probably should have been called `pg_get_owned_sequence`; its current name reflects the fact that it has historically been used with serial-type columns.) The first parameter is a table name with optional schema, and the second parameter is a column name. Because the first parameter potentially contains both schema and table names, it is parsed per usual SQL rules, meaning it is lower-cased by default. The second parameter, being just a column name, is treated literally and so has its case preserved. The result is suitably formatted for passing to the sequence functions (see [Section 9.17](https://www.postgresql.org/docs/current/functions-sequence.html "9.17. Sequence Manipulation Functions")).

A typical use is in reading the current value of the sequence for an identity or serial column, for example:

SELECT currval(pg\_get\_serial\_sequence('sometable', 'id'));

 |
| 

`pg_get_statisticsobjdef` ( _`statobj`_ `oid` ) → `text`

Reconstructs the creating command for an extended statistics object. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_triggerdef` ( _`trigger`_ `oid` \[, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the creating command for a trigger. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_userbyid` ( _`role`_ `oid` ) → `name`

Returns a role's name given its OID.

 |
| 

`pg_get_viewdef` ( _`view`_ `oid` \[, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the underlying `SELECT` command for a view or materialized view. (This is a decompiled reconstruction, not the original text of the command.)

 |
| 

`pg_get_viewdef` ( _`view`_ `oid`, _`wrap_column`_ `integer` ) → `text`

Reconstructs the underlying `SELECT` command for a view or materialized view. (This is a decompiled reconstruction, not the original text of the command.) In this form of the function, pretty-printing is always enabled, and long lines are wrapped to try to keep them shorter than the specified number of columns.

 |
| 

`pg_get_viewdef` ( _`view`_ `text` \[, _`pretty`_ `boolean` \] ) → `text`

Reconstructs the underlying `SELECT` command for a view or materialized view, working from a textual name for the view rather than its OID. (This is deprecated; use the OID variant instead.)

 |
| 

`pg_index_column_has_property` ( _`index`_ `regclass`, _`column`_ `integer`, _`property`_ `text` ) → `boolean`

Tests whether an index column has the named property. Common index column properties are listed in [Table 9.77](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-INDEX-COLUMN-PROPS "Table 9.77. Index Column Properties"). (Note that extension access methods can define additional property names for their indexes.) `NULL` is returned if the property name is not known or does not apply to the particular object, or if the OID or column number does not identify a valid object.

 |
| 

`pg_index_has_property` ( _`index`_ `regclass`, _`property`_ `text` ) → `boolean`

Tests whether an index has the named property. Common index properties are listed in [Table 9.78](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-INDEX-PROPS "Table 9.78. Index Properties"). (Note that extension access methods can define additional property names for their indexes.) `NULL` is returned if the property name is not known or does not apply to the particular object, or if the OID does not identify a valid object.

 |
| 

`pg_indexam_has_property` ( _`am`_ `oid`, _`property`_ `text` ) → `boolean`

Tests whether an index access method has the named property. Access method properties are listed in [Table 9.79](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-INDEXAM-PROPS "Table 9.79. Index Access Method Properties"). `NULL` is returned if the property name is not known or does not apply to the particular object, or if the OID does not identify a valid object.

 |
| 

`pg_options_to_table` ( _`options_array`_ `text[]` ) → `setof record` ( _`option_name`_ `text`, _`option_value`_ `text` )

Returns the set of storage options represented by a value from `pg_class`.`reloptions` or `pg_attribute`.`attoptions`.

 |
| 

`pg_settings_get_flags` ( _`guc`_ `text` ) → `text[]`

Returns an array of the flags associated with the given GUC, or `NULL` if it does not exist. The result is an empty array if the GUC exists but there are no flags to show. Only the most useful flags listed in [Table 9.80](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-PG-SETTINGS-FLAGS "Table 9.80. GUC Flags") are exposed.

 |
| 

`pg_tablespace_databases` ( _`tablespace`_ `oid` ) → `setof oid`

Returns the set of OIDs of databases that have objects stored in the specified tablespace. If this function returns any rows, the tablespace is not empty and cannot be dropped. To identify the specific objects populating the tablespace, you will need to connect to the database(s) identified by `pg_tablespace_databases` and query their `pg_class` catalogs.

 |
| 

`pg_tablespace_location` ( _`tablespace`_ `oid` ) → `text`

Returns the file system path that this tablespace is located in.

 |
| 

`pg_typeof` ( `"any"` ) → `regtype`

Returns the OID of the data type of the value that is passed to it. This can be helpful for troubleshooting or dynamically constructing SQL queries. The function is declared as returning `regtype`, which is an OID alias type (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); this means that it is the same as an OID for comparison purposes but displays as a type name.

`pg_typeof(33)` → `integer`

 |
| 

`COLLATION FOR` ( `"any"` ) → `text`

Returns the name of the collation of the value that is passed to it. The value is quoted and schema-qualified if necessary. If no collation was derived for the argument expression, then `NULL` is returned. If the argument is not of a collatable data type, then an error is raised.

`collation for ('foo'::text)` → `"default"`

`collation for ('foo' COLLATE "de_DE")` → `"de_DE"`

 |
| 

`to_regclass` ( `text` ) → `regclass`

Translates a textual relation name to its OID. A similar result is obtained by casting the string to type `regclass` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regcollation` ( `text` ) → `regcollation`

Translates a textual collation name to its OID. A similar result is obtained by casting the string to type `regcollation` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regnamespace` ( `text` ) → `regnamespace`

Translates a textual schema name to its OID. A similar result is obtained by casting the string to type `regnamespace` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regoper` ( `text` ) → `regoper`

Translates a textual operator name to its OID. A similar result is obtained by casting the string to type `regoper` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found or is ambiguous.

 |
| 

`to_regoperator` ( `text` ) → `regoperator`

Translates a textual operator name (with parameter types) to its OID. A similar result is obtained by casting the string to type `regoperator` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regproc` ( `text` ) → `regproc`

Translates a textual function or procedure name to its OID. A similar result is obtained by casting the string to type `regproc` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found or is ambiguous.

 |
| 

`to_regprocedure` ( `text` ) → `regprocedure`

Translates a textual function or procedure name (with argument types) to its OID. A similar result is obtained by casting the string to type `regprocedure` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regrole` ( `text` ) → `regrole`

Translates a textual role name to its OID. A similar result is obtained by casting the string to type `regrole` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")); however, this function will return `NULL` rather than throwing an error if the name is not found.

 |
| 

`to_regtype` ( `text` ) → `regtype`

Parses a string of text, extracts a potential type name from it, and translates that name into a type OID. A syntax error in the string will result in an error; but if the string is a syntactically valid type name that happens not to be found in the catalogs, the result is `NULL`. A similar result is obtained by casting the string to type `regtype` (see [Section 8.19](https://www.postgresql.org/docs/current/datatype-oid.html "8.19. Object Identifier Types")), except that that will throw error for name not found.

 |
| 

`to_regtypemod` ( `text` ) → `integer`

Parses a string of text, extracts a potential type name from it, and translates its type modifier, if any. A syntax error in the string will result in an error; but if the string is a syntactically valid type name that happens not to be found in the catalogs, the result is `NULL`. The result is `-1` if no type modifier is present.

`to_regtypemod` can be combined with [to\_regtype](https://www.postgresql.org/docs/current/functions-info.html#TO-REGTYPE) to produce appropriate inputs for [format\_type](https://www.postgresql.org/docs/current/functions-info.html#FORMAT-TYPE), allowing a string representing a type name to be canonicalized.

`format_type(to_regtype('varchar(32)'), to_regtypemod('varchar(32)'))` → `character varying(32)`

 |
