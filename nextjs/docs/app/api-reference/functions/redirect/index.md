---
title: "redirect"
source: "https://nextjs.org/docs/app/api-reference/functions/redirect"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/redirect"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:48.048Z"
content_hash: "3566b2e3c8b346066b1006136e23295bb4e942fbae61597a081f111f6bcb68fa"
menu_path: ["redirect"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/permanentRedirect/index.md", "title": "permanentRedirect"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/refresh/index.md", "title": "refresh"}
---

# redirect

Last updated April 23, 2026

The `redirect` function allows you to redirect the user to another URL. `redirect` can be used while rendering in [Server and Client Components](../../../getting-started/server-and-client-components/index.md), [Route Handlers](../../file-conventions/route/index.md), and [Server Functions](../../../getting-started/mutating-data/index.md).

When used in a [streaming context](../../../getting-started/linking-and-navigating/index.md#streaming), this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](../not-found/index.md) instead.

## Reference[](#reference)

### Parameters[](#parameters)

The `redirect` function accepts two arguments:

```
redirect(path, type)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | The URL to redirect to. Can be a relative or absolute path. |
| `type` | `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform. |

By default, `redirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](../../../getting-started/mutating-data/index.md) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `RedirectType` object contains the available options for the `type` parameter.

```
import { redirect, RedirectType } from 'next/navigation'
 
redirect('/redirect-to', RedirectType.replace)
// or
redirect('/redirect-to', RedirectType.push)
```

The `type` parameter has no effect when used in Server Components.

### Returns[](#returns)

`redirect` does not return a value.

## Behavior[](#behavior)

-   In Server Actions and Route Handlers, redirect should be called **outside** the `try` block when using `try/catch` statements.
-   If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the [`permanentRedirect` function](../permanentRedirect/index.md) instead.
-   `redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.
-   `redirect` can be called in Client Components during the rendering process but not in event handlers. You can use the [`useRouter` hook](../use-router/index.md) instead.
-   `redirect` also accepts absolute URLs and can be used to redirect to external links.
-   If you'd like to redirect before the render process, use [`next.config.js`](../../../guides/redirecting/index.md#redirects-in-nextconfigjs) or [Proxy](../../../guides/redirecting/index.md#nextresponseredirect-in-proxy).

## Example[](#example)

### Server Component[](#server-component)

Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

app/team/\[id\]/page.tsx

JavaScriptTypeScript

```
import { redirect } from 'next/navigation'
 
async function fetchTeam(id: string) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}
 
export default async function Profile({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const team = await fetchTeam(id)
 
  if (!team) {
    redirect('/login')
  }
 
  // ...
}
```

> **Good to know**: `redirect` does not require you to use `return redirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

### Client Component[](#client-component)

`redirect` can be directly used in a Client Component.

components/client-redirect.tsx

JavaScriptTypeScript

```
'use client'
 
import { redirect, usePathname } from 'next/navigation'
 
export function ClientRedirect() {
  const pathname = usePathname()
 
  if (pathname.startsWith('/admin') && !pathname.includes('/login')) {
    redirect('/admin/login')
  }
 
  return <div>Login Page</div>
}
```

> **Good to know**: When using `redirect` in a Client Component on initial page load during Server-Side Rendering (SSR), it will perform a server-side redirect.

`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the [`useRouter`](../use-router/index.md) hook.

app/client-redirect.tsx

JavaScriptTypeScript

```
'use client'
 
import { navigate } from './actions'
 
export function ClientRedirect() {
  return (
    <form action={navigate}>
      <input type="text" name="id" />
      <button>Submit</button>
    </form>
  )
}
```

app/actions.ts

JavaScriptTypeScript

```
'use server'
 
import { redirect } from 'next/navigation'
 
export async function navigate(data: FormData) {
  redirect(`/posts/${data.get('id')}`)
}
```

## FAQ[](#faq)

### Why does `redirect` use 307 and 308?[](#why-does-redirect-use-307-and-308)

When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.

Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.

The introduction of the `307` status code means that the request method is preserved as `POST`.

-   `302` - Temporary redirect, will change the request method from `POST` to `GET`
-   `307` - Temporary redirect, will preserve the request method as `POST`

The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will _always_ be preserved as `POST` requests.

[Learn more](https://developer.mozilla.org/docs/Web/HTTP/Redirections) about HTTP Redirects.

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.0.0` | `redirect` introduced. |

[

### permanentRedirect

API Reference for the permanentRedirect function.

](../permanentRedirect/index.md)

Was this helpful?
