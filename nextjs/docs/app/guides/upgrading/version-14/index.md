---
title: "How to upgrade to version 14"
source: "https://nextjs.org/docs/app/guides/upgrading/version-14"
canonical_url: "https://nextjs.org/docs/app/guides/upgrading/version-14"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:53.750Z"
content_hash: "3917b0605b66e3007c60ab49b0b17ae4d9056666616f8d60a6d16636753813e4"
menu_path: ["How to upgrade to version 14"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/upgrading/codemods/index.md", "title": "Codemods"}
nav_next: {"path": "nextjs/docs/app/guides/upgrading/version-15/index.md", "title": "How to upgrade to version 15"}
---

# How to upgrade to version 14

Last updated April 15, 2026

## Upgrading from 13 to 14[](#upgrading-from-13-to-14)

To update to Next.js version 14, run the following command using your preferred package manager:

Terminal

```
npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

Terminal

```
yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

Terminal

```
pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

Terminal

```
bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

### v14 Summary[](#v14-summary)

*   The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life.
*   The `next export` command has been removed in favor of `output: 'export'` config. Please see the [docs](nextjs/docs/app/guides/static-exports/index.md) for more information.
*   The `next/server` import for `ImageResponse` was renamed to `next/og`. A [codemod is available](/docs/app/guides/upgrading/codemods#next-og-import) to safely and automatically rename your imports.
*   The `@next/font` package has been fully removed in favor of the built-in `next/font`. A [codemod is available](/docs/app/guides/upgrading/codemods#built-in-next-font) to safely and automatically rename your imports.
*   The WASM target for `next-swc` has been removed.

[Previous

Codemods

](/docs/app/guides/upgrading/codemods)

[Next

Version 15

](/docs/app/guides/upgrading/version-15)

Was this helpful?

supported.

Send




