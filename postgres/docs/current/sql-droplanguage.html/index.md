---
title: "PostgreSQL: Documentation: 18: DROP LANGUAGE"
source: "https://www.postgresql.org/docs/current/sql-droplanguage.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droplanguage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:32.477Z"
content_hash: "74e3e7110543764b4e340f0e6ad00b98bb43a1162a7c0b3cb15d9d90d99083f7"
menu_path: ["PostgreSQL: Documentation: 18: DROP LANGUAGE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-timezone-abbrevs.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.33.\u00a0pg_timezone_abbrevs"}
nav_next: {"path": "postgres/docs/current/catalog-pg-tablespace.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.56.\u00a0pg_tablespace"}
---

DROP LANGUAGE — remove a procedural language

## Synopsis

DROP \[ PROCEDURAL \] LANGUAGE \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP LANGUAGE` removes the definition of a previously registered procedural language. You must be a superuser or the owner of the language to use `DROP LANGUAGE`.

### Note

As of PostgreSQL 9.1, most procedural languages have been made into “extensions”, and should therefore be removed with [`DROP EXTENSION`](https://www.postgresql.org/docs/current/sql-dropextension.html "DROP EXTENSION") not `DROP LANGUAGE`.

## Parameters

`IF EXISTS`

Do not throw an error if the language does not exist. A notice is issued in this case.

_`name`_

The name of an existing procedural language.

`CASCADE`

Automatically drop objects that depend on the language (such as functions in the language), and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the language if any objects depend on it. This is the default.

## Examples

This command removes the procedural language `plsample`:

DROP LANGUAGE plsample;

## Compatibility

There is no `DROP LANGUAGE` statement in the SQL standard.


