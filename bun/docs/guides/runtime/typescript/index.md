---
title: "Install TypeScript declarations for Bun"
source: "https://bun.com/docs/guides/runtime/typescript"
canonical_url: "https://bun.com/docs/guides/runtime/typescript"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:53:25.251Z"
content_hash: "1c5cbae8f536d1a1d1af1676dffd649a99362b4d6e850fc49fd0d4966629978a"
menu_path: ["Install TypeScript declarations for Bun"]
section_path: []
---
To install TypeScript definitions for Bun’s built-in APIs in your project, install `@types/bun`.

terminal

```
bun add -d @types/bun # dev dependency
```

* * *

Below is the full set of recommended `compilerOptions` for a Bun project. With this `tsconfig.json`, you can use top-level await, extensioned or extensionless imports, and JSX.

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
    "noPropertyAccessFromIndexSignature": false
  }
}
```

* * *

If you’re using TypeScript 6.0 or later, you’ll also need to add `"types": ["bun"]` to your `compilerOptions`. See [TypeScript 6 and 7](https://bun.com/docs/typescript-6) for details.

* * *

Refer to [Ecosystem > TypeScript](https://bun.com/docs/runtime/typescript) for a complete guide to TypeScript support in Bun.
