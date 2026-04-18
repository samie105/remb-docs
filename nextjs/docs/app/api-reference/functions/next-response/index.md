---
title: "NextResponse"
source: "https://nextjs.org/docs/app/api-reference/functions/next-response"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/next-response"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:55.371Z"
content_hash: "763380b1704626c42798d6ec99e538f9e3851b2b73f7f03135721eae49c4984c"
menu_path: ["NextResponse"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/next-request/index.md", "title": "NextRequest"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/not-found/index.md", "title": "notFound"}
---

# NextResponse

Last updated April 15, 2026

NextResponse extends the [Web Response API](https://developer.mozilla.org/docs/Web/API/Response) with additional convenience methods.

## `cookies`[](#cookies)

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the response.

### `set(name, value)`[](#setname-value)

Given a name, set a cookie with the given value on the response.

```
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner', 'false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

### `get(name)`[](#getname)

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

### `getAll()`[](#getall)

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.

```
// Given incoming request /home
let response = NextResponse.next()
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

### `has(name)`[](#hasname)

Given a cookie name, return `true` if the cookie exists on the response.

```
// Given incoming request /home
let response = NextResponse.next()
// Returns true if cookie exists, false if it does not
response.cookies.has('experiments')
```

### `delete(name)`[](#deletename)

Given a cookie name, delete the cookie from the response.

```
// Given incoming request /home
let response = NextResponse.next()
// Returns true for deleted, false if nothing is deleted
response.cookies.delete('experiments')
```

## `json()`[](#json)

Produce a response with the given JSON body.

app/api/route.ts

TypeScript

JavaScriptTypeScript

```
import { NextResponse } from 'next/server'
 
export async function GET(request: Request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```

## `redirect()`[](#redirect)

Produce a response that redirects to a [URL](https://developer.mozilla.org/docs/Web/API/URL).

```
import { NextResponse } from 'next/server'
 
return NextResponse.redirect(new URL('/new', request.url))
```

The [URL](https://developer.mozilla.org/docs/Web/API/URL) can be created and modified before being used in the `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.

```
import { NextResponse } from 'next/server'
 
// Given an incoming request...
const loginUrl = new URL('/login', request.url)
// Add ?from=/incoming-url to the /login URL
loginUrl.searchParams.set('from', request.nextUrl.pathname)
// And redirect to the new URL
return NextResponse.redirect(loginUrl)
```

## `rewrite()`[](#rewrite)

Produce a response that rewrites (proxies) the given [URL](https://developer.mozilla.org/docs/Web/API/URL) while preserving the original URL.

```
import { NextResponse } from 'next/server'
 
// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
return NextResponse.rewrite(new URL('/proxy', request.url))
```

## `next()`[](#next)

The `next()` method is useful for Proxy, as it allows you to return early and continue routing.

```
import { NextResponse } from 'next/server'
 
return NextResponse.next()
```

You can also forward `headers` upstream when producing the response, using `NextResponse.next({ request: { headers } })`:

```
import { NextResponse } from 'next/server'
 
// Given an incoming request...
const newHeaders = new Headers(request.headers)
// Add a new header
newHeaders.set('x-version', '123')
// Forward the modified request headers upstream
return NextResponse.next({
  request: {
    // New request headers
    headers: newHeaders,
  },
})
```

This forwards `newHeaders` upstream to the target page, route, or server action, and does not expose them to the client. While this pattern is useful for passing data upstream, it should be used with caution because the headers containing this data may be forwarded to external services.

In contrast, `NextResponse.next({ headers })` is a shorthand for sending headers from proxy to the client. This is **NOT** good practice and should be avoided. Among other reasons because setting response headers like `Content-Type`, can override framework expectations (for example, the `Content-Type` used by Server Actions), leading to failed submissions or broken streaming responses.

```
import { type NextRequest, NextResponse } from 'next/server'
 
async function proxy(request: NextRequest) {
  const headers = await injectAuth(request.headers)
  // DO NOT forward headers like this
  return NextResponse.next({ headers })
}
```

In general, avoid copying all incoming request headers because doing so can leak sensitive data to clients or upstream services.

Prefer a defensive approach by creating a subset of incoming request headers using an allow-list. For example, you might discard custom `x-*` headers and only forward known-safe headers:

```
import { type NextRequest, NextResponse } from 'next/server'
 
function proxy(request: NextRequest) {
  const incoming = new Headers(request.headers)
  const forwarded = new Headers()
 
  for (const [name, value] of incoming) {
    const headerName = name.toLowerCase()
    // Keep only known-safe headers, discard custom x-* and other sensitive ones
    if (
      !headerName.startsWith('x-') &&
      headerName !== 'authorization' &&
      headerName !== 'cookie'
    ) {
      // Preserve original header name casing
      forwarded.set(name, value)
    }
  }
 
  return NextResponse.next({
    request: {
      headers: forwarded,
    },
  })
}
```

[Previous

NextRequest

](/docs/app/api-reference/functions/next-request)

[Next

notFound

](/docs/app/api-reference/functions/not-found)

Was this helpful?

supported.

Send
