---
title: "PostgreSQL: Documentation: 18: DROP CAST"
source: "https://www.postgresql.org/docs/current/sql-dropcast.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropcast.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:31.025Z"
content_hash: "3edb264599a03edbaf94299b24ce4485000708f5021fc84fceaa2243eee856ed"
menu_path: ["PostgreSQL: Documentation: 18: DROP CAST"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-drop-access-method.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP ACCESS METHOD"}
nav_next: {"path": "postgres/docs/current/sql-dropcollation.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP COLLATION"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-dropcast.html "PostgreSQL 18 - DROP CAST") ([18](/docs/18/sql-dropcast.html "PostgreSQL 18 - DROP CAST")) / [17](/docs/17/sql-dropcast.html "PostgreSQL 17 - DROP CAST") / [16](/docs/16/sql-dropcast.html "PostgreSQL 16 - DROP CAST") / [15](/docs/15/sql-dropcast.html "PostgreSQL 15 - DROP CAST") / [14](/docs/14/sql-dropcast.html "PostgreSQL 14 - DROP CAST")

Development Versions: [devel](/docs/devel/sql-dropcast.html "PostgreSQL devel - DROP CAST")

Unsupported versions: [13](/docs/13/sql-dropcast.html "PostgreSQL 13 - DROP CAST") / [12](/docs/12/sql-dropcast.html "PostgreSQL 12 - DROP CAST") / [11](/docs/11/sql-dropcast.html "PostgreSQL 11 - DROP CAST") / [10](/docs/10/sql-dropcast.html "PostgreSQL 10 - DROP CAST") / [9.6](/docs/9.6/sql-dropcast.html "PostgreSQL 9.6 - DROP CAST") / [9.5](/docs/9.5/sql-dropcast.html "PostgreSQL 9.5 - DROP CAST") / [9.4](/docs/9.4/sql-dropcast.html "PostgreSQL 9.4 - DROP CAST") / [9.3](/docs/9.3/sql-dropcast.html "PostgreSQL 9.3 - DROP CAST") / [9.2](/docs/9.2/sql-dropcast.html "PostgreSQL 9.2 - DROP CAST") / [9.1](/docs/9.1/sql-dropcast.html "PostgreSQL 9.1 - DROP CAST") / [9.0](/docs/9.0/sql-dropcast.html "PostgreSQL 9.0 - DROP CAST") / [8.4](/docs/8.4/sql-dropcast.html "PostgreSQL 8.4 - DROP CAST") / [8.3](/docs/8.3/sql-dropcast.html "PostgreSQL 8.3 - DROP CAST") / [8.2](/docs/8.2/sql-dropcast.html "PostgreSQL 8.2 - DROP CAST") / [8.1](/docs/8.1/sql-dropcast.html "PostgreSQL 8.1 - DROP CAST") / [8.0](/docs/8.0/sql-dropcast.html "PostgreSQL 8.0 - DROP CAST") / [7.4](/docs/7.4/sql-dropcast.html "PostgreSQL 7.4 - DROP CAST") / [7.3](/docs/7.3/sql-dropcast.html "PostgreSQL 7.3 - DROP CAST")

## DROP CAST

DROP CAST — remove a cast

## Synopsis

DROP CAST \[ IF EXISTS \] (_`source_type`_ AS _`target_type`_) \[ CASCADE | RESTRICT \]

## Description

`DROP CAST` removes a previously defined cast.

To be able to drop a cast, you must own the source or the target data type. These are the same privileges that are required to create a cast.

## Parameters

`IF EXISTS`

Do not throw an error if the cast does not exist. A notice is issued in this case.

_`source_type`_

The name of the source data type of the cast.

_`target_type`_

The name of the target data type of the cast.

`CASCADE`  
`RESTRICT`

These key words do not have any effect, since there are no dependencies on casts.

## Examples

To drop the cast from type `text` to type `int`:

DROP CAST (text AS int);

## Compatibility

The `DROP CAST` command conforms to the SQL standard.

## See Also

[CREATE CAST](sql-createcast.html "CREATE CAST")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-dropcast.html/) to report a documentation issue.
