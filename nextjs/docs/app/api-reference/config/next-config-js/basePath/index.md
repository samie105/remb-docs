---
title: "basePath"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:06:58.180Z"
content_hash: "cf197f2dbe49ab22860e1d36c74c71bb51ce7d735fbcfd5816decbe642c68a60"
menu_path: ["basePath"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/authInterrupts/index.md", "title": "authInterrupts"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/cacheComponents/index.md", "title": "cacheComponents"}
---

# basePath

Last updated April 15, 2026

To deploy a Next.js application under a sub-path of a domain you can use the `basePath` config option.

`basePath` allows you to set a path prefix for the application. For example, to use `/docs` instead of `''` (an empty string, the default), open `next.config.js` and add the `basePath` config:

next.config.js

```
module.exports = {
  basePath: '/docs',
}
```

> **Good to know**: This value must be set at build time and cannot be changed without re-building as the value is inlined in the client-side bundles.

### Links[](#links)

When linking to other pages using `next/link` and `next/router` the `basePath` will be automatically applied.

For example, using `/about` will automatically become `/docs/about` when `basePath` is set to `/docs`.

```
export default function HomePage() {
  return (
    <>
      <Link href="/about">About Page</Link>
    </>
  )
}
```

Output html:

```
<a href="/docs/about">About Page</a>
```

This makes sure that you don't have to change all links in your application when changing the `basePath` value.

### Images[](#images)

When using the [`next/image`](/docs/app/api-reference/components/image) component, you will need to add the `basePath` in front of `src`.

For example, using `/docs/me.png` will properly serve your image when `basePath` is set to `/docs`.

```
import Image from 'next/image'
 
function Home() {
  return (
    <>
      <h1>My Homepage</h1>
      <Image
        src="/docs/me.png"
        alt="Picture of the author"
        width={500}
        height={500}
      />
      <p>Welcome to my homepage!</p>
    </>
  )
}
 
export default Home
```

[Previous

authInterrupts

](/docs/app/api-reference/config/next-config-js/authInterrupts)

[Next

cacheComponents

](/docs/app/api-reference/config/next-config-js/cacheComponents)

Was this helpful?

supported.

Send


