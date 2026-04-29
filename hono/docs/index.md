---
title: "Hono ​"
source: "https://hono.dev/docs/"
canonical_url: "https://hono.dev/docs/"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:27.252Z"
content_hash: "a50350254bf2c41db401b1f8ccfb625d0e91ce1517e42f3577027bfd64198ade"
menu_path: ["Hono ​"]
section_path: []
nav_prev: {"path": "middleware/third-party/index.md", "title": "Third-party Middleware \u200b"}
---

## Hono [​](#hono)

Hono - _**means flame🔥 in Japanese**_ - is a small, simple, and ultrafast web framework built on Web Standards. It works on any JavaScript runtime: Cloudflare Workers, Fastly Compute, Deno, Bun, Vercel, Netlify, AWS Lambda, Lambda@Edge, and Node.js.

Fast, but not only fast.

ts

```
import { Hono } from 'hono'
const app = new Hono()

app.get('/', (c) => c.text('Hono!'))

export default app
```

## Quick Start [​](#quick-start)

Just run this:

npmyarnpnpmbundeno

sh

```
npm create hono@latest
```

sh

```
yarn create hono
```

sh

```
pnpm create hono@latest
```

sh

```
bun create hono@latest
```

sh

```
deno init --npm hono@latest
```

## Features [​](#features)

*   **Ultrafast** 🚀 - The router `RegExpRouter` is really fast. Not using linear loops. Fast.
*   **Lightweight** 🪶 - The `hono/tiny` preset is under 14kB. Hono has zero dependencies and uses only the Web Standards.
*   **Multi-runtime** 🌍 - Works on Cloudflare Workers, Fastly Compute, Deno, Bun, AWS Lambda, or Node.js. The same code runs on all platforms.
*   **Batteries Included** 🔋 - Hono has built-in middleware, custom middleware, third-party middleware, and helpers. Batteries included.
*   **Delightful DX** 😃 - Super clean APIs. First-class TypeScript support. Now, we've got "Types".

## Use-cases [​](#use-cases)

Hono is a simple web application framework similar to Express, without a frontend. But it runs on CDN Edges and allows you to construct larger applications when combined with middleware. Here are some examples of use-cases.

*   Building Web APIs
*   Proxy of backend servers
*   Front of CDN
*   Edge application
*   Base server for a library
*   Full-stack application

## Who is using Hono? [​](#who-is-using-hono)

Project

Platform

What for?

[cdnjs](https://cdnjs.com/)

Cloudflare Workers

A free and open-source CDN service. _Hono is used for the API server_.

[Cloudflare D1](https://www.cloudflare.com/developer-platform/d1/)

Cloudflare Workers

Serverless SQL databases. _Hono is used for the internal API server_.

[Cloudflare Workers KV](https://www.cloudflare.com/developer-platform/workers-kv/)

Cloudflare Workers

Serverless key-value database. _Hono is used for the internal API server_.

[BaseAI](https://baseai.dev/)

Local AI Server

Serverless AI agent pipes with memory. An open-source agentic AI framework for web. _API server with Hono_.

[Unkey](https://unkey.dev/)

Cloudflare Workers

An open-source API authentication and authorization. _Hono is used for the API server_.

[OpenStatus](https://openstatus.dev/)

Bun

An open-source website & API monitoring platform. _Hono is used for the API server_.

[Deno Benchmarks](https://deno.com/benchmarks)

Deno

A secure TypeScript runtime built on V8. _Hono is used for benchmarking_.

[Clerk](https://clerk.com/)

Cloudflare Workers

An open-source User Management Platform. _Hono is used for the API server_.

And the following.

*   [Drivly](https://driv.ly/) - Cloudflare Workers
*   [repeat.dev](https://repeat.dev/) - Cloudflare Workers

Do you want to see more? See [Who is using Hono in production?](https://github.com/orgs/honojs/discussions/1510).

## Hono in 1 minute [​](#hono-in-1-minute)

A demonstration to create an application for Cloudflare Workers with Hono.

![A gif showing a hono app being created quickly with fast iteration.](https://hono.dev/images/sc.gif)

## Ultrafast [​](#ultrafast)

**Hono is the fastest**, compared to other routers for Cloudflare Workers.

```
Hono x 402,820 ops/sec ±4.78% (80 runs sampled)
itty-router x 212,598 ops/sec ±3.11% (87 runs sampled)
sunder x 297,036 ops/sec ±4.76% (77 runs sampled)
worktop x 197,345 ops/sec ±2.40% (88 runs sampled)
Fastest is Hono
✨  Done in 28.06s.
```

See [more benchmarks](concepts/benchmarks/index.md).

## Lightweight [​](#lightweight)

**Hono is so small**. With the `hono/tiny` preset, its size is **under 14KB** when minified. There are many middleware and adapters, but they are bundled only when used. For context, the size of Express is 572KB.

```
$ npx wrangler dev --minify ./src/index.ts
 ⛅️ wrangler 2.20.0
--------------------
⬣ Listening at http://0.0.0.0:8787
- http://127.0.0.1:8787
- http://192.168.128.165:8787
Total Upload: 11.47 KiB / gzip: 4.34 KiB
```

## Multiple routers [​](#multiple-routers)

**Hono has multiple routers**.

**RegExpRouter** is the fastest router in the JavaScript world. It matches the route using a single large Regex created before dispatch. With **SmartRouter**, it supports all route patterns.

**LinearRouter** registers the routes very quickly, so it's suitable for an environment that initializes applications every time. **PatternRouter** simply adds and matches the pattern, making it small.

See [more information about routes](concepts/routers/index.md).

Thanks to the use of the **Web Standards**, Hono works on a lot of platforms.

*   Cloudflare Workers
*   Cloudflare Pages
*   Fastly Compute
*   Deno
*   Bun
*   Vercel
*   AWS Lambda
*   Lambda@Edge
*   Others

And by using [a Node.js adapter](https://github.com/honojs/node-server), Hono works on Node.js.

See [more information about Web Standards](concepts/web-standard/index.md).

## Middleware & Helpers [​](#middleware-helpers)

**Hono has many middleware and helpers**. This makes "Write Less, do more" a reality.

Out of the box, Hono provides middleware and helpers for:

*   [Basic Authentication](middleware/builtin/basic-auth/index.md)
*   [Bearer Authentication](middleware/builtin/bearer-auth/index.md)
*   [Body Limit](middleware/builtin/body-limit/index.md)
*   [Cache](middleware/builtin/cache/index.md)
*   [Compress](middleware/builtin/compress/index.md)
*   [Context Storage](middleware/builtin/context-storage/index.md)
*   [Cookie](helpers/cookie/index.md)
*   [CORS](middleware/builtin/cors/index.md)
*   [ETag](middleware/builtin/etag/index.md)
*   [html](helpers/html/index.md)
*   [JSX](guides/jsx/index.md)
*   [JWT Authentication](middleware/builtin/jwt/index.md)
*   [Logger](middleware/builtin/logger/index.md)
*   [Language](middleware/builtin/language/index.md)
*   [Pretty JSON](middleware/builtin/pretty-json/index.md)
*   [Secure Headers](middleware/builtin/secure-headers/index.md)
*   [SSG](helpers/ssg/index.md)
*   [Streaming](helpers/streaming/index.md)
*   [GraphQL Server](https://github.com/honojs/middleware/tree/main/packages/graphql-server)
*   [Firebase Authentication](https://github.com/honojs/middleware/tree/main/packages/firebase-auth)
*   [Sentry](https://github.com/honojs/middleware/tree/main/packages/sentry)
*   Others!

For example, adding ETag and request logging only takes a few lines of code with Hono:

ts

```
import { Hono } from 'hono'
import { etag } from 'hono/etag'
import { logger } from 'hono/logger'

const app = new Hono()
app.use(etag(), logger())
```

See [more information about Middleware](concepts/middleware/index.md).

## Developer Experience [​](#developer-experience)

Hono provides a delightful "**Developer Experience**".

Easy access to Request/Response thanks to the `Context` object. Moreover, Hono is written in TypeScript. Hono has "**Types**".

For example, the path parameters will be literal types.

![A screenshot showing Hono having proper literal typing when URL parameters. The URL "/entry/:date/:id" allows for request parameters to be "date" or "id"](https://hono.dev/images/ss.png)

And, the Validator and Hono Client `hc` enable the RPC mode. In RPC mode, you can use your favorite validator such as Zod and easily share server-side API specs with the client and build type-safe applications.

See [Hono Stacks](concepts/stacks/index.md).
