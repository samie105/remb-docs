---
title: "Scopes and registries"
source: "https://bun.com/docs/pm/scopes-registries"
canonical_url: "https://bun.com/docs/pm/scopes-registries"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:05.151Z"
content_hash: "2280bb4ccf22d1255618172b817a2d3d6e96ee3db387ce3cb416ad67ae6bddf2"
menu_path: ["Scopes and registries"]
section_path: []
---
*   [.npmrc](#npmrc)

The default registry is `registry.npmjs.org`. This can be globally configured in `bunfig.toml`:

bunfig.toml

```
[install]
# set default registry as a string
registry = "https://registry.npmjs.org"
# set a token
registry = { url = "https://registry.npmjs.org", token = "123456" }
# set a username/password
registry = "https://username:password@registry.npmjs.org"
```

To configure a private registry scoped to a particular organization:

bunfig.toml

```
[install.scopes]
# registry as string
"@myorg1" = "https://username:password@registry.myorg.com/"

# registry with username/password
# you can reference environment variables
"@myorg2" = { username = "myusername", password = "$NPM_PASS", url = "https://registry.myorg.com/" }

# registry with token
"@myorg3" = { token = "$npm_token", url = "https://registry.myorg.com/" }
```

### `.npmrc`

Bun also reads `.npmrc` files, [learn more](https://bun.com/docs/pm/npmrc).

Was this page helpful?
