---
title: "Next.js ​"
source: "https://hono.dev/docs/getting-started/nextjs"
canonical_url: "https://hono.dev/docs/getting-started/nextjs"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:54.777Z"
content_hash: "82a771ba1415da55996025fdc7098a50b1c9a5a5cf57c810ea2ba32b6be442e4"
menu_path: ["Next.js ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/vercel/index.md", "title": "Vercel \u200b"}
nav_next: {"path": "hono/docs/getting-started/netlify/index.md", "title": "Netlify \u200b"}
---

Next.js is a flexible React framework that gives you building blocks to create fast web applications.

You can run Hono on Next.js when using the Node.js runtime.  
On Vercel, deploying Hono with Next.js is easy by using Vercel Functions.

## 1\. Setup [​](#_1-setup)

A starter for Next.js is available. Start your project with "create-hono" command. Select `nextjs` template for this example.

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

Move into `my-app` and install the dependencies.

npmyarnpnpmbun

sh

```
cd my-app
npm i
```

sh

```
cd my-app
yarn
```

sh

```
cd my-app
pnpm i
```

sh

```
cd my-app
bun i
```

## 2\. Hello World [​](#_2-hello-world)

If you use the App Router, Edit `app/api/[[...route]]/route.ts`. Refer to the [Supported HTTP Methods](https://nextjs.org/docs/app/building-your-application/routing/route-handlers#supported-http-methods) section for more options.

ts

```
import { Hono } from 'hono'
import { handle } from 'hono/vercel'

const app = new Hono().basePath('/api')

app.get('/hello', (c) => {
  return c.json({
    message: 'Hello Next.js!',
  })
})

export const GET = handle(app)
export const POST = handle(app)
```

## 3\. Run [​](#_3-run)

Run the development server locally. Then, access `http://localhost:3000` in your Web browser.

npmyarnpnpmbun

sh

```
npm run dev
```

sh

```
yarn dev
```

sh

```
pnpm dev
```

sh

```
bun run dev
```

Now, `/api/hello` just returns JSON, but if you build React UIs, you can create a full-stack application with Hono.

## 4\. Deploy [​](#_4-deploy)

If you have a Vercel account, you can deploy by linking the Git repository.

## Pages Router [​](#pages-router)

If you use the Pages Router, you'll need to install the Node.js adapter first.

npmyarnpnpmbun

sh

```
npm i @hono/node-server
```

sh

```
yarn add @hono/node-server
```

sh

```
pnpm add @hono/node-server
```

sh

```
bun add @hono/node-server
```

Then, you can utilize the `handle` function imported from `@hono/node-server/vercel` in `pages/api/[[...route]].ts`.

ts

```
import { Hono } from 'hono'
import { handle } from '@hono/node-server/vercel'
import type { PageConfig } from 'next'

export const config: PageConfig = {
  api: {
    bodyParser: false,
  },
}

const app = new Hono().basePath('/api')

app.get('/hello', (c) => {
  return c.json({
    message: 'Hello Next.js!',
  })
})

export default handle(app)
```

In order for this to work with the Pages Router, it's important to disable Vercel Node.js helpers by setting up an environment variable in your project dashboard or in your `.env` file.

text

```
NODEJS_HELPERS=0
```

