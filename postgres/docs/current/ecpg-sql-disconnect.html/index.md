---
title: "PostgreSQL: Documentation: 18: DISCONNECT"
source: "https://www.postgresql.org/docs/current/ecpg-sql-disconnect.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-disconnect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:41.068Z"
content_hash: "b5dd51b5c0fa1d57a181676decfb299d164f20b8c970225b4b64e10a3e5f37e8"
menu_path: ["PostgreSQL: Documentation: 18: DISCONNECT"]
section_path: []
nav_prev: {"path": "postgres/docs/current/progress-reporting.html/index.md", "title": "PostgreSQL: Documentation: 18: 27.4.\u00a0Progress Reporting"}
nav_next: {"path": "postgres/docs/current/view-pg-replication-origin-status.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.19.\u00a0pg_replication_origin_status"}
---

DISCONNECT — terminate a database connection

## Synopsis

DISCONNECT _`connection_name`_
DISCONNECT \[ CURRENT \]
DISCONNECT ALL

## Description

`DISCONNECT` closes a connection (or all connections) to the database.

## Parameters

_`connection_name`_ [#](#ECPG-SQL-DISCONNECT-CONNECTION-NAME)

A database connection name established by the `CONNECT` command.

`CURRENT` [#](#ECPG-SQL-DISCONNECT-CURRENT)

Close the “current” connection, which is either the most recently opened connection, or the connection set by the `SET CONNECTION` command. This is also the default if no argument is given to the `DISCONNECT` command.

`ALL` [#](#ECPG-SQL-DISCONNECT-ALL)

Close all open connections.

## Examples

int
main(void)
{
    EXEC SQL CONNECT TO testdb AS con1 USER testuser;
    EXEC SQL CONNECT TO testdb AS con2 USER testuser;
    EXEC SQL CONNECT TO testdb AS con3 USER testuser;

    EXEC SQL DISCONNECT CURRENT;  /\* close con3          \*/
    EXEC SQL DISCONNECT ALL;      /\* close con2 and con1 \*/

    return 0;
}

## Compatibility

`DISCONNECT` is specified in the SQL standard.


