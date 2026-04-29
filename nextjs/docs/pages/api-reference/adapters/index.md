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
nav_prev: {"path": "nextjs/docs/pages/api-reference/cli/next/index.md", "title": "next CLI"}
nav_next: {"path": "nextjs/docs/pages/api-reference/adapters/configuration/index.md", "title": "Configuration"}
---

# Adapters

Last updated April 23, 2026

Use this section to build and validate deployment adapters that integrate with the Next.js build and runtime model.

-   [Configuration](../../../app/api-reference/adapters/configuration/index.md)
-   [Creating an Adapter](../../../app/api-reference/adapters/creating-an-adapter/index.md)
-   [API Reference](../../../app/api-reference/adapters/api-reference/index.md)
-   [Testing Adapters](../../../app/api-reference/adapters/testing-adapters/index.md)
-   [Routing with `@next/routing`](../../../app/api-reference/adapters/routing-with-next-routing/index.md)
-   [Implementing PPR in an Adapter](../../../app/api-reference/adapters/implementing-ppr-in-an-adapter/index.md)
-   [Runtime Integration](../../../app/api-reference/adapters/runtime-integration/index.md)
-   [Invoking Entrypoints](../../../app/api-reference/adapters/invoking-entrypoints/index.md)
-   [Output Types](../../../app/api-reference/adapters/output-types/index.md)
-   [Routing Information](../../../app/api-reference/adapters/routing-information/index.md)
-   [Use Cases](../../../app/api-reference/adapters/use-cases/index.md)

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
