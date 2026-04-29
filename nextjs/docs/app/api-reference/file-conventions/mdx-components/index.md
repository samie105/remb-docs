---
title: "mdx-components.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:08:50.890Z"
content_hash: "6d8c1600cff492821235d74d5ccca5037715982c5a7252fea44028e419600792"
menu_path: ["mdx-components.js"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/loading/index.md", "title": "loading.js"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/not-found/index.md", "title": "not-found.js"}
---

# mdx-components.js

Last updated April 23, 2026

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](../../../guides/mdx/index.md) and will not work without it. Additionally, you can use it to [customize styles](../../../guides/mdx/index.md#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

mdx-components.tsx

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

JavaScriptTypeScript

```
import type { MDXComponents } from 'mdx/types'
 
const components: MDXComponents = {}
 
export function useMDXComponents(): MDXComponents {
  return components
}
```

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v13.1.2` | MDX Components added |

## Learn more about MDX Components

[

### MDX

Learn how to configure MDX and use it in your Next.js apps.

](../../../guides/mdx/index.md)

Was this helpful?
