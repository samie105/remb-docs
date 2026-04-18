---
title: "Adapters"
source: "https://nextjs.org/docs/app/api-reference/adapters"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:05:34.414Z"
content_hash: "48afc282169a9810a6e3ccc310302117643614eff390d10d9676258541eb8540"
menu_path: ["Adapters"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/cli/next/index.md", "title": "next CLI"}
nav_next: {"path": "nextjs/docs/app/api-reference/adapters/configuration/index.md", "title": "Configuration"}
---

# Adapters

Last updated April 15, 2026

Use this section to build and validate deployment adapters that integrate with the Next.js build and runtime model.

*   [Configuration](/docs/app/api-reference/adapters/configuration)
*   [Creating an Adapter](/docs/app/api-reference/adapters/creating-an-adapter)
*   [API Reference](/docs/app/api-reference/adapters/api-reference)
*   [Testing Adapters](/docs/app/api-reference/adapters/testing-adapters)
*   [Routing with `@next/routing`](/docs/app/api-reference/adapters/routing-with-next-routing)
*   [Implementing PPR in an Adapter](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)
*   [Runtime Integration](/docs/app/api-reference/adapters/runtime-integration)
*   [Invoking Entrypoints](/docs/app/api-reference/adapters/invoking-entrypoints)
*   [Output Types](/docs/app/api-reference/adapters/output-types)
*   [Routing Information](/docs/app/api-reference/adapters/routing-information)
*   [Use Cases](/docs/app/api-reference/adapters/use-cases)

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

[Previous

next CLI

](/docs/app/api-reference/cli/next)

[Next

Configuration

](/docs/app/api-reference/adapters/configuration)

Was this helpful?

supported.

Send




