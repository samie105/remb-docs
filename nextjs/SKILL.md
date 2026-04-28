## Overview

Next.js is a React framework for production that uses file-system routing, server rendering, and static generation to build full-stack applications. An agent must know it because routing, rendering, caching, and deployment contracts are all controlled by framework conventions and adapter interfaces.

## Mental Model

Next.js treats directories and files as URL routes, using special files and configuration to define layouts, loading states, and API boundaries. The framework compiles this into platform-agnostic outputs that adapters transform into hosting-specific deployments, bridging the CLI build step to runtime behavior. Start with the adapters overview to understand the platform bridge, then study the CLI and configuration contracts.
Links: [`nextjs/docs/app/api-reference/adapters/index.md`](nextjs/docs/app/api-reference/adapters/index.md), [`nextjs/docs/app/api-reference/cli/next/index.md`](nextjs/docs/app/api-reference/cli/next/index.md), [`nextjs/docs/app/api-reference/config/next-config-js/index.md`](nextjs/docs/app/api-reference/config/next-config-js/index.md)

## Learning Paths

**Getting Started**
1. `nextjs/docs/app/api-reference/cli/create-next-app/index.md`
2. `nextjs/docs/app/api-reference/cli/next/index.md`
3. `nextjs/docs/app/api-reference/config/next-config-js/index.md`
4. `nextjs/docs/app/api-reference/adapters/index.md`

**Production Ready**
1. `nextjs/docs/app/api-reference/config/next-config-js/index.md`
2. `nextjs/docs/app/api-reference/config/next-config-js/cacheHandlers/index.md`
3. `nextjs/docs/app/guides/how-revalidation-works/index.md`
4. `nextjs/docs/app/api-reference/adapters/runtime-integration/index.md`
5. `nextjs/docs/app/api-reference/adapters/testing-adapters/index.md`

**Reference Deep-Dive**
1. `nextjs/docs/app/api-reference/index.md`
2. `nextjs/docs/app/api-reference/adapters/output-types/index.md`
3. `nextjs/docs/app/api-reference/adapters/routing-information/index.md`
4. `nextjs/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter/index.md`
5. `nextjs/docs/app/api-reference/turbopack/index.md`

## Concept Map

- CLI & Tooling
  - Commands & Options
    - `nextjs/docs/app/api-reference/cli/next/index.md`
    - `nextjs/docs/app/api-reference/cli/create-next-app/index.md`
  - Turbopack
    - `nextjs/docs/app/api-reference/turbopack/index.md`
- Configuration
  - Core Config
    - `nextjs/docs/app/api-reference/config/next-config-js/index.md`
  - Cache & Revalidation
    - `nextjs/docs/app/api-reference/config/next-config-js/cacheHandlers/index.md`
    - `nextjs/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath/index.md`
    - `nextjs/docs/app/guides/how-revalidation-works/index.md`
- Adapters & Deployment
  - Overview & Use Cases
    - `nextjs/docs/app/api-reference/adapters/index.md`
    - `nextjs/docs/app/api-reference/adapters/use-cases/index.md`
  - Creating & Testing
    - `nextjs/docs/app/api-reference/adapters/creating-an-adapter/index.md`
    - `nextjs/docs/app/api-reference/adapters/testing-adapters/index.md`
  - Output Types
    - `nextjs/docs/app/api-reference/adapters/output-types/index.md`
  - Routing & Entrypoints
    - `nextjs/docs/app/api-reference/adapters/routing-information/index.md`
    - `nextjs/docs/app/api-reference/adapters/routing-with-next-routing/index.md`
    - `nextjs/docs/app/api-reference/adapters/invoking-entrypoints/index.md`
  - Runtime & PPR
    - `nextjs/docs/app/api-reference/adapters/runtime-integration/index.md`
    - `nextjs/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter/index.md`
  - API Surface
    - `nextjs/docs/app/api-reference/adapters/api-reference/index.md`
    - `nextjs/docs/app/api-reference/adapters/configuration/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Scaffold a new project | `nextjs/docs/app/api-reference/cli/create-next-app/index.md` |
| Understand build and dev commands | `nextjs/docs/app/api-reference/cli/next/index.md` |
| Configure next.config.js | `nextjs/docs/app/api-reference/config/next-config-js/index.md` |
| Learn how caching works | `nextjs/docs/app/guides/how-revalidation-works/index.md` |
| Deploy to a custom platform | `nextjs/docs/app/api-reference/adapters/index.md` |
| Build a custom adapter | `nextjs/docs/app/api-reference/adapters/creating-an-adapter/index.md` |
| Map outputs to pages, API routes, or app routes | `nextjs/docs/app/api-reference/adapters/output-types/index.md` |
| Handle routing in an adapter | `nextjs/docs/app/api-reference/adapters/routing-information/index.md` |
| Integrate with the runtime and PPR | `nextjs/docs/app/api-reference/adapters/runtime-integration/index.md` |
| Test an adapter before shipping | `nextjs/docs/app/api-reference/adapters/testing-adapters/index.md` |
| Use Turbopack | `nextjs/docs/app/api-reference/turbopack/index.md` |

## Top Must-Know Pages

1. `nextjs/docs/app/api-reference/adapters/index.md` — Entry point for understanding how Next.js bridges build output to any hosting platform.
2. `nextjs/docs/app/api-reference/cli/next/index.md` — Reference for all CLI commands, dev server options, and build flags.
3. `nextjs/docs/app/api-reference/config/next-config-js/index.md` — Central configuration file that controls phases, caching, and experimental features.
4. `nextjs/docs/app/api-reference/cli/create-next-app/index.md` — Tooling reference for bootstrapping projects with templates and linter options.
5. `nextjs/docs/app/api-reference/adapters/creating-an-adapter/index.md` — Step-by-step guide to building a custom deployment adapter.
6. `nextjs/docs/app/api-reference/adapters/output-types/index.md` — Defines the shape of pages, API routes, app pages, and app routes outputs.
7. `nextjs/docs/app/api-reference/adapters/routing-information/index.md` — Explains beforeMiddleware, beforeFiles, afterFiles, and dynamicRoutes adapter hooks.
8. `nextjs/docs/app/api-reference/adapters/runtime-integration/index.md` — Covers handler context, PPR chain headers, and cache integration.
9. `nextjs/docs/app/guides/how-revalidation-works/index.md` — Deep dive into the revalidation and caching lifecycle.
10. `nextjs/docs/app/api-reference/turbopack/index.md` — Documentation for the Turbopack bundler and its CLI integration.