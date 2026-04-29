---
title: "deno install"
source: "https://docs.deno.com/runtime/reference/cli/install/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/install/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:30:15.790Z"
content_hash: "3bef85b5a645ad7f0a489311f6a1f5835be18eb2421c00b0aeb3fa6027c87ee1"
menu_path: ["deno install"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/init/index.md", "title": "deno init"}
nav_next: {"path": "deno/runtime/reference/cli/jupyter/index.md", "title": "Jupyter Kernel for Deno"}
---

# Install using deno install

deno install -n awesome_cli https://example.com/awesome/cli.ts
```

### deno install --global --compile \[PACKAGE\_OR\_URL\]

Use this command to compile a package or script into a standalone, self-contained binary. The resulting executable can be distributed and run without requiring Deno to be installed on the target system.

\>\_

```sh
deno install --global --compile -A npm:@anthropic-ai/claude-code
```

This combines the behavior of [`deno compile`](../compile/index.md) with global installation — producing a native binary placed in the installation root (same as `--global` without `--compile`).

## Native Node.js addons

A lot of popular packages npm packages like [`npm:sqlite3`](https://www.npmjs.com/package/sqlite3) or [`npm:duckdb`](https://www.npmjs.com/package/duckdb) depend on ["lifecycle scripts"](https://docs.npmjs.com/cli/v10/using-npm/scripts#life-cycle-scripts), eg. `preinstall` or `postinstall` scripts. Most often running these scripts is required for a package to work correctly.

Unlike npm, Deno does not run these scripts by default as they pose a potential security vulnerability.

You can still run these scripts by passing the `--allow-scripts=<packages>` flag when running `deno install`:

\>\_

```sh
deno install --allow-scripts=npm:sqlite3
```

_Install all dependencies and allow `npm:sqlite3` package to run its lifecycle scripts_.

## \--quiet flag

The `--quiet` flag suppresses diagnostic output when installing dependencies. When used with `deno install`, it will hide progress indicators, download information, and success messages.

\>\_

```sh
deno install --quiet jsr:@std/http/file-server
```

This is useful for scripting environments or when you want cleaner output in CI pipelines.

## Uninstall

You can uninstall dependencies or binary script with `deno uninstall` command:

\>\_

```sh
deno uninstall express
Removed express
```

\>\_

```sh
deno uninstall -g file-server
deleted /Users/deno/.deno/bin/file-server
✅ Successfully uninstalled file-server
```

See [`deno uninstall` page for more details](../uninstall/index.md).

Command line usage:

```
deno install [OPTIONS] [cmd]... [-- [SCRIPT_ARG]...]
```

Installs dependencies either in the local project or globally to a bin directory.

### Local installation

Add dependencies to the local project's configuration (`deno.json / package.json`) and installs them in the package cache. If no dependency is specified, installs all dependencies listed in the config file. If the `--entrypoint` flag is passed, installs the dependencies of the specified entrypoint(s).

```
deno install
```

```
deno install jsr:@std/bytes
```

```
deno install npm:chalk
```

```
deno install --entrypoint entry1.ts entry2.ts
```

### Global installation

If the `--global` flag is set, installs a script as an executable in the installation root's bin directory.

```
deno install --global --allow-net --allow-read jsr:@std/http/file-server
```

```
deno install -g https://examples.deno.land/color-logging.ts
```

To change the executable name, use `-n`/`--name`:

```
deno install -g --allow-net --allow-read -n serve jsr:@std/http/file-server
```

The executable name is inferred by default:

-   Attempt to take the file stem of the URL path. The above example would become `file_server`.
-   If the file stem is something generic like `main`, `mod`, `index` or `cli`, and the path has no parent, take the file name of the parent path. Otherwise settle with the generic name.
-   If the resulting name has an `@...` suffix, strip it.

To change the installation root, use `--root`:

```
deno install -g --allow-net --allow-read --root /usr/local jsr:@std/http/file-server
```

The installation root is determined, in order of precedence:

-   `--root` option
-   `DENO_INSTALL_ROOT` environment variable
-   `$HOME/.deno`

These must be added to the path manually if required.

## Type checking options

`--check`<CHECK\_TYPE>optional

Set type-checking behavior. This subcommand type-checks local modules by default, so adding `--check` is redundant If the value of "all" is supplied, remote modules will be included. Alternatively, the 'deno check' subcommand can be used.

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

`--compile`

Install the script as a compiled executable.

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--dev, -D`

Add the package as a dev dependency. Note: This only applies when adding to a `package.json` file.

`--entrypoint, -e`

Install dependents of the specified entrypoint(s).

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--force, -f`

Forcefully overwrite existing installation.

`--global, -g`

Install a package or script as a globally available executable.

`--jsr`

assume unprefixed package names are jsr packages.

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--lockfile-only`

Install only updating the lockfile.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--name, -n`<name>

Executable file name.

`--no-config`

Disable automatic loading of the configuration file.

`--npm`

assume unprefixed package names are npm packages.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

`--root`<root>

Installation root.

`--save-exact`

Save exact version without the caret (^).

`--seed`<NUMBER>

Set the random number generator seed.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

## Debugging options

`--inspect`<HOST\_PORT>optional

Activate inspector on host:port \[default: 127.0.0.1:9229\]. Host and port are optional. Using port 0 will assign a random free port.

`--inspect-brk`<HOST\_PORT>optional

Activate inspector on host:port, wait for debugger to connect and break at the start of user script.

`--inspect-wait`<HOST\_PORT>optional

Activate inspector on host:port and wait for debugger to connect before running user code.
