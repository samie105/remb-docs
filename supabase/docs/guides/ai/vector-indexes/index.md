---
title: "Vector indexes"
source: "https://supabase.com/docs/guides/ai/vector-indexes"
canonical_url: "https://supabase.com/docs/guides/ai/vector-indexes"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:41.483Z"
content_hash: "6d379bfd9f67e6db12573152c0e40fd3ff2ef3939e57b35fdf915b112892a233"
menu_path: ["AI & Vectors","AI & Vectors","More","More","More","Vector indexes","Vector indexes","Overview","Overview"]
section_path: ["AI & Vectors","AI & Vectors","More","More","More","Vector indexes","Vector indexes","Overview","Overview"]
---
# 

Vector indexes

* * *

Once your vector table starts to grow, you will likely want to add an index to speed up queries. Without indexes, you'll be performing a sequential scan which can be a resource-intensive operation when you have many records.

## Choosing an index[#](#choosing-an-index)

Today `pgvector` supports two types of indexes:

*   [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes)
*   [IVFFlat](/docs/guides/ai/vector-indexes/ivf-indexes)

In general we recommend using [HNSW](/docs/guides/ai/vector-indexes/hnsw-indexes) because of its [performance](/blog/increase-performance-pgvector-hnsw#hnsw-performance-1536-dimensions) and [robustness against changing data](/docs/guides/ai/vector-indexes/hnsw-indexes#when-should-you-create-hnsw-indexes).

## Distance operators[#](#distance-operators)

Indexes can be used to improve performance of nearest neighbor search using various distance measures. `pgvector` includes 3 distance operators:

Operator

Description

[**Operator class**](https://www.postgresql.org/docs/current/sql-createopclass.html)

`<->`

Euclidean distance

`vector_l2_ops`

`<#>`

negative inner product

`vector_ip_ops`

`<=>`

cosine distance

`vector_cosine_ops`

For pgvector versions 0.7.0 and above, it's possible to create indexes on vectors with the following maximum dimensions:

*   vector: up to 2,000 dimensions
*   halfvec: up to 4,000 dimensions
*   bit: up to 64,000 dimensions

You can check your current pgvector version by running: `SELECT * FROM pg_extension WHERE extname = 'vector';` or by navigating to the [Extensions](/dashboard/project/_/database/extensions) tab in your Supabase project dashboard.

If you are on an earlier version of pgvector, you should [upgrade your project here](/dashboard/project/_/settings/infrastructure).

## Resources[#](#resources)

Read more about indexing on `pgvector`'s [GitHub page](https://github.com/pgvector/pgvector#indexing).
