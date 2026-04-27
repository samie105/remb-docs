---
title: "Adapters"
source: "https://nextjs.org/docs/app/api-reference/adapters"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:04:27.397Z"
content_hash: "9a35856f59bb5f469fdcef4a3a0cde714b196a6b81da43325fcec9e1fe86bf7e"
menu_path: ["Adapters"]
section_path: []
version: "latest"
content_language: "en"
---
[App Router](/docs/app)[API Reference](/docs/app/api-reference)Adapters

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

](/docs/app/api-reference/adapters/configuration)[

### Creating an Adapter

Create an adapter module that implements the \`NextAdapter\` interface.

](/docs/app/api-reference/adapters/creating-an-adapter)[

### API Reference

Reference for \`modifyConfig\` and \`onBuildComplete\` in the \`NextAdapter\` interface.

](/docs/app/api-reference/adapters/api-reference)[

### Testing Adapters

Validate adapters with the Next.js compatibility test harness and custom lifecycle scripts.

](/docs/app/api-reference/adapters/testing-adapters)[

### Routing with @next/routing

Use \`@next/routing\` to apply Next.js route matching behavior in adapters.

](/docs/app/api-reference/adapters/routing-with-next-routing)[

### Implementing PPR in an Adapter

Implement Partial Prerendering support in an adapter using fallback output and cache hooks.

](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)[

### Runtime Integration

Understand how build-time adapters and runtime cache interfaces work together.

](/docs/app/api-reference/adapters/runtime-integration)[

### Invoking Entrypoints

Invoke Node.js and Edge build entrypoints with adapter runtime context.

](/docs/app/api-reference/adapters/invoking-entrypoints)[

### Output Types

Reference for all build output types exposed to adapters.

](/docs/app/api-reference/adapters/output-types)[

### Routing Information

Reference for routing phases and route fields exposed in \`onBuildComplete\`.

](/docs/app/api-reference/adapters/routing-information)[

### Use Cases

Common patterns and examples for deployment adapter implementations.

](/docs/app/api-reference/adapters/use-cases)

Was this helpful?
