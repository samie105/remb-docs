---
title: "public Folder"
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder"
canonical_url: "https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:21:26.245Z"
content_hash: "a172b1f8ddfb4fc944c5f75be5f3aed2697fad5b312477a92adb291e8f26a4bd"
menu_path: ["public Folder"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/file-conventions/proxy/index.md", "title": "Proxy"}
nav_next: {"path": "nextjs/docs/pages/api-reference/file-conventions/src-folder/index.md", "title": "src Directory"}
---

# public Folder

Last updated April 23, 2026

Next.js can serve static files, like images, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

For example, the file `public/avatars/me.png` can be viewed by visiting the `/avatars/me.png` path. The code to display that image might look like:

avatar.js

```
import Image from 'next/image'
 
export function Avatar({ id, alt }) {
  return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
}
 
export function AvatarOfMe() {
  return <Avatar id="me" alt="A portrait of me" />
}
```

## Caching[](#caching)

Next.js cannot safely cache assets in the `public` folder because they may change. The default caching headers applied are:

```
Cache-Control: public, max-age=0
```

## Robots, Favicons, and others[](#robots-favicons-and-others)

The folder is also useful for `robots.txt`, `favicon.ico`, Google Site Verification, and any other static files (including `.html`). But make sure to not have a static file with the same name as a file in the `pages/` directory, as this will result in an error. [Read more](/docs/messages/conflicting-public-file-page).

Was this helpful?
