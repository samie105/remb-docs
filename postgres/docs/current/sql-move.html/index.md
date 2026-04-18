---
title: "PostgreSQL: Documentation: 18: MOVE"
source: "https://www.postgresql.org/docs/current/sql-move.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-move.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:18.117Z"
content_hash: "60d76d642ddd5deca55cf2f0f1ca4bb05e2615a8e252cf4b7c295e4a2e07cc9b"
menu_path: ["PostgreSQL: Documentation: 18: MOVE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ddl-others.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.14.\u00a0Other Database Objects"}
nav_next: {"path": "postgres/docs/current/xaggr.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.12.\u00a0User-Defined Aggregates"}
---

MOVE — position a cursor

## Synopsis

MOVE \[ _`direction`_ \] \[ FROM | IN \] _`cursor_name`_

where _`direction`_ can be one of:

    NEXT
    PRIOR
    FIRST
    LAST
    ABSOLUTE _`count`_
    RELATIVE _`count`_
    _`count`_
    ALL
    FORWARD
    FORWARD _`count`_
    FORWARD ALL
    BACKWARD
    BACKWARD _`count`_
    BACKWARD ALL

## Description

`MOVE` repositions a cursor without retrieving any data. `MOVE` works exactly like the `FETCH` command, except it only positions the cursor and does not return rows.

The parameters for the `MOVE` command are identical to those of the `FETCH` command; refer to [FETCH](https://www.postgresql.org/docs/current/sql-fetch.html "FETCH") for details on syntax and usage.

## Outputs

On successful completion, a `MOVE` command returns a command tag of the form

MOVE _`count`_

The _`count`_ is the number of rows that a `FETCH` command with the same parameters would have returned (possibly zero).

## Examples

BEGIN WORK;
DECLARE liahona CURSOR FOR SELECT \* FROM films;

-- Skip the first 5 rows:
MOVE FORWARD 5 IN liahona;
MOVE 5

-- Fetch the 6th row from the cursor liahona:
FETCH 1 FROM liahona;
 code  | title  | did | date\_prod  |  kind  |  len
-------+--------+-----+------------+--------+-------
 P\_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
(1 row)

-- Close the cursor liahona and end the transaction:
CLOSE liahona;
COMMIT WORK;

## Compatibility

There is no `MOVE` statement in the SQL standard.


