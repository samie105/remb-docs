---
title: "Vector search with Next.js and OpenAI"
source: "https://supabase.com/docs/guides/ai/examples/nextjs-vector-search"
canonical_url: "https://supabase.com/docs/guides/ai/examples/nextjs-vector-search"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:48.432Z"
content_hash: "51d0e435b06059ee2e634a5427ecd030b1f18c5ece7d3c2e7456b58ca389199e"
menu_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Adding generative Q&A to your Next.js site","Adding generative Q&A to your Next.js site"]
section_path: ["AI & Vectors","AI & Vectors","JavaScript Examples","JavaScript Examples","Adding generative Q&A to your Next.js site","Adding generative Q&A to your Next.js site"]
nav_prev: {"path": "supabase/docs/guides/ai/examples/mixpeek-video-search/index.md", "title": "Video Search with Mixpeek Multimodal Embeddings"}
nav_next: {"path": "supabase/docs/guides/ai/examples/openai/index.md", "title": "Generating OpenAI GPT3 completions"}
---

# 

Vector search with Next.js and OpenAI

## 

Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.

* * *

While our [Headless Vector search](/docs/guides/ai/examples/headless-vector-search) provides a toolkit for generative Q&A, in this tutorial we'll go more in-depth, build a custom ChatGPT-like search experience from the ground-up using Next.js. You will:

1.  Convert your markdown into embeddings using OpenAI.
2.  Store you embeddings in Postgres using pgvector.
3.  Deploy a function for answering your users' questions.

You can read our [Supabase Clippy](/blog/chatgpt-supabase-docs) blog post for a full example.

We assume that you have a Next.js project with a collection of `.mdx` files nested inside your `pages` directory. We will start developing locally with the Supabase CLI and then push our local database changes to our hosted Supabase project. You can find the [full Next.js example on GitHub](https://github.com/supabase-community/nextjs-openai-doc-search).

## Create a project[#](#create-a-project)

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.

## Prepare the database[#](#prepare-the-database)

Let's prepare the database schema. We can use the "OpenAI Vector Search" quickstart in the [SQL Editor](/dashboard/project/_/sql), or you can copy/paste the SQL below and run it yourself.

1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
2.  Click **OpenAI Vector Search**.
3.  Click **Run**.

## Pre-process the knowledge base at build time[#](#pre-process-the-knowledge-base-at-build-time)

With our database set up, we need to process and store all `.mdx` files in the `pages` directory. You can find the full script [here](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts), or follow the steps below:

1

### Generate Embeddings

Create a new file `lib/generate-embeddings.ts` and copy the code over from [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/lib/generate-embeddings.ts).

```
1curl \2https://raw.githubusercontent.com/supabase-community/nextjs-openai-doc-search/main/lib/generate-embeddings.ts \3-o "lib/generate-embeddings.ts"
```

2

### Set up environment variables

We need some environment variables to run the script. Add them to your `.env` file and make sure your `.env` file is not committed to source control! You can get your local Supabase credentials by running `supabase status`.

```
1NEXT_PUBLIC_SUPABASE_URL=2NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=3SUPABASE_SERVICE_ROLE_KEY=45# Get your key at https://platform.openai.com/account/api-keys6OPENAI_API_KEY=
```

3

### Run script at build time

Include the script in your `package.json` script commands to enable Vercel to automatically run it at build time.

```
1"scripts": {2  "dev": "next dev",3  "build": "pnpm run embeddings && next build",4  "start": "next start",5  "embeddings": "tsx lib/generate-embeddings.ts"6},
```

## Create text completion with OpenAI API[#](#create-text-completion-with-openai-api)

Anytime a user asks a question, we need to create an embedding for their question, perform a similarity search, and then send a text completion request to the OpenAI API with the query and then context content merged together into a prompt.

All of this is glued together in a [Vercel Edge Function](https://vercel.com/docs/concepts/functions/edge-functions), the code for which can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/pages/api/vector-search.ts).

1

### Create Embedding for Question

In order to perform similarity search we need to turn the question into an embedding.

```
1const embeddingResponse = await fetch('https://api.openai.com/v1/embeddings', {2  method: 'POST',3  headers: {4    Authorization: `Bearer ${openAiKey}`,5    'Content-Type': 'application/json',6  },7  body: JSON.stringify({8    model: 'text-embedding-ada-002',9    input: sanitizedQuery.replaceAll('\n', ' '),10  }),11})1213if (embeddingResponse.status !== 200) {14  throw new ApplicationError('Failed to create embedding for question', embeddingResponse)15}1617const {18  data: [{ embedding }],19} = await embeddingResponse.json()
```

2

### Perform similarity search

Using the `embeddingResponse` we can now perform similarity search by performing an remote procedure call (RPC) to the database function we created earlier.

```
1const { error: matchError, data: pageSections } = await supabaseClient.rpc(2  'match_page_sections',3  {4    embedding,5    match_threshold: 0.78,6    match_count: 10,7    min_content_length: 50,8  }9)
```

3

### Perform text completion request

With the relevant content for the user's question identified, we can now build the prompt and make a text completion request via the OpenAI API.

If successful, the OpenAI API will respond with a `text/event-stream` response that we can forward to the client where we'll process the event stream to smoothly print the answer to the user.

```
1const prompt = codeBlock`2  ${oneLine`3    You are a very enthusiastic Supabase representative who loves4    to help people! Given the following sections from the Supabase5    documentation, answer the question using only that information,6    outputted in markdown format. If you are unsure and the answer7    is not explicitly written in the documentation, say8    "Sorry, I don't know how to help with that."9  `}1011  Context sections:12  ${contextText}1314  Question: """15  ${sanitizedQuery}16  """1718  Answer as markdown (including related code snippets if available):19`2021const completionOptions: CreateCompletionRequest = {22  model: 'gpt-3.5-turbo-instruct',23  prompt,24  max_tokens: 512,25  temperature: 0,26  stream: true,27}2829const response = await fetch('https://api.openai.com/v1/completions', {30  method: 'POST',31  headers: {32    Authorization: `Bearer ${openAiKey}`,33    'Content-Type': 'application/json',34  },35  body: JSON.stringify(completionOptions),36})3738if (!response.ok) {39  const error = await response.json()40  throw new ApplicationError('Failed to generate completion', error)41}4243// Proxy the streamed SSE response from OpenAI44return new Response(response.body, {45  headers: {46    'Content-Type': 'text/event-stream',47  },48})
```

## Display the answer on the frontend[#](#display-the-answer-on-the-frontend)

In a last step, we need to process the event stream from the OpenAI API and print the answer to the user. The full code for this can be found on [GitHub](https://github.com/supabase-community/nextjs-openai-doc-search/blob/main/components/SearchDialog.tsx).

```
1const handleConfirm = React.useCallback(2  async (query: string) => {3    setAnswer(undefined)4    setQuestion(query)5    setSearch('')6    dispatchPromptData({ index: promptIndex, answer: undefined, query })7    setHasError(false)8    setIsLoading(true)910    const eventSource = new SSE(`api/vector-search`, {11      headers: {12        apikey: process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY ?? '',13        Authorization: `Bearer ${process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY}`,14        'Content-Type': 'application/json',15      },16      payload: JSON.stringify({ query }),17    })1819    function handleError<T>(err: T) {20      setIsLoading(false)21      setHasError(true)22      console.error(err)23    }2425    eventSource.addEventListener('error', handleError)26    eventSource.addEventListener('message', (e: any) => {27      try {28        setIsLoading(false)2930        if (e.data === '[DONE]') {31          setPromptIndex((x) => {32            return x + 133          })34          return35        }3637        const completionResponse: CreateCompletionResponse = JSON.parse(e.data)38        const text = completionResponse.choices[0].text3940        setAnswer((answer) => {41          const currentAnswer = answer ?? ''4243          dispatchPromptData({44            index: promptIndex,45            answer: currentAnswer + text,46          })4748          return (answer ?? '') + text49        })50      } catch (err) {51        handleError(err)52      }53    })5455    eventSource.stream()5657    eventSourceRef.current = eventSource5859    setIsLoading(true)60  },61  [promptIndex, promptData]62)
```

## Learn more[#](#learn-more)

Want to learn more about the awesome tech that is powering this?

*   Read about how we built [ChatGPT for the Supabase Docs](/blog/chatgpt-supabase-docs).
*   Read the pgvector Docs for [Embeddings and vector similarity](/docs/guides/database/extensions/pgvector)
*   Watch Greg's video for a full breakdown:
