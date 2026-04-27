---
title: "deno compile"
source: "https://docs.deno.com/runtime/reference/cli/compile/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/compile/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:27:16.513Z"
content_hash: "549a095f6801cb7dba6942a2f884d993c209fa154f1b1c80d3918ab57f66a5c0"
menu_path: ["deno compile"]
section_path: []
content_language: "en"
---
**On this page**

-   [Flags](#flags)
-   [Cross Compilation](#cross-compilation)
    -   [Supported Targets](#supported-targets)
-   [Icons](#icons)
-   [Dynamic Imports](#dynamic-imports)
-   [Including Data Files or Directories](#including-data-files-or-directories)
-   [Workers](#workers)
-   [Self-Extracting Executables](#self-extracting-executables)
    -   [Trade-offs](#trade-offs)
-   [Code Signing](#code-signing)
    -   [macOS](#macos)
    -   [Windows](#windows)
-   [Unavailable in executables](#unavailable-in-executables)
-   [Type checking options](#type-checking-options)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)
-   [Compile options](#compile-options)

## Flags

As with [`deno install`](/runtime/reference/cli/install/), the runtime flags used to execute the script must be specified at compilation time. This includes permission flags.

\>\_

```sh
deno compile --allow-read --allow-net jsr:@std/http/file-server
```

[Script arguments](/runtime/getting_started/command_line_interface/#passing-script-arguments) can be partially embedded.

\>\_

```sh
deno compile --allow-read --allow-net jsr:@std/http/file-server -p 8080

./file_server --help
```

## Cross Compilation

You can cross-compile binaries for other platforms by using the `--target` flag.

```
# Cross compile for Apple Silicon
deno compile --target aarch64-apple-darwin main.ts

# Cross compile for Windows with an icon
deno compile --target x86_64-pc-windows-msvc --icon ./icon.ico main.ts
```

### Supported Targets

Deno supports cross compiling to all targets regardless of the host platform.

| OS | Architecture | Target |
| --- | --- | --- |
| Windows | x86\_64 | `x86_64-pc-windows-msvc` |
| macOS | x86\_64 | `x86_64-apple-darwin` |
| macOS | ARM64 | `aarch64-apple-darwin` |
| Linux | x86\_64 | `x86_64-unknown-linux-gnu` |
| Linux | ARM64 | `aarch64-unknown-linux-gnu` |

## Icons

It is possible to add an icon to the executable by using the `--icon` flag when targeting Windows. The icon must be in the `.ico` format.

```
deno compile --icon icon.ico main.ts

# Cross compilation with icon
deno compile --target x86_64-pc-windows-msvc --icon ./icon.ico main.ts
```

## Dynamic Imports

By default, statically analyzable dynamic imports (imports that have the string literal within the `import("...")` call expression) will be included in the output.

```ts
// calculator.ts and its dependencies will be included in the binary
const calculator = await import("./calculator.ts");
```

But non-statically analyzable dynamic imports won't:

```ts
const specifier = condition ? "./calc.ts" : "./better_calc.ts";
const calculator = await import(specifier);
```

To include non-statically analyzable dynamic imports, specify an `--include <path>` flag.

\>\_

```sh
deno compile --include calc.ts --include better_calc.ts main.ts
```

## Including Data Files or Directories

Starting in Deno 2.1, you can include files or directories in the executable by specifying them via the `--include <path>` flag.

\>\_

```sh
deno compile --include names.csv --include data main.ts
```

Then read the file relative to the directory path of the current module via `import.meta.dirname`:

```ts
// main.ts
const names = Deno.readTextFileSync(import.meta.dirname + "/names.csv");
const dataFiles = Deno.readDirSync(import.meta.dirname + "/data");

// use names and dataFiles here
```

Note this currently only works for files on the file system and not remote files.

## Workers

Similarly to non-statically analyzable dynamic imports, code for [workers](/runtime/reference/web_platform_apis/#web-workers) is not included in the compiled executable by default. There are two ways to include workers:

1.  Use the `--include <path>` flag to include the worker code.

\>\_

```sh
deno compile --include worker.ts main.ts
```

2.  Import worker module using a statically analyzable import.

```ts
// main.ts
import "./worker.ts";
```

\>\_

```sh
deno compile main.ts
```

## Self-Extracting Executables

By default, compiled executables serve embedded files from an in-memory virtual file system. The `--self-extracting` flag changes this behavior so that the binary extracts all embedded files to disk on first run and uses real file system operations at runtime.

\>\_

```sh
deno compile --self-extracting main.ts
```

This is useful for scenarios where code needs real files on disk, such as native addons or native code that reads relative files.

The extraction directory is chosen in order of preference:

1.  `<exe_dir>/.<exe_name>/<hash>/` (next to the compiled binary)
2.  Platform data directory fallback:
    -   Linux: `$XDG_DATA_HOME/<exe_name>/<hash>` or `~/.local/share/<exe_name>/<hash>`
    -   macOS: `~/Library/Application Support/<exe_name>/<hash>`
    -   Windows: `%LOCALAPPDATA%\<exe_name>\<hash>`

Files are only extracted once — subsequent runs reuse the extracted directory if it already exists and the hash matches.

### Trade-offs

Self-extracting mode enables broader compatibility, but comes with some trade-offs:

-   **Initial startup cost**: The first run takes longer due to file extraction.
-   **Disk usage**: Extracted files take up additional space on disk.
-   **Memory usage**: Higher memory usage since embedded content can no longer be referenced as static data.
-   **Tamper risk**: Users or other code can modify the extracted files on disk.

## Code Signing

### macOS

By default, on macOS, the compiled executable will be signed using an ad-hoc signature which is the equivalent of running `codesign -s -`:

\>\_

```sh
deno compile -o main main.ts
codesign --verify -vv ./main

./main: valid on disk
./main: satisfies its Designated Requirement
```

You can specify a signing identity when code signing the executable just like you would do with any other macOS executable:

\>\_

```sh
codesign -s "Developer ID Application: Your Name" ./main
```

Refer to the [official documentation](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution) for more information on codesigning and notarization on macOS.

### Windows

On Windows, the compiled executable can be signed using the `SignTool.exe` utility.

\>\_

```sh
deno compile -o main.exe main.ts
signtool sign /fd SHA256 main.exe
```

## Unavailable in executables

-   [Web Storage API](/runtime/reference/web_platform_apis/#web-storage)
-   [Web Cache](/api/web/~/Cache)

Command line usage:

```
deno compile [OPTIONS] [SCRIPT_ARG]...
```

Compiles the given script into a self contained executable.

```
deno compile --allow-read --allow-net jsr:@std/http/file-server
```

```
deno compile --output file_server jsr:@std/http/file-server
```

Any flags specified which affect runtime behavior will be applied to the resulting binary.

This allows distribution of a Deno application to systems that do not have Deno installed. Under the hood, it bundles a slimmed down version of the Deno runtime along with your JavaScript or TypeScript code.

Cross-compiling to different target architectures is supported using the `--target` flag. On the first invocation of `deno compile`, Deno will download the relevant binary and cache it in `$DENO_DIR`.

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

`--v8-flags`<V8\_FLAGS>optional

To see a list of all available flags use `--v8-flags=--help` Flags can also be set via the DENO\_V8\_FLAGS environment variable. Any flags set with this flag are appended after the DENO\_V8\_FLAGS environment variable.

## Compile options

`--exclude`<exclude>

Excludes a file/directory in the compiled executable. Use this flag to exclude a specific file or directory within the included files. For example, to exclude a certain folder in the bundled node\_modules directory.

`--icon`<icon>

Set the icon of the executable on Windows (.ico).

`--include`<include>

Includes an additional module or file/directory in the compiled executable. Use this flag if a dynamically imported module or a web worker main module fails to load in the executable or to embed a file or directory in the executable. This flag can be passed multiple times, to include multiple additional modules.

`--no-terminal`

Hide terminal on Windows.

`--output, -o`<output>

Output file (defaults to $PWD/).

`--self-extracting`

Create a self-extracting binary that extracts the embedded file system to disk on first run and then runs from there.

`--target`<target>

Target OS architecture.
