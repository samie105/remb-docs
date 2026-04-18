---
title: "PostgreSQL: Documentation: 18: DECLARE STATEMENT"
source: "https://www.postgresql.org/docs/current/ecpg-sql-declare-statement.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-declare-statement.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:44.716Z"
content_hash: "be2f56892576c537a8d3125aaedde496d75c3520e3f6039c7e8b449d7ab930bd"
menu_path: ["PostgreSQL: Documentation: 18: DECLARE STATEMENT"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-dropeventtrigger.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"}
nav_next: {"path": "postgres/docs/current/btree-gin.html/index.md", "title": "PostgreSQL: Documentation: 18: F.7.\u00a0btree_gin \u2014 GIN operator classes with B-tree behavior"}
---

DECLARE STATEMENT — declare SQL statement identifier

## Synopsis

EXEC SQL \[ AT _`connection_name`_ \] DECLARE _`statement_name`_ STATEMENT

## Description

`DECLARE STATEMENT` declares an SQL statement identifier. SQL statement identifier can be associated with the connection. When the identifier is used by dynamic SQL statements, the statements are executed using the associated connection. The namespace of the declaration is the precompile unit, and multiple declarations to the same SQL statement identifier are not allowed. Note that if the precompiler runs in Informix compatibility mode and some SQL statement is declared, "database" can not be used as a cursor name.

## Parameters

_`connection_name`_ [#](#ECPG-SQL-DECLARE-STATEMENT-CONNECTION-NAME)

A database connection name established by the `CONNECT` command.

AT clause can be omitted, but such statement has no meaning.

_`statement_name`_ [#](#ECPG-SQL-DECLARE-STATEMENT-STATEMENT-NAME)

The name of an SQL statement identifier, either as an SQL identifier or a host variable.

## Notes

This association is valid only if the declaration is physically placed on top of a dynamic statement.

## Examples

EXEC SQL CONNECT TO postgres AS con1;
EXEC SQL AT con1 DECLARE sql\_stmt STATEMENT;
EXEC SQL DECLARE cursor\_name CURSOR FOR sql\_stmt;
EXEC SQL PREPARE sql\_stmt FROM :dyn\_string;
EXEC SQL OPEN cursor\_name;
EXEC SQL FETCH cursor\_name INTO :column1;
EXEC SQL CLOSE cursor\_name;

## Compatibility

`DECLARE STATEMENT` is an extension of the SQL standard, but can be used in famous DBMSs.

