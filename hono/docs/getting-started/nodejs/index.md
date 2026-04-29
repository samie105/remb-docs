---
title: "Node.js ​"
source: "https://hono.dev/docs/getting-started/nodejs"
canonical_url: "https://hono.dev/docs/getting-started/nodejs"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:52.776Z"
content_hash: "b380501355aaa01174f50692156b5381cf2a69dbcf8ce720f366b8d79557fbaf"
menu_path: ["Node.js ​"]
section_path: []
nav_prev: {"path": "../service-worker/index.md", "title": "Service Worker \u200b"}
nav_next: {"path": "../../api/hono/index.md", "title": "App - Hono \u200b"}
---

[Node.js](https://nodejs.org/) is an open-source, cross-platform JavaScript runtime environment.

Hono was not designed for Node.js at first, but with a [Node.js Adapter](https://github.com/honojs/node-server), it can run on Node.js as well.

INFO

It works on Node.js versions greater than 18.x. The specific required Node.js versions are as follows:

*   18.x => 18.14.1+
*   19.x => 19.7.0+
*   20.x => 20.0.0+

Essentially, you can simply use the latest version of each major release.

## 1\. Setup [​](#_1-setup)

A starter for Node.js is available. Start your project with "create-hono" command. Select `nodejs` template for this example.

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
import { serve } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono()
app.get('/', (c) => c.text('Hello Node.js!'))

serve(app)
```

If you want to gracefully shut down the server, write it like this:

ts

```
const server = serve(app)

// graceful shutdown
process.on('SIGINT', () => {
  server.close()
  process.exit(0)
})
process.on('SIGTERM', () => {
  server.close((err) => {
    if (err) {
      console.error(err)
      process.exit(1)
    }
    process.exit(0)
  })
})
```

## 3\. Run [​](#_3-run)

Run the development server locally. Then, access `http://localhost:3000` in your Web browser.

npmyarnpnpm

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

## Change port number [​](#change-port-number)

You can specify the port number with the `port` option.

ts

```
serve({
  fetch: app.fetch,
  port: 8787,
})
```

## Access the raw Node.js APIs [​](#access-the-raw-node-js-apis)

You can access the Node.js APIs from `c.env.incoming` and `c.env.outgoing`.

ts

```
import { Hono } from 'hono'
import { serve, type HttpBindings } from '@hono/node-server'
// or `Http2Bindings` if you use HTTP2

type Bindings = HttpBindings & {
  /* ... */
}

const app = new Hono<{ Bindings: Bindings }>()

app.get('/', (c) => {
  return c.json({
    remoteAddress: c.env.incoming.socket.remoteAddress,
  })
})

serve(app)
```

## Serve static files [​](#serve-static-files)

You can use `serveStatic` to serve static files from the local file system. For example, suppose the directory structure is as follows:

sh

```
./
├── favicon.ico
├── index.ts
└── static
    ├── hello.txt
    └── image.png
```

If a request to the path `/static/*` comes in and you want to return a file under `./static`, you can write the following:

ts

```
import { serveStatic } from '@hono/node-server/serve-static'

app.use('/static/*', serveStatic({ root: './' }))
```

WARNING

The `root` option resolves paths relative to the current working directory (`process.cwd()`). This means the behavior depends on **where you run your Node.js process from**, not where your source file is located. If you start your server from a different directory, file resolution may fail.

For reliable path resolution that always points to the same directory as your source file, use `import.meta.url`:

ts

```
import { fileURLToPath } from 'node:url'
import { serveStatic } from '@hono/node-server/serve-static'

app.use(
  '/static/*',
  serveStatic({ root: fileURLToPath(new URL('./', import.meta.url)) })
)
```

Use the `path` option to serve `favicon.ico` in the directory root:

ts

```
app.use('/favicon.ico', serveStatic({ path: './favicon.ico' }))
```

If a request to the path `/hello.txt` or `/image.png` comes in and you want to return a file named `./static/hello.txt` or `./static/image.png`, you can use the following:

ts

```
app.use('*', serveStatic({ root: './static' }))
```

### `rewriteRequestPath` [​](#rewriterequestpath)

If you want to map `http://localhost:3000/static/*` to `./statics`, you can use the `rewriteRequestPath` option:

ts

```
app.get(
  '/static/*',
  serveStatic({
    root: './',
    rewriteRequestPath: (path) =>
      path.replace(/^\/static/, '/statics'),
  })
)
```

## http2 [​](#http2)

You can run hono on a [Node.js http2 Server](https://nodejs.org/api/http2.html).

### unencrypted http2 [​](#unencrypted-http2)

ts

```
import { createServer } from 'node:http2'

const server = serve({
  fetch: app.fetch,
  createServer,
})
```

### encrypted http2 [​](#encrypted-http2)

ts

```
import { createSecureServer } from 'node:http2'
import { readFileSync } from 'node:fs'

const server = serve({
  fetch: app.fetch,
  createServer: createSecureServer,
  serverOptions: {
    key: readFileSync('localhost-privkey.pem'),
    cert: readFileSync('localhost-cert.pem'),
  },
})
```

## Building & Deployment [​](#building-deployment)

npmyarnpnpmbun

sh

```
npm run build
```

sh

```
yarn run build
```

sh

```
pnpm run build
```

sh

```
bun run build
```

### Dockerfile [​](#dockerfile)

Here is an example of a Node.js Dockerfile.

Dockerfile

```
FROM node:22-alpine AS base

FROM base AS builder

RUN apk add --no-cache gcompat
WORKDIR /app

COPY package*json tsconfig.json src ./

RUN npm ci && \
    npm run build && \
    npm prune --production

FROM base AS runner
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 hono

COPY --from=builder --chown=hono:nodejs /app/node_modules /app/node_modules
COPY --from=builder --chown=hono:nodejs /app/dist /app/dist
COPY --from=builder --chown=hono:nodejs /app/package.json /app/package.json

USER hono
EXPOSE 3000

CMD ["node", "/app/dist/index.js"]
```
