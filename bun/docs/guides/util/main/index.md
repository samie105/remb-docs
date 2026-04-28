---
title: "Get the absolute path to the current entrypoint"
source: "https://bun.com/docs/guides/util/main"
canonical_url: "https://bun.com/docs/guides/util/main"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:09.773Z"
content_hash: "218a5e8862df1ac968594a3cf46e5016c7e6998a89b346fe097db80190227ff4"
menu_path: ["Get the absolute path to the current entrypoint"]
section_path: []
nav_prev: {"path": "bun/docs/guides/util/javascript-uuid/index.md", "title": "Generate a UUID"}
nav_next: {"path": "bun/docs/guides/util/path-to-file-url/index.md", "title": "Convert an absolute path to a file URL"}
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

The `Bun.main` property contains the absolute path to the current entrypoint.

```
console.log(Bun.main);
```

* * *

The printed path corresponds to the file that is executed with `bun run`.

terminal

```
bun run index.ts
```

```
/path/to/index.ts
```

terminal

```
bun run foo.ts
```

```
/path/to/foo.ts
```

* * *

See [Docs > API > Utils](/docs/runtime/utils) for more useful utilities.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/util/main.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/util/main>)

[

Check if the current file is the entrypoint

Previous

](/docs/guides/util/entrypoint)[

Build an app with Astro and Bun

Next

](/docs/guides/ecosystem/astro)
