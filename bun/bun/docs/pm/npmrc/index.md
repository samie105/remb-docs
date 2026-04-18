---
title: ".npmrc support"
source: "https://bun.com/docs/pm/npmrc"
canonical_url: "https://bun.com/docs/pm/npmrc"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:58:03.197Z"
content_hash: "e10a78802637e7f086bafd339cbacc848b445ecf0e06df03b1f8e18d23243688"
menu_path: [".npmrc support"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/overrides/index.md", "title": "Overrides and resolutions"}
nav_next: {"path": "bun/bun/docs/pm/scopes-registries/index.md", "title": "Scopes and registries"}
---

# set an auth token for the registry
# ${...} is a placeholder for environment variables
//http://localhost:4873/:_authToken=${NPM_TOKEN}

# or you could set a username and password
# note that the password is base64 encoded
//http://localhost:4873/:username=myusername

//http://localhost:4873/:_password=${NPM_PASSWORD}

# or use _auth, which is your username and password
# combined into a single string, which is then base 64 encoded
//http://localhost:4873/:_auth=${NPM_AUTH}
```

The following options are supported:

*   `_authToken`
*   `username`
*   `_password` (base64 encoded password)
*   `_auth` (base64 encoded username:password, e.g. `btoa(username + ":" + password)`)
*   `email`

The equivalent `bunfig.toml` option is to add a key in [`install.scopes`](bun/bun/docs/runtime/bunfig/index.md#install-registry):

bunfig.toml

```
[install.scopes]
myorg = { url = "http://localhost:4873/", username = "myusername", password = "$NPM_PASSWORD" }
```

### `link-workspace-packages`: Control workspace package installation

Controls how workspace packages are installed when available locally:

.npmrc

```
link-workspace-packages=true
```

The equivalent `bunfig.toml` option is [`install.linkWorkspacePackages`](bun/bun/docs/runtime/bunfig/index.md#install-linkworkspacepackages):

bunfig.toml

```
[install]
linkWorkspacePackages = true
```

### `save-exact`: Save exact versions

Always saves exact versions without the `^` prefix:

.npmrc

```
save-exact=true
```

The equivalent `bunfig.toml` option is [`install.exact`](bun/bun/docs/runtime/bunfig/index.md#install-exact):

bunfig.toml

```
[install]
exact = true
```

### `ignore-scripts`: Skip lifecycle scripts

Prevents running lifecycle scripts during installation:

.npmrc

```
ignore-scripts=true
```

This is equivalent to using the `--ignore-scripts` flag with `bun install`.

### `dry-run`: Preview changes without installing

Shows what would be installed without actually installing:

.npmrc

```
dry-run=true
```

The equivalent `bunfig.toml` option is [`install.dryRun`](bun/bun/docs/runtime/bunfig/index.md#install-dryrun):

bunfig.toml

```
[install]
dryRun = true
```

### `cache`: Configure cache directory

Set the cache directory path, or disable caching:

.npmrc

```
# set a custom cache directory
cache=/path/to/cache

# or disable caching
cache=false
```

The equivalent `bunfig.toml` option is [`install.cache`](bun/bun/docs/runtime/bunfig/index.md#install-cache):

bunfig.toml

```
[install.cache]
# set a custom cache directory
dir = "/path/to/cache"

# or disable caching
disable = true
```

### `ca` and `cafile`: Configure CA certificates

Configure custom CA certificates for registry connections:

.npmrc

```
# single CA certificate
ca="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"

# multiple CA certificates
ca[]="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
ca[]="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"

# or specify a path to a CA file
cafile=/path/to/ca-bundle.crt
```

### `omit` and `include`: Control dependency types

Control which dependency types are installed:

.npmrc

```
# omit dev dependencies
omit=dev

# omit multiple types
omit[]=dev
omit[]=optional

# include specific types (overrides omit)
include=dev
```

Valid values: `dev`, `peer`, `optional`

### `install-strategy` and `node-linker`: Installation strategy

Control how packages are installed in `node_modules`. Bun supports two different configuration options for compatibility with different package managers. **npm’s `install-strategy`:**

.npmrc

```
# flat node_modules structure (default)
install-strategy=hoisted

# symlinked structure
install-strategy=linked
```

**pnpm/yarn’s `node-linker`:** The `node-linker` option controls the installation mode. Bun supports values from both pnpm and yarn:

Value

Description

Accepted by

`isolated`

Symlinked structure with isolated dependencies

pnpm

`hoisted`

Flat node\_modules structure

pnpm

`pnpm`

Symlinked structure (same as `isolated`)

yarn

`node-modules`

Flat node\_modules structure (same as `hoisted`)

yarn

.npmrc

```
# symlinked/isolated mode
node-linker=isolated
node-linker=pnpm

# flat/hoisted mode
node-linker=hoisted
node-linker=node-modules
```

### `public-hoist-pattern` and `hoist-pattern`: Control hoisting

Control which packages are hoisted to the root `node_modules`:

.npmrc

```
# packages matching this pattern will be hoisted to the root
public-hoist-pattern=*eslint*

# multiple patterns
public-hoist-pattern[]=*eslint*
public-hoist-pattern[]=*prettier*

# control general hoisting behavior
hoist-pattern=*
```

