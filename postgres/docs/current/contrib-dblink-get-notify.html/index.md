---
title: "PostgreSQL: Documentation: 18: dblink_get_notify"
source: "https://www.postgresql.org/docs/current/contrib-dblink-get-notify.html"
canonical_url: "https://www.postgresql.org/docs/current/contrib-dblink-get-notify.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:09.475Z"
content_hash: "4e09686fa531cdfc054c2b56d065dad36950c8a60cd97072d5f88ad8dfb7a3f4"
menu_path: ["PostgreSQL: Documentation: 18: dblink_get_notify"]
section_path: []
---
dblink\_get\_notify — retrieve async notifications on a connection

## Synopsis

dblink\_get\_notify() returns setof (notify\_name text, be\_pid int, extra text)
dblink\_get\_notify(text connname) returns setof (notify\_name text, be\_pid int, extra text)

## Description

`dblink_get_notify` retrieves notifications on either the unnamed connection, or on a named connection if specified. To receive notifications via dblink, `LISTEN` must first be issued, using `dblink_exec`. For details see [LISTEN](https://www.postgresql.org/docs/current/sql-listen.html "LISTEN") and [NOTIFY](https://www.postgresql.org/docs/current/sql-notify.html "NOTIFY").

## Arguments

_`connname`_

The name of a named connection to get notifications on.

## Return Value

Returns `setof (notify_name text, be_pid int, extra text)`, or an empty set if none.

## Examples

SELECT dblink\_exec('LISTEN virtual');
 dblink\_exec
-------------
 LISTEN
(1 row)

SELECT \* FROM dblink\_get\_notify();
 notify\_name | be\_pid | extra
-------------+--------+-------
(0 rows)

NOTIFY virtual;
NOTIFY

SELECT \* FROM dblink\_get\_notify();
 notify\_name | be\_pid | extra
-------------+--------+-------
 virtual     |   1229 |
(1 row)
