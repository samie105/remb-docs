---
title: "Add a tarball dependency"
source: "https://bun.com/docs/guides/install/add-tarball"
canonical_url: "https://bun.com/docs/guides/install/add-tarball"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:33.229Z"
content_hash: "cea822d6ecd8466a2389fb5a808b04db3557ce3babed248c2e6bf3c7ad024b72"
menu_path: ["Add a tarball dependency"]
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

Bun’s package manager can install any publicly available tarball URL as a dependency of your project.

terminal

```
bun add zod@https://registry.npmjs.org/zod/-/zod-3.21.4.tgz
```

* * *

Running this command will download, extract, and install the tarball to your project’s `node_modules` directory. It will also add the following line to your `package.json`:

package.json

```
{
  "dependencies": {
    "zod": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz"
  }
}
```

* * *

The package `"zod"` can now be imported as usual.

```
import { z } from "zod";
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/add-tarball.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/add-tarball>)

[

Add a Git dependency

Previous

](/docs/guides/install/add-git)[

Install a package under a different name

Next

](/docs/guides/install/npm-alias)
