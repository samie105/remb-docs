---
title: "PostgreSQL: Documentation: 18: Chapter 14. Performance Tips"
source: "https://www.postgresql.org/docs/current/performance-tips.html"
canonical_url: "https://www.postgresql.org/docs/current/performance-tips.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:39.767Z"
content_hash: "5f725704687c65d5f6b0719da2f5d6e1c730fe1627a5c9d65a86aafdf34983f8"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 14. Performance Tips"]
section_path: []
content_language: "en"
nav_prev: {"path": "postgres/docs/current/textsearch.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a012.\u00a0Full Text Search"}
nav_next: {"path": "postgres/docs/current/parallel-query.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a015.\u00a0Parallel Query"}
---

Development Versions: [devel](https://www.postgresql.org/docs/devel/performance-tips.html "PostgreSQL devel - Chapter 14. Performance Tips")

| Chapter 14. Performance Tips |
| --- |
| [Prev](https://www.postgresql.org/docs/current/locking-indexes.html "13.7. Locking and Indexes")  | [Up](https://www.postgresql.org/docs/current/sql.html "Part II. The SQL Language") | Part II. The SQL Language | [Home](https://www.postgresql.org/docs/current/index.html "PostgreSQL 18.3 Documentation") |  [Next](https://www.postgresql.org/docs/current/using-explain.html "14.1. Using EXPLAIN") |

* * *

Query performance can be affected by many things. Some of these can be controlled by the user, while others are fundamental to the underlying design of the system. This chapter provides some hints about understanding and tuning PostgreSQL performance.
