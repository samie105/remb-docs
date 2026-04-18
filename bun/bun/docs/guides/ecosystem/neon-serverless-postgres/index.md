---
title: "Use Neon's Serverless Postgres with Bun"
source: "https://bun.com/docs/guides/ecosystem/neon-serverless-postgres"
canonical_url: "https://bun.com/docs/guides/ecosystem/neon-serverless-postgres"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:51.688Z"
content_hash: "4628f78de79e2625fd6c0b1d1795d6c1fcdbd4e8120dcc1b00b9778824c40385"
menu_path: ["Use Neon's Serverless Postgres with Bun"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/ecosystem/neon-drizzle/index.md", "title": "Use Neon Postgres through Drizzle ORM"}
nav_next: {"path": "bun/bun/docs/guides/ecosystem/nextjs/index.md", "title": "Build an app with Next.js and Bun"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

[Neon](https://neon.tech/) is a fully managed serverless Postgres. Neon separates compute and storage to offer modern developer features such as autoscaling, branching, bottomless storage, and more.

* * *

Get started by creating a project directory, initializing the directory using `bun init`, and adding the [Neon serverless driver](https://github.com/neondatabase/serverless/) as a project dependency.

terminal

```
mkdir bun-neon-postgres
cd bun-neon-postgres
bun init -y
bun add @neondatabase/serverless
```

* * *

Create a `.env.local` file and add your [Neon Postgres connection string](https://neon.tech/docs/connect/connect-from-any-app) to it.

.env.local

```
DATABASE_URL=postgresql://usertitle:password@ep-adj-noun-guid.us-east-1.aws.neon.tech/neondb?sslmode=require
```

* * *

Paste the following code into your project’s `index.ts` file.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { neon } from "@neondatabase/serverless";

// Bun automatically loads the DATABASE_URL from .env.local
// Refer to: https://bun.com/docs/runtime/environment-variables for more information
const sql = neon(process.env.DATABASE_URL);

const rows = await sql`SELECT version()`;

console.log(rows[0].version);
```

* * *

Start the program using `bun ./index.ts`. The Postgres version should be printed to the console.

terminal

```
bun ./index.ts
```

```
PostgreSQL 16.2 on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
```

* * *

This example used the Neon serverless driver’s SQL-over-HTTP functionality. Neon’s serverless driver also exposes `Client` and `Pool` constructors to enable sessions, interactive transactions, and node-postgres compatibility. Refer to [Neon’s documentation](https://neon.tech/docs/serverless/serverless-driver) for a complete overview of the serverless driver.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/neon-serverless-postgres.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/neon-serverless-postgres>)

[

Use Neon Postgres through Drizzle ORM

Previous

](/docs/guides/ecosystem/neon-drizzle)[

Build an app with Next.js and Bun

Next

](/docs/guides/ecosystem/nextjs)
