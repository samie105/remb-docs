---
title: "mdx-components.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:08.223Z"
content_hash: "3161675f0505d8ec7c1ba05467d58c4b36fdde70c6aa0d2fe3cb818452a137f3"
menu_path: ["mdx-components.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/loading/index.md", "title": "loading.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/not-found/index.md", "title": "not-found.js"}
---

# mdx-components.js

Last updated April 15, 2026

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](/docs/app/guides/mdx) and will not work without it. Additionally, you can use it to [customize styles](/docs/app/guides/mdx#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

mdx-components.tsx

TypeScript

JavaScriptTypeScript

```
import type { MDXComponents } from 'mdx/types'
 
const components: MDXComponents = {}
 
export function useMDXComponents(): MDXComponents {
  return components
}
```

## Exports[](#exports)

### `useMDXComponents` function[](#usemdxcomponents-function)

The file must export a single function named `useMDXComponents`. This function does not accept any arguments.

mdx-components.tsx

TypeScript

JavaScriptTypeScript

```
import type { MDXComponents } from 'mdx/types'
 
const components: MDXComponents = {}
 
export function useMDXComponents(): MDXComponents {
  return components
}
```

## Version History[](#version-history)

Version

Changes

`v13.1.2`

MDX Components added

## Learn more about MDX Components

[

### MDX

Learn how to configure MDX and use it in your Next.js apps.

](/docs/app/guides/mdx)

[Previous

loading.js

](/docs/app/api-reference/file-conventions/loading)

[Next

not-found.js

](/docs/app/api-reference/file-conventions/not-found)

Was this helpful?

supported.

Send
