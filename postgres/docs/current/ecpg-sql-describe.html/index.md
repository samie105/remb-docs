---
title: "PostgreSQL: Documentation: 18: DESCRIBE"
source: "https://www.postgresql.org/docs/current/ecpg-sql-describe.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-describe.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:01.493Z"
content_hash: "dc2f3531c0e017993acc335573461c44d13f968981898e1162a5e015ad55a6e1"
menu_path: ["PostgreSQL: Documentation: 18: DESCRIBE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ecpg-errors.html/index.md", "title": "PostgreSQL: Documentation: 18: 34.8.\u00a0Error Handling"}
nav_next: {"path": "postgres/docs/current/plpgsql-development-tips.html/index.md", "title": "PostgreSQL: Documentation: 18: 41.12.\u00a0Tips for Developing in PL/pgSQL"}
---

DESCRIBE — obtain information about a prepared statement or result set

## Synopsis

DESCRIBE \[ OUTPUT \] _`prepared_name`_ USING \[ SQL \] DESCRIPTOR _`descriptor_name`_
DESCRIBE \[ OUTPUT \] _`prepared_name`_ INTO \[ SQL \] DESCRIPTOR _`descriptor_name`_
DESCRIBE \[ OUTPUT \] _`prepared_name`_ INTO _`sqlda_name`_

## Description

`DESCRIBE` retrieves metadata information about the result columns contained in a prepared statement, without actually fetching a row.

## Parameters

_`prepared_name`_ [#](#ECPG-SQL-DESCRIBE-PREPARED-NAME)

The name of a prepared statement. This can be an SQL identifier or a host variable.

_`descriptor_name`_ [#](#ECPG-SQL-DESCRIBE-DESCRIPTOR-NAME)

A descriptor name. It is case sensitive. It can be an SQL identifier or a host variable.

_`sqlda_name`_ [#](#ECPG-SQL-DESCRIBE-SQLDA-NAME)

The name of an SQLDA variable.

## Examples

EXEC SQL ALLOCATE DESCRIPTOR mydesc;
EXEC SQL PREPARE stmt1 FROM :sql\_stmt;
EXEC SQL DESCRIBE stmt1 INTO SQL DESCRIPTOR mydesc;
EXEC SQL GET DESCRIPTOR mydesc VALUE 1 :charvar = NAME;
EXEC SQL DEALLOCATE DESCRIPTOR mydesc;

## Compatibility

`DESCRIBE` is specified in the SQL standard.


