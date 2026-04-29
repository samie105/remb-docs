---
title: "Linking and Navigating"
source: "https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:22:49.398Z"
content_hash: "a4c101df7d72d640b6b333fbfeceecc6dd78cc9835d6e0c6012de547243945b7"
menu_path: ["Linking and Navigating"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/dynamic-routes/index.md", "title": "Dynamic Routes"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/routing/custom-app/index.md", "title": "Custom App"}
---

# Linking and Navigating

Last updated April 23, 2026

The Next.js router allows you to do client-side route transitions between pages, similar to a single-page application.

A React component called `Link` is provided to do this client-side route transition.

```
import Link from 'next/link'
 
function Home() {
  return (
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/about">About Us</Link>
      </li>
      <li>
        <Link href="/blog/hello-world">Blog Post</Link>
      </li>
    </ul>
  )
}
 
export default Home
```

The example above uses multiple links. Each one maps a path (`href`) to a known page:

-   `/` → `pages/index.js`
-   `/about` → `pages/about.js`
-   `/blog/hello-world` → `pages/blog/[slug].js`

Any `<Link />` in the viewport (initially or through scroll) will be prefetched by default (including the corresponding data) for pages using [Static Generation](../../data-fetching/get-static-props/index.md). The corresponding data for [server-rendered](../../data-fetching/get-server-side-props/index.md) routes is fetched _only when_ the `<Link />` is clicked.

## Linking to dynamic paths[](#linking-to-dynamic-paths)

You can also use interpolation to create the path, which comes in handy for [dynamic route segments](../dynamic-routes/index.md). For example, to show a list of posts which have been passed to the component as a prop:

```
import Link from 'next/link'
 
function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${encodeURIComponent(post.slug)}`}>
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}
 
export default Posts
```

> [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) is used in the example to keep the path utf-8 compatible.

Alternatively, using a URL Object:

```
import Link from 'next/link'
 
function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link
            href={{
              pathname: '/blog/[slug]',
              query: { slug: post.slug },
            }}
          >
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}
 
export default Posts
```

Now, instead of using interpolation to create the path, we use a URL object in `href` where:

-   `pathname` is the name of the page in the `pages` directory. `/blog/[slug]` in this case.
-   `query` is an object with the dynamic segment. `slug` in this case.

## Injecting the router[](#injecting-the-router)

To access the [`router` object](../../../api-reference/functions/use-router/index.md#router-object) in a React component you can use [`useRouter`](../../../api-reference/functions/use-router/index.md) or [`withRouter`](../../../api-reference/functions/use-router/index.md#withrouter).

In general we recommend using [`useRouter`](../../../api-reference/functions/use-router/index.md).

## Imperative Routing[](#imperative-routing)

[`next/link`](../../../api-reference/components/link/index.md) should be able to cover most of your routing needs, but you can also do client-side navigations without it, take a look at the [documentation for `next/router`](../../../api-reference/functions/use-router/index.md).

The following example shows how to do basic page navigations with [`useRouter`](../../../api-reference/functions/use-router/index.md):

```
import { useRouter } from 'next/router'
 
export default function ReadMore() {
  const router = useRouter()
 
  return (
    <button onClick={() => router.push('/about')}>
      Click here to read more
    </button>
  )
}
```

## Shallow Routing[](#shallow-routing)

**Examples**

-   [Shallow Routing](https://github.com/vercel/next.js/tree/canary/examples/with-shallow-routing)

Shallow routing allows you to change the URL without running data fetching methods again, that includes [`getServerSideProps`](../../data-fetching/get-server-side-props/index.md), [`getStaticProps`](../../data-fetching/get-static-props/index.md), and [`getInitialProps`](../../../api-reference/functions/get-initial-props/index.md).

You'll receive the updated `pathname` and the `query` via the [`router` object](../../../api-reference/functions/use-router/index.md#router-object) (added by [`useRouter`](../../../api-reference/functions/use-router/index.md) or [`withRouter`](../../../api-reference/functions/use-router/index.md#withrouter)), without losing state.

To enable shallow routing, set the `shallow` option to `true`. Consider the following example:

```
import { useEffect } from 'react'
import { useRouter } from 'next/router'
 
// Current URL is '/'
function Page() {
  const router = useRouter()
 
  useEffect(() => {
    // Always do navigations after the first render
    router.push('/?counter=10', undefined, { shallow: true })
  }, [])
 
  useEffect(() => {
    // The counter changed!
  }, [router.query.counter])
}
 
export default Page
```

The URL will get updated to `/?counter=10` and the page won't get replaced, only the state of the route is changed.

You can also watch for URL changes via [`componentDidUpdate`](https://react.dev/reference/react/Component#componentdidupdate) as shown below:

```
componentDidUpdate(prevProps) {
  const { pathname, query } = this.props.router
  // verify props have changed to avoid an infinite loop
  if (query.counter !== prevProps.router.query.counter) {
    // fetch data based on the new query
  }
}
```

### Caveats[](#caveats)

Shallow routing **only** works for URL changes in the current page. For example, let's assume we have another page called `pages/about.js`, and you run this:

```
router.push('/?counter=10', '/about?counter=10', { shallow: true })
```

Since that's a new page, it'll unload the current page, load the new one and wait for data fetching even though we asked to do shallow routing.

When shallow routing is used with proxy it will not ensure the new page matches the current page like previously done without proxy. This is due to proxy being able to rewrite dynamically and can't be verified client-side without a data fetch which is skipped with shallow, so a shallow route change must always be treated as shallow.

Was this helpful?
