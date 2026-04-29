---
title: "PostgreSQL: Documentation: 18: dropdb"
source: "https://www.postgresql.org/docs/current/app-dropdb.html"
canonical_url: "https://www.postgresql.org/docs/current/app-dropdb.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:45.756Z"
content_hash: "f96290942cef79734756e39da656e2510e6b90b3092034c629dc4b33ef4d3c0b"
menu_path: ["PostgreSQL: Documentation: 18: dropdb"]
section_path: []
nav_prev: {"path": "postgres/docs/current/amcheck.html/index.md", "title": "PostgreSQL: Documentation: 18: F.1.\u00a0amcheck \u2014 tools to verify table and index consistency"}
nav_next: {"path": "postgres/docs/current/app-pg-ctl.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_ctl"}
---

dropdb — remove a PostgreSQL database

## Synopsis

`dropdb` \[_`connection-option`_...\] \[_`option`_...\] _`dbname`_

## Description

dropdb destroys an existing PostgreSQL database. The user who executes this command must be a database superuser or the owner of the database.

dropdb is a wrapper around the SQL command [`DROP DATABASE`](https://www.postgresql.org/docs/current/sql-dropdatabase.html "DROP DATABASE"). There is no effective difference between dropping databases via this utility and via other methods for accessing the server.

## Options

dropdb accepts the following command-line arguments:

_`dbname`_

Specifies the name of the database to be removed.

`-e`  
`--echo`

Echo the commands that dropdb generates and sends to the server.

`-f`  
`--force`

Attempt to terminate all existing connections to the target database before dropping it. See [DROP DATABASE](https://www.postgresql.org/docs/current/sql-dropdatabase.html "DROP DATABASE") for more information on this option.

`-i`  
`--interactive`

Issues a verification prompt before doing anything destructive.

`-V`  
`--version`

Print the dropdb version and exit.

`--if-exists`

Do not throw an error if the database does not exist. A notice is issued in this case.

`-?`  
`--help`

Show help about dropdb command line arguments, and exit.

dropdb also accepts the following command-line arguments for connection parameters:

``-h _`host`_``  
``--host=_`host`_``

Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket.

``-p _`port`_``  
``--port=_`port`_``

Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections.

``-U _`username`_``  
``--username=_`username`_``

User name to connect as.

`-w`  
`--no-password`

Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.

`-W`  
`--password`

Force dropdb to prompt for a password before connecting to a database.

This option is never essential, since dropdb will automatically prompt for a password if the server demands password authentication. However, dropdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

``--maintenance-db=_`dbname`_``

Specifies the name of the database to connect to in order to drop the target database. If not specified, the `postgres` database will be used; if that does not exist (or is the database being dropped), `template1` will be used. This can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options.

## Environment

`PGHOST`  
`PGPORT`  
`PGUSER`

Default connection parameters

`PG_COLOR`

Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see [Section 32.15](https://www.postgresql.org/docs/current/libpq-envars.html "32.15. Environment Variables")).

## Diagnostics

In case of difficulty, see [DROP DATABASE](https://www.postgresql.org/docs/current/sql-dropdatabase.html "DROP DATABASE") and [psql](https://www.postgresql.org/docs/current/app-psql.html "psql") for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.

## Examples

To destroy the database `demo` on the default database server:

```
$ 
```

To destroy the database `demo` using the server on host `eden`, port 5000, with verification and a peek at the underlying command:

```
$ 
```
