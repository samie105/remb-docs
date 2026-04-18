---
title: "PostgreSQL: Documentation: 18: ALTER LANGUAGE"
source: "https://www.postgresql.org/docs/current/sql-alterlanguage.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-alterlanguage.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:34.149Z"
content_hash: "01991d2bf1ecf4bafdac7c0979905c1be36e25c187f38796c7fe4468fdf8eddd"
menu_path: ["PostgreSQL: Documentation: 18: ALTER LANGUAGE"]
section_path: []
nav_prev: {"path": "postgres/docs/current/config-setting.html/index.md", "title": "PostgreSQL: Documentation: 18: 19.1.\u00a0Setting Parameters"}
nav_next: {"path": "postgres/docs/current/indexes-types.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.2.\u00a0Index Types"}
---

ALTER LANGUAGE — change the definition of a procedural language

## Synopsis

ALTER \[ PROCEDURAL \] LANGUAGE _`name`_ RENAME TO _`new_name`_
ALTER \[ PROCEDURAL \] LANGUAGE _`name`_ OWNER TO { _`new_owner`_ | CURRENT\_ROLE | CURRENT\_USER | SESSION\_USER }

## Description

`ALTER LANGUAGE` changes the definition of a procedural language. The only functionality is to rename the language or assign a new owner. You must be superuser or owner of the language to use `ALTER LANGUAGE`.

## Parameters

_`name`_

Name of a language

_`new_name`_

The new name of the language

_`new_owner`_

The new owner of the language

## Compatibility

There is no `ALTER LANGUAGE` statement in the SQL standard.
