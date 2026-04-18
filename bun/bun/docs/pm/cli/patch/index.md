---
title: "bun patch"
source: "https://bun.com/docs/pm/cli/patch"
canonical_url: "https://bun.com/docs/pm/cli/patch"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:31.932Z"
content_hash: "6e2226923ee1f5e6f3e315ec0c312a3ef9b4eafc48aec7ec8ef2e167f27a769d"
menu_path: ["bun patch"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/outdated/index.md", "title": "bun outdated"}
nav_next: {"path": "bun/bun/docs/pm/cli/pm/index.md", "title": "bun pm"}
---

# you can supply the package name
bun patch react

# ...and a precise version in case multiple versions are installed
bun patch react@17.0.2

# or the path to the package
bun patch node_modules/react
```

#### Step 2. Test your changes locally

`bun patch <pkg>` makes it safe to edit the `<pkg>` in `node_modules/` directly, while preserving the integrity of Bun’s [Global Cache](bun/bun/docs/pm/global-cache/index.md). This works by re-creating an unlinked clone of the package in `node_modules/` and diffing it against the original package in the Global Cache.

#### Step 3. Commit your changes

Once you’re happy with your changes, run `bun patch --commit <path or pkg>`. Bun will generate a patch file in `patches/`, update your `package.json` and lockfile, and Bun will start using the patched package:

terminal

```
# you can supply the path to the patched package
bun patch --commit node_modules/react

# ... or the package name and optionally the version
bun patch --commit react@17.0.2

# choose the directory to store the patch files
bun patch --commit react --patches-dir=mypatches

# `patch-commit` is available for compatibility with pnpm
bun patch-commit react
```

* * *

## CLI Usage

```
bun patch <package>@<version>
```

### Patch Generation

\--commit

boolean

Install a package containing modifications in `dir`

\--patches-dir

string

The directory to put the patch file in (only if —commit is used)

### Dependency Management

\--production

boolean

Don’t install devDependencies. Alias: `-p`

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s `package.json` (dependency scripts are never run)

\--trust

boolean

Add to `trustedDependencies` in the project’s `package.json` and install the package(s)

\--global

boolean

Install globally. Alias: `-g`

\--omit

string

Exclude `dev`, `optional`, or `peer` dependencies from install

### Project Files & Lockfiles

\--yarn

boolean

Write a `yarn.lock` file (yarn v1). Alias: `-y`

\--no-save

boolean

Don’t update `package.json` or save a lockfile

\--save

boolean

default:"true"

Save to `package.json` (true by default)

\--frozen-lockfile

boolean

Disallow changes to lockfile

\--save-text-lockfile

boolean

Save a text-based lockfile

\--lockfile-only

boolean

Generate a lockfile without installing dependencies

### Installation Control

\--backend

string

default:"clonefile"

Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

\--linker

string

Linker strategy (one of `isolated` or `hoisted`)

\--dry-run

boolean

Don’t install anything

\--force

boolean

Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

\--no-verify

boolean

Skip verifying integrity of newly downloaded packages

### Network & Registry

\--ca

string

Provide a Certificate Authority signing certificate

\--cafile

string

Same as `—ca`, but as a file path to the certificate

\--registry

string

Use a specific registry by default, overriding `.npmrc`, `bunfig.toml`, and environment variables

\--network-concurrency

number

default:"48"

Maximum number of concurrent network requests (default 48)

### Performance & Resource

\--concurrent-scripts

number

default:"5"

Maximum number of concurrent jobs for lifecycle scripts (default 5)

### Caching

\--cache-dir

string

Store & load cached data from a specific directory path

\--no-cache

boolean

Ignore manifest cache entirely

### Output & Logging

\--silent

boolean

Don’t log anything

\--quiet

boolean

Only show tarball name when packing

\--verbose

boolean

Excessively verbose logging

\--no-progress

boolean

Disable the progress bar

\--no-summary

boolean

Don’t print a summary

### Platform Targeting

\--cpu

string

Override CPU architecture for optional dependencies (e.g., `x64`, `arm64`, `*` for all)

\--os

string

Override operating system for optional dependencies (e.g., `linux`, `darwin`, `*` for all)

### Global Configuration & Context

\--config

string

Specify path to config file (`bunfig.toml`). Alias: `-c`

\--cwd

string

Set a specific current working directory

### Help

\--help

boolean

Print this help menu. Alias: `-h`
