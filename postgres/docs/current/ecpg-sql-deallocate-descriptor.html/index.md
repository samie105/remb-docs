---
title: "PostgreSQL: Documentation: 18: DEALLOCATE DESCRIPTOR"
source: "https://www.postgresql.org/docs/current/ecpg-sql-deallocate-descriptor.html"
canonical_url: "https://www.postgresql.org/docs/current/ecpg-sql-deallocate-descriptor.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:19.543Z"
content_hash: "14224790e0f5852846201d30c50abac58c2d22b5d1449bc7d1c436b148dc26cc"
menu_path: ["PostgreSQL: Documentation: 18: DEALLOCATE DESCRIPTOR"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-update.html/index.md", "title": "PostgreSQL: Documentation: 18: UPDATE"}
nav_next: {"path": "postgres/docs/current/catalog-pg-publication-namespace.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.41.\u00a0pg_publication_namespace"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/ecpg-sql-deallocate-descriptor.html "PostgreSQL 18 - DEALLOCATE DESCRIPTOR") ([18](/docs/18/ecpg-sql-deallocate-descriptor.html "PostgreSQL 18 - DEALLOCATE DESCRIPTOR")) / [17](/docs/17/ecpg-sql-deallocate-descriptor.html "PostgreSQL 17 - DEALLOCATE DESCRIPTOR") / [16](/docs/16/ecpg-sql-deallocate-descriptor.html "PostgreSQL 16 - DEALLOCATE DESCRIPTOR") / [15](/docs/15/ecpg-sql-deallocate-descriptor.html "PostgreSQL 15 - DEALLOCATE DESCRIPTOR") / [14](/docs/14/ecpg-sql-deallocate-descriptor.html "PostgreSQL 14 - DEALLOCATE DESCRIPTOR")

Development Versions: [devel](/docs/devel/ecpg-sql-deallocate-descriptor.html "PostgreSQL devel - DEALLOCATE DESCRIPTOR")

Unsupported versions: [13](/docs/13/ecpg-sql-deallocate-descriptor.html "PostgreSQL 13 - DEALLOCATE DESCRIPTOR") / [12](/docs/12/ecpg-sql-deallocate-descriptor.html "PostgreSQL 12 - DEALLOCATE DESCRIPTOR") / [11](/docs/11/ecpg-sql-deallocate-descriptor.html "PostgreSQL 11 - DEALLOCATE DESCRIPTOR") / [10](/docs/10/ecpg-sql-deallocate-descriptor.html "PostgreSQL 10 - DEALLOCATE DESCRIPTOR") / [9.6](/docs/9.6/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.6 - DEALLOCATE DESCRIPTOR") / [9.5](/docs/9.5/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.5 - DEALLOCATE DESCRIPTOR") / [9.4](/docs/9.4/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.4 - DEALLOCATE DESCRIPTOR") / [9.3](/docs/9.3/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.3 - DEALLOCATE DESCRIPTOR") / [9.2](/docs/9.2/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.2 - DEALLOCATE DESCRIPTOR") / [9.1](/docs/9.1/ecpg-sql-deallocate-descriptor.html "PostgreSQL 9.1 - DEALLOCATE DESCRIPTOR")

## DEALLOCATE DESCRIPTOR

DEALLOCATE DESCRIPTOR — deallocate an SQL descriptor area

## Synopsis

DEALLOCATE DESCRIPTOR _`name`_

## Description

`DEALLOCATE DESCRIPTOR` deallocates a named SQL descriptor area.

## Parameters

_`name`_ [#](#ECPG-SQL-DEALLOCATE-DESCRIPTOR-NAME)

The name of the descriptor which is going to be deallocated. It is case sensitive. This can be an SQL identifier or a host variable.

## Examples

EXEC SQL DEALLOCATE DESCRIPTOR mydesc;

## Compatibility

`DEALLOCATE DESCRIPTOR` is specified in the SQL standard.

## See Also

[ALLOCATE DESCRIPTOR](ecpg-sql-allocate-descriptor.html "ALLOCATE DESCRIPTOR"), [GET DESCRIPTOR](ecpg-sql-get-descriptor.html "GET DESCRIPTOR"), [SET DESCRIPTOR](ecpg-sql-set-descriptor.html "SET DESCRIPTOR")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/ecpg-sql-deallocate-descriptor.html/) to report a documentation issue.


