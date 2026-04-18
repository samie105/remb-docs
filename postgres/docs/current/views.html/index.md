---
title: "PostgreSQL: Documentation: 18: Chapter 53. System Views"
source: "https://www.postgresql.org/docs/current/views.html"
canonical_url: "https://www.postgresql.org/docs/current/views.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:47.045Z"
content_hash: "c311107146e097ab513dd93f71e9f43be7bab15b2aa8b21bfe2464ec6067417d"
menu_path: ["PostgreSQL: Documentation: 18: Chapter 53. System Views"]
section_path: []
nav_prev: {"path": "postgres/docs/current/reference-client.html/index.md", "title": "PostgreSQL Client Applications"}
nav_next: {"path": "postgres/docs/current/protocol.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a054.\u00a0Frontend/Backend Protocol"}
---

In addition to the system catalogs, PostgreSQL provides a number of built-in views. Some system views provide convenient access to some commonly used queries on the system catalogs. Other views provide access to internal server state.

The information schema ([Chapter 35](https://www.postgresql.org/docs/current/information-schema.html "Chapter 35. The Information Schema")) provides an alternative set of views which overlap the functionality of the system views. Since the information schema is SQL-standard whereas the views described here are PostgreSQL\-specific, it's usually better to use the information schema if it provides all the information you need.

[Table 53.1](https://www.postgresql.org/docs/current/views-overview.html#VIEW-TABLE "Table 53.1. System Views") lists the system views described here. More detailed documentation of each view follows below. There are some additional views that provide access to accumulated statistics; they are described in [Table 27.2](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-VIEWS-TABLE "Table 27.2. Collected Statistics Views").

