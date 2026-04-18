---
title: "PostgreSQL: Documentation: 18: F.33. pgstattuple — obtain tuple-level statistics"
source: "https://www.postgresql.org/docs/current/pgstattuple.html"
canonical_url: "https://www.postgresql.org/docs/current/pgstattuple.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:33.556Z"
content_hash: "30f89dd3b54bac8aca7bcf940167fa1b1e91c1bb8b878fbfe894b0f6d196d728"
menu_path: ["PostgreSQL: Documentation: 18: F.33. pgstattuple — obtain tuple-level statistics"]
section_path: []
nav_prev: {"path": "postgres/docs/current/protocol-changes.html/index.md", "title": "PostgreSQL: Documentation: 18: 54.10.\u00a0Summary of Changes since Protocol 2.0"}
nav_next: {"path": "postgres/docs/current/indexes-ordering.html/index.md", "title": "PostgreSQL: Documentation: 18: 11.4.\u00a0Indexes and ORDER BY"}
---

The `pgstattuple` module provides various functions to obtain tuple-level statistics.

Because these functions return detailed page-level information, access is restricted by default. By default, only the role `pg_stat_scan_tables` has `EXECUTE` privilege. Superusers of course bypass this restriction. After the extension has been installed, users may issue `GRANT` commands to change the privileges on the functions to allow others to execute them. However, it might be preferable to add those users to the `pg_stat_scan_tables` role instead.

### F.33.1. Functions [#](#PGSTATTUPLE-FUNCS)

`pgstattuple(regclass) returns record`

`pgstattuple` returns a relation's physical length, percentage of “dead” tuples, and other info. This may help users to determine whether vacuum is necessary or not. The argument is the target relation's name (optionally schema-qualified) or OID. For example:

test=> SELECT \* FROM pgstattuple('pg\_catalog.pg\_proc');
-\[ RECORD 1 \]------+-------
table\_len          | 458752
tuple\_count        | 1470
tuple\_len          | 438896
tuple\_percent      | 95.67
dead\_tuple\_count   | 11
dead\_tuple\_len     | 3157
dead\_tuple\_percent | 0.69
free\_space         | 8932
free\_percent       | 1.95

The output columns are described in [Table F.24](https://www.postgresql.org/docs/current/pgstattuple.html#PGSTATTUPLE-COLUMNS "Table F.24. pgstattuple Output Columns").

**Table F.24. `pgstattuple` Output Columns**

  

Column

Type

Description

`table_len`

`bigint`

Physical relation length in bytes

`tuple_count`

`bigint`

Number of live tuples

`tuple_len`

`bigint`

Total length of live tuples in bytes

`tuple_percent`

`float8`

Percentage of live tuples

`dead_tuple_count`

`bigint`

Number of dead tuples

`dead_tuple_len`

`bigint`

Total length of dead tuples in bytes

`dead_tuple_percent`

`float8`

Percentage of dead tuples

`free_space`

`bigint`

Total free space in bytes

`free_percent`

`float8`

Percentage of free space

  

### Note

The `table_len` will always be greater than the sum of the `tuple_len`, `dead_tuple_len` and `free_space`. The difference is accounted for by fixed page overhead, the per-page table of pointers to tuples, and padding to ensure that tuples are correctly aligned.

`pgstattuple` acquires only a read lock on the relation. So the results do not reflect an instantaneous snapshot; concurrent updates will affect them.

`pgstattuple` judges a tuple is “dead” if `HeapTupleSatisfiesDirty` returns false.

`pgstattuple(text) returns record`

This is the same as `pgstattuple(regclass)`, except that the target relation is specified as TEXT. This function is kept because of backward-compatibility so far, and will be deprecated in some future release.

`pgstatindex(regclass) returns record`

`pgstatindex` returns a record showing information about a B-tree index. For example:

test=> SELECT \* FROM pgstatindex('pg\_cast\_oid\_index');
-\[ RECORD 1 \]------+------
version            | 2
tree\_level         | 0
index\_size         | 16384
root\_block\_no      | 1
internal\_pages     | 0
leaf\_pages         | 1
empty\_pages        | 0
deleted\_pages      | 0
avg\_leaf\_density   | 54.27
leaf\_fragmentation | 0

The output columns are:

  

Column

Type

Description

`version`

`integer`

B-tree version number

`tree_level`

`integer`

Tree level of the root page

`index_size`

`bigint`

Total index size in bytes

`root_block_no`

`bigint`

Location of root page (zero if none)

`internal_pages`

`bigint`

Number of “internal” (upper-level) pages

`leaf_pages`

`bigint`

Number of leaf pages

`empty_pages`

`bigint`

Number of empty pages

`deleted_pages`

`bigint`

Number of deleted pages

`avg_leaf_density`

`float8`

Average density of leaf pages

`leaf_fragmentation`

`float8`

Leaf page fragmentation

The reported `index_size` will normally correspond to one more page than is accounted for by `internal_pages + leaf_pages + empty_pages + deleted_pages`, because it also includes the index's metapage.

As with `pgstattuple`, the results are accumulated page-by-page, and should not be expected to represent an instantaneous snapshot of the whole index.

`pgstatindex(text) returns record`

This is the same as `pgstatindex(regclass)`, except that the target index is specified as TEXT. This function is kept because of backward-compatibility so far, and will be deprecated in some future release.

`pgstatginindex(regclass) returns record`

`pgstatginindex` returns a record showing information about a GIN index. For example:

test=> SELECT \* FROM pgstatginindex('test\_gin\_index');
-\[ RECORD 1 \]--+--
version        | 1
pending\_pages  | 0
pending\_tuples | 0

The output columns are:

  

Column

Type

Description

`version`

`integer`

GIN version number

`pending_pages`

`integer`

Number of pages in the pending list

`pending_tuples`

`bigint`

Number of tuples in the pending list

`pgstathashindex(regclass) returns record`

`pgstathashindex` returns a record showing information about a HASH index. For example:

test=> select \* from pgstathashindex('con\_hash\_index');
-\[ RECORD 1 \]--+-----------------
version        | 4
bucket\_pages   | 33081
overflow\_pages | 0
bitmap\_pages   | 1
unused\_pages   | 32455
live\_items     | 10204006
dead\_items     | 0
free\_percent   | 61.8005949100872

The output columns are:

  

Column

Type

Description

`version`

`integer`

HASH version number

`bucket_pages`

`bigint`

Number of bucket pages

`overflow_pages`

`bigint`

Number of overflow pages

`bitmap_pages`

`bigint`

Number of bitmap pages

`unused_pages`

`bigint`

Number of unused pages

`live_items`

`bigint`

Number of live tuples

`dead_tuples`

`bigint`

Number of dead tuples

`free_percent`

`float`

Percentage of free space

`pg_relpages(regclass) returns bigint`

`pg_relpages` returns the number of pages in the relation.

`pg_relpages(text) returns bigint`

This is the same as `pg_relpages(regclass)`, except that the target relation is specified as TEXT. This function is kept because of backward-compatibility so far, and will be deprecated in some future release.

`pgstattuple_approx(regclass) returns record`

`pgstattuple_approx` is a faster alternative to `pgstattuple` that returns approximate results. The argument is the target relation's name or OID. For example:

test=> SELECT \* FROM pgstattuple\_approx('pg\_catalog.pg\_proc'::regclass);
-\[ RECORD 1 \]--------+-------
table\_len            | 573440
scanned\_percent      | 2
approx\_tuple\_count   | 2740
approx\_tuple\_len     | 561210
approx\_tuple\_percent | 97.87
dead\_tuple\_count     | 0
dead\_tuple\_len       | 0
dead\_tuple\_percent   | 0
approx\_free\_space    | 11996
approx\_free\_percent  | 2.09

The output columns are described in [Table F.25](https://www.postgresql.org/docs/current/pgstattuple.html#PGSTATAPPROX-COLUMNS "Table F.25. pgstattuple_approx Output Columns").

Whereas `pgstattuple` always performs a full-table scan and returns an exact count of live and dead tuples (and their sizes) and free space, `pgstattuple_approx` tries to avoid the full-table scan and returns exact dead tuple statistics along with an approximation of the number and size of live tuples and free space.

It does this by skipping pages that have only visible tuples according to the visibility map (if a page has the corresponding VM bit set, then it is assumed to contain no dead tuples). For such pages, it derives the free space value from the free space map, and assumes that the rest of the space on the page is taken up by live tuples.

For pages that cannot be skipped, it scans each tuple, recording its presence and size in the appropriate counters, and adding up the free space on the page. At the end, it estimates the total number of live tuples based on the number of pages and tuples scanned (in the same way that VACUUM estimates pg\_class.reltuples).

**Table F.25. `pgstattuple_approx` Output Columns**

  

Column

Type

Description

`table_len`

`bigint`

Physical relation length in bytes (exact)

`scanned_percent`

`float8`

Percentage of table scanned

`approx_tuple_count`

`bigint`

Number of live tuples (estimated)

`approx_tuple_len`

`bigint`

Total length of live tuples in bytes (estimated)

`approx_tuple_percent`

`float8`

Percentage of live tuples

`dead_tuple_count`

`bigint`

Number of dead tuples (exact)

`dead_tuple_len`

`bigint`

Total length of dead tuples in bytes (exact)

`dead_tuple_percent`

`float8`

Percentage of dead tuples

`approx_free_space`

`bigint`

Total free space in bytes (estimated)

`approx_free_percent`

`float8`

Percentage of free space

In the above output, the free space figures may not match the `pgstattuple` output exactly, because the free space map gives us an exact figure, but is not guaranteed to be accurate to the byte.


