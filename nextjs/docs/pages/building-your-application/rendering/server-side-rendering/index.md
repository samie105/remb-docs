---
title: "Server-side Rendering (SSR)"
source: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:23:10.660Z"
content_hash: "c1d6e0eec60fcae6233331d3b2546ea0c7bb94d197c1c33fbb1e4d3de5d5da7a"
menu_path: ["Server-side Rendering (SSR)"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/building-your-application/routing/custom-error/index.md", "title": "Custom Errors"}
nav_next: {"path": "nextjs/docs/pages/building-your-application/rendering/static-site-generation/index.md", "title": "Static Site Generation (SSG)"}
---

# Server-side Rendering (SSR)

Last updated April 15, 2026

> Also referred to as "SSR" or "Dynamic Rendering".

If a page uses **Server-side Rendering**, the page HTML is generated on **each request**.

To use Server-side Rendering for a page, you need to `export` an `async` function called `getServerSideProps`. This function will be called by the server on every request.

For example, suppose that your page needs to prerender frequently updated data (fetched from an external API). You can write `getServerSideProps` which fetches this data and passes it to `Page` like below:

```
export default function Page({ data }) {
  // Render data...
}
 
// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()
 
  // Pass data to the page via props
  return { props: { data } }
}
```

As you can see, `getServerSideProps` is similar to `getStaticProps`, but the difference is that `getServerSideProps` is run on every request instead of on build time.

To learn more about how `getServerSideProps` works, check out our [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/get-server-side-props).

Was this helpful?

supported.

Send




