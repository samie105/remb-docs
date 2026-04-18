---
title: "PostgreSQL: Documentation: 18: Chapter 9. Functions and Operators"
source: "https://www.postgresql.org/docs/current/functions.html"
canonical_url: "https://www.postgresql.org/docs/current/functions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:55.419Z"
content_hash: "35d84544b503444abaaa74249e941d40e0cf94542570f14aa5333beb6e63a8d6"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 9. Functions and Operators"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ddl.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a05.\u00a0Data Definition"}
nav_next: {"path": "postgres/docs/current/textsearch.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a012.\u00a0Full Text Search"}
---

PostgreSQL provides a large number of functions and operators for the built-in data types. This chapter describes most of them, although additional special-purpose functions appear in relevant sections of the manual. Users can also define their own functions and operators, as described in [Part V](https://www.postgresql.org/docs/current/server-programming.html "Part V. Server Programming"). The psql commands `\df` and `\do` can be used to list all available functions and operators, respectively.

The notation used throughout this chapter to describe the argument and result data types of a function or operator is like this:

```
repeat
```

which says that the function `repeat` takes one text and one integer argument and returns a result of type text. The right arrow is also used to indicate the result of an example, thus:

repeat('Pg', 4) → `PgPgPgPg`

If you are concerned about portability then note that most of the functions and operators described in this chapter, with the exception of the most trivial arithmetic and comparison operators and some explicitly marked functions, are not specified by the SQL standard. Some of this extended functionality is present in other SQL database management systems, and in many cases this functionality is compatible and consistent between the various implementations.

