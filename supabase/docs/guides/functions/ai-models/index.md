---
title: "Running AI Models"
source: "https://supabase.com/docs/guides/functions/ai-models"
canonical_url: "https://supabase.com/docs/guides/functions/ai-models"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:42.620Z"
content_hash: "eada3470c441e84039401dcf050fd90d64fd5272af86050b1bc720ae4fdf6e86"
menu_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","AI Models","AI Models"]
section_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","AI Models","AI Models"]
nav_prev: {"path": "../index.md", "title": "Edge Functions"}
nav_next: {"path": "../architecture/index.md", "title": "Edge Functions Architecture"}
---

# 

Running AI Models

## 

Run AI models in Edge Functions using the built-in Supabase AI API.

* * *

Edge Functions have a built-in API for running AI models. You can use this API to generate embeddings, build conversational workflows, and do other AI related tasks in your Edge Functions.

This allows you to:

*   Generate text embeddings without external dependencies
*   Run Large Language Models via Ollama or Llamafile
*   Build conversational AI workflows

* * *

## Setup[#](#setup)

There are no external dependencies or packages to install to enable the API.

Create a new inference session:

```
1const model = new Supabase.ai.Session('model-name')
```

To get type hints and checks for the API, import types from `functions-js`:

```
1import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
```

### Running a model inference[#](#running-a-model-inference)

Once the session is instantiated, you can call it with inputs to perform inferences:

```
1// For embeddings (gte-small model)2const embeddings = await model.run('Hello world', {3  mean_pool: true,4  normalize: true,5})67// For text generation (non-streaming)8const response = await model.run('Write a haiku about coding', {9  stream: false,10  timeout: 30,11})1213// For streaming responses14const stream = await model.run('Tell me a story', {15  stream: true,16  mode: 'ollama',17})
```

* * *

## Generate text embeddings[#](#generate-text-embeddings)

Generate text embeddings using the built-in [`gte-small`](https://huggingface.co/Supabase/gte-small) model:

`gte-small` model exclusively caters to English texts, and any lengthy texts will be truncated to a maximum of 512 tokens. While you can provide inputs longer than 512 tokens, truncation may affect the accuracy.

```
1const model = new Supabase.ai.Session('gte-small')23Deno.serve(async (req: Request) => {4  const params = new URL(req.url).searchParams5  const input = params.get('input')6  const output = await model.run(input, { mean_pool: true, normalize: true })7  return new Response(JSON.stringify(output), {8    headers: {9      'Content-Type': 'application/json',10      Connection: 'keep-alive',11    },12  })13})
```

* * *

## Using Large Language Models (LLM)[#](#using-large-language-models-llm)

Inference via larger models is supported via [Ollama](https://ollama.com/) and [Mozilla Llamafile](https://github.com/Mozilla-Ocho/llamafile). In the first iteration, you can use it with a self-managed Ollama or [Llamafile server](https://www.docker.com/blog/a-quick-guide-to-containerizing-llamafile-with-docker-for-ai-applications/).

We are progressively rolling out support for the hosted solution. To sign up for early access, fill out [this form](https://forms.supabase.com/supabase.ai-llm-early-access).

* * *

## Running locally[#](#running-locally)

1

### Install Ollama

[Install Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) and pull the Mistral model

```
1ollama pull mistral
```

2

### Run the Ollama server

```
1ollama serve
```

3

### Set the function secret

Set a function secret called `AI_INFERENCE_API_HOST` to point to the Ollama server

```
1echo "AI_INFERENCE_API_HOST=http://host.docker.internal:11434" >> supabase/functions/.env
```

4

### Create a new function

```
1supabase functions new ollama-test
```

```
1import 'jsr:@supabase/functions-js/edge-runtime.d.ts'2const session = new Supabase.ai.Session('mistral')34Deno.serve(async (req: Request) => {5  const params = new URL(req.url).searchParams6  const prompt = params.get('prompt') ?? ''78  // Get the output as a stream9  const output = await session.run(prompt, { stream: true })1011  const headers = new Headers({12    'Content-Type': 'text/event-stream',13    Connection: 'keep-alive',14  })1516  // Create a stream17  const stream = new ReadableStream({18    async start(controller) {19      const encoder = new TextEncoder()2021      try {22        for await (const chunk of output) {23          controller.enqueue(encoder.encode(chunk.response ?? ''))24        }25      } catch (err) {26        console.error('Stream error:', err)27      } finally {28        controller.close()29      }30    },31  })3233  // Return the stream to the user34  return new Response(stream, {35    headers,36  })37})
```

5

### Serve the function

```
1supabase functions serve --env-file supabase/functions/.env
```

6

### Execute the function

```
1curl --get "http://localhost:54321/functions/v1/ollama-test" \2--data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \3-H "Authorization: $ANON_KEY"
```

* * *

## Deploying to production[#](#deploying-to-production)

Once the function is working locally, it's time to deploy to production.

1

### Deploy an Ollama or Llamafile server

Deploy an Ollama or Llamafile server and set a function secret called `AI_INFERENCE_API_HOST` to point to the deployed server:

```
1supabase secrets set AI_INFERENCE_API_HOST=https://path-to-your-llm-server/
```

2

### Deploy the function

```
1supabase functions deploy
```

3

### Execute the function

```
1curl --get "https://project-ref.supabase.co/functions/v1/ollama-test" \2--data-urlencode "prompt=write a short rap song about Supabase, the Postgres Developer platform, as sung by Nicki Minaj" \3-H "Authorization: $ANON_KEY"
```

As demonstrated in the video above, running Ollama locally is typically slower than running it in on a server with dedicated GPUs. We are collaborating with the Ollama team to improve local performance.

In the future, a hosted LLM API, will be provided as part of the Supabase platform. Supabase will scale and manage the API and GPUs for you. To sign up for early access, fill up [this form](https://forms.supabase.com/supabase.ai-llm-early-access).
