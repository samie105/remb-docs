---
title: "PostgreSQL: Documentation: 18: SPI_gettype"
source: "https://www.postgresql.org/docs/current/spi-spi-gettype.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-gettype.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:53.098Z"
content_hash: "a3f9eac84733c761167dad700fbfe464dc1c770bb275d4ee3a2292ea0385c111"
menu_path: ["PostgreSQL: Documentation: 18: SPI_gettype"]
section_path: []
nav_prev: {"path": "postgres/docs/current/functions-logical.html/index.md", "title": "PostgreSQL: Documentation: 18: 9.1.\u00a0Logical Operators"}
nav_next: {"path": "postgres/docs/current/indexes-expressional.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.7.\u00a0Indexes on Expressions"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-gettype.html "PostgreSQL 18 - SPI_gettype") ([18](/docs/18/spi-spi-gettype.html "PostgreSQL 18 - SPI_gettype")) / [17](/docs/17/spi-spi-gettype.html "PostgreSQL 17 - SPI_gettype") / [16](/docs/16/spi-spi-gettype.html "PostgreSQL 16 - SPI_gettype") / [15](/docs/15/spi-spi-gettype.html "PostgreSQL 15 - SPI_gettype") / [14](/docs/14/spi-spi-gettype.html "PostgreSQL 14 - SPI_gettype")

Development Versions: [devel](/docs/devel/spi-spi-gettype.html "PostgreSQL devel - SPI_gettype")

Unsupported versions: [13](/docs/13/spi-spi-gettype.html "PostgreSQL 13 - SPI_gettype") / [12](/docs/12/spi-spi-gettype.html "PostgreSQL 12 - SPI_gettype") / [11](/docs/11/spi-spi-gettype.html "PostgreSQL 11 - SPI_gettype") / [10](/docs/10/spi-spi-gettype.html "PostgreSQL 10 - SPI_gettype") / [9.6](/docs/9.6/spi-spi-gettype.html "PostgreSQL 9.6 - SPI_gettype") / [9.5](/docs/9.5/spi-spi-gettype.html "PostgreSQL 9.5 - SPI_gettype") / [9.4](/docs/9.4/spi-spi-gettype.html "PostgreSQL 9.4 - SPI_gettype") / [9.3](/docs/9.3/spi-spi-gettype.html "PostgreSQL 9.3 - SPI_gettype") / [9.2](/docs/9.2/spi-spi-gettype.html "PostgreSQL 9.2 - SPI_gettype") / [9.1](/docs/9.1/spi-spi-gettype.html "PostgreSQL 9.1 - SPI_gettype") / [9.0](/docs/9.0/spi-spi-gettype.html "PostgreSQL 9.0 - SPI_gettype") / [8.4](/docs/8.4/spi-spi-gettype.html "PostgreSQL 8.4 - SPI_gettype") / [8.3](/docs/8.3/spi-spi-gettype.html "PostgreSQL 8.3 - SPI_gettype") / [8.2](/docs/8.2/spi-spi-gettype.html "PostgreSQL 8.2 - SPI_gettype") / [8.1](/docs/8.1/spi-spi-gettype.html "PostgreSQL 8.1 - SPI_gettype") / [8.0](/docs/8.0/spi-spi-gettype.html "PostgreSQL 8.0 - SPI_gettype") / [7.4](/docs/7.4/spi-spi-gettype.html "PostgreSQL 7.4 - SPI_gettype")

## SPI\_gettype

SPI\_gettype — return the data type name of the specified column

## Synopsis

char \* SPI\_gettype(TupleDesc _`rowdesc`_, int _`colnumber`_)

## Description

`SPI_gettype` returns a copy of the data type name of the specified column. (You can use `pfree` to release the copy of the name when you don't need it anymore.)

## Arguments

``TupleDesc _`rowdesc`_``

input row description

``int _`colnumber`_``

column number (count starts at 1)

## Return Value

The data type name of the specified column, or `NULL` on error. `SPI_result` is set to `SPI_ERROR_NOATTRIBUTE` on error.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-gettype.html/) to report a documentation issue.

