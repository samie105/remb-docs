---
title: "PostgreSQL: Documentation: 18: DROP SCHEMA"
source: "https://www.postgresql.org/docs/current/sql-dropschema.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-dropschema.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:01.459Z"
content_hash: "1b27e2b2e095839acd0da4491bb896cb86537f8d934d1993f2fc87d69ed6937a"
menu_path: ["PostgreSQL: Documentation: 18: DROP SCHEMA"]
section_path: []
---
DROP SCHEMA — remove a schema

## Synopsis

DROP SCHEMA \[ IF EXISTS \] _`name`_ \[, ...\] \[ CASCADE | RESTRICT \]

## Description

`DROP SCHEMA` removes schemas from the database.

A schema can only be dropped by its owner or a superuser. Note that the owner can drop the schema (and thereby all contained objects) even if they do not own some of the objects within the schema.

## Parameters

`IF EXISTS`

Do not throw an error if the schema does not exist. A notice is issued in this case.

_`name`_

The name of a schema.

`CASCADE`

Automatically drop objects (tables, functions, etc.) that are contained in the schema, and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the schema if it contains any objects. This is the default.

## Notes

Using the `CASCADE` option might make the command remove objects in other schemas besides the one(s) named.

## Examples

To remove schema `mystuff` from the database, along with everything it contains:

DROP SCHEMA mystuff CASCADE;

## Compatibility

`DROP SCHEMA` is fully conforming with the SQL standard, except that the standard only allows one schema to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.
