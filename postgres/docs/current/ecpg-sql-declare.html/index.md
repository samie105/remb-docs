---
title: "PostgreSQL: Documentation: 18: DECLARE"
source: "https://www.postgresql.org/docs/current/ecpg-sql-declare.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-declare.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:44.995Z"
content_hash: "28856c6a28c7b522ae21b8a9142f0c883d7c64c17b594048cfe86bc25650b828"
menu_path: ["PostgreSQL: Documentation: 18: DECLARE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-role-table-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.37.\u00a0role_table_grants"}
nav_next: {"path": "postgres/docs/current/infoschema-role-udt-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.38.\u00a0role_udt_grants"}
---

DECLARE — define a cursor

## Synopsis

DECLARE _`cursor_name`_ \[ BINARY \] \[ ASENSITIVE | INSENSITIVE \] \[ \[ NO \] SCROLL \] CURSOR \[ { WITH | WITHOUT } HOLD \] FOR _`prepared_name`_
DECLARE _`cursor_name`_ \[ BINARY \] \[ ASENSITIVE | INSENSITIVE \] \[ \[ NO \] SCROLL \] CURSOR \[ { WITH | WITHOUT } HOLD \] FOR _`query`_

## Description

`DECLARE` declares a cursor for iterating over the result set of a prepared statement. This command has slightly different semantics from the direct SQL command `DECLARE`: Whereas the latter executes a query and prepares the result set for retrieval, this embedded SQL command merely declares a name as a “loop variable” for iterating over the result set of a query; the actual execution happens when the cursor is opened with the `OPEN` command.

## Parameters

_`cursor_name`_ [#](#ECPG-SQL-DECLARE-CURSOR-NAME)

A cursor name, case sensitive. This can be an SQL identifier or a host variable.

_`prepared_name`_ [#](#ECPG-SQL-DECLARE-PREPARED-NAME)

The name of a prepared query, either as an SQL identifier or a host variable.

_`query`_ [#](#ECPG-SQL-DECLARE-QUERY)

A [SELECT](https://www.postgresql.org/docs/current/sql-select.html "SELECT") or [VALUES](https://www.postgresql.org/docs/current/sql-values.html "VALUES") command which will provide the rows to be returned by the cursor.

For the meaning of the cursor options, see [DECLARE](https://www.postgresql.org/docs/current/sql-declare.html "DECLARE").

## Examples

Examples declaring a cursor for a query:

EXEC SQL DECLARE C CURSOR FOR SELECT \* FROM My\_Table;
EXEC SQL DECLARE C CURSOR FOR SELECT Item1 FROM T;
EXEC SQL DECLARE cur1 CURSOR FOR SELECT version();

An example declaring a cursor for a prepared statement:

EXEC SQL PREPARE stmt1 AS SELECT version();
EXEC SQL DECLARE cur1 CURSOR FOR stmt1;

## Compatibility

`DECLARE` is specified in the SQL standard.

