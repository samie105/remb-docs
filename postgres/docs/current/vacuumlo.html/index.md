---
title: "PostgreSQL: Documentation: 18: vacuumlo"
source: "https://www.postgresql.org/docs/current/vacuumlo.html"
canonical_url: "https://www.postgresql.org/docs/current/vacuumlo.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:56.984Z"
content_hash: "225eb4d02546088cc209c26390c3e70964d541cfd05bb759793ccfa8032711b5"
menu_path: ["PostgreSQL: Documentation: 18: vacuumlo"]
section_path: []
---
vacuumlo — remove orphaned large objects from a PostgreSQL database

## Synopsis

`vacuumlo` \[_`option`_...\] _`dbname`_...

## Description

vacuumlo is a simple utility program that will remove any “orphaned” large objects from a PostgreSQL database. An orphaned large object (LO) is considered to be any LO whose OID does not appear in any `oid` or `lo` data column of the database.

If you use this, you may also be interested in the `lo_manage` trigger in the [lo](https://www.postgresql.org/docs/current/lo.html "F.21. lo — manage large objects") module. `lo_manage` is useful to try to avoid creating orphaned LOs in the first place.

All databases named on the command line are processed.

## Options

vacuumlo accepts the following command-line arguments:

``-l _`limit`_``  
``--limit=_`limit`_``

Remove no more than _`limit`_ large objects per transaction (default 1000). Since the server acquires a lock per LO removed, removing too many LOs in one transaction risks exceeding [max\_locks\_per\_transaction](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION). Set the limit to zero if you want all removals done in a single transaction.

`-n`  
`--dry-run`

Don't remove anything, just show what would be done.

`-v`  
`--verbose`

Write a lot of progress messages.

`-V`  
`--version`

Print the vacuumlo version and exit.

`-?`  
`--help`

Show help about vacuumlo command line arguments, and exit.

vacuumlo also accepts the following command-line arguments for connection parameters:

``-h _`host`_``  
``--host=_`host`_``

Database server's host.

``-p _`port`_``  
``--port=_`port`_``

Database server's port.

``-U _`username`_``  
``--username=_`username`_``

User name to connect as.

`-w`  
`--no-password`

Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password.

`-W`  
`--password`

Force vacuumlo to prompt for a password before connecting to a database.

This option is never essential, since vacuumlo will automatically prompt for a password if the server demands password authentication. However, vacuumlo will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

## Environment

`PGHOST`  
`PGPORT`  
`PGUSER`

Default connection parameters.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see [Section 32.15](https://www.postgresql.org/docs/current/libpq-envars.html "32.15. Environment Variables")).

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## Notes

vacuumlo works by the following method: First, vacuumlo builds a temporary table which contains all of the OIDs of the large objects in the selected database. It then scans through all columns in the database that are of type `oid` or `lo`, and removes matching entries from the temporary table. (Note: Only types with these names are considered; in particular, domains over them are not considered.) The remaining entries in the temporary table identify orphaned LOs. These are removed.
