---
title: "PostgreSQL: Documentation: 18: 33.2. Implementation Features"
source: "https://www.postgresql.org/docs/current/lo-implementation.html"
canonical_url: "https://www.postgresql.org/docs/current/lo-implementation.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:48.646Z"
content_hash: "d58860134f035069353fdc6e33458ecee9b2e2a943957f0635ec0c89b6116354"
menu_path: ["PostgreSQL: Documentation: 18: 33.2. Implementation Features"]
section_path: []
---
The large object implementation breaks large objects up into “chunks” and stores the chunks in rows in the database. A B-tree index guarantees fast searches for the correct chunk number when doing random access reads and writes.

The chunks stored for a large object do not have to be contiguous. For example, if an application opens a new large object, seeks to offset 1000000, and writes a few bytes there, this does not result in allocation of 1000000 bytes worth of storage; only of chunks covering the range of data bytes actually written. A read operation will, however, read out zeroes for any unallocated locations preceding the last existing chunk. This corresponds to the common behavior of “sparsely allocated” files in Unix file systems.

As of PostgreSQL 9.0, large objects have an owner and a set of access permissions, which can be managed using [GRANT](https://www.postgresql.org/docs/current/sql-grant.html "GRANT") and [REVOKE](https://www.postgresql.org/docs/current/sql-revoke.html "REVOKE"). `SELECT` privileges are required to read a large object, and `UPDATE` privileges are required to write or truncate it. Only the large object's owner (or a database superuser) can delete, comment on, or change the owner of a large object. To adjust this behavior for compatibility with prior releases, see the [lo\_compat\_privileges](https://www.postgresql.org/docs/current/runtime-config-compatible.html#GUC-LO-COMPAT-PRIVILEGES) run-time parameter.
