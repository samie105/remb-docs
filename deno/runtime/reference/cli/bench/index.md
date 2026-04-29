---
title: "deno bench"
source: "https://docs.deno.com/runtime/reference/cli/bench/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/bench/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:26:10.640Z"
content_hash: "482aabb2ff5baee53fbdd941af9b18dca3a49f905d6dc6b634dfae76b3016ad7"
menu_path: ["deno bench"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/audit/index.md", "title": "deno audit"}
nav_next: {"path": "deno/runtime/reference/cli/bundle/index.md", "title": "deno bundle"}
---

# Run all benches in the current directory and all sub-directories
deno bench

# Run all benches in the util directory
deno bench util/

# Run just my_bench.ts
deno bench my_bench.ts
```

> ⚠️ If you want to pass additional CLI arguments to the bench files use `--` to inform Deno that remaining arguments are scripts arguments.

\>\_

```sh
# Pass additional arguments to the bench file
deno bench my_bench.ts -- -e --foo --bar
```

`deno bench` uses the same permission model as `deno run` and therefore will require, for example, `--allow-write` to write to the file system during benching.

To see all runtime options with `deno bench`, you can reference the command line help:

\>\_

```sh
deno help bench
```

## Filtering

There are a number of options to filter the benches you are running.

### Command line filtering

Benches can be run individually or in groups using the command line `--filter` option.

The filter flags accept a string or a pattern as value.

Assuming the following benches:

```ts
Deno.bench({
  name: "my-bench",
  fn: () => {/* bench function zero */},
});
Deno.bench({
  name: "bench-1",
  fn: () => {/* bench function one */},
});
Deno.bench({
  name: "bench2",
  fn: () => {/* bench function two */},
});
```

This command will run all of these benches because they all contain the word "bench".

\>\_

```sh
deno bench --filter "bench" benchmarks/
```

On the flip side, the following command uses a pattern and will run the second and third benchmarks.

\>\_

```sh
deno bench --filter "/bench-*\d/" benchmarks/
```

_To let Deno know that you want to use a pattern, wrap your filter with forward-slashes like the JavaScript syntactic sugar for a regex._

### Bench definition filtering

Within the benches themselves, you have two options for filtering.

#### Filtering out (ignoring these benches)

Sometimes you want to ignore benches based on some sort of condition (for example you only want a benchmark to run on Windows). For this you can use the `ignore` boolean in the bench definition. If it is set to true the bench will be skipped.

```ts
Deno.bench({
  name: "bench windows feature",
  ignore: Deno.build.os !== "windows",
  fn() {
    // do windows feature
  },
});
```

#### Filtering in (only run these benches)

Sometimes you may be in the middle of a performance problem within a large bench class and you would like to focus on just that single bench and ignore the rest for now. For this you can use the `only` option to tell the benchmark harness to only run benches with this set to true. Multiple benches can set this option. While the benchmark run will report on the success or failure of each bench, the overall benchmark run will always fail if any bench is flagged with `only`, as this is a temporary measure only which disables nearly all of your benchmarks.

```ts
Deno.bench({
  name: "Focus on this bench only",
  only: true,
  fn() {
    // bench complicated stuff
  },
});
```

## JSON output

To retrieve the output as JSON, use the `--json` flag:

\>\_

```sh
deno bench my_bench.ts --json
{
  "version": 1,
  "runtime": "Deno/2.4.2 x86_64-unknown-linux-gnu",
  "cpu": "12th Gen Intel(R) Core(TM) i3-12100",
  "benches": [
    {
      "origin": "file:///path/to/my_bench.ts",
      "group": null,
      "name": "Test",
      "baseline": false,
      "results": [
        {
          "ok": {
            "n": 51,
            "min": 946.7129,
            "max": 3024.3281,
            "avg": 1241.3926823529412,
            "p75": 1174.9718,
            "p99": 3024.3281,
            "p995": 3024.3281,
            "p999": 3024.3281,
            "highPrecision": false,
            "usedExplicitTimers": false
          }
        }
      ]
    }
  ]
}
```

Command line usage:

```
deno bench [OPTIONS] [files]... [-- [SCRIPT_ARG]...]
```

Run benchmarks using Deno's built-in bench tool.

Evaluate the given files, run all benches declared with 'Deno.bench()' and report results to standard output:

```
deno bench src/fetch_bench.ts src/signal_bench.ts
```

If you specify a directory instead of a file, the path is expanded to all contained files matching the glob `{*_,*.,}bench.{js,mjs,ts,mts,jsx,tsx}`:

```
deno bench src/
```

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

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--ext`<ext>

Set content type of the supplied file.

`--filter`<filter>

Run benchmarks with this string or regexp pattern in the bench name.

`--ignore`<ignore>

Ignore files.

`--json`

UNSTABLE: Output benchmark result in JSON format.

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-config`

Disable automatic loading of the configuration file.

`--no-run`

Cache bench modules, but don't run benchmarks.

`--permit-no-files`

Don't return an error code if no files were found.

`--preload`<FILE>

A list of files that will be executed before the main module.

`--require`<FILE>

A list of CommonJS modules that will be executed before the main module.

`--seed`<NUMBER>

Set the random number generator seed.

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

## File watching options

`--no-clear-screen`

Do not clear terminal screen when under watch mode.

`--watch`

Watch for file changes and restart process automatically. Only local files from entry point module graph are watched.

`--watch-exclude`<FILES>optional

Exclude provided files/patterns from watch mode.
