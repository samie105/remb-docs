---
title: "PostgreSQL: Documentation: 18: SPI_getnspname"
source: "https://www.postgresql.org/docs/current/spi-spi-getnspname.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-getnspname.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:37.757Z"
content_hash: "c73ff1563b4ea86f64f4283cf5043bd4fd42360f1b308c7192eeb7c57a05d81d"
menu_path: ["PostgreSQL: Documentation: 18: SPI_getnspname"]
section_path: []
content_language: "en"
nav_prev: {"path": "../spi-spi-getbinval.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getbinval"}
nav_next: {"path": "../spi-spi-getrelname.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_getrelname"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/spi-spi-getnspname.html "PostgreSQL devel - SPI_getnspname")

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

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](https://www.postgresql.org/account/comments/new/18/spi-spi-getnspname.html/) to report a documentation issue.
