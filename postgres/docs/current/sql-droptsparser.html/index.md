---
title: "PostgreSQL: Documentation: 18: DROP TEXT SEARCH PARSER"
source: "https://www.postgresql.org/docs/current/sql-droptsparser.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droptsparser.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:17.831Z"
content_hash: "b61e6aca21ace24eb55e42244386041b39eafe6a8faaad83018f09510971e5c8"
menu_path: ["PostgreSQL: Documentation: 18: DROP TEXT SEARCH PARSER"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.22.\u00a0pg_rules"}
nav_next: {"path": "postgres/docs/current/sql-createtype.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE TYPE"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-droptsparser.html "PostgreSQL 18 - DROP TEXT SEARCH PARSER") ([18](/docs/18/sql-droptsparser.html "PostgreSQL 18 - DROP TEXT SEARCH PARSER")) / [17](/docs/17/sql-droptsparser.html "PostgreSQL 17 - DROP TEXT SEARCH PARSER") / [16](/docs/16/sql-droptsparser.html "PostgreSQL 16 - DROP TEXT SEARCH PARSER") / [15](/docs/15/sql-droptsparser.html "PostgreSQL 15 - DROP TEXT SEARCH PARSER") / [14](/docs/14/sql-droptsparser.html "PostgreSQL 14 - DROP TEXT SEARCH PARSER")

Development Versions: [devel](/docs/devel/sql-droptsparser.html "PostgreSQL devel - DROP TEXT SEARCH PARSER")

Unsupported versions: [13](/docs/13/sql-droptsparser.html "PostgreSQL 13 - DROP TEXT SEARCH PARSER") / [12](/docs/12/sql-droptsparser.html "PostgreSQL 12 - DROP TEXT SEARCH PARSER") / [11](/docs/11/sql-droptsparser.html "PostgreSQL 11 - DROP TEXT SEARCH PARSER") / [10](/docs/10/sql-droptsparser.html "PostgreSQL 10 - DROP TEXT SEARCH PARSER") / [9.6](/docs/9.6/sql-droptsparser.html "PostgreSQL 9.6 - DROP TEXT SEARCH PARSER") / [9.5](/docs/9.5/sql-droptsparser.html "PostgreSQL 9.5 - DROP TEXT SEARCH PARSER") / [9.4](/docs/9.4/sql-droptsparser.html "PostgreSQL 9.4 - DROP TEXT SEARCH PARSER") / [9.3](/docs/9.3/sql-droptsparser.html "PostgreSQL 9.3 - DROP TEXT SEARCH PARSER") / [9.2](/docs/9.2/sql-droptsparser.html "PostgreSQL 9.2 - DROP TEXT SEARCH PARSER") / [9.1](/docs/9.1/sql-droptsparser.html "PostgreSQL 9.1 - DROP TEXT SEARCH PARSER") / [9.0](/docs/9.0/sql-droptsparser.html "PostgreSQL 9.0 - DROP TEXT SEARCH PARSER") / [8.4](/docs/8.4/sql-droptsparser.html "PostgreSQL 8.4 - DROP TEXT SEARCH PARSER") / [8.3](/docs/8.3/sql-droptsparser.html "PostgreSQL 8.3 - DROP TEXT SEARCH PARSER")

## DROP TEXT SEARCH PARSER

DROP TEXT SEARCH PARSER — remove a text search parser

## Synopsis

DROP TEXT SEARCH PARSER \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP TEXT SEARCH PARSER` drops an existing text search parser. You must be a superuser to use this command.

## Parameters

`IF EXISTS`

Do not throw an error if the text search parser does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of an existing text search parser.

`CASCADE`

Automatically drop objects that depend on the text search parser, and in turn all objects that depend on those objects (see [Section 5.15](ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the text search parser if any objects depend on it. This is the default.

## Examples

Remove the text search parser `my_parser`:

DROP TEXT SEARCH PARSER my\_parser;

This command will not succeed if there are any existing text search configurations that use the parser. Add `CASCADE` to drop such configurations along with the parser.

## Compatibility

There is no `DROP TEXT SEARCH PARSER` statement in the SQL standard.

## See Also

[ALTER TEXT SEARCH PARSER](sql-altertsparser.html "ALTER TEXT SEARCH PARSER"), [CREATE TEXT SEARCH PARSER](sql-createtsparser.html "CREATE TEXT SEARCH PARSER")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-droptsparser.html/) to report a documentation issue.

