---
title: "PostgreSQL: Documentation: 18: Chapter 15. Parallel Query"
source: "https://www.postgresql.org/docs/current/parallel-query.html"
canonical_url: "https://www.postgresql.org/docs/current/parallel-query.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:53.606Z"
content_hash: "4ea3b6207c6a220761d25c09eb7ee692a2dbef61e541b34d1338ae8ad6bbae85"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 15. Parallel Query"]
section_path: []
nav_prev: {"path": "postgres/docs/current/performance-tips.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a014.\u00a0Performance Tips"}
nav_next: {"path": "postgres/docs/current/runtime.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a018.\u00a0Server Setup and Operation"}
---

PostgreSQL can devise query plans that can leverage multiple CPUs in order to answer queries faster. This feature is known as parallel query. Many queries cannot benefit from parallel query, either due to limitations of the current implementation or because there is no imaginable query plan that is any faster than the serial query plan. However, for queries that can benefit, the speedup from parallel query is often very significant. Many queries can run more than twice as fast when using parallel query, and some queries can run four times faster or even more. Queries that touch a large amount of data but return only a few rows to the user will typically benefit most. This chapter explains some details of how parallel query works and in which situations it can be used so that users who wish to make use of it can understand what to expect.

