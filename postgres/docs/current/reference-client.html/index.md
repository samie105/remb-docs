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
---
This part contains reference information for PostgreSQL client applications and utilities. Not all of these commands are of general utility; some might require special privileges. The common feature of these applications is that they can be run on any host, independent of where the database server resides.

When specified on the command line, user and database names have their case preserved — the presence of spaces or special characters might require quoting. Table names and other identifiers do not have their case preserved, except where documented, and might require quoting.

**Table of Contents**

[clusterdb](https://www.postgresql.org/docs/current/app-clusterdb.html) — cluster a PostgreSQL database

[createdb](https://www.postgresql.org/docs/current/app-createdb.html) — create a new PostgreSQL database

[createuser](https://www.postgresql.org/docs/current/app-createuser.html) — define a new PostgreSQL user account

[dropdb](https://www.postgresql.org/docs/current/app-dropdb.html) — remove a PostgreSQL database

[dropuser](https://www.postgresql.org/docs/current/app-dropuser.html) — remove a PostgreSQL user account

[ecpg](https://www.postgresql.org/docs/current/app-ecpg.html) — embedded SQL C preprocessor

[pg\_amcheck](https://www.postgresql.org/docs/current/app-pgamcheck.html) — checks for corruption in one or more PostgreSQL databases

[pg\_basebackup](https://www.postgresql.org/docs/current/app-pgbasebackup.html) — take a base backup of a PostgreSQL cluster

[pgbench](https://www.postgresql.org/docs/current/pgbench.html) — run a benchmark test on PostgreSQL

[pg\_combinebackup](https://www.postgresql.org/docs/current/app-pgcombinebackup.html) — reconstruct a full backup from an incremental backup and dependent backups

[pg\_config](https://www.postgresql.org/docs/current/app-pgconfig.html) — retrieve information about the installed version of PostgreSQL

[pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) — export a PostgreSQL database as an SQL script or to other formats

[pg\_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html) — extract a PostgreSQL database cluster into a script file

[pg\_isready](https://www.postgresql.org/docs/current/app-pg-isready.html) — check the connection status of a PostgreSQL server

[pg\_receivewal](https://www.postgresql.org/docs/current/app-pgreceivewal.html) — stream write-ahead logs from a PostgreSQL server

[pg\_recvlogical](https://www.postgresql.org/docs/current/app-pgrecvlogical.html) — control PostgreSQL logical decoding streams

[pg\_restore](https://www.postgresql.org/docs/current/app-pgrestore.html) — restore a PostgreSQL database from an archive file created by pg\_dump

[pg\_verifybackup](https://www.postgresql.org/docs/current/app-pgverifybackup.html) — verify the integrity of a base backup of a PostgreSQL cluster

[psql](https://www.postgresql.org/docs/current/app-psql.html) — PostgreSQL interactive terminal

[reindexdb](https://www.postgresql.org/docs/current/app-reindexdb.html) — reindex a PostgreSQL database

[vacuumdb](https://www.postgresql.org/docs/current/app-vacuumdb.html) — garbage-collect and analyze a PostgreSQL database
