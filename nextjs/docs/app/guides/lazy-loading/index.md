---
title: "How to lazy load Client Components and libraries"
source: "https://nextjs.org/docs/app/guides/lazy-loading"
canonical_url: "https://nextjs.org/docs/app/guides/lazy-loading"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:14:59.197Z"
content_hash: "d91316086ee76faa7b1fa6c3c690c0f322b9e13b865d6b7b94bedb0ad0cceb9c"
menu_path: ["How to lazy load Client Components and libraries"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/json-ld/index.md", "title": "How to implement JSON-LD in your Next.js application"}
nav_next: {"path": "nextjs/docs/app/guides/local-development/index.md", "title": "How to optimize your local development environment"}
---

# How to lazy load Client Components and libraries

Last updated April 15, 2026

[Lazy loading](https://developer.mozilla.org/docs/Web/Performance/Lazy_loading) in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.

It allows you to defer loading of **Client Components** and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.

There are two ways you can implement lazy loading in Next.js:

1.  Using [Dynamic Imports](#nextdynamic) with `next/dynamic`
2.  Using [`React.lazy()`](https://react.dev/reference/react/lazy) with [Suspense](https://react.dev/reference/react/Suspense)

By default, Server Components are automatically [code split](https://developer.mozilla.org/docs/Glossary/Code_splitting), and you can use [streaming](/docs/app/guides/streaming) to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.

## `next/dynamic`[](#nextdynamic)

`next/dynamic` is a composite of [`React.lazy()`](https://react.dev/reference/react/lazy) and [Suspense](https://react.dev/reference/react/Suspense). It behaves the same way in the `app` and `pages` directories to allow for incremental migration.

## Examples[](#examples)

### Importing Client Components[](#importing-client-components)

app/page.js

```
'use client'
 
import { useState } from 'react'
import dynamic from 'next/dynamic'
 
// Client Components:
const ComponentA = dynamic(() => import('../components/A'))
const ComponentB = dynamic(() => import('../components/B'))
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
 
export default function ClientComponentExample() {
  const [showMore, setShowMore] = useState(false)
 
  return (
    <div>
      {/* Load immediately, but in a separate client bundle */}
      <ComponentA />
 
      {/* Load on demand, only when/if the condition is met */}
      {showMore && <ComponentB />}
      <button onClick={() => setShowMore(!showMore)}>Toggle</button>
 
      {/* Load only on the client side */}
      <ComponentC />
    </div>
  )
}
```

> **Note:** When a Server Component dynamically imports a Client Component, automatic [code splitting](https://developer.mozilla.org/docs/Glossary/Code_splitting) is currently **not** supported.

### Skipping SSR[](#skipping-ssr)

When using `React.lazy()` and Suspense, Client Components will be [prerendered](https://github.com/reactwg/server-components/discussions/4) (SSR) by default.

> **Note:** `ssr: false` option will only work for Client Components, move it into Client Components ensure the client code-splitting working properly.

If you want to disable prerendering for a Client Component, you can use the `ssr` option set to `false`:

```
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
```

### Importing Server Components[](#importing-server-components)

If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself. It will also help preload the static assets such as CSS when you're using it in Server Components.

app/page.js

```
import dynamic from 'next/dynamic'
 
// Server Component:
const ServerComponent = dynamic(() => import('../components/ServerComponent'))
 
export default function ServerComponentExample() {
  return (
    <div>
      <ServerComponent />
    </div>
  )
}
```

> **Note:** `ssr: false` option is not supported in Server Components. You will see an error if you try to use it in Server Components. `ssr: false` is not allowed with `next/dynamic` in Server Components. Please move it into a Client Component.

### Loading External Libraries[](#loading-external-libraries)

External libraries can be loaded on demand using the [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) function. This example uses the external library `fuse.js` for fuzzy search. The module is only loaded on the client after the user types in the search input.

app/page.js

```
'use client'
 
import { useState } from 'react'
 
const names = ['Tim', 'Joe', 'Bel', 'Lee']
 
export default function Page() {
  const [results, setResults] = useState()
 
  return (
    <div>
      <input
        type="text"
        placeholder="Search"
        onChange={async (e) => {
          const { value } = e.currentTarget
          // Dynamically load fuse.js
          const Fuse = (await import('fuse.js')).default
          const fuse = new Fuse(names)
 
          setResults(fuse.search(value))
        }}
      />
      <pre>Results: {JSON.stringify(results, null, 2)}</pre>
    </div>
  )
}
```

### Adding a custom loading component[](#adding-a-custom-loading-component)

app/page.js

```
'use client'
 
import dynamic from 'next/dynamic'
 
const WithCustomLoading = dynamic(
  () => import('../components/WithCustomLoading'),
  {
    loading: () => <p>Loading...</p>,
  }
)
 
export default function Page() {
  return (
    <div>
      {/* The loading component will be rendered while  <WithCustomLoading/> is loading */}
      <WithCustomLoading />
    </div>
  )
}
```

### Importing Named Exports[](#importing-named-exports)

To dynamically import a named export, you can return it from the Promise returned by [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) function:

components/hello.js

```
'use client'
 
export function Hello() {
  return <p>Hello!</p>
}
```

app/page.js

```
import dynamic from 'next/dynamic'
 
const ClientComponent = dynamic(() =>
  import('../components/hello').then((mod) => mod.Hello)
)
```

## Magic Comments[](#magic-comments)

Next.js supports magic comments to control how dynamic imports are handled by the bundler. These comments work with dynamic `import()`, `require()`, `require.resolve()`, and `new Worker()` expressions.

> **Good to know:** Magic comments do not work with static `import` statements (`import x from 'y'`). They only work with dynamic expressions.

### `webpackIgnore` / `turbopackIgnore`[](#webpackignore--turbopackignore)

Use these comments to skip bundling a dynamic import. The import expression will be left as-is in the output, useful for runtime-only modules:

```
// Skip bundling - import happens at runtime
const runtime = await import(/* webpackIgnore: true */ 'runtime-module')
 
// Turbopack-specific variant
const plugin = await import(/* turbopackIgnore: true */ pluginPath)
 
// Also works with require
const mod = require(/* webpackIgnore: true */ 'runtime-module')
```

### `turbopackOptional` (Turbopack only)[](#turbopackoptional-turbopack-only)

Use this comment to suppress build errors when a module might not exist. The import will still throw at runtime if the module is missing:

```
// No build error if './optional-feature' doesn't exist
// Runtime will throw MODULE_NOT_FOUND if executed
const feature = await import(/* turbopackOptional: true */ './optional-feature')
 
// Also works with require
const mod = require(/* turbopackOptional: true */ './optional-module')
```

This is useful for:

*   Conditional features that may not be installed
*   Plugin systems where modules are optional
*   Gradual migrations where some files may not exist yet

> **Good to know:** `webpackOptional` is not supported. Use `turbopackOptional` instead when using Turbopack.

[Previous

JSON-LD

](/docs/app/guides/json-ld)

[Next

Development Environment

](/docs/app/guides/local-development)

Was this helpful?

supported.

Send




