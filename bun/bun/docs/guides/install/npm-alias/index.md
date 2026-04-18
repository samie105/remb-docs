---
title: "Install a package under a different name"
source: "https://bun.com/docs/guides/install/npm-alias"
canonical_url: "https://bun.com/docs/guides/install/npm-alias"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:09.861Z"
content_hash: "93d4196e9722c4b26034bb92cac96a430876e2e003a0796c281dc08c99af7a72"
menu_path: ["Install a package under a different name"]
section_path: []
nav_prev: {"path": "bun/bun/docs/guides/install/jfrog-artifactory/index.md", "title": "Using bun install with Artifactory"}
nav_next: {"path": "bun/bun/docs/guides/install/registry-scope/index.md", "title": "Configure a private registry for an organization scope with bun install"}
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

To install an npm package under an alias:

terminal

```
bun add my-custom-name@npm:zod
```

* * *

The `zod` package can now be imported as `my-custom-name`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)index.ts

```
import { z } from "my-custom-name";

z.string();
```

* * *

See [Docs > Package manager](/docs/pm/cli/install) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/npm-alias.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/npm-alias>)

[

Add a tarball dependency

Previous

](/docs/guides/install/add-tarball)[

Configuring a monorepo using workspaces

Next

](/docs/guides/install/workspaces)
