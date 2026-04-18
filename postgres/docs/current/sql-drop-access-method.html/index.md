---
title: "PostgreSQL: Documentation: 18: DROP ACCESS METHOD"
source: "https://www.postgresql.org/docs/current/sql-drop-access-method.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-drop-access-method.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:39.623Z"
content_hash: "a6623f2ea90918a814cc5a86ea0fb32f596f4d9220b5b78b7f66abd146520af1"
menu_path: ["PostgreSQL: Documentation: 18: DROP ACCESS METHOD"]
section_path: []
nav_prev: {"path": "postgres/docs/current/source-format.html/index.md", "title": "PostgreSQL: Documentation: 18: 55.1.\u00a0Formatting"}
nav_next: {"path": "postgres/docs/current/sql-dropeventtrigger.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP EVENT TRIGGER"}
---

DROP ACCESS METHOD — remove an access method

## Synopsis

DROP ACCESS METHOD \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP ACCESS METHOD` removes an existing access method. Only superusers can drop access methods.

## Parameters

`IF EXISTS`

Do not throw an error if the access method does not exist. A notice is issued in this case.

_`name`_

The name of an existing access method.

`CASCADE`

Automatically drop objects that depend on the access method (such as operator classes, operator families, and indexes), and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the access method if any objects depend on it. This is the default.

## Examples

Drop the access method `heptree`:

DROP ACCESS METHOD heptree;

## Compatibility

`DROP ACCESS METHOD` is a PostgreSQL extension.
