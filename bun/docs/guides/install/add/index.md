---
title: "Add a dependency"
source: "https://bun.com/docs/guides/install/add"
canonical_url: "https://bun.com/docs/guides/install/add"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:00.005Z"
content_hash: "021b24c20454045ffb7200df1daa259917bd05d450a9642bfddc91efcee81fb0"
menu_path: ["Add a dependency"]
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

To add an npm package as a dependency, use `bun add`.

terminal

```
bun add zod
```

* * *

This will add the package to `dependencies` in `package.json`. By default, the `^` range specifier will be used, to indicate that any future minor or patch versions are acceptable.

package.json

```
{
  "dependencies": {
    "zod": "^3.0.0"
  }
}
```

* * *

To “pin” to an exact version of the package, use `--exact`. This will add the package to `dependencies` without the `^`, pinning your project to the exact version you installed.

terminal

```
bun add zod --exact
```

* * *

To specify an exact version or a tag:

terminal

```
bun add zod@3.0.0
bun add zod@next
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add>)

[

Read environment variables

Previous

](/docs/guides/runtime/read-env)[

Add a development dependency

Next

](/docs/guides/install/add-dev)
