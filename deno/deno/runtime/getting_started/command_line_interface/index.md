---
title: "Command line interface"
source: "https://docs.deno.com/runtime/getting_started/command_line_interface/"
canonical_url: "https://docs.deno.com/runtime/getting_started/command_line_interface/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:04.492Z"
content_hash: "2d5a19b1285012052015bb8c621e72824b5bc675493f09b78cf9675b9ee54112"
menu_path: ["Command line interface"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/getting_started/setup_your_environment/index.md", "title": "Set up your environment"}
nav_next: {"path": "deno/deno/runtime/fundamentals/typescript/index.md", "title": "TypeScript support"}
---

# Good. We grant net permission to net_client.ts.
deno run --allow-net net_client.ts

# Bad! --allow-net was passed to Deno.args, throws a net permission error.
deno run net_client.ts --allow-net
```

## Common flags

Some flags can be used with multiple related subcommands. We discuss these below.

### Watch mode

You can supply the `--watch` flag to `deno run`, `deno test`, and `deno fmt` to enable the built-in file watcher. The watcher enables automatic reloading of your application whenever changes are detected in the source files. This is particularly useful during development, as it allows you to see the effects of your changes immediately without manually restarting the application.

The files that are watched will depend on the subcommand used:

*   for `deno run` and `deno test` the entrypoint, and all local files that the entrypoint statically imports will be watched.
*   for `deno fmt` all local files and directories specified as command line arguments (or the working directory if no specific files/directories is passed) are watched.

```shell
deno run --watch main.ts
deno test --watch
deno fmt --watch
```

You can exclude paths or patterns from watching by providing the `--watch-exclude` flag. The syntax is `--watch-exclude=path1,path2`. For example:

```shell
deno run --watch --watch-exclude=file1.ts,file2.ts main.ts
```

This will exclude file1.ts and file2.ts from being watched.

To exclude a pattern, remember to surround it in quotes to prevent your shell from expanding the glob:

```shell
deno run --watch --watch-exclude='*.js' main.ts
```

### Hot Module Replacement mode

You can use `--watch-hmr` flag with `deno run` to enable the hot module replacement mode. Instead of restarting the program, the runtime will try to update the program in-place. If updating in-place fails, the program will still be restarted.

\>\_

```sh
deno run --watch-hmr main.ts
```

When a hot module replacement is triggered, the runtime will dispatch a `CustomEvent` of type `hmr` that will include `path` property in its `detail` object. You can listen for this event and perform any additional logic that you need to do when a module is updated (eg. notify a browser over a WebSocket connection).

```ts
addEventListener("hmr", (e) => {
  console.log("HMR triggered", e.detail.path);
});
```

### Integrity flags (lock files)

Affect commands which can download resources to the cache: `deno install`, `deno run`, `deno test`, `deno doc`, and `deno compile`.

\>\_

```sh
--lock <FILE>    Check the specified lock file
--frozen[=<BOOLEAN>] Error out if lockfile is out of date
```

Find out more about these [here](/runtime/fundamentals/modules/#integrity-checking-and-lock-files).

### Cache and compilation flags

Affect commands which can populate the cache: `deno install`, `deno run`, `deno test`, `deno doc`, and `deno compile`. As well as the flags above, this includes those which affect module resolution, compilation configuration etc.

\>\_

```sh
--config <FILE>               Load configuration file
--import-map <FILE>           Load import map file
--no-remote                   Do not resolve remote modules
--reload=<CACHE_BLOCKLIST>    Reload source code cache (recompile TypeScript)
```

### Runtime flags

Affect commands which execute user code: `deno run` and `deno test`. These include all of the above as well as the following.

### Type checking flags

You can type-check your code (without executing it) using the command:

```shell
> deno check main.ts
```

You can also type-check your code before execution by using the `--check` argument to deno run:

```shell
> deno run --check main.ts
```

This flag affects `deno run` and `deno eval`. The following table describes the type-checking behavior of various subcommands. Here "Local" means that only errors from local code will induce type-errors, modules imported from https URLs (remote) may have type errors that are not reported. (To turn on type-checking for all modules, use `--check=all`.)

Subcommand

Type checking mode

`deno bench`

📁 Local

`deno check`

📁 Local

`deno compile`

📁 Local

`deno eval`

❌ None

`deno repl`

❌ None

`deno run`

❌ None

`deno test`

📁 Local

### Permission flags

These are listed [here](/runtime/fundamentals/security/).

### Other runtime flags

More flags which affect the execution environment.

\>\_

```sh
--cached-only                Require that remote dependencies are already cached
--inspect=<HOST:PORT>        activate inspector on host:port ...
--inspect-brk=<HOST:PORT>    activate inspector on host:port and break at ...
--inspect-wait=<HOST:PORT>   activate inspector on host:port and wait for ...
--location <HREF>            Value of 'globalThis.location' used by some web APIs
--prompt                     Fallback to prompt if required permission wasn't passed
--seed <NUMBER>              Seed Math.random()
--v8-flags=<v8-flags>        Set V8 command line options. For help: ...
```

