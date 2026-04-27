---
title: "PostgreSQL: Documentation: 18: 52.53. pg_statistic_ext_data"
source: "https://www.postgresql.org/docs/current/catalog-pg-statistic-ext-data.html"
canonical_url: "https://www.postgresql.org/docs/current/catalog-pg-statistic-ext-data.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-27T20:46:22.714Z"
content_hash: "bcc004ab9e0233a52e1cd4ca00847b93b666908fb130b2e2eff26c06c47e6677"
menu_path: ["PostgreSQL: Documentation: 18: 52.53. pg_statistic_ext_data"]
section_path: []
content_language: "en"
---
Development Versions: [devel](https://www.postgresql.org/docs/devel/catalog-pg-statistic-ext-data.html "PostgreSQL devel - 52.53. pg_statistic_ext_data")

Unsupported versions: [13](https://www.postgresql.org/docs/13/catalog-pg-statistic-ext-data.html "PostgreSQL 13 - 52.53. pg_statistic_ext_data") / [12](https://www.postgresql.org/docs/12/catalog-pg-statistic-ext-data.html "PostgreSQL 12 - 52.53. pg_statistic_ext_data")

The catalog `pg_statistic_ext_data` holds data for extended planner statistics defined in [`pg_statistic_ext`](https://www.postgresql.org/docs/current/catalog-pg-statistic-ext.html "52.52. pg_statistic_ext"). Each row in this catalog corresponds to a _statistics object_ created with [`CREATE STATISTICS`](https://www.postgresql.org/docs/current/sql-createstatistics.html "CREATE STATISTICS").

Normally there is one entry, with `stxdinherit` = `false`, for each statistics object that has been analyzed. If the table has inheritance children or partitions, a second entry with `stxdinherit` = `true` is also created. This row represents the statistics object over the inheritance tree, i.e., statistics for the data you'd see with ``SELECT * FROM _`table`_*``, whereas the `stxdinherit` = `false` row represents the results of ``SELECT * FROM ONLY _`table`_``.

Like [`pg_statistic`](https://www.postgresql.org/docs/current/catalog-pg-statistic.html "52.51. pg_statistic"), `pg_statistic_ext_data` should not be readable by the public, since the contents might be considered sensitive. (Example: most common combinations of values in columns might be quite interesting.) [`pg_stats_ext`](https://www.postgresql.org/docs/current/view-pg-stats-ext.html "53.30. pg_stats_ext") is a publicly readable view on `pg_statistic_ext_data` (after joining with [`pg_statistic_ext`](https://www.postgresql.org/docs/current/catalog-pg-statistic-ext.html "52.52. pg_statistic_ext")) that only exposes information about tables the current user owns.

**Table 52.53. `pg_statistic_ext_data` Columns**

| 
Column Type

Description

 |
| --- |
| 

`stxoid` `oid` (references [`pg_statistic_ext`](https://www.postgresql.org/docs/current/catalog-pg-statistic-ext.html "52.52. pg_statistic_ext").`oid`)

Extended statistics object containing the definition for this data

 |
| 

`stxdinherit` `bool`

If true, the stats include values from child tables, not just the values in the specified relation

 |
| 

`stxdndistinct` `pg_ndistinct`

N-distinct counts, serialized as `pg_ndistinct` type

 |
| 

`stxddependencies` `pg_dependencies`

Functional dependency statistics, serialized as `pg_dependencies` type

 |
| 

`stxdmcv` `pg_mcv_list`

MCV (most-common values) list statistics, serialized as `pg_mcv_list` type

 |
| 

`stxdexpr` `pg_statistic[]`

Per-expression statistics, serialized as an array of `pg_statistic` type

 |
