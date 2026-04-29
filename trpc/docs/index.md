---
title: "tRPC | tRPC"
source: "https://trpc.io/docs/"
canonical_url: "https://trpc.io/docs/"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:31.608Z"
content_hash: "081fc80a86489680c1364f7ebe52aad8a208bd706faeb1835f56acaace101582"
menu_path: ["tRPC | tRPC"]
section_path: []
nav_next: {"path": "trpc/docs/quickstart/index.md", "title": "Quickstart"}
---

End-to-end typesafe APIs made easy

[![weekly downloads](https://img.shields.io/npm/dm/%40trpc/server.svg)](https://npmcharts.com/compare/@trpc/server?interval=30) [![GitHub License](https://img.shields.io/github/license/trpc/trpc.svg?label=license&style=flat)](https://github.com/trpc/trpc) [![GitHub Stars](https://img.shields.io/github/stars/trpc/trpc.svg?label=%F0%9F%8C%9F%20stars&style=flat)](https://github.com/trpc/trpc)

## Introduction[​](#introduction "Direct link to Introduction")

tRPC lets you build & consume fully typesafe APIs without schemas or code generation. It combines concepts from [REST](https://www.sitepoint.com/rest-api/) and [GraphQL](https://graphql.org/) - if you are unfamiliar with either, take a look at the key [Concepts](concepts/index.md).

In full-stack TypeScript projects, keeping API contracts in sync between the client and server is a common pain point. tRPC does this by leveraging TypeScript's type inference directly, with no code generation step, and catches problems at build time.

tRPC can run standalone or mounted as an endpoint on your existing REST API using our extensive ecosystem of adapters.

## Features[​](#features "Direct link to Features")

*   ✅  Well-tested and production ready.
*   🧙‍♂️  Full static typesafety & autocompletion on the client, for inputs, outputs, and errors.
*   🐎  Snappy DX - No code generation, run-time bloat, or build pipeline.
*   🍃  Light - tRPC has zero runtime dependencies and a tiny client-side footprint.
*   🐻  For new and old projects - Easy to start with or add to your existing brownfield project.
*   🔋  Framework agnostic - The tRPC community has built [adapters](https://trpc.io/docs/awesome-trpc#-extensions--community-add-ons) for all of the most popular frameworks.
*   🥃  Subscriptions support - Add typesafe real-time updates to your application.
*   ⚡️  Request batching - Requests made at the same time can be automatically combined into one.
*   👀  Examples - Check out an [example](example-apps/index.md) to learn with or use as a starting point.

## Quick Look[​](#quick-look "Direct link to Quick Look")

*   [tRPC in 100 Seconds](https://www.youtube.com/watch?v=0DyAyLdVW0I)
*   [Matt Pocock: Learn tRPC in 5 minutes](https://www.youtube.com/watch?v=S6rcrkbsDI0)
*   [Chris Bautista: Making typesafe APIs easy with tRPC](https://www.youtube.com/watch?v=2LYM8gf184U)

See more on the [Videos & Community Resources](https://trpc.io/docs/videos-and-community-resources) page.

## Try tRPC[​](#try-trpc "Direct link to Try tRPC")

*   [Minimal Example](https://stackblitz.com/github/trpc/trpc/tree/main/examples/minimal?file=server%2Findex.ts&file=client%2Findex.ts&view=editor) — Node.js http server + client.
*   [Minimal Next.js Example](https://stackblitz.com/github/trpc/trpc/tree/main/examples/next-minimal-starter?file=src%2Fpages%2Fapi%2Ftrpc%2F%5Btrpc%5D.ts&file=src%2Fpages%2Findex.tsx) — single endpoint + page.

Or use an [example app](example-apps/index.md) to get started locally.

## Adopt tRPC[​](#adopt-trpc "Direct link to Adopt tRPC")

### Creating a new project[​](#creating-a-new-project "Direct link to Creating a new project")

Since tRPC can live inside of many different frameworks, you will first need to decide where you want to use it.

On the backend, there are [adapters](server/adapters/index.md) for a range of frameworks as well as vanilla Node.js. On the frontend, you can use our [TanStack React Query](client/tanstack-react-query/setup/index.md) or [Next.js](client/nextjs/index.md) integrations, a [third-party integration](community/awesome-trpc/index.md#frontend-frameworks) for a variety of other frameworks, or the [Vanilla Client](client/vanilla/setup/index.md), which works anywhere JavaScript runs.

After choosing your stack, you can either scaffold your app using a [template](example-apps/index.md), or start from scratch using the documentation for your chosen backend and frontend integration.

### Adding tRPC to an existing project[​](#adding-trpc-to-an-existing-project "Direct link to Adding tRPC to an existing project")

Adding tRPC to an existing project is not significantly different from starting a new project, so the same resources apply. The main challenge is that it can feel difficult to know how to integrate tRPC with your existing application. Here are some tips:

*   You don't need to port all of your existing backend logic to tRPC. A common migration strategy is to initially only use tRPC for new endpoints, and only later migrate existing endpoints to tRPC.
*   If you're not sure where to start, check the documentation for your backend [adapter](server/adapters/index.md) and frontend implementation, as well as the [example apps](example-apps/index.md).
*   If you are looking for some inspiration of how tRPC might look as part of a larger codebase, there are some examples in [Open-source projects using tRPC](community/awesome-trpc/index.md#-open-source-projects-using-trpc).

Join us on [Discord](https://trpc.io/discord) to ask questions and share your experiences!
