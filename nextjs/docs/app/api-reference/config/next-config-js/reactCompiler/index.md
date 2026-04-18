---
title: "reactCompiler"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:14.939Z"
content_hash: "4532e4a4002b826c50f885f0645b80d359e60d57ca12311f2268ec223c32f6bd"
menu_path: ["reactCompiler"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize/index.md", "title": "proxyClientMaxBodySize"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength/index.md", "title": "reactMaxHeadersLength"}
---

# reactCompiler

Last updated April 15, 2026

Next.js includes support for the [React Compiler](https://react.dev/learn/react-compiler/introduction), a tool designed to improve performance by automatically optimizing component rendering. This reduces the need for manual memoization using `useMemo` and `useCallback`.

Next.js includes a custom performance optimization written in SWC that makes the React Compiler more efficient. Instead of running the compiler on every file, Next.js analyzes your project and only applies the React Compiler to relevant files. This avoids unnecessary work and leads to faster builds compared to using the Babel plugin on its own.

## How It Works[](#how-it-works)

The React Compiler runs through a Babel plugin. To keep builds fast, Next.js uses a custom SWC optimization that only applies the React Compiler to relevant files—like those with JSX or React Hooks.

This avoids compiling everything and keeps the performance cost minimal. You may still see slightly slower builds compared to the default Rust-based compiler, but the impact is small and localized.

To use it, install the `babel-plugin-react-compiler`:

pnpmnpmyarnbun

Terminal

```
pnpm add -D babel-plugin-react-compiler
```

Then, add `reactCompiler` option in `next.config.js`:

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  reactCompiler: true,
}
 
export default nextConfig
```

## Annotations[](#annotations)

You can configure the compiler to run in "opt-in" mode as follows:

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  reactCompiler: {
    compilationMode: 'annotation',
  },
}
 
export default nextConfig
```

Then, you can annotate specific components or hooks with the `"use memo"` directive from React to opt-in:

app/page.tsx

TypeScript

JavaScriptTypeScript

```
export default function Page() {
  'use memo'
  // ...
}
```

> **Note:** You can also use the `"use no memo"` directive from React for the opposite effect, to opt-out a component or hook.

[Previous

proxyClientMaxBodySize

](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize)

[Next

reactMaxHeadersLength

](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)

Was this helpful?

supported.

Send
