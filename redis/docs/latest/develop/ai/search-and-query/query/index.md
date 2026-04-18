---
title: "Querying data"
source: "https://redis.io/docs/latest/develop/ai/search-and-query/query/"
canonical_url: "https://redis.io/docs/latest/develop/ai/search-and-query/query/"
docset: "redis"
kind: "database"
adapter: "generic"
last_crawled_at: "2026-04-18T17:05:16.433Z"
content_hash: "221065ba11b17a9919f5f8b7effa967e0a68829ffa74d336b1bdeeb0c7f06f93"
menu_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data"]
section_path: ["Docs\n        Docs","Docs\n        Docs","Docs","Docs","→\n      \n        Develop with Redis","→","Develop with Redis","→\n      \n        Redis for AI and search","→","Redis for AI and search","→\n      \n        Redis Search","→","Redis Search","→\n      \n        Querying data","→","Querying data"]
---
# Querying data

Understand how to query, search, and aggregate Redis data

Redis Open Source distinguishes between the [FT.SEARCH](/docs/latest/commands/ft.search/) and [FT.AGGREGATE](/docs/latest/commands/ft.aggregate/) query commands. You should use [FT.SEARCH](/docs/latest/commands/ft.search/) if you want to perform selections and projections only. If you also need to apply mapping functions, group, or aggregate data, use the [FT.AGGREGATE](/docs/latest/commands/ft.aggregate/) command.

*   **Selection**: A selection allows you to return all documents that fulfill specific criteria.
*   **Projection**: Projections are used to return specific fields of the result set. You can also map/project to calculated field values.
*   **Aggregation**: Aggregations collect and summarize data across several fields.

Here is a short SQL comparison using the [bicycle dataset](./data/bicycles.txt):

Type

SQL

Redis

Selection

`SELECT * FROM bicycles WHERE price >= 1000`

`FT.SEARCH idx:bicycle "@price:[1000 +inf]"`

Simple projection

`SELECT id, price FROM bicycles`

`FT.SEARCH idx:bicycle "*" RETURN 2 __key, price`

Calculated projection

`SELECT id, price-price*0.1 AS discounted FROM bicycles`

`FT.AGGREGATE idx:bicycle "*" LOAD 2 __key price APPLY "@price-@price*0.1" AS discounted`

Aggregation

`SELECT condition, AVG(price) AS avg_price FROM bicycles GROUP BY condition`

`FT.AGGREGATE idx:bicycle "*" GROUPBY 1 @condition REDUCE AVG 1 @price AS avg_price`

The following articles provide an overview of how to query data with the [FT.SEARCH](/docs/latest/commands/ft.search/) command:

*   [Exact match queries](/docs/latest/develop/ai/search-and-query/query/exact-match/)
*   [Range queries](/docs/latest/develop/ai/search-and-query/query/range/)
*   [Full-text search](/docs/latest/develop/ai/search-and-query/query/full-text/)
*   [Geospatial queries](/docs/latest/develop/ai/search-and-query/query/geo-spatial/)
*   [Vector search](/docs/latest/develop/ai/search-and-query/query/vector-search/)
*   [Combined queries](/docs/latest/develop/ai/search-and-query/query/combined/)

You can find further details about aggregation queries with [FT.AGGREGATE](/docs/latest/commands/ft.aggregate/) in the following article:

*   [Aggregation queries](/docs/latest/develop/ai/search-and-query/query/aggregation/)
