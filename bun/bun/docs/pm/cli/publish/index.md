---
title: "bun publish"
source: "https://bun.com/docs/pm/cli/publish"
canonical_url: "https://bun.com/docs/pm/cli/publish"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:39.906Z"
content_hash: "0c8f677481df6437454bced88ef90c2ac6872ccfce385628bd2be81c2d67cf2e"
menu_path: ["bun publish"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/remove/index.md", "title": "bun remove"}
nav_next: {"path": "bun/bun/docs/pm/cli/update/index.md", "title": "bun update"}
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

`bun publish` will automatically pack your package into a tarball, strip catalog and workspace protocols from the `package.json` (resolving versions if necessary), and publish to the registry specified in your configuration files. Both `bunfig.toml` and `.npmrc` files are supported.

terminal

```
## Publishing the package from the current working directory
bun publish
```

```
bun publish v1.3.3 (ca7428e9)

packed 203B package.json
packed 224B README.md
packed 30B index.ts
packed 0.64KB tsconfig.json

Total files: 4
Shasum: 79e2b4377b63f4de38dc7ea6e5e9dbee08311a69
Integrity: sha512-6QSNlDdSwyG/+[...]X6wXHriDWr6fA==
Unpacked size: 1.1KB
Packed size: 0.76KB
Tag: latest
Access: default
Registry: http://localhost:4873/

 + publish-1@1.0.0
```

Alternatively, you can pack and publish your package separately by using `bun pm pack` followed by `bun publish` with the path to the output tarball.

terminal

```
bun pm pack
...
bun publish ./package.tgz
```

`bun publish` will not run lifecycle scripts (`prepublishOnly/prepack/prepare/postpack/publish/postpublish`) if a tarball path is provided. Scripts will only be run if the package is packed by `bun publish`.

### 

[​

](#access)

`--access`

The `--access` flag can be used to set the access level of the package being published. The access level can be one of `public` or `restricted`. Unscoped packages are always public, and attempting to publish an unscoped package with `--access restricted` will result in an error.

terminal

```
bun publish --access public
```

`--access` can also be set in the `publishConfig` field of your `package.json`.

package.json

```
{
  "publishConfig": {
    "access": "restricted"
  }
}
```

### 

[​

](#tag)

`--tag`

Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

terminal

```
bun publish --tag alpha
```

`--tag` can also be set in the `publishConfig` field of your `package.json`.

package.json

```
{
  "publishConfig": {
    "tag": "next"
  }
}
```

### 

[​

](#dry-run)

`--dry-run`

The `--dry-run` flag can be used to simulate the publish process without actually publishing the package. This is useful for verifying the contents of the published package without actually publishing the package.

terminal

```
bun publish --dry-run
```

### 

[​

](#tolerate-republish)

`--tolerate-republish`

Exit with code 0 instead of 1 if the package version already exists. Useful in CI/CD where jobs may be re-run.

terminal

```
bun publish --tolerate-republish
```

### 

[​

](#gzip-level)

`--gzip-level`

Specify the level of gzip compression to use when packing the package. Only applies to `bun publish` without a tarball path argument. Values range from `0` to `9` (default is `9`).

### 

[​

](#auth-type)

`--auth-type`

If you have 2FA enabled for your npm account, `bun publish` will prompt you for a one-time password. This can be done through a browser or the CLI. The `--auth-type` flag can be used to tell the npm registry which method you prefer. The possible values are `web` and `legacy`, with `web` being the default.

terminal

```
bun publish --auth-type legacy
...
This operation requires a one-time password.
Enter OTP: 123456
...
```

### 

[​

](#otp)

`--otp`

Provide a one-time password directly to the CLI. If the password is valid, this will skip the extra prompt for a one-time password before publishing. Example usage:

terminal

```
bun publish --otp 123456
```

`bun publish` respects the `NPM_CONFIG_TOKEN` environment variable which can be used when publishing in github actions or automated workflows.

* * *

## 

[​

](#cli-usage)

CLI Usage

terminal

```
bun publish dist
```

### 

[​

](#publishing-options)

Publishing Options

[​

](#param-access)

\--access

string

The `--access` flag can be used to set the access level of the package being published. The access level can be one of `public` or `restricted`. Unscoped packages are always public, and attempting to publish an unscoped package with `--access restricted` will result in an error.

terminal

```
bun publish --access public
```

`--access` can also be set in the `publishConfig` field of your `package.json`.

package.json

```
{
  "publishConfig": {
    "access": "restricted"
  }
}
```

[​

](#param-tag)

\--tag

string

default:"latest"

Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

terminal

```
bun publish --tag alpha
```

`--tag` can also be set in the `publishConfig` field of your `package.json`.

package.json

```
{
  "publishConfig": {
    "tag": "next"
  }
}
```

[​

](#param-dry-run-val)

\--dry-run=<val>

string

The `--dry-run` flag can be used to simulate the publish process without actually publishing the package. This is useful for verifying the contents of the published package without actually publishing the package.

```
bun publish --dry-run
```

[​

](#param-gzip-level)

\--gzip-level

string

default:"9"

Specify the level of gzip compression to use when packing the package. Only applies to `bun publish` without a tarball path argument. Values range from `0` to `9` (default is `9`).

[​

](#param-auth-type)

\--auth-type

string

default:"web"

If you have 2FA enabled for your npm account, `bun publish` will prompt you for a one-time password. This can be done through a browser or the CLI. The `--auth-type` flag can be used to tell the npm registry which method you prefer. The possible values are `web` and `legacy`, with `web` being the default.

terminal

```
bun publish --auth-type legacy
...
This operation requires a one-time password.
Enter OTP: 123456
...
```

[​

](#param-otp)

\--otp

string

default:"web"

Provide a one-time password directly to the CLI. If the password is valid, this will skip the extra prompt for a one-time password before publishing. Example usage:

terminal

```
bun publish --otp 123456
```

`bun publish` respects the `NPM_CONFIG_TOKEN` environment variable which can be used when publishing in github actions or automated workflows.

### 

[​

](#registry-configuration)

Registry Configuration

#### 

[​

](#custom-registry)

Custom Registry

[​

](#param-registry)

\--registry

string

Specify registry URL, overriding .npmrc and bunfig.toml

```
bun publish --registry https://my-private-registry.com
```

#### 

[​

](#ssl-certificates)

SSL Certificates

[​

](#param-ca)

\--ca

string

Provide Certificate Authority signing certificate

[​

](#param-cafile)

\--cafile

string

Path to Certificate Authority certificate file

```
bun publish --ca "-----BEGIN CERTIFICATE-----..."
```

### 

[​

](#publishing-options-2)

Publishing Options

#### 

[​

](#dependency-management)

Dependency Management

[​

](#param-p-production)

\-p, --production

boolean

Don’t install devDependencies

[​

](#param-omit)

\--omit

string

Exclude dependency types: `dev`, `optional`, or `peer`

[​

](#param-f-force)

\-f, --force

boolean

Always request the latest versions from the registry & reinstall all dependencies

#### 

[​

](#script-control)

Script Control

[​

](#param-ignore-scripts)

\--ignore-scripts

boolean

Skip lifecycle scripts during packing and publishing

[​

](#param-trust)

\--trust

boolean

Add packages to trustedDependencies and run their scripts

**Lifecycle Scripts** — When providing a pre-built tarball, lifecycle scripts (prepublishOnly, prepack, etc.) are not executed. Scripts only run when Bun packs the package itself.

#### 

[​

](#file-management)

File Management

[​

](#param-no-save)

\--no-save

boolean

Don’t update package.json or lockfile

[​

](#param-frozen-lockfile)

\--frozen-lockfile

boolean

Disallow changes to lockfile

[​

](#param-yarn)

\--yarn

boolean

Generate yarn.lock file (yarn v1 compatible)

#### 

[​

](#performance)

Performance

[​

](#param-backend)

\--backend

string

Platform optimizations: `clonefile` (default), `hardlink`, `symlink`, or `copyfile`

[​

](#param-network-concurrency)

\--network-concurrency

number

default:"48"

Maximum concurrent network requests

[​

](#param-concurrent-scripts)

\--concurrent-scripts

number

default:"5"

Maximum concurrent lifecycle scripts

#### 

[​

](#output-control)

Output Control

[​

](#param-silent)

\--silent

boolean

Suppress all output

[​

](#param-verbose)

\--verbose

boolean

Show detailed logging

[​

](#param-no-progress)

\--no-progress

boolean

Hide progress bar

[​

](#param-no-summary)

\--no-summary

boolean

Don’t print publish summary

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/publish.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/publish>)

[

bunx

Previous

](/docs/pm/bunx)[

bun outdated

Next

](/docs/pm/cli/outdated)
