---
title: "Generating OpenAI GPT3 completions"
source: "https://supabase.com/docs/guides/ai/examples/openai"
canonical_url: "https://supabase.com/docs/guides/ai/examples/openai"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:53.380Z"
content_hash: "1c1e7db6e3a219342e27f14792fb5dee25e71cc14815e9d12e0c8f798593323e"
menu_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","OpenAI completions using Edge Functions","OpenAI completions using Edge Functions"]
section_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","OpenAI completions using Edge Functions","OpenAI completions using Edge Functions"]
nav_prev: {"path": "supabase/docs/guides/ai/examples/nextjs-vector-search/index.md", "title": "Vector search with Next.js and OpenAI"}
nav_next: {"path": "supabase/docs/guides/ai/examples/semantic-image-search-amazon-titan/index.md", "title": "Semantic Image Search with Amazon Titan"}
---

# 

Generating OpenAI GPT3 completions

## 

Generate GPT text completions using OpenAI and Supabase Edge Functions.

* * *

OpenAI provides a [completions API](https://platform.openai.com/docs/api-reference/completions) that allows you to use their generative GPT models in your own applications.

OpenAI's API is intended to be used from the server-side. Supabase offers Edge Functions to make it easy to interact with third party APIs like OpenAI.

## Setup Supabase project[#](#setup-supabase-project)

If you haven't already, [install the Supabase CLI](../../../cli/index.md) and initialize your project:

```
1supabase init
```

## Create edge function[#](#create-edge-function)

Scaffold a new edge function called `openai` by running:

```
1supabase functions new openai
```

A new edge function will now exist under `./supabase/functions/openai/index.ts`.

We'll design the function to take your user's query (via POST request) and forward it to OpenAI's API.

```
1import OpenAI from 'https://deno.land/x/openai@v4.24.0/mod.ts'23Deno.serve(async (req) => {4  const { query } = await req.json()5  const apiKey = Deno.env.get('OPENAI_API_KEY')6  const openai = new OpenAI({7    apiKey: apiKey,8  })910  // Documentation here: https://github.com/openai/openai-node11  const chatCompletion = await openai.chat.completions.create({12    messages: [{ role: 'user', content: query }],13    // Choose model from here: https://platform.openai.com/docs/models14    model: 'gpt-3.5-turbo',15    stream: false,16  })1718  const reply = chatCompletion.choices[0].message.content1920  return new Response(reply, {21    headers: { 'Content-Type': 'text/plain' },22  })23})
```

Note that we are setting `stream` to `false` which will wait until the entire response is complete before returning. If you wish to stream GPT's response word-by-word back to your client, set `stream` to `true`.

## Create OpenAI key[#](#create-openai-key)

You may have noticed we were passing `OPENAI_API_KEY` in the Authorization header to OpenAI. To generate this key, go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and create a new secret key.

After getting the key, copy it into a new file called `.env.local` in your `./supabase` folder:

```
1OPENAI_API_KEY=your-key-here
```

## Run locally[#](#run-locally)

Serve the edge function locally by running:

```
1supabase functions serve --env-file ./supabase/.env.local --no-verify-jwt
```

Notice how we are passing in the `.env.local` file.

Use cURL or Postman to make a POST request to [http://localhost:54321/functions/v1/openai](http://localhost:54321/functions/v1/openai).

```
1curl -i --location --request POST http://localhost:54321/functions/v1/openai \2  --header 'Content-Type: application/json' \3  --data '{"query":"What is Supabase?"}'
```

You should see a GPT response come back from OpenAI!

## Deploy[#](#deploy)

Deploy your function to the cloud by running:

```
1supabase functions deploy --no-verify-jwt openai2supabase secrets set --env-file ./supabase/.env.local
```

## Go deeper[#](#go-deeper)

If you're interesting in learning how to use this to build your own ChatGPT, read [the blog post](/blog/chatgpt-supabase-docs) and check out the video:
