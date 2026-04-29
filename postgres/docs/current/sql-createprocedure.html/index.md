---
title: "PostgreSQL: Documentation: 18: CREATE PROCEDURE"
source: "https://www.postgresql.org/docs/current/sql-createprocedure.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createprocedure.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:56.815Z"
content_hash: "aa7c4bd49d4abb84bb6c183b0e21094f54391654270c0a41ffb9a8b36278375f"
menu_path: ["PostgreSQL: Documentation: 18: CREATE PROCEDURE"]
section_path: []
nav_prev: {"path": "../sql-createpolicy.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE POLICY"}
nav_next: {"path": "../sql-createpublication.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE PUBLICATION"}
---

CREATE PROCEDURE — define a new procedure

## Synopsis

CREATE \[ OR REPLACE \] PROCEDURE
    _`name`_ ( \[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[ { DEFAULT | = } _`default_expr`_ \] \[, ...\] \] )
  { LANGUAGE _`lang_name`_
    | TRANSFORM { FOR TYPE _`type_name`_ } \[, ... \]
    | \[ EXTERNAL \] SECURITY INVOKER | \[ EXTERNAL \] SECURITY DEFINER
    | SET _`configuration_parameter`_ { TO _`value`_ | = _`value`_ | FROM CURRENT }
    | AS '_`definition`_'
    | AS '_`obj_file`_', '_`link_symbol`_'
    | _`sql_body`_
  } ...

## Description

`CREATE PROCEDURE` defines a new procedure. `CREATE OR REPLACE PROCEDURE` will either create a new procedure, or replace an existing definition. To be able to define a procedure, the user must have the `USAGE` privilege on the language.

If a schema name is included, then the procedure is created in the specified schema. Otherwise it is created in the current schema. The name of the new procedure must not match any existing procedure or function with the same input argument types in the same schema. However, procedures and functions of different argument types can share a name (this is called _overloading_).

To replace the current definition of an existing procedure, use `CREATE OR REPLACE PROCEDURE`. It is not possible to change the name or argument types of a procedure this way (if you tried, you would actually be creating a new, distinct procedure).

When `CREATE OR REPLACE PROCEDURE` is used to replace an existing procedure, the ownership and permissions of the procedure do not change. All other procedure properties are assigned the values specified or implied in the command. You must own the procedure to replace it (this includes being a member of the owning role).

The user that creates the procedure becomes the owner of the procedure.

To be able to create a procedure, you must have `USAGE` privilege on the argument types.

Refer to [Section 36.4](https://www.postgresql.org/docs/current/xproc.html "36.4. User-Defined Procedures") for further information on writing procedures.

## Parameters

_`name`_

The name (optionally schema-qualified) of the procedure to create.

_`argmode`_

The mode of an argument: `IN`, `OUT`, `INOUT`, or `VARIADIC`. If omitted, the default is `IN`.

_`argname`_

The name of an argument.

_`argtype`_

The data type(s) of the procedure's arguments (optionally schema-qualified), if any. The argument types can be base, composite, or domain types, or can reference the type of a table column.

Depending on the implementation language it might also be allowed to specify “pseudo-types” such as `cstring`. Pseudo-types indicate that the actual argument type is either incompletely specified, or outside the set of ordinary SQL data types.

The type of a column is referenced by writing ``_`table_name`_._`column_name`_%TYPE``. Using this feature can sometimes help make a procedure independent of changes to the definition of a table.

_`default_expr`_

An expression to be used as default value if the parameter is not specified. The expression has to be coercible to the argument type of the parameter. All input parameters following a parameter with a default value must have default values as well.

_`lang_name`_

The name of the language that the procedure is implemented in. It can be `sql`, `c`, `internal`, or the name of a user-defined procedural language, e.g., `plpgsql`. The default is `sql` if _`sql_body`_ is specified. Enclosing the name in single quotes is deprecated and requires matching case.

``TRANSFORM { FOR TYPE _`type_name`_ } [, ... ] }``

Lists which transforms a call to the procedure should apply. Transforms convert between SQL types and language-specific data types; see [CREATE TRANSFORM](https://www.postgresql.org/docs/current/sql-createtransform.html "CREATE TRANSFORM"). Procedural language implementations usually have hardcoded knowledge of the built-in types, so those don't need to be listed here. If a procedural language implementation does not know how to handle a type and no transform is supplied, it will fall back to a default behavior for converting data types, but this depends on the implementation.

`[EXTERNAL] SECURITY INVOKER`  
`[EXTERNAL] SECURITY DEFINER`

`SECURITY INVOKER` indicates that the procedure is to be executed with the privileges of the user that calls it. That is the default. `SECURITY DEFINER` specifies that the procedure is to be executed with the privileges of the user that owns it.

The key word `EXTERNAL` is allowed for SQL conformance, but it is optional since, unlike in SQL, this feature applies to all procedures not only external ones.

A `SECURITY DEFINER` procedure cannot execute transaction control statements (for example, `COMMIT` and `ROLLBACK`, depending on the language).

_`configuration_parameter`_  
_`value`_

The `SET` clause causes the specified configuration parameter to be set to the specified value when the procedure is entered, and then restored to its prior value when the procedure exits. `SET FROM CURRENT` saves the value of the parameter that is current when `CREATE PROCEDURE` is executed as the value to be applied when the procedure is entered.

If a `SET` clause is attached to a procedure, then the effects of a `SET LOCAL` command executed inside the procedure for the same variable are restricted to the procedure: the configuration parameter's prior value is still restored at procedure exit. However, an ordinary `SET` command (without `LOCAL`) overrides the `SET` clause, much as it would do for a previous `SET LOCAL` command: the effects of such a command will persist after procedure exit, unless the current transaction is rolled back.

If a `SET` clause is attached to a procedure, then that procedure cannot execute transaction control statements (for example, `COMMIT` and `ROLLBACK`, depending on the language).

See [SET](https://www.postgresql.org/docs/current/sql-set.html "SET") and [Chapter 19](https://www.postgresql.org/docs/current/runtime-config.html "Chapter 19. Server Configuration") for more information about allowed parameter names and values.

_`definition`_

A string constant defining the procedure; the meaning depends on the language. It can be an internal procedure name, the path to an object file, an SQL command, or text in a procedural language.

It is often helpful to use dollar quoting (see [Section 4.1.2.4](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-DOLLAR-QUOTING "4.1.2.4. Dollar-Quoted String Constants")) to write the procedure definition string, rather than the normal single quote syntax. Without dollar quoting, any single quotes or backslashes in the procedure definition must be escaped by doubling them.

``_`obj_file`_, _`link_symbol`_``

This form of the `AS` clause is used for dynamically loadable C language procedures when the procedure name in the C language source code is not the same as the name of the SQL procedure. The string _`obj_file`_ is the name of the shared library file containing the compiled C procedure, and is interpreted as for the [`LOAD`](https://www.postgresql.org/docs/current/sql-load.html "LOAD") command. The string _`link_symbol`_ is the procedure's link symbol, that is, the name of the procedure in the C language source code. If the link symbol is omitted, it is assumed to be the same as the name of the SQL procedure being defined.

When repeated `CREATE PROCEDURE` calls refer to the same object file, the file is only loaded once per session. To unload and reload the file (perhaps during development), start a new session.

_`sql_body`_

The body of a `LANGUAGE SQL` procedure. This should be a block

BEGIN ATOMIC
  _`statement`_;
  _`statement`_;
  ...
  _`statement`_;
END

This is similar to writing the text of the procedure body as a string constant (see _`definition`_ above), but there are some differences: This form only works for `LANGUAGE SQL`, the string constant form works for all languages. This form is parsed at procedure definition time, the string constant form is parsed at execution time; therefore this form cannot support polymorphic argument types and other constructs that are not resolvable at procedure definition time. This form tracks dependencies between the procedure and objects used in the procedure body, so `DROP ... CASCADE` will work correctly, whereas the form using string literals may leave dangling procedures. Finally, this form is more compatible with the SQL standard and other SQL implementations.

## Notes

See [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION") for more details on function creation that also apply to procedures.

Use [CALL](https://www.postgresql.org/docs/current/sql-call.html "CALL") to execute a procedure.

## Examples

CREATE PROCEDURE insert\_data(a integer, b integer)
LANGUAGE SQL
AS $$
INSERT INTO tbl VALUES (a);
INSERT INTO tbl VALUES (b);
$$;

or

CREATE PROCEDURE insert\_data(a integer, b integer)
LANGUAGE SQL
BEGIN ATOMIC
  INSERT INTO tbl VALUES (a);
  INSERT INTO tbl VALUES (b);
END;

and call like this:

CALL insert\_data(1, 2);

## Compatibility

A `CREATE PROCEDURE` command is defined in the SQL standard. The PostgreSQL implementation can be used in a compatible way but has many extensions. For details see also [CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html "CREATE FUNCTION").
