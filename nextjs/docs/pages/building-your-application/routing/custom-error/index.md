---
title: "Custom Errors"
source: "https://nextjs.org/docs/pages/building-your-application/routing/custom-error"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/routing/custom-error"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:23:26.279Z"
content_hash: "3226756541068e2b867342f76614335b81b2c01deeb73318fe9b2fcf477ff602"
menu_path: ["Custom Errors"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/api-routes/index.md", "title": "API Routes"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/rendering/server-side-rendering/index.md", "title": "Server-side Rendering (SSR)"}
---

# Custom Errors

Last updated April 15, 2026

## 404 Page[](#404-page)

A 404 page may be accessed very often. Server-rendering an error page for every visit increases the load of the Next.js server. This can result in increased costs and slow experiences.

To avoid the above pitfalls, Next.js provides a static 404 page by default without having to add any additional files.

### Customizing The 404 Page[](#customizing-the-404-page)

To create a custom 404 page you can create a `pages/404.js` file. This file is statically generated at build time.

pages/404.js

```
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>
}
```

> **Good to know**: You can use [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props) inside this page if you need to fetch data at build time.

## 500 Page[](#500-page)

Server-rendering an error page for every visit adds complexity to responding to errors. To help users get responses to errors as fast as possible, Next.js provides a static 500 page by default without having to add any additional files.

### Customizing The 500 Page[](#customizing-the-500-page)

To customize the 500 page you can create a `pages/500.js` file. This file is statically generated at build time.

pages/500.js

```
export default function Custom500() {
  return <h1>500 - Server-side error occurred</h1>
}
```

> **Good to know**: You can use [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props) inside this page if you need to fetch data at build time.

### More Advanced Error Page Customizing[](#more-advanced-error-page-customizing)

500 errors are handled both client-side and server-side by the `Error` component. If you wish to override it, define the file `pages/_error.js` and add the following code:

```
function Error({ statusCode }) {
  return (
    <p>
      {statusCode
        ? `An error ${statusCode} occurred on server`
        : 'An error occurred on client'}
    </p>
  )
}
 
Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404
  return { statusCode }
}
 
export default Error
```

> `pages/_error.js` is only used in production. In development you’ll get an error with the call stack to know where the error originated from.

### Reusing the built-in error page[](#reusing-the-built-in-error-page)

If you want to render the built-in error page you can by importing the `Error` component:

```
import Error from 'next/error'
 
export async function getServerSideProps() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const errorCode = res.ok ? false : res.status
  const json = await res.json()
 
  return {
    props: { errorCode, stars: json.stargazers_count },
  }
}
 
export default function Page({ errorCode, stars }) {
  if (errorCode) {
    return <Error statusCode={errorCode} />
  }
 
  return <div>Next stars: {stars}</div>
}
```

The `Error` component also takes `title` as a property if you want to pass in a text message along with a `statusCode`.

If you have a custom `Error` component be sure to import that one instead. `next/error` exports the default component used by Next.js.

### Caveats[](#caveats)

*   `Error` does not currently support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props).
*   `_error`, like `_app`, is a reserved pathname. `_error` is used to define the customized layouts and behaviors of the error pages. `/_error` will render 404 when accessed directly via [routing](/docs/pages/building-your-application/routing) or rendering in a [custom server](/docs/pages/guides/custom-server).

Was this helpful?

supported.

Send




