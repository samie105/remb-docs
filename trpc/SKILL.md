## Overview

tRPC is a TypeScript toolkit for building end-to-end typesafe APIs without schemas or code generation. It lets you define procedures on the server and call them directly from the client with full autocompletion and type inference. An agent needs to know it to navigate its router-based server architecture, link-based client configuration, and framework-specific setup patterns.

## Mental Model

tRPC splits concerns into a type-safe backend built from routers and procedures, and a flexible client that composes behavior through links. The server exposes functions; the client consumes them via HTTP, WebSockets, or batching links, with context flowing through every request. Start with `trpc/docs/quickstart/index.md` for the server, then `trpc/docs/client/index.md` for the vanilla client, and `trpc/docs/client/links/index.md` to understand how requests travel.

## Learning Paths

**Getting Started**
1. `trpc/docs/quickstart/index.md`
2. `trpc/docs/server/routers/index.md`
3. `trpc/docs/server/context/index.md`
4. `trpc/docs/client/index.md`

**Production Ready**
1. `trpc/docs/server/adapters/index.md`
2. `trpc/docs/server/middlewares/index.md`
3. `trpc/docs/server/validators/index.md`
4. `trpc/docs/server/data-transformers/index.md`
5. `trpc/docs/client/headers/index.md`

**Reference Deep-Dive**
1. `trpc/docs/server/error-handling/index.md`
2. `trpc/docs/server/error-formatting/index.md`
3. `trpc/docs/server/metadata/index.md`
4. `trpc/docs/typedoc/client/index/type-aliases/TRPCLink/index.md`
5. `trpc/docs/client/links/index.md`

## Concept Map

- **Server Foundation**
  - Routers: `trpc/docs/server/routers/index.md`
  - Procedures: `trpc/docs/server/procedures/index.md`
  - Context: `trpc/docs/server/context/index.md`
  - Middlewares: `trpc/docs/server/middlewares/index.md`
  - Validators: `trpc/docs/server/validators/index.md`
- **Client Transport**
  - Links Overview: `trpc/docs/client/links/index.md`
  - HTTP Link: `trpc/docs/client/links/httpLink/index.md`
  - Batch Link: `trpc/docs/client/links/httpBatchLink/index.md`
  - Batch Stream Link: `trpc/docs/client/links/httpBatchStreamLink/index.md`
  - Subscription Link: `trpc/docs/client/links/httpSubscriptionLink/index.md`
  - WebSocket Link: `trpc/docs/client/links/wsLink/index.md`
- **Framework Setup**
  - Next.js App Router: `trpc/docs/client/nextjs/app-router-setup/index.md`
  - Next.js Pages Router SSR: `trpc/docs/client/nextjs/pages-router/ssr/index.md`
  - Next.js Pages Router SSG: `trpc/docs/client/nextjs/pages-router/ssg/index.md`
  - TanStack Query: `trpc/docs/client/tanstack-react-query/setup/index.md`
- **Deployment & Adapters**
  - Adapters Overview: `trpc/docs/server/adapters/index.md`
  - Standalone: `trpc/docs/server/adapters/standalone/index.md`
  - Fetch / Edge: `trpc/docs/server/adapters/fetch/index.md`
  - Express: `trpc/docs/server/adapters/express/index.md`
- **Advanced Topics**
  - Data Transformers: `trpc/docs/server/data-transformers/index.md`
  - Error Handling: `trpc/docs/server/error-handling/index.md`
  - Error Formatting: `trpc/docs/server/error-formatting/index.md`
  - CORS: `trpc/docs/client/cors/index.md`
  - Headers: `trpc/docs/client/headers/index.md`
  - Server-Side Calls: `trpc/docs/server/server-side-calls/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Bootstrap a new project | `trpc/docs/quickstart/index.md` |
| Set up Next.js App Router | `trpc/docs/client/nextjs/app-router-setup/index.md` |
| Choose or configure a server adapter | `trpc/docs/server/adapters/index.md` |
| Add request context (auth, headers) | `trpc/docs/server/context/index.md` |
| Validate procedure inputs | `trpc/docs/server/validators/index.md` |
| Compose client transport logic | `trpc/docs/client/links/index.md` |
| Send cookies cross-origin | `trpc/docs/client/cors/index.md` |
| Handle custom headers | `trpc/docs/client/headers/index.md` |
| Stream or batch requests | `trpc/docs/client/links/httpBatchStreamLink/index.md` |
| Use WebSocket subscriptions | `trpc/docs/client/links/httpSubscriptionLink/index.md` |
| Transform data over the wire | `trpc/docs/server/data-transformers/index.md` |
| Merge multiple routers | `trpc/docs/server/merging-routers/index.md` |
| Call procedures server-to-server | `trpc/docs/server/server-side-calls/index.md` |

## Top Must-Know Pages

1. `trpc/docs/quickstart/index.md` — Covers installation and your first router, query, and input parser.
2. `trpc/docs/server/routers/index.md` — Defines router initialization, sub-routers, and runtime configuration.
3. `trpc/docs/server/context/index.md` — Explains how to create inner and outer context for requests.
4. `trpc/docs/client/index.md` — Describes when to use the vanilla client and its limitations.
5. `trpc/docs/client/links/index.md` — The canonical reference for terminating links and custom link chains.
6. `trpc/docs/client/nextjs/app-router-setup/index.md` — Step-by-step deps, router, and handler setup for Next.js App Router.
7. `trpc/docs/server/adapters/fetch/index.md` — Reference for deploying tRPC on edge runtimes using Web APIs.
8. `trpc/docs/server/validators/index.md` — How to parse and validate procedure inputs before execution.
9. `trpc/docs/server/data-transformers/index.md` — Configuring superjson, devalue, or asymmetric upload/download transformers.
10. `trpc/docs/server/error-handling/index.md` — Patterns for catching, formatting, and returning backend errors.