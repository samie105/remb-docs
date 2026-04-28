---
title: "deno eval"
source: "https://docs.deno.com/runtime/reference/cli/eval/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/eval/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:29:09.652Z"
content_hash: "83981c61071ffd1a04cbb15d1ba0b65afb5a52c6f1cab9c8456d856a99e381d3"
menu_path: ["deno eval"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/doc/index.md", "title": "deno doc"}
nav_next: {"path": "deno/runtime/reference/cli/fmt/index.md", "title": "deno fmt"}
---

# 3

deno eval -p "Deno.version"
# { deno: "2.x.x", v8: "...", typescript: "..." }
```

## Reading from stdin

Combine with piped input for quick data processing:

\>\_

```sh
echo '{"name":"deno"}' | deno eval -p "
  const text = await new Response(Deno.stdin.readable).text();
  JSON.parse(text).name
"
```

Command line usage:

```
deno eval [OPTIONS] [CODE_ARG]...
```

Evaluate JavaScript from the command line.

```
deno eval "console.log('hello world')"
```

To evaluate as TypeScript:

```
deno eval --ext=ts "const v: string = 'hello'; console.log(v)"
```

This command has implicit access to all permissions.

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

`--cpu-prof`

Start the V8 CPU profiler on startup and write the profile to disk on exit. Profiles are written to the current directory by default.

`--cpu-prof-dir`<DIR>

Directory where the V8 CPU profiles will be written. Implicitly enables `--cpu-prof`.

`--cpu-prof-flamegraph`

Generate an SVG flamegraph alongside the CPU profile.

`--cpu-prof-interval`<MICROSECONDS>

Sampling interval in microseconds for CPU profiling (default: 1000).

`--cpu-prof-md`

Generate a human-readable markdown report alongside the CPU profile.

`--cpu-prof-name`<NAME>

Filename for the CPU profile (defaults to CPU...cpuprofile).

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--ext`<ext>

Set content type of the supplied file.

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-config`

Disable automatic loading of the configuration file.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--print, -p`

print result to stdout.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

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
