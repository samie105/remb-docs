---
title: "PostgreSQL: Documentation: 18: COMMIT PREPARED"
source: "https://www.postgresql.org/docs/current/sql-commit-prepared.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-commit-prepared.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:18.158Z"
content_hash: "752607b861cade7bd5c8ede38744af9a147476c24e6d18e1776a99092580ca50"
menu_path: ["PostgreSQL: Documentation: 18: COMMIT PREPARED"]
section_path: []
nav_prev: {"path": "../sql-comment.html/index.md", "title": "PostgreSQL: Documentation: 18: COMMENT"}
nav_next: {"path": "../sql-commit.html/index.md", "title": "PostgreSQL: Documentation: 18: COMMIT"}
---

COMMIT PREPARED — commit a transaction that was earlier prepared for two-phase commit

## Synopsis

COMMIT PREPARED _`transaction_id`_

## Description

`COMMIT PREPARED` commits a transaction that is in prepared state.

## Parameters

_`transaction_id`_

The transaction identifier of the transaction that is to be committed.

## Notes

To commit a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction.

This command cannot be executed inside a transaction block. The prepared transaction is committed immediately.

All currently available prepared transactions are listed in the [`pg_prepared_xacts`](https://www.postgresql.org/docs/current/view-pg-prepared-xacts.html "53.17. pg_prepared_xacts") system view.

## Examples

Commit the transaction identified by the transaction identifier `foobar`:

COMMIT PREPARED 'foobar';

## Compatibility

`COMMIT PREPARED` is a PostgreSQL extension. It is intended for use by external transaction management systems, some of which are covered by standards (such as X/Open XA), but the SQL side of those systems is not standardized.
