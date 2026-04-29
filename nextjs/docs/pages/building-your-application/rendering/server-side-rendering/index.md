---
title: "Server-side Rendering (SSR)"
source: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
canonical_url: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:22:28.823Z"
content_hash: "3d1f0e677c67f533d94d4827b18716da47d8fac98063136ba4778c1d2ec9c013"
menu_path: ["Server-side Rendering (SSR)"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../../routing/custom-error/index.md", "title": "Custom Errors"}
nav_next: {"path": "../static-site-generation/index.md", "title": "Static Site Generation (SSG)"}
---

# Server-side Rendering (SSR)

Last updated April 23, 2026

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
