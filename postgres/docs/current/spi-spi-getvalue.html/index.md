---
title: "PostgreSQL: Documentation: 18: SPI_getvalue"
source: "https://www.postgresql.org/docs/current/spi-spi-getvalue.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-getvalue.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:37.946Z"
content_hash: "dbe8cb32b389c249d4dca9ed4af7cdc3fa94127f6a870221f82a19d6108c3ee1"
menu_path: ["PostgreSQL: Documentation: 18: SPI_getvalue"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-gettypeid.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_gettypeid"}
nav_next: {"path": "postgres/docs/current/spi-spi-register-relation.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_register_relation"}
---

SPI\_getvalue — return the string value of the specified column

## Synopsis

char \* SPI\_getvalue(HeapTuple _`row`_, TupleDesc _`rowdesc`_, int _`colnumber`_)

## Description

`SPI_getvalue` returns the string representation of the value of the specified column.

The result is returned in memory allocated using `palloc`. (You can use `pfree` to release the memory when you don't need it anymore.)

## Arguments

``HeapTuple _`row`_``

input row to be examined

``TupleDesc _`rowdesc`_``

input row description

``int _`colnumber`_``

column number (count starts at 1)

## Return Value

Column value, or `NULL` if the column is null, _`colnumber`_ is out of range (`SPI_result` is set to `SPI_ERROR_NOATTRIBUTE`), or no output function is available (`SPI_result` is set to `SPI_ERROR_NOOUTFUNC`).
