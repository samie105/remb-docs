---
title: "bun remove"
source: "https://bun.com/docs/pm/cli/remove"
canonical_url: "https://bun.com/docs/pm/cli/remove"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:38.713Z"
content_hash: "2fef9f2426439f15f1d0199b766e1fa51b68ae40aa971a04c63171ef247d63a7"
menu_path: ["bun remove"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/pm/index.md", "title": "bun pm"}
nav_next: {"path": "bun/bun/docs/pm/cli/publish/index.md", "title": "bun publish"}
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

## 

[​

](#basic-usage)

Basic Usage

terminal

```
bun remove ts-node
```

* * *

## 

[​

](#cli-usage)

CLI Usage

terminal

```
bun remove <package>
```

### 

[​

](#general-information)

General Information

[​

](#param-help)

\--help

boolean

Print this help menu. Alias: `-h`

### 

[​

](#configuration)

Configuration

[​

](#param-config)

\--config

string

Specify path to config file (`bunfig.toml`). Alias: `-c`

### 

[​

](#package-json-interaction)

Package.json Interaction

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

](#lockfile-behavior)

Lockfile Behavior

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

### 

[​

](#dependency-filtering)

Dependency Filtering

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

Use a specific registry by default, overriding `.npmrc`, `bunfig.toml` and environment variables

### 

[​

](#execution-control-&-validation)

Execution Control & Validation

[​

](#param-dry-run)

\--dry-run

boolean

Don’t install anything

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

](#script-execution)

Script Execution

[​

](#param-ignore-scripts)

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s `package.json` (dependency scripts are never run)

[​

](#param-concurrent-scripts)

\--concurrent-scripts

number

default:"5"

Maximum number of concurrent jobs for lifecycle scripts (default 5)

### 

[​

](#scope-&-path)

Scope & Path

[​

](#param-global)

\--global

boolean

Install globally. Alias: `-g`

[​

](#param-cwd)

\--cwd

string

Set a specific cwd

### 

[​

](#advanced-&-performance)

Advanced & Performance

[​

](#param-backend)

\--backend

string

default:"clonefile"

Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

[​

](#param-network-concurrency)

\--network-concurrency

number

default:"48"

Maximum number of concurrent network requests (default 48)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/cli/remove.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/cli/remove>)

[

bun add

Previous

](/docs/pm/cli/add)[

bun update

Next

](/docs/pm/cli/update)


