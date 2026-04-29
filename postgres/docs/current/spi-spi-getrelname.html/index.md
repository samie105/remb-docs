---
title: "PostgreSQL: Documentation: 18: SPI_getrelname"
source: "https://www.postgresql.org/docs/current/spi-spi-getrelname.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-getrelname.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:41.412Z"
content_hash: "df3b528a705c7a37f78e75c281ecb00434db4dab0730c9e0c85dad82934ae602"
menu_path: ["PostgreSQL: Documentation: 18: SPI_getrelname"]
section_path: []
nav_prev: {"path": "../spi-spi-getnspname.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getnspname"}
nav_next: {"path": "../spi-spi-gettype.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_gettype"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-getrelname.html "PostgreSQL 18 - SPI_getrelname") ([18](/docs/18/spi-spi-getrelname.html "PostgreSQL 18 - SPI_getrelname")) / [17](/docs/17/spi-spi-getrelname.html "PostgreSQL 17 - SPI_getrelname") / [16](/docs/16/spi-spi-getrelname.html "PostgreSQL 16 - SPI_getrelname") / [15](/docs/15/spi-spi-getrelname.html "PostgreSQL 15 - SPI_getrelname") / [14](/docs/14/spi-spi-getrelname.html "PostgreSQL 14 - SPI_getrelname")

Development Versions: [devel](/docs/devel/spi-spi-getrelname.html "PostgreSQL devel - SPI_getrelname")

Unsupported versions: [13](/docs/13/spi-spi-getrelname.html "PostgreSQL 13 - SPI_getrelname") / [12](/docs/12/spi-spi-getrelname.html "PostgreSQL 12 - SPI_getrelname") / [11](/docs/11/spi-spi-getrelname.html "PostgreSQL 11 - SPI_getrelname") / [10](/docs/10/spi-spi-getrelname.html "PostgreSQL 10 - SPI_getrelname") / [9.6](/docs/9.6/spi-spi-getrelname.html "PostgreSQL 9.6 - SPI_getrelname") / [9.5](/docs/9.5/spi-spi-getrelname.html "PostgreSQL 9.5 - SPI_getrelname") / [9.4](/docs/9.4/spi-spi-getrelname.html "PostgreSQL 9.4 - SPI_getrelname") / [9.3](/docs/9.3/spi-spi-getrelname.html "PostgreSQL 9.3 - SPI_getrelname") / [9.2](/docs/9.2/spi-spi-getrelname.html "PostgreSQL 9.2 - SPI_getrelname") / [9.1](/docs/9.1/spi-spi-getrelname.html "PostgreSQL 9.1 - SPI_getrelname") / [9.0](/docs/9.0/spi-spi-getrelname.html "PostgreSQL 9.0 - SPI_getrelname") / [8.4](/docs/8.4/spi-spi-getrelname.html "PostgreSQL 8.4 - SPI_getrelname") / [8.3](/docs/8.3/spi-spi-getrelname.html "PostgreSQL 8.3 - SPI_getrelname") / [8.2](/docs/8.2/spi-spi-getrelname.html "PostgreSQL 8.2 - SPI_getrelname") / [8.1](/docs/8.1/spi-spi-getrelname.html "PostgreSQL 8.1 - SPI_getrelname") / [8.0](/docs/8.0/spi-spi-getrelname.html "PostgreSQL 8.0 - SPI_getrelname") / [7.4](/docs/7.4/spi-spi-getrelname.html "PostgreSQL 7.4 - SPI_getrelname")

## SPI\_getrelname

SPI\_getrelname — return the name of the specified relation

## Synopsis

char \* SPI\_getrelname(Relation _`rel`_)

## Description

`SPI_getrelname` returns a copy of the name of the specified relation. (You can use `pfree` to release the copy of the name when you don't need it anymore.)

## Arguments

``Relation _`rel`_``

input relation

## Return Value

The name of the specified relation.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-getrelname.html/) to report a documentation issue.
