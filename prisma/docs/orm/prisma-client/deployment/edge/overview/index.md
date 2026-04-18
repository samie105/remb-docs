---
title: "Deploying edge functions with Prisma ORM"
source: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/overview"
canonical_url: "https://www.prisma.io/docs/orm/prisma-client/deployment/edge/overview"
docset: "prisma"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:58.852Z"
content_hash: "af143a134f4b47ba46279163527e6a0e705f5f32bc215e3b1fe50a3d722ede80"
menu_path: ["Deploying edge functions with Prisma ORM"]
section_path: []
---
Deployment

Edge

Learn how to deploy your Prisma-backed apps to edge functions like Cloudflare Workers or Vercel Edge Functions

You can deploy an application that uses Prisma ORM to the edge. Depending on which edge function provider and which database you use, there are different considerations and things to be aware of.

Questions answered in this page

*   Which database drivers work on edge?
*   How do driver adapters affect connections?
*   When to use Prisma Postgres or Accelerate?

Here is a brief overview of all the edge function providers that are currently supported by Prisma ORM:

Provider / Product

Supported natively with Prisma ORM

Supported with Prisma Postgres (and Prisma Accelerate)

Vercel Edge Functions

✅ (Preview; only compatible drivers)

✅

Vercel Edge Middleware

✅ (Preview; only compatible drivers)

✅

Cloudflare Workers

✅ (Preview; only compatible drivers)

✅

Cloudflare Pages

✅ (Preview; only compatible drivers)

✅

Deno Deploy

[Not yet](https://github.com/prisma/prisma/issues/2452)

✅

Deploying edge functions that use Prisma ORM on Cloudflare and Vercel is currently in [Preview](https://www.prisma.io/docs/orm/more/releases#preview).

### [Why are there limitations around database drivers in edge functions?](#why-are-there-limitations-around-database-drivers-in-edge-functions)

Edge functions typically don't use the standard Node.js runtime. For example, Vercel Edge Functions and Cloudflare Workers are running code in [V8 isolates](https://v8docs.nodesource.com/node-0.8/d5/dda/classv8_1_1_isolate.html). Deno Deploy is using the [Deno](https://deno.com/) JavaScript runtime. As a consequence, these edge functions only have access to a small subset of the standard Node.js APIs and also have constrained computing resources (CPU and memory).

In particular, the constraint of not being able to freely open TCP connections makes it difficult to talk to a traditional database from an edge function. While Cloudflare has introduced a [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) API that enables limited TCP connections, this still only enables database access using specific database drivers that are compatible with that API.

### [Which database drivers are edge-compatible?](#which-database-drivers-are-edge-compatible)

Here is an overview of the different database drivers and their compatibility with different edge function offerings:

*   [Neon Serverless](https://neon.tech/docs/serverless/serverless-driver) uses HTTP to access the database. It works with Cloudflare Workers and Vercel Edge Functions.
*   [PlanetScale Serverless](https://planetscale.com/docs/tutorials/planetscale-serverless-driver) uses HTTP to access the database. It works with Cloudflare Workers and Vercel Edge Functions.
*   [`node-postgres`](https://node-postgres.com/) (`pg`) uses Cloudflare's `connect()` (TCP) to access the database. It is only compatible with Cloudflare Workers, not with Vercel Edge Functions.
*   [`@libsql/client`](https://github.com/tursodatabase/libsql-client-ts) is used to access Turso databases. It works with Cloudflare Workers and Vercel Edge Functions.
*   [Cloudflare D1](https://developers.cloudflare.com/d1/) is used to access D1 databases. It is only compatible with Cloudflare Workers, not with Vercel Edge Functions.
*   [Prisma Postgres](https://www.prisma.io/docs/postgres) is used to access a PostgreSQL database built on bare-metal using unikernels. It is supported on both Cloudflare Workers and Vercel.

There's [also work being done](https://github.com/sidorares/node-mysql2/pull/2289) on the `node-mysql2` driver which will enable access to traditional MySQL databases from Cloudflare Workers and Pages in the future as well.

You can use all of these drivers with Prisma ORM using the respective [driver adapters](https://www.prisma.io/docs/orm/core-concepts/supported-databases/database-drivers).

Depending on which deployment provider and database/driver you use, there may be special considerations. Please take a look at the deployment docs for your respective scenario to make sure you can deploy your application successfully:

*   Cloudflare
    *   [PostgreSQL (traditional)](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#postgresql-traditional)
    *   [PlanetScale](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#planetscale)
    *   [Neon](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-cloudflare#neon)
    *   [Cloudflare D1](https://www.prisma.io/docs/guides/deployment/cloudflare-d1)
    *   [Prisma Postgres](https://developers.cloudflare.com/workers/tutorials/using-prisma-postgres-with-workers)
*   Vercel
    *   [Vercel Postgres](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#vercel-postgres)
    *   [Neon](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#neon)
    *   [PlanetScale](https://www.prisma.io/docs/orm/prisma-client/deployment/edge/deploy-to-vercel#planetscale)
    *   [Prisma Postgres](https://www.prisma.io/docs/guides/frameworks/nextjs)

If you want to deploy an app using Turso, you can follow the instructions [here](https://www.prisma.io/docs/orm/core-concepts/supported-databases/sqlite#using-driver-adapters).

[Edit on GitHub](https://github.com/prisma/docs/edit/main/apps/docs/content/docs/orm/prisma-client/deployment/edge/overview.mdx)
