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
nav_prev: {"path": "bun/bun/docs/guides/install/cicd/index.md", "title": "Install dependencies with Bun in GitHub Actions"}
nav_next: {"path": "bun/bun/docs/guides/install/from-npm-install-to-bun-install/index.md", "title": "Migrate from npm install to bun install"}
---

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

