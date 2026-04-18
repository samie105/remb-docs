---
title: "refresh"
source: "https://nextjs.org/docs/app/api-reference/functions/refresh"
canonical_url: "https://nextjs.org/docs/app/api-reference/functions/refresh"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:12:06.113Z"
content_hash: "a515483e9a50586f475c9a3db19a5f4e383d91d7d5ed9a3c26b012486d246107"
menu_path: ["refresh"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/functions/redirect/index.md", "title": "redirect"}
nav_next: {"path": "nextjs/docs/app/api-reference/functions/revalidatePath/index.md", "title": "revalidatePath"}
---

# refresh

Last updated April 15, 2026

`refresh` allows you to refresh the client router from within a [Server Action](/docs/app/getting-started/mutating-data).

## Usage[](#usage)

`refresh` can **only** be called from within Server Actions. It cannot be used in Route Handlers, Client Components, or any other context.

## Parameters[](#parameters)

```
refresh(): void;
```

## Returns[](#returns)

`refresh` does not return a value.

## Examples[](#examples)

app/actions.ts

TypeScript

JavaScriptTypeScript

```
'use server'
 
import { refresh } from 'next/cache'
 
export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')
 
  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })
 
  refresh()
}
```

### Error when used outside Server Actions[](#error-when-used-outside-server-actions)

app/api/posts/route.ts

TypeScript

JavaScriptTypeScript

```
import { refresh } from 'next/cache'
 
export async function POST() {
  // This will throw an error
  refresh()
}
```

[Previous

redirect

](/docs/app/api-reference/functions/redirect)

[Next

revalidatePath

](/docs/app/api-reference/functions/revalidatePath)

Was this helpful?

supported.

Send


