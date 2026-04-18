---
title: "PostgreSQL: Documentation: 18: END"
source: "https://www.postgresql.org/docs/current/sql-end.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-end.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:07.995Z"
content_hash: "312f07091bbc44302542b785ad6c30963a91c2a4bdc908a7eddf7d55de0d7024"
menu_path: ["PostgreSQL: Documentation: 18: END"]
section_path: []
nav_prev: {"path": "postgres/docs/current/lo-funcs.html/index.md", "title": "PostgreSQL: Documentation: 18: 33.4.\u00a0Server-Side Functions"}
nav_next: {"path": "postgres/docs/current/bki-format.html/index.md", "title": "PostgreSQL: Documentation: 18: 68.3.\u00a0BKI File Format"}
---

END — commit the current transaction

## Synopsis

END \[ WORK | TRANSACTION \] \[ AND \[ NO \] CHAIN \]

## Description

`END` commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs. This command is a PostgreSQL extension that is equivalent to [`COMMIT`](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT").

## Parameters

`WORK`  
`TRANSACTION`

Optional key words. They have no effect.

`AND CHAIN`

If `AND CHAIN` is specified, a new transaction is immediately started with the same transaction characteristics (see [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION")) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use [`ROLLBACK`](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK") to abort a transaction.

Issuing `END` when not inside a transaction does no harm, but it will provoke a warning message.

## Examples

To commit the current transaction and make all changes permanent:

END;

## Compatibility

`END` is a PostgreSQL extension that provides functionality equivalent to [`COMMIT`](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT"), which is specified in the SQL standard.


