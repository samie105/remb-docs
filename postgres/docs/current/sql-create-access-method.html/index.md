---
title: "PostgreSQL: Documentation: 18: CREATE ACCESS METHOD"
source: "https://www.postgresql.org/docs/current/sql-create-access-method.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-create-access-method.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:32.373Z"
content_hash: "309ad30a8c05864b08cae97fc60a4343af09d6588183e1972539bc53932c7e41"
menu_path: ["PostgreSQL: Documentation: 18: CREATE ACCESS METHOD"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-droptablespace.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP TABLESPACE"}
nav_next: {"path": "postgres/docs/current/ecpg-concept.html/index.md", "title": "PostgreSQL: Documentation: 18: 34.1.\u00a0The Concept"}
---

CREATE ACCESS METHOD — define a new access method

## Synopsis

CREATE ACCESS METHOD _`name`_
    TYPE _`access_method_type`_
    HANDLER _`handler_function`_

## Description

`CREATE ACCESS METHOD` creates a new access method.

The access method name must be unique within the database.

Only superusers can define new access methods.

## Parameters

_`name`_

The name of the access method to be created.

_`access_method_type`_

This clause specifies the type of access method to define. Only `TABLE` and `INDEX` are supported at present.

_`handler_function`_

_`handler_function`_ is the name (possibly schema-qualified) of a previously registered function that represents the access method. The handler function must be declared to take a single argument of type `internal`, and its return type depends on the type of access method; for `TABLE` access methods, it must be `table_am_handler` and for `INDEX` access methods, it must be `index_am_handler`. The C-level API that the handler function must implement varies depending on the type of access method. The table access method API is described in [Chapter 62](https://www.postgresql.org/docs/current/tableam.html "Chapter 62. Table Access Method Interface Definition") and the index access method API is described in [Chapter 63](https://www.postgresql.org/docs/current/indexam.html "Chapter 63. Index Access Method Interface Definition").

## Examples

Create an index access method `heptree` with handler function `heptree_handler`:

CREATE ACCESS METHOD heptree TYPE INDEX HANDLER heptree\_handler;

## Compatibility

`CREATE ACCESS METHOD` is a PostgreSQL extension.
