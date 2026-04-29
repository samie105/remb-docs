---
title: "ESLint Plugin"
source: "https://nextjs.org/docs/app/api-reference/config/eslint"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/eslint"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:05:39.621Z"
content_hash: "0a429a1f7a9d0fb77a7c642a6075c20a8dc2742cf8c89fcdd7733dac94f7a43e"
menu_path: ["ESLint Plugin"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/config/typescript/index.md", "title": "TypeScript"}
nav_next: {"path": "nextjs/docs/app/api-reference/cli/index.md", "title": "CLI"}
---

# ESLint Plugin

Last updated April 23, 2026

Next.js provides an ESLint configuration package, [`eslint-config-next`](https://www.npmjs.com/package/eslint-config-next), that makes it easy to catch common issues in your application. It includes the [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next) plugin along with recommended rule-sets from [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react) and [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks).

The package provides two main configurations:

-   **`eslint-config-next`**: Base configuration with Next.js, React, and React Hooks rules. Supports both JavaScript and TypeScript files.
-   **`eslint-config-next/core-web-vitals`**: Includes everything from the base config, plus upgrades rules that impact [Core Web Vitals](https://web.dev/vitals/) from warnings to errors. Recommended for most projects.

Additionally, for TypeScript projects:

-   **`eslint-config-next/typescript`**: Adds TypeScript-specific linting rules from [`typescript-eslint`](https://typescript-eslint.io/). Use this alongside the base or core-web-vitals config.

## Setup ESLint[](#setup-eslint)

Get linting working quickly with the ESLint CLI (flat config):

1.  Install ESLint and the Next.js config:
    
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
    pnpm add -D eslint eslint-config-next
    ```
    
2.  Create `eslint.config.mjs` with the Next.js config:
    
    eslint.config.mjs
    
    ```
    import { defineConfig, globalIgnores } from 'eslint/config'
    import nextVitals from 'eslint-config-next/core-web-vitals'
     
    const eslintConfig = defineConfig([
      ...nextVitals,
      // Override default ignores of eslint-config-next.
      globalIgnores([
        // Default ignores of eslint-config-next:
        '.next/**',
        'out/**',
        'build/**',
        'next-env.d.ts',
      ]),
    ])
     
    export default eslintConfig
    ```
    
3.  Run ESLint:
    
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
    pnpm exec eslint .
    ```
    

## Reference[](#reference)

The `eslint-config-next` package includes the `recommended` rule-sets from the following ESLint plugins:

-   [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react)
-   [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks)
-   [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next)

### Rules[](#rules)

The `@next/eslint-plugin-next` rules included are:

| Enabled in recommended config | Rule | Description |
| --- | --- | --- |
|  | [@next/next/google-font-display](../../../../messages/google-font-display/index.md) | Enforce font-display behavior with Google Fonts. |
|  | [@next/next/google-font-preconnect](../../../../messages/google-font-preconnect/index.md) | Ensure `preconnect` is used with Google Fonts. |
|  | [@next/next/inline-script-id](../../../../messages/inline-script-id/index.md) | Enforce `id` attribute on `next/script` components with inline content. |
|  | [@next/next/next-script-for-ga](../../../../messages/next-script-for-ga/index.md) | Prefer `next/script` component when using the inline script for Google Analytics. |
|  | [@next/next/no-assign-module-variable](../../../../messages/no-assign-module-variable/index.md) | Prevent assignment to the `module` variable. |
|  | [@next/next/no-async-client-component](../../../../messages/no-async-client-component/index.md) | Prevent Client Components from being async functions. |
|  | [@next/next/no-before-interactive-script-outside-document](../../../../messages/no-before-interactive-script-outside-document/index.md) | Prevent usage of `next/script`'s `beforeInteractive` strategy outside of `pages/_document.js`. |
|  | [@next/next/no-css-tags](../../../../messages/no-css-tags/index.md) | Prevent manual stylesheet tags. |
|  | [@next/next/no-document-import-in-page](../../../../messages/no-document-import-in-page/index.md) | Prevent importing `next/document` outside of `pages/_document.js`. |
|  | [@next/next/no-duplicate-head](../../../../messages/no-duplicate-head/index.md) | Prevent duplicate usage of `<Head>` in `pages/_document.js`. |
|  | [@next/next/no-head-element](../../../../messages/no-head-element/index.md) | Prevent usage of `<head>` element. |
|  | [@next/next/no-head-import-in-document](../../../../messages/no-head-import-in-document/index.md) | Prevent usage of `next/head` in `pages/_document.js`. |
|  | [@next/next/no-html-link-for-pages](../../../../messages/no-html-link-for-pages/index.md) | Prevent usage of `<a>` elements to navigate to internal Next.js pages. |
|  | [@next/next/no-img-element](../../../../messages/no-img-element/index.md) | Prevent usage of `<img>` element due to slower LCP and higher bandwidth. |
|  | [@next/next/no-page-custom-font](../../../../messages/no-page-custom-font/index.md) | Prevent page-only custom fonts. |
|  | [@next/next/no-script-component-in-head](../../../../messages/no-script-component-in-head/index.md) | Prevent usage of `next/script` in `next/head` component. |
|  | [@next/next/no-styled-jsx-in-document](../../../../messages/no-styled-jsx-in-document/index.md) | Prevent usage of `styled-jsx` in `pages/_document.js`. |
|  | [@next/next/no-sync-scripts](../../../../messages/no-sync-scripts/index.md) | Prevent synchronous scripts. |
|  | [@next/next/no-title-in-document-head](../../../../messages/no-title-in-document-head/index.md) | Prevent usage of `<title>` with `Head` component from `next/document`. |
|  | @next/next/no-typos | Prevent common typos in [Next.js's data fetching functions](../../../../pages/building-your-application/data-fetching/index.md) |
|  | [@next/next/no-unwanted-polyfillio](../../../../messages/no-unwanted-polyfillio/index.md) | Prevent duplicate polyfills from Polyfill.io. |

We recommend using an appropriate [integration](https://eslint.org/docs/user-guide/integrations#editors) to view warnings and errors directly in your code editor during development.

**next lint removal**

Starting with Next.js 16, `next lint` is removed.

As part of the removal, the `eslint` option in your Next config file is no longer needed and can be safely removed.

## Examples[](#examples)

### Specifying a root directory within a monorepo[](#specifying-a-root-directory-within-a-monorepo)

If you're using `@next/eslint-plugin-next` in a project where Next.js isn't installed in your root directory (such as a monorepo), you can tell `@next/eslint-plugin-next` where to find your Next.js application using the `settings` property in your `eslint.config.mjs`:

eslint.config.mjs

```
import { defineConfig } from 'eslint/config'
import eslintNextPlugin from '@next/eslint-plugin-next'
 
const eslintConfig = defineConfig([
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    plugins: {
      next: eslintNextPlugin,
    },
    settings: {
      next: {
        rootDir: 'packages/my-app/',
      },
    },
  },
])
 
export default eslintConfig
```

`rootDir` can be a path (relative or absolute), a glob (i.e. `"packages/*/"`), or an array of paths and/or globs.

### Disabling rules[](#disabling-rules)

If you would like to modify or disable any rules provided by the supported plugins (`react`, `react-hooks`, `next`), you can directly change them using the `rules` property in your `eslint.config.mjs`:

eslint.config.mjs

```
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
 
const eslintConfig = defineConfig([
  ...nextVitals,
  {
    rules: {
      'react/no-unescaped-entities': 'off',
      '@next/next/no-page-custom-font': 'off',
    },
  },
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])
 
export default eslintConfig
```

### With Core Web Vitals[](#with-core-web-vitals)

Enable the `eslint-config-next/core-web-vitals` configuration in your ESLint config.

eslint.config.mjs

```
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
 
const eslintConfig = defineConfig([
  ...nextVitals,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])
 
export default eslintConfig
```

`eslint-config-next/core-web-vitals` upgrades certain lint rules in `@next/eslint-plugin-next` from warnings to errors to help improve your [Core Web Vitals](https://web.dev/vitals/) metrics.

> The `eslint-config-next/core-web-vitals` configuration is automatically included for new applications built with [Create Next App](../../cli/create-next-app/index.md).

### With TypeScript[](#with-typescript)

In addition to the Next.js ESLint rules, `create-next-app --typescript` will also add TypeScript-specific lint rules with `eslint-config-next/typescript` to your config:

eslint.config.mjs

```
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import nextTs from 'eslint-config-next/typescript'
 
const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])
 
export default eslintConfig
```

Those rules are based on [`plugin:@typescript-eslint/recommended`](https://typescript-eslint.io/linting/configs#recommended). See [typescript-eslint > Configs](https://typescript-eslint.io/linting/configs) for more details.

### With Prettier[](#with-prettier)

ESLint also contains code formatting rules, which can conflict with your existing [Prettier](https://prettier.io/) setup. We recommend including [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) in your ESLint config to make ESLint and Prettier work together.

First, install the dependency:

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
pnpm add -D eslint-config-prettier
```

Then, add `prettier` to your existing ESLint config:

eslint.config.mjs

```
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import prettier from 'eslint-config-prettier/flat'
 
const eslintConfig = defineConfig([
  ...nextVitals,
  prettier,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])
 
export default eslintConfig
```

### Running lint on staged files[](#running-lint-on-staged-files)

If you would like to use ESLint with [lint-staged](https://github.com/okonet/lint-staged) to run the linter on staged git files, add the following to the `.lintstagedrc.js` file in the root of your project:

.lintstagedrc.js

```
const path = require('path')
 
const buildEslintCommand = (filenames) =>
  `eslint --fix ${filenames
    .map((f) => `"${path.relative(process.cwd(), f)}"`)
    .join(' ')}`
 
module.exports = {
  '*.{js,jsx,ts,tsx}': [buildEslintCommand],
}
```

## Migrating existing config[](#migrating-existing-config)

If you already have ESLint configured in your application, there are two approaches to integrate Next.js linting rules, depending on your setup.

#### Using the plugin directly[](#using-the-plugin-directly)

Use `@next/eslint-plugin-next` directly if you have any of the following already configured:

-   Conflicting plugins installed separately or through another config (such as `airbnb` or `react-app`):
    -   `react`
    -   `react-hooks`
    -   `jsx-a11y`
    -   `import`
-   Custom `parserOptions` different from Next.js defaults (only if you have [customized your Babel configuration](/docs/pages/guides/babel))
-   `eslint-plugin-import` with custom Node.js and/or TypeScript [resolvers](https://github.com/benmosher/eslint-plugin-import#resolvers)

In these cases, use `@next/eslint-plugin-next` directly to avoid conflicts:

First, install the plugin:

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
pnpm add -D @next/eslint-plugin-next
```

Then add it to your ESLint config:

eslint.config.mjs

```
import { defineConfig } from 'eslint/config'
import nextPlugin from '@next/eslint-plugin-next'
 
const eslintConfig = defineConfig([
  // Your other configurations...
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    plugins: {
      '@next/next': nextPlugin,
    },
    rules: {
      ...nextPlugin.configs.recommended.rules,
    },
  },
])
 
export default eslintConfig
```

This approach eliminates the risk of collisions or errors that can occur when the same plugins or parsers are imported across multiple configurations.

#### Adding to existing config[](#adding-to-existing-config)

If you're adding Next.js to an existing ESLint setup, spread the Next.js config into your array:

eslint.config.mjs

```
import nextConfig from 'eslint-config-next/core-web-vitals'
// Your other config imports...
 
const eslintConfig = [
  // Your other configurations...
  ...nextConfig,
]
 
export default eslintConfig
```

When you spread `...nextConfig`, you're adding multiple config objects that include file patterns, plugins, rules, ignores, and parser settings. ESLint applies configs in order, so later rules can override earlier ones for matching files.

> **Good to know:** This approach works well for straightforward setups. If you have a complex existing config with specific file patterns or plugin configurations that conflict, consider using the plugin directly (as shown above) for more granular control.

| Version | Changes |
| --- | --- |
| `v16.0.0` | `next lint` and the `eslint` next.config.js option were removed in favor of the ESLint CLI. A [codemod](../../../guides/upgrading/codemods/index.md#migrate-from-next-lint-to-eslint-cli) is available to help you migrate. |

Was this helpful?
