---
title: "PostgreSQL: Documentation: 18: COMMIT"
source: "https://www.postgresql.org/docs/current/sql-commit.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-commit.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:57.807Z"
content_hash: "fa84b8a3dcdb8858aae04e872c2f1161b1c87cebfc7a53563c85786fe4dfe4ee"
menu_path: ["PostgreSQL: Documentation: 18: COMMIT"]
section_path: []
nav_prev: {"path": "postgres/docs/current/infoschema-role-routine-grants.html/index.md", "title": "PostgreSQL: Documentation: 18: 35.36.\u00a0role_routine_grants"}
nav_next: {"path": "postgres/docs/current/indexes-unique.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.6.\u00a0Unique Indexes"}
---

COMMIT — commit the current transaction

## Synopsis

COMMIT \[ WORK | TRANSACTION \] \[ AND \[ NO \] CHAIN \]

## Description

`COMMIT` commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs.

## Parameters

`WORK`  
`TRANSACTION` [#](#SQL-COMMIT-TRANSACTION)

Optional key words. They have no effect.

`AND CHAIN` [#](#SQL-COMMIT-CHAIN)

If `AND CHAIN` is specified, a new transaction is immediately started with the same transaction characteristics (see [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION")) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use [ROLLBACK](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK") to abort a transaction.

Issuing `COMMIT` when not inside a transaction does no harm, but it will provoke a warning message. `COMMIT AND CHAIN` when not inside a transaction is an error.

## Examples

To commit the current transaction and make all changes permanent:

COMMIT;

## Compatibility

The command `COMMIT` conforms to the SQL standard. The form `COMMIT TRANSACTION` is a PostgreSQL extension.
