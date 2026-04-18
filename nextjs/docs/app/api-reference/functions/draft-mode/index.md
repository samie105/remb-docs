---
title: "draftMode"
source: "https://nextjs.org/docs/app/api-reference/functions/draft-mode"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/draft-mode"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:25.220Z"
content_hash: "7493d3a8211ee57bc09642c808194eefc0cd19dcd64d78f4cf8ef31a5cd3e4fc"
menu_path: ["draftMode"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/cookies/index.md", "title": "cookies"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/fetch/index.md", "title": "fetch"}
---

# draftMode

Last updated April 15, 2026

`draftMode` is an **async** function allows you to enable and disable [Draft Mode](/docs/app/guides/draft-mode), as well as check if Draft Mode is enabled in a [Server Component](/docs/app/getting-started/server-and-client-components).

app/page.ts

TypeScript

JavaScriptTypeScript

```
import { draftMode } from 'next/headers'
 
export default async function Page() {
  const { isEnabled } = await draftMode()
}
```

## Reference[](#reference)

The following methods and properties are available:

Method

Description

`isEnabled`

A boolean value that indicates if Draft Mode is enabled.

`enable()`

Enables Draft Mode in a Route Handler by setting a cookie (`__prerender_bypass`).

`disable()`

Disables Draft Mode in a Route Handler by deleting a cookie.

## Good to know[](#good-to-know)

*   `draftMode` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
    *   In version 14 and earlier, `draftMode` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
*   A new bypass cookie value will be generated each time you run `next build`. This ensures that the bypass cookie can’t be guessed.
*   To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.

## Examples[](#examples)

### Enabling Draft Mode[](#enabling-draft-mode)

To enable Draft Mode, create a new [Route Handler](/docs/app/api-reference/file-conventions/route) and call the `enable()` method:

app/draft/route.ts

TypeScript

JavaScriptTypeScript

```
import { draftMode } from 'next/headers'
 
export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

### Disabling Draft Mode[](#disabling-draft-mode)

By default, the Draft Mode session ends when the browser is closed.

To disable Draft Mode manually, call the `disable()` method in your [Route Handler](/docs/app/api-reference/file-conventions/route):

app/draft/route.ts

TypeScript

JavaScriptTypeScript

```
import { draftMode } from 'next/headers'
 
export async function GET(request: Request) {
  const draft = await draftMode()
  draft.disable()
  return new Response('Draft mode is disabled')
}
```

Then, send a request to invoke the Route Handler. If calling the route using the [`<Link>` component](/docs/app/api-reference/components/link), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.

### Checking if Draft Mode is enabled[](#checking-if-draft-mode-is-enabled)

You can check if Draft Mode is enabled in a Server Component with the `isEnabled` property:

app/page.ts

TypeScript

JavaScriptTypeScript

```
import { draftMode } from 'next/headers'
 
export default async function Page() {
  const { isEnabled } = await draftMode()
  return (
    <main>
      <h1>My Blog Post</h1>
      <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
    </main>
  )
}
```

## Version History[](#version-history)

Version

Changes

`v15.0.0-RC`

`draftMode` is now an async function. A [codemod](/docs/app/guides/upgrading/codemods#150) is available.

`v13.4.0`

`draftMode` introduced.

## Next Steps

Learn how to use Draft Mode with this step-by-step guide.

[

### Draft Mode

Next.js has draft mode to toggle between static and dynamic pages. You can learn how it works with App Router here.

](/docs/app/guides/draft-mode)

[Previous

cookies

](/docs/app/api-reference/functions/cookies)

[Next

fetch

](/docs/app/api-reference/functions/fetch)

Was this helpful?

supported.

Send


