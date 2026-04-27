---
title: "deno repl"
source: "https://docs.deno.com/runtime/reference/cli/repl/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/repl/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:32:14.189Z"
content_hash: "628612176160da0baf2320bf037513cd5678a3425c609584534f386ed9bd2451"
menu_path: ["deno repl"]
section_path: []
content_language: "en"
---
**On this page**

-   [Special variables](#special-variables)
-   [Special functions](#special-functions)
-   [\--eval flag](#--eval-flag)
-   [\--eval-file flag](#--eval-file-flag)
    -   [Relative Import Path Resolution](#relative-import-path-resolution)
-   [Tab completions](#tab-completions)
-   [Keyboard shortcuts](#keyboard-shortcuts)
-   [DENO\_REPL\_HISTORY](#deno_repl_history)
-   [Options](#options)
-   [Dependency management options](#dependency-management-options)
-   [Debugging options](#debugging-options)

## Special variables

The REPL provides a couple of special variables, that are always available:

| Identifier | Description |
| --- | --- |
| \_ | Yields the last evaluated expression |
| \_error | Yields the last thrown error |

\>\_

```sh
Deno 1.14.3
exit using ctrl+d or close()
> "hello world!"
"hello world!"
> _
"hello world!"
> const foo = "bar";
undefined
> _
undefined
```

## Special functions

The REPL provides several functions in the global scope:

| Function | Description |
| --- | --- |
| clear() | Clears the entire terminal screen |
| close() | Close the current REPL session |

## `--eval` flag

`--eval` flag allows you to run some code in the runtime before you are dropped into the REPL. This is useful for importing some code you commonly use in the REPL, or modifying the runtime in some way:

\>\_

```sh
deno repl --allow-net --eval 'import { assert } from "jsr:@std/assert@1"'
Deno 1.45.3
exit using ctrl+d, ctrl+c, or close()
> assert(true)
undefined
> assert(false)
Uncaught AssertionError
    at assert (https://jsr.io/@std/assert/1.0.0/assert.ts:21:11)
    at <anonymous>:1:22
```

## `--eval-file` flag

`--eval-file` flag allows you to run code from specified files before you are dropped into the REPL. Like the `--eval` flag, this is useful for importing code you commonly use in the REPL, or modifying the runtime in some way.

Files can be specified as paths or URLs. URL files are cached and can be reloaded via the `--reload` flag.

If `--eval` is also specified, then `--eval-file` files are run before the `--eval` code.

\>\_

```sh
deno repl --eval-file=https://docs.deno.com/examples/welcome.ts,https://docs.deno.com/examples/local.ts
Download https://docs.deno.com/examples/welcome.ts
Welcome to Deno!
Download https://docs.deno.com/examples/local.ts
Deno 1.45.3
exit using ctrl+d or close()
> local // this variable is defined locally in local.ts, but not exported
"This is a local variable inside of local.ts"
```

### Relative Import Path Resolution

If `--eval-file` specifies a code file that contains relative imports, then the runtime will try to resolve the imports relative to the current working directory. It will not try to resolve them relative to the code file's location. This can cause "Module not found" errors when `--eval-file` is used with module files:

\>\_

```sh
deno repl --eval-file=https://jsr.io/@std/encoding/1.0.0/ascii85.ts
error in --eval-file file https://jsr.io/@std/encoding/1.0.0/ascii85.ts. Uncaught TypeError: Module not found "file:///home/_validate_binary_like.ts".
    at async <anonymous>:2:13
Deno 1.45.3
exit using ctrl+d or close()
>
```

## Tab completions

Tab completions are a crucial feature for quick navigation in the REPL. After hitting `tab` key, Deno will now show a list of all possible completions.

\>\_

```sh
deno repl
Deno 1.45.3
exit using ctrl+d or close()
> Deno.read
readTextFile      readFile          readDirSync       readLinkSync      readAll           read
readTextFileSync  readFileSync      readDir           readLink          readAllSync       readSync
```

## Keyboard shortcuts

| Keystroke | Action |
| --- | --- |
| Ctrl-A, Home | Move cursor to the beginning of line |
| Ctrl-B, Left | Move cursor one character left |
| Ctrl-C | Interrupt and cancel the current edit |
| Ctrl-D | If line _is_ empty, signal end of line |
| Ctrl-D, Del | If line is _not_ empty, delete character under cursor |
| Ctrl-E, End | Move cursor to end of line |
| Ctrl-F, Right | Move cursor one character right |
| Ctrl-H, Backspace | Delete character before cursor |
| Ctrl-I, Tab | Next completion |
| Ctrl-J, Ctrl-M, Enter | Finish the line entry |
| Ctrl-K | Delete from cursor to end of line |
| Ctrl-L | Clear screen |
| Ctrl-N, Down | Next match from history |
| Ctrl-P, Up | Previous match from history |
| Ctrl-R | Reverse Search history (Ctrl-S forward, Ctrl-G cancel) |
| Ctrl-T | Transpose previous character with current character |
| Ctrl-U | Delete from start of line to cursor |
| Ctrl-V, Ctrl-Q | Insert the subsequent character verbatim instead of performing any Action associated with it. For example, to insert a newline while editing a multi-line history entry, press Ctrl-V then Ctrl-J (Ctrl-J is the ASCII Control Character `Line Feed`) |
| Ctrl-W | Delete word leading up to cursor (using white space as a word boundary) |
| Ctrl-X Ctrl-U | Undo |
| Ctrl-Y | Paste from Yank buffer |
| Ctrl-Y | Paste from Yank buffer (Meta-Y to paste next yank instead) |
| Ctrl-Z | Suspend (Unix only) |
| Ctrl-\_ | Undo |
| Meta-0, 1, ..., - | Specify the digit to the argument. `–` starts a negative argument. |
| Meta < | Move to first entry in history |
| Meta > | Move to last entry in history |
| Meta-B, Alt-Left | Move cursor to previous word |
| Meta-Backspace | Kill from the start of the current word, or, if between words, to the start of the previous word |
| Meta-C | Capitalize the current word |
| Meta-D | Delete forwards one word |
| Meta-F, Alt-Right | Move cursor to next word |
| Meta-L | Lower-case the next word |
| Meta-T | Transpose words |
| Meta-U | Upper-case the next word |
| Meta-Y | See Ctrl-Y |
| Ctrl-S | Insert a new line |

## `DENO_REPL_HISTORY`

By default, Deno stores REPL history in a `deno_history.txt` file within the `DENO_DIR` directory. The location of your `DENO_DIR` directory and other resources, can be found by running the `deno info`.

You can use `DENO_REPL_HISTORY` environmental variable to control where Deno stores the REPL history file. You can set it to an empty value, Deno will not store the history file.

Command line usage:

```
deno repl [OPTIONS] [-- [ARGS]...]
```

Starts a read-eval-print-loop, which lets you interactively build up program state in the global context. It is especially useful for quick prototyping and checking snippets of code.

TypeScript is supported, however it is not type-checked, only transpiled.

## Options

`--cert`<FILE>

Load certificate authority from PEM encoded file.

`[--conditions](< https://docs.deno.com/go/conditional-exports>)`<conditions>

Use this argument to specify custom conditions for npm package exports. You can also use DENO\_CONDITIONS env var. .

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--env-file`<FILE>optional

Load environment variables from local file Only the first environment variable with a given key is used. Existing process environment variables are not overwritten, so if variables with the same names already exist in the environment, their values will be preserved. Where multiple declarations for the same environment variable exist in your .env file, the first one encountered is applied. This is determined by the order of the files you pass as arguments.

`--eval`<code>

Evaluates the provided code when the REPL starts.

`--eval-file`<eval-file>

Evaluates the provided file(s) as scripts when the REPL starts. Accepts file paths and URLs.

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

## Debugging options

`--inspect`<HOST\_PORT>optional

Activate inspector on host:port \[default: 127.0.0.1:9229\]. Host and port are optional. Using port 0 will assign a random free port.

`--inspect-brk`<HOST\_PORT>optional

Activate inspector on host:port, wait for debugger to connect and break at the start of user script.

`--inspect-wait`<HOST\_PORT>optional

Activate inspector on host:port and wait for debugger to connect before running user code.
