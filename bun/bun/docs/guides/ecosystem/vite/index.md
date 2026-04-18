---
title: "Build a frontend using Vite and Bun"
source: "https://bun.com/docs/guides/ecosystem/vite"
canonical_url: "https://bun.com/docs/guides/ecosystem/vite"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:06.227Z"
content_hash: "a2205516910ca3295854e39122d7cd30908c98aec7c27aba4b8af7fea6ba3fe0"
menu_path: ["Build a frontend using Vite and Bun"]
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

You can use Vite with Bun, but many projects get faster builds & drop hundreds of dependencies by switching to [HTML imports](/docs/bundler/html-static).

* * *

Vite works out of the box with Bun. Get started with one of Vite’s templates.

terminal

```
bun create vite my-app
```

```
✔ Select a framework: › React
✔ Select a variant: › TypeScript + SWC
Scaffolding project in /path/to/my-app...
```

* * *

Then `cd` into the project directory and install dependencies.

terminal

```
cd my-app
bun install
```

* * *

Start the development server with the `vite` CLI using `bunx`. The `--bun` flag tells Bun to run Vite’s CLI using `bun` instead of `node`; by default Bun respects Vite’s `#!/usr/bin/env node` [shebang line](https://en.wikipedia.org/wiki/Shebang_\(Unix\)).

terminal

```
bunx --bun vite
```

* * *

To simplify this command, update the `"dev"` script in `package.json` to the following.

package.json

```
  "scripts": {
    "dev": "vite", 
    "dev": "bunx --bun vite", 
    "build": "vite build",
    "serve": "vite preview"
  },
  // ...
```

* * *

Now you can start the development server with `bun run dev`.

terminal

```
bun run dev
```

* * *

The following command will build your app for production.

terminal

```
bunx --bun vite build
```

* * *

This is a stripped down guide to get you started with Vite + Bun. For more information, see the [Vite documentation](https://vite.dev/guide/).

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/ecosystem/vite.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/ecosystem/vite>)

[

Run Bun as a daemon with systemd

Previous

](/docs/guides/ecosystem/systemd)[

Bun Redis with Upstash

Next

](/docs/guides/ecosystem/upstash)
