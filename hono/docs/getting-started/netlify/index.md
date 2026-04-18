---
title: "Netlify ​"
source: "https://hono.dev/docs/getting-started/netlify"
canonical_url: "https://hono.dev/docs/getting-started/netlify"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:04.490Z"
content_hash: "985c6efafed8752a03a28669ad7b501d0a20c563b41a5b6714ed9ed131bc629a"
menu_path: ["Netlify ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/nextjs/index.md", "title": "Next.js \u200b"}
nav_next: {"path": "hono/docs/getting-started/aws-lambda/index.md", "title": "AWS Lambda \u200b"}
---

Netlify provides static site hosting and serverless backend services. [Edge Functions](https://docs.netlify.com/edge-functions/overview/) enables us to make the web pages dynamic.

Edge Functions support writing in Deno and TypeScript, and deployment is made easy through the [Netlify CLI](https://docs.netlify.com/cli/get-started/). With Hono, you can create the application for Netlify Edge Functions.

## 1\. Setup [​](#_1-setup)

A starter for Netlify is available. Start your project with "create-hono" command. Select `netlify` template for this example.

npmyarnpnpmbundeno

sh

```
npm create hono@latest my-app
```

sh

```
yarn create hono my-app
```

sh

```
pnpm create hono my-app
```

sh

```
bun create hono@latest my-app
```

sh

```
deno init --npm hono my-app
```

Move into `my-app`.

## 2\. Hello World [​](#_2-hello-world)

Edit `netlify/edge-functions/index.ts`:

ts

```
import { Hono } from 'jsr:@hono/hono'
import { handle } from 'jsr:@hono/hono/netlify'

const app = new Hono()

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

export default handle(app)
```

## 3\. Run [​](#_3-run)

Run the development server with Netlify CLI. Then, access `http://localhost:8888` in your Web browser.

sh

```
netlify dev
```

## 4\. Deploy [​](#_4-deploy)

You can deploy with a `netlify deploy` command.

sh

```
netlify deploy --prod
```

## `Context` [​](#context)

You can access the Netlify's `Context` through `c.env`:

ts

```
import { Hono } from 'jsr:@hono/hono'
import { handle } from 'jsr:@hono/hono/netlify'

// Import the type definition
import type { Context } from 'https://edge.netlify.com/'

export type Env = {
  Bindings: {
    context: Context
  }
}

const app = new Hono<Env>()

app.get('/country', (c) =>
  c.json({
    'You are in': c.env.context.geo.country?.name,
  })
)

export default handle(app)
```
