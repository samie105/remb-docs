---
title: "PostgreSQL: Documentation: 18: 53.19. pg_replication_origin_status"
source: "https://www.postgresql.org/docs/current/view-pg-replication-origin-status.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-replication-origin-status.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:44:06.341Z"
content_hash: "2b7a0cffe18fb3b5dcb76923f62a84d1ed72083d4eb4aa115ad9094ec3efee03"
menu_path: ["PostgreSQL: Documentation: 18: 53.19. pg_replication_origin_status"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/view-pg-replication-origin-status.html "PostgreSQL devel - 53.19. pg_replication_origin_status")

The `pg_replication_origin_status` view contains information about how far replay for a certain origin has progressed. For more on replication origins see [Chapter 48](https://www.postgresql.org/docs/current/replication-origins.html "Chapter 48. Replication Progress Tracking").

**Table 53.19. `pg_replication_origin_status` Columns**

| 
Column Type

Description

 |
| --- |
| 

`local_id` `oid` (references [`pg_replication_origin`](https://www.postgresql.org/docs/current/catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roident`)

internal node identifier

 |
| 

`external_id` `text` (references [`pg_replication_origin`](https://www.postgresql.org/docs/current/catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roname`)

external node identifier

 |
| 

`remote_lsn` `pg_lsn`

The origin node's LSN up to which data has been replicated.

 |
| 

`local_lsn` `pg_lsn`

This node's LSN at which `remote_lsn` has been replicated. Used to flush commit records before persisting data to disk when using asynchronous commits.

 |
