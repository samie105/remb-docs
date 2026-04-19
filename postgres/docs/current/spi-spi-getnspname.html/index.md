---
title: "PostgreSQL: Documentation: 18: SPI_getnspname"
source: "https://www.postgresql.org/docs/current/spi-spi-getnspname.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-getnspname.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:00.750Z"
content_hash: "9bacc6fd175664c917d9590d0336d55d85c813bc8d8894e2dd19555a786bdcf5"
menu_path: ["PostgreSQL: Documentation: 18: SPI_getnspname"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-spi-getbinval.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getbinval"}
nav_next: {"path": "postgres/docs/current/spi-spi-getrelname.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getrelname"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/spi-spi-getnspname.html "PostgreSQL devel - SPI_getnspname")

SPI\_getnspname

[Prev](https://www.postgresql.org/docs/current/spi-spi-getrelname.html "SPI_getrelname") 

[Up](https://www.postgresql.org/docs/current/spi-interface-support.html "45.2. Interface Support Functions")

45.2. Interface Support Functions

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 [Next](https://www.postgresql.org/docs/current/spi-spi-result-code-string.html "SPI_result_code_string")

* * *

SPI\_getnspname — return the namespace of the specified relation

## Synopsis

char \* SPI\_getnspname(Relation _`rel`_)

## Description

`SPI_getnspname` returns a copy of the name of the namespace that the specified `Relation` belongs to. This is equivalent to the relation's schema. You should `pfree` the return value of this function when you are finished with it.

## Arguments

``Relation _`rel`_``

input relation

## Return Value

The name of the specified relation's namespace.

* * *

[Prev](https://www.postgresql.org/docs/current/spi-spi-getrelname.html "SPI_getrelname") 

[Up](https://www.postgresql.org/docs/current/spi-interface-support.html "45.2. Interface Support Functions")

 [Next](https://www.postgresql.org/docs/current/spi-spi-result-code-string.html "SPI_result_code_string")

SPI\_getrelname 

[Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation")

 SPI\_result\_code\_string
