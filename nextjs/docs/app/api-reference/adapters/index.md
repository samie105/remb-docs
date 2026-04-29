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
nav_prev: {"path": "nextjs/docs/app/api-reference/cli/next/index.md", "title": "next CLI"}
nav_next: {"path": "nextjs/docs/app/api-reference/adapters/configuration/index.md", "title": "Configuration"}
---

# Adapters

Last updated April 23, 2026

Use this section to build and validate deployment adapters that integrate with the Next.js build and runtime model.

-   [Configuration](configuration/index.md)
-   [Creating an Adapter](creating-an-adapter/index.md)
-   [API Reference](api-reference/index.md)
-   [Testing Adapters](testing-adapters/index.md)
-   [Routing with `@next/routing`](routing-with-next-routing/index.md)
-   [Implementing PPR in an Adapter](implementing-ppr-in-an-adapter/index.md)
-   [Runtime Integration](runtime-integration/index.md)
-   [Invoking Entrypoints](invoking-entrypoints/index.md)
-   [Output Types](output-types/index.md)
-   [Routing Information](routing-information/index.md)
-   [Use Cases](use-cases/index.md)

[

### Configuration

Configure \`adapterPath\` or \`NEXT\_ADAPTER\_PATH\` to use a custom deployment adapter.

](configuration/index.md)[

### Creating an Adapter

Create an adapter module that implements the \`NextAdapter\` interface.

](creating-an-adapter/index.md)[

### API Reference

Reference for \`modifyConfig\` and \`onBuildComplete\` in the \`NextAdapter\` interface.

](api-reference/index.md)[

### Testing Adapters

Validate adapters with the Next.js compatibility test harness and custom lifecycle scripts.

](testing-adapters/index.md)[

### Routing with @next/routing

Use \`@next/routing\` to apply Next.js route matching behavior in adapters.

](routing-with-next-routing/index.md)[

### Implementing PPR in an Adapter

Implement Partial Prerendering support in an adapter using fallback output and cache hooks.

](implementing-ppr-in-an-adapter/index.md)[

### Runtime Integration

Understand how build-time adapters and runtime cache interfaces work together.

](runtime-integration/index.md)[

### Invoking Entrypoints

Invoke Node.js and Edge build entrypoints with adapter runtime context.

](invoking-entrypoints/index.md)[

### Output Types

Reference for all build output types exposed to adapters.

](output-types/index.md)[

### Routing Information

Reference for routing phases and route fields exposed in \`onBuildComplete\`.

](routing-information/index.md)[

### Use Cases

Common patterns and examples for deployment adapter implementations.

](use-cases/index.md)

Was this helpful?
