---
title: "PostgreSQL: Documentation: 18: DROP FUNCTION"
source: "https://www.postgresql.org/docs/current/sql-dropfunction.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropfunction.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:26.909Z"
content_hash: "c5d51820d7fe7eb6f7546ddcef189a27a28b3c51880c843cf1786bc395949496"
menu_path: ["PostgreSQL: Documentation: 18: DROP FUNCTION"]
section_path: []
content_language: "en"
nav_prev: {"path": "../sql-dropeventtrigger.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"}
nav_next: {"path": "../sql-dropgroup.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP GROUP"}
---

DROP FUNCTION — remove a function

## Synopsis

DROP FUNCTION \[ IF EXISTS \] _`name`_ \[ ( \[ \[ _`argmode`_ \] \[ _`argname`_ \] _`argtype`_ \[, ...\] \] ) \] \[, ...\]
    \[ CASCADE | RESTRICT \]

## Description

`DROP FUNCTION` removes the definition of an existing function. To execute this command the user must be the owner of the function. The argument types to the function must be specified, since several different functions can exist with the same name and different argument lists.

## Parameters

`IF EXISTS`

Do not throw an error if the function does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of an existing function. If no argument list is specified, the name must be unique in its schema.

_`argmode`_

The mode of an argument: `IN`, `OUT`, `INOUT`, or `VARIADIC`. If omitted, the default is `IN`. Note that `DROP FUNCTION` does not actually pay any attention to `OUT` arguments, since only the input arguments are needed to determine the function's identity. So it is sufficient to list the `IN`, `INOUT`, and `VARIADIC` arguments.

_`argname`_

The name of an argument. Note that `DROP FUNCTION` does not actually pay any attention to argument names, since only the argument data types are needed to determine the function's identity.

_`argtype`_

The data type(s) of the function's arguments (optionally schema-qualified), if any.

`CASCADE`

Automatically drop objects that depend on the function (such as operators or triggers), and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the function if any objects depend on it. This is the default.

## Examples

This command removes the square root function:

DROP FUNCTION sqrt(integer);

Drop multiple functions in one command:

DROP FUNCTION sqrt(integer), sqrt(bigint);

If the function name is unique in its schema, it can be referred to without an argument list:

DROP FUNCTION update\_employee\_salaries;

Note that this is different from

DROP FUNCTION update\_employee\_salaries();

which refers to a function with zero arguments, whereas the first variant can refer to a function with any number of arguments, including zero, as long as the name is unique.

## Compatibility

This command conforms to the SQL standard, with these PostgreSQL extensions:

-   The standard only allows one function to be dropped per command.
    
-   The `IF EXISTS` option
    
-   The ability to specify argument modes and names
