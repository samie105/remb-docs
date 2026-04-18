---
title: "PostgreSQL: Documentation: 18: pg_controldata"
source: "https://www.postgresql.org/docs/current/app-pgcontroldata.html"
canonical_url: "https://www.postgresql.org/docs/current/app-pgcontroldata.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:25.084Z"
content_hash: "9bb45bc18bfcf2080a106a262ad693215b3f407ad5ec2d0f7644cad672ab39fa"
menu_path: ["PostgreSQL: Documentation: 18: pg_controldata"]
section_path: []
nav_prev: {"path": "postgres/docs/current/sql-alterforeigntable.html/index.md", "title": "PostgreSQL: Documentation: 18: ALTER FOREIGN TABLE"}
nav_next: {"path": "postgres/docs/current/sql-alterdefaultprivileges.html/index.md", "title": "PostgreSQL: Documentation: 18: ALTER DEFAULT PRIVILEGES"}
---

pg\_controldata — display control information of a PostgreSQL database cluster

## Synopsis

`pg_controldata` \[_`option`_\] \[\[ `-D` | `--pgdata` \]_`datadir`_\]

## Description

`pg_controldata` prints information initialized during `initdb`, such as the catalog version. It also shows information about write-ahead logging and checkpoint processing. This information is cluster-wide, and not specific to any one database.

This utility can only be run by the user who initialized the cluster because it requires read access to the data directory. You can specify the data directory on the command line, or use the environment variable `PGDATA`. This utility supports the options `-V` and `--version`, which print the pg\_controldata version and exit. It also supports options `-?` and `--help`, which output the supported arguments.

## Environment

`PGDATA`

Default data directory location

`PG_COLOR`

Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.


