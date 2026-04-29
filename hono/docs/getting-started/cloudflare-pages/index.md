---
title: "Cloudflare Pages ​"
source: "https://hono.dev/docs/getting-started/cloudflare-pages"
canonical_url: "https://hono.dev/docs/getting-started/cloudflare-pages"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:35:47.014Z"
content_hash: "f1fd40ac614573c3a85237f91e083efde823340ecd5275ecc076620bde888b3e"
menu_path: ["Cloudflare Pages ​"]
section_path: []
nav_prev: {"path": "../cloudflare-workers/index.md", "title": "Cloudflare Workers \u200b"}
nav_next: {"path": "../deno/index.md", "title": "Deno \u200b"}
---

[Cloudflare Pages](https://pages.cloudflare.com/) is an edge platform for full-stack web applications. It serves static files and dynamic content provided by Cloudflare Workers.

Hono fully supports Cloudflare Pages. It introduces a delightful developer experience. Vite's dev server is fast, and deploying with Wrangler is super quick.

## 1\. Setup [​](#_1-setup)

A starter for Cloudflare Pages is available. Start your project with "create-hono" command. Select `cloudflare-pages` template for this example.

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

Below is a basic directory structure.

text

```
./
├── package.json
├── public
│   └── static // Put your static files.
│       └── style.css // You can refer to it as `/static/style.css`.
├── src
│   ├── index.tsx // The entry point for server-side.
│   └── renderer.tsx
├── tsconfig.json
└── vite.config.ts
```

## 2\. Hello World [​](#_2-hello-world)

Edit `src/index.tsx` like the following:

tsx

```
import { Hono } from 'hono'
import { renderer } from './renderer'

const app = new Hono()

app.get('*', renderer)

app.get('/', (c) => {
  return c.render(<h1>Hello, Cloudflare Pages!</h1>)
})

export default app
```

## 3\. Run [​](#_3-run)

Run the development server locally. Then, access `http://localhost:5173` in your Web browser.

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

## 4\. Deploy [​](#_4-deploy)

If you have a Cloudflare account, you can deploy to Cloudflare. In `package.json`, `$npm_execpath` needs to be changed to your package manager of choice.

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

### Deploy via the Cloudflare dashboard with GitHub [​](#deploy-via-the-cloudflare-dashboard-with-github)

1.  Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
2.  In Account Home, select Workers & Pages > Create application > Pages > Connect to Git.
3.  Authorize your GitHub account, and select the repository. In Set up builds and deployments, provide the following information:

Configuration option

Value

Production branch

`main`

Build command

`npm run build`

Build directory

`dist`

## Bindings [​](#bindings)

You can use Cloudflare Bindings like Variables, KV, D1, and others. In this section, let's use Variables and KV.

### Create `wrangler.toml` [​](#create-wrangler-toml)

First, create `wrangler.toml` for local Bindings:

sh

```
touch wrangler.toml
```

Edit `wrangler.toml`. Specify Variable with the name `MY_NAME`.

toml

```
[vars]
MY_NAME = "Hono"
```

### Create KV [​](#create-kv)

Next, make the KV. Run the following `wrangler` command:

sh

```
wrangler kv namespace create MY_KV --preview
```

Note down the `preview_id` as the following output:

```
{ binding = "MY_KV", preview_id = "abcdef" }
```

Specify `preview_id` with the name of Bindings, `MY_KV`:

toml

```
[[kv_namespaces]]
binding = "MY_KV"
id = "abcdef"
```

### Edit `vite.config.ts` [​](#edit-vite-config-ts)

Edit the `vite.config.ts`:

ts

```
import devServer from '@hono/vite-dev-server'
import adapter from '@hono/vite-dev-server/cloudflare'
import build from '@hono/vite-cloudflare-pages'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [
    devServer({
      entry: 'src/index.tsx',
      adapter, // Cloudflare Adapter
    }),
    build(),
  ],
})
```

### Use Bindings in your application [​](#use-bindings-in-your-application)

Use Variable and KV in your application. Set the types.

ts

```
type Bindings = {
  MY_NAME: string
  MY_KV: KVNamespace
}

const app = new Hono<{ Bindings: Bindings }>()
```

Use them:

tsx

```
app.get('/', async (c) => {
  await c.env.MY_KV.put('name', c.env.MY_NAME)
  const name = await c.env.MY_KV.get('name')
  return c.render(<h1>Hello! {name}</h1>)
})
```

### In production [​](#in-production)

For Cloudflare Pages, you will use `wrangler.toml` for local development, but for production, you will set up Bindings in the dashboard.

## Client-side [​](#client-side)

You can write client-side scripts and import them into your application using Vite's features. If `/src/client.ts` is the entry point for the client, simply write it in the script tag. Additionally, `import.meta.env.PROD` is useful for detecting whether it's running on a dev server or in the build phase.

tsx

```
app.get('/', (c) => {
  return c.html(
    <html>
      <head>
        {import.meta.env.PROD ? (
          <script type='module' src='/static/client.js'></script>
        ) : (
          <script type='module' src='/src/client.ts'></script>
        )}
      </head>
      <body>
        <h1>Hello</h1>
      </body>
    </html>
  )
})
```

In order to build the script properly, you can use the example config file `vite.config.ts` as shown below.

ts

```
import pages from '@hono/vite-cloudflare-pages'
import devServer from '@hono/vite-dev-server'
import { defineConfig } from 'vite'

export default defineConfig(({ mode }) => {
  if (mode === 'client') {
    return {
      build: {
        rollupOptions: {
          input: './src/client.ts',
          output: {
            entryFileNames: 'static/client.js',
          },
        },
      },
    }
  } else {
    return {
      plugins: [
        pages(),
        devServer({
          entry: 'src/index.tsx',
        }),
      ],
    }
  }
})
```

You can run the following command to build the server and client script.

sh

```
vite build --mode client && vite build
```

## Cloudflare Pages Middleware [​](#cloudflare-pages-middleware)

Cloudflare Pages uses its own [middleware](https://developers.cloudflare.com/pages/functions/middleware/) system that is different from Hono's middleware. You can enable it by exporting `onRequest` in a file named `_middleware.ts` like this:

ts

```
// functions/_middleware.ts
export async function onRequest(pagesContext) {
  console.log(`You are accessing ${pagesContext.request.url}`)
  return await pagesContext.next()
}
```

Using `handleMiddleware`, you can use Hono's middleware as Cloudflare Pages middleware.

ts

```
// functions/_middleware.ts
import { handleMiddleware } from 'hono/cloudflare-pages'

export const onRequest = handleMiddleware(async (c, next) => {
  console.log(`You are accessing ${c.req.url}`)
  await next()
})
```

You can also use built-in and 3rd party middleware for Hono. For example, to add Basic Authentication, you can use [Hono's Basic Authentication Middleware](../../middleware/builtin/basic-auth/index.md).

ts

```
// functions/_middleware.ts
import { handleMiddleware } from 'hono/cloudflare-pages'
import { basicAuth } from 'hono/basic-auth'

export const onRequest = handleMiddleware(
  basicAuth({
    username: 'hono',
    password: 'acoolproject',
  })
)
```

If you want to apply multiple middleware, you can write it like this:

ts

```
import { handleMiddleware } from 'hono/cloudflare-pages'

// ...

export const onRequest = [
  handleMiddleware(middleware1),
  handleMiddleware(middleware2),
  handleMiddleware(middleware3),
]
```

### Accessing `EventContext` [​](#accessing-eventcontext)

You can access [`EventContext`](https://developers.cloudflare.com/pages/functions/api-reference/#eventcontext) object via `c.env` in `handleMiddleware`.

ts

```
// functions/_middleware.ts
import { handleMiddleware } from 'hono/cloudflare-pages'

export const onRequest = [
  handleMiddleware(async (c, next) => {
    c.env.eventContext.data.user = 'Joe'
    await next()
  }),
]
```

Then, you can access the data value in via `c.env.eventContext` in the handler:

ts

```
// functions/api/[[route]].ts
import type { EventContext } from 'hono/cloudflare-pages'
import { handle } from 'hono/cloudflare-pages'

// ...

type Env = {
  Bindings: {
    eventContext: EventContext
  }
}

const app = new Hono<Env>().basePath('/api')

app.get('/hello', (c) => {
  return c.json({
    message: `Hello, ${c.env.eventContext.data.user}!`, // 'Joe'
  })
})

export const onRequest = handle(app)
```
