---
title: "How to set up instrumentation"
source: "https://nextjs.org/docs/app/guides/instrumentation"
canonical_url: "https://nextjs.org/docs/app/guides/instrumentation"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:13:45.090Z"
content_hash: "4292d405dd9e861a1a94ffcd2bda751ee239a87afb7d1adbe3ebc833a7dfdc71"
menu_path: ["How to set up instrumentation"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/incremental-static-regeneration/index.md", "title": "How to implement Incremental Static Regeneration (ISR)"}
nav_next: {"path": "nextjs/docs/app/guides/internationalization/index.md", "title": "Internationalization"}
---

# How to set up instrumentation

Last updated April 23, 2026

Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.

## Convention[](#convention)

To set up instrumentation, create `instrumentation.ts|js` file in the **root directory** of your project (or inside the [`src`](/docs/app/api-reference/file-conventions/src-folder) folder if using one).

Then, export a `register` function in the file. This function will be called **once** when a new Next.js server instance is initiated, and must complete before the server is ready to handle requests.

For example, to use Next.js with [OpenTelemetry](https://opentelemetry.io/) and [@vercel/otel](https://vercel.com/docs/observability/otel-overview):

instrumentation.ts

JavaScriptTypeScript

```
import { registerOTel } from '@vercel/otel'
 
export function register() {
  registerOTel('next-app')
}
```

See the [Next.js with OpenTelemetry example](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry) for a complete implementation.

> **Good to know**:
> 
> -   The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
> -   If you use the [`pageExtensions` config option](/docs/app/api-reference/config/next-config-js/pageExtensions) to add a suffix, you will also need to update the `instrumentation` filename to match.

## Examples[](#examples)

### Importing files with side effects[](#importing-files-with-side-effects)

Sometimes, it may be useful to import a file in your code because of the side effects it will cause. For example, you might import a file that defines a set of global variables, but never explicitly use the imported file in your code. You would still have access to the global variables the package has declared.

We recommend importing files using JavaScript `import` syntax within your `register` function. The following example demonstrates a basic usage of `import` in a `register` function:

instrumentation.ts

JavaScriptTypeScript

```
export async function register() {
  await import('package-with-side-effect')
}
```

> **Good to know:**
> 
> We recommend importing the file from within the `register` function, rather than at the top of the file. By doing this, you can colocate all of your side effects in one place in your code, and avoid any unintended consequences from importing globally at the top of the file.

### Importing runtime-specific code[](#importing-runtime-specific-code)

Next.js calls `register` in all environments, so it's important to conditionally import any code that doesn't support specific runtimes (e.g. [Edge or Node.js](/docs/app/api-reference/edge)). You can use the `NEXT_RUNTIME` environment variable to get the current environment:

instrumentation.ts

JavaScriptTypeScript

```
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation-node')
  }
 
  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./instrumentation-edge')
  }
}
```

## Learn more about Instrumentation

[

### instrumentation.js

API reference for the instrumentation.js file.

](/docs/app/api-reference/file-conventions/instrumentation)

Was this helpful?
