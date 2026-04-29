---
title: "PostgreSQL: Documentation: 18: pg_archivecleanup"
source: "https://www.postgresql.org/docs/current/pgarchivecleanup.html"
canonical_url: "https://www.postgresql.org/docs/current/pgarchivecleanup.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:48:58.235Z"
content_hash: "0279255ab6451061f5c9b01bb872ee1f7af56eebc263009aa56e43d8766eec76"
menu_path: ["PostgreSQL: Documentation: 18: pg_archivecleanup"]
section_path: []
content_language: "en"
nav_prev: {"path": "../perm-functions.html/index.md", "title": "PostgreSQL: Documentation: 18: 21.6.\u00a0Function Security"}
nav_next: {"path": "../pgbench.html/index.md", "title": "PostgreSQL: Documentation: 18: pgbench"}
---

pg\_archivecleanup — clean up PostgreSQL WAL archive files

## Synopsis

`pg_archivecleanup` \[_`option`_...\] _`archivelocation`_ _`oldestkeptwalfile`_

## Description

pg\_archivecleanup is designed to be used as an `archive_cleanup_command` to clean up WAL file archives when running as a standby server (see [Section 26.2](https://www.postgresql.org/docs/current/warm-standby.html "26.2. Log-Shipping Standby Servers")). pg\_archivecleanup can also be used as a standalone program to clean WAL file archives.

To configure a standby server to use pg\_archivecleanup, put this into its `postgresql.conf` configuration file:

archive\_cleanup\_command = 'pg\_archivecleanup _`archivelocation`_ %r'

where _`archivelocation`_ is the directory from which WAL segment files should be removed.

When used within [archive\_cleanup\_command](../runtime-config-wal.html/index.md#GUC-ARCHIVE-CLEANUP-COMMAND), all WAL files logically preceding the value of the `%r` argument will be removed from _`archivelocation`_. This minimizes the number of files that need to be retained, while preserving crash-restart capability. Use of this parameter is appropriate if the _`archivelocation`_ is a transient staging area for this particular standby server, but _not_ when the _`archivelocation`_ is intended as a long-term WAL archive area, or when multiple standby servers are recovering from the same archive location.

When used as a standalone program all WAL files logically preceding the _`oldestkeptwalfile`_ will be removed from _`archivelocation`_. In this mode, if you specify a `.partial` or `.backup` file name, then only the file prefix will be used as the _`oldestkeptwalfile`_. This treatment of `.backup` file name allows you to remove all WAL files archived prior to a specific base backup without error. For example, the following example will remove all files older than WAL file name `000000010000003700000010`:

pg\_archivecleanup -d archive 000000010000003700000010.00000020.backup

pg\_archivecleanup:  keep WAL file "archive/000000010000003700000010" and later
pg\_archivecleanup:  removing file "archive/00000001000000370000000F"
pg\_archivecleanup:  removing file "archive/00000001000000370000000E"

pg\_archivecleanup assumes that _`archivelocation`_ is a directory readable and writable by the server-owning user.

## Options

pg\_archivecleanup accepts the following command-line arguments:

`-b`  
`--clean-backup-history`

Remove backup history files as well. See [Section 25.3.2](https://www.postgresql.org/docs/current/continuous-archiving.html#BACKUP-BASE-BACKUP "25.3.2. Making a Base Backup") for details about backup history files.

`-d`  
`--debug`

Print lots of debug logging output on `stderr`.

`-n`  
`--dry-run`

Print the names of the files that would have been removed on `stdout` (performs a dry run).

`-V`  
`--version`

Print the pg\_archivecleanup version and exit.

``-x _`extension`_``  
``--strip-extension=_`extension`_``

Provide an extension that will be stripped from all file names before deciding if they should be deleted. This is typically useful for cleaning up archives that have been compressed during storage, and therefore have had an extension added by the compression program. For example: `-x .gz`.

`-?`  
`--help`

Show help about pg\_archivecleanup command line arguments, and exit.

## Environment

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## Notes

pg\_archivecleanup is designed to work with PostgreSQL 8.0 and later when used as a standalone utility, or with PostgreSQL 9.0 and later when used as an archive cleanup command.

pg\_archivecleanup is written in C and has an easy-to-modify source code, with specifically designated sections to modify for your own needs

## Examples

On Linux or Unix systems, you might use:

archive\_cleanup\_command = 'pg\_archivecleanup -d /mnt/standby/archive %r 2>>cleanup.log'

where the archive directory is physically located on the standby server, so that the `archive_command` is accessing it across NFS, but the files are local to the standby. This will:

-   produce debugging output in `cleanup.log`
    
-   remove no-longer-needed files from the archive directory
