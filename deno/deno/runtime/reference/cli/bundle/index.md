---
title: "deno bundle"
source: "https://docs.deno.com/runtime/reference/cli/bundle/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/bundle/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:22.458Z"
content_hash: "86feba1d3b086237403c6681f66e12c3ba1e014f4e287ede3f8696743755e7e2"
menu_path: ["deno bundle"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/bench/index.md", "title": "deno bench"}
nav_next: {"path": "deno/deno/runtime/reference/cli/check/index.md", "title": "deno check"}
---

On this page

*   [Basic usage](#basic-usage)
*   [Type checking options](#type-checking-options)
*   [Dependency management options](#dependency-management-options)
*   [Options](#options)

Info

`deno bundle` is currently an experimental subcommand and is subject to changes.

`deno bundle` combines your module and all of its dependencies into a single JavaScript file.

## Basic usage

\>\_

```sh
deno bundle main.ts output.js
```

The output file can then be run with Deno or in other JavaScript runtimes:

\>\_

```sh
deno run output.js
```

For more on bundling strategies with Deno, see the [Bundling](/runtime/reference/bundling/) guide.

Command line usage:

```
deno bundle [OPTIONS] [file]...
```

Output a single JavaScript file with all dependencies.

deno bundle jsr:@std/http/file-server -o file-server.bundle.js

If no output file is given, the output is written to standard output:

deno bundle jsr:@std/http/file-server

## Type checking options

`--check`<CHECK\_TYPE>optional

Enable type-checking. This subcommand does not type-check by default If the value of "all" is supplied, remote modules will be included. Alternatively, the 'deno check' subcommand can be used.

`--no-check`<NO\_CHECK\_TYPE>optional

Skip type-checking. If the value of "remote" is supplied, diagnostic errors from remote modules will be ignored.

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

`--allow-import, -I`<IP\_OR\_HOSTNAME>optional

Allow importing from remote hosts. Optionally specify allowed IP addresses and host names, with ports as necessary. Default value: deno.land:443,[jsr.io:443](http://jsr.io:443),[esm.sh:443](http://esm.sh:443),[raw.esm.sh:443](http://raw.esm.sh:443),[cdn.jsdelivr.net:443](http://cdn.jsdelivr.net:443),[raw.githubusercontent.com:443](http://raw.githubusercontent.com:443),[gist.githubusercontent.com:443](http://gist.githubusercontent.com:443).

`--allow-scripts`<PACKAGE>optional

Allow running npm lifecycle scripts for the given packages Note: Scripts will only be executed when using a node\_modules directory (`--node-modules-dir`).

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`--code-splitting`

Enable code splitting.

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--deny-import`<IP\_OR\_HOSTNAME>optional

Deny importing from remote hosts. Optionally specify denied IP addresses and host names, with ports as necessary.

`--external`<external>

`--format`<format>

`--inline-imports`<inline-imports>optional

Whether to inline imported modules into the importing file \[default: true\]

`--keep-names`

Keep function and class names.

`--minify`

Minify the output.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-config`

Disable automatic loading of the configuration file.

`--outdir`<outdir>

Output directory for bundled files.

`--output, -o`<output>

Output path\`.

`--packages`<packages>

How to handle packages. Accepted values are 'bundle' or 'external'.

`--platform`<platform>

Platform to bundle for. Accepted values are 'browser' or 'deno'.

`--sourcemap`<sourcemap>optional

Generate source map. Accepted values are 'linked', 'inline', or 'external'.

`--watch`

Watch and rebuild on changes.
