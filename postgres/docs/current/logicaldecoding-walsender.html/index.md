---
title: "PostgreSQL: Documentation: 18: 47.3. Streaming Replication Protocol Interface"
source: "https://www.postgresql.org/docs/current/logicaldecoding-walsender.html"
canonical_url: "https://www.postgresql.org/docs/current/logicaldecoding-walsender.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:49:24.214Z"
content_hash: "3eee4285cb4b50207cc5a74b3df21aa669268b893dee52c3f93a7f031db00e2a"
menu_path: ["PostgreSQL: Documentation: 18: 47.3. Streaming Replication Protocol Interface"]
section_path: []
content_language: "en"
---
The commands

-   ``CREATE_REPLICATION_SLOT _`slot_name`_ LOGICAL _`output_plugin`_``
    
-   ``DROP_REPLICATION_SLOT _`slot_name`_`` \[ `WAIT` \]
    
-   ``START_REPLICATION SLOT _`slot_name`_ LOGICAL ...``
    

are used to create, drop, and stream changes from a replication slot, respectively. These commands are only available over a replication connection; they cannot be used via SQL. See [Section 54.4](https://www.postgresql.org/docs/current/protocol-replication.html "54.4. Streaming Replication Protocol") for details on these commands.

The command [pg\_recvlogical](https://www.postgresql.org/docs/current/app-pgrecvlogical.html "pg_recvlogical") can be used to control logical decoding over a streaming replication connection. (It uses these commands internally.)
