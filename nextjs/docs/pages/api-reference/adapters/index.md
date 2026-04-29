---
title: "Adapters"
source: "https://nextjs.org/docs/pages/api-reference/adapters"
canonical_url: "https://nextjs.org/docs/pages/api-reference/adapters"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:18:19.042Z"
content_hash: "98441b2a20a44ae3b9227d1b0e237de4fedd02054437189c7bfe5c4aa09b1312"
menu_path: ["Adapters"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../cli/next/index.md", "title": "next CLI"}
nav_next: {"path": "configuration/index.md", "title": "Configuration"}
---

# Adapters

Last updated April 23, 2026

Use this section to build and validate deployment adapters that integrate with the Next.js build and runtime model.

-   [Configuration](/docs/app/api-reference/adapters/configuration)
-   [Creating an Adapter](/docs/app/api-reference/adapters/creating-an-adapter)
-   [API Reference](/docs/app/api-reference/adapters/api-reference)
-   [Testing Adapters](/docs/app/api-reference/adapters/testing-adapters)
-   [Routing with `@next/routing`](/docs/app/api-reference/adapters/routing-with-next-routing)
-   [Implementing PPR in an Adapter](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)
-   [Runtime Integration](/docs/app/api-reference/adapters/runtime-integration)
-   [Invoking Entrypoints](/docs/app/api-reference/adapters/invoking-entrypoints)
-   [Output Types](/docs/app/api-reference/adapters/output-types)
-   [Routing Information](/docs/app/api-reference/adapters/routing-information)
-   [Use Cases](/docs/app/api-reference/adapters/use-cases)

[

### Configuration

Configure \`adapterPath\` or \`NEXT\_ADAPTER\_PATH\` to use a custom deployment adapter.

](/docs/pages/api-reference/adapters/configuration)[

### Creating an Adapter

Create an adapter module that implements the \`NextAdapter\` interface.

](/docs/pages/api-reference/adapters/creating-an-adapter)[

### API Reference

Reference for \`modifyConfig\` and \`onBuildComplete\` in the \`NextAdapter\` interface.

](/docs/pages/api-reference/adapters/api-reference)[

### Testing Adapters

Validate adapters with the Next.js compatibility test harness and custom lifecycle scripts.

](/docs/pages/api-reference/adapters/testing-adapters)[

### Routing with @next/routing

Use \`@next/routing\` to apply Next.js route matching behavior in adapters.

](/docs/pages/api-reference/adapters/routing-with-next-routing)[

### Implementing PPR in an Adapter

Implement Partial Prerendering support in an adapter using fallback output and cache hooks.

](/docs/pages/api-reference/adapters/implementing-ppr-in-an-adapter)[

### Runtime Integration

Understand how build-time adapters and runtime cache interfaces work together.

](/docs/pages/api-reference/adapters/runtime-integration)[

### Invoking Entrypoints

Invoke Node.js and Edge build entrypoints with adapter runtime context.

](/docs/pages/api-reference/adapters/invoking-entrypoints)[

### Output Types

Reference for all build output types exposed to adapters.

](/docs/pages/api-reference/adapters/output-types)[

### Routing Information

Reference for routing phases and route fields exposed in \`onBuildComplete\`.

](/docs/pages/api-reference/adapters/routing-information)[

### Use Cases

Common patterns and examples for deployment adapter implementations.

](/docs/pages/api-reference/adapters/use-cases)

Was this helpful?
