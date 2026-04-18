---
title: "permanentRedirect"
source: "https://nextjs.org/docs/app/api-reference/functions/permanentRedirect"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/permanentRedirect"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:12:00.798Z"
content_hash: "55c4778b3f9c5217e42b949ddf9ba1284bc6e368eef185cfb07b87e4102c8bb8"
menu_path: ["permanentRedirect"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/not-found/index.md", "title": "notFound"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/redirect/index.md", "title": "redirect"}
---

# permanentRedirect

Last updated April 15, 2026

The `permanentRedirect` function allows you to redirect the user to another URL. `permanentRedirect` can be used in Server Components, Client Components, [Route Handlers](/docs/app/api-reference/file-conventions/route), and [Server Functions](/docs/app/getting-started/mutating-data).

When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](/docs/app/api-reference/functions/not-found) instead.

> **Good to know**: If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the [`redirect` function](/docs/app/api-reference/functions/redirect) instead.

## Parameters[](#parameters)

The `permanentRedirect` function accepts two arguments:

```
permanentRedirect(path, type)
```

Parameter

Type

Description

`path`

`string`

The URL to redirect to. Can be a relative or absolute path.

`type`

`'replace'` (default) or `'push'` (default in Server Actions)

The type of redirect to perform.

By default, `permanentRedirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](/docs/app/getting-started/mutating-data) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `RedirectType` object contains the available options for the `type` parameter.

```
import { permanentRedirect, RedirectType } from 'next/navigation'
 
permanentRedirect('/redirect-to', RedirectType.replace)
// or
permanentRedirect('/redirect-to', RedirectType.push)
```

The `type` parameter has no effect when used in Server Components.

## Returns[](#returns)

`permanentRedirect` does not return a value.

## Example[](#example)

Invoking the `permanentRedirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

app/team/\[id\]/page.js

```
import { permanentRedirect } from 'next/navigation'
 
async function fetchTeam(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({ params }) {
  const { id } = await params
  const team = await fetchTeam(id)
  if (!team) {
    permanentRedirect('/login')
  }
 
  // ...
}
```

> **Good to know**: `permanentRedirect` does not require you to use `return permanentRedirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

[

### redirect

API Reference for the redirect function.

](/docs/app/api-reference/functions/redirect)

[Previous

notFound

](/docs/app/api-reference/functions/not-found)

[Next

redirect

](/docs/app/api-reference/functions/redirect)

Was this helpful?

supported.

Send




