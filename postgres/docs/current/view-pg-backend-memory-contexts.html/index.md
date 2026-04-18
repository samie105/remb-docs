---
title: "PostgreSQL: Documentation: 18: 53.5. pg_backend_memory_contexts"
source: "https://www.postgresql.org/docs/current/view-pg-backend-memory-contexts.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-backend-memory-contexts.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:02.859Z"
content_hash: "6f61d6f8d8c11c9a1011693710d87e4b0624a4b564d0d411378ab42af49aca89"
menu_path: ["PostgreSQL: Documentation: 18: 53.5. pg_backend_memory_contexts"]
section_path: []
nav_prev: {"path": "postgres/docs/current/gssapi-enc.html/index.md", "title": "PostgreSQL: Documentation: 18: 18.10.\u00a0Secure TCP/IP Connections with GSSAPI Encryption"}
nav_next: {"path": "postgres/docs/current/plperl-triggers.html/index.md", "title": "PostgreSQL: Documentation: 18: 43.6.\u00a0PL/Perl Triggers"}
---

The view `pg_backend_memory_contexts` displays all the memory contexts of the server process attached to the current session.

`pg_backend_memory_contexts` contains one row for each memory context.

**Table 53.5. `pg_backend_memory_contexts` Columns**

Column Type

Description

`name` `text`

Name of the memory context

`ident` `text`

Identification information of the memory context. This field is truncated at 1024 bytes

`type` `text`

Type of the memory context

`level` `int4`

The 1-based level of the context in the memory context hierarchy. The level of a context also shows the position of that context in the `path` column.

`path` `int4[]`

Array of transient numerical identifiers to describe the memory context hierarchy. The first element is for `TopMemoryContext`, subsequent elements contain intermediate parents and the final element contains the identifier for the current context.

`total_bytes` `int8`

Total bytes allocated for this memory context

`total_nblocks` `int8`

Total number of blocks allocated for this memory context

`free_bytes` `int8`

Free space in bytes

`free_chunks` `int8`

Total number of free chunks

`used_bytes` `int8`

Used space in bytes

By default, the `pg_backend_memory_contexts` view can be read only by superusers or roles with the privileges of the `pg_read_all_stats` role.

Since memory contexts are created and destroyed during the running of a query, the identifiers stored in the `path` column can be unstable between multiple invocations of the view in the same query. The example below demonstrates an effective usage of this column and calculates the total number of bytes used by `CacheMemoryContext` and all of its children:

WITH memory\_contexts AS (
    SELECT \* FROM pg\_backend\_memory\_contexts
)
SELECT sum(c1.total\_bytes)
FROM memory\_contexts c1, memory\_contexts c2
WHERE c2.name = 'CacheMemoryContext'
AND c1.path\[c2.level\] = c2.path\[c2.level\];

The [Common Table Expression](https://www.postgresql.org/docs/current/queries-with.html "7.8. WITH Queries (Common Table Expressions)") is used to ensure the context IDs in the `path` column match between both evaluations of the view.

