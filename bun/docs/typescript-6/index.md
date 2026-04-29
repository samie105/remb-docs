---
title: "TypeScript 6 and 7"
source: "https://bun.com/docs/typescript-6"
canonical_url: "https://bun.com/docs/typescript-6"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:51.566Z"
content_hash: "84ab917b392c6f706d846e60d3d997982779a255f7aa5d352359ab8bce7e3965"
menu_path: ["TypeScript 6 and 7"]
section_path: []
nav_prev: {"path": "bun/docs/typescript/index.md", "title": "TypeScript"}
---

TypeScript 6.0 changed how type definitions are discovered. If you’ve upgraded TypeScript and your editor no longer recognizes `Bun`, `Request`, or other globals from `@types/bun`, here’s how to fix it.

## What changed

Starting in TypeScript 6.0, the `types` field in `compilerOptions` defaults to an empty array instead of including all `@types/*` packages. You now need to explicitly list the type packages you use.

## Add `"types": ["bun"]` to your tsconfig

In your `tsconfig.json`, add `"types": ["bun"]` to `compilerOptions`:

tsconfig.json

```
{
  "compilerOptions": {
    "types": ["bun"], 
  },
}
```

This tells TypeScript to load type definitions from `@types/bun`. If you use other `@types/*` packages, include them too:

tsconfig.json

```
{
  "compilerOptions": {
    "types": ["bun", "react"],
  },
}
```

You still need `@types/bun` installed — the `types` option tells TypeScript _which_ packages to include, but the package itself must exist in `node_modules`:

terminal

```
bun add -d @types/bun
```

## Full recommended tsconfig.json

Here’s the full recommended `tsconfig.json` for a Bun project using TypeScript 6.0 or later:

tsconfig.json

```
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,
    "types": ["bun"],

    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags (disabled by default)
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noPropertyAccessFromIndexSignature": false,
  },
}
```

## Does this apply to TypeScript 7?

Yes. TypeScript 7 carries forward the same default. If you’re upgrading directly from TypeScript 5 to 7, the same fix applies — add `"types": ["bun"]` to your `compilerOptions`.
