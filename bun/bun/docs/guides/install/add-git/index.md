---
title: "Add a Git dependency"
source: "https://bun.com/docs/guides/install/add-git"
canonical_url: "https://bun.com/docs/guides/install/add-git"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:18.475Z"
content_hash: "5a582534e2ca8c36f9ed490a3091e2e7d613f867f4768048bcc9cd7ced8156c0"
menu_path: ["Add a Git dependency"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/install/add-dev/index.md", "title": "Add a development dependency"}
nav_next: {"path": "bun/bun/docs/guides/install/add-optional/index.md", "title": "Add an optional dependency"}
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

Bun supports directly adding GitHub repositories as dependencies of your project.

terminal

```
bun add github:lodash/lodash
```

* * *

This will add the following line to your `package.json`:

package.json

```
{
  "dependencies": {
    "lodash": "github:lodash/lodash"
  }
}
```

* * *

Bun supports a number of protocols for specifying Git dependencies.

terminal

```
bun add git+https://github.com/lodash/lodash.git
bun add git+ssh://github.com/lodash/lodash.git#4.17.21
bun add git@github.com:lodash/lodash.git
bun add github:colinhacks/zod
```

**Note:** GitHub dependencies download via HTTP tarball when possible for faster installation.

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add-git.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add-git>)

[

Add a peer dependency

Previous

](/docs/guides/install/add-peer)[

Add a tarball dependency

Next

](/docs/guides/install/add-tarball)

