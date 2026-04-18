---
title: "PostgreSQL: Documentation: 18: DROP DOMAIN"
source: "https://www.postgresql.org/docs/current/sql-dropdomain.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropdomain.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:19.484Z"
content_hash: "c8db54d63d6fa6e73a307ffd230f2404f260e6cc41e1d253ef7f38b569567442"
menu_path: ["PostgreSQL: Documentation: 18: DROP DOMAIN"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-dropdatabase.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP DATABASE"}
nav_next: {"path": "postgres/docs/current/sql-dropeventtrigger.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-dropdomain.html "PostgreSQL 18 - DROP DOMAIN") ([18](/docs/18/sql-dropdomain.html "PostgreSQL 18 - DROP DOMAIN")) / [17](/docs/17/sql-dropdomain.html "PostgreSQL 17 - DROP DOMAIN") / [16](/docs/16/sql-dropdomain.html "PostgreSQL 16 - DROP DOMAIN") / [15](/docs/15/sql-dropdomain.html "PostgreSQL 15 - DROP DOMAIN") / [14](/docs/14/sql-dropdomain.html "PostgreSQL 14 - DROP DOMAIN")

Development Versions: [devel](/docs/devel/sql-dropdomain.html "PostgreSQL devel - DROP DOMAIN")

Unsupported versions: [13](/docs/13/sql-dropdomain.html "PostgreSQL 13 - DROP DOMAIN") / [12](/docs/12/sql-dropdomain.html "PostgreSQL 12 - DROP DOMAIN") / [11](/docs/11/sql-dropdomain.html "PostgreSQL 11 - DROP DOMAIN") / [10](/docs/10/sql-dropdomain.html "PostgreSQL 10 - DROP DOMAIN") / [9.6](/docs/9.6/sql-dropdomain.html "PostgreSQL 9.6 - DROP DOMAIN") / [9.5](/docs/9.5/sql-dropdomain.html "PostgreSQL 9.5 - DROP DOMAIN") / [9.4](/docs/9.4/sql-dropdomain.html "PostgreSQL 9.4 - DROP DOMAIN") / [9.3](/docs/9.3/sql-dropdomain.html "PostgreSQL 9.3 - DROP DOMAIN") / [9.2](/docs/9.2/sql-dropdomain.html "PostgreSQL 9.2 - DROP DOMAIN") / [9.1](/docs/9.1/sql-dropdomain.html "PostgreSQL 9.1 - DROP DOMAIN") / [9.0](/docs/9.0/sql-dropdomain.html "PostgreSQL 9.0 - DROP DOMAIN") / [8.4](/docs/8.4/sql-dropdomain.html "PostgreSQL 8.4 - DROP DOMAIN") / [8.3](/docs/8.3/sql-dropdomain.html "PostgreSQL 8.3 - DROP DOMAIN") / [8.2](/docs/8.2/sql-dropdomain.html "PostgreSQL 8.2 - DROP DOMAIN") / [8.1](/docs/8.1/sql-dropdomain.html "PostgreSQL 8.1 - DROP DOMAIN") / [8.0](/docs/8.0/sql-dropdomain.html "PostgreSQL 8.0 - DROP DOMAIN") / [7.4](/docs/7.4/sql-dropdomain.html "PostgreSQL 7.4 - DROP DOMAIN") / [7.3](/docs/7.3/sql-dropdomain.html "PostgreSQL 7.3 - DROP DOMAIN")

## DROP DOMAIN

DROP DOMAIN — remove a domain

## Synopsis

DROP DOMAIN \[ IF EXISTS \] _`name`_ \[, ...\] \[ CASCADE | RESTRICT \]

## Description

`DROP DOMAIN` removes a domain. Only the owner of a domain can remove it.

## Parameters

`IF EXISTS`

Do not throw an error if the domain does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of an existing domain.

`CASCADE`

Automatically drop objects that depend on the domain (such as table columns), and in turn all objects that depend on those objects (see [Section 5.15](ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the domain if any objects depend on it. This is the default.

## Examples

To remove the domain `box`:

DROP DOMAIN box;

## Compatibility

This command conforms to the SQL standard, except for the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also

[CREATE DOMAIN](sql-createdomain.html "CREATE DOMAIN"), [ALTER DOMAIN](sql-alterdomain.html "ALTER DOMAIN")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-dropdomain.html/) to report a documentation issue.
