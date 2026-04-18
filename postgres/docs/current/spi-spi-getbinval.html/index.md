---
title: "PostgreSQL: Documentation: 18: SPI_getbinval"
source: "https://www.postgresql.org/docs/current/spi-spi-getbinval.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-getbinval.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:02.181Z"
content_hash: "9f46ebb79d80876ad4aaaedc3b2dbd08628f3a8c5555662efcebf7a902028c0a"
menu_path: ["PostgreSQL: Documentation: 18: SPI_getbinval"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-wait-events.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.38.\u00a0pg_wait_events"}
nav_next: {"path": "postgres/docs/current/pgbuffercache.html/index.md", "title": "PostgreSQL: Documentation: 18: F.25.\u00a0pg_buffercache \u2014 inspect PostgreSQL buffer cache state"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-getbinval.html "PostgreSQL 18 - SPI_getbinval") ([18](/docs/18/spi-spi-getbinval.html "PostgreSQL 18 - SPI_getbinval")) / [17](/docs/17/spi-spi-getbinval.html "PostgreSQL 17 - SPI_getbinval") / [16](/docs/16/spi-spi-getbinval.html "PostgreSQL 16 - SPI_getbinval") / [15](/docs/15/spi-spi-getbinval.html "PostgreSQL 15 - SPI_getbinval") / [14](/docs/14/spi-spi-getbinval.html "PostgreSQL 14 - SPI_getbinval")

Development Versions: [devel](/docs/devel/spi-spi-getbinval.html "PostgreSQL devel - SPI_getbinval")

Unsupported versions: [13](/docs/13/spi-spi-getbinval.html "PostgreSQL 13 - SPI_getbinval") / [12](/docs/12/spi-spi-getbinval.html "PostgreSQL 12 - SPI_getbinval") / [11](/docs/11/spi-spi-getbinval.html "PostgreSQL 11 - SPI_getbinval") / [10](/docs/10/spi-spi-getbinval.html "PostgreSQL 10 - SPI_getbinval") / [9.6](/docs/9.6/spi-spi-getbinval.html "PostgreSQL 9.6 - SPI_getbinval") / [9.5](/docs/9.5/spi-spi-getbinval.html "PostgreSQL 9.5 - SPI_getbinval") / [9.4](/docs/9.4/spi-spi-getbinval.html "PostgreSQL 9.4 - SPI_getbinval") / [9.3](/docs/9.3/spi-spi-getbinval.html "PostgreSQL 9.3 - SPI_getbinval") / [9.2](/docs/9.2/spi-spi-getbinval.html "PostgreSQL 9.2 - SPI_getbinval") / [9.1](/docs/9.1/spi-spi-getbinval.html "PostgreSQL 9.1 - SPI_getbinval") / [9.0](/docs/9.0/spi-spi-getbinval.html "PostgreSQL 9.0 - SPI_getbinval") / [8.4](/docs/8.4/spi-spi-getbinval.html "PostgreSQL 8.4 - SPI_getbinval") / [8.3](/docs/8.3/spi-spi-getbinval.html "PostgreSQL 8.3 - SPI_getbinval") / [8.2](/docs/8.2/spi-spi-getbinval.html "PostgreSQL 8.2 - SPI_getbinval") / [8.1](/docs/8.1/spi-spi-getbinval.html "PostgreSQL 8.1 - SPI_getbinval") / [8.0](/docs/8.0/spi-spi-getbinval.html "PostgreSQL 8.0 - SPI_getbinval") / [7.4](/docs/7.4/spi-spi-getbinval.html "PostgreSQL 7.4 - SPI_getbinval")

## SPI\_getbinval

SPI\_getbinval — return the binary value of the specified column

## Synopsis

Datum SPI\_getbinval(HeapTuple _`row`_, TupleDesc _`rowdesc`_, int _`colnumber`_,
                    bool \* _`isnull`_)

## Description

`SPI_getbinval` returns the value of the specified column in the internal form (as type `Datum`).

This function does not allocate new space for the datum. In the case of a pass-by-reference data type, the return value will be a pointer into the passed row.

## Arguments

``HeapTuple _`row`_``

input row to be examined

``TupleDesc _`rowdesc`_``

input row description

``int _`colnumber`_``

column number (count starts at 1)

``bool * _`isnull`_``

flag for a null value in the column

## Return Value

The binary value of the column is returned. The variable pointed to by _`isnull`_ is set to true if the column is null, else to false.

`SPI_result` is set to `SPI_ERROR_NOATTRIBUTE` on error.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-getbinval.html/) to report a documentation issue.
