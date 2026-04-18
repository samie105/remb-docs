---
title: "deno add"
source: "https://docs.deno.com/runtime/reference/cli/add/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/add/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:14.994Z"
content_hash: "73dd9f41f09dbfbe965eba2e1f0db2c1dd5943cb0dcf473abdd347431e4280b9"
menu_path: ["deno add"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/fundamentals/stability_and_releases/index.md", "title": "Stability and releases"}
nav_next: {"path": "deno/deno/runtime/reference/cli/approve_scripts/index.md", "title": "deno approve-scripts"}
---

On this page

*   [Examples](#examples)
*   [Where dependencies are stored](#where-dependencies-are-stored)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

The `deno add` command adds dependencies to your project's configuration file. It is an alias for [`deno install [PACKAGES]`](/runtime/reference/cli/install/#deno-install-packages). For more on how Deno handles dependencies, see [Modules and dependencies](/runtime/fundamentals/modules/).

## Examples

Add packages from JSR and npm:

\>\_

```sh
deno add @std/path npm:express
```

By default, dependencies are added with a caret (`^`) version range. Use `--save-exact` to pin to an exact version:

\>\_

```sh
deno add --save-exact @std/path
```

This saves the dependency without the `^` prefix (e.g., `1.0.0` instead of `^1.0.0`).

Treat unprefixed package names as npm packages:

\>\_

```sh
deno add --npm express
```

## Where dependencies are stored

If your project has a `package.json`, npm packages will be added to `dependencies` in `package.json`. Otherwise, all packages are added to the `imports` field in [`deno.json`](/runtime/fundamentals/configuration/).

Command line usage:

```
deno add [OPTIONS] [packages]...
```

Add dependencies to your configuration file.

```
deno add jsr:@std/path
```

You can also add npm packages:

```
deno add npm:react
```

Or multiple dependencies at once:

```
deno add jsr:@std/path jsr:@std/assert npm:chalk
```

## Options

`--allow-scripts`<PACKAGE>optional

Allow running npm lifecycle scripts for the given packages Note: Scripts will only be executed when using a node\_modules directory (`--node-modules-dir`).

`--dev, -D`

Add the package as a dev dependency. Note: This only applies when adding to a `package.json` file.

`--jsr`

assume unprefixed package names are jsr packages.

`--lockfile-only`

Install only updating the lockfile.

`--npm`

assume unprefixed package names are npm packages.

`--save-exact`

Save exact version without the caret (^).

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.


