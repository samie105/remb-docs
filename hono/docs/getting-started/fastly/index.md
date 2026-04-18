---
title: "Fastly Compute ​"
source: "https://hono.dev/docs/getting-started/fastly"
canonical_url: "https://hono.dev/docs/getting-started/fastly"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:00.035Z"
content_hash: "3122fde8d0f8a57f03112cfd9b607f6f88593cfd6e268e043890e63838a29105"
menu_path: ["Fastly Compute ​"]
section_path: []
nav_prev: {"path": "hono/docs/getting-started/bun/index.md", "title": "Bun \u200b"}
nav_next: {"path": "hono/docs/getting-started/vercel/index.md", "title": "Vercel \u200b"}
---

[Fastly Compute](https://www.fastly.com/products/edge-compute) is an advanced edge computing system that runs your code, in your favorite language, on Fastly's global edge network. Hono also works on Fastly Compute.

You can develop the application locally and publish it with a few commands using [Fastly CLI](https://www.fastly.com/documentation/reference/tools/cli/), which is installed locally automatically as part of the template.

## 1\. Setup [​](#_1-setup)

A starter for Fastly Compute is available. Start your project with "create-hono" command. Select `fastly` template for this example.

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

Move to `my-app` and install the dependencies.

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

Edit `src/index.ts`:

ts

```
// src/index.ts
import { Hono } from 'hono'
import { fire } from '@fastly/hono-fastly-compute'

const app = new Hono()

app.get('/', (c) => c.text('Hello Fastly!'))

fire(app)
```

NOTE

When using `fire` (or `buildFire()`) from `@fastly/hono-fastly-compute'` at the top level of your application, it is suitable to use `Hono` from `'hono'` rather than `'hono/quick'`, because `fire` causes its router to build its internal data during the application initialization phase.

## 3\. Run [​](#_3-run)

Run the development server locally. Then, access `http://localhost:7676` in your Web browser.

npmyarnpnpmbun

sh

```
npm run start
```

sh

```
yarn start
```

sh

```
pnpm run start
```

sh

```
bun run start
```

## 4\. Deploy [​](#_4-deploy)

To build and deploy your application to your Fastly account, type the following command. The first time you deploy the application, you will be prompted to create a new service in your account.

If you don't have an account yet, you must [create your Fastly account](https://www.fastly.com/signup/).

npmyarnpnpmbun

sh

```
npm run deploy
```

sh

```
yarn deploy
```

sh

```
pnpm run deploy
```

sh

```
bun run deploy
```

## Bindings [​](#bindings)

In Fastly Compute, you can bind Fastly platform resources, such as KV Stores, Config Stores, Secret Stores, Backends, Access Control Lists, Named Log Streams, and Environment Variables. You can access them through `c.env`, and will have their individual SDK types.

To use these bindings, import `buildFire` instead of `fire` from `@fastly/hono-fastly-compute`. Define your [bindings](https://github.com/fastly/compute-js-context?tab=readme-ov-file#typed-bindings-with-buildcontextproxy) and pass them to [`buildFire()`](https://github.com/fastly/hono-fastly-compute?tab=readme-ov-file#basic-example) to obtain `fire`. Then use `fire.Bindings` to define your `Env` type as you construct `Hono`.

ts

```
// src/index.ts
import { buildFire } from '@fastly/hono-fastly-compute'

const fire = buildFire({
  siteData: 'KVStore:site-data', // I have a KV Store named "site-data"
})

const app = new Hono<{ Bindings: typeof fire.Bindings }>()

app.put('/upload/:key', async (c, next) => {
  // e.g., Access the KV Store
  const key = c.req.param('key')
  await c.env.siteData.put(key, c.req.body)
  return c.text(`Put ${key} successfully!`)
})

fire(app)
```


