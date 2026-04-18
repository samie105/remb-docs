---
title: "PostgreSQL: Documentation: 18: dblink_fetch"
source: "https://www.postgresql.org/docs/current/contrib-dblink-fetch.html"
canonical_url: "https://www.postgresql.org/docs/current/contrib-dblink-fetch.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:43.598Z"
content_hash: "53fbfe63b28b880fbc137acb3e47bfedadef45693e620a0b89a408ac399b1f53"
menu_path: ["PostgreSQL: Documentation: 18: dblink_fetch"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-pgchecksums.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_checksums"}
nav_next: {"path": "postgres/docs/current/sql-dropindex.html/index.md", "title": "PostgreSQL: Documentation: 18: DROP INDEX"}
---

dblink\_fetch — returns rows from an open cursor in a remote database

## Synopsis

dblink\_fetch(text cursorname, int howmany \[, bool fail\_on\_error\]) returns setof record
dblink\_fetch(text connname, text cursorname, int howmany \[, bool fail\_on\_error\]) returns setof record

## Description

`dblink_fetch` fetches rows from a cursor previously established by `dblink_open`.

## Arguments

_`connname`_

Name of the connection to use; omit this parameter to use the unnamed connection.

_`cursorname`_

The name of the cursor to fetch from.

_`howmany`_

The maximum number of rows to retrieve. The next _`howmany`_ rows are fetched, starting at the current cursor position, moving forward. Once the cursor has reached its end, no more rows are produced.

_`fail_on_error`_

If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function returns no rows.

## Return Value

The function returns the row(s) fetched from the cursor. To use this function, you will need to specify the expected set of columns, as previously discussed for `dblink`.

## Notes

On a mismatch between the number of return columns specified in the `FROM` clause, and the actual number of columns returned by the remote cursor, an error will be thrown. In this event, the remote cursor is still advanced by as many rows as it would have been if the error had not occurred. The same is true for any other error occurring in the local query after the remote `FETCH` has been done.

## Examples

SELECT dblink\_connect('dbname=postgres options=-csearch\_path=');
 dblink\_connect
----------------
 OK
(1 row)

SELECT dblink\_open('foo', 'select proname, prosrc from pg\_proc where proname like ''bytea%''');
 dblink\_open
-------------
 OK
(1 row)

SELECT \* FROM dblink\_fetch('foo', 5) AS (funcname name, source text);
 funcname |  source
----------+----------
 byteacat | byteacat
 byteacmp | byteacmp
 byteaeq  | byteaeq
 byteage  | byteage
 byteagt  | byteagt
(5 rows)

SELECT \* FROM dblink\_fetch('foo', 5) AS (funcname name, source text);
 funcname  |  source
-----------+-----------
 byteain   | byteain
 byteale   | byteale
 bytealike | bytealike
 bytealt   | bytealt
 byteane   | byteane
(5 rows)

SELECT \* FROM dblink\_fetch('foo', 5) AS (funcname name, source text);
  funcname  |   source
------------+------------
 byteanlike | byteanlike
 byteaout   | byteaout
(2 rows)

SELECT \* FROM dblink\_fetch('foo', 5) AS (funcname name, source text);
 funcname | source
----------+--------
(0 rows)
