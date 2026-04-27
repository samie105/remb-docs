---
title: "deno run"
source: "https://docs.deno.com/runtime/reference/cli/run/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/run/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:32:26.932Z"
content_hash: "c3e22534e3c6aaecc9af1191a061832d19d890496171ea0194e3d3ab9124e9e0"
menu_path: ["deno run"]
section_path: []
content_language: "en"
---
**On this page**

-   [Usage](#usage)
    -   [Permissions examples](#permissions-examples)
-   [Watch](#watch)
-   [Running a package.json script](#running-a-package.json-script)
-   [Running code from stdin](#running-code-from-stdin)
-   [Terminate run](#terminate-run)
-   [Type checking options](#type-checking-options)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)
-   [Debugging options](#debugging-options)
-   [File watching options](#file-watching-options)

## Usage

Run a local file:

\>\_

```sh
deno run main.ts
```

The `run` subcommand is optional — you can also just use `deno <file>`:

\>\_

```sh
deno main.ts
```

By default, Deno runs programs in a sandbox without access to disk, network or ability to spawn subprocesses. This is because the Deno runtime is [secure by default](/runtime/fundamentals/security/). You can grant or deny required permissions using the [`--allow-*` and `--deny-*` flags](/runtime/fundamentals/security/#permissions-list).

### Permissions examples

Grant permission to read from disk and listen to network:

\>\_

```sh
deno run --allow-read --allow-net server.ts
```

Grant permission to read allow-listed files from disk:

\>\_

```sh
deno run --allow-read=/etc server.ts
```

Grant all permissions _this is not recommended and should only be used for testing_:

\>\_

```sh
deno run -A server.ts
```

If your project requires multiple security flags you should consider using a [`deno task`](/runtime/reference/cli/task/) to execute them.

## Watch

To watch for file changes and restart process automatically use the `--watch` flag. Deno's built in application watcher will restart your application as soon as files are changed.

_Be sure to put the flag before the file name_ eg:

\>\_

```sh
deno run --allow-net --watch server.ts
```

Deno's watcher will notify you of changes in the console, and will warn in the console if there are errors while you work.

## Running a package.json script

`package.json` scripts can be executed with the [`deno task`](/runtime/reference/cli/task/) command.

## Running code from stdin

You can pipe code from stdin and run it immediately:

\>\_

```sh
echo "console.log('hello')" | deno run -
```

## Terminate run

To stop the run command use `ctrl + c`.

Command line usage:

```
deno run [OPTIONS] [SCRIPT_ARG]...
```

Run a JavaScript or TypeScript program, or a task or script.

By default all programs are run in sandbox without access to disk, network or ability to spawn subprocesses.

```
deno run https://docs.deno.com/hello_world.ts
```

Grant permission to read from disk and listen to network:

```
deno run --allow-read --allow-net jsr:@std/http/file-server
```

Grant permission to read allow-listed files from disk:

```
deno run --allow-read=/etc jsr:@std/http/file-server
```

Grant all permissions:

```
deno run -A jsr:@std/http/file-server
```

Specifying the filename '-' to read the file from stdin.

```
curl https://docs.deno.com/hello_world.ts | deno run -
```

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

`--coverage`<DIR>optional

Collect coverage profile data into DIR. If DIR is not specified, it uses 'coverage/'. This option can also be set via the DENO\_COVERAGE\_DIR environment variable.

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

`--no-code-cache`

Disable V8 code cache feature.

`--no-config`

Disable automatic loading of the configuration file.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

`--seed`<NUMBER>

Set the random number generator seed.

`--tunnel, -t`<tunnel>optional

Execute tasks with a tunnel to Deno Deploy.

Create a secure connection between your local machine and Deno Deploy, providing access to centralised environment variables, logging, and serving from your local environment to the public internet.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

## Debugging options

`--inspect`<HOST\_PORT>optional

Activate inspector on host:port \[default: 127.0.0.1:9229\]. Host and port are optional. Using port 0 will assign a random free port.

`--inspect-brk`<HOST\_PORT>optional

Activate inspector on host:port, wait for debugger to connect and break at the start of user script.

`--inspect-wait`<HOST\_PORT>optional

Activate inspector on host:port and wait for debugger to connect before running user code.

## File watching options

`--no-clear-screen`

Do not clear terminal screen when under watch mode.

`--watch`<FILES>optional

Watch for file changes and restart process automatically. Local files from entry point module graph are watched by default. Additional paths might be watched by passing them as arguments to this flag.

`--watch-exclude`<FILES>optional

Exclude provided files/patterns from watch mode.

`--watch-hmr`<FILES>optional

Watch for file changes and restart process automatically. Local files from entry point module graph are watched by default. Additional paths might be watched by passing them as arguments to this flag.
