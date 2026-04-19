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
---
[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

[Vercel](https://vercel.com/) is a cloud platform that lets you build, deploy, and scale your apps.

The Bun runtime is in Beta; certain features (e.g., automatic source maps, byte-code caching, metrics on `node:http/https`) are not yet supported.

`Bun.serve` is currently not supported on Vercel Functions. Use Bun with frameworks supported by Vercel, like Next.js, Express, Hono, or Nitro.

* * *

1

[

](#)

Configure Bun in vercel.json

To enable the Bun runtime for your Functions, add a `bunVersion` field in your `vercel.json` file:

vercel.json

```
{
	"bunVersion": "1.x"
}
```

Vercel automatically detects this configuration and runs your application on Bun. The value has to be `"1.x"`, Vercel handles the minor version internally.For best results, match your local Bun version with the version used by Vercel.

2

[

](#)

Next.js configuration

If you’re deploying a **Next.js** project (including ISR), update your `package.json` scripts to use the Bun runtime:

package.json

```
{
	"scripts": {
		"dev": "bun --bun next dev", 
		"build": "bun --bun next build"
	}
}
```

The `--bun` flag runs the Next.js CLI under Bun. Bundling (via Turbopack or Webpack) remains unchanged, but all commands execute within the Bun runtime.

This ensures both local development and builds use Bun.

3

[

](#)

Deploy your app

Connect your repository to Vercel, or deploy from the CLI:

terminal

```
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

](/docs/guides)[

Deploy a Bun application on Railway

Next

](/docs/guides/deployment/railway)
