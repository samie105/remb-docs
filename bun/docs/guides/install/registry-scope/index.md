---
title: "Configure a private registry for an organization scope with bun install"
source: "https://bun.com/docs/guides/install/registry-scope"
canonical_url: "https://bun.com/docs/guides/install/registry-scope"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:14.405Z"
content_hash: "63a65bba32195b150636d3fcd7cbca672cdcfc48a42226bfa097b8a71ff7a1b3"
menu_path: ["Configure a private registry for an organization scope with bun install"]
section_path: []
nav_prev: {"path": "bun/docs/guides/install/npm-alias/index.md", "title": "Install a package under a different name"}
nav_next: {"path": "bun/docs/guides/install/trusted/index.md", "title": "Add a trusted dependency"}
---

# as a string
"@myorg1" = "https://usertitle:password@registry.myorg.com/"

# as an object with username/password
# you can reference environment variables
"@myorg2" = {
  username = "myusername",
  password = "$npm_pass",
  url = "https://registry.myorg.com/"
}

# as an object with token
"@myorg3" = { token = "$npm_token", url = "https://registry.myorg.com/" }

```

* * *

Your `bunfig.toml` can reference environment variables. Bun automatically loads environment variables from `.env.local`, `.env.[NODE_ENV]`, and `.env`. See [Docs > Environment variables](../../../runtime/environment-variables/index.md) for more information.

bunfig.toml

```
[install.scopes]
"@myorg3" = { token = "$npm_token", url = "https://registry.myorg.com/" }
```

* * *

See [Docs > Package manager](../../../pm/cli/install/index.md) for complete documentation of Bun’s package manager.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/install/registry-scope.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/install/registry-scope>)

[

Override the default npm registry for bun install

Previous

](../custom-registry/index.md)[

Using bun install with an Azure Artifacts npm registry

Next

](../azure-artifacts/index.md)
