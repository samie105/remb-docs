---
title: "headers"
source: "https://nextjs.org/docs/app/api-reference/functions/headers"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/headers"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:48.045Z"
content_hash: "dcdbd479e928826b3c9a9306314cad2e30399afbdfa6563c6b1f165ba412a6f7"
menu_path: ["headers"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/generate-viewport/index.md", "title": "generateViewport"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/image-response/index.md", "title": "ImageResponse"}
---

# headers

Last updated April 15, 2026

`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a [Server Component](/docs/app/getting-started/server-and-client-components).

app/page.tsx

TypeScript

JavaScriptTypeScript

```
import { headers } from 'next/headers'
 
export default async function Page() {
  const headersList = await headers()
  const userAgent = headersList.get('user-agent')
}
```

## Reference[](#reference)

### Parameters[](#parameters)

`headers` does not take any parameters.

### Returns[](#returns)

`headers` returns a **read-only** [Web Headers](https://developer.mozilla.org/docs/Web/API/Headers) object.

*   [`Headers.entries()`](https://developer.mozilla.org/docs/Web/API/Headers/entries): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing to go through all key/value pairs contained in this object.
*   [`Headers.forEach()`](https://developer.mozilla.org/docs/Web/API/Headers/forEach): Executes a provided function once for each key/value pair in this `Headers` object.
*   [`Headers.get()`](https://developer.mozilla.org/docs/Web/API/Headers/get): Returns a [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) sequence of all the values of a header within a `Headers` object with a given name.
*   [`Headers.has()`](https://developer.mozilla.org/docs/Web/API/Headers/has): Returns a boolean stating whether a `Headers` object contains a certain header.
*   [`Headers.keys()`](https://developer.mozilla.org/docs/Web/API/Headers/keys): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all keys of the key/value pairs contained in this object.
*   [`Headers.values()`](https://developer.mozilla.org/docs/Web/API/Headers/values): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all values of the key/value pairs contained in this object.

## Good to know[](#good-to-know)

*   `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
    *   In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
*   Since `headers` is read-only, you cannot `set` or `delete` the outgoing request headers.
*   `headers` is a [Request-time API](/docs/app/glossary#request-time-apis) whose returned values cannot be known ahead of time. Using it in will opt a route into **[dynamic rendering](/docs/app/glossary#dynamic-rendering)**.

## Examples[](#examples)

### Using the Authorization header[](#using-the-authorization-header)

app/page.js

```
import { headers } from 'next/headers'
 
export default async function Page() {
  const authorization = (await headers()).get('authorization')
  const res = await fetch('...', {
    headers: { authorization }, // Forward the authorization header
  })
  const user = await res.json()
 
  return <h1>{user.name}</h1>
}
```

## Version History[](#version-history)

Version

Changes

`v15.0.0-RC`

`headers` is now an async function. A [codemod](/docs/app/guides/upgrading/codemods#150) is available.

`v13.0.0`

`headers` introduced.

[Previous

generateViewport

](/docs/app/api-reference/functions/generate-viewport)

[Next

ImageResponse

](/docs/app/api-reference/functions/image-response)

Was this helpful?

supported.

Send




