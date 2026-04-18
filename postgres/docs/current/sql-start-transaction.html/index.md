---
title: "PostgreSQL: Documentation: 18: START TRANSACTION"
source: "https://www.postgresql.org/docs/current/sql-start-transaction.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-start-transaction.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:57.803Z"
content_hash: "cc857a1bd99a6151a2e6fc2ce6a377cac83b9c80130dba1dfb60520430b55c39"
menu_path: ["PostgreSQL: Documentation: 18: START TRANSACTION"]
section_path: []
nav_prev: {"path": "postgres/docs/current/xfunc.html/index.md", "title": "PostgreSQL: Documentation: 18: 36.3.\u00a0User-Defined Functions"}
nav_next: {"path": "postgres/docs/current/sepgsql.html/index.md", "title": "PostgreSQL: Documentation: 18: F.40.\u00a0sepgsql \u2014 SELinux-, label-based mandatory access control (MAC) security module"}
---

START TRANSACTION — start a transaction block

## Synopsis

START TRANSACTION \[ _`transaction_mode`_ \[, ...\] \]

where _`transaction_mode`_ is one of:

    ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
    READ WRITE | READ ONLY
    \[ NOT \] DEFERRABLE

## Description

This command begins a new transaction block. If the isolation level, read/write mode, or deferrable mode is specified, the new transaction has those characteristics, as if [`SET TRANSACTION`](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") was executed. This is the same as the [`BEGIN`](https://www.postgresql.org/docs/current/sql-begin.html "BEGIN") command.

## Parameters

Refer to [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION") for information on the meaning of the parameters to this statement.

## Compatibility

In the standard, it is not necessary to issue `START TRANSACTION` to start a transaction block: any SQL command implicitly begins a block. PostgreSQL's behavior can be seen as implicitly issuing a `COMMIT` after each command that does not follow `START TRANSACTION` (or `BEGIN`), and it is therefore often called “autocommit”. Other relational database systems might offer an autocommit feature as a convenience.

The `DEFERRABLE` _`transaction_mode`_ is a PostgreSQL language extension.

The SQL standard requires commas between successive _`transaction_modes`_, but for historical reasons PostgreSQL allows the commas to be omitted.

See also the compatibility section of [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "SET TRANSACTION").

