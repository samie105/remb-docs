---
title: "Pages and Layouts"
source: "https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:22:51.870Z"
content_hash: "8fcb8e19ae2ce111913402632e35fd49c21067a5bd85218809e893844f3dfd81"
menu_path: ["Pages and Layouts"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/index.md", "title": "Routing"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/routing/dynamic-routes/index.md", "title": "Dynamic Routes"}
---

# Pages and Layouts

Last updated April 23, 2026

The Pages Router has a file-system based router built on the concept of pages.

When a file is added to the `pages` directory, it's automatically available as a route.

In Next.js, a **page** is a [React Component](https://react.dev/learn/your-first-component) exported from a `.js`, `.jsx`, `.ts`, or `.tsx` file in the `pages` directory. Each page is associated with a route based on its file name.

**Example**: If you create `pages/about.js` that exports a React component like below, it will be accessible at `/about`.

```
export default function About() {
  return <div>About</div>
}
```

## Index routes[](#index-routes)

The router will automatically route files named `index` to the root of the directory.

-   `pages/index.js` → `/`
-   `pages/blog/index.js` → `/blog`

## Nested routes[](#nested-routes)

The router supports nested files. If you create a nested folder structure, files will automatically be routed in the same way still.

-   `pages/blog/first-post.js` → `/blog/first-post`
-   `pages/dashboard/settings/username.js` → `/dashboard/settings/username`

## Pages with Dynamic Routes[](#pages-with-dynamic-routes)

Next.js supports pages with dynamic routes. For example, if you create a file called `pages/posts/[id].js`, then it will be accessible at `posts/1`, `posts/2`, etc.

> To learn more about dynamic routing, check the [Dynamic Routing documentation](../dynamic-routes/index.md).

## Layout Pattern[](#layout-pattern)

The React model allows us to deconstruct a [page](index.md) into a series of components. Many of these components are often reused between pages. For example, you might have the same navigation bar and footer on every page.

components/layout.js

```
import Navbar from './navbar'
import Footer from './footer'
 
export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```

## Examples[](#examples)

### Single Shared Layout with Custom App[](#single-shared-layout-with-custom-app)

If you only have one layout for your entire application, you can create a [Custom App](../custom-app/index.md) and wrap your application with the layout. Since the `<Layout />` component is re-used when changing pages, its component state will be preserved (e.g. input values).

pages/\_app.js

```
import Layout from '../components/layout'
 
export default function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
```

### Per-Page Layouts[](#per-page-layouts)

If you need multiple layouts, you can add a property `getLayout` to your page, allowing you to return a React component for the layout. This allows you to define the layout on a _per-page basis_. Since we're returning a function, we can have complex nested layouts if desired.

pages/index.js

```
 
import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'
 
export default function Page() {
  return (
    /** Your content */
  )
}
 
Page.getLayout = function getLayout(page) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}
```

pages/\_app.js

```
export default function MyApp({ Component, pageProps }) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)
 
  return getLayout(<Component {...pageProps} />)
}
```

When navigating between pages, we want to _persist_ page state (input values, scroll position, etc.) for a Single-Page Application (SPA) experience.

This layout pattern enables state persistence because the React component tree is maintained between page transitions. With the component tree, React can understand which elements have changed to preserve state.

> **Good to know**: This process is called [reconciliation](https://react.dev/learn/preserving-and-resetting-state), which is how React understands which elements have changed.

### With TypeScript[](#with-typescript)

When using TypeScript, you must first create a new type for your pages which includes a `getLayout` function. Then, you must create a new type for your `AppProps` which overrides the `Component` property to use the previously created type.

pages/index.tsx

JavaScriptTypeScript

```
import type { ReactElement } from 'react'
import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'
import type { NextPageWithLayout } from './_app'
 
const Page: NextPageWithLayout = () => {
  return <p>hello world</p>
}
 
Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}
 
export default Page
```

pages/\_app.tsx

JavaScriptTypeScript

```
import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'
 
export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode
}
 
type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}
 
export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)
 
  return getLayout(<Component {...pageProps} />)
}
```

### Data Fetching[](#data-fetching)

Inside your layout, you can fetch data on the client-side using `useEffect` or a library like [SWR](https://swr.vercel.app/). Because this file is not a [Page](index.md), you cannot use `getStaticProps` or `getServerSideProps` currently.

components/layout.js

```
import useSWR from 'swr'
import Navbar from './navbar'
import Footer from './footer'
 
export default function Layout({ children }) {
  const { data, error } = useSWR('/api/navigation', fetcher)
 
  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>
 
  return (
    <>
      <Navbar links={data.links} />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```

Was this helpful?
