---
title: "Overrides and resolutions"
source: "https://bun.com/docs/pm/overrides"
canonical_url: "https://bun.com/docs/pm/overrides"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:01.526Z"
content_hash: "fa5279b29e05281ce1996a4cf6324a1cae0c8250363cf9ec9291e9d630950ec7"
menu_path: ["Overrides and resolutions"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/npmrc/index.md", "title": ".npmrc support"}
nav_next: {"path": "bun/bun/docs/pm/scopes-registries/index.md", "title": "Scopes and registries"}
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

Bun supports npm’s `"overrides"` and Yarn’s `"resolutions"` in `package.json`. These are mechanisms for specifying a version range for _metadependencies_—the dependencies of your dependencies.

package.json

```
{
  "name": "my-app",
  "dependencies": {
    "foo": "^2.0.0"
  },
  "overrides": { 
    "bar": "~4.4.0"
  } 
}
```

By default, Bun will install the latest version of all dependencies and metadependencies, according to the ranges specified in each package’s `package.json`. Let’s say you have a project with one dependency, `foo`, which in turn has a dependency on `bar`. This means `bar` is a _metadependency_ of our project.

package.json

```
{
  "name": "my-app",
  "dependencies": {
    "foo": "^2.0.0"
  }
}
```

When you run `bun install`, Bun will install the latest versions of each package.

tree layout of node\_modules

```
node_modules
├── foo@1.2.3
└── bar@4.5.6
```

But what if a security vulnerability was introduced in `bar@4.5.6`? We may want a way to pin `bar` to an older version that doesn’t have the vulnerability. This is where `"overrides"`/`"resolutions"` come in.

* * *

## 

[​

](#overrides)

`"overrides"`

Add `bar` to the `"overrides"` field in `package.json`. Bun will defer to the specified version range when determining which version of `bar` to install, whether it’s a dependency or a metadependency.

Bun currently only supports top-level `"overrides"`. [Nested overrides](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#overrides) are not supported.

package.json

```
{
  "name": "my-app",
  "dependencies": {
    "foo": "^2.0.0"
  },
  "overrides": { 
    "bar": "~4.4.0"
  } 
}
```

## 

[​

](#resolutions)

`"resolutions"`

The syntax is similar for `"resolutions"`, which is Yarn’s alternative to `"overrides"`. Bun supports this feature to make migration from Yarn easier. As with `"overrides"`, _nested resolutions_ are not currently supported.

package.json

```
{
  "name": "my-app",
  "dependencies": {
    "foo": "^2.0.0"
  },
  "resolutions": { 
    "bar": "~4.4.0"
  } 
}
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/overrides.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/overrides>)

[

Scopes and registries

Previous

](/docs/pm/scopes-registries)[

Security Scanner API

Next

](/docs/pm/security-scanner-api)
