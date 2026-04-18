---
title: "Generate Embeddings"
source: "https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings"
canonical_url: "https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:52:12.503Z"
content_hash: "c72248b0e34f450bbf56263f55be78440feabb5bb70e29070a31299b40b5919f"
menu_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Generate Embeddings","Generate Embeddings"]
section_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Generate Embeddings","Generate Embeddings"]
nav_prev: {"path": "supabase/docs/guides/ai/quickstarts/hello-world/index.md", "title": "Creating and managing collections"}
nav_next: {"path": "supabase/docs/guides/ai/quickstarts/text-deduplication/index.md", "title": "Semantic Text Deduplication"}
---

# 

Generate Embeddings

## 

Generate text embeddings using Edge Functions.

* * *

This guide will walk you through how to generate high quality text embeddings in [Edge Functions](/docs/guides/functions) using its built-in AI inference API, so no external API is required.

## Build the Edge Function[#](#build-the-edge-function)

Let's build an Edge Function that will accept an input string and generate an embedding for it. Edge Functions are server-side TypeScript HTTP endpoints that run on-demand closest to your users.

1

### Set up Supabase locally

Make sure you have the latest version of the [Supabase CLI installed](/docs/guides/cli/getting-started).

Initialize Supabase in the root directory of your app and start your local stack.

```
1supabase init2supabase start
```

2

### Create Edge Function

Create an Edge Function that we will use to generate embeddings. We'll call this `embed` (you can name this anything you like).

This will create a new TypeScript file called `index.ts` under `./supabase/functions/embed`.

```
1supabase functions new embed
```

3

### Setup Inference Session

Let's create a new inference session to be used in the lifetime of this function. Multiple requests can use the same inference session.

Currently, only the `gte-small` ([https://huggingface.co/Supabase/gte-small](https://huggingface.co/Supabase/gte-small)) text embedding model is supported in Supabase's Edge Runtime.

```
1const session = new Supabase.ai.Session('gte-small');
```

4

### Implement request handler

Modify our request handler to accept an `input` string from the POST request JSON body.

Then generate the embedding by calling `session.run(input)`.

```
1Deno.serve(async (req) => {2  // Extract input string from JSON body3  const { input } = await req.json();45  // Generate the embedding from the user input6  const embedding = await session.run(input, {7    mean_pool: true,8    normalize: true,9  });1011  // Return the embedding12  return new Response(13    JSON.stringify({ embedding }),14    { headers: { 'Content-Type': 'application/json' } }15  );16});
```

Note the two options we pass to `session.run()`:

*   `mean_pool`: The first option sets `pooling` to `mean`. Pooling refers to how token-level embedding representations are compressed into a single sentence embedding that reflects the meaning of the entire sentence. Average pooling is the most common type of pooling for sentence embeddings.
*   `normalize`: The second option normalizes the embedding vector so that it can be used with distance measures like dot product. A normalized vector means its length (magnitude) is 1 - also referred to as a unit vector. A vector is normalized by dividing each element by the vector's length (magnitude), which maintains its direction but changes its length to 1.

5

### Test it!

To test the Edge Function, first start a local functions server.

```
1supabase functions serve
```

Then in a new shell, create an HTTP request using cURL and pass in your input in the JSON body.

```
1curl --request POST 'http://localhost:54321/functions/v1/embed' \2  --header 'Authorization: Bearer ANON_KEY' \3  --header 'Content-Type: application/json' \4  --data '{ "input": "hello world" }'
```

Be sure to replace `ANON_KEY` with your project's anonymous key. You can get this key by running `supabase status`.

## Next steps[#](#next-steps)

*   Learn more about [embedding concepts](/docs/guides/ai/concepts)
*   [Store your embeddings](/docs/guides/ai/vector-columns) in a database

