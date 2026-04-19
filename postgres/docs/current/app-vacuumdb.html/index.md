---
title: "PostgreSQL: Documentation: 18: vacuumdb"
source: "https://www.postgresql.org/docs/current/app-vacuumdb.html"
canonical_url: "https://www.postgresql.org/docs/current/app-vacuumdb.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:40.562Z"
content_hash: "dc3b0dc5bc2c4d44837f530c2fd6fb770bce636bbc9d91a34c1c139cd755dd85"
menu_path: ["PostgreSQL: Documentation: 18: vacuumdb"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-reindexdb.html/index.md", "title": "PostgreSQL: Documentation: 18: reindexdb"}
nav_next: {"path": "postgres/docs/current/basic-archive.html/index.md", "title": "PostgreSQL: Documentation: 18: F.5.\u00a0basic_archive \u2014 an example WAL archive module"}
---

vacuumdb — garbage-collect and analyze a PostgreSQL database

## Synopsis

`vacuumdb` \[_`connection-option`_...\] \[_`option`_...\] \[ `-t` | `--table` _`table`_ \[( _`column`_ \[,...\] )\] \] ... \[ _`dbname`_ | `-a` | `--all` \]

`vacuumdb` \[_`connection-option`_...\] \[_`option`_...\] \[ `-n` | `--schema` _`schema`_ \] ... \[ _`dbname`_ | `-a` | `--all` \]

`vacuumdb` \[_`connection-option`_...\] \[_`option`_...\] \[ `-N` | `--exclude-schema` _`schema`_ \] ... \[ _`dbname`_ | `-a` | `--all` \]

## Description

vacuumdb is a utility for cleaning a PostgreSQL database. vacuumdb will also generate internal statistics used by the PostgreSQL query optimizer.

vacuumdb is a wrapper around the SQL command [`VACUUM`](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM"). There is no effective difference between vacuuming and analyzing databases via this utility and via other methods for accessing the server.

## Options

vacuumdb accepts the following command-line arguments:

`-a`  
`--all`

Vacuum all databases.

``--buffer-usage-limit _`size`_``

Specifies the [](postgres/docs/current/glossary.html/index.md#GLOSSARY-BUFFER-ACCESS-STRATEGY)[Buffer Access Strategy](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-BUFFER-ACCESS-STRATEGY "Buffer Access Strategy") ring buffer size for a given invocation of vacuumdb. This size is used to calculate the number of shared buffers which will be reused as part of this strategy. See [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM").

``[-d] _`dbname`_``  
``[--dbname=]_`dbname`_``

Specifies the name of the database to be cleaned or analyzed, when `-a`/`--all` is not used. If this is not specified, the database name is read from the environment variable `PGDATABASE`. If that is not set, the user name specified for the connection is used. The _`dbname`_ can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options.

`--disable-page-skipping`

Disable skipping pages based on the contents of the visibility map.

`-e`  
`--echo`

Echo the commands that vacuumdb generates and sends to the server.

`-f`  
`--full`

Perform “full” vacuuming.

`-F`  
`--freeze`

Aggressively “freeze” tuples.

`--force-index-cleanup`

Always remove index entries pointing to dead tuples.

``-j _`njobs`_``  
``--jobs=_`njobs`_``

Execute the vacuum or analyze commands in parallel by running _`njobs`_ commands simultaneously. This option may reduce the processing time but it also increases the load on the database server.

vacuumdb will open _`njobs`_ connections to the database, so make sure your [max\_connections](postgres/docs/current/runtime-config-connection.html/index.md#GUC-MAX-CONNECTIONS) setting is high enough to accommodate all connections.

Note that using this mode together with the `-f` (`FULL`) option might cause deadlock failures if certain system catalogs are processed in parallel.

``--min-mxid-age _`mxid_age`_``

Only execute the vacuum or analyze commands on tables with a multixact ID age of at least _`mxid_age`_. This setting is useful for prioritizing tables to process to prevent multixact ID wraparound (see [Section 24.1.5.1](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-MULTIXACT-WRAPAROUND "24.1.5.1. Multixacts and Wraparound")).

For the purposes of this option, the multixact ID age of a relation is the greatest of the ages of the main relation and its associated TOAST table, if one exists. Since the commands issued by vacuumdb will also process the TOAST table for the relation if necessary, it does not need to be considered separately.

``--min-xid-age _`xid_age`_``

Only execute the vacuum or analyze commands on tables with a transaction ID age of at least _`xid_age`_. This setting is useful for prioritizing tables to process to prevent transaction ID wraparound (see [Section 24.1.5](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "24.1.5. Preventing Transaction ID Wraparound Failures")).

For the purposes of this option, the transaction ID age of a relation is the greatest of the ages of the main relation and its associated TOAST table, if one exists. Since the commands issued by vacuumdb will also process the TOAST table for the relation if necessary, it does not need to be considered separately.

`--missing-stats-only`

Only analyze relations that are missing statistics for a column, index expression, or extended statistics object. When used with `--analyze-in-stages`, this option prevents vacuumdb from temporarily replacing existing statistics with ones generated with lower statistics targets, thus avoiding transiently worse query optimizer choices.

This option can only be used in conjunction with `--analyze-only` or `--analyze-in-stages`.

Note that `--missing-stats-only` requires `SELECT` privileges on [`pg_statistic`](https://www.postgresql.org/docs/current/catalog-pg-statistic.html "52.51. pg_statistic") and [`pg_statistic_ext_data`](https://www.postgresql.org/docs/current/catalog-pg-statistic-ext-data.html "52.53. pg_statistic_ext_data"), which are restricted to superusers by default.

``-n _`schema`_``  
``--schema=_`schema`_``

Clean or analyze all tables in _`schema`_ only. Multiple schemas can be vacuumed by writing multiple `-n` switches.

``-N _`schema`_``  
``--exclude-schema=_`schema`_``

Do not clean or analyze any tables in _`schema`_. Multiple schemas can be excluded by writing multiple `-N` switches.

`--no-index-cleanup`

Do not remove index entries pointing to dead tuples.

`--no-process-main`

Skip the main relation.

`--no-process-toast`

Skip the TOAST table associated with the table to vacuum, if any.

`--no-truncate`

Do not truncate empty pages at the end of the table.

``-P _`parallel_workers`_``  
``--parallel=_`parallel_workers`_``

Specify the number of parallel workers for _parallel vacuum_. This allows the vacuum to leverage multiple CPUs to process indexes. See [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM").

`-q`  
`--quiet`

Do not display progress messages.

`--skip-locked`

Skip relations that cannot be immediately locked for processing.

``-t _`table`_ [ (_`column`_ [,...]) ]``  
``--table=_`table`_ [ (_`column`_ [,...]) ]``

Clean or analyze _`table`_ only. Column names can be specified only in conjunction with the `--analyze` or `--analyze-only` options. Multiple tables can be vacuumed by writing multiple `-t` switches.

### Tip

If you specify columns, you probably have to escape the parentheses from the shell. (See examples below.)

`-v`  
`--verbose`

Print detailed information during processing.

`-V`  
`--version`

Print the vacuumdb version and exit.

`-z`  
`--analyze`

Also calculate statistics for use by the optimizer.

`-Z`  
`--analyze-only`

Only calculate statistics for use by the optimizer (no vacuum).

`--analyze-in-stages`

Only calculate statistics for use by the optimizer (no vacuum), like `--analyze-only`. Run three stages of analyze; the first stage uses the lowest possible statistics target (see [default\_statistics\_target](postgres/docs/current/runtime-config-query.html/index.md#GUC-DEFAULT-STATISTICS-TARGET)) to produce usable statistics faster, and subsequent stages build the full statistics.

This option is only useful to analyze a database that currently has no statistics or has wholly incorrect ones, such as if it is newly populated from a restored dump or by `pg_upgrade`. Be aware that running with this option in a database with existing statistics may cause the query optimizer choices to become transiently worse due to the low statistics targets of the early stages.

`-?`  
`--help`

Show help about vacuumdb command line arguments, and exit.

vacuumdb also accepts the following command-line arguments for connection parameters:

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

Force vacuumdb to prompt for a password before connecting to a database.

This option is never essential, since vacuumdb will automatically prompt for a password if the server demands password authentication. However, vacuumdb will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

``--maintenance-db=_`dbname`_``

When the `-a`/`--all` is used, connect to this database to gather the list of databases to vacuum. If not specified, the `postgres` database will be used, or if that does not exist, `template1` will be used. This can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options. Also, connection string parameters other than the database name itself will be re-used when connecting to other databases.

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

In case of difficulty, see [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "VACUUM") and [psql](https://www.postgresql.org/docs/current/app-psql.html "psql") for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the libpq front-end library will apply.

## Examples

To clean the database `test`:

```
$ 
```

To clean and analyze for the optimizer a database named `bigdb`:

```
$ 
```

To clean a single table `foo` in a database named `xyzzy`, and analyze a single column `bar` of the table for the optimizer:

```
$ 
```

To clean all tables in the `foo` and `bar` schemas in a database named `xyzzy`:

```
$ 
```
