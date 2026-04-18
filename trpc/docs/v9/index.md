---
title: "tRPC | tRPC"
source: "https://trpc.io/docs/v9/"
canonical_url: "https://trpc.io/docs/v9/"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:40:57.118Z"
content_hash: "28411899305acb7935b8c2fa6db494300359795be88d00e0e89054aca513aec5"
menu_path: ["tRPC | tRPC"]
section_path: []
---
![tRPC](https://trpc.io/img/logo-text-white.svg)

End-to-end typesafe APIs made easy

[![codecov](https://codecov.io/gh/trpc/trpc/branch/main/graph/badge.svg?token=KPPS918B0G)](https://codecov.io/gh/trpc/trpc)[![GitHub License](https://img.shields.io/github/license/trpc/trpc.svg?label=license&style=flat)](https://github.com/trpc/trpc)[![GitHub Stars](https://img.shields.io/github/stars/trpc/trpc.svg?label=%F0%9F%8C%9F%20stars&style=flat)](https://github.com/trpc/trpc)

## Watch Video

[Alex / KATT](https://twitter.com/alexdotjs) and Prisma's Mahmoud Abdelwahab doing a deep dive into tRPC.

## Introduction[​](#introduction "Direct link to Introduction")

tRPC allows you to easily build & consume fully typesafe APIs, without schemas or code generation.

As TypeScript and static typing increasingly becomes a best practice in web programming, the API presents a major pain point. We need better ways to **statically type** our API endpoints and **share those types** between our client and server (or server-to-server). We set out to build a simple library for building typesafe APIs that leverages the full power of modern TypeScript. Introducing tRPC!

### An alternative to traditional REST or GraphQL[​](#an-alternative-to-traditional-rest-or-graphql "Direct link to An alternative to traditional REST or GraphQL")

Currently GraphQL is the dominant way to implement typesafe APIs in TypeScript (and it's amazing!). Since GraphQL is designed as a language-agnostic specification for implementing APIs, it doesn't take full advantage of the power of a language like TypeScript - [further reading](https://trpc.io/docs/v9/further-reading#relationship-to-graphql).

If your project is built with full-stack TypeScript, you can share types **directly** between your client and server, without relying on code generation.

## Features[​](#features "Direct link to Features")

*   ✅  Well-tested and production ready.
*   🧙‍♂️  Full static typesafety & autocompletion on the client, for inputs, outputs and errors.
*   🐎  Snappy DX - No code generation, run-time bloat, or build pipeline.
*   🍃  Light - tRPC has zero deps and a tiny client-side footprint.
*   🐻  Easy to add to your existing brownfield project.
*   🔋  Batteries included - React.js/Next.js/Express.js/Fastify adapters. _(But tRPC is not tied to React and there are many [community adapters](https://trpc.io/docs/awesome-trpc#-extensions--community-add-ons) for other libraries)_
*   🥃  Subscriptions support.
*   ⚡️  Request batching - requests made at the same time can be automatically combined into one.
*   👀  Quite a few [examples](https://trpc.io/docs/v9/example-apps) that you can use for reference or as a starting point.
