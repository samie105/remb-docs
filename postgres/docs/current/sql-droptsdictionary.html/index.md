---
title: "PostgreSQL: Documentation: 18: DROP TEXT SEARCH DICTIONARY"
source: "https://www.postgresql.org/docs/current/sql-droptsdictionary.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-droptsdictionary.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:26.047Z"
content_hash: "463dc2fbe27ac1b4040b08c896961a56787a7cb37cd112586420524c3f76ca47"
menu_path: ["PostgreSQL: Documentation: 18: DROP TEXT SEARCH DICTIONARY"]
section_path: []
---
DROP TEXT SEARCH DICTIONARY — remove a text search dictionary

## Synopsis

DROP TEXT SEARCH DICTIONARY \[ IF EXISTS \] _`name`_ \[ CASCADE | RESTRICT \]

## Description

`DROP TEXT SEARCH DICTIONARY` drops an existing text search dictionary. To execute this command you must be the owner of the dictionary.

## Parameters

`IF EXISTS`

Do not throw an error if the text search dictionary does not exist. A notice is issued in this case.

_`name`_

The name (optionally schema-qualified) of an existing text search dictionary.

`CASCADE`

Automatically drop objects that depend on the text search dictionary, and in turn all objects that depend on those objects (see [Section 5.15](https://www.postgresql.org/docs/current/ddl-depend.html "5.15. Dependency Tracking")).

`RESTRICT`

Refuse to drop the text search dictionary if any objects depend on it. This is the default.

## Examples

Remove the text search dictionary `english`:

DROP TEXT SEARCH DICTIONARY english;

This command will not succeed if there are any existing text search configurations that use the dictionary. Add `CASCADE` to drop such configurations along with the dictionary.

## Compatibility

There is no `DROP TEXT SEARCH DICTIONARY` statement in the SQL standard.
