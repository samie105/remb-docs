---
title: "PostgreSQL: Documentation: 18: Chapter 33. Large Objects"
source: "https://www.postgresql.org/docs/current/largeobjects.html"
canonical_url: "https://www.postgresql.org/docs/current/largeobjects.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:24.759Z"
content_hash: "9a68e1808ca6130a1913e3297dfd081b68d95cb308da39be93fb90abc25a2766"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 33. Large Objects"]
section_path: []
nav_prev: {"path": "../jit.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a030.\u00a0Just-in-Time Compilation (JIT)"}
nav_next: {"path": "../ecpg.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a034.\u00a0ECPG \u2014 Embedded SQL in C"}
---

PostgreSQL has a _large object_ facility, which provides stream-style access to user data that is stored in a special large-object structure. Streaming access is useful when working with data values that are too large to manipulate conveniently as a whole.

This chapter describes the implementation and the programming and query language interfaces to PostgreSQL large object data. We use the libpq C library for the examples in this chapter, but most programming interfaces native to PostgreSQL support equivalent functionality. Other interfaces might use the large object interface internally to provide generic support for large values. This is not described here.
