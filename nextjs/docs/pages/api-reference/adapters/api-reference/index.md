---
title: "API Reference"
source: "https://nextjs.org/docs/pages/api-reference/adapters/api-reference"
canonical_url: "https://nextjs.org/docs/pages/api-reference/adapters/api-reference"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:21.299Z"
content_hash: "181b09382fa3ce3a692dee490d223e83ee8fe374acd2120d4c44bcdb8db751e4"
menu_path: ["API Reference"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/adapters/creating-an-adapter/index.md", "title": "Creating an Adapter"}
nav_next: {"path": "nextjs/docs/pages/api-reference/adapters/testing-adapters/index.md", "title": "Testing Adapters"}
---

# API Reference

Last updated April 23, 2026

## `async modifyConfig(config, context)`[](#async-modifyconfigconfig-context)

Called for any CLI command that loads the `next.config.js` file to allow modification of the configuration.

**Parameters:**

-   `config`: The complete Next.js configuration object
-   `context.phase`: The current build phase (see [phases](/docs/app/api-reference/config/next-config-js#phase))
-   `context.nextVersion`: Version of Next.js being used

**Returns:** The modified configuration object (can be async)

## `async onBuildComplete(context)`[](#async-onbuildcompletecontext)

Called after the build process completes with detailed information about routes and outputs.

**Parameters:**

-   `context.routing`: Object containing Next.js routing phases and metadata
    -   `routing.beforeMiddleware`: Routes executed before middleware (includes header and redirect handling)
    -   `routing.beforeFiles`: Rewrite routes checked before filesystem route matching
    -   `routing.afterFiles`: Rewrite routes checked after filesystem route matching
    -   `routing.dynamicRoutes`: Dynamic route matching table
    -   `routing.onMatch`: Routes applied after a successful match (for example immutable static asset cache headers)
    -   `routing.fallback`: Final rewrite fallback routes
    -   `routing.shouldNormalizeNextData`: Whether `/_next/data/<buildId>/...` URLs should be normalized during matching
    -   `routing.rsc`: Route metadata used for React Server Components routing behavior
-   `context.outputs`: Detailed information about all build outputs organized by type
-   `context.projectDir`: Absolute path to the Next.js project directory
-   `context.repoRoot`: Absolute path to the detected repository root
-   `context.distDir`: Absolute path to the build output directory
-   `context.config`: The final Next.js configuration (with `modifyConfig` applied)
-   `context.nextVersion`: Version of Next.js being used
-   `context.buildId`: Unique identifier for the current build

Was this helpful?
