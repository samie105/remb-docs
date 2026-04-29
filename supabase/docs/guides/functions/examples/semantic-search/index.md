---
title: "Semantic Search"
source: "https://supabase.com/docs/guides/functions/examples/semantic-search"
canonical_url: "https://supabase.com/docs/guides/functions/examples/semantic-search"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:43.416Z"
content_hash: "cc3659ac29bc816c517c78b95103034fe8ba82cf7e28dfb6aa9b509e17cd00fd"
menu_path: ["Edge Functions","Edge Functions","Examples","Examples","Semantic AI Search","Semantic AI Search"]
section_path: ["Edge Functions","Edge Functions","Examples","Examples","Semantic AI Search","Semantic AI Search"]
nav_prev: {"path": "../screenshots/index.md", "title": "Taking Screenshots with Puppeteer"}
nav_next: {"path": "../send-emails/index.md", "title": "Sending Emails"}
---

# 

Semantic Search

## 

Semantic Search with pgvector and Supabase Edge Functions

* * *

[Semantic search](/docs/guides/ai/semantic-search) interprets the meaning behind user queries rather than exact [keywords](/docs/guides/ai/keyword-search). It uses machine learning to capture the intent and context behind the query, handling language nuances like synonyms, phrasing variations, and word relationships.

Since Supabase Edge Runtime [v1.36.0](https://github.com/supabase/edge-runtime/releases/tag/v1.36.0) you can run the [`gte-small` model](https://huggingface.co/Supabase/gte-small) natively within Supabase Edge Functions without any external dependencies! This allows you to generate text embeddings without calling any external APIs!

In this tutorial you're implementing three parts:

1.  A [`generate-embedding`](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/functions/generate-embedding/index.ts) database webhook edge function which generates embeddings when a content row is added (or updated) in the [`public.embeddings`](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/migrations/20240408072601_embeddings.sql) table.
2.  A [`query_embeddings` Postgres function](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/migrations/20240410031515_vector-search.sql) which allows us to perform similarity search from an Edge Function via [Remote Procedure Call (RPC)](/docs/guides/database/functions?language=js).
3.  A [`search` edge function](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions/supabase/functions/search/index.ts) which generates the embedding for the search term, performs the similarity search via RPC function call, and returns the result.

You can find the complete example code on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/edge-functions)

### Create the database table and webhook[#](#create-the-database-table-and-webhook)

Given the [following table definition](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/migrations/20240408072601_embeddings.sql):

```
1create extension if not exists vector with schema extensions;23create table embeddings (4  id bigint primary key generated always as identity,5  content text not null,6  embedding extensions.vector (384)7);8alter table embeddings enable row level security;910create index on embeddings using hnsw (embedding vector_ip_ops);
```

You can deploy the [following edge function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/functions/generate-embedding/index.ts) as a [database webhook](/docs/guides/database/webhooks) to generate the embeddings for any text content inserted into the table:

```
1const model = new Supabase.ai.Session('gte-small')23Deno.serve(async (req) => {4  const payload: WebhookPayload = await req.json()5  const { content, id } = payload.record67  // Generate embedding.8  const embedding = await model.run(content, {9    mean_pool: true,10    normalize: true,11  })1213  // Store in database.14  const { error } = await supabase15    .from('embeddings')16    .update({ embedding: JSON.stringify(embedding) })17    .eq('id', id)18  if (error) console.warn(error.message)1920  return new Response('ok')21})
```

## Create a Database Function and RPC[#](#create-a-database-function-and-rpc)

With the embeddings now stored in your Postgres database table, you can query them from Supabase Edge Functions by utilizing [Remote Procedure Calls (RPC)](/docs/guides/database/functions?language=js).

Given the [following Postgres Function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/migrations/20240410031515_vector-search.sql):

```
1-- Matches document sections using vector similarity search on embeddings2--3-- Returns a setof embeddings so that we can use PostgREST resource embeddings (joins with other tables)4-- Additional filtering like limits can be chained to this function call5create or replace function query_embeddings(embedding extensions.vector(384), match_threshold float)6returns setof embeddings7language plpgsql8as $$9begin10  return query11  select *12  from embeddings1314  -- The inner product is negative, so we negate match_threshold15  where embeddings.embedding <#> embedding < -match_threshold1617  -- Our embeddings are normalized to length 1, so cosine similarity18  -- and inner product will produce the same query results.19  -- Using inner product which can be computed faster.20  --21  -- For the different distance functions, see https://github.com/pgvector/pgvector22  order by embeddings.embedding <#> embedding;23end;24$$;
```

## Query vectors in Supabase Edge Functions[#](#query-vectors-in-supabase-edge-functions)

You can use `supabase-js` to first generate the embedding for the search term and then invoke the Postgres function to find the relevant results from your stored embeddings, right from your [Supabase Edge Function](https://github.com/supabase/supabase/blob/master/examples/ai/edge-functions/supabase/functions/search/index.ts):

```
1const model = new Supabase.ai.Session('gte-small')23Deno.serve(async (req) => {4  const { search } = await req.json()5  if (!search) return new Response('Please provide a search param!')6  // Generate embedding for search term.7  const embedding = await model.run(search, {8    mean_pool: true,9    normalize: true,10  })1112  // Query embeddings.13  const { data: result, error } = await supabase14    .rpc('query_embeddings', {15      embedding,16      match_threshold: 0.8,17    })18    .select('content')19    .limit(3)20  if (error) {21    return Response.json(error)22  }2324  return Response.json({ search, result })25})
```

You now have AI powered semantic search set up without any external dependencies! Just you, pgvector, and Supabase Edge Functions!
