---
title: "Build an app with Next.js and Bun"
source: "https://bun.com/docs/guides/ecosystem/nextjs"
canonical_url: "https://bun.com/docs/guides/ecosystem/nextjs"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:44:56.875Z"
content_hash: "9dea4cd1ed82969dee672fc45bcafc8d9526a78b587bcb103d98882cd9a8f981"
menu_path: ["Build an app with Next.js and Bun"]
section_path: []
nav_prev: {"path": "../neon-serverless-postgres/index.md", "title": "Use Neon's Serverless Postgres with Bun"}
nav_next: {"path": "../nuxt/index.md", "title": "Build an app with Nuxt and Bun"}
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

[Next.js](https://nextjs.org/) is a React framework for building full-stack web applications. It supports server-side rendering, static site generation, API routes, and more. Bun provides fast package installation and can run Next.js development and production servers.

* * *

1

[

](#)

Create a new Next.js app

Use the interactive CLI to create a new Next.js app. This will scaffold a new Next.js project and automatically install dependencies.

terminal

```
bun create next-app@latest my-bun-app
```

2

[

](#)

Start the dev server

Change to the project directory and run the dev server with Bun.

terminal

```
cd my-bun-app
bun --bun run dev
```

This starts the Next.js dev server with Bun’s runtime.Open [`http://localhost:3000`](http://localhost:3000) with your browser to see the result. Any changes you make to `app/page.tsx` will be hot-reloaded in the browser.

3

[

](#)

Update scripts in package.json

Modify the scripts field in your `package.json` by prefixing the Next.js CLI commands with `bun --bun`. This ensures that Bun executes the Next.js CLI for common tasks like `dev`, `build`, and `start`.

package.json

```
{
  "scripts": {
    "dev": "bun --bun next dev", 
    "build": "bun --bun next build", 
    "start": "bun --bun next start", 
  }
}
```

* * *

## 

[​

](#hosting)

Hosting

Next.js applications on Bun can be deployed to various platforms.

* * *

## 

[​

](#templates)

Templates

![bun-nextjs-basic](https://mintcdn.com/bun-1dd33a4e/M5IN-LfyV8DoQVZm/images/templates/bun-nextjs-basic.png?fit=max&auto=format&n=M5IN-LfyV8DoQVZm&q=85&s=2bc9edb73c9c49d88e8ced9e2158f75a)

![bun-nextjs-todo](https://mintcdn.com/bun-1dd33a4e/M5IN-LfyV8DoQVZm/images/templates/bun-nextjs-todo.png?fit=max&auto=format&n=M5IN-LfyV8DoQVZm&q=85&s=e8f398caf487c6b925a53025c42f4dab)

* * *

[→ See Next.js’s official documentation](https://nextjs.org/docs) for more information on building and deploying Next.js applications.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/nextjs.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/nextjs>)

[

Use Neon's Serverless Postgres with Bun

Previous

](/docs/guides/ecosystem/neon-serverless-postgres)[

Build an app with Nuxt and Bun

Next

](/docs/guides/ecosystem/nuxt)
