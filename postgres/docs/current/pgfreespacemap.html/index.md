---
title: "PostgreSQL: Documentation: 18: F.27. pg_freespacemap — examine the free space map"
source: "https://www.postgresql.org/docs/current/pgfreespacemap.html"
canonical_url: "https://www.postgresql.org/docs/current/pgfreespacemap.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:47.151Z"
content_hash: "0d85e56f3c8d14acac22755833d8dd23e6263406e861682495780fa212ca2b68"
menu_path: ["PostgreSQL: Documentation: 18: F.27. pg_freespacemap — examine the free space map"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgcrypto.html/index.md", "title": "PostgreSQL: Documentation: 18: F.26.\u00a0pgcrypto \u2014 cryptographic functions"}
nav_next: {"path": "postgres/docs/current/pglogicalinspect.html/index.md", "title": "PostgreSQL: Documentation: 18: F.28.\u00a0pg_logicalinspect \u2014 logical decoding components inspection"}
---

The `pg_freespacemap` module provides a means for examining the [free space map](https://www.postgresql.org/docs/current/storage-fsm.html "66.3. Free Space Map") (FSM). It provides a function called `pg_freespace`, or two overloaded functions, to be precise. The functions show the value recorded in the free space map for a given page, or for all pages in the relation.

By default use is restricted to superusers and roles with privileges of the `pg_stat_scan_tables` role. Access may be granted to others using `GRANT`.

### F.27.1. Functions [#](#PGFREESPACEMAP-FUNCS)

`pg_freespace(rel regclass IN, blkno bigint IN) returns int2`

Returns the amount of free space on the page of the relation, specified by `blkno`, according to the FSM.

`pg_freespace(rel regclass IN, blkno OUT bigint, avail OUT int2)`

Displays the amount of free space on each page of the relation, according to the FSM. A set of `(blkno bigint, avail int2)` tuples is returned, one tuple for each page in the relation.

The values stored in the free space map are not exact. They're rounded to precision of 1/256th of `BLCKSZ` (32 bytes with default `BLCKSZ`), and they're not kept fully up-to-date as tuples are inserted and updated.

For indexes, what is tracked is entirely-unused pages, rather than free space within pages. Therefore, the values are not meaningful, just whether a page is in-use or empty.

### F.27.2. Sample Output [#](#PGFREESPACEMAP-SAMPLE-OUTPUT)

postgres=# SELECT \* FROM pg\_freespace('foo');
 blkno | avail
-------+-------
     0 |     0
     1 |     0
     2 |     0
     3 |    32
     4 |   704
     5 |   704
     6 |   704
     7 |  1216
     8 |   704
     9 |   704
    10 |   704
    11 |   704
    12 |   704
    13 |   704
    14 |   704
    15 |   704
    16 |   704
    17 |   704
    18 |   704
    19 |  3648
(20 rows)

postgres=# SELECT \* FROM pg\_freespace('foo', 7);
 pg\_freespace
--------------
         1216
(1 row)
