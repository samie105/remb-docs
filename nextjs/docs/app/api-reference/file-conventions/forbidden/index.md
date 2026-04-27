---
title: "forbidden.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:36.085Z"
content_hash: "c209f07d55ec28402e316c204d0758be693653ab6c11383cba38505a9835452f"
menu_path: ["forbidden.js"]
section_path: []
version: "latest"
content_language: "en"
---
[API Reference](/docs/app/api-reference)[File-system conventions](/docs/app/api-reference/file-conventions)forbidden.js

# forbidden.js

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 23, 2026

The **forbidden** file is used to render UI when the [`forbidden`](/docs/app/api-reference/functions/forbidden) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.

app/forbidden.tsx

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

| Version | Changes |
| --- | --- |
| `v15.1.0` | `forbidden.js` introduced. |

[

### forbidden

API Reference for the forbidden function.

](/docs/app/api-reference/functions/forbidden)

Was this helpful?
