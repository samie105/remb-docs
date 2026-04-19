---
title: "bunx"
source: "https://bun.com/docs/pm/bunx"
canonical_url: "https://bun.com/docs/pm/bunx"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:57:03.052Z"
content_hash: "cc110fa0cd70f96f352b068fab205abdec52bd823e8b3ed3829f94dc0f9ddc59"
menu_path: ["bunx"]
section_path: []
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

`bunx` is an alias for `bun x`. The `bunx` CLI will be auto-installed when you install `bun`.

Use `bunx` to auto-install and run packages from `npm`. It’s Bun’s equivalent of `npx` or `yarn dlx`.

terminal

```
bunx cowsay "Hello world!"
```

⚡️ **Speed** — With Bun’s fast startup times, `bunx` is [roughly 100x faster](https://twitter.com/jarredsumner/status/1606163655527059458) than `npx` for locally installed packages.

Packages can declare executables in the `"bin"` field of their `package.json`. These are known as _package executables_ or _package binaries_.

package.json

```
{
  // ... other fields
  "name": "my-cli",
  "bin": {
    "my-cli": "dist/index.js"
  }
}
```

These executables are commonly plain JavaScript files marked with a [shebang line](https://en.wikipedia.org/wiki/Shebang_\(Unix\)) to indicate which program should be used to execute them. The following file indicates that it should be executed with `node`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f)dist/index.js

```
#!/usr/bin/env node

console.log("Hello world!");
```

These executables can be run with `bunx`,

terminal

```
bunx my-cli
```

As with `npx`, `bunx` will check for a locally installed package first, then fall back to auto-installing the package from `npm`. Installed packages will be stored in Bun’s global cache for future use.

## 

[​

](#arguments-and-flags)

Arguments and flags

To pass additional command-line flags and arguments through to the executable, place them after the executable name.

terminal

```
bunx my-cli --foo bar
```

* * *

## 

[​

](#shebangs)

Shebangs

By default, Bun respects shebangs. If an executable is marked with `#!/usr/bin/env node`, Bun will spin up a `node` process to execute the file. However, in some cases it may be desirable to run executables using Bun’s runtime, even if the executable indicates otherwise. To do so, include the `--bun` flag.

terminal

```
bunx --bun my-cli
```

The `--bun` flag must occur _before_ the executable name. Flags that appear _after_ the name are passed through to the executable.

terminal

```
bunx --bun my-cli # good
bunx my-cli --bun # bad
```

## 

[​

](#package-flag)

Package flag

**`--package <pkg>` or `-p <pkg>`** - Run binary from specific package. Useful when binary name differs from package name:

terminal

```
bunx -p renovate renovate-config-validator
bunx --package @angular/cli ng
```

To force bun to always be used with a script, use a shebang.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f)dist/index.js

```
#!/usr/bin/env bun
```

* * *

## 

[​

](#usage)

Usage

```
bunx [flags] <package>[@version] [flags and arguments for the package]
```

Execute an npm package executable (CLI), automatically installing into a global shared cache if not installed in `node_modules`.

### 

[​

](#flags)

Flags

[​

](#param-bun)

\--bun

boolean

Force the command to run with Bun instead of Node.js, even if the executable contains a Node shebang (`#!/usr/bin/env node`)

[​

](#param-p-package)

\-p, --package

string

Specify package to install when binary name differs from package name

[​

](#param-no-install)

\--no-install

boolean

Skip installation if package is not already installed

[​

](#param-verbose)

\--verbose

boolean

Enable verbose output during installation

[​

](#param-silent)

\--silent

boolean

Suppress output during installation

### 

[​

](#examples)

Examples

terminal

```
# Run Prisma migrations
bunx prisma migrate

# Format a file with Prettier
bunx prettier foo.js

# Run a specific version of a package
bunx uglify-js@3.14.0 app.js

# Use --package when binary name differs from package name
bunx -p @angular/cli ng new my-app

# Force running with Bun instead of Node.js, even if the executable contains a Node shebang
bunx --bun vite dev foo.js
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/pm/bunx.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /pm/bunx>)

[

bun update

Previous

](/docs/pm/cli/update)[

bun publish

Next

](/docs/pm/cli/publish)
