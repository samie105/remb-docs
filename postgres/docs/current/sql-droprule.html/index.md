---
title: "PostgreSQL: Documentation: 18: DROP RULE"
source: "https://www.postgresql.org/docs/current/sql-droprule.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droprule.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:47.036Z"
content_hash: "72e6bb397d7767571cee20c021eb9f496bad14c9b635c67713e684a48ca44153"
menu_path: ["PostgreSQL: Documentation: 18: DROP RULE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-droprole.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP ROLE"}
nav_next: {"path": "postgres/docs/current/sql-dropschema.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP SCHEMA"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-droprule.html "PostgreSQL 18 - DROP RULE") ([18](/docs/18/sql-droprule.html "PostgreSQL 18 - DROP RULE")) / [17](/docs/17/sql-droprule.html "PostgreSQL 17 - DROP RULE") / [16](/docs/16/sql-droprule.html "PostgreSQL 16 - DROP RULE") / [15](/docs/15/sql-droprule.html "PostgreSQL 15 - DROP RULE") / [14](/docs/14/sql-droprule.html "PostgreSQL 14 - DROP RULE")

Development Versions: [devel](/docs/devel/sql-droprule.html "PostgreSQL devel - DROP RULE")

Unsupported versions: [13](/docs/13/sql-droprule.html "PostgreSQL 13 - DROP RULE") / [12](/docs/12/sql-droprule.html "PostgreSQL 12 - DROP RULE") / [11](/docs/11/sql-droprule.html "PostgreSQL 11 - DROP RULE") / [10](/docs/10/sql-droprule.html "PostgreSQL 10 - DROP RULE") / [9.6](/docs/9.6/sql-droprule.html "PostgreSQL 9.6 - DROP RULE") / [9.5](/docs/9.5/sql-droprule.html "PostgreSQL 9.5 - DROP RULE") / [9.4](/docs/9.4/sql-droprule.html "PostgreSQL 9.4 - DROP RULE") / [9.3](/docs/9.3/sql-droprule.html "PostgreSQL 9.3 - DROP RULE") / [9.2](/docs/9.2/sql-droprule.html "PostgreSQL 9.2 - DROP RULE") / [9.1](/docs/9.1/sql-droprule.html "PostgreSQL 9.1 - DROP RULE") / [9.0](/docs/9.0/sql-droprule.html "PostgreSQL 9.0 - DROP RULE") / [8.4](/docs/8.4/sql-droprule.html "PostgreSQL 8.4 - DROP RULE") / [8.3](/docs/8.3/sql-droprule.html "PostgreSQL 8.3 - DROP RULE") / [8.2](/docs/8.2/sql-droprule.html "PostgreSQL 8.2 - DROP RULE") / [8.1](/docs/8.1/sql-droprule.html "PostgreSQL 8.1 - DROP RULE") / [8.0](/docs/8.0/sql-droprule.html "PostgreSQL 8.0 - DROP RULE") / [7.4](/docs/7.4/sql-droprule.html "PostgreSQL 7.4 - DROP RULE") / [7.3](/docs/7.3/sql-droprule.html "PostgreSQL 7.3 - DROP RULE") / [7.2](/docs/7.2/sql-droprule.html "PostgreSQL 7.2 - DROP RULE") / [7.1](/docs/7.1/sql-droprule.html "PostgreSQL 7.1 - DROP RULE")

## DROP RULE

DROP RULE — remove a rewrite rule

## Synopsis

DROP RULE \[ IF EXISTS \] _`name`_ ON _`table_name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP RULE` drops a rewrite rule.

## Parameters

`IF EXISTS`

Do not throw an error if the rule does not exist. A notice is issued in this case.

_`name`_

The name of the rule to drop.

_`table_name`_

The name (optionally schema-qualified) of the table or view that the rule applies to.

`CASCADE`

Automatically drop objects that depend on the rule, and in turn all objects that depend on those objects (see [Section 5.15](ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the rule if any objects depend on it. This is the default.

## Examples

To drop the rewrite rule `newrule`:

DROP RULE newrule ON mytable;

## Compatibility

`DROP RULE` is a PostgreSQL language extension, as is the entire query rewrite system.

## See Also

[CREATE RULE](sql-createrule.html "CREATE RULE"), [ALTER RULE](sql-alterrule.html "ALTER RULE")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-droprule.html/) to report a documentation issue.
