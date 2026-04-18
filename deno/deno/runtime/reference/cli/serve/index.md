---
title: "deno serve"
source: "https://docs.deno.com/runtime/reference/cli/serve/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/serve/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:04.856Z"
content_hash: "61bb1a7bfe7868f754435fed34fab9aed3703c23bf3be3be81e63fc12b80de5d"
menu_path: ["deno serve"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/sandbox/index.md", "title": "deno sandbox"}
nav_next: {"path": "deno/deno/runtime/reference/cli/task/index.md", "title": "deno task"}
---

On this page

*   [Basic usage](#basic-usage)
*   [Default export shape](#default-export-shape)
    *   [fetch (required)](#fetch-\(required\))
    *   [onListen (optional)](#onlisten-\(optional\))
*   [Routing requests](#routing-requests)
*   [Binding to a hostname](#binding-to-a-hostname)
*   [Horizontal scaling](#horizontal-scaling)
*   [Watch mode](#watch-mode)
*   [Permissions](#permissions)
*   [Type checking options](#type-checking-options)
*   [Dependency management options](#dependency-management-options)
*   [Options](#options)
*   [Debugging options](#debugging-options)
*   [File watching options](#file-watching-options)

`deno serve` runs a file as an HTTP server using [`Deno.serve()`](/api/deno/~/Deno.serve). The file must export a default object with a `fetch` handler. For a full guide on building HTTP servers, see [Writing an HTTP Server](/runtime/fundamentals/http_server/).

## Basic usage

server.ts

```typescript
export default {
  fetch(_req: Request) {
    return new Response("Hello world!");
  },
} satisfies Deno.ServeDefaultExport;
```

\>\_

```sh
deno serve server.ts
```

By default, the server listens on port **8000**. Override it with `--port`:

\>\_

```sh
deno serve --port=3000 server.ts
```

## Default export shape

The file must export a default object that satisfies [`Deno.ServeDefaultExport`](/api/deno/~/Deno.ServeDefaultExport). The object has two properties:

```typescript
export interface ServeDefaultExport {
  fetch: ServeHandler;
  onListen?: (localAddr: Deno.Addr) => void;
}
```

### `fetch` (required)

The `fetch` handler receives a standard [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and a [`ServeHandlerInfo`](/api/deno/~/Deno.ServeHandlerInfo) object with connection metadata:

```typescript
type ServeHandler = (
  request: Request,
  info: ServeHandlerInfo,
) => Response | Promise<Response>;

interface ServeHandlerInfo {
  remoteAddr: Deno.Addr; // remote address of the connection
  completed: Promise<void>; // resolves when the request completes
}
```

If the handler throws, the error is isolated to that request — the server continues serving.

### `onListen` (optional)

Called once when the server starts listening. If omitted, a default message is logged to the console.

server.ts

```typescript
export default {
  fetch(request, info) {
    const { hostname, port } = info.remoteAddr as Deno.NetAddr;
    console.log(`${request.method} ${request.url} from ${hostname}:${port}`);

    return new Response("Hello, World!", {
      headers: { "content-type": "text/plain" },
    });
  },

  onListen({ hostname, port }) {
    console.log(`Server running at http://${hostname}:${port}/`);
  },
} satisfies Deno.ServeDefaultExport;
```

Any other properties on the default export are silently ignored. If `fetch` is missing, no server starts. If `fetch` or `onListen` exist but are not functions, a `TypeError` is thrown.

## Routing requests

Use the request URL to route to different handlers:

server.ts

```typescript
export default {
  fetch(request: Request) {
    const url = new URL(request.url);

    if (url.pathname === "/api/health") {
      return Response.json({ status: "ok" });
    }

    return new Response("Not found", { status: 404 });
  },
} satisfies Deno.ServeDefaultExport;
```

## Binding to a hostname

By default, `deno serve` listens on `0.0.0.0`. Use `--host` to bind to a specific interface:

\>\_

```sh
deno serve --host=127.0.0.1 server.ts
```

## Horizontal scaling

Run multiple server instances across CPU cores for better throughput:

\>\_

```sh
deno serve --parallel server.ts
```

## Watch mode

Restart the server automatically when files change:

\>\_

```sh
deno serve --watch server.ts
```

## Permissions

`deno serve` automatically allows the server to listen without requiring `--allow-net`. Additional permissions (like file reads) must be granted explicitly:

\>\_

```sh
deno serve --allow-read server.ts
```

Command line usage:

```
deno serve [OPTIONS] [SCRIPT_ARG]...
```

Run a server defined in a main module

The serve command uses the default exports of the main module to determine which servers to start.

Start a server defined in server.ts:

```
deno serve server.ts
```

Start a server defined in server.ts, watching for changes and running on port 5050:

```
deno serve --watch --port 5050 server.ts
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

`--host`<host>

The TCP address to serve on, defaulting to 0.0.0.0 (all interfaces).

`--location`<HREF>

Value of globalThis.location used by some web APIs.

`--minimum-dependency-age`<minimum-dependency-age>

(Unstable) The age in minutes, ISO-8601 duration or RFC3339 absolute timestamp (e.g. '120' for two hours, 'P2D' for two days, '2025-09-16' for cutoff date, '2025-09-16T12:00:00+00:00' for cutoff time, '0' to disable).

`--no-code-cache`

Disable V8 code cache feature.

`--no-config`

Disable automatic loading of the configuration file.

`--open`

Open the browser on the address that the server is running on.

`--parallel`

Run multiple server workers in parallel. Parallelism defaults to the number of available CPUs or the value of the DENO\_JOBS environment variable.

`--port`<port>

The TCP port to serve on. Pass 0 to pick a random free port \[default: 8000\]

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


