---
title: "use server"
source: "https://nextjs.org/docs/app/api-reference/directives/use-server"
canonical_url: "https://nextjs.org/docs/app/api-reference/directives/use-server"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:20.656Z"
content_hash: "ee7cab26f8ef781944e43bcdc202ac1727a03117c5a8170d49bb1bf24b045638"
menu_path: ["use server"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/directives/use-client/index.md", "title": "use client"}
nav_next: {"path": "nextjs/docs/app/api-reference/components/index.md", "title": "Components"}
---

# use server

Last updated April 23, 2026

The `use server` directive designates a function or file to be executed on the **server side**. It can be used at the top of a file to indicate that all functions in the file are server-side, or inline at the top of a function to mark the function as a [Server Function](https://19.react.dev/reference/rsc/server-functions). This is a React feature.

## Using `use server` at the top of a file[](#using-use-server-at-the-top-of-a-file)

The following example shows a file with a `use server` directive at the top. All functions in the file are executed on the server.

app/actions.ts

JavaScriptTypeScript

```
'use server'
import { db } from '@/lib/db' // Your database client
import { auth } from '@/lib/auth'
 
export async function createUser(data: { name: string; email: string }) {
  const session = await auth()
  if (!session?.user) {
    throw new Error('Unauthorized')
  }
 
  const user = await db.user.create({ data })
  return { id: user.id, name: user.name }
}
```

### Using Server Functions in a Client Component[](#using-server-functions-in-a-client-component)

To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the `use server` directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.

Assuming you have a `fetchUsers` Server Function in `actions.ts`:

app/actions.ts

JavaScriptTypeScript

```
'use server'
import { db } from '@/lib/db' // Your database client
import { auth } from '@/lib/auth'
 
export async function fetchUsers() {
  const session = await auth()
  if (!session?.user) {
    throw new Error('Unauthorized')
  }
 
  const users = await db.user.findMany({
    select: { id: true, name: true, email: true },
  })
  return users
}
```

Then you can import the `fetchUsers` Server Function into a Client Component and execute it on the client-side.

app/components/my-button.tsx

JavaScriptTypeScript

```
'use client'
import { fetchUsers } from '../actions'
 
export default function MyButton() {
  return <button onClick={() => fetchUsers()}>Fetch Users</button>
}
```

## Using `use server` inline[](#using-use-server-inline)

In the following example, `use server` is used inline at the top of a function to mark it as a [Server Function](https://19.react.dev/reference/rsc/server-functions):

app/posts/\[id\]/page.tsx

JavaScriptTypeScript

```
import { EditPost } from './edit-post'
import { revalidatePath } from 'next/cache'
 
export default async function PostPage({ params }: { params: { id: string } }) {
  const post = await getPost(params.id)
 
  async function updatePost(formData: FormData) {
    'use server'
    // Verify auth before saving (e.g. inside savePost)
    await savePost(params.id, formData)
    revalidatePath(`/posts/${params.id}`)
  }
 
  return <EditPost updatePostAction={updatePost} post={post} />
}
```

## Security considerations[](#security-considerations)

Design your data access functions as secure primitives: validate inputs, check authentication and authorization, and constrain return types to only what the caller needs. When Server Functions delegate to a [Data Access Layer](/docs/app/guides/data-security#using-a-data-access-layer-for-mutations), these guarantees live in one place and apply consistently.

### Authentication and authorization[](#authentication-and-authorization)

Always authenticate and authorize users before performing sensitive server-side operations. Read authentication from cookies or headers rather than accepting tokens as function parameters.

app/actions.ts

JavaScriptTypeScript

```
'use server'
 
import { db } from '@/lib/db' // Your database client
import { auth } from '@/lib/auth' // Your authentication library
 
export async function createUser(data: { name: string; email: string }) {
  const session = await auth()
  if (!session?.user) {
    throw new Error('Unauthorized')
  }
  const newUser = await db.user.create({ data })
  return { id: newUser.id, name: newUser.name }
}
```

### Return values[](#return-values)

Server Function return values are serialized and sent to the client. Only return data the UI needs, not raw database records. See the [Data Security guide](/docs/app/guides/data-security#controlling-return-values) for more details.

## Reference[](#reference)

See the [React documentation](https://react.dev/reference/rsc/use-server) for more information on `use server`.

Was this helpful?
