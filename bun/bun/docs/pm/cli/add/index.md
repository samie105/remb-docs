---
title: "bun add"
source: "https://bun.com/docs/pm/cli/add"
canonical_url: "https://bun.com/docs/pm/cli/add"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:13.130Z"
content_hash: "6e14fcad8768e6c1884766fddb565cb2a4defab67b9447682496a7a1247ac259"
menu_path: ["bun add"]
section_path: []
nav_prev: {"path": "bun/bun/docs/pm/cli/audit/index.md", "title": "bun audit"}
nav_next: {"path": "bun/bun/docs/pm/cli/info/index.md", "title": "bun info"}
---

# where `bun add --global` installs packages
globalDir = "~/.bun/install/global"

# where globally-installed package bins are linked
globalBinDir = "~/.bun/bin"
```

## Trusted dependencies

Unlike other npm clients, Bun does not execute arbitrary lifecycle scripts for installed dependencies, such as `postinstall`. These scripts represent a potential security risk, as they can execute arbitrary code on your machine. To tell Bun to allow lifecycle scripts for a particular package, add the package to `trustedDependencies` in your package.json.

package.json

```
{
  "name": "my-app",
  "version": "1.0.0",
  "trustedDependencies": ["my-trusted-package"] 
}
```

Bun reads this field and will run lifecycle scripts for `my-trusted-package`.

## Git dependencies

To add a dependency from a public or private git repository:

terminal

```
bun add git@github.com:moment/moment.git
```

Bun supports a variety of protocols, including [`github`](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#github-urls), [`git`](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#git-urls-as-dependencies), `git+ssh`, `git+https`, and many more.

package.json

```
{
  "dependencies": {
    "dayjs": "git+https://github.com/iamkun/dayjs.git",
    "lodash": "git+ssh://github.com/lodash/lodash.git#4.17.21",
    "moment": "git@github.com:moment/moment.git",
    "zod": "github:colinhacks/zod"
  }
}
```

## Tarball dependencies

A package name can correspond to a publicly hosted `.tgz` file. During installation, Bun will download and install the package from the specified tarball URL, rather than from the package registry.

terminal

```
bun add zod@https://registry.npmjs.org/zod/-/zod-3.21.4.tgz
```

This will add the following line to your `package.json`:

package.json

```
{
  "dependencies": {
    "zod": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz"
  }
}
```

* * *

## CLI Usage

```
bun add <package> <@version>
```

### Dependency Management

\--production

boolean

Don’t install devDependencies. Alias: `-p`

\--omit

string

Exclude `dev`, `optional`, or `peer` dependencies from install

\--global

boolean

Install globally. Alias: `-g`

\--dev

boolean

Add dependency to `devDependencies`. Alias: `-d`

\--optional

boolean

Add dependency to `optionalDependencies`

\--peer

boolean

Add dependency to `peerDependencies`

\--exact

boolean

Add the exact version instead of the `^` range. Alias: `-E`

\--only-missing

boolean

Only add dependencies to `package.json` if they are not already present

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

\--trust

boolean

Add to `trustedDependencies` in the project’s `package.json` and install the package(s)

\--save-text-lockfile

boolean

Save a text-based lockfile

\--lockfile-only

boolean

Generate a lockfile without installing dependencies

### Installation Control

\--dry-run

boolean

Don’t install anything

\--force

boolean

Always request the latest versions from the registry & reinstall all dependencies. Alias: `-f`

\--no-verify

boolean

Skip verifying integrity of newly downloaded packages

\--ignore-scripts

boolean

Skip lifecycle scripts in the project’s `package.json` (dependency scripts are never run)

\--analyze

boolean

Recursively analyze & install dependencies of files passed as arguments (using Bun’s bundler). Alias: `-a`

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

\--backend

string

default:"clonefile"

Platform-specific optimizations for installing dependencies. Possible values: `clonefile` (default), `hardlink`, `symlink`, `copyfile`

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

\--verbose

boolean

Excessively verbose logging

\--no-progress

boolean

Disable the progress bar

\--no-summary

boolean

Don’t print a summary

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


