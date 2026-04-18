---
title: "Python client"
source: "https://supabase.com/docs/guides/ai/vecs-python-client"
canonical_url: "https://supabase.com/docs/guides/ai/vecs-python-client"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:32.697Z"
content_hash: "a685d0c97b064a286ff323b501824e05f9a28c452e83a7508d929ffe5f62abd6"
menu_path: ["AI & Vectors","AI & Vectors","Python Examples","Python Examples","Developing locally with Vecs","Developing locally with Vecs"]
section_path: ["AI & Vectors","AI & Vectors","Python Examples","Python Examples","Developing locally with Vecs","Developing locally with Vecs"]
nav_prev: {"path": "supabase/docs/guides/ai/structured-unstructured/index.md", "title": "Structured and Unstructured"}
nav_next: {"path": "supabase/docs/guides/ai/vector-indexes/index.md", "title": "Vector indexes"}
---

# 

Python client

## 

Manage unstructured vector stores in Postgres.

* * *

Supabase provides a Python client called [`vecs`](https://github.com/supabase/vecs) for managing unstructured vector stores. This client provides a set of useful tools for creating and querying collections in Postgres using the [pgvector](/docs/guides/database/extensions/pgvector) extension.

## Quick start[#](#quick-start)

Let's see how Vecs works using a local database. Make sure you have the Supabase CLI [installed](/docs/guides/cli#installation) on your machine.

### Initialize your project[#](#initialize-your-project)

Start a local Postgres instance in any folder using the `init` and `start` commands. Make sure you have Docker running!

```
1# Initialize your project2supabase init34# Start Postgres5supabase start
```

### Create a collection[#](#create-a-collection)

Inside a Python shell, run the following commands to create a new collection called "docs", with 3 dimensions.

```
1import vecs23# create vector store client4vx = vecs.create_client("postgresql://postgres:postgres@localhost:54322/postgres")56# create a collection of vectors with 3 dimensions7docs = vx.get_or_create_collection(name="docs", dimension=3)
```

### Add embeddings[#](#add-embeddings)

Now we can insert some embeddings into our "docs" collection using the `upsert()` command:

```
1import vecs23# create vector store client4docs = vecs.get_or_create_collection(name="docs", dimension=3)56# a collection of vectors with 3 dimensions7vectors=[8  ("vec0", [0.1, 0.2, 0.3], {"year": 1973}),9  ("vec1", [0.7, 0.8, 0.9], {"year": 2012})10]1112# insert our vectors13docs.upsert(vectors=vectors)
```

### Query the collection[#](#query-the-collection)

You can now query the collection to retrieve a relevant match:

```
1import vecs23docs = vecs.get_or_create_collection(name="docs", dimension=3)45# query the collection filtering metadata for "year" = 20126docs.query(7    data=[0.4,0.5,0.6],      # required8    limit=1,                         # number of records to return9    filters={"year": {"$eq": 2012}}, # metadata filters10)
```

## Deep dive[#](#deep-dive)

For a more in-depth guide on `vecs` collections, see [API](/docs/guides/ai/python/api).

## Resources[#](#resources)

*   Official Vecs Documentation: [https://supabase.github.io/vecs/api](https://supabase.github.io/vecs/api)
*   Source Code: [https://github.com/supabase/vecs](https://github.com/supabase/vecs)

