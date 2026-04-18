---
title: "PostgreSQL: Documentation: 18: SPI_register_relation"
source: "https://www.postgresql.org/docs/current/spi-spi-register-relation.html"
canonical_url: "https://www.postgresql.org/docs/current/spi-spi-register-relation.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:00.556Z"
content_hash: "519d00ea16a6a3659643caa8998caf0f17b2dbd9502462d58330d7cd87fbd676"
menu_path: ["PostgreSQL: Documentation: 18: SPI_register_relation"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-set-role.html/index.md", "title": "PostgreSQL: Documentation: 18: SET ROLE"}
nav_next: {"path": "postgres/docs/current/runtime-config-preset.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.15.\u00a0Preset Options"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/spi-spi-register-relation.html "PostgreSQL 18 - SPI_register_relation") ([18](/docs/18/spi-spi-register-relation.html "PostgreSQL 18 - SPI_register_relation")) / [17](/docs/17/spi-spi-register-relation.html "PostgreSQL 17 - SPI_register_relation") / [16](/docs/16/spi-spi-register-relation.html "PostgreSQL 16 - SPI_register_relation") / [15](/docs/15/spi-spi-register-relation.html "PostgreSQL 15 - SPI_register_relation") / [14](/docs/14/spi-spi-register-relation.html "PostgreSQL 14 - SPI_register_relation")

Development Versions: [devel](/docs/devel/spi-spi-register-relation.html "PostgreSQL devel - SPI_register_relation")

Unsupported versions: [13](/docs/13/spi-spi-register-relation.html "PostgreSQL 13 - SPI_register_relation") / [12](/docs/12/spi-spi-register-relation.html "PostgreSQL 12 - SPI_register_relation") / [11](/docs/11/spi-spi-register-relation.html "PostgreSQL 11 - SPI_register_relation") / [10](/docs/10/spi-spi-register-relation.html "PostgreSQL 10 - SPI_register_relation")

## SPI\_register\_relation

SPI\_register\_relation — make an ephemeral named relation available by name in SPI queries

## Synopsis

int SPI\_register\_relation(EphemeralNamedRelation _`enr`_)

## Description

`SPI_register_relation` makes an ephemeral named relation, with associated information, available to queries planned and executed through the current SPI connection.

## Arguments

``EphemeralNamedRelation _`enr`_``

the ephemeral named relation registry entry

## Return Value

If the execution of the command was successful then the following (nonnegative) value will be returned:

`SPI_OK_REL_REGISTER`

if the relation has been successfully registered by name

On error, one of the following negative values is returned:

`SPI_ERROR_ARGUMENT`

if _`enr`_ is `NULL` or its `name` field is `NULL`

`SPI_ERROR_UNCONNECTED`

if called from an unconnected C function

`SPI_ERROR_REL_DUPLICATE`

if the name specified in the `name` field of _`enr`_ is already registered for this connection

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/spi-spi-register-relation.html/) to report a documentation issue.
