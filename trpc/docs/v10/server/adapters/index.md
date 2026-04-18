---
title: "Adapters"
source: "https://trpc.io/docs/v10/server/adapters"
canonical_url: "https://trpc.io/docs/v10/server/adapters"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:01.847Z"
content_hash: "e87309762e7e2c4afec66dc94e9ee809b6b06b537d3e3def545bafe1dd576fec"
menu_path: ["Adapters"]
section_path: []
---
tRPC is not a server on its own, and must therefore be served using other hosts, such as a simple [Node.js HTTP Server](https://trpc.io/docs/v10/server/adapters/standalone), [Express](https://trpc.io/docs/v10/server/adapters/express), or even [Next.js](https://trpc.io/docs/v10/server/adapters/nextjs). Most tRPC features are the same no matter which backend you choose. **Adapters** act as the glue between the host system and your tRPC API.

Adapters typically follow some common conventions, allowing you to set up context creation via `createContext`, and globally handle errors via `onError`, but importantly allow you to choose an appropriate host for your application.

We support many modes of hosting an API, which you will find documented here.

*   For serverful APIs, you might want our [Standalone](https://trpc.io/docs/v10/server/adapters/standalone) adapter, or use the [Express](https://trpc.io/docs/v10/server/adapters/express) or [Fastify](https://trpc.io/docs/v10/server/adapters/fastify) adapters to hook into your existing APIs
*   You might want a serverless solution and choose [AWS Lambda](https://trpc.io/docs/v10/server/adapters/aws-lambda), or [Fetch](https://trpc.io/docs/v10/server/adapters/fetch) for edge runtimes
*   You might have a full-stack framework and want a full integration like [Next.js](https://trpc.io/docs/v10/server/adapters/nextjs), or you could use the [Fetch](https://trpc.io/docs/v10/server/adapters/fetch) adapter with Next.js, Astro, Remix, or SolidStart

tip

For local development or serverful infrastructure, the simplest Adapter to use is the [Standalone Adapter](https://trpc.io/docs/v10/server/adapters/standalone), which can be used to run a standard Node.js HTTP Server. We recommend this when you need to get started quickly and have no existing HTTP Server to integrate with. Swapping out later is trivial if your needs change.
