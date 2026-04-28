---
title: "public Folder"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/public-folder"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/public-folder"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:20.235Z"
content_hash: "6fe16c289963ef20c2685b97a1b07edf213e3d41daa5d2a93c378e341a1a7583"
menu_path: ["public Folder"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/proxy/index.md", "title": "proxy.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/route/index.md", "title": "route.js"}
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

For static metadata files, such as `robots.txt`, `favicon.ico`, etc, you should use [special metadata files](/docs/app/api-reference/file-conventions/metadata) inside the `app` folder.

Was this helpful?
