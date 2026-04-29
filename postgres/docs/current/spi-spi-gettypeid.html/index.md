---
title: "PostgreSQL: Documentation: 18: SPI_gettypeid"
source: "https://www.postgresql.org/docs/current/spi-spi-gettypeid.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-gettypeid.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:06.797Z"
content_hash: "a68634ac5ec876029e7b597646bb5ab24fbed6ec116981375175b198c185e025"
menu_path: ["PostgreSQL: Documentation: 18: SPI_gettypeid"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-gettype.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_gettype"}
nav_next: {"path": "postgres/docs/current/spi-spi-getvalue.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getvalue"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-gettypeid.html "PostgreSQL 18 - SPI_gettypeid") ([18](/docs/18/spi-spi-gettypeid.html "PostgreSQL 18 - SPI_gettypeid")) / [17](/docs/17/spi-spi-gettypeid.html "PostgreSQL 17 - SPI_gettypeid") / [16](/docs/16/spi-spi-gettypeid.html "PostgreSQL 16 - SPI_gettypeid") / [15](/docs/15/spi-spi-gettypeid.html "PostgreSQL 15 - SPI_gettypeid") / [14](/docs/14/spi-spi-gettypeid.html "PostgreSQL 14 - SPI_gettypeid")

Development Versions: [devel](/docs/devel/spi-spi-gettypeid.html "PostgreSQL devel - SPI_gettypeid")

Unsupported versions: [13](/docs/13/spi-spi-gettypeid.html "PostgreSQL 13 - SPI_gettypeid") / [12](/docs/12/spi-spi-gettypeid.html "PostgreSQL 12 - SPI_gettypeid") / [11](/docs/11/spi-spi-gettypeid.html "PostgreSQL 11 - SPI_gettypeid") / [10](/docs/10/spi-spi-gettypeid.html "PostgreSQL 10 - SPI_gettypeid") / [9.6](/docs/9.6/spi-spi-gettypeid.html "PostgreSQL 9.6 - SPI_gettypeid") / [9.5](/docs/9.5/spi-spi-gettypeid.html "PostgreSQL 9.5 - SPI_gettypeid") / [9.4](/docs/9.4/spi-spi-gettypeid.html "PostgreSQL 9.4 - SPI_gettypeid") / [9.3](/docs/9.3/spi-spi-gettypeid.html "PostgreSQL 9.3 - SPI_gettypeid") / [9.2](/docs/9.2/spi-spi-gettypeid.html "PostgreSQL 9.2 - SPI_gettypeid") / [9.1](/docs/9.1/spi-spi-gettypeid.html "PostgreSQL 9.1 - SPI_gettypeid") / [9.0](/docs/9.0/spi-spi-gettypeid.html "PostgreSQL 9.0 - SPI_gettypeid") / [8.4](/docs/8.4/spi-spi-gettypeid.html "PostgreSQL 8.4 - SPI_gettypeid") / [8.3](/docs/8.3/spi-spi-gettypeid.html "PostgreSQL 8.3 - SPI_gettypeid") / [8.2](/docs/8.2/spi-spi-gettypeid.html "PostgreSQL 8.2 - SPI_gettypeid") / [8.1](/docs/8.1/spi-spi-gettypeid.html "PostgreSQL 8.1 - SPI_gettypeid") / [8.0](/docs/8.0/spi-spi-gettypeid.html "PostgreSQL 8.0 - SPI_gettypeid") / [7.4](/docs/7.4/spi-spi-gettypeid.html "PostgreSQL 7.4 - SPI_gettypeid")

## SPI\_gettypeid

SPI\_gettypeid — return the data type OID of the specified column

## Synopsis

Oid SPI\_gettypeid(TupleDesc _`rowdesc`_, int _`colnumber`_)

## Description

`SPI_gettypeid` returns the OID of the data type of the specified column.

## Arguments

``TupleDesc _`rowdesc`_``

input row description

``int _`colnumber`_``

column number (count starts at 1)

## Return Value

The OID of the data type of the specified column or `InvalidOid` on error. On error, `SPI_result` is set to `SPI_ERROR_NOATTRIBUTE`.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-gettypeid.html/) to report a documentation issue.
