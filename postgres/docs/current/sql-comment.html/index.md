---
title: "PostgreSQL: Documentation: 18: COMMENT"
source: "https://www.postgresql.org/docs/current/sql-comment.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-comment.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:51.004Z"
content_hash: "4a62f77cc169a8f8a3b4cf5e61581ce2da4ef401f4f954e564b4f67ba08d650c"
menu_path: ["PostgreSQL: Documentation: 18: COMMENT"]
section_path: []
nav_prev: {"path": "postgres/docs/current/textsearch-parsers.html/index.md", "title": "PostgreSQL: Documentation: 18: 12.5.\u00a0Parsers"}
nav_next: {"path": "postgres/docs/current/catalog-pg-publication.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.40.\u00a0pg_publication"}
---

COMMENT — define or change the comment of an object

## Synopsis

COMMENT ON
{
  ACCESS METHOD _`object_name`_ |
  AGGREGATE _`aggregate_name`_ ( _`aggregate_signature`_ ) |
  CAST (_`source_type`_ AS _`target_type`_) |
  COLLATION _`object_name`_ |
  COLUMN _`relation_name`_._`column_name`_ |
  CONSTRAINT _`constraint_name`_ ON _`table_name`_ |
  CONSTRAINT _`constraint_name`_ ON DOMAIN _`domain_name`_ |
  CONVERSION _`object_name`_ |
  DATABASE _`object_name`_ |
  DOMAIN _`object_name`_ |
  EXTENSION _`object_name`_ |
  EVENT TRIGGER _`object_name`_ |
  FOREIGN DATA WRAPPER _`object_name`_ |
  FOREIGN TABLE _`object_name`_ |
  FUNCTION _`function_name`_ \[ ( \[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[, ...\] \] ) \] |
  INDEX _`object_name`_ |
  LARGE OBJECT _`large_object_oid`_ |
  MATERIALIZED VIEW _`object_name`_ |
  OPERATOR _`operator_name`_ (_`left_type`_, _`right_type`_) |
  OPERATOR CLASS _`object_name`_ USING _`index_method`_ |
  OPERATOR FAMILY _`object_name`_ USING _`index_method`_ |
  POLICY _`policy_name`_ ON _`table_name`_ |
  \[ PROCEDURAL \] LANGUAGE _`object_name`_ |
  PROCEDURE _`procedure_name`_ \[ ( \[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[, ...\] \] ) \] |
  PUBLICATION _`object_name`_ |
  ROLE _`object_name`_ |
  ROUTINE _`routine_name`_ \[ ( \[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[, ...\] \] ) \] |
  RULE _`rule_name`_ ON _`table_name`_ |
  SCHEMA _`object_name`_ |
  SEQUENCE _`object_name`_ |
  SERVER _`object_name`_ |
  STATISTICS _`object_name`_ |
  SUBSCRIPTION _`object_name`_ |
  TABLE _`object_name`_ |
  TABLESPACE _`object_name`_ |
  TEXT SEARCH CONFIGURATION _`object_name`_ |
  TEXT SEARCH DICTIONARY _`object_name`_ |
  TEXT SEARCH PARSER _`object_name`_ |
  TEXT SEARCH TEMPLATE _`object_name`_ |
  TRANSFORM FOR _`type_name`_ LANGUAGE _`lang_name`_ |
  TRIGGER _`trigger_name`_ ON _`table_name`_ |
  TYPE _`object_name`_ |
  VIEW _`object_name`_
} IS { _`string_literal`_ | NULL }

where _`aggregate_signature`_ is:

\* |
\[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[ , ... \] |
\[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[ , ... \] \] ORDER BY \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[ , ... \]

## Description

`COMMENT` stores a comment about a database object.

Only one comment string is stored for each object, so to modify a comment, issue a new `COMMENT` command for the same object. To remove a comment, write `NULL` in place of the text string. Comments are automatically dropped when their object is dropped.

A `SHARE UPDATE EXCLUSIVE` lock is acquired on the object to be commented.

For most kinds of object, only the object's owner can set the comment. Roles don't have owners, so the rule for `COMMENT ON ROLE` is that you must be superuser to comment on a superuser role, or have the `CREATEROLE` privilege and have been granted `ADMIN OPTION` on the target role. Likewise, access methods don't have owners either; you must be superuser to comment on an access method. Of course, a superuser can comment on anything.

Comments can be viewed using psql's `\d` family of commands. Other user interfaces to retrieve comments can be built atop the same built-in functions that psql uses, namely `obj_description`, `col_description`, and `shobj_description` (see [Table 9.82](https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-COMMENT-TABLE "Table 9.82. Comment Information Functions")).

## Parameters

_`object_name`_  
_`relation_name`_._`column_name`_  
_`aggregate_name`_  
_`constraint_name`_  
_`function_name`_  
_`operator_name`_  
_`policy_name`_  
_`procedure_name`_  
_`routine_name`_  
_`rule_name`_  
_`trigger_name`_

The name of the object to be commented. Names of objects that reside in schemas (tables, functions, etc.) can be schema-qualified. When commenting on a column, _`relation_name`_ must refer to a table, view, composite type, or foreign table.

_`table_name`_  
_`domain_name`_

When creating a comment on a constraint, a trigger, a rule or a policy these parameters specify the name of the table or domain on which that object is defined.

_`source_type`_

The name of the source data type of the cast.

_`target_type`_

The name of the target data type of the cast.

_`argmode`_

The mode of a function, procedure, or aggregate argument: `IN`, `OUT`, `INOUT`, or `VARIADIC`. If omitted, the default is `IN`. Note that `COMMENT` does not actually pay any attention to `OUT` arguments, since only the input arguments are needed to determine the function's identity. So it is sufficient to list the `IN`, `INOUT`, and `VARIADIC` arguments.

_`argname`_

The name of a function, procedure, or aggregate argument. Note that `COMMENT` does not actually pay any attention to argument names, since only the argument data types are needed to determine the function's identity.

_`argtype`_

The data type of a function, procedure, or aggregate argument.

_`large_object_oid`_

The OID of the large object.

_`left_type`_  
_`right_type`_

The data type(s) of the operator's arguments (optionally schema-qualified). Write `NONE` for the missing argument of a prefix operator.

`PROCEDURAL`

This is a noise word.

_`type_name`_

The name of the data type of the transform.

_`lang_name`_

The name of the language of the transform.

_`string_literal`_

The new comment contents, written as a string literal.

`NULL`

Write `NULL` to drop the comment.

## Notes

There is presently no security mechanism for viewing comments: any user connected to a database can see all the comments for objects in that database. For shared objects such as databases, roles, and tablespaces, comments are stored globally so any user connected to any database in the cluster can see all the comments for shared objects. Therefore, don't put security-critical information in comments.

## Examples

Attach a comment to the table `mytable`:

COMMENT ON TABLE mytable IS 'This is my table.';

Remove it again:

COMMENT ON TABLE mytable IS NULL;

Some more examples:

COMMENT ON ACCESS METHOD gin IS 'GIN index access method';
COMMENT ON AGGREGATE my\_aggregate (double precision) IS 'Computes sample variance';
COMMENT ON CAST (text AS int4) IS 'Allow casts from text to int4';
COMMENT ON COLLATION "fr\_CA" IS 'Canadian French';
COMMENT ON COLUMN my\_table.my\_column IS 'Employee ID number';
COMMENT ON CONVERSION my\_conv IS 'Conversion to UTF8';
COMMENT ON CONSTRAINT bar\_col\_cons ON bar IS 'Constrains column col';
COMMENT ON CONSTRAINT dom\_col\_constr ON DOMAIN dom IS 'Constrains col of domain';
COMMENT ON DATABASE my\_database IS 'Development Database';
COMMENT ON DOMAIN my\_domain IS 'Email Address Domain';
COMMENT ON EVENT TRIGGER abort\_ddl IS 'Aborts all DDL commands';
COMMENT ON EXTENSION hstore IS 'implements the hstore data type';
COMMENT ON FOREIGN DATA WRAPPER mywrapper IS 'my foreign data wrapper';
COMMENT ON FOREIGN TABLE my\_foreign\_table IS 'Employee Information in other database';
COMMENT ON FUNCTION my\_function (timestamp) IS 'Returns Roman Numeral';
COMMENT ON INDEX my\_index IS 'Enforces uniqueness on employee ID';
COMMENT ON LANGUAGE plpython IS 'Python support for stored procedures';
COMMENT ON LARGE OBJECT 346344 IS 'Planning document';
COMMENT ON MATERIALIZED VIEW my\_matview IS 'Summary of order history';
COMMENT ON OPERATOR ^ (text, text) IS 'Performs intersection of two texts';
COMMENT ON OPERATOR - (NONE, integer) IS 'Unary minus';
COMMENT ON OPERATOR CLASS int4ops USING btree IS '4 byte integer operators for btrees';
COMMENT ON OPERATOR FAMILY integer\_ops USING btree IS 'all integer operators for btrees';
COMMENT ON POLICY my\_policy ON mytable IS 'Filter rows by users';
COMMENT ON PROCEDURE my\_proc (integer, integer) IS 'Runs a report';
COMMENT ON PUBLICATION alltables IS 'Publishes all operations on all tables';
COMMENT ON ROLE my\_role IS 'Administration group for finance tables';
COMMENT ON ROUTINE my\_routine (integer, integer) IS 'Runs a routine (which is a function or procedure)';
COMMENT ON RULE my\_rule ON my\_table IS 'Logs updates of employee records';
COMMENT ON SCHEMA my\_schema IS 'Departmental data';
COMMENT ON SEQUENCE my\_sequence IS 'Used to generate primary keys';
COMMENT ON SERVER myserver IS 'my foreign server';
COMMENT ON STATISTICS my\_statistics IS 'Improves planner row estimations';
COMMENT ON SUBSCRIPTION alltables IS 'Subscription for all operations on all tables';
COMMENT ON TABLE my\_schema.my\_table IS 'Employee Information';
COMMENT ON TABLESPACE my\_tablespace IS 'Tablespace for indexes';
COMMENT ON TEXT SEARCH CONFIGURATION my\_config IS 'Special word filtering';
COMMENT ON TEXT SEARCH DICTIONARY swedish IS 'Snowball stemmer for Swedish language';
COMMENT ON TEXT SEARCH PARSER my\_parser IS 'Splits text into words';
COMMENT ON TEXT SEARCH TEMPLATE snowball IS 'Snowball stemmer';
COMMENT ON TRANSFORM FOR hstore LANGUAGE plpython3u IS 'Transform between hstore and Python dict';
COMMENT ON TRIGGER my\_trigger ON my\_table IS 'Used for RI';
COMMENT ON TYPE complex IS 'Complex number data type';
COMMENT ON VIEW my\_view IS 'View of departmental costs';

## Compatibility

There is no `COMMENT` command in the SQL standard.


