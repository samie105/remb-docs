---
title: "PostgreSQL: Documentation: 18: pg_walsummary"
source: "https://www.postgresql.org/docs/current/app-pgwalsummary.html"
canonical_url: "https://www.postgresql.org/docs/current/app-pgwalsummary.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:13.425Z"
content_hash: "9b720d747c9961c0a0987db7904482e22cb5fed26dab3c2c7cbb10bd7fb0dea4"
menu_path: ["PostgreSQL: Documentation: 18: pg_walsummary"]
section_path: []
nav_prev: {"path": "postgres/docs/current/ddl-default.html/index.md", "title": "PostgreSQL: Documentation: 18: 5.2.\u00a0Default Values"}
nav_next: {"path": "postgres/docs/current/catalog-pg-namespace.html/index.md", "title": "PostgreSQL: Documentation: 18: 52.32.\u00a0pg_namespace"}
---

pg\_walsummary — print contents of WAL summary files

## Synopsis

`pg_walsummary` \[_`option`_...\] \[_`file`_...\]

## Description

pg\_walsummary is used to print the contents of WAL summary files. These binary files are found with the `pg_wal/summaries` subdirectory of the data directory, and can be converted to text using this tool. This is not ordinarily necessary, since WAL summary files primarily exist to support [incremental backup](https://www.postgresql.org/docs/current/continuous-archiving.html#BACKUP-INCREMENTAL-BACKUP "25.3.3. Making an Incremental Backup"), but it may be useful for debugging purposes.

A WAL summary file is indexed by tablespace OID, relation OID, and relation fork. For each relation fork, it stores the list of blocks that were modified by WAL within the range summarized in the file. It can also store a "limit block," which is 0 if the relation fork was created or truncated within the relevant WAL range, and otherwise the shortest length to which the relation fork was truncated. If the relation fork was not created, deleted, or truncated within the relevant WAL range, the limit block is undefined or infinite and will not be printed by this tool.

## Options

`-i`  
`--individual`

By default, `pg_walsummary` prints one line of output for each range of one or more consecutive modified blocks. This can make the output a lot briefer, since a relation where all blocks from 0 through 999 were modified will produce only one line of output rather than 1000 separate lines. This option requests a separate line of output for every modified block.

`-q`  
`--quiet`

Do not print any output, except for errors. This can be useful when you want to know whether a WAL summary file can be successfully parsed but don't care about the contents.

`-V`  
`--version`

Display version information, then exit.

`-?`  
`--help`

Shows help about pg\_walsummary command line arguments, and exits.

## Environment

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

