---
title: "Environment Variables"
source: "https://bun.com/docs/runtime/environment-variables"
canonical_url: "https://bun.com/docs/runtime/environment-variables"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:59:26.323Z"
content_hash: "13fc91ad7b637729f4d25eae9e050a4e3ffa08fe612519ea046a4c3d29b98517"
menu_path: ["Environment Variables"]
section_path: []
nav_prev: {"path": "bun/docs/runtime/debugger/index.md", "title": "Debugging"}
nav_next: {"path": "bun/docs/runtime/ffi/index.md", "title": "FFI"}
---

# Disable loading .env files
env = false
```

Explicitly provided environment files via `--env-file` will still be loaded even when default loading is disabled.

* * *

## 

[​

](#quotation-marks)

Quotation marks

Bun supports double quotes, single quotes, and template literal backticks:

.env

```
FOO='hello'
FOO="hello"
FOO=`hello`
```

### 

[​

](#expansion)

Expansion

Environment variables are automatically _expanded_. This means you can reference previously-defined variables in your environment variables.

.env

```
FOO=world
BAR=hello$FOO
```

```
process.env.BAR; // => "helloworld"
```

This is useful for constructing connection strings or other compound values.

.env

```
DB_USER=postgres
DB_PASSWORD=secret
DB_HOST=localhost
DB_PORT=5432
DB_URL=postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME
```

This can be disabled by escaping the `$` with a backslash.

.env

```
FOO=world
BAR=hello\$FOO
```

```
process.env.BAR; // => "hello$FOO"
```

### 

[​

](#dotenv)

`dotenv`

Bun reads `.env` files automatically, so `dotenv` and `dotenv-expand` are unnecessary.

## 

[​

](#reading-environment-variables)

Reading environment variables

The current environment variables can be accessed via `process.env`.

```
process.env.API_TOKEN; // => "secret"
```

Bun also exposes these variables via `Bun.env` and `import.meta.env`, which are aliases of `process.env`.

```
Bun.env.API_TOKEN; // => "secret"
import.meta.env.API_TOKEN; // => "secret"
```

To print all currently-set environment variables to the command line, run `bun --print process.env`. This is useful for debugging.

```
bun --print process.env
BAZ=stuff
FOOBAR=aaaaaa
<lots more lines>
```

## 

[​

](#typescript)

TypeScript

In TypeScript, all properties of `process.env` are typed as `string | undefined`.

```
Bun.env.whatever;
// string | undefined
```

To get autocompletion and tell TypeScript to treat a variable as a non-optional string, we’ll use [interface merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#merging-interfaces).

```
declare module "bun" {
  interface Env {
    AWESOME: string;
  }
}
```

Add this line to any file in your project. It will globally add the `AWESOME` property to `process.env` and `Bun.env`.

```
process.env.AWESOME; // => string
```

## 

[​

](#configuring-bun)

Configuring Bun

These environment variables are read by Bun and configure aspects of its behavior.

Name

Description

`NODE_TLS_REJECT_UNAUTHORIZED`

`NODE_TLS_REJECT_UNAUTHORIZED=0` disables SSL certificate validation. This is useful for testing and debugging, but you should be very hesitant to use this in production. Note: This environment variable was originally introduced by Node.js and we kept the name for compatibility.

`BUN_CONFIG_VERBOSE_FETCH`

If `BUN_CONFIG_VERBOSE_FETCH=curl`, then fetch requests will log the url, method, request headers and response headers to the console. This is useful for debugging network requests. This also works with `node:http`. `BUN_CONFIG_VERBOSE_FETCH=1` is equivalent to `BUN_CONFIG_VERBOSE_FETCH=curl` except without the `curl` output.

`BUN_RUNTIME_TRANSPILER_CACHE_PATH`

The runtime transpiler caches the transpiled output of source files larger than 50 kb. This makes CLIs using Bun load faster. If `BUN_RUNTIME_TRANSPILER_CACHE_PATH` is set, then the runtime transpiler will cache transpiled output to the specified directory. If `BUN_RUNTIME_TRANSPILER_CACHE_PATH` is set to an empty string or the string `"0"`, then the runtime transpiler will not cache transpiled output. If `BUN_RUNTIME_TRANSPILER_CACHE_PATH` is unset, then the runtime transpiler will cache transpiled output to the platform-specific cache directory.

`TMPDIR`

Bun occasionally requires a directory to store intermediate assets during bundling or other operations. If unset, defaults to the platform-specific temporary directory: `/tmp` on Linux, `/private/tmp` on macOS.

`NO_COLOR`

If `NO_COLOR=1`, then ANSI color output is [disabled](https://no-color.org/).

`FORCE_COLOR`

If `FORCE_COLOR=1`, then ANSI color output is force enabled, even if `NO_COLOR` is set.

`BUN_CONFIG_MAX_HTTP_REQUESTS`

Control the maximum number of concurrent HTTP requests sent by fetch and `bun install`. Defaults to `256`. If you are running into rate limits or connection issues, you can reduce this number.

`BUN_CONFIG_NO_CLEAR_TERMINAL_ON_RELOAD`

If `BUN_CONFIG_NO_CLEAR_TERMINAL_ON_RELOAD=true`, then `bun --watch` will not clear the console on reload

`DO_NOT_TRACK`

Disable uploading crash reports to `bun.report` on crash. On macOS & Windows, crash report uploads are enabled by default. Otherwise, telemetry is not sent yet as of May 21st, 2024, but we are planning to add telemetry in the coming weeks. If `DO_NOT_TRACK=1`, then auto-uploading crash reports and telemetry are both [disabled](https://do-not-track.dev/).

`BUN_OPTIONS`

Prepends command-line arguments to any Bun execution. For example, `BUN_OPTIONS="--hot"` makes `bun run dev` behave like `bun --hot run dev`

## 

[​

](#runtime-transpiler-caching)

Runtime transpiler caching

For files larger than 50 KB, Bun caches transpiled output into `$BUN_RUNTIME_TRANSPILER_CACHE_PATH` or the platform-specific cache directory. This makes CLIs using Bun load faster. This transpiler cache is global and shared across all projects. It is safe to delete the cache at any time. It is a content-addressable cache, so it will never contain duplicate entries. It is also safe to delete the cache while a Bun process is running. It is recommended to disable this cache when using ephemeral filesystems like Docker. Bun’s Docker images automatically disable this cache.

### 

[​

](#disable-the-runtime-transpiler-cache)

Disable the runtime transpiler cache

To disable the runtime transpiler cache, set `BUN_RUNTIME_TRANSPILER_CACHE_PATH` to an empty string or the string `"0"`.

```
BUN_RUNTIME_TRANSPILER_CACHE_PATH=0 bun run dev
```

### 

[​

](#what-does-it-cache)

What does it cache?

It caches:

*   The transpiled output of source files larger than 50 KB.
*   The sourcemap for the transpiled output of the file

The file extension `.pile` is used for these cached files.

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/environment-variables.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/environment-variables>)

[

Workers

Previous

](../workers/index.md)[

Shell

Next

](../shell/index.md)
