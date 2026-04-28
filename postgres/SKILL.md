## Overview

PostgreSQL is an open-source object-relational database management system that emphasizes extensibility, standards compliance, and durability through its process-per-connection architecture and Write-Ahead Log (WAL). An agent needs fluency in Postgres to run queries, automate backups, tune replication and connection behavior, and troubleshoot corruption or performance issues using its CLI tools and configuration hierarchy.

## Mental Model

Postgres separates client utilities from the server process: each connection gets its own backend process, while shared memory and WAL coordinate durability and recovery. The configuration layer (`runtime-config-*`) controls everything from connection limits to replication semantics, and the client application suite (`app-*`) provides discrete tools for backup, maintenance, and benchmarking. Start with the WAL and connection runtime pages to understand durability and access, then use the client reference index to map the toolset to operational tasks.

## Learning Paths

**Getting Started**
1. `postgres/docs/current/app-psql.html/index.md` — Query and administer via the interactive terminal.
2. `postgres/docs/current/acronyms.html/index.md` — Decode terminology used across the documentation.
3. `postgres/docs/current/reference-client.html/index.md` — Orient yourself to the full client application suite.

**Production Operations**
1. `postgres/docs/current/app-pg-ctl.html/index.md` — Manage server startup, shutdown, and signaling.
2. `postgres/docs/current/app-pgbasebackup.html/index.md` — Take physical base backups for PITR.
3. `postgres/docs/current/app-pgverifybackup.html/index.md` — Confirm backup integrity before relying on it.
4. `postgres/docs/current/app-pgchecksums.html/index.md` — Enable and verify data-page checksums.
5. `postgres/docs/current/amcheck.html/index.md` — Detect table and index corruption early.

**Migration, Replication & Benchmarking**
1. `postgres/docs/current/app-pg-dumpall.html/index.md` — Export all databases and global objects.
2. `postgres/docs/current/app-pgrestore.html/index.md` — Restore selected objects from archives.
3. `postgres/docs/current/app-pgreceivewal.html/index.md` — Stream WAL for archiving or standby setup.
4. `postgres/docs/current/app-pgrecvlogical.html/index.md` — Consume logical replication streams.
5. `postgres/docs/current/pgbench.html/index.md` — Benchmark throughput and locking behavior.

## Concept Map

- **Interactive Access & Terminology**
  - SQL shell and scripting: `postgres/docs/current/app-psql.html/index.md`
  - Glossary of acronyms: `postgres/docs/current/acronyms.html/index.md`
  - Client application index: `postgres/docs/current/reference-client.html/index.md`

- **Server Control & Configuration**
  - Server lifecycle management: `postgres/docs/current/app-pg-ctl.html/index.md`
  - WAL and durability settings: `postgres/docs/current/runtime-config-wal.html/index.md`
  - Connection and authentication limits: `postgres/docs/current/runtime-config-connection.html/index.md`
  - Replication configuration: `postgres/docs/current/runtime-config-replication.html/index.md`

- **Backup, Restore & Verification**
  - Physical base backup: `postgres/docs/current/app-pgbasebackup.html/index.md`
  - Backup integrity check: `postgres/docs/current/app-pgverifybackup.html/index.md`
  - Cluster-wide logical export: `postgres/docs/current/app-pg-dumpall.html/index.md`
  - Selective archive restore: `postgres/docs/current/app-pgrestore.html/index.md`

- **Replication & Archiving**
  - WAL streaming client: `postgres/docs/current/app-pgreceivewal.html/index.md`
  - Logical decoding client: `postgres/docs/current/app-pgrecvlogical.html/index.md`

- **Maintenance, Integrity & Performance**
  - Data-page checksums: `postgres/docs/current/app-pgchecksums.html/index.md`
  - Table and index consistency: `postgres/docs/current/amcheck.html/index.md`
  - Index rebuilding: `postgres/docs/current/app-reindexdb.html/index.md`
  - Database removal: `postgres/docs/current/app-dropdb.html/index.md`
  - Load testing: `postgres/docs/current/pgbench.html/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Run ad-hoc SQL or admin scripts | `postgres/docs/current/app-psql.html/index.md` |
| Start, stop, or reload the server | `postgres/docs/current/app-pg-ctl.html/index.md` |
| Back up the entire data directory | `postgres/docs/current/app-pgbasebackup.html/index.md` |
| Verify a backup before a restore | `postgres/docs/current/app-pgverifybackup.html/index.md` |
| Export all databases and globals | `postgres/docs/current/app-pg-dumpall.html/index.md` |
| Restore objects from a custom archive | `postgres/docs/current/app-pgrestore.html/index.md` |
| Stream WAL for a standby or archive | `postgres/docs/current/app-pgreceivewal.html/index.md` |
| Read logical change streams | `postgres/docs/current/app-pgrecvlogical.html/index.md` |
| Check for table or index corruption | `postgres/docs/current/amcheck.html/index.md` |
| Rebuild indexes after bloat or errors | `postgres/docs/current/app-reindexdb.html/index.md` |
| Remove a database | `postgres/docs/current/app-dropdb.html/index.md` |
| Benchmark throughput and latency | `postgres/docs/current/pgbench.html/index.md` |
| Tune WAL or replication behavior | `postgres/docs/current/runtime-config-wal.html/index.md` |
| Tune connections and authentication | `postgres/docs/current/runtime-config-connection.html/index.md` |
| Decode Postgres acronyms | `postgres/docs/current/acronyms.html/index.md` |

## Top Must-Know Pages

1. `postgres/docs/current/app-psql.html/index.md` — The interactive terminal for daily queries, scripting, and administration.
2. `postgres/docs/current/app-pgbasebackup.html/index.md` — The standard tool for physical backups and PITR foundations.
3. `postgres/docs/current/app-pg-ctl.html/index.md` — Controls server initialization, startup, shutdown, and restarts.
4. `postgres/docs/current/runtime-config-wal.html/index.md` — Governs durability, archiving, and replication through WAL parameters.
5. `postgres/docs/current/app-pgreceivewal.html/index.md` — Streams WAL segments in real time to archives or standbys.
6. `postgres/docs/current/app-pg-dumpall.html/index.md` — Exports cluster-wide data and global objects for migrations.
7. `postgres/docs/current/app-reindexdb.html/index.md` — Rebuilds indexes across databases after corruption or bloat.
8. `postgres/docs/current/amcheck.html/index.md` — Verifies logical and physical consistency of tables and indexes.
9. `postgres/docs/current/app-pgverifybackup.html/index.md` — Validates that a base backup is complete and restorable.
10. `postgres/docs/current/reference-client.html/index.md` — The canonical index of every official client application.