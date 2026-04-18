---
title: "Structured and Unstructured"
source: "https://supabase.com/docs/guides/ai/structured-unstructured"
canonical_url: "https://supabase.com/docs/guides/ai/structured-unstructured"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:29.396Z"
content_hash: "b762e946718e9ce804df7426e38f0fa134ff52fe905ce68c731f75b8cdc5dacc"
menu_path: ["AI & Vectors","AI & Vectors","Structured & unstructured","Structured & unstructured"]
section_path: ["AI & Vectors","AI & Vectors","Structured & unstructured","Structured & unstructured"]
nav_prev: {"path": "supabase/docs/guides/ai/semantic-search/index.md", "title": "Semantic search"}
nav_next: {"path": "supabase/docs/guides/ai/vecs-python-client/index.md", "title": "Python client"}
---

# 

Structured and Unstructured

## 

Supabase is flexible enough to associate structured and unstructured metadata with embeddings.

* * *

Most vector stores treat metadata associated with embeddings like NoSQL, unstructured data. Supabase is flexible enough to store unstructured and structured metadata.

## Structured[#](#structured)

```
1create table docs (2  id uuid primary key,3  embedding extensions.vector(3),4  content text,5  url text6);78insert into docs9  (id, embedding, content, url)10values11  ('79409372-7556-4ccc-ab8f-5786a6cfa4f7', array[0.1, 0.2, 0.3], 'Hello world', '/hello-world');
```

Notice that we've associated two pieces of metadata, `content` and `url`, with the embedding. Those fields can be filtered, constrained, indexed, and generally operated on using the full power of SQL. Structured metadata fits naturally with a traditional Supabase application, and can be managed via database [migrations](/docs/guides/deployment/database-migrations).

## Unstructured[#](#unstructured)

```
1create table docs (2  id uuid primary key,3  embedding extensions.vector(3),4  meta jsonb5);67insert into docs8  (id, embedding, meta)9values10  (11    '79409372-7556-4ccc-ab8f-5786a6cfa4f7',12    array[0.1, 0.2, 0.3],13    '{"content": "Hello world", "url": "/hello-world"}'14  );
```

An unstructured approach does not specify the metadata fields that are expected. It stores all metadata in a flexible `json`/`jsonb` column. The tradeoff is that the querying/filtering capabilities of a schemaless data type are less flexible than when each field has a dedicated column. It also pushes the burden of metadata data integrity onto application code, which is more error prone than enforcing constraints in the database.

The unstructured approach is recommended:

*   for ephemeral/interactive workloads e.g. data science or scientific research
*   when metadata fields are user-defined or unknown
*   during rapid prototyping

Client libraries like python's [vecs](https://github.com/supabase/vecs) use this structure. For example, running:

```
1#!/usr/bin/env python32import vecs34# In practice, do not hard-code your password. Use environment variables.5DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"67# create vector store client8vx = vecs.create_client(DB_CONNECTION)910docs = vx.get_or_create_collection(name="docs", dimension=1536)1112docs.upsert(vectors=[13  ('79409372-7556-4ccc-ab8f-5786a6cfa4f7', [100, 200, 300], { url: '/hello-world' })14])
```

automatically creates the unstructured SQL table during the call to `get_or_create_collection`.

Note that when working with client libraries that emit SQL DDL, like `create table ...`, you should add that SQL to your migrations when moving to production to maintain a single source of truth for your database's schema.

## Hybrid[#](#hybrid)

The structured metadata style is recommended when the fields being tracked are known in advance. If you have a combination of known and unknown metadata fields, you can accommodate the unknown fields by adding a `json`/`jsonb` column to the table. In that situation, known fields should continue to use dedicated columns for best query performance and throughput.

```
1create table docs (2  id uuid primary key,3  embedding extensions.vector(3),4  content text,5  url string,6  meta jsonb7);89insert into docs10  (id, embedding, content, url, meta)11values12  (13    '79409372-7556-4ccc-ab8f-5786a6cfa4f7',14    array[0.1, 0.2, 0.3],15    'Hello world',16    '/hello-world',17    '{"key": "value"}'18  );
```

## Choosing the right model[#](#choosing-the-right-model)

Both approaches create a table where you can store your embeddings and some metadata. You should choose the best approach for your use-case. In summary:

*   Structured metadata is best when fields are known in advance or query patterns are predictable e.g. a production Supabase application
*   Unstructured metadata is best when fields are unknown/user-defined or when working with data interactively e.g. exploratory research

Both approaches are valid, and the one you should choose depends on your use-case.


