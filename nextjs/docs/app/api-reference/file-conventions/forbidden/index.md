---
title: "forbidden.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:09:51.243Z"
content_hash: "359375f6b8394a1306ad9781780a6ca2c16a7d892aabee07a06f0db658a44d01"
menu_path: ["forbidden.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/error/index.md", "title": "error.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/instrumentation/index.md", "title": "instrumentation.js"}
---

# forbidden.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

The **forbidden** file is used to render UI when the [`forbidden`](/docs/app/api-reference/functions/forbidden) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.

app/forbidden.tsx

TypeScript

JavaScriptTypeScript

```
import Link from 'next/link'
 
export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

## Reference[](#reference)

### Props[](#props)

`forbidden.js` components do not accept any props.

## Version History[](#version-history)

Version

Changes

`v15.1.0`

`forbidden.js` introduced.

[

### forbidden

API Reference for the forbidden function.

](/docs/app/api-reference/functions/forbidden)

[Previous

error.js

](/docs/app/api-reference/file-conventions/error)

[Next

instrumentation.js

](/docs/app/api-reference/file-conventions/instrumentation)

Was this helpful?

supported.

Send
