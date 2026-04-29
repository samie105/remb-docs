---
title: "Upgrading"
source: "https://nextjs.org/docs/app/getting-started/upgrading"
canonical_url: "https://nextjs.org/docs/app/getting-started/upgrading"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:12:32.924Z"
content_hash: "16e125e025f1084e0c7f0238b791ec64fc22246795cb4decd9a41c936dcd545b"
menu_path: ["Upgrading"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/getting-started/deploying/index.md", "title": "Deploying"}
nav_next: {"path": "nextjs/docs/app/guides/index.md", "title": "Guides"}
---

# Upgrading

Last updated April 23, 2026

## Latest version[](#latest-version)

To update to the latest version of Next.js, you can use the `upgrade` command:

#### pnpm

pnpm

#### npm

npm

#### yarn

yarn

#### bun

bun

Terminal

```
pnpm next upgrade
```

Versions before Next.js 16.1.0 do not support the `upgrade` command and need to use a separate package instead:

Terminal

```
npx @next/codemod@canary upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:

#### pnpm

pnpm

#### npm

npm

#### yarn

yarn

#### bun

bun

Terminal

```
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

## Canary version[](#canary-version)

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

#### pnpm

pnpm

#### npm

npm

#### yarn

yarn

#### bun

bun

Terminal

```
pnpm add next@canary
```

### Features available in canary[](#features-available-in-canary)

The following features are currently available in canary:

**Authentication**:

-   [`forbidden`](../../api-reference/functions/forbidden/index.md)
-   [`unauthorized`](../../api-reference/functions/unauthorized/index.md)
-   [`forbidden.js`](../../api-reference/file-conventions/forbidden/index.md)
-   [`unauthorized.js`](../../api-reference/file-conventions/unauthorized/index.md)
-   [`authInterrupts`](../../api-reference/config/next-config-js/authInterrupts/index.md)

## Version guides

See the version guides for in-depth upgrade instructions.

[

### Version 16

Upgrade your Next.js Application from Version 15 to 16.

](../../guides/upgrading/version-16/index.md)[

### Version 15

Upgrade your Next.js Application from Version 14 to 15.

](../../guides/upgrading/version-15/index.md)[

### Version 14

Upgrade your Next.js Application from Version 13 to 14.

](../../guides/upgrading/version-14/index.md)

Was this helpful?
