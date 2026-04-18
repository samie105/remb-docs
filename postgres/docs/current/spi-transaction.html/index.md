---
title: "PostgreSQL: Documentation: 18: 45.4. Transaction Management"
source: "https://www.postgresql.org/docs/current/spi-transaction.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-transaction.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:41.938Z"
content_hash: "089b403bb76bd554b683fb15f8c7414b23bf1142d894c283fe917a63bcfc355d"
menu_path: ["PostgreSQL: Documentation: 18: 45.4. Transaction Management"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-createsequence.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE SEQUENCE"}
nav_next: {"path": "postgres/docs/current/app-dropdb.html/index.md", "title": "PostgreSQL: Documentation: 18: dropdb"}
---

It is not possible to run transaction control commands such as `COMMIT` and `ROLLBACK` through SPI functions such as `SPI_execute`. There are, however, separate interface functions that allow transaction control through SPI.

It is not generally safe and sensible to start and end transactions in arbitrary user-defined SQL-callable functions without taking into account the context in which they are called. For example, a transaction boundary in the middle of a function that is part of a complex SQL expression that is part of some SQL command will probably result in obscure internal errors or crashes. The interface functions presented here are primarily intended to be used by procedural language implementations to support transaction management in SQL-level procedures that are invoked by the `CALL` command, taking the context of the `CALL` invocation into account. SPI-using procedures implemented in C can implement the same logic, but the details of that are beyond the scope of this documentation.


