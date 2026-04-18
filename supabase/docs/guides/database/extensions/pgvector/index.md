---
title: "pgvector: Embeddings and vector similarity"
source: "https://supabase.com/docs/guides/database/extensions/pgvector"
canonical_url: "https://supabase.com/docs/guides/database/extensions/pgvector"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:04.871Z"
content_hash: "4782327f736c5882efec542b607431d7cf956706330efc00a17f94162ce6ee38"
menu_path: ["Database","Database","Extensions","Extensions","pgvector: Embeddings and vector similarity","pgvector: Embeddings and vector similarity"]
section_path: ["Database","Database","Extensions","Extensions","pgvector: Embeddings and vector similarity","pgvector: Embeddings and vector similarity"]
nav_prev: {"path": "supabase/docs/guides/database/extensions/pgroonga/index.md", "title": "PGroonga: Multilingual Full Text Search"}
nav_next: {"path": "supabase/docs/guides/database/extensions/pgsodium/index.md", "title": "pgsodium (pending deprecation): Encryption Features"}
---

# 

pgvector: Embeddings and vector similarity

* * *

[pgvector](https://github.com/pgvector/pgvector/) is a Postgres extension for vector similarity search. It can also be used for storing [embeddings](/blog/openai-embeddings-postgres-vector).

The name of pgvector's Postgres extension is [vector](https://github.com/pgvector/pgvector/blob/258eaf58fdaff1843617ff59ea855e0768243fe9/README.md?plain=1#L64).

Learn more about Supabase's [AI & Vector](/docs/guides/ai) offering.

## Concepts[#](#concepts)

### Vector similarity[#](#vector-similarity)

Vector similarity refers to a measure of the similarity between two related items. For example, if you have a list of products, you can use vector similarity to find similar products. To do this, you need to convert each product into a "vector" of numbers, using a mathematical model. You can use a similar model for text, images, and other types of data. Once all of these vectors are stored in the database, you can use vector similarity to find similar items.

### Embeddings[#](#embeddings)

This is particularly useful if you're building AI applications with large language models. You can create and store [embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) for retrieval augmented generation (RAG).

## Usage[#](#usage)

### Enable the extension[#](#enable-the-extension)

1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
2.  Click on **Extensions** in the sidebar.
3.  Search for "vector" and enable the extension.

## Usage[#](#usage)

### Create a table to store vectors[#](#create-a-table-to-store-vectors)

```
1create table posts (2  id serial primary key,3  title text not null,4  body text not null,5  embedding extensions.vector(384)6);
```

### Storing a vector / embedding[#](#storing-a-vector--embedding)

In this example we'll generate a vector using Transformer.js, then store it in the database using the Supabase client.

```
1import { pipeline } from '@xenova/transformers'2const generateEmbedding = await pipeline('feature-extraction', 'Supabase/gte-small')34const title = 'First post!'5const body = 'Hello world!'67// Generate a vector using Transformers.js8const output = await generateEmbedding(body, {9  pooling: 'mean',10  normalize: true,11})1213// Extract the embedding output14const embedding = Array.from(output.data)1516// Store the vector in Postgres17const { data, error } = await supabase.from('posts').insert({18  title,19  body,20  embedding,21})
```

## Specific usage cases[#](#specific-usage-cases)

### Queries with filtering[#](#queries-with-filtering)

If you use an IVFFlat or HNSW index and naively filter the results based on the value of another column, you may get fewer rows returned than requested.

For example, the following query may return fewer than 5 rows, even if 5 corresponding rows exist in the database. This is because the embedding index may not return 5 rows matching the filter.

```
1SELECT * FROM items WHERE category_id = 123 ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

To get the exact number of requested rows, use [iterative search](https://github.com/pgvector/pgvector/?tab=readme-ov-file#iterative-index-scans) to continue scanning the index until enough results are found.

## More pgvector and Supabase resources[#](#more-pgvector-and-supabase-resources)

*   [Supabase Clippy: ChatGPT for Supabase Docs](/blog/chatgpt-supabase-docs)
*   [Storing OpenAI embeddings in Postgres with pgvector](/blog/openai-embeddings-postgres-vector)
*   [A ChatGPT Plugins Template built with Supabase Edge Runtime](/blog/building-chatgpt-plugins-template)
*   [Template for building your own custom ChatGPT style doc search](https://github.com/supabase-community/nextjs-openai-doc-search)
