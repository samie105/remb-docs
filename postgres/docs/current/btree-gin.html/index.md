---
title: "PostgreSQL: Documentation: 18: F.7. btree_gin — GIN operator classes with B-tree behavior"
source: "https://www.postgresql.org/docs/current/btree-gin.html"
canonical_url: "https://www.postgresql.org/docs/current/btree-gin.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:46.146Z"
content_hash: "06c6b43bd85596e375671a467739052f174f4f81f372e1c2808b38475d991218"
menu_path: ["PostgreSQL: Documentation: 18: F.7. btree_gin — GIN operator classes with B-tree behavior"]
section_path: []
nav_prev: {"path": "postgres/docs/current/brin.html/index.md", "title": "PostgreSQL: Documentation: 18: 65.5.\u00a0BRIN Indexes"}
nav_next: {"path": "postgres/docs/current/btree-gist.html/index.md", "title": "PostgreSQL: Documentation: 18: F.8.\u00a0btree_gist \u2014 GiST operator classes with B-tree behavior"}
---

`btree_gin` provides GIN operator classes that implement B-tree equivalent behavior for the data types `int2`, `int4`, `int8`, `float4`, `float8`, `timestamp with time zone`, `timestamp without time zone`, `time with time zone`, `time without time zone`, `date`, `interval`, `oid`, `money`, `"char"`, `varchar`, `text`, `bytea`, `bit`, `varbit`, `macaddr`, `macaddr8`, `inet`, `cidr`, `uuid`, `name`, `bool`, `bpchar`, and all `enum` types.

In general, these operator classes will not outperform the equivalent standard B-tree index methods, and they lack one major feature of the standard B-tree code: the ability to enforce uniqueness. However, they are useful for GIN testing and as a base for developing other GIN operator classes. Also, for queries that test both a GIN-indexable column and a B-tree-indexable column, it might be more efficient to create a multicolumn GIN index that uses one of these operator classes than to create two separate indexes that would have to be combined via bitmap ANDing.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

### F.7.1. Example Usage [#](#BTREE-GIN-EXAMPLE-USAGE)

CREATE TABLE test (a int4);
-- create index
CREATE INDEX testidx ON test USING GIN (a);
-- query
SELECT \* FROM test WHERE a < 10;
