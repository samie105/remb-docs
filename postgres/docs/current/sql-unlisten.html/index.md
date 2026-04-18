---
title: "PostgreSQL: Documentation: 18: UNLISTEN"
source: "https://www.postgresql.org/docs/current/sql-unlisten.html"
canonical_url: "https://www.postgresql.org/docs/current/sql-unlisten.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:04.342Z"
content_hash: "5ccf565fa9d6b287c4accc615945b987288a099bc6c8be94536c1512ef3c1919"
menu_path: ["PostgreSQL: Documentation: 18: UNLISTEN"]
section_path: []
nav_prev: {"path": "postgres/docs/current/view-pg-views.html/index.md", "title": "PostgreSQL: Documentation: 18: 53.37.\u00a0pg_views"}
nav_next: {"path": "postgres/docs/current/spi-spi-gettypeid.html/index.md", "title": "PostgreSQL: Documentation: 18: SPI_gettypeid"}
---

UNLISTEN — stop listening for a notification

## Synopsis

UNLISTEN { _`channel`_ | \* }

## Description

`UNLISTEN` is used to remove an existing registration for `NOTIFY` events. `UNLISTEN` cancels any existing registration of the current PostgreSQL session as a listener on the notification channel named _`channel`_. The special wildcard `*` cancels all listener registrations for the current session.

[NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html "NOTIFY") contains a more extensive discussion of the use of `LISTEN` and `NOTIFY`.

## Parameters

_`channel`_

Name of a notification channel (any identifier).

`*`

All current listen registrations for this session are cleared.

## Notes

You can unlisten something you were not listening for; no warning or error will appear.

At the end of each session, `UNLISTEN *` is automatically executed.

A transaction that has executed `UNLISTEN` cannot be prepared for two-phase commit.

## Examples

To make a registration:

LISTEN virtual;
NOTIFY virtual;
Asynchronous notification "virtual" received from server process with PID 8448.

Once `UNLISTEN` has been executed, further `NOTIFY` messages will be ignored:

UNLISTEN virtual;
NOTIFY virtual;
-- no NOTIFY event is received

## Compatibility

There is no `UNLISTEN` command in the SQL standard.
