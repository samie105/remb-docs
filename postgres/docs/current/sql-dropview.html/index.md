---
title: "PostgreSQL: Documentation: 18: DROP VIEW"
source: "https://www.postgresql.org/docs/current/sql-dropview.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropview.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:12.682Z"
content_hash: "62974256be4b8e1197f72de02209a1e12080fe86c27cfde034290d8ab3fbec0e"
menu_path: ["PostgreSQL: Documentation: 18: DROP VIEW"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgtesttiming.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_test_timing"}
nav_next: {"path": "postgres/docs/current/view-pg-rules.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.22.\u00a0pg_rules"}
---

DROP VIEW — remove a view

## Synopsis

DROP VIEW \[ IF EXISTS \] _`name`_ \[, ...\] \[ CASCADE | RESTRICT \]

## Description

`DROP VIEW` drops an existing view. To execute this command you must be the owner of the view.

## Parameters

`IF EXISTS`

Do not throw an error if the view does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of the view to remove.

`CASCADE`

Automatically drop objects that depend on the view (such as other views), and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the view if any objects depend on it. This is the default.

## Examples

This command will remove the view called `kinds`:

DROP VIEW kinds;

## Compatibility

This command conforms to the SQL standard, except that the standard only allows one view to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

