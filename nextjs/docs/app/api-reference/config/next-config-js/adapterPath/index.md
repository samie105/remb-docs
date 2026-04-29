---
title: "adapterPath"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:40.594Z"
content_hash: "c985dbd0a43b4c81b553c68f2a437047d48902c96d8a74d957ef2476727ef71e"
menu_path: ["adapterPath"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/index.md", "title": "next.config.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/allowedDevOrigins/index.md", "title": "allowedDevOrigins"}
---

# adapterPath

Last updated April 23, 2026

Next.js provides a built-in adapters API. It allows deployment platforms or build systems to integrate with the Next.js build process.

For a full reference implementation, see the [`nextjs/adapter-vercel`](https://github.com/nextjs/adapter-vercel) adapter.

## Configuration[](#configuration)

To use an adapter, specify the path to your adapter module in `adapterPath`:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  adapterPath: require.resolve('./my-adapter.js'),
}
 
module.exports = nextConfig
```

Alternatively `NEXT_ADAPTER_PATH` can be set to enable zero-config usage in deployment platforms.

## Adapters[](#adapters)

For full adapter implementation details, use the dedicated Adapters section:

-   [Configuration](../../../adapters/configuration/index.md)
-   [Creating an Adapter](../../../adapters/creating-an-adapter/index.md)
-   [API Reference](../../../adapters/api-reference/index.md)
-   [Testing Adapters](../../../adapters/testing-adapters/index.md)
-   [Routing with `@next/routing`](../../../adapters/routing-with-next-routing/index.md)
-   [Implementing PPR in an Adapter](../../../adapters/implementing-ppr-in-an-adapter/index.md)
-   [Runtime Integration](../../../adapters/runtime-integration/index.md)
-   [Invoking Entrypoints](../../../adapters/invoking-entrypoints/index.md)
-   [Output Types](../../../adapters/output-types/index.md)
-   [Routing Information](../../../adapters/routing-information/index.md)
-   [Use Cases](../../../adapters/use-cases/index.md)

## Creating an Adapter[](#creating-an-adapter)

See [Creating an Adapter](../../../adapters/creating-an-adapter/index.md).

## API Reference[](#api-reference)

See [API Reference](../../../adapters/api-reference/index.md).

## Testing Adapters[](#testing-adapters)

See [Testing Adapters](../../../adapters/testing-adapters/index.md).

## Routing with `@next/routing`[](#routing-with-nextrouting)

See [Routing with `@next/routing`](../../../adapters/routing-with-next-routing/index.md).

## Implementing PPR in an Adapter[](#implementing-ppr-in-an-adapter)

See [Implementing PPR in an Adapter](../../../adapters/implementing-ppr-in-an-adapter/index.md).

## Runtime Integration[](#runtime-integration)

See [Runtime Integration](../../../adapters/runtime-integration/index.md).

## Invoking Entrypoints[](#invoking-entrypoints)

See [Invoking Entrypoints](../../../adapters/invoking-entrypoints/index.md).

## Output Types[](#output-types)

See [Output Types](../../../adapters/output-types/index.md).

## Routing Information[](#routing-information)

See [Routing Information](../../../adapters/routing-information/index.md).

## Use Cases[](#use-cases)

See [Use Cases](../../../adapters/use-cases/index.md).

Was this helpful?
