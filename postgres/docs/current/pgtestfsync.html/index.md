---
title: "PostgreSQL: Documentation: 18: pg_test_fsync"
source: "https://www.postgresql.org/docs/current/pgtestfsync.html"
canonical_url: "https://www.postgresql.org/docs/current/pgtestfsync.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:54.861Z"
content_hash: "d5c142884331946e2f4f9100588f500db1933d1313728f4e2f7d13ad48163f2c"
menu_path: ["PostgreSQL: Documentation: 18: pg_test_fsync"]
section_path: []
---
pg\_test\_fsync — determine fastest `wal_sync_method` for PostgreSQL

## Synopsis

`pg_test_fsync` \[_`option`_...\]

## Description

pg\_test\_fsync is intended to give you a reasonable idea of what the fastest [wal\_sync\_method](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-SYNC-METHOD) is on your specific system, as well as supplying diagnostic information in the event of an identified I/O problem. However, differences shown by pg\_test\_fsync might not make any significant difference in real database throughput, especially since many database servers are not speed-limited by their write-ahead logs. pg\_test\_fsync reports average file sync operation time in microseconds for each `wal_sync_method`, which can also be used to inform efforts to optimize the value of [commit\_delay](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-COMMIT-DELAY).

## Options

pg\_test\_fsync accepts the following command-line options:

`-f`  
`--filename`

Specifies the file name to write test data in. This file should be in the same file system that the `pg_wal` directory is or will be placed in. (`pg_wal` contains the WAL files.) The default is `pg_test_fsync.out` in the current directory.

`-s`  
`--secs-per-test`

Specifies the number of seconds for each test. The more time per test, the greater the test's accuracy, but the longer it takes to run. The default is 5 seconds, which allows the program to complete in under 2 minutes.

`-V`  
`--version`

Print the pg\_test\_fsync version and exit.

`-?`  
`--help`

Show help about pg\_test\_fsync command line arguments, and exit.

## Environment

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.
