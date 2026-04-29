---
title: "PostgreSQL: Documentation: 18: CALL"
source: "https://www.postgresql.org/docs/current/sql-call.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-call.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:42.956Z"
content_hash: "6e3f1f36ab811dc0d8123bc6e3b5ae2e52c90e3db51e3d427660dfc6aef7c6de"
menu_path: ["PostgreSQL: Documentation: 18: CALL"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-begin.html/index.md", "title": "PostgreSQL: Documentation: 18: BEGIN"}
nav_next: {"path": "postgres/docs/current/sql-checkpoint.html/index.md", "title": "PostgreSQL: Documentation: 18: CHECKPOINT"}
---

CALL — invoke a procedure

## Synopsis

CALL _`name`_ ( \[ _`argument`_ \] \[, ...\] )

## Description

`CALL` executes a procedure.

If the procedure has any output parameters, then a result row will be returned, containing the values of those parameters.

## Parameters

_`name`_

The name (optionally schema-qualified) of the procedure.

_`argument`_

An argument expression for the procedure call.

Arguments can include parameter names, using the syntax ``_`name`_ => _`value`_``. This works the same as in ordinary function calls; see [Section 4.3](https://www.postgresql.org/docs/current/sql-syntax-calling-funcs.html "4.3. Calling Functions") for details.

Arguments must be supplied for all procedure parameters that lack defaults, including `OUT` parameters. However, arguments matching `OUT` parameters are not evaluated, so it's customary to just write `NULL` for them. (Writing something else for an `OUT` parameter might cause compatibility problems with future PostgreSQL versions.)

## Notes

The user must have `EXECUTE` privilege on the procedure in order to be allowed to invoke it.

To call a function (not a procedure), use `SELECT` instead.

If `CALL` is executed in a transaction block, then the called procedure cannot execute transaction control statements. Transaction control statements are only allowed if `CALL` is executed in its own transaction.

PL/pgSQL handles output parameters in `CALL` commands differently; see [Section 41.6.3](https://www.postgresql.org/docs/current/plpgsql-control-structures.html#PLPGSQL-STATEMENTS-CALLING-PROCEDURE "41.6.3. Calling a Procedure").

## Examples

CALL do\_db\_maintenance();

## Compatibility

`CALL` conforms to the SQL standard, except for the handling of output parameters. The standard says that users should write variables to receive the values of output parameters.
