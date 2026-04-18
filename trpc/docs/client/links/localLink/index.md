---
title: "Local Link"
source: "https://trpc.io/docs/client/links/localLink"
canonical_url: "https://trpc.io/docs/client/links/localLink"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:09.244Z"
content_hash: "f20b085613e33efe674a63c028e94a66266ba3cf00a38747ada07ab915e4d360"
menu_path: ["Local Link"]
section_path: []
nav_prev: {"path": "trpc/docs/client/links/httpSubscriptionLink/index.md", "title": "HTTP Subscription Link"}
nav_next: {"path": "trpc/docs/client/links/loggerLink/index.md", "title": "Logger Link"}
---

`localLink` is a [**terminating link**](trpc/docs/client/links/index.md#the-terminating-link) that allows you to make tRPC procedure calls directly in your application without going through HTTP.

info

We have prefixed this as `unstable_` as it's a new API, but you're safe to use it! [Read more](trpc/docs/faq/index.md#unstable).

## Usage[​](#usage "Direct link to Usage")

tsx

`import { createTRPCClient, unstable_localLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`import { appRouter } from './server';`

`const client = createTRPCClient<AppRouter>({`

  `links: [`

    `unstable_localLink({`

      `router: appRouter,`

      `createContext: async () => {`

        `// Create your context here`

        `return {};`

      `},`

      `onError: (opts) => {`

        `// Log errors here, similarly to how you would in an API route`

        `console.error('Error:', opts.error);`

      `},`

    `}),`

  `],`

`});`

## Features[​](#features "Direct link to Features")

*   Direct procedure calls without HTTP overhead
*   Full support for queries, mutations, and subscriptions
*   Automatic error handling and transformation
*   Support for abort signals
*   Type-safe context creation

## Options[​](#options "Direct link to Options")

The `localLink` accepts the following options:

ts

`type LocalLinkOptions<TRouter extends AnyRouter> = {`

  `router: TRouter;`

  `createContext: () => Promise<inferRouterContext<TRouter>>;`

  `onError?: (opts: ErrorHandlerOptions<inferRouterContext<TRouter>>) => void;`

`} & TransformerOptions<inferClientTypes<TRouter>>;`

### router[​](#router "Direct link to router")

The tRPC router instance to use for procedure calls.

### createContext[​](#createcontext "Direct link to createContext")

A function that creates the context for each procedure call. This is called for each request and should return a promise that resolves to the context object.

### onError[​](#onerror "Direct link to onError")

An optional error handler that is called when an error occurs during a procedure call. It receives the error, operation type, path, input, and context.

### transformer[​](#transformer "Direct link to transformer")

Optional input/output transformers for serialization/deserialization of data.

## Notes[​](#notes "Direct link to Notes")

*   It's recommended to use this link in scenarios where you need direct procedure calls without HTTP
*   For most client-side applications, you should use the `httpLink` or other HTTP-based links instead
*   The link supports all tRPC features including queries, mutations, and subscriptions
*   Error handling and transformation are handled automatically, just like with HTTP-based links

