---
title: "PostgreSQL: Documentation: 18: SPI_start_transaction"
source: "https://www.postgresql.org/docs/current/spi-spi-start-transaction.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-start-transaction.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:24.161Z"
content_hash: "e7bdd36be66d9c16679863b13a44af71dd206ba937a94017d4d627854eb746a4"
menu_path: ["PostgreSQL: Documentation: 18: SPI_start_transaction"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-truncate.html/index.md", "title": "PostgreSQL: Documentation: 18: TRUNCATE"}
nav_next: {"path": "postgres/docs/current/sql-droptsdictionary.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP TEXT SEARCH DICTIONARY"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/spi-spi-start-transaction.html "PostgreSQL devel - SPI_start_transaction")

Unsupported versions: [13](https://www.postgresql.org/docs/13/spi-spi-start-transaction.html "PostgreSQL 13 - SPI_start_transaction") / [12](https://www.postgresql.org/docs/12/spi-spi-start-transaction.html "PostgreSQL 12 - SPI_start_transaction") / [11](https://www.postgresql.org/docs/11/spi-spi-start-transaction.html "PostgreSQL 11 - SPI_start_transaction")

SPI\_start\_transaction

[Prev](https://www.postgresql.org/docs/current/spi-spi-rollback.html "SPI_rollback") 

[Up](https://www.postgresql.org/docs/current/spi-transaction.html "45.4. Transaction Management")

45.4. Transaction Management

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/spi-visibility.html "45.5. Visibility of Data Changes")

* * *

SPI\_start\_transaction — obsolete function

## Synopsis

void SPI\_start\_transaction(void)

## Description

`SPI_start_transaction` does nothing, and exists only for code compatibility with earlier PostgreSQL releases. It used to be required after calling `SPI_commit` or `SPI_rollback`, but now those functions start a new transaction automatically.

* * *

[Prev](https://www.postgresql.org/docs/current/spi-spi-rollback.html "SPI_rollback") 

[Up](https://www.postgresql.org/docs/current/spi-transaction.html "45.4. Transaction Management")

 [Next](https://www.postgresql.org/docs/current/spi-visibility.html "45.5. Visibility of Data Changes")

SPI\_rollback 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 45.5. Visibility of Data Changes

