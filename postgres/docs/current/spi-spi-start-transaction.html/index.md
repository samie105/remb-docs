---
title: "PostgreSQL: Documentation: 18: SPI_start_transaction"
source: "https://www.postgresql.org/docs/current/spi-spi-start-transaction.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-start-transaction.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:04.398Z"
content_hash: "8b8f95d1fb935135b75a7e89a15f75de1ca1eae48c3f712bdc5d814edefda3c1"
menu_path: ["PostgreSQL: Documentation: 18: SPI_start_transaction"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/spi-spi-start-transaction.html "PostgreSQL devel - SPI_start_transaction")

Unsupported versions: [13](https://www.postgresql.org/docs/13/spi-spi-start-transaction.html "PostgreSQL 13 - SPI_start_transaction") / [12](https://www.postgresql.org/docs/12/spi-spi-start-transaction.html "PostgreSQL 12 - SPI_start_transaction") / [11](https://www.postgresql.org/docs/11/spi-spi-start-transaction.html "PostgreSQL 11 - SPI_start_transaction")

SPI\_start\_transaction — obsolete function

## Synopsis

void SPI\_start\_transaction(void)

## Description

`SPI_start_transaction` does nothing, and exists only for code compatibility with earlier PostgreSQL releases. It used to be required after calling `SPI_commit` or `SPI_rollback`, but now those functions start a new transaction automatically.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](https://www.postgresql.org/account/comments/new/18/spi-spi-start-transaction.html/) to report a documentation issue.
