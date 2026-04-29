---
title: "PostgreSQL: Documentation: 18: F.34. pg_surgery — perform low-level surgery on relation data"
source: "https://www.postgresql.org/docs/current/pgsurgery.html"
canonical_url: "https://www.postgresql.org/docs/current/pgsurgery.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:51.992Z"
content_hash: "5b3387ae22ae1992000a7529dd357b52c7547282ce3dfbd22c0d7c42c9f4f4c4"
menu_path: ["PostgreSQL: Documentation: 18: F.34. pg_surgery — perform low-level surgery on relation data"]
section_path: []
nav_prev: {"path": "postgres/docs/current/pgstattuple.html/index.md", "title": "PostgreSQL: Documentation: 18: F.33.\u00a0pgstattuple \u2014 obtain tuple-level statistics"}
nav_next: {"path": "postgres/docs/current/pgtestfsync.html/index.md", "title": "PostgreSQL: Documentation: 18: pg_test_fsync"}
---

The `pg_surgery` module provides various functions to perform surgery on a damaged relation. These functions are unsafe by design and using them may corrupt (or further corrupt) your database. For example, these functions can easily be used to make a table inconsistent with its own indexes, to cause `UNIQUE` or `FOREIGN KEY` constraint violations, or even to make tuples visible which, when read, will cause a database server crash. They should be used with great caution and only as a last resort.

### F.34.1. Functions [#](#PGSURGERY-FUNCS)

`heap_force_kill(regclass, tid[]) returns void`

`heap_force_kill` marks “used” line pointers as “dead” without examining the tuples. The intended use of this function is to forcibly remove tuples that are not otherwise accessible. For example:

test=> select \* from t1 where ctid = '(0, 1)';
ERROR:  could not access status of transaction 4007513275
DETAIL:  Could not open file "pg\_xact/0EED": No such file or directory.

test=# select heap\_force\_kill('t1'::regclass, ARRAY\['(0, 1)'\]::tid\[\]);
 heap\_force\_kill
-----------------

(1 row)

test=# select \* from t1 where ctid = '(0, 1)';
(0 rows)

`heap_force_freeze(regclass, tid[]) returns void`

`heap_force_freeze` marks tuples as frozen without examining the tuple data. The intended use of this function is to make accessible tuples which are inaccessible due to corrupted visibility information, or which prevent the table from being successfully vacuumed due to corrupted visibility information. For example:

test=> vacuum t1;
ERROR:  found xmin 507 from before relfrozenxid 515
CONTEXT:  while scanning block 0 of relation "public.t1"

test=# select ctid from t1 where xmin = 507;
 ctid
-------
 (0,3)
(1 row)

test=# select heap\_force\_freeze('t1'::regclass, ARRAY\['(0, 3)'\]::tid\[\]);
 heap\_force\_freeze
-------------------

(1 row)

test=# select ctid from t1 where xmin = 2;
 ctid
-------
 (0,3)
(1 row)
