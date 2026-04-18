---
title: "Override the default npm registry for bun install"
source: "https://bun.com/docs/guides/install/custom-registry"
canonical_url: "https://bun.com/docs/guides/install/custom-registry"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:46.472Z"
content_hash: "80d9871ae5d0efbf90b9bb2d644ef7ac299dcdb17b9e8da927fab1684244d2ca"
menu_path: ["Override the default npm registry for bun install"]
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

The default registry is `registry.npmjs.org`. This can be globally configured in `bunfig.toml`.

bunfig.toml

```
[install]
# set default registry as a string
registry = "https://registry.npmjs.org"

# if needed, set a token
registry = { url = "https://registry.npmjs.org", token = "123456" }

# if needed, set a username/password
registry = "https://usertitle:password@registry.npmjs.org"
```

* * *

Your `bunfig.toml` can reference environment variables. Bun automatically loads environment variables from `.env.local`, `.env.[NODE_ENV]`, and `.env`. See [Docs > Environment variables](/docs/runtime/environment-variables) for more information.

bunfig.toml

```
[install]
registry = { url = "https://registry.npmjs.org", token = "$npm_token" }
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/custom-registry.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/custom-registry>)

[

Configuring a monorepo using workspaces

Previous

](/docs/guides/install/workspaces)[

Configure a private registry for an organization scope with bun install

Next

](/docs/guides/install/registry-scope)
