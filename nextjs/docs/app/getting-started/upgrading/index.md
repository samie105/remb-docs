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
---
[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Upgrading

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

-   [`forbidden`](/docs/app/api-reference/functions/forbidden)
-   [`unauthorized`](/docs/app/api-reference/functions/unauthorized)
-   [`forbidden.js`](/docs/app/api-reference/file-conventions/forbidden)
-   [`unauthorized.js`](/docs/app/api-reference/file-conventions/unauthorized)
-   [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts)

## Version guides

See the version guides for in-depth upgrade instructions.

[

### Version 16

Upgrade your Next.js Application from Version 15 to 16.

](/docs/app/guides/upgrading/version-16)[

### Version 15

Upgrade your Next.js Application from Version 14 to 15.

](/docs/app/guides/upgrading/version-15)[

### Version 14

Upgrade your Next.js Application from Version 13 to 14.

](/docs/app/guides/upgrading/version-14)

Was this helpful?
