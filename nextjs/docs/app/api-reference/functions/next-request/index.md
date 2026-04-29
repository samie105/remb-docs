---
title: "NextRequest"
source: "https://nextjs.org/docs/app/api-reference/functions/next-request"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/next-request"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:37.696Z"
content_hash: "1781dbc67ec829d555912ed4066e72711e75b179b8154b61f9529bc74578a453"
menu_path: ["NextRequest"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../image-response/index.md", "title": "ImageResponse"}
nav_next: {"path": "../next-response/index.md", "title": "NextResponse"}
---

# NextRequest

Last updated April 23, 2026

NextRequest extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional convenience methods.

## `cookies`[](#cookies)

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the request.

### `set(name, value)`[](#setname-value)

Given a name, set a cookie with the given value on the request.

```
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a `Set-Cookie:show-banner=false;path=/home` header
request.cookies.set('show-banner', 'false')
```

### `get(name)`[](#getname)

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```
// Given incoming request /home
// { name: 'show-banner', value: 'false', Path: '/home' }
request.cookies.get('show-banner')
```

### `getAll()`[](#getall)

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.

```
// Given incoming request /home
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
```

### `delete(name)`[](#deletename)

Given a cookie name, delete the cookie from the request.

```
// Returns true for deleted, false is nothing is deleted
request.cookies.delete('experiments')
```

### `has(name)`[](#hasname)

Given a cookie name, return `true` if the cookie exists on the request.

```
// Returns true if cookie exists, false if it does not
request.cookies.has('experiments')
```

### `clear()`[](#clear)

Remove all cookies from the request.

```
request.cookies.clear()
```

## `nextUrl`[](#nexturl)

Extends the native [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API with additional convenience methods, including Next.js specific properties.

```
// Given a request to /home, pathname is /home
request.nextUrl.pathname
// Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
request.nextUrl.searchParams
```

The following options are available:

| Property | Type | Description |
| --- | --- | --- |
| `basePath` | `string` | The [base path](/docs/app/api-reference/config/next-config-js/basePath) of the URL. |
| `buildId` | `string` | `undefined` | The build identifier of the Next.js application. Can be [customized](/docs/app/api-reference/config/next-config-js/generateBuildId). |
| `pathname` | `string` | The pathname of the URL. |
| `searchParams` | `Object` | The search parameters of the URL. |

> **Note:** The internationalization properties from the Pages Router are not available for usage in the App Router. Learn more about [internationalization with the App Router](/docs/app/guides/internationalization).

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.0.0` | `ip` and `geo` removed. |

Was this helpful?
