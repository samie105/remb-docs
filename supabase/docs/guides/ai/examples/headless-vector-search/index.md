---
title: "Adding generative Q&A for your documentation"
source: "https://supabase.com/docs/guides/ai/examples/headless-vector-search"
canonical_url: "https://supabase.com/docs/guides/ai/examples/headless-vector-search"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:26.896Z"
content_hash: "8a601dc38605d2305363460d217140de8679f490f03485f0ad984b78eaa8148b"
menu_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Adding generative Q&A to your documentation","Adding generative Q&A to your documentation"]
section_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Adding generative Q&A to your documentation","Adding generative Q&A to your documentation"]
nav_prev: {"path": "supabase/docs/guides/ai/examples/building-chatgpt-plugins/index.md", "title": "Building ChatGPT plugins"}
nav_next: {"path": "supabase/docs/guides/ai/examples/huggingface-image-captioning/index.md", "title": "Generate image captions using Hugging Face"}
---

# 

Adding generative Q&A for your documentation

## 

Learn how to build a ChatGPT-style doc search powered using our headless search toolkit.

* * *

Supabase provides a [Headless Search Toolkit](https://github.com/supabase/headless-vector-search) for adding "Generative Q&A" to your documentation. The toolkit is "headless", so that you can integrate it into your existing website and style it to match your website theme.

You can see how this works with the Supabase docs. Just hit `cmd+k` and "ask" for something like "what are the features of Supabase?". You will see that the response is streamed back, using the information provided in the docs:

![headless search](/docs/img/ai/headless-search/headless.png)

## Tech stack[#](#tech-stack)

*   Supabase: Database & Edge Functions.
*   OpenAI: Embeddings and completions.
*   GitHub Actions: for ingesting your markdown docs.

## Toolkit[#](#toolkit)

This toolkit consists of 2 parts:

*   The [Headless Vector Search](https://github.com/supabase/headless-vector-search) template which you can deploy in your own organization.
*   A [GitHub Action](https://github.com/supabase/embeddings-generator) which will ingest your markdown files, convert them to embeddings, and store them in your database.

## Usage[#](#usage)

There are 3 steps to build similarity search inside your documentation:

1.  Prepare your database.
2.  Ingest your documentation.
3.  Add a search interface.

### Prepare your database[#](#prepare-your-database)

To prepare, create a [new Supabase project](https://database.new) and store the database and API credentials, which you can find in the project [settings](/dashboard/project/_/settings).

Now we can use the [Headless Vector Search](https://github.com/supabase/headless-vector-search#set-up) instructions to set up the database:

1.  Clone the repo to your local machine: `git clone git@github.com:supabase/headless-vector-search.git`
2.  Link the repo to your remote project: `supabase link --project-ref XXX`
3.  Apply the database migrations: `supabase db push`
4.  Set your OpenAI key as a secret: `supabase secrets set OPENAI_API_KEY=sk-xxx`
5.  Deploy the Edge Functions: `supabase functions deploy --no-verify-jwt`
6.  Expose `docs` schema via API in Supabase Dashboard [settings](/dashboard/project/_/settings/api) > `API Settings` > `Exposed schemas`

### Ingest your documentation[#](#ingest-your-documentation)

Now we need to push your documentation into the database as embeddings. You can do this manually, but to make it easier we've created a [GitHub Action](https://github.com/marketplace/actions/supabase-embeddings-generator) which can update your database every time there is a Pull Request.

In your knowledge base repository, create a new action called `.github/workflows/generate_embeddings.yml` with the following content:

```
1name: 'generate_embeddings'2on: # run on main branch changes3  push:4    branches:5      - main67jobs:8  generate:9    runs-on: ubuntu-latest10    steps:11      - uses: actions/checkout@v312      - uses: supabase/embeddings-generator@v0.0.x # Update this to the latest version.13        with:14          supabase-url: 'https://your-project-ref.supabase.co' # Update this to your project URL.15          supabase-service-role-key: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}16          openai-key: ${{ secrets.OPENAI_API_KEY }}17          docs-root-path: 'docs' # the path to the root of your md(x) files
```

Make sure to choose the latest version, and set your `SUPABASE_SERVICE_ROLE_KEY` and `OPENAI_API_KEY` as repository secrets in your repo settings (settings > secrets > actions).

### Add a search interface[#](#add-a-search-interface)

Now inside your docs, you need to create a search interface. Because this is a headless interface, you can use it with any language. The only requirement is that you send the user query to the `query` Edge Function, which will stream an answer back from OpenAI. It might look something like this:

```
1const onSubmit = (e: Event) => {2  e.preventDefault()3  answer.value = ""4  isLoading.value = true56  const query = new URLSearchParams({ query: inputRef.current!.value })7  const projectUrl = `https://your-project-ref.supabase.co/functions/v1`8  const queryURL = `${projectURL}/${query}`9  const eventSource = new EventSource(queryURL)1011  eventSource.addEventListener("error", (err) => {12    isLoading.value = false13    console.error(err)14  })1516  eventSource.addEventListener("message", (e: MessageEvent) => {17    isLoading.value = false1819    if (e.data === "[DONE]") {20      eventSource.close()21      return22    }2324    const completionResponse: CreateCompletionResponse = JSON.parse(e.data)25    const text = completionResponse.choices[0].text2627    answer.value += text28  });2930  isLoading.value = true31}
```

## Resources[#](#resources)

*   Read about how we built [ChatGPT for the Supabase Docs](/blog/chatgpt-supabase-docs).
*   Read the pgvector Docs for [Embeddings and vector similarity](../../../database/extensions/pgvector/index.md)
*   See how to build something like this from scratch [using Next.js](../nextjs-vector-search/index.md).
