---
title: "unauthorized.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:44.399Z"
content_hash: "6f4afa219c2ff930f26b83ca120664fe4e38bb9eb6b4bbdc879411354c93dec0"
menu_path: ["unauthorized.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../template/index.md", "title": "template.js"}
nav_next: {"path": "../metadata/index.md", "title": "Metadata Files API Reference"}
---

# unauthorized.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The **unauthorized** file is used to render UI when the [`unauthorized`](/docs/app/api-reference/functions/unauthorized) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `401` status code.

app/unauthorized.tsx

JavaScriptTypeScript

```
import Login from '@/app/components/Login'
 
export default function Unauthorized() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

## Reference[](#reference)

### Props[](#props)

`unauthorized.js` components do not accept any props.

## Examples[](#examples)

### Displaying login UI to unauthenticated users[](#displaying-login-ui-to-unauthenticated-users)

You can use [`unauthorized`](/docs/app/api-reference/functions/unauthorized) function to render the `unauthorized.js` file with a login UI.

app/dashboard/page.tsx

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
 
export default async function DashboardPage() {
  const session = await verifySession()
 
  if (!session) {
    unauthorized()
  }
 
  return <div>Dashboard</div>
}
```

app/unauthorized.tsx

JavaScriptTypeScript

```
import Login from '@/app/components/Login'
 
export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `unauthorized.js` introduced. |

[

### unauthorized

API Reference for the unauthorized function.

](/docs/app/api-reference/functions/unauthorized)

Was this helpful?
