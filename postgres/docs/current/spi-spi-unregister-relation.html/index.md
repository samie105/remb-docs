---
title: "PostgreSQL: Documentation: 18: SPI_unregister_relation"
source: "https://www.postgresql.org/docs/current/spi-spi-unregister-relation.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-unregister-relation.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:24.555Z"
content_hash: "216a9827dec2a8fb384fdf6bc5683bf485b9f2cd57eb4bc9b6b0b277dc8e2f41"
menu_path: ["PostgreSQL: Documentation: 18: SPI_unregister_relation"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ddl-depend.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.15.\u00a0Dependency Tracking"}
nav_next: {"path": "postgres/docs/current/event-trigger-interface.html/index.md", "title": "PostgreSQL: Documentation: 18: 38.2.\u00a0Writing Event Trigger Functions in C"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-unregister-relation.html "PostgreSQL 18 - SPI_unregister_relation") ([18](/docs/18/spi-spi-unregister-relation.html "PostgreSQL 18 - SPI_unregister_relation")) / [17](/docs/17/spi-spi-unregister-relation.html "PostgreSQL 17 - SPI_unregister_relation") / [16](/docs/16/spi-spi-unregister-relation.html "PostgreSQL 16 - SPI_unregister_relation") / [15](/docs/15/spi-spi-unregister-relation.html "PostgreSQL 15 - SPI_unregister_relation") / [14](/docs/14/spi-spi-unregister-relation.html "PostgreSQL 14 - SPI_unregister_relation")

Development Versions: [devel](/docs/devel/spi-spi-unregister-relation.html "PostgreSQL devel - SPI_unregister_relation")

Unsupported versions: [13](/docs/13/spi-spi-unregister-relation.html "PostgreSQL 13 - SPI_unregister_relation") / [12](/docs/12/spi-spi-unregister-relation.html "PostgreSQL 12 - SPI_unregister_relation") / [11](/docs/11/spi-spi-unregister-relation.html "PostgreSQL 11 - SPI_unregister_relation") / [10](/docs/10/spi-spi-unregister-relation.html "PostgreSQL 10 - SPI_unregister_relation")

## SPI\_unregister\_relation

SPI\_unregister\_relation — remove an ephemeral named relation from the registry

## Synopsis

int SPI\_unregister\_relation(const char \* _`name`_)

## Description

`SPI_unregister_relation` removes an ephemeral named relation from the registry for the current connection.

## Arguments

``const char * _`name`_``

the relation registry entry name

## Return Value

If the execution of the command was successful then the following (nonnegative) value will be returned:

`SPI_OK_REL_UNREGISTER`

if the tuplestore has been successfully removed from the registry

On error, one of the following negative values is returned:

`SPI_ERROR_ARGUMENT`

if _`name`_ is `NULL`

`SPI_ERROR_UNCONNECTED`

if called from an unconnected C function

`SPI_ERROR_REL_NOT_FOUND`

if _`name`_ is not found in the registry for the current connection

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-unregister-relation.html/) to report a documentation issue.


