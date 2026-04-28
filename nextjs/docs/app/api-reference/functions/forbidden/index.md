---
title: "forbidden"
source: "https://nextjs.org/docs/app/api-reference/functions/forbidden"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/forbidden"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:10:10.685Z"
content_hash: "31f547fa6c2e5bbd6ebc12b42785523de85465c79bb4137fc1f98d481b1bd43e"
menu_path: ["forbidden"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/fetch/index.md", "title": "fetch"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/generate-image-metadata/index.md", "title": "generateImageMetadata"}
---

# forbidden

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`forbidden.js` file](/docs/app/api-reference/file-conventions/forbidden).

To start using `forbidden`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

next.config.ts

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}
 
export default nextConfig
```

`forbidden` can be invoked in [Server Components](/docs/app/getting-started/server-and-client-components), [Server Functions](/docs/app/getting-started/mutating-data), and [Route Handlers](/docs/app/api-reference/file-conventions/route).

app/auth/page.tsx

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
 
export default async function AdminPage() {
  const session = await verifySession()
 
  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }
 
  // Render the admin page for authorized users
  return <></>
}
```

## Good to know[](#good-to-know)

-   The `forbidden` function cannot be called in the [root layout](/docs/app/api-reference/file-conventions/layout#root-layout).

## Examples[](#examples)

### Role-based route protection[](#role-based-route-protection)

You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

app/admin/page.tsx

JavaScriptTypeScript

```
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
 
export default async function AdminPage() {
  const session = await verifySession()
 
  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }
 
  // Render the admin page for authorized users
  return (
    <main>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </main>
  )
}
```

### Mutations with Server Actions[](#mutations-with-server-actions)

When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.

app/actions/update-role.ts

JavaScriptTypeScript

```
'use server'
 
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
import db from '@/app/lib/db'
 
export async function updateRole(formData: FormData) {
  const session = await verifySession()
 
  // Ensure only admins can update roles
  if (session.role !== 'admin') {
    forbidden()
  }
 
  // Perform the role update for authorized users
  // ...
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v15.1.0` | `forbidden` introduced. |

[

### forbidden.js

API reference for the forbidden.js special file.

](/docs/app/api-reference/file-conventions/forbidden)

Was this helpful?
