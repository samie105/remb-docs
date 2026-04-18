---
title: "How to set up Vitest with Next.js"
source: "https://nextjs.org/docs/app/guides/testing/vitest"
canonical_url: "https://nextjs.org/docs/app/guides/testing/vitest"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:44.422Z"
content_hash: "d46a144732ac695a6acc4e8f5357dfb295e834b5e54d49bda4e8701ffb4d4481"
menu_path: ["How to set up Vitest with Next.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/testing/playwright/index.md", "title": "How to set up Playwright with Next.js"}
nav_next: {"path": "nextjs/docs/app/guides/third-party-libraries/index.md", "title": "How to optimize third-party libraries"}
---

# How to set up Vitest with Next.js

Last updated April 15, 2026

Vitest and React Testing Library are frequently used together for **Unit Testing**. This guide will show you how to setup Vitest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using **E2E tests** for `async` components.

## Quickstart[](#quickstart)

You can use `create-next-app` with the Next.js [with-vitest](https://github.com/vercel/next.js/tree/canary/examples/with-vitest) example to quickly get started:

pnpmnpmyarnbun

Terminal

```
pnpm create next-app --example with-vitest with-vitest-app
```

## Manual Setup[](#manual-setup)

To manually set up Vitest, install `vitest` and the following packages as dev dependencies:

pnpmnpmyarnbun

Terminal

```
# Using TypeScript
pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom vite-tsconfig-paths
# Using JavaScript
pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom
```

Create a `vitest.config.mts|js` file in the root of your project, and add the following options:

vitest.config.mts

TypeScript

JavaScriptTypeScript

```
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'
 
export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: {
    environment: 'jsdom',
  },
})
```

For more information on configuring Vitest, please refer to the [Vitest Configuration](https://vitest.dev/config/#configuration) docs.

Then, add a `test` script to your `package.json`:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test": "vitest"
  }
}
```

When you run `npm run test`, Vitest will **watch** for changes in your project by default.

## Creating your first Vitest Unit Test[](#creating-your-first-vitest-unit-test)

Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:

app/page.tsx

TypeScript

JavaScriptTypeScript

```
import Link from 'next/link'
 
export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

\_\_tests\_\_/page.test.tsx

TypeScript

JavaScriptTypeScript

```
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'
 
test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```

> **Good to know**: The example above uses the common `__tests__` convention, but test files can also be colocated inside the `app` router.

## Running your tests[](#running-your-tests)

Then, run the following command to run your tests:

pnpmnpmyarnbun

Terminal

```
pnpm test
```

## Additional Resources[](#additional-resources)

You may find these resources helpful:

*   [Next.js with Vitest example](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
*   [Vitest Docs](https://vitest.dev/guide/)
*   [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)

[Previous

Playwright

](/docs/app/guides/testing/playwright)

[Next

Third Party Libraries

](/docs/app/guides/third-party-libraries)

Was this helpful?

supported.

Send
