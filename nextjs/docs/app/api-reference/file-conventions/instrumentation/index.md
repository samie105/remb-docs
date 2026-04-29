---
title: "instrumentation.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:38.248Z"
content_hash: "777eb7a76bf7666a59cc6fe5bee73813142a25a324773ab10bcac54adc3edebb"
menu_path: ["instrumentation.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/forbidden/index.md", "title": "forbidden.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/instrumentation-client/index.md", "title": "instrumentation-client.js"}
---

# instrumentation.js

Last updated April 23, 2026

The `instrumentation.js|ts` file is used to integrate observability tools into your application, allowing you to track the performance and behavior, and to debug issues in production.

To use it, place the file in the **root** of your application or inside a [`src` folder](../src-folder/index.md) if using one.

## Exports[](#exports)

### `register` (optional)[](#register-optional)

The file exports a `register` function that is called **once** when a new Next.js server instance is initiated, and must complete before the server is ready to handle requests. `register` can be an async function.

instrumentation.ts

JavaScriptTypeScript

```
import { registerOTel } from '@vercel/otel'
 
export function register() {
  registerOTel('next-app')
}
```

### `onRequestError` (optional)[](#onrequesterror-optional)

You can optionally export an `onRequestError` function to track **server** errors to any custom observability provider.

-   If you're running any async tasks in `onRequestError`, make sure they're awaited. `onRequestError` will be triggered when the Next.js server captures the error.
-   The `error` instance might not be the original error instance thrown, as it may be processed by React if encountered during Server Components rendering. If this happens, you can use `digest` property on an error to identify the actual error type.

instrumentation.ts

JavaScriptTypeScript

```
import { type Instrumentation } from 'next'
 
export const onRequestError: Instrumentation.onRequestError = async (
  err,
  request,
  context
) => {
  await fetch('https://.../report-error', {
    method: 'POST',
    body: JSON.stringify({
      message: err.message,
      request,
      context,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
}
```

#### Parameters[](#parameters)

The function accepts three parameters: `error`, `request`, and `context`.

Types

```
export function onRequestError(
  error: { digest: string } & Error,
  request: {
    path: string // resource path, e.g. /blog?name=foo
    method: string // request method. e.g. GET, POST, etc
    headers: { [key: string]: string | string[] }
  },
  context: {
    routerKind: 'Pages Router' | 'App Router' // the router type
    routePath: string // the route file path, e.g. /app/blog/[dynamic]
    routeType: 'render' | 'route' | 'action' | 'proxy' // the context in which the error occurred
    renderSource:
      | 'react-server-components'
      | 'react-server-components-payload'
      | 'server-rendering'
    revalidateReason: 'on-demand' | 'stale' | undefined // undefined is a normal request without revalidation
    renderType: 'dynamic' | 'dynamic-resume' // 'dynamic-resume' for PPR
  }
): void | Promise<void>
```

-   `error`: The caught error itself (type is always `Error`), and a `digest` property which is the unique ID of the error.
-   `request`: Read-only request information associated with the error.
-   `context`: The context in which the error occurred. This can be the type of router (App or Pages Router), and/or (Server Components (`'render'`), Route Handlers (`'route'`), Server Actions (`'action'`), or Proxy (`'proxy'`)).

### Specifying the runtime[](#specifying-the-runtime)

The `instrumentation.js` file works in both the Node.js and Edge runtime, however, you can use `process.env.NEXT_RUNTIME` to target a specific runtime.

instrumentation.js

```
export function register() {
  if (process.env.NEXT_RUNTIME === 'edge') {
    return require('./register.edge')
  } else {
    return require('./register.node')
  }
}
 
export function onRequestError() {
  if (process.env.NEXT_RUNTIME === 'edge') {
    return require('./on-request-error.edge')
  } else {
    return require('./on-request-error.node')
  }
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `onRequestError` introduced, `instrumentation` stable |
| `v14.0.4` | Turbopack support for `instrumentation` |
| `v13.2.0` | `instrumentation` introduced as an experimental feature |

## Learn more about Instrumentation

[

### Instrumentation

Learn how to use instrumentation to run code at server startup in your Next.js app

](../../../guides/instrumentation/index.md)

Was this helpful?
