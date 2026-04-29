---
title: "Concepts"
source: "https://trpc.io/docs/concepts"
canonical_url: "https://trpc.io/docs/concepts"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:21.814Z"
content_hash: "fccf4d6807da1358b2a41775f564cda5a98002eb1791e266c390e52d142287b9"
menu_path: ["Concepts"]
section_path: []
nav_prev: {"path": "trpc/docs/skills/index.md", "title": "Agent Skills"}
nav_next: {"path": "trpc/docs/example-apps/index.md", "title": "Example Apps"}
---

## What is RPC? What mindset should I adopt?[​](#what-is-rpc-what-mindset-should-i-adopt "Direct link to What is RPC? What mindset should I adopt?")

### It's just functions[​](#its-just-functions "Direct link to It's just functions")

RPC is short for "Remote Procedure Call". It is a way of calling functions on one computer (the server) from another computer (the client). With traditional HTTP/REST APIs, you call a URL and get a response. With RPC, you call a function and get a response.

ts

`// HTTP/REST`

`const res = await fetch('/api/users/1');`

`const user = await res.json();`

`// RPC`

`const user = await api.users.getById({ id: 1 });`

tRPC (TypeScript Remote Procedure Call) is one implementation of RPC, designed for TypeScript monorepos. It has its own flavor, but is RPC at its heart.

### Don't think about HTTP/REST implementation details[​](#dont-think-about-httprest-implementation-details "Direct link to Don't think about HTTP/REST implementation details")

If you inspect the network traffic of a tRPC app, you'll see that it's fairly standard HTTP requests and responses, but you don't need to think about the implementation details while writing your application code. You call functions, and tRPC takes care of everything else. You should ignore details like HTTP Verbs, since they carry meaning in REST APIs but, in RPC, form part of your function names instead, for instance: `getUser(id)` instead of `GET /users/:id`.

## Vocabulary[​](#vocabulary "Direct link to Vocabulary")

Below are some terms that are used frequently in the tRPC ecosystem. We'll be using these throughout the documentation, so it's good to get familiar with them. Most of these concepts also have their own pages in the documentation.

Term

Description

[**Procedure ↗**](../server/procedures/index.md)

API endpoint - can be a **query**, **mutation**, or **subscription**.

**Query**

A **procedure** that gets some data.

**Mutation**

A **procedure** that creates, updates, or deletes some data.

[**Subscription ↗**](https://trpc.io/docs/subscriptions)

A **procedure** that creates a persistent connection and listens to changes.

[**Router ↗**](../server/routers/index.md)

A collection of **procedures** (and/or other routers) under a shared namespace.

[**Context ↗**](../server/context/index.md)

Stuff that every **procedure** can access. Commonly used for things like session state and database connections.

[**Middleware ↗**](../server/middlewares/index.md)

A function that can run code before and after a **procedure**. Can modify **context**.

[**Validation ↗**](../server/procedures/index.md#input-validation)

"Does this input data contain the right stuff?"
