---
title: "PostgreSQL: Documentation: 18: CLOSE"
source: "https://www.postgresql.org/docs/current/sql-close.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-close.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:50:59.914Z"
content_hash: "97a6249927cf873845d27b0826f426957ffc809a15bb2f7758f8781c363b07f0"
menu_path: ["PostgreSQL: Documentation: 18: CLOSE"]
section_path: []
content_language: "en"
nav_prev: {"path": "../sql-checkpoint.html/index.md", "title": "PostgreSQL: Documentation: 18: CHECKPOINT"}
nav_next: {"path": "../sql-cluster.html/index.md", "title": "PostgreSQL: Documentation: 18: CLUSTER"}
---

## Synopsis

CLOSE { _`name`_ | ALL }

## Description

`CLOSE` frees the resources associated with an open cursor. After the cursor is closed, no subsequent operations are allowed on it. A cursor should be closed when it is no longer needed.

Every non-holdable open cursor is implicitly closed when a transaction is terminated by `COMMIT` or `ROLLBACK`. A holdable cursor is implicitly closed if the transaction that created it aborts via `ROLLBACK`. If the creating transaction successfully commits, the holdable cursor remains open until an explicit `CLOSE` is executed, or the client disconnects.

## Parameters

_`name`_

The name of an open cursor to close.

`ALL`

Close all open cursors.

## Notes

PostgreSQL does not have an explicit `OPEN` cursor statement; a cursor is considered open when it is declared. Use the [`DECLARE`](https://www.postgresql.org/docs/current/sql-declare.html "DECLARE") statement to declare a cursor.

You can see all available cursors by querying the [`pg_cursors`](https://www.postgresql.org/docs/current/view-pg-cursors.html "53.7. pg_cursors") system view.

If a cursor is closed after a savepoint which is later rolled back, the `CLOSE` is not rolled back; that is, the cursor remains closed.

## Examples

Close the cursor `liahona`:

CLOSE liahona;

## Compatibility

`CLOSE` is fully conforming with the SQL standard. `CLOSE ALL` is a PostgreSQL extension.
