---
title: "PostgreSQL: Documentation: 18: Chapter 64. Write Ahead Logging for Extensions"
source: "https://www.postgresql.org/docs/current/wal-for-extensions.html"
canonical_url: "https://www.postgresql.org/docs/current/wal-for-extensions.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:25.365Z"
content_hash: "cbf5df6317f12890285d95fe235f5fce6eef945a88b9ee164c27009020df5945"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 64. Write Ahead Logging for Extensions"]
section_path: []
nav_prev: {"path": "postgres/docs/current/geqo.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a061.\u00a0Genetic Query Optimizer"}
nav_next: {"path": "postgres/docs/current/indextypes.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a065.\u00a0Built-in Index Access Methods"}
---

Certain extensions, principally extensions that implement custom access methods, may need to perform write-ahead logging in order to ensure crash-safety. PostgreSQL provides two ways for extensions to achieve this goal.

First, extensions can choose to use [generic WAL](https://www.postgresql.org/docs/current/generic-wal.html "64.1. Generic WAL Records"), a special type of WAL record which describes changes to pages in a generic way. This method is simple to implement and does not require that an extension library be loaded in order to apply the records. However, generic WAL records will be ignored when performing logical decoding.

Second, extensions can choose to use a [custom resource manager](https://www.postgresql.org/docs/current/custom-rmgr.html "64.2. Custom WAL Resource Managers"). This method is more flexible, supports logical decoding, and can sometimes generate much smaller write-ahead log records than would be possible with generic WAL. However, it is more complex for an extension to implement.

