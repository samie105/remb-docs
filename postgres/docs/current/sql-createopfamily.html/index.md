---
title: "PostgreSQL: Documentation: 18: CREATE OPERATOR FAMILY"
source: "https://www.postgresql.org/docs/current/sql-createopfamily.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-createopfamily.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:05.932Z"
content_hash: "804f78d883a7404cf8185d0964c4a4aeb12c9fce0674b4a8efbd45992ed8baf6"
menu_path: ["PostgreSQL: Documentation: 18: CREATE OPERATOR FAMILY"]
section_path: []
nav_prev: {"path": "../sql-createdomain.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE DOMAIN"}
nav_next: {"path": "../sql-createpolicy.html/index.md", "title": "PostgreSQL: Documentation: 18: CREATE POLICY"}
---

CREATE OPERATOR FAMILY — define a new operator family

## Synopsis

CREATE OPERATOR FAMILY _`name`_ USING _`index_method`_

## Description

`CREATE OPERATOR FAMILY` creates a new operator family. An operator family defines a collection of related operator classes, and perhaps some additional operators and support functions that are compatible with these operator classes but not essential for the functioning of any individual index. (Operators and functions that are essential to indexes should be grouped within the relevant operator class, rather than being “loose” in the operator family. Typically, single-data-type operators are bound to operator classes, while cross-data-type operators can be loose in an operator family containing operator classes for both data types.)

The new operator family is initially empty. It should be populated by issuing subsequent `CREATE OPERATOR CLASS` commands to add contained operator classes, and optionally `ALTER OPERATOR FAMILY` commands to add “loose” operators and their corresponding support functions.

If a schema name is given then the operator family is created in the specified schema. Otherwise it is created in the current schema. Two operator families in the same schema can have the same name only if they are for different index methods.

The user who defines an operator family becomes its owner. Presently, the creating user must be a superuser. (This restriction is made because an erroneous operator family definition could confuse or even crash the server.)

Refer to [Section 36.16](https://www.postgresql.org/docs/current/xindex.html "36.16. Interfacing Extensions to Indexes") for further information.

## Parameters

_`name`_

The name of the operator family to be created. The name can be schema-qualified.

_`index_method`_

The name of the index method this operator family is for.

## Compatibility

`CREATE OPERATOR FAMILY` is a PostgreSQL extension. There is no `CREATE OPERATOR FAMILY` statement in the SQL standard.
