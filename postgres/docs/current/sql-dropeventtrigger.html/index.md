---
title: "PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"
source: "https://www.postgresql.org/docs/current/sql-dropeventtrigger.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropeventtrigger.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:42.097Z"
content_hash: "7f09536501c388f6b2b333b79bf83b6c9dea87953c220c772ab951c0623a5b9c"
menu_path: ["PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-drop-access-method.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP ACCESS METHOD"}
nav_next: {"path": "postgres/docs/current/ecpg-sql-declare-statement.html/index.md", "title": "PostgreSQL: Documentation: 18: DECLARE STATEMENT"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/sql-dropeventtrigger.html "PostgreSQL 18 - DROP EVENT TRIGGER") ([18](/docs/18/sql-dropeventtrigger.html "PostgreSQL 18 - DROP EVENT TRIGGER")) / [17](/docs/17/sql-dropeventtrigger.html "PostgreSQL 17 - DROP EVENT TRIGGER") / [16](/docs/16/sql-dropeventtrigger.html "PostgreSQL 16 - DROP EVENT TRIGGER") / [15](/docs/15/sql-dropeventtrigger.html "PostgreSQL 15 - DROP EVENT TRIGGER") / [14](/docs/14/sql-dropeventtrigger.html "PostgreSQL 14 - DROP EVENT TRIGGER")

Development Versions: [devel](/docs/devel/sql-dropeventtrigger.html "PostgreSQL devel - DROP EVENT TRIGGER")

Unsupported versions: [13](/docs/13/sql-dropeventtrigger.html "PostgreSQL 13 - DROP EVENT TRIGGER") / [12](/docs/12/sql-dropeventtrigger.html "PostgreSQL 12 - DROP EVENT TRIGGER") / [11](/docs/11/sql-dropeventtrigger.html "PostgreSQL 11 - DROP EVENT TRIGGER") / [10](/docs/10/sql-dropeventtrigger.html "PostgreSQL 10 - DROP EVENT TRIGGER") / [9.6](/docs/9.6/sql-dropeventtrigger.html "PostgreSQL 9.6 - DROP EVENT TRIGGER") / [9.5](/docs/9.5/sql-dropeventtrigger.html "PostgreSQL 9.5 - DROP EVENT TRIGGER") / [9.4](/docs/9.4/sql-dropeventtrigger.html "PostgreSQL 9.4 - DROP EVENT TRIGGER") / [9.3](/docs/9.3/sql-dropeventtrigger.html "PostgreSQL 9.3 - DROP EVENT TRIGGER")

## DROP EVENT TRIGGER

DROP EVENT TRIGGER — remove an event trigger

## Synopsis

DROP EVENT TRIGGER \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP EVENT TRIGGER` removes an existing event trigger. To execute this command, the current user must be the owner of the event trigger.

## Parameters

`IF EXISTS`

Do not throw an error if the event trigger does not exist. A notice is issued in this case.

_`name`_

The name of the event trigger to remove.

`CASCADE`

Automatically drop objects that depend on the trigger, and in turn all objects that depend on those objects (see [Section 5.15](ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the trigger if any objects depend on it. This is the default.

## Examples

Destroy the trigger `snitch`:

DROP EVENT TRIGGER snitch;

## Compatibility

There is no `DROP EVENT TRIGGER` statement in the SQL standard.

## See Also

[CREATE EVENT TRIGGER](sql-createeventtrigger.html "CREATE EVENT TRIGGER"), [ALTER EVENT TRIGGER](sql-altereventtrigger.html "ALTER EVENT TRIGGER")

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/sql-dropeventtrigger.html/) to report a documentation issue.


