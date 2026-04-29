---
title: "Configuring a monorepo using workspaces"
source: "https://bun.com/docs/guides/install/workspaces"
canonical_url: "https://bun.com/docs/guides/install/workspaces"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:24.119Z"
content_hash: "ef430a2ae5c0f12c153b124f140991297501458f112e291b5318bedb898c9a45"
menu_path: ["Configuring a monorepo using workspaces"]
section_path: []
nav_prev: {"path": "../trusted/index.md", "title": "Add a trusted dependency"}
nav_next: {"path": "../yarnlock/index.md", "title": "Generate a yarn-compatible lockfile"}
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

Bun’s package manager supports npm `"workspaces"`. This allows you to split a codebase into multiple distinct “packages” that live in the same repository, can depend on each other, and (when possible) share a `node_modules` directory. Clone [this sample project](https://github.com/colinhacks/bun-workspaces) to experiment with workspaces.

* * *

The root `package.json` should not contain any `"dependencies"`, `"devDependencies"`, etc. Each individual package should be self-contained and declare its own dependencies. Similarly, it’s conventional to declare `"private": true` to avoid accidentally publishing the root package to `npm`.

package.json

```
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": ["packages/*"]
}
```

* * *

It’s common to place all packages in a `packages` directory. The `"workspaces"` field in package.json supports glob patterns, so you can use `packages/*` to indicate that each subdirectory of `packages` should be considered separate _package_ (also known as a workspace).

File Tree

```
.
├── package.json
├── node_modules
└── packages
    ├── stuff-a
    │   └── package.json
    └── stuff-b
        └── package.json
```

* * *

To add dependencies between workspaces, use the `"workspace:*"` syntax. Here we’re adding `stuff-a` as a dependency of `stuff-b`.

packages/stuff-b/package.json

```
{
  "name": "stuff-b",
  "dependencies": {
    "stuff-a": "workspace:*"
  }
}
```

* * *

Once added, run `bun install` from the project root to install dependencies for all workspaces.

terminal

```
bun install
```

* * *

To add npm dependencies to a particular workspace, `cd` to the appropriate directory and run `bun add` commands as you would normally. Bun will detect that you are in a workspace and hoist the dependency as needed.

terminal

```
cd packages/stuff-a
bun add zod
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/workspaces.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/workspaces>)

[

Install a package under a different name

Previous

](/docs/guides/install/npm-alias)[

Override the default npm registry for bun install

Next

](/docs/guides/install/custom-registry)
