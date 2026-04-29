---
title: "PostgreSQL: Documentation: 18: DROP COLLATION"
source: "https://www.postgresql.org/docs/current/sql-dropcollation.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropcollation.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:26.559Z"
content_hash: "fbd8455c4e967875ef136ab8d89b46f533c7975c453e5b46c9e00b50130d133d"
menu_path: ["PostgreSQL: Documentation: 18: DROP COLLATION"]
section_path: []
nav_prev: {"path": "../sql-dropcast.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP CAST"}
nav_next: {"path": "../sql-dropdatabase.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP DATABASE"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-dropcollation.html "PostgreSQL 18 - DROP COLLATION") ([18](/docs/18/sql-dropcollation.html "PostgreSQL 18 - DROP COLLATION")) / [17](/docs/17/sql-dropcollation.html "PostgreSQL 17 - DROP COLLATION") / [16](/docs/16/sql-dropcollation.html "PostgreSQL 16 - DROP COLLATION") / [15](/docs/15/sql-dropcollation.html "PostgreSQL 15 - DROP COLLATION") / [14](/docs/14/sql-dropcollation.html "PostgreSQL 14 - DROP COLLATION")

Development Versions: [devel](/docs/devel/sql-dropcollation.html "PostgreSQL devel - DROP COLLATION")

Unsupported versions: [13](/docs/13/sql-dropcollation.html "PostgreSQL 13 - DROP COLLATION") / [12](/docs/12/sql-dropcollation.html "PostgreSQL 12 - DROP COLLATION") / [11](/docs/11/sql-dropcollation.html "PostgreSQL 11 - DROP COLLATION") / [10](/docs/10/sql-dropcollation.html "PostgreSQL 10 - DROP COLLATION") / [9.6](/docs/9.6/sql-dropcollation.html "PostgreSQL 9.6 - DROP COLLATION") / [9.5](/docs/9.5/sql-dropcollation.html "PostgreSQL 9.5 - DROP COLLATION") / [9.4](/docs/9.4/sql-dropcollation.html "PostgreSQL 9.4 - DROP COLLATION") / [9.3](/docs/9.3/sql-dropcollation.html "PostgreSQL 9.3 - DROP COLLATION") / [9.2](/docs/9.2/sql-dropcollation.html "PostgreSQL 9.2 - DROP COLLATION") / [9.1](/docs/9.1/sql-dropcollation.html "PostgreSQL 9.1 - DROP COLLATION")

## DROP COLLATION

DROP COLLATION — remove a collation

## Synopsis

DROP COLLATION \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP COLLATION` removes a previously defined collation. To be able to drop a collation, you must own the collation.

## Parameters

`IF EXISTS`

Do not throw an error if the collation does not exist. A notice is issued in this case.

_`name`_

The name of the collation. The collation name can be schema-qualified.

`CASCADE`

Automatically drop objects that depend on the collation, and in turn all objects that depend on those objects (see [Section 5.15](ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the collation if any objects depend on it. This is the default.

## Examples

To drop the collation named `german`:

DROP COLLATION german;

## Compatibility

The `DROP COLLATION` command conforms to the SQL standard, apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also

[ALTER COLLATION](sql-altercollation.html "ALTER COLLATION"), [CREATE COLLATION](sql-createcollation.html "CREATE COLLATION")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-dropcollation.html/) to report a documentation issue.
