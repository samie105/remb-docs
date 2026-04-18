---
title: "PostgreSQL: Documentation: 18: F.28. pg_logicalinspect — logical decoding components inspection"
source: "https://www.postgresql.org/docs/current/pglogicalinspect.html"
canonical_url: "https://www.postgresql.org/docs/current/pglogicalinspect.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:44.935Z"
content_hash: "c56420bec55368fdee99c0f244a87cf2087114303ffe3e35e70a0bc2476db64c"
menu_path: ["PostgreSQL: Documentation: 18: F.28. pg_logicalinspect — logical decoding components inspection"]
section_path: []
---
The `pg_logicalinspect` module provides SQL functions that allow you to inspect the contents of logical decoding components. It allows the inspection of serialized logical snapshots of a running PostgreSQL database cluster, which is useful for debugging or educational purposes.

By default, use of these functions is restricted to superusers and members of the `pg_read_server_files` role. Access may be granted by superusers to others using `GRANT`.

### F.28.1. Functions [#](#PGLOGICALINSPECT-FUNCS)

`pg_get_logical_snapshot_meta(filename text) returns record` [#](#PGLOGICALINSPECT-FUNCS-PG-GET-LOGICAL-SNAPSHOT-META)

Gets logical snapshot metadata about a snapshot file that is located in the server's `pg_logical/snapshots` directory. The _`filename`_ argument represents the snapshot file name. For example:

postgres=# SELECT \* FROM pg\_ls\_logicalsnapdir();
-\[ RECORD 1 \]+-----------------------
name         | 0-40796E18.snap
size         | 152
modification | 2024-08-14 16:36:32+00

postgres=# SELECT \* FROM pg\_get\_logical\_snapshot\_meta('0-40796E18.snap');
-\[ RECORD 1 \]--------
magic    | 1369563137
checksum | 1028045905
version  | 6

postgres=# SELECT ss.name, meta.\* FROM pg\_ls\_logicalsnapdir() AS ss,
pg\_get\_logical\_snapshot\_meta(ss.name) AS meta;
-\[ RECORD 1 \]-------------
name     | 0-40796E18.snap
magic    | 1369563137
checksum | 1028045905
version  | 6

If _`filename`_ does not match a snapshot file, the function raises an error.

`pg_get_logical_snapshot_info(filename text) returns record` [#](#PGLOGICALINSPECT-FUNCS-PG-GET-LOGICAL-SNAPSHOT-INFO)

Gets logical snapshot information about a snapshot file that is located in the server's `pg_logical/snapshots` directory. The _`filename`_ argument represents the snapshot file name. For example:

postgres=# SELECT \* FROM pg\_ls\_logicalsnapdir();
-\[ RECORD 1 \]+-----------------------
name         | 0-40796E18.snap
size         | 152
modification | 2024-08-14 16:36:32+00

postgres=# SELECT \* FROM pg\_get\_logical\_snapshot\_info('0-40796E18.snap');
-\[ RECORD 1 \]------------+-----------
state                    | consistent
xmin                     | 751
xmax                     | 751
start\_decoding\_at        | 0/40796AF8
two\_phase\_at             | 0/40796AF8
initial\_xmin\_horizon     | 0
building\_full\_snapshot   | f
in\_slot\_creation         | f
last\_serialized\_snapshot | 0/0
next\_phase\_at            | 0
committed\_count          | 0
committed\_xip            |
catchange\_count          | 2
catchange\_xip            | {751,752}

postgres=# SELECT ss.name, info.\* FROM pg\_ls\_logicalsnapdir() AS ss,
pg\_get\_logical\_snapshot\_info(ss.name) AS info;
-\[ RECORD 1 \]------------+----------------
name                     | 0-40796E18.snap
state                    | consistent
xmin                     | 751
xmax                     | 751
start\_decoding\_at        | 0/40796AF8
two\_phase\_at             | 0/40796AF8
initial\_xmin\_horizon     | 0
building\_full\_snapshot   | f
in\_slot\_creation         | f
last\_serialized\_snapshot | 0/0
next\_phase\_at            | 0
committed\_count          | 0
committed\_xip            |
catchange\_count          | 2
catchange\_xip            | {751,752}

If _`filename`_ does not match a snapshot file, the function raises an error.
