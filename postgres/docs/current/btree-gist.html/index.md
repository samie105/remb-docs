---
title: "PostgreSQL: Documentation: 18: F.8. btree_gist — GiST operator classes with B-tree behavior"
source: "https://www.postgresql.org/docs/current/btree-gist.html"
canonical_url: "https://www.postgresql.org/docs/current/btree-gist.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:28.702Z"
content_hash: "f5dd71ea7c755e45c013bbbcc2bf026a4a8edf8d54bed2719ff0f5723423990d"
menu_path: ["PostgreSQL: Documentation: 18: F.8. btree_gist — GiST operator classes with B-tree behavior"]
section_path: []
---
`btree_gist` provides GiST index operator classes that implement B-tree equivalent behavior for the data types `int2`, `int4`, `int8`, `float4`, `float8`, `numeric`, `timestamp with time zone`, `timestamp without time zone`, `time with time zone`, `time without time zone`, `date`, `interval`, `oid`, `money`, `char`, `varchar`, `text`, `bytea`, `bit`, `varbit`, `macaddr`, `macaddr8`, `inet`, `cidr`, `uuid`, `bool` and all `enum` types.

In general, these operator classes will not outperform the equivalent standard B-tree index methods, and they lack one major feature of the standard B-tree code: the ability to enforce uniqueness. However, they provide some other features that are not available with a B-tree index, as described below. Also, these operator classes are useful when a multicolumn GiST index is needed, wherein some of the columns are of data types that are only indexable with GiST but other columns are just simple data types. Lastly, these operator classes are useful for GiST testing and as a base for developing other GiST operator classes.

In addition to the typical B-tree search operators, `btree_gist` also provides index support for `<>` (“not equals”). This may be useful in combination with an [exclusion constraint](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-EXCLUDE), as described below.

Also, for data types for which there is a natural distance metric, `btree_gist` defines a distance operator `<->`, and provides GiST index support for nearest-neighbor searches using this operator. Distance operators are provided for `int2`, `int4`, `int8`, `float4`, `float8`, `timestamp with time zone`, `timestamp without time zone`, `time without time zone`, `date`, `interval`, `oid`, and `money`.

By default `btree_gist` builds GiST index with `sortsupport` in _sorted_ mode. This usually results in much faster index built speed. It is still possible to revert to buffered built strategy by using the `buffering` parameter when creating the index.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

### F.8.1. Example Usage [#](#BTREE-GIST-EXAMPLE-USAGE)

Simple example using `btree_gist` instead of `btree`:

CREATE TABLE test (a int4);
-- create index
CREATE INDEX testidx ON test USING GIST (a);
-- query
SELECT \* FROM test WHERE a < 10;
-- nearest-neighbor search: find the ten entries closest to "42"
SELECT \*, a <-> 42 AS dist FROM test ORDER BY a <-> 42 LIMIT 10;

Use an [exclusion constraint](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-EXCLUDE) to enforce the rule that a cage at a zoo can contain only one kind of animal:

\=> CREATE TABLE zoo (
  cage   INTEGER,
  animal TEXT,
  EXCLUDE USING GIST (cage WITH =, animal WITH <>)
);

=> INSERT INTO zoo VALUES(123, 'zebra');
INSERT 0 1
=> INSERT INTO zoo VALUES(123, 'zebra');
INSERT 0 1
=> INSERT INTO zoo VALUES(123, 'lion');
ERROR:  conflicting key value violates exclusion constraint "zoo\_cage\_animal\_excl"
DETAIL:  Key (cage, animal)=(123, lion) conflicts with existing key (cage, animal)=(123, zebra).
=> INSERT INTO zoo VALUES(124, 'lion');
INSERT 0 1
