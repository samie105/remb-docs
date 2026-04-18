---
title: "PostgreSQL: Documentation: 18: 53.35. pg_user"
source: "https://www.postgresql.org/docs/current/view-pg-user.html"
canonical_url: "https://www.postgresql.org/docs/current/view-pg-user.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:26.759Z"
content_hash: "3c0c8d46045d06aaa4efebb116dab9d45daa04257b8c6454653e33a43a86a259"
menu_path: ["PostgreSQL: Documentation: 18: 53.35. pg_user"]
section_path: []
nav_prev: {"path": "postgres/docs/current/wal-intro.html/index.md", "title": "PostgreSQL: Documentation: 18: 28.3.\u00a0Write-Ahead Logging (WAL)"}
nav_next: {"path": "postgres/docs/current/app-pgcreatesubscriber.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_createsubscriber"}
---

The view `pg_user` provides access to information about database users. This is simply a publicly readable view of [`pg_shadow`](https://www.postgresql.org/docs/current/view-pg-shadow.html "53.26. pg_shadow") that blanks out the password field.

**Table 53.35. `pg_user` Columns**

Column Type

Description

`usename` `name`

User name

`usesysid` `oid`

ID of this user

`usecreatedb` `bool`

User can create databases

`usesuper` `bool`

User is a superuser

`userepl` `bool`

User can initiate streaming replication and put the system in and out of backup mode.

`usebypassrls` `bool`

User bypasses every row-level security policy, see [Section 5.9](https://www.postgresql.org/docs/current/ddl-rowsecurity.html "5.9. Row Security Policies") for more information.

`passwd` `text`

Not the password (always reads as `********`)

`valuntil` `timestamptz`

Password expiry time (only used for password authentication)

`useconfig` `text[]`

Session defaults for run-time configuration variables

