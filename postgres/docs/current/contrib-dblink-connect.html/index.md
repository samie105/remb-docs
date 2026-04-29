---
title: "PostgreSQL: Documentation: 18: dblink_connect"
source: "https://www.postgresql.org/docs/current/contrib-dblink-connect.html"
canonical_url: "https://www.postgresql.org/docs/current/contrib-dblink-connect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:39.627Z"
content_hash: "4a1e0b17c46b0f1d2a5028908c46e551ec93fabee497c1643b9e80491a15b6f9"
menu_path: ["PostgreSQL: Documentation: 18: dblink_connect"]
section_path: []
nav_prev: {"path": "../contrib-dblink-connect-u.html/index.md", "title": "PostgreSQL: Documentation: 18: dblink_connect_u"}
nav_next: {"path": "../contrib-dblink-disconnect.html/index.md", "title": "PostgreSQL: Documentation: 18: dblink_disconnect"}
---

dblink\_connect — opens a persistent connection to a remote database

## Synopsis

dblink\_connect(text connstr) returns text
dblink\_connect(text connname, text connstr) returns text

## Description

`dblink_connect()` establishes a connection to a remote PostgreSQL database. The server and database to be contacted are identified through a standard libpq connection string. Optionally, a name can be assigned to the connection. Multiple named connections can be open at once, but only one unnamed connection is permitted at a time. The connection will persist until closed or until the database session is ended.

The connection string may also be the name of an existing foreign server. It is recommended to use the foreign-data wrapper `dblink_fdw` when defining the foreign server. See the example below, as well as [CREATE SERVER](https://www.postgresql.org/docs/current/sql-createserver.html "CREATE SERVER") and [CREATE USER MAPPING](https://www.postgresql.org/docs/current/sql-createusermapping.html "CREATE USER MAPPING").

## Arguments

_`connname`_

The name to use for this connection; if omitted, an unnamed connection is opened, replacing any existing unnamed connection.

_`connstr`_

libpq\-style connection info string, for example `hostaddr=127.0.0.1 port=5432 dbname=mydb user=postgres password=mypasswd options=-csearch_path=`. For details see [Section 32.1.1](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). Alternatively, the name of a foreign server.

## Return Value

Returns status, which is always `OK` (since any error causes the function to throw an error instead of returning).

## Notes

If untrusted users have access to a database that has not adopted a [secure schema usage pattern](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATTERNS "5.10.6. Usage Patterns"), begin each session by removing publicly-writable schemas from `search_path`. One could, for example, add `options=-csearch_path=` to _`connstr`_. This consideration is not specific to `dblink`; it applies to every interface for executing arbitrary SQL commands.

The foreign-data wrapper `dblink_fdw` has an additional Boolean option `use_scram_passthrough` that controls whether `dblink` will use the SCRAM pass-through authentication to connect to the remote database. With SCRAM pass-through authentication, `dblink` uses SCRAM-hashed secrets instead of plain-text user passwords to connect to the remote server. This avoids storing plain-text user passwords in PostgreSQL system catalogs. See the documentation of the equivalent [`use_scram_passthrough`](https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW-OPTION-USE-SCRAM-PASSTHROUGH) option of postgres\_fdw for further details and restrictions.

Only superusers may use `dblink_connect` to create connections that use neither password authentication, SCRAM pass-through, nor GSSAPI-authentication. If non-superusers need this capability, use `dblink_connect_u` instead.

It is unwise to choose connection names that contain equal signs, as this opens a risk of confusion with connection info strings in other `dblink` functions.

## Examples

SELECT dblink\_connect('dbname=postgres options=-csearch\_path=');
 dblink\_connect
----------------
 OK
(1 row)

SELECT dblink\_connect('myconn', 'dbname=postgres options=-csearch\_path=');
 dblink\_connect
----------------
 OK
(1 row)

-- FOREIGN DATA WRAPPER functionality
-- Note: local connections that don't use SCRAM pass-through require password
--       authentication for this to work properly. Otherwise, you will receive
--       the following error from dblink\_connect():
--       ERROR:  password is required
--       DETAIL:  Non-superuser cannot connect if the server does not request a password.
--       HINT:  Target server's authentication method must be changed.

CREATE SERVER fdtest FOREIGN DATA WRAPPER dblink\_fdw OPTIONS (hostaddr '127.0.0.1', dbname 'contrib\_regression');

CREATE USER regress\_dblink\_user WITH PASSWORD 'secret';
CREATE USER MAPPING FOR regress\_dblink\_user SERVER fdtest OPTIONS (user 'regress\_dblink\_user', password 'secret');
GRANT USAGE ON FOREIGN SERVER fdtest TO regress\_dblink\_user;
GRANT SELECT ON TABLE foo TO regress\_dblink\_user;

\\set ORIGINAL\_USER :USER
\\c - regress\_dblink\_user
SELECT dblink\_connect('myconn', 'fdtest');
 dblink\_connect
----------------
 OK
(1 row)

SELECT \* FROM dblink('myconn', 'SELECT \* FROM foo') AS t(a int, b text, c text\[\]);
 a  | b |       c
----+---+---------------
  0 | a | {a0,b0,c0}
  1 | b | {a1,b1,c1}
  2 | c | {a2,b2,c2}
  3 | d | {a3,b3,c3}
  4 | e | {a4,b4,c4}
  5 | f | {a5,b5,c5}
  6 | g | {a6,b6,c6}
  7 | h | {a7,b7,c7}
  8 | i | {a8,b8,c8}
  9 | j | {a9,b9,c9}
 10 | k | {a10,b10,c10}
(11 rows)

\\c - :ORIGINAL\_USER
REVOKE USAGE ON FOREIGN SERVER fdtest FROM regress\_dblink\_user;
REVOKE SELECT ON TABLE foo FROM regress\_dblink\_user;
DROP USER MAPPING FOR regress\_dblink\_user SERVER fdtest;
DROP USER regress\_dblink\_user;
DROP SERVER fdtest;
