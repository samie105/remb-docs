---
title: "typescript"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:09:01.697Z"
content_hash: "b9d066a59ea87f4695c58e21159a3b68e02b0bc3f14cf77ae1918d2c690cbdf9"
menu_path: ["typescript"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/typedRoutes/index.md", "title": "typedRoutes"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/urlImports/index.md", "title": "urlImports"}
---

# typescript

Last updated April 15, 2026

Configure TypeScript behavior with the `typescript` option in `next.config.js`:

next.config.js

```
module.exports = {
  typescript: {
    ignoreBuildErrors: false,
    tsconfigPath: 'tsconfig.json',
  },
}
```

## Options[](#options)

Option

Type

Default

Description

`ignoreBuildErrors`

`boolean`

`false`

Allow production builds to complete even with TypeScript errors.

`tsconfigPath`

`string`

`'tsconfig.json'`

Path to a custom `tsconfig.json` file.

## `ignoreBuildErrors`[](#ignorebuilderrors)

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

Note that this completely skips the TypeScript type checking step. It does not run TypeScript and suppress errors, it bypasses the check entirely.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

next.config.js

```
module.exports = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}
```

## `tsconfigPath`[](#tsconfigpath)

Use a different TypeScript configuration file for builds or tooling:

next.config.js

```
module.exports = {
  typescript: {
    tsconfigPath: 'tsconfig.build.json',
  },
}
```

See the [TypeScript configuration](/docs/app/api-reference/config/typescript#custom-tsconfig-path) page for more details.

[Previous

typedRoutes

](/docs/app/api-reference/config/next-config-js/typedRoutes)

[Next

urlImports

](/docs/app/api-reference/config/next-config-js/urlImports)

Was this helpful?

supported.

Send




