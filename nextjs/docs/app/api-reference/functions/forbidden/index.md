---
title: "forbidden"
source: "https://nextjs.org/docs/app/api-reference/functions/forbidden"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/forbidden"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:30.424Z"
content_hash: "e5efd40539149a3632baab29329eca6bb592c9a9aa0f2a1aa06b70807a218f5d"
menu_path: ["forbidden"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/fetch/index.md", "title": "fetch"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/generate-image-metadata/index.md", "title": "generateImageMetadata"}
---

# forbidden

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`forbidden.js` file](/docs/app/api-reference/file-conventions/forbidden).

To start using `forbidden`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:

next.config.ts

TypeScript

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

TypeScript

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

*   The `forbidden` function cannot be called in the [root layout](/docs/app/api-reference/file-conventions/layout#root-layout).

## Examples[](#examples)

### Role-based route protection[](#role-based-route-protection)

You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

app/admin/page.tsx

TypeScript

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

TypeScript

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

Version

Changes

`v15.1.0`

`forbidden` introduced.

[

### forbidden.js

API reference for the forbidden.js special file.

](/docs/app/api-reference/file-conventions/forbidden)

[Previous

fetch

](/docs/app/api-reference/functions/fetch)

[Next

generateImageMetadata

](/docs/app/api-reference/functions/generate-image-metadata)

Was this helpful?

supported.

Send




