---
title: "adapterPath"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:06:48.244Z"
content_hash: "8f6a70e20f3ff278ec23d1c5163dc21025da1111a76bda025d9c787ad0c497bf"
menu_path: ["adapterPath"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/index.md", "title": "next.config.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/allowedDevOrigins/index.md", "title": "allowedDevOrigins"}
---

# adapterPath

Last updated April 15, 2026

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

## Creating an Adapter[](#creating-an-adapter)

See [Creating an Adapter](/docs/app/api-reference/adapters/creating-an-adapter).

## API Reference[](#api-reference)

See [API Reference](/docs/app/api-reference/adapters/api-reference).

## Testing Adapters[](#testing-adapters)

See [Testing Adapters](/docs/app/api-reference/adapters/testing-adapters).

## Routing with `@next/routing`[](#routing-with-nextrouting)

See [Routing with `@next/routing`](/docs/app/api-reference/adapters/routing-with-next-routing).

## Implementing PPR in an Adapter[](#implementing-ppr-in-an-adapter)

See [Implementing PPR in an Adapter](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter).

## Runtime Integration[](#runtime-integration)

See [Runtime Integration](/docs/app/api-reference/adapters/runtime-integration).

## Invoking Entrypoints[](#invoking-entrypoints)

See [Invoking Entrypoints](/docs/app/api-reference/adapters/invoking-entrypoints).

## Output Types[](#output-types)

See [Output Types](/docs/app/api-reference/adapters/output-types).

## Routing Information[](#routing-information)

See [Routing Information](/docs/app/api-reference/adapters/routing-information).

## Use Cases[](#use-cases)

See [Use Cases](/docs/app/api-reference/adapters/use-cases).

[Previous

next.config.js

](/docs/app/api-reference/config/next-config-js)

[Next

allowedDevOrigins

](/docs/app/api-reference/config/next-config-js/allowedDevOrigins)

Was this helpful?

supported.

Send




