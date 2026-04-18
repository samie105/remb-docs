---
title: "PostgreSQL: Documentation: 18: 9.31. Statistics Information Functions"
source: "https://www.postgresql.org/docs/current/functions-statistics.html"
canonical_url: "https://www.postgresql.org/docs/current/functions-statistics.html"
docset: "postgres"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T16:46:50.697Z"
content_hash: "777de9986e994c63c0146e9b41479bfc258e75ea2a3013841536f96aff48a164"
menu_path: ["PostgreSQL: Documentation: 18: 9.31. Statistics Information Functions"]
section_path: []
---
February 26, 2026: [PostgreSQL 18.3, 17.9, 16.13, 15.17, and 14.22 Released!](/about/news/postgresql-183-179-1613-1517-and-1422-released-3246/)

[Documentation](/docs/ "Documentation") → [PostgreSQL 18](/docs/18/index.html)

Supported Versions: [Current](/docs/current/functions-statistics.html "PostgreSQL 18 - 9.31. Statistics Information Functions") ([18](/docs/18/functions-statistics.html "PostgreSQL 18 - 9.31. Statistics Information Functions")) / [17](/docs/17/functions-statistics.html "PostgreSQL 17 - 9.31. Statistics Information Functions") / [16](/docs/16/functions-statistics.html "PostgreSQL 16 - 9.31. Statistics Information Functions") / [15](/docs/15/functions-statistics.html "PostgreSQL 15 - 9.31. Statistics Information Functions") / [14](/docs/14/functions-statistics.html "PostgreSQL 14 - 9.31. Statistics Information Functions")

Development Versions: [devel](/docs/devel/functions-statistics.html "PostgreSQL devel - 9.31. Statistics Information Functions")

Unsupported versions: [13](/docs/13/functions-statistics.html "PostgreSQL 13 - 9.31. Statistics Information Functions") / [12](/docs/12/functions-statistics.html "PostgreSQL 12 - 9.31. Statistics Information Functions")

## 9.31. Statistics Information Functions [#](#FUNCTIONS-STATISTICS)

PostgreSQL provides a function to inspect complex statistics defined using the `CREATE STATISTICS` command.

### 9.31.1. Inspecting MCV Lists [#](#FUNCTIONS-STATISTICS-MCV)

```
pg_mcv_list_items
```

`pg_mcv_list_items` returns a set of records describing all items stored in a multi-column MCV list. It returns the following columns:

  

Name

Type

Description

`index`

`integer`

index of the item in the MCV list

`values`

`text[]`

values stored in the MCV item

`nulls`

`boolean[]`

flags identifying `NULL` values

`frequency`

`double precision`

frequency of this MCV item

`base_frequency`

`double precision`

base frequency of this MCV item

The `pg_mcv_list_items` function can be used like this:

SELECT m.\* FROM pg\_statistic\_ext join pg\_statistic\_ext\_data on (oid = stxoid),
                pg\_mcv\_list\_items(stxdmcv) m WHERE stxname = 'stts';

Values of the `pg_mcv_list` type can be obtained only from the `pg_statistic_ext_data`.`stxdmcv` column.

## Submit correction

If you see anything in the documentation that is not correct, does not match your experience with the particular feature or requires further clarification, please use [this form](/account/comments/new/18/functions-statistics.html/) to report a documentation issue.
