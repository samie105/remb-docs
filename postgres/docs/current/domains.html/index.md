---
title: "PostgreSQL: Documentation: 18: 8.18. Domain Types"
source: "https://www.postgresql.org/docs/current/domains.html"
canonical_url: "https://www.postgresql.org/docs/current/domains.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:23.702Z"
content_hash: "129012280990b43908d4c89e5e0dc69dcdc818a59ec4c1556e033dfbb4b0ea6f"
menu_path: ["PostgreSQL: Documentation: 18: 8.18. Domain Types"]
section_path: []
nav_prev: {"path": "postgres/docs/current/plpython-database.html/index.md", "title": "PostgreSQL: Documentation: 18: 44.6.\u00a0Database Access"}
nav_next: {"path": "postgres/docs/current/wal-intro.html/index.md", "title": "PostgreSQL: Documentation: 18: 28.3.\u00a0Write-Ahead Logging (WAL)"}
---

A _domain_ is a user-defined data type that is based on another _underlying type_. Optionally, it can have constraints that restrict its valid values to a subset of what the underlying type would allow. Otherwise it behaves like the underlying type — for example, any operator or function that can be applied to the underlying type will work on the domain type. The underlying type can be any built-in or user-defined base type, enum type, array type, composite type, range type, or another domain.

For example, we could create a domain over integers that accepts only positive integers:

CREATE DOMAIN posint AS integer CHECK (VALUE > 0);
CREATE TABLE mytable (id posint);
INSERT INTO mytable VALUES(1);   -- works
INSERT INTO mytable VALUES(-1);  -- fails

When an operator or function of the underlying type is applied to a domain value, the domain is automatically down-cast to the underlying type. Thus, for example, the result of `mytable.id - 1` is considered to be of type `integer` not `posint`. We could write `(mytable.id - 1)::posint` to cast the result back to `posint`, causing the domain's constraints to be rechecked. In this case, that would result in an error if the expression had been applied to an `id` value of 1. Assigning a value of the underlying type to a field or variable of the domain type is allowed without writing an explicit cast, but the domain's constraints will be checked.

For additional information see [CREATE DOMAIN](https://www.postgresql.org/docs/current/sql-createdomain.html "CREATE DOMAIN").
