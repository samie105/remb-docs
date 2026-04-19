---
title: "Benchmarks ​"
source: "https://hono.dev/docs/concepts/benchmarks"
canonical_url: "https://hono.dev/docs/concepts/benchmarks"
docset: "hono"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:33:16.265Z"
content_hash: "424ff8ed639368ddb51837384f5dfbc8f528821d3bb146e14b18db8e986f2ee5"
menu_path: ["Benchmarks ​"]
section_path: []
nav_prev: {"path": "hono/docs/concepts/routers/index.md", "title": "Routers \u200b"}
nav_next: {"path": "hono/docs/concepts/web-standard/index.md", "title": "Web Standards \u200b"}
---

Benchmarks are only benchmarks, but they are important to us.

## Routers [​](#routers)

We measured the speeds of a bunch of JavaScript routers. For example, `find-my-way` is a very fast router used inside Fastify.

*   @medley/router
*   find-my-way
*   koa-tree-router
*   trek-router
*   express (includes handling)
*   koa-router

First, we registered the following routing to each of our routers. These are similar to those used in the real world.

ts

```
export const routes: Route[] = [
  { method: 'GET', path: '/user' },
  { method: 'GET', path: '/user/comments' },
  { method: 'GET', path: '/user/avatar' },
  { method: 'GET', path: '/user/lookup/username/:username' },
  { method: 'GET', path: '/user/lookup/email/:address' },
  { method: 'GET', path: '/event/:id' },
  { method: 'GET', path: '/event/:id/comments' },
  { method: 'POST', path: '/event/:id/comment' },
  { method: 'GET', path: '/map/:location/events' },
  { method: 'GET', path: '/status' },
  { method: 'GET', path: '/very/deeply/nested/route/hello/there' },
  { method: 'GET', path: '/static/*' },
]
```

Then we sent the Request to the endpoints like below.

ts

```
const routes: (Route & { name: string })[] = [
  {
    name: 'short static',
    method: 'GET',
    path: '/user',
  },
  {
    name: 'static with same radix',
    method: 'GET',
    path: '/user/comments',
  },
  {
    name: 'dynamic route',
    method: 'GET',
    path: '/user/lookup/username/hey',
  },
  {
    name: 'mixed static dynamic',
    method: 'GET',
    path: '/event/abcd1234/comments',
  },
  {
    name: 'post',
    method: 'POST',
    path: '/event/abcd1234/comment',
  },
  {
    name: 'long static',
    method: 'GET',
    path: '/very/deeply/nested/route/hello/there',
  },
  {
    name: 'wildcard',
    method: 'GET',
    path: '/static/index.html',
  },
]
```

Let's see the results.

### On Node.js [​](#on-node-js)

The following screenshots show the results on Node.js.

![](https://hono.dev/images/bench01.png)

![](https://hono.dev/images/bench02.png)

![](https://hono.dev/images/bench03.png)

![](https://hono.dev/images/bench04.png)

![](https://hono.dev/images/bench05.png)

![](https://hono.dev/images/bench06.png)

![](https://hono.dev/images/bench07.png)

![](https://hono.dev/images/bench08.png)

### On Bun [​](#on-bun)

The following screenshots show the results on Bun.

![](https://hono.dev/images/bench09.png)

![](https://hono.dev/images/bench10.png)

![](https://hono.dev/images/bench11.png)

![](https://hono.dev/images/bench12.png)

![](https://hono.dev/images/bench13.png)

![](https://hono.dev/images/bench14.png)

![](https://hono.dev/images/bench15.png)

![](https://hono.dev/images/bench16.png)

## Cloudflare Workers [​](#cloudflare-workers)

**Hono is the fastest**, compared to other routers for Cloudflare Workers.

*   Machine: Apple MacBook Pro, 32 GiB, M1 Pro
*   Scripts: [benchmarks/handle-event](https://github.com/honojs/hono/tree/main/benchmarks/handle-event)

```
Hono x 402,820 ops/sec ±4.78% (80 runs sampled)
itty-router x 212,598 ops/sec ±3.11% (87 runs sampled)
sunder x 297,036 ops/sec ±4.76% (77 runs sampled)
worktop x 197,345 ops/sec ±2.40% (88 runs sampled)
Fastest is Hono
✨  Done in 28.06s.
```

## Deno [​](#deno)

**Hono is the fastest**, compared to other frameworks for Deno.

*   Machine: Apple MacBook Pro, 32 GiB, M1 Pro, Deno v1.22.0
*   Scripts: [benchmarks/deno](https://github.com/honojs/hono/tree/main/benchmarks/deno)
*   Method: `bombardier --fasthttp -d 10s -c 100 'http://localhost:8000/user/lookup/username/foo'`

Framework

Version

Results

**Hono**

3.0.0

**Requests/sec: 136112**

Fast

4.0.0-beta.1

Requests/sec: 103214

Megalo

0.3.0

Requests/sec: 64597

Faster

5.7

Requests/sec: 54801

oak

10.5.1

Requests/sec: 43326

opine

2.2.0

Requests/sec: 30700

Another benchmark result: [denosaurs/bench](https://github.com/denosaurs/bench)

## Bun [​](#bun)

Hono is one of the fastest frameworks for Bun. You can see it below.

*   [SaltyAom/bun-http-framework-benchmark](https://github.com/SaltyAom/bun-http-framework-benchmark)
