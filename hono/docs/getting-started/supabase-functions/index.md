---
title: "Supabase Edge Functions ​"
source: "https://hono.dev/docs/getting-started/supabase-functions"
canonical_url: "https://hono.dev/docs/getting-started/supabase-functions"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:02.710Z"
content_hash: "ee899c6911b76e6be857a13bb9e42fad482549d6b5bcbac404330385510bbf10"
menu_path: ["Supabase Edge Functions ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/google-cloud-run/index.md", "title": "Google Cloud Run \u200b"}
nav_next: {"path": "hono/docs/getting-started/ali-function-compute/index.md", "title": "Alibaba Cloud Function Compute \u200b"}
---

[Supabase](https://supabase.com/) is an open-source alternative to Firebase, offering a suite of tools similar to Firebase's capabilities, including database, authentication, storage, and now, serverless functions.

Supabase Edge Functions are server-side TypeScript functions that are distributed globally, running closer to your users for improved performance. These functions are developed using [Deno](https://deno.com/), which brings several benefits, including improved security and a modern JavaScript/TypeScript runtime.

Here's how you can get started with Supabase Edge Functions:

## 1\. Setup [​](#_1-setup)

### Prerequisites [​](#prerequisites)

Before you begin, make sure you have the Supabase CLI installed. If you haven't installed it yet, follow the instructions in the [official documentation](https://supabase.com/docs/guides/cli/getting-started).

### Creating a New Project [​](#creating-a-new-project)

1.  Open your terminal or command prompt.
    
2.  Create a new Supabase project in a directory on your local machine by running:
    

bash

```
supabase init
```

This command initializes a new Supabase project in the current directory.

### Adding an Edge Function [​](#adding-an-edge-function)

3.  Inside your Supabase project, create a new Edge Function named `hello-world`:

bash

```
supabase functions new hello-world
```

This command creates a new Edge Function with the specified name in your project.

## 2\. Hello World [​](#_2-hello-world)

Edit the `hello-world` function by modifying the file `supabase/functions/hello-world/index.ts`:

ts

```
import { Hono } from 'jsr:@hono/hono'

// change this to your function name
const functionName = 'hello-world'
const app = new Hono().basePath(`/${functionName}`)

app.get('/hello', (c) => c.text('Hello from hono-server!'))

Deno.serve(app.fetch)
```

## 3\. Run [​](#_3-run)

To run the function locally, use the following command:

1.  Use the following command to serve the function:

bash

```
supabase start # start the supabase stack
supabase functions serve --no-verify-jwt # start the Functions watcher
```

The `--no-verify-jwt` flag allows you to bypass JWT verification during local development.

2.  Make a GET request using cURL or Postman to `http://127.0.0.1:54321/functions/v1/hello-world/hello`:

bash

```
curl  --location  'http://127.0.0.1:54321/functions/v1/hello-world/hello'
```

This request should return the text "Hello from hono-server!".

## 4\. Deploy [​](#_4-deploy)

You can deploy all of your Edge Functions in Supabase with a single command:

bash

```
supabase functions deploy
```

Alternatively, you can deploy individual Edge Functions by specifying the name of the function in the deploy command:

bash

```
supabase functions deploy hello-world
```

For more deployment methods, visit the Supabase documentation on [Deploying to Production](https://supabase.com/docs/guides/functions/deploy).

