---
title: "deno x"
source: "https://docs.deno.com/runtime/reference/cli/x/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/x/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:35:11.371Z"
content_hash: "fb97ccf917608f0253a9901c6e2e4cddc81d3e8d4ba44cb35741505374756f00"
menu_path: ["deno x"]
section_path: []
content_language: "en"
nav_prev: {"path": "../unstable_flags/index.md", "title": "Unstable feature flags"}
nav_next: {"path": "../../std/index.md", "title": "Deno Standard Library (@std)"}
---

**On this page**

-   [Installing the dx alias](#installing-the-dx-alias)
-   [Basic usage](#basic-usage)
-   [How it works](#how-it-works)
-   [Permissions](#permissions)
-   [Type checking options](#type-checking-options)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)
-   [Debugging options](#debugging-options)

`deno x` executes a package from npm or JSR without installing it permanently. It is similar to `npx` in the npm ecosystem.

## Installing the `dx` alias

For convenience, you can install `deno x` as a standalone `dx` binary that runs with all permissions by default:

\>\_

```sh
deno x --install-alias
```

Then use it directly:

\>\_

```sh
dx npm:create-vite my-app
```

You can customize the alias name:

\>\_

```sh
deno x --install-alias=denox
```

## Basic usage

Run an npm package:

\>\_

```sh
deno x npm:create-vite my-app
```

Run a JSR package:

\>\_

```sh
deno x jsr:@std/http/file-server
```

## How it works

`deno x` downloads the package to the global cache (if not already cached), resolves the package's binary entry point, and executes it. The package is not added to your project's [`deno.json`](/runtime/fundamentals/configuration/) or `package.json`.

## Permissions

The executed package runs with the permissions you specify:

\>\_

```sh
deno x --allow-read --allow-net npm:serve .
```

Or grant all permissions:

\>\_

```sh
deno x -A npm:create-vite my-app
```

Command line usage:

```
deno x [OPTIONS] [SCRIPT_ARG]...
```

Execute a binary from npm or jsr, like npx

## Type checking options

`--check`<CHECK\_TYPE>optional

Enable type-checking. This subcommand does not type-check by default If the value of "all" is supplied, remote modules will be included. Alternatively, the 'deno check' subcommand can be used.

`--no-check`<NO\_CHECK\_TYPE>optional

Skip type-checking. If the value of "remote" is supplied, diagnostic errors from remote modules will be ignored.

## Dependency management options

`--cached-only`

Require that remote dependencies are already cached.

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`[--import-map](< https://docs.deno.com/runtime/manual/basics/import_maps>)`<FILE>

Load import map file from local file or remote URL.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

`--no-npm`

Do not resolve npm modules.

`--no-remote`

Do not resolve remote modules.

`--node-modules-dir`<MODE>optional

Sets the node modules management mode for npm packages.

`--reload, -r`<CACHE\_BLOCKLIST>optional

Reload source code cache (recompile TypeScript) no value Reload everything jsr:@std/http/file-server,jsr:@std/assert/assert-equals Reloads specific modules npm: Reload all npm modules npm:chalk Reload specific npm module.

`--vendor`<vendor>optional

Toggles local vendor folder usage for remote modules and a node\_modules folder for npm packages.

## Options

`--allow-scripts`<PACKAGE>optional

Allow running npm lifecycle scripts for the given packages Note: Scripts will only be executed when using a node\_modules directory (`--node-modules-dir`).

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--install-alias`<install-alias>optional

Creates a dx alias so you can run dx  instead of deno x .

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-config`

Disable automatic loading of the configuration file.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

`--seed`<NUMBER>

Set the random number generator seed.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

`--yes, -y`

Assume confirmation for all prompts.

## Debugging options

`--inspect`<HOST\_PORT>optional

Activate inspector on host:port \[default: 127.0.0.1:9229\]. Host and port are optional. Using port 0 will assign a random free port.

`--inspect-brk`<HOST\_PORT>optional

Activate inspector on host:port, wait for debugger to connect and break at the start of user script.

`--inspect-wait`<HOST\_PORT>optional

Activate inspector on host:port and wait for debugger to connect before running user code.
