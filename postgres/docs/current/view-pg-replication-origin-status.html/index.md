---
title: "PostgreSQL: Documentation: 18: 53.19. pg_replication_origin_status"
source: "https://www.postgresql.org/docs/current/view-pg-replication-origin-status.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-replication-origin-status.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:46.295Z"
content_hash: "398431ae89be41265b6a9b0dea1b839fda896224c75561e1c498896733981311"
menu_path: ["PostgreSQL: Documentation: 18: 53.19. pg_replication_origin_status"]
section_path: []
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-replication-origin-status.html "PostgreSQL devel - 53.19. pg_replication_origin_status")

The `pg_replication_origin_status` view contains information about how far replay for a certain origin has progressed. For more on replication origins see [Chapter 48](https://www.postgresql.org/docs/current/replication-origins.html "Chapter 48. Replication Progress Tracking").

**Table 53.19. `pg_replication_origin_status` Columns**

Column Type

Description

`local_id` `oid` (references [`pg_replication_origin`](https://www.postgresql.org/docs/current/catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roident`)

internal node identifier

`external_id` `text` (references [`pg_replication_origin`](https://www.postgresql.org/docs/current/catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roname`)

external node identifier

`remote_lsn` `pg_lsn`

The origin node's LSN up to which data has been replicated.

`local_lsn` `pg_lsn`

This node's LSN at which `remote_lsn` has been replicated. Used to flush commit records before persisting data to disk when using asynchronous commits.
