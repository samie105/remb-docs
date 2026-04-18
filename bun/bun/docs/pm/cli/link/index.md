---
title: "bun link"
source: "https://bun.com/docs/pm/cli/link"
canonical_url: "https://bun.com/docs/pm/cli/link"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:22.413Z"
content_hash: "df2e70e33a17dee2d19af103bad89551af2ca2194311c7fe280ac3f7f25c5f6f"
menu_path: ["bun link"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/install/index.md", "title": "bun install"}
nav_next: {"path": "bun/bun/docs/pm/cli/outdated/index.md", "title": "bun outdated"}
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

Use `bun link` in a local directory to register the current package as a “linkable” package.

terminal

```
cd /path/to/cool-pkg
cat package.json
bun link
```

```
bun link v1.3.3 (7416672e)
Success! Registered "cool-pkg"

To use cool-pkg in a project, run:
  bun link cool-pkg

Or add it in dependencies in your package.json file:
  "cool-pkg": "link:cool-pkg"
```

This package can now be “linked” into other projects using `bun link cool-pkg`. This will create a symlink in the `node_modules` directory of the target project, pointing to the local directory.

terminal

```
cd /path/to/my-app
bun link cool-pkg
```

In addition, the `--save` flag can be used to add `cool-pkg` to the `dependencies` field of your app’s package.json with a special version specifier that tells Bun to load from the registered local directory instead of installing from `npm`:

package.json

```
{
  "name": "my-app",
  "version": "1.0.0",
  "dependencies": {
    "cool-pkg": "link:cool-pkg"
  }
}
```

## 

[​

](#unlinking)

Unlinking

Use `bun unlink` in the root directory to unregister a local package.

terminal

```
cd /path/to/cool-pkg
bun unlink
```

```
bun unlink v1.3.3 (7416672e)
```

* * *

# 

[​

](#cli-usage)

CLI Usage

```
bun link <packages>
```

### 

[​

](#installation-scope)

Installation Scope

[​

](#param-global)

\--global

boolean

Install globally. Alias: `-g`

### 

[​

](#dependency-management)

Dependency Management

[​

](#param-production)

\--production

boolean

Don’t install devDependencies. Alias: `-p`

[​

](#param-omit)

\--omit

string

Exclude `dev`, `optional`, or `peer` dependencies from install

### 

[​

](#project-files-&-lockfiles)

Project Files & Lockfiles

[​

](#param-yarn)

\--yarn

boolean

Write a `yarn.lock` file (yarn v1). Alias: `-y`

[​

](#param-frozen-lockfile)

\--frozen-lockfile

boolean

Disallow changes to lockfile

[​

](#param-save-text-lockfile)

\--save-text-lockfile

boolean

Save a text-based lockfile

[​

](#param-lockfile-only)

\--lockfile-only

boolean

Generate a lockfile without installing dependencies

[​

](#param-no-save)

\--no-save

boolean

Don’t update `package.json` or save a lockfile

[​

](#param-save)

\--save

boolean

default:"true"

Save to `package.json` (true by default)

[​

](#param-trust)

\--trust

boolean

Add to `trustedDependencies` in the project’s `package.json` and install the package(s)

### 

[​

](#installation-control)

Installation Control

[​

](#param-force)

\--force

boolean

Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

[​

](#param-no-verify)

\--no-verify

boolean

Skip verifying integrity of newly downloaded packages

[​

](#param-backend)

\--backend

string

default:"clonefile"

Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

[​

](#param-linker)

\--linker

string

Linker strategy (one of `isolated` or `hoisted`)

[​

](#param-dry-run)

\--dry-run

boolean

Don’t install anything

[​

](#param-ignore-scripts)

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s `package.json` (dependency scripts are never run)

### 

[​

](#network-&-registry)

Network & Registry

[​

](#param-ca)

\--ca

string

Provide a Certificate Authority signing certificate

[​

](#param-cafile)

\--cafile

string

Same as `—ca`, but as a file path to the certificate

[​

](#param-registry)

\--registry

string

Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment variables

[​

](#param-network-concurrency)

\--network-concurrency

number

default:"48"

Maximum number of concurrent network requests (default 48)

### 

[​

](#performance-&-resource)

Performance & Resource

[​

](#param-concurrent-scripts)

\--concurrent-scripts

number

default:"5"

Maximum number of concurrent jobs for lifecycle scripts (default 5)

### 

[​

](#caching)

Caching

[​

](#param-cache-dir)

\--cache-dir

string

Store & load cached data from a specific directory path

[​

](#param-no-cache)

\--no-cache

boolean

Ignore manifest cache entirely

### 

[​

](#output-&-logging)

Output & Logging

[​

](#param-silent)

\--silent

boolean

Don’t log anything

[​

](#param-quiet)

\--quiet

boolean

Only show tarball name when packing

[​

](#param-verbose)

\--verbose

boolean

Excessively verbose logging

[​

](#param-no-progress)

\--no-progress

boolean

Disable the progress bar

[​

](#param-no-summary)

\--no-summary

boolean

Don’t print a summary

### 

[​

](#platform-targeting)

Platform Targeting

[​

](#param-cpu)

\--cpu

string

Override CPU architecture for optional dependencies (e.g., `x64`, `arm64`, `*` for all)

[​

](#param-os)

\--os

string

Override operating system for optional dependencies (e.g., `linux`, `darwin`, `*` for all)

### 

[​

](#global-configuration-&-context)

Global Configuration & Context

[​

](#param-config)

\--config

string

Specify path to config file (`bunfig.toml`). Alias: `-c`

[​

](#param-cwd)

\--cwd

string

Set a specific current working directory

### 

[​

](#help)

Help

[​

](#param-help)

\--help

boolean

Print this help menu. Alias: `-h`

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/link.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/link>)

[

Catalogs

Previous

](/docs/pm/catalogs)[

bun pm

Next

](/docs/pm/cli/pm)
