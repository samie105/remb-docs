---
title: "PostgreSQL: Documentation: 18: reindexdb"
source: "https://www.postgresql.org/docs/current/app-reindexdb.html"
canonical_url: "https://www.postgresql.org/docs/current/app-reindexdb.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:03.138Z"
content_hash: "2dc600c3cc2f8e3b9f4176207aa44bec7aa4564d802aa4a300052c35cea82357"
menu_path: ["PostgreSQL: Documentation: 18: reindexdb"]
section_path: []
---
reindexdb — reindex a PostgreSQL database

## Synopsis

`reindexdb` \[_`connection-option`_...\] \[_`option`_...\] \[ `-S` | `--schema` _`schema`_ \] ... \[ `-t` | `--table` _`table`_ \] ... \[ `-i` | `--index` _`index`_ \] ... \[ `-s` | `--system` \] \[ _`dbname`_ | `-a` | `--all` \]

## Description

reindexdb is a utility for rebuilding indexes in a PostgreSQL database.

reindexdb is a wrapper around the SQL command [`REINDEX`](https://www.postgresql.org/docs/current/sql-reindex.html "REINDEX"). There is no effective difference between reindexing databases via this utility and via other methods for accessing the server.

## Options

reindexdb accepts the following command-line arguments:

`-a`  
`--all`

Reindex all databases.

`--concurrently`

Use the `CONCURRENTLY` option. See [REINDEX](https://www.postgresql.org/docs/current/sql-reindex.html "REINDEX"), where all the caveats of this option are explained in detail.

``[-d] _`dbname`_``  
``[--dbname=]_`dbname`_``

Specifies the name of the database to be reindexed, when `-a`/`--all` is not used. If this is not specified, the database name is read from the environment variable `PGDATABASE`. If that is not set, the user name specified for the connection is used. The _`dbname`_ can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options.

`-e`  
`--echo`

Echo the commands that reindexdb generates and sends to the server.

``-i _`index`_``  
``--index=_`index`_``

Recreate _`index`_ only. Multiple indexes can be recreated by writing multiple `-i` switches.

``-j _`njobs`_``  
``--jobs=_`njobs`_``

Execute the reindex commands in parallel by running _`njobs`_ commands simultaneously. This option may reduce the processing time but it also increases the load on the database server.

reindexdb will open _`njobs`_ connections to the database, so make sure your [max\_connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS) setting is high enough to accommodate all connections.

Note that this option is incompatible with the `--system` option.

`-q`  
`--quiet`

Do not display progress messages.

`-s`  
`--system`

Reindex database's system catalogs only.

``-S _`schema`_``  
``--schema=_`schema`_``

Reindex _`schema`_ only. Multiple schemas can be reindexed by writing multiple `-S` switches.

``-t _`table`_``  
``--table=_`table`_``

Reindex _`table`_ only. Multiple tables can be reindexed by writing multiple `-t` switches.

``--tablespace=_`tablespace`_``

Specifies the tablespace where indexes are rebuilt. (This name is processed as a double-quoted identifier.)

`-v`  
`--verbose`

Print detailed information during processing.

`-V`  
`--version`

Print the reindexdb version and exit.

`-?`  
`--help`

Show help about reindexdb command line arguments, and exit.

reindexdb also accepts the following command-line arguments for connection parameters:

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

Force reindexdb to prompt for a password before connecting to a database.

This option is never essential, since reindexdb will automatically prompt for a password if the server demands password authentication. However, reindexdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

``--maintenance-db=_`dbname`_``

When the `-a`/`--all` is used, connect to this database to gather the list of databases to reindex. If not specified, the `postgres` database will be used, or if that does not exist, `template1` will be used. This can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options. Also, connection string parameters other than the database name itself will be re-used when connecting to other databases.

## Environment

`PGDATABASE`  
`PGHOST`  
`PGPORT`  
`PGUSER`

Default connection parameters

`PG_COLOR`

Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see [Section 32.15](https://www.postgresql.org/docs/current/libpq-envars.html "32.15. Environment Variables")).

## Diagnostics

In case of difficulty, see [REINDEX](https://www.postgresql.org/docs/current/sql-reindex.html "REINDEX") and [psql](https://www.postgresql.org/docs/current/app-psql.html "psql") for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.

## Examples

To reindex the database `test`:

```
$ 
```

To reindex the table `foo` and the index `bar` in a database named `abcd`:

```
$ 
```
