---
title: "Deploy a Bun application on Vercel"
source: "https://bun.com/docs/guides/deployment/vercel"
canonical_url: "https://bun.com/docs/guides/deployment/vercel"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:23.059Z"
content_hash: "3e7e56da82faeb67d0e49fbe5a5fccc4635450ee2e70aaa4b212827cf0a1d47e"
menu_path: ["Deploy a Bun application on Vercel"]
section_path: []
nav_prev: {"path": "bun/docs/guides/deployment/render/index.md", "title": "Deploy a Bun application on Render"}
nav_next: {"path": "bun/docs/guides/ecosystem/astro/index.md", "title": "Build an app with Astro and Bun"}
---

# Using bunx (no global install)
bunx vercel login
bunx vercel deploy
```

Or install the Vercel CLI globally:

terminal

```
bun i -g vercel
vercel login
vercel deploy
```

[Learn more in the Vercel Deploy CLI documentation →](https://vercel.com/docs/cli/deploy)

4

[

](#)

Verify the runtime

To confirm your deployment uses Bun, log the Bun version:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
console.log("runtime", process.versions.bun);
```

```
runtime 1.3.3
```

[See the Vercel Bun Runtime documentation for feature support →](https://vercel.com/docs/functions/runtimes/bun#feature-support)

* * *

*   [Fluid compute](https://vercel.com/docs/fluid-compute): Both Bun and Node.js runtimes run on Fluid compute and support the same core Vercel Functions features.
*   [Middleware](https://vercel.com/docs/routing-middleware): To run Routing Middleware with Bun, set the runtime to `nodejs`:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)middleware.ts

```
export const config = { runtime: "nodejs" }; 
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/deployment/vercel.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/deployment/vercel>)

[

Guides

Previous

](../../index.md)[

Deploy a Bun application on Railway

Next

](../railway/index.md)
