---
title: "Overview"
source: "https://trpc.io/docs/server/adapters"
canonical_url: "https://trpc.io/docs/server/adapters"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:59.803Z"
content_hash: "6d926a3122c9384ea0ade18ee892b8ae631832d1f55e31b9308467c858fed852"
menu_path: ["Overview"]
section_path: []
nav_prev: {"path": "../../rpc/index.md", "title": "HTTP RPC Specification"}
nav_next: {"path": "aws-lambda/index.md", "title": "AWS Lambda + API Gateway Adapter"}
---

tRPC is not a server on its own, and must therefore be served using other hosts, such as a simple [Node.js HTTP Server](standalone/index.md), [Express](express/index.md), or even [Next.js](nextjs/index.md). Most tRPC features are the same no matter which backend you choose. **Adapters** act as the glue between the host system and your tRPC API.

Adapters typically follow some common conventions, allowing you to set up context creation via `createContext`, and globally handle errors via `onError`, but importantly allow you to choose an appropriate host for your application.

We support many modes of hosting an API, which you will find documented here.

*   For serverful APIs, you might want our [Standalone](standalone/index.md) adapter, or use the [Express](express/index.md) or [Fastify](fastify/index.md) adapters to hook into your existing APIs
*   You might want a serverless solution and choose [AWS Lambda](aws-lambda/index.md), or [Fetch](fetch/index.md) for edge runtimes
*   You might have a full-stack framework and want a full integration like [Next.js](nextjs/index.md), or you could use the [Fetch](fetch/index.md) adapter with Next.js, Astro, Remix, or SolidStart

tip

For local development or serverful infrastructure, the simplest Adapter to use is the [Standalone Adapter](standalone/index.md), which can be used to run a standard Node.js HTTP Server. We recommend this when you need to get started quickly and have no existing HTTP Server to integrate with. Swapping out later is trivial if your needs change.
