---
title: "PostgreSQL: Documentation: 18: EXECUTE IMMEDIATE"
source: "https://www.postgresql.org/docs/current/ecpg-sql-execute-immediate.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-execute-immediate.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:16.902Z"
content_hash: "6a92330d2903ab4df12d161687bc16e6fdb82c7789aeabc557b0213dd68bcbf8"
menu_path: ["PostgreSQL: Documentation: 18: EXECUTE IMMEDIATE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/catalog-pg-shdepend.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.48.\u00a0pg_shdepend"}
nav_next: {"path": "postgres/docs/current/infoschema-domain-udt-usage.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.22.\u00a0domain_udt_usage"}
---

EXECUTE IMMEDIATE — dynamically prepare and execute a statement

## Synopsis

EXECUTE IMMEDIATE _`string`_

## Description

`EXECUTE IMMEDIATE` immediately prepares and executes a dynamically specified SQL statement, without retrieving result rows.

## Parameters

_`string`_ [#](#ECPG-SQL-EXECUTE-IMMEDIATE-STRING)

A literal string or a host variable containing the SQL statement to be executed.

## Notes

In typical usage, the _`string`_ is a host variable reference to a string containing a dynamically-constructed SQL statement. The case of a literal string is not very useful; you might as well just write the SQL statement directly, without the extra typing of `EXECUTE IMMEDIATE`.

If you do use a literal string, keep in mind that any double quotes you might wish to include in the SQL statement must be written as octal escapes (`\042`) not the usual C idiom `\"`. This is because the string is inside an `EXEC SQL` section, so the ECPG lexer parses it according to SQL rules not C rules. Any embedded backslashes will later be handled according to C rules; but `\"` causes an immediate syntax error because it is seen as ending the literal.

## Examples

Here is an example that executes an `INSERT` statement using `EXECUTE IMMEDIATE` and a host variable named `command`:

sprintf(command, "INSERT INTO test (name, amount, letter) VALUES ('db: ''r1''', 1, 'f')");
EXEC SQL EXECUTE IMMEDIATE :command;

## Compatibility

`EXECUTE IMMEDIATE` is specified in the SQL standard.


