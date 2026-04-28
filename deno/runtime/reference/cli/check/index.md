---
title: "deno check"
source: "https://docs.deno.com/runtime/reference/cli/check/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/check/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:26:43.143Z"
content_hash: "93234718b8df98cf1fc197d3b316d954cf34ba9519410f3340bf8078fe3cf45c"
menu_path: ["deno check"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/bundle/index.md", "title": "deno bundle"}
nav_next: {"path": "deno/runtime/reference/cli/clean/index.md", "title": "deno clean"}
---

**On this page**

-   [Basic usage](#basic-usage)
-   [Type-checking remote modules](#type-checking-remote-modules)
-   [Type-checking JavaScript files](#type-checking-javascript-files)
-   [Using in CI](#using-in-ci)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)

`deno check` type-checks your TypeScript (or JavaScript) code without running it. This is useful in CI pipelines or before deploying to catch type errors early. For more on TypeScript in Deno, see the [TypeScript](/runtime/fundamentals/typescript/) guide.

## Basic usage

\>\_

```sh
deno check main.ts
```

Check multiple files:

\>\_

```sh
deno check src/server.ts src/utils.ts
```

## Type-checking remote modules

By default, only local modules are type-checked. Use `--all` to also type-check remote dependencies:

\>\_

```sh
deno check --all main.ts
```

## Type-checking JavaScript files

If you have a JavaScript project and want to type-check it without adding `// @ts-check` to every file, use the `--check-js` flag:

\>\_

```sh
deno check --check-js main.js
```

## Using in CI

`deno check` exits with a non-zero status code if there are type errors, making it suitable for CI pipelines:

\>\_

```sh
deno check main.ts && echo "Types OK"
```

Note that [`deno test`](/runtime/reference/cli/test/) and [`deno bench`](/runtime/reference/cli/bench/) already perform type-checking by default, so you don't need a separate `deno check` step if you're already running tests. Use `deno check` when you want to type-check without running anything — for example, as a fast early step in CI:

\>\_

```sh
deno check main.ts
deno lint
deno test
```

Command line usage:

```
deno check [OPTIONS] [file]...
```

Download and type-check without execution.

```
deno check jsr:@std/http/file-server
```

Unless --reload is specified, this command will not re-download already cached dependencies

## Dependency management options

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

`--all`

Type-check all code, including remote modules and npm packages.

`--allow-import, -I`<IP\_OR\_HOSTNAME>optional

Allow importing from remote hosts. Optionally specify allowed IP addresses and host names, with ports as necessary. Default value: deno.land:443,[jsr.io:443](http://jsr.io:443),[esm.sh:443](http://esm.sh:443),[raw.esm.sh:443](http://raw.esm.sh:443),[cdn.jsdelivr.net:443](http://cdn.jsdelivr.net:443),[raw.githubusercontent.com:443](http://raw.githubusercontent.com:443),[gist.githubusercontent.com:443](http://gist.githubusercontent.com:443).

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`--check-js`

Enable type-checking of JavaScript files (equivalent to `compilerOptions.checkJs: true`).

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--deny-import`<IP\_OR\_HOSTNAME>optional

Deny importing from remote hosts. Optionally specify denied IP addresses and host names, with ports as necessary.

`--doc`

Type-check code blocks in JSDoc as well as actual code.

`--doc-only`

Type-check code blocks in JSDoc and Markdown only.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-code-cache`

Disable V8 code cache feature.

`--no-config`

Disable automatic loading of the configuration file.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.
