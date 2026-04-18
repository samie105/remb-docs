---
title: "PostgreSQL: Documentation: 18: BEGIN"
source: "https://www.postgresql.org/docs/current/sql-begin.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-begin.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:02.060Z"
content_hash: "214be7cb5a089cc18a75c5ad36cfaa6a423ab145621d0efa221ca1ed91277035"
menu_path: ["PostgreSQL: Documentation: 18: BEGIN"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-analyze.html/index.md", "title": "PostgreSQL: Documentation: 18: ANALYZE"}
nav_next: {"path": "postgres/docs/current/sql-call.html/index.md", "title": "PostgreSQL: Documentation: 18: CALL"}
---

BEGIN — start a transaction block

## Synopsis

BEGIN \[ WORK | TRANSACTION \] \[ _`transaction_mode`_ \[, ...\] \]

where _`transaction_mode`_ is one of:

    ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
    READ WRITE | READ ONLY
    \[ NOT \] DEFERRABLE

## Description

`BEGIN` initiates a transaction block, that is, all statements after a `BEGIN` command will be executed in a single transaction until an explicit [`COMMIT`](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT") or [`ROLLBACK`](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK") is given. By default (without `BEGIN`), PostgreSQL executes transactions in “autocommit” mode, that is, each statement is executed in its own transaction and a commit is implicitly performed at the end of the statement (if execution was successful, otherwise a rollback is done).

Statements are executed more quickly in a transaction block, because transaction start/commit requires significant CPU and disk activity. Execution of multiple statements inside a transaction is also useful to ensure consistency when making several related changes: other sessions will be unable to see the intermediate states wherein not all the related updates have been done.

If the isolation level, read/write mode, or deferrable mode is specified, the new transaction has those characteristics, as if [`SET TRANSACTION`](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") was executed.

## Parameters

`WORK`  
`TRANSACTION`

Optional key words. They have no effect.

Refer to [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for information on the meaning of the other parameters to this statement.

## Notes

[`START TRANSACTION`](https://www.postgresql.org/docs/current/sql-start-transaction.html "START TRANSACTION") has the same functionality as `BEGIN`.

Use [`COMMIT`](https://www.postgresql.org/docs/current/sql-commit.html "COMMIT") or [`ROLLBACK`](https://www.postgresql.org/docs/current/sql-rollback.html "ROLLBACK") to terminate a transaction block.

Issuing `BEGIN` when already inside a transaction block will provoke a warning message. The state of the transaction is not affected. To nest transactions within a transaction block, use savepoints (see [SAVEPOINT](https://www.postgresql.org/docs/current/sql-savepoint.html "SAVEPOINT")).

For reasons of backwards compatibility, the commas between successive _`transaction_modes`_ can be omitted.

## Examples

To begin a transaction block:

BEGIN;

## Compatibility

`BEGIN` is a PostgreSQL language extension. It is equivalent to the SQL-standard command [`START TRANSACTION`](https://www.postgresql.org/docs/current/sql-start-transaction.html "START TRANSACTION"), whose reference page contains additional compatibility information.

The `DEFERRABLE` _`transaction_mode`_ is a PostgreSQL language extension.

Incidentally, the `BEGIN` key word is used for a different purpose in embedded SQL. You are advised to be careful about the transaction semantics when porting database applications.
