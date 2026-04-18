---
title: "PostgreSQL: Documentation: 18: 47.3. Streaming Replication Protocol Interface"
source: "https://www.postgresql.org/docs/current/logicaldecoding-walsender.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-walsender.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:40.749Z"
content_hash: "c7c42c65532f9991a9e8a2e65ce1aaa882ddf3741cab2e6513bc114612a7917a"
menu_path: ["PostgreSQL: Documentation: 18: 47.3. Streaming Replication Protocol Interface"]
section_path: []
nav_prev: {"path": "postgres/docs/current/contrib-dblink-connect.html/index.md", "title": "PostgreSQL: Documentation: 18: dblink_connect"}
nav_next: {"path": "postgres/docs/current/query-path.html/index.md", "title": "PostgreSQL: Documentation: 18: 51.1.\u00a0The Path of a Query"}
---

The commands

*   ``CREATE_REPLICATION_SLOT _`slot_name`_ LOGICAL _`output_plugin`_``
    
*   ``DROP_REPLICATION_SLOT _`slot_name`_`` \[ `WAIT` \]
    
*   ``START_REPLICATION SLOT _`slot_name`_ LOGICAL ...``
    

are used to create, drop, and stream changes from a replication slot, respectively. These commands are only available over a replication connection; they cannot be used via SQL. See [Section 54.4](https://www.postgresql.org/docs/current/protocol-replication.html "54.4. Streaming Replication Protocol") for details on these commands.

The command [pg\_recvlogical](https://www.postgresql.org/docs/current/app-pgrecvlogical.html "pg_recvlogical") can be used to control logical decoding over a streaming replication connection. (It uses these commands internally.)


