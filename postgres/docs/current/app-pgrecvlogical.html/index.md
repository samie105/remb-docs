---
title: "PostgreSQL: Documentation: 18: pg_recvlogical"
source: "https://www.postgresql.org/docs/current/app-pgrecvlogical.html"
canonical_url: "https://www.postgresql.org/docs/current/app-pgrecvlogical.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:35.853Z"
content_hash: "e347f4fc66fac725d738ebc06de39de11ecba0cb6c4a0e11f25933de434f66db"
menu_path: ["PostgreSQL: Documentation: 18: pg_recvlogical"]
section_path: []
---
pg\_recvlogical — control PostgreSQL logical decoding streams

## Synopsis

`pg_recvlogical` \[_`option`_...\]

## Description

`pg_recvlogical` controls logical decoding replication slots and streams data from such replication slots.

It creates a replication-mode connection, so it is subject to the same constraints as [pg\_receivewal](https://www.postgresql.org/docs/current/app-pgreceivewal.html "pg_receivewal"), plus those for logical replication (see [Chapter 47](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding")).

`pg_recvlogical` has no equivalent to the logical decoding SQL interface's peek and get modes. It sends replay confirmations for data lazily as it receives it and on clean exit. To examine pending data on a slot without consuming it, use [`pg_logical_slot_peek_changes`](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-REPLICATION "9.28.6. Replication Management Functions").

In the absence of fatal errors, pg\_recvlogical will run until terminated by the SIGINT (**Control**+**C**) or SIGTERM signal.

When pg\_recvlogical receives a SIGHUP signal, it closes the current output file and opens a new one using the filename specified by the `--file` option. This allows us to rotate the output file by first renaming the current file and then sending a SIGHUP signal to pg\_recvlogical.

## Options

At least one of the following options must be specified to select an action:

`--create-slot`

Create a new logical replication slot with the name specified by `--slot`, using the output plugin specified by `--plugin`, for the database specified by `--dbname`.

The `--slot` and `--dbname` are required for this action.

The `--enable-two-phase` and `--enable-failover` options can be specified with `--create-slot`.

`--drop-slot`

Drop the replication slot with the name specified by `--slot`, then exit.

The `--slot` is required for this action.

`--start`

Begin streaming changes from the logical replication slot specified by `--slot`, continuing until terminated by a signal. If the server side change stream ends with a server shutdown or disconnect, retry in a loop unless `--no-loop` is specified.

The `--slot` and `--dbname`, `--file` are required for this action.

The stream format is determined by the output plugin specified when the slot was created.

The connection must be to the same database used to create the slot.

`--create-slot` and `--start` can be specified together. `--drop-slot` cannot be combined with another action.

The following command-line options control the location and format of the output and other replication behavior:

``-E _`lsn`_``  
``--endpos=_`lsn`_``

In `--start` mode, automatically stop replication and exit with normal exit status 0 when receiving reaches the specified LSN. If specified when not in `--start` mode, an error is raised.

If there's a record with LSN exactly equal to _`lsn`_, the record will be output.

The `--endpos` option is not aware of transaction boundaries and may truncate output partway through a transaction. Any partially output transaction will not be consumed and will be replayed again when the slot is next read from. Individual messages are never truncated.

`--enable-failover`

Enables the slot to be synchronized to the standbys. This option may only be specified with `--create-slot`.

``-f _`filename`_``  
``--file=_`filename`_``

Write received and decoded transaction data into this file. Use `-` for stdout.

This parameter is required for `--start`.

``-F _`interval_seconds`_``  
``--fsync-interval=_`interval_seconds`_``

Specifies how often pg\_recvlogical should issue `fsync()` calls to ensure the output file is safely flushed to disk.

The server will occasionally request the client to perform a flush and report the flush position to the server. This setting is in addition to that, to perform flushes more frequently.

Specifying an interval of `0` disables issuing `fsync()` calls altogether, while still reporting progress to the server. In this case, data could be lost in the event of a crash.

``-I _`lsn`_``  
``--startpos=_`lsn`_``

In `--start` mode, start replication from the given LSN. For details on the effect of this, see the documentation in [Chapter 47](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding") and [Section 54.4](https://www.postgresql.org/docs/current/protocol-replication.html "54.4. Streaming Replication Protocol"). Ignored in other modes.

`--if-not-exists`

Do not error out when `--create-slot` is specified and a slot with the specified name already exists.

`-n`  
`--no-loop`

When the connection to the server is lost, do not retry in a loop, just exit.

``-o _`name`_[=_`value`_]``  
``--option=_`name`_[=_`value`_]``

Pass the option _`name`_ to the output plugin with, if specified, the option value _`value`_. Which options exist and their effects depends on the used output plugin.

``-P _`plugin`_``  
``--plugin=_`plugin`_``

When creating a slot, use the specified logical decoding output plugin. See [Chapter 47](https://www.postgresql.org/docs/current/logicaldecoding.html "Chapter 47. Logical Decoding"). This option has no effect if the slot already exists.

``-s _`interval_seconds`_``  
``--status-interval=_`interval_seconds`_``

This option has the same effect as the option of the same name in [pg\_receivewal](https://www.postgresql.org/docs/current/app-pgreceivewal.html "pg_receivewal"). See the description there.

``-S _`slot_name`_``  
``--slot=_`slot_name`_``

In `--start` mode, use the existing logical replication slot named _`slot_name`_. In `--create-slot` mode, create the slot with this name. In `--drop-slot` mode, delete the slot with this name.

This parameter is required for any of actions.

`-t`  
`--enable-two-phase`  
`--two-phase` (deprecated)

Enables decoding of prepared transactions. This option may only be specified with `--create-slot`.

`-v`  
`--verbose`

Enables verbose mode.

The following command-line options control the database connection parameters.

``-d _`dbname`_``  
``--dbname=_`dbname`_``

The database to connect to. See the description of the actions for what this means in detail. The _`dbname`_ can be a [connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING "32.1.1. Connection Strings"). If so, connection string parameters will override any conflicting command line options.

This parameter is required for `--create-slot` and `--start`.

``-h _`hostname-or-ip`_``  
``--host=_`hostname-or-ip`_``

Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the `PGHOST` environment variable, if set, else a Unix domain socket connection is attempted.

``-p _`port`_``  
``--port=_`port`_``

Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. Defaults to the `PGPORT` environment variable, if set, or a compiled-in default.

``-U _`user`_``  
``--username=_`user`_``

User name to connect as. Defaults to current operating system user name.

`-w`  
`--no-password`

Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.

`-W`  
`--password`

Force pg\_recvlogical to prompt for a password before connecting to a database.

This option is never essential, since pg\_recvlogical will automatically prompt for a password if the server demands password authentication. However, pg\_recvlogical will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

The following additional options are available:

`-V`  
`--version`

Print the pg\_recvlogical version and exit.

`-?`  
`--help`

Show help about pg\_recvlogical command line arguments, and exit.

## Exit Status

pg\_recvlogical will exit with status 0 when terminated by the SIGINT or SIGTERM signal. (That is the normal way to end it. Hence it is not an error.) For fatal errors or other signals, the exit status will be nonzero.

## Environment

This utility, like most other PostgreSQL utilities, uses the environment variables supported by libpq (see [Section 32.15](https://www.postgresql.org/docs/current/libpq-envars.html "32.15. Environment Variables")).

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## Notes

pg\_recvlogical will preserve group permissions on the received WAL files if group permissions are enabled on the source cluster.
