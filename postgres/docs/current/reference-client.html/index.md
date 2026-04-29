---
title: "PostgreSQL Client Applications"
source: "https://www.postgresql.org/docs/current/reference-client.html"
canonical_url: "https://www.postgresql.org/docs/current/reference-client.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:45.265Z"
content_hash: "08f460bf5f9f4ca4ea8cf8e359726b34150ebf8aa3c6393ea9c49092140885c8"
menu_path: ["PostgreSQL Client Applications"]
section_path: []
nav_prev: {"path": "../sql-commands.html/index.md", "title": "SQL Commands"}
nav_next: {"path": "../views.html/index.md", "title": "PostgreSQL: Documentation: 18: Chapter\u00a053.\u00a0System Views"}
---

This part contains reference information for PostgreSQL client applications and utilities. Not all of these commands are of general utility; some might require special privileges. The common feature of these applications is that they can be run on any host, independent of where the database server resides.

When specified on the command line, user and database names have their case preserved — the presence of spaces or special characters might require quoting. Table names and other identifiers do not have their case preserved, except where documented, and might require quoting.

**Table of Contents**

[clusterdb](https://www.postgresql.org/docs/current/app-clusterdb.html) — cluster a PostgreSQL database

[createdb](https://www.postgresql.org/docs/current/app-createdb.html) — create a new PostgreSQL database

[createuser](https://www.postgresql.org/docs/current/app-createuser.html) — define a new PostgreSQL user account

[dropdb](../app-dropdb.html/index.md) — remove a PostgreSQL database

[dropuser](https://www.postgresql.org/docs/current/app-dropuser.html) — remove a PostgreSQL user account

[ecpg](https://www.postgresql.org/docs/current/app-ecpg.html) — embedded SQL C preprocessor

[pg\_amcheck](https://www.postgresql.org/docs/current/app-pgamcheck.html) — checks for corruption in one or more PostgreSQL databases

[pg\_basebackup](../app-pgbasebackup.html/index.md) — take a base backup of a PostgreSQL cluster

[pgbench](../pgbench.html/index.md) — run a benchmark test on PostgreSQL

[pg\_combinebackup](https://www.postgresql.org/docs/current/app-pgcombinebackup.html) — reconstruct a full backup from an incremental backup and dependent backups

[pg\_config](https://www.postgresql.org/docs/current/app-pgconfig.html) — retrieve information about the installed version of PostgreSQL

[pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) — export a PostgreSQL database as an SQL script or to other formats

[pg\_dumpall](../app-pg-dumpall.html/index.md) — extract a PostgreSQL database cluster into a script file

[pg\_isready](https://www.postgresql.org/docs/current/app-pg-isready.html) — check the connection status of a PostgreSQL server

[pg\_receivewal](../app-pgreceivewal.html/index.md) — stream write-ahead logs from a PostgreSQL server

[pg\_recvlogical](../app-pgrecvlogical.html/index.md) — control PostgreSQL logical decoding streams

[pg\_restore](../app-pgrestore.html/index.md) — restore a PostgreSQL database from an archive file created by pg\_dump

[pg\_verifybackup](../app-pgverifybackup.html/index.md) — verify the integrity of a base backup of a PostgreSQL cluster

[psql](../app-psql.html/index.md) — PostgreSQL interactive terminal

[reindexdb](../app-reindexdb.html/index.md) — reindex a PostgreSQL database

[vacuumdb](../app-vacuumdb.html/index.md) — garbage-collect and analyze a PostgreSQL database
