---
title: "tRPC"
source: "https://trpc.io/docs/v10/"
canonical_url: "https://trpc.io/docs/v10/"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:31:48.149Z"
content_hash: "c36bfcd104efa17936c5c23c1660d45db4ce2cde49a03ef4351082e8d015d0ab"
menu_path: ["tRPC"]
section_path: []
nav_prev: {"path": "trpc/docs/example-apps/index.md", "title": "Example Apps"}
nav_next: {"path": "trpc/docs/v10/client/index.md", "title": "Client Overview"}
---

End-to-end typesafe APIs made easy

[![codecov](https://codecov.io/gh/trpc/trpc/branch/main/graph/badge.svg?token=KPPS918B0G)](https://codecov.io/gh/trpc/trpc) [![weekly downloads](https://img.shields.io/npm/dm/%40trpc/server.svg)](https://npmcharts.com/compare/@trpc/server?interval=30) [![GitHub License](https://img.shields.io/github/license/trpc/trpc.svg?label=license&style=flat)](https://github.com/trpc/trpc) [![GitHub Stars](https://img.shields.io/github/stars/trpc/trpc.svg?label=%F0%9F%8C%9F%20stars&style=flat)](https://github.com/trpc/trpc)

## Introduction[​](#introduction "Direct link to Introduction")

tRPC allows you to easily build & consume fully typesafe APIs without schemas or code generation.

As TypeScript and static typing increasingly becomes a best practice in web development, API contracts present a major pain point. We need better ways to **statically type** our API endpoints and **share those types** between our client and server (or server-to-server). We set out to build a simple library for building typesafe APIs that leverages the full power of modern TypeScript.

### An alternative to traditional REST or GraphQL[​](#an-alternative-to-traditional-rest-or-graphql "Direct link to An alternative to traditional REST or GraphQL")

Currently, GraphQL is the dominant way to implement typesafe APIs in TypeScript ([and it's amazing!](trpc/docs/v10/further-reading/index.md#relationship-to-graphql)). Since GraphQL is designed as a language-agnostic specification for implementing APIs, it doesn't take full advantage of the power of a language like TypeScript.

If your project is built with full-stack TypeScript, you can share types **directly** between your client and server, without relying on code generation.

### Who is tRPC for?[​](#who-is-trpc-for "Direct link to Who is tRPC for?")

tRPC is for full-stack TypeScript developers. It makes it easy to write endpoints that you can safely use in both the front and backend of your app. Type errors with your API contracts will be caught at build time, reducing the surface for bugs in your application at runtime.

## Features[​](#features "Direct link to Features")

*   ✅  Well-tested and production ready.
*   🧙‍♂️  Full static typesafety & autocompletion on the client, for inputs, outputs, and errors.
*   🐎  Snappy DX - No code generation, run-time bloat, or build pipeline.
*   🍃  Light - tRPC has zero deps and a tiny client-side footprint.
*   🐻  For new and old projects - Easy to start with or add to your existing brownfield project.
*   🔋  Framework agnostic - The tRPC community has built [adapters](https://trpc.io/docs/awesome-trpc#-extensions--community-add-ons) for all of the most popular frameworks.
*   🥃  Subscriptions support - Add typesafe observability to your application.
*   ⚡️  Request batching - Requests made at the same time can be automatically combined into one.
*   👀  Examples - Check out an [example](trpc/docs/v10/example-apps/index.md) to learn with or use as a starting point.

