---
title: "PostgreSQL: Documentation: 18: DROP TABLE"
source: "https://www.postgresql.org/docs/current/sql-droptable.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droptable.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:19.911Z"
content_hash: "f0d89e1f65ad4dff6e83f3de7bc089b64031ba732a25d7e22fd9a08609f26637"
menu_path: ["PostgreSQL: Documentation: 18: DROP TABLE"]
section_path: []
nav_prev: {"path": "../sql-dropschema.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP SCHEMA"}
nav_next: {"path": "../sql-droptablespace.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP TABLESPACE"}
---

DROP TABLE — remove a table

## Synopsis

DROP TABLE \[ IF EXISTS \] _`name`_ \[, ...\] \[ CASCADE | RESTRICT \]

## Description

`DROP TABLE` removes tables from the database. Only the table owner, the schema owner, and superuser can drop a table. To empty a table of rows without destroying the table, use [`DELETE`](https://www.postgresql.org/docs/current/sql-delete.html "DELETE") or [`TRUNCATE`](https://www.postgresql.org/docs/current/sql-truncate.html "TRUNCATE").

`DROP TABLE` always removes any indexes, rules, triggers, and constraints that exist for the target table. However, to drop a table that is referenced by a view or a foreign-key constraint of another table, `CASCADE` must be specified. (`CASCADE` will remove a dependent view entirely, but in the foreign-key case it will only remove the foreign-key constraint, not the other table entirely.)

## Parameters

`IF EXISTS`

Do not throw an error if the table does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of the table to drop.

`CASCADE`

Automatically drop objects that depend on the table (such as views), and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the table if any objects depend on it. This is the default.

## Examples

To destroy two tables, `films` and `distributors`:

DROP TABLE films, distributors;

## Compatibility

This command conforms to the SQL standard, except that the standard only allows one table to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.
