---
title: "PostgreSQL: Documentation: 18: 52.52. pg_statistic_ext"
source: "https://www.postgresql.org/docs/current/catalog-pg-statistic-ext.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-statistic-ext.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:54.119Z"
content_hash: "9cfcb9f47f006707f188a5afa3130f53f38dcf9ae4e4aa4428ea649e47eab149"
menu_path: ["PostgreSQL: Documentation: 18: 52.52. pg_statistic_ext"]
section_path: []
---
The catalog `pg_statistic_ext` holds definitions of extended planner statistics. Each row in this catalog corresponds to a _statistics object_ created with [`CREATE STATISTICS`](https://www.postgresql.org/docs/current/sql-createstatistics.html "CREATE STATISTICS").

**Table 52.52. `pg_statistic_ext` Columns**

Column Type

Description

`oid` `oid`

Row identifier

`stxrelid` `oid` (references [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "52.11. pg_class").`oid`)

Table containing the columns described by this object

`stxname` `name`

Name of the statistics object

`stxnamespace` `oid` (references [`pg_namespace`](https://www.postgresql.org/docs/current/catalog-pg-namespace.html "52.32. pg_namespace").`oid`)

The OID of the namespace that contains this statistics object

`stxowner` `oid` (references [`pg_authid`](https://www.postgresql.org/docs/current/catalog-pg-authid.html "52.8. pg_authid").`oid`)

Owner of the statistics object

`stxkeys` `int2vector` (references [`pg_attribute`](https://www.postgresql.org/docs/current/catalog-pg-attribute.html "52.7. pg_attribute").`attnum`)

An array of attribute numbers, indicating which table columns are covered by this statistics object; for example a value of `1 3` would mean that the first and the third table columns are covered

`stxstattarget` `int2`

`stxstattarget` controls the level of detail of statistics accumulated for this statistics object by [`ANALYZE`](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE"). A zero value indicates that no statistics should be collected. A null value says to use the maximum of the statistics targets of the referenced columns, if set, or the system default statistics target. Positive values of `stxstattarget` determine the target number of “most common values” to collect.

`stxkind` `char[]`

An array containing codes for the enabled statistics kinds; valid values are: `d` for n-distinct statistics, `f` for functional dependency statistics, `m` for most common values (MCV) list statistics, and `e` for expression statistics

`stxexprs` `pg_node_tree`

Expression trees (in `nodeToString()` representation) for statistics object attributes that are not simple column references. This is a list with one element per expression. Null if all statistics object attributes are simple references.

The `pg_statistic_ext` entry is filled in completely during [`CREATE STATISTICS`](https://www.postgresql.org/docs/current/sql-createstatistics.html "CREATE STATISTICS"), but the actual statistical values are not computed then. Subsequent [`ANALYZE`](https://www.postgresql.org/docs/current/sql-analyze.html "ANALYZE") commands compute the desired values and populate an entry in the [`pg_statistic_ext_data`](https://www.postgresql.org/docs/current/catalog-pg-statistic-ext-data.html "52.53. pg_statistic_ext_data") catalog.
