---
title: "How to set up Vitest with Next.js"
source: "https://nextjs.org/docs/app/guides/testing/vitest"
canonical_url: "https://nextjs.org/docs/app/guides/testing/vitest"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:16:06.424Z"
content_hash: "90b29c2cd7ceb4d5233b95c2b73f3ff3f296459ff5e57142e4694d550df21d4f"
menu_path: ["How to set up Vitest with Next.js"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun"]
content_language: "en"
---
[Guides](/docs/app/guides)[Testing](/docs/app/guides/testing)Vitest

# How to set up Vitest with Next.js

Last updated April 23, 2026

Vitest and React Testing Library are frequently used together for **Unit Testing**. This guide will show you how to setup Vitest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using **E2E tests** for `async` components.

## Quickstart[](#quickstart)

You can use `create-next-app` with the Next.js [with-vitest](https://github.com/vercel/next.js/tree/canary/examples/with-vitest) example to quickly get started:

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
pnpm create next-app --example with-vitest with-vitest-app
```

## Manual Setup[](#manual-setup)

To manually set up Vitest, install `vitest` and the following packages as dev dependencies:

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
# Using TypeScript
pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom vite-tsconfig-paths
# Using JavaScript
pnpm add -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom
```

Create a `vitest.config.mts|js` file in the root of your project, and add the following options:

vitest.config.mts

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
pnpm test
```

## Additional Resources[](#additional-resources)

You may find these resources helpful:

-   [Next.js with Vitest example](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
-   [Vitest Docs](https://vitest.dev/guide/)
-   [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)

Was this helpful?
