---
title: "PostgreSQL: Documentation: 18: dblink_disconnect"
source: "https://www.postgresql.org/docs/current/contrib-dblink-disconnect.html"
canonical_url: "https://www.postgresql.org/docs/current/contrib-dblink-disconnect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:13.190Z"
content_hash: "fbc8a62e667aab638798e2d8d0d98f4c4d2d6cbaf58d43d683dd7a384d84b378"
menu_path: ["PostgreSQL: Documentation: 18: dblink_disconnect"]
section_path: []
nav_prev: {"path": "postgres/docs/current/spi-visibility.html/index.md", "title": "PostgreSQL: Documentation: 18: 45.5.\u00a0Visibility of Data Changes"}
nav_next: {"path": "postgres/docs/current/sql-dropdomain.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP DOMAIN"}
---

February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/contrib-dblink-disconnect.html "PostgreSQL 18 - dblink_disconnect") ([18](/docs/18/contrib-dblink-disconnect.html "PostgreSQL 18 - dblink_disconnect")) / [17](/docs/17/contrib-dblink-disconnect.html "PostgreSQL 17 - dblink_disconnect") / [16](/docs/16/contrib-dblink-disconnect.html "PostgreSQL 16 - dblink_disconnect") / [15](/docs/15/contrib-dblink-disconnect.html "PostgreSQL 15 - dblink_disconnect") / [14](/docs/14/contrib-dblink-disconnect.html "PostgreSQL 14 - dblink_disconnect")

Development Versions: [devel](/docs/devel/contrib-dblink-disconnect.html "PostgreSQL devel - dblink_disconnect")

Unsupported versions: [13](/docs/13/contrib-dblink-disconnect.html "PostgreSQL 13 - dblink_disconnect") / [12](/docs/12/contrib-dblink-disconnect.html "PostgreSQL 12 - dblink_disconnect") / [11](/docs/11/contrib-dblink-disconnect.html "PostgreSQL 11 - dblink_disconnect") / [10](/docs/10/contrib-dblink-disconnect.html "PostgreSQL 10 - dblink_disconnect") / [9.6](/docs/9.6/contrib-dblink-disconnect.html "PostgreSQL 9.6 - dblink_disconnect") / [9.5](/docs/9.5/contrib-dblink-disconnect.html "PostgreSQL 9.5 - dblink_disconnect") / [9.4](/docs/9.4/contrib-dblink-disconnect.html "PostgreSQL 9.4 - dblink_disconnect") / [9.3](/docs/9.3/contrib-dblink-disconnect.html "PostgreSQL 9.3 - dblink_disconnect") / [9.2](/docs/9.2/contrib-dblink-disconnect.html "PostgreSQL 9.2 - dblink_disconnect") / [9.1](/docs/9.1/contrib-dblink-disconnect.html "PostgreSQL 9.1 - dblink_disconnect") / [9.0](/docs/9.0/contrib-dblink-disconnect.html "PostgreSQL 9.0 - dblink_disconnect") / [8.4](/docs/8.4/contrib-dblink-disconnect.html "PostgreSQL 8.4 - dblink_disconnect") / [8.3](/docs/8.3/contrib-dblink-disconnect.html "PostgreSQL 8.3 - dblink_disconnect")

## dblink\_disconnect

dblink\_disconnect — closes a persistent connection to a remote database

## Synopsis

dblink\_disconnect() returns text
dblink\_disconnect(text connname) returns text

## Description

`dblink_disconnect()` closes a connection previously opened by `dblink_connect()`. The form with no arguments closes an unnamed connection.

## Arguments

_`connname`_

The name of a named connection to be closed.

## Return Value

Returns status, which is always `OK` (since any error causes the function to throw an error instead of returning).

## Examples

SELECT dblink\_disconnect();
 dblink\_disconnect
-------------------
 OK
(1 row)

SELECT dblink\_disconnect('myconn');
 dblink\_disconnect
-------------------
 OK
(1 row)

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/contrib-dblink-disconnect.html/) to report a documentation issue.
