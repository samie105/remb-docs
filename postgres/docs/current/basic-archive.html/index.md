---
title: "PostgreSQL: Documentation: 18: F.5. basic_archive — an example WAL archive module"
source: "https://www.postgresql.org/docs/current/basic-archive.html"
canonical_url: "https://www.postgresql.org/docs/current/basic-archive.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:31:53.660Z"
content_hash: "fff69f44da18a73d1d1a18bdc7c9730995c832b35d8c05533061be8497d689fb"
menu_path: ["PostgreSQL: Documentation: 18: F.5. basic_archive — an example WAL archive module"]
section_path: []
nav_prev: {"path": "postgres/docs/current/app-vacuumdb.html/index.md", "title": "PostgreSQL: Documentation: 18: vacuumdb"}
nav_next: {"path": "postgres/docs/current/bki-commands.html/index.md", "title": "PostgreSQL: Documentation: 18: 68.4.\u00a0BKI Commands"}
---

`basic_archive` is an example of an archive module. This module copies completed WAL segment files to the specified directory. This may not be especially useful, but it can serve as a starting point for developing your own archive module. For more information about archive modules, see [Chapter 49](https://www.postgresql.org/docs/current/archive-modules.html "Chapter 49. Archive Modules").

In order to function, this module must be loaded via [archive\_library](../runtime-config-wal.html/index.md#GUC-ARCHIVE-LIBRARY), and [archive\_mode](../runtime-config-wal.html/index.md#GUC-ARCHIVE-MODE) must be enabled.

### F.5.1. Configuration Parameters [#](#BASIC-ARCHIVE-CONFIGURATION-PARAMETERS)

`basic_archive.archive_directory` (`string`)

The directory where the server should copy WAL segment files. This directory must already exist. The default is an empty string, which effectively halts WAL archiving, but if [archive\_mode](../runtime-config-wal.html/index.md#GUC-ARCHIVE-MODE) is enabled, the server will accumulate WAL segment files in the expectation that a value will soon be provided.

These parameters must be set in `postgresql.conf`. Typical usage might be:

\# postgresql.conf
archive\_mode = 'on'
archive\_library = 'basic\_archive'
basic\_archive.archive\_directory = '/path/to/archive/directory'

### F.5.2. Notes [#](#BASIC-ARCHIVE-NOTES)

Server crashes may leave temporary files with the prefix `archtemp` in the archive directory. It is recommended to delete such files before restarting the server after a crash. It is safe to remove such files while the server is running as long as they are unrelated to any archiving still in progress, but users should use extra caution when doing so.
