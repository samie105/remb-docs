---
title: "Bundler"
source: "https://bun.com/docs/bundler"
canonical_url: "https://bun.com/docs/bundler"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:36:24.740Z"
content_hash: "2fc265d7e268a1de3a4a3560e28ba6d7f5c4d2d4ae0b73d7e9e589de126a153f"
menu_path: ["Bundler"]
section_path: []
nav_prev: {"path": "bun/docs/index.md", "title": "Welcome to Bun"}
nav_next: {"path": "bun/docs/bundler/bytecode/index.md", "title": "Bytecode Caching"}
---

# CommonJS bytecode
bun build ./index.tsx --outdir ./out --bytecode

# ESM bytecode (requires --compile)
bun build ./index.tsx --outfile ./mycli --bytecode --format=esm --compile
```

## Executables

Bun supports “compiling” a JavaScript/TypeScript entrypoint into a standalone executable. This executable contains a copy of the Bun binary.

terminal

```
bun build ./cli.tsx --outfile mycli --compile
./mycli
```

Refer to [Bundler > Executables](executables/index.md) for complete documentation.

## Logs and errors

On failure, `Bun.build` returns a rejected promise with an `AggregateError`. This can be logged to the console for pretty printing of the error list, or programmatically read with a try/catch block.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
try {
  const result = await Bun.build({
    entrypoints: ["./index.tsx"],
    outdir: "./out",
  });
} catch (e) {
  // TypeScript does not allow annotations on the catch clause
  const error = e as AggregateError;
  console.error("Build Failed");

  // Example: Using the built-in formatter
  console.error(error);

  // Example: Serializing the failure as a JSON string.
  console.error(JSON.stringify(error, null, 2));
}
```

Most of the time, an explicit try/catch is not needed, as Bun will neatly print uncaught exceptions. You can use a top-level await on the `Bun.build` call instead. Each item in `error.errors` is an instance of `BuildMessage` or `ResolveMessage` (subclasses of `Error`), containing detailed information for each error.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
class BuildMessage {
  name: string;
  position?: Position;
  message: string;
  level: "error" | "warning" | "info" | "debug" | "verbose";
}

class ResolveMessage extends BuildMessage {
  code: string;
  referrer: string;
  specifier: string;
  importKind: ImportKind;
}
```

On build success, the returned object contains a `logs` property, which contains bundler warnings and info messages.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
const result = await Bun.build({
  entrypoints: ["./index.tsx"],
  outdir: "./out",
});

if (result.logs.length > 0) {
  console.warn("Build succeeded with warnings:");
  for (const message of result.logs) {
    // Bun will pretty print the message object
    console.warn(message);
  }
}
```

## Reference

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)Typescript Definitions

```
interface Bun {
  build(options: BuildOptions): Promise<BuildOutput>;
}

interface BuildConfig {
  entrypoints: string[]; // list of file path
  outdir?: string; // output directory
  target?: Target; // default: "browser"
  /**
   * Output module format. Top-level await is only supported for `"esm"`.
   *
   * Can be:
   * - `"esm"`
   * - `"cjs"` (**experimental**)
   * - `"iife"` (**experimental**)
   *
   * @default "esm"
   */
  format?: "esm" | "cjs" | "iife";
  /**
   * JSX configuration object for controlling JSX transform behavior
   */
  jsx?: {
    runtime?: "automatic" | "classic";
    importSource?: string;
    factory?: string;
    fragment?: string;
    sideEffects?: boolean;
    development?: boolean;
  };
  naming?:
    | string
    | {
        chunk?: string;
        entry?: string;
        asset?: string;
      };
  root?: string; // project root
  splitting?: boolean; // default true, enable code splitting
  plugins?: BunPlugin[];
  external?: string[];
  packages?: "bundle" | "external";
  publicPath?: string;
  define?: Record<string, string>;
  loader?: { [k in string]: Loader };
  sourcemap?: "none" | "linked" | "inline" | "external" | boolean; // default: "none", true -> "inline"
  /**
   * package.json `exports` conditions used when resolving imports
   *
   * Equivalent to `--conditions` in `bun build` or `bun run`.
   *
   * https://nodejs.org/api/packages.html#exports
   */
  conditions?: Array<string> | string;

  /**
   * Controls how environment variables are handled during bundling.
   *
   * Can be one of:
   * - `"inline"`: Injects environment variables into the bundled output by converting `process.env.FOO`
   *   references to string literals containing the actual environment variable values
   * - `"disable"`: Disables environment variable injection entirely
   * - A string ending in `*`: Inlines environment variables that match the given prefix.
   *   For example, `"MY_PUBLIC_*"` will only include env vars starting with "MY_PUBLIC_"
   */
  env?: "inline" | "disable" | `${string}*`;
  minify?:
    | boolean
    | {
        whitespace?: boolean;
        syntax?: boolean;
        identifiers?: boolean;
      };
  /**
   * Ignore dead code elimination/tree-shaking annotations such as @__PURE__ and package.json
   * "sideEffects" fields. This should only be used as a temporary workaround for incorrect
   * annotations in libraries.
   */
  ignoreDCEAnnotations?: boolean;
  /**
   * Force emitting @__PURE__ annotations even if minify.whitespace is true.
   */
  emitDCEAnnotations?: boolean;

  /**
   * Generate bytecode for the output. This can dramatically improve cold
   * start times, but will make the final output larger and slightly increase
   * memory usage.
   *
   * - CommonJS: works with or without `compile: true`
   * - ESM: requires `compile: true`
   *
   * Without an explicit `format`, defaults to CommonJS.
   *
   * Must be `target: "bun"`
   * @default false
   */
  bytecode?: boolean;
  /**
   * Add a banner to the bundled code such as "use client";
   */
  banner?: string;
  /**
   * Add a footer to the bundled code such as a comment block like
   *
   * `// made with bun!`
   */
  footer?: string;

  /**
   * Drop function calls to matching property accesses.
   */
  drop?: string[];

  /**
   * - When set to `true`, the returned promise rejects with an AggregateError when a build failure happens.
   * - When set to `false`, returns a {@link BuildOutput} with `{success: false}`
   *
   * @default true
   */
  throw?: boolean;

  /**
   * Custom tsconfig.json file path to use for path resolution.
   * Equivalent to `--tsconfig-override` in the CLI.
   */
  tsconfig?: string;

  outdir?: string;
}

interface BuildOutput {
  outputs: BuildArtifact[];
  success: boolean;
  logs: Array<BuildMessage | ResolveMessage>;
}

interface BuildArtifact extends Blob {
  path: string;
  loader: Loader;
  hash: string | null;
  kind: "entry-point" | "chunk" | "asset" | "sourcemap" | "bytecode";
  sourcemap: BuildArtifact | null;
}

type Loader =
  | "js"
  | "jsx"
  | "ts"
  | "tsx"
  | "css"
  | "json"
  | "jsonc"
  | "toml"
  | "yaml"
  | "text"
  | "file"
  | "napi"
  | "wasm"
  | "html";

interface BuildOutput {
  outputs: BuildArtifact[];
  success: boolean;
  logs: Array<BuildMessage | ResolveMessage>;
}

declare class ResolveMessage {
  readonly name: "ResolveMessage";
  readonly position: Position | null;
  readonly code: string;
  readonly message: string;
  readonly referrer: string;
  readonly specifier: string;
  readonly importKind:
    | "entry_point"
    | "stmt"
    | "require"
    | "import"
    | "dynamic"
    | "require_resolve"
    | "at"
    | "at_conditional"
    | "url"
    | "internal";
  readonly level: "error" | "warning" | "info" | "debug" | "verbose";

  toString(): string;
}
```

* * *

## CLI Usage

```
bun build <entry points>
```

### General Configuration

\--production

boolean

Set `NODE_ENV=production` and enable minification

\--bytecode

boolean

Use a bytecode cache when compiling

\--target

string

default:"browser"

Intended execution environment for the bundle. One of `browser`, `bun`, or `node`

\--conditions

string

Pass custom resolution conditions

\--env

string

default:"disable"

Inline environment variables into the bundle as `process.env.$`. To inline variables matching a prefix, use a glob like `FOO_PUBLIC_*`

### Output & File Handling

\--outdir

string

default:"dist"

Output directory (used when building multiple entry points)

\--outfile

string

Write output to a specific file

\--sourcemap

string

default:"none"

Generate source maps. One of `linked`, `inline`, `external`, or `none`

Add a banner to the output (e.g. `“use client”` for React Server Components)

Add a footer to the output (e.g. `// built with bun!`)

\--format

string

default:"esm"

Module format of the output bundle. One of `esm`, `cjs`, or `iife`. Defaults to `cjs` when `—bytecode` is used.

### File Naming

\--entry-naming

string

default:"\[dir\]/\[name\].\[ext\]"

Customize entry point filenames

\--chunk-naming

string

default:"\[name\]-\[hash\].\[ext\]"

Customize chunk filenames

\--asset-naming

string

default:"\[name\]-\[hash\].\[ext\]"

Customize asset filenames

### Bundling Options

\--root

string

Root directory used when bundling multiple entry points

\--splitting

boolean

Enable code splitting for shared modules

\--public-path

string

Prefix to be added to import paths in bundled code

\--external

string

Exclude modules from the bundle (supports wildcards). Alias: `-e`

\--packages

string

default:"bundle"

How to treat dependencies: `external` or `bundle`

\--no-bundle

boolean

Transpile only — do not bundle

\--css-chunking

boolean

Chunk CSS files together to reduce duplication (only when multiple entry points import CSS)

### Minification & Optimization

\--emit-dce-annotations

boolean

default:"true"

Re-emit Dead Code Elimination annotations. Disabled when `—minify-whitespace` is used

\--minify

boolean

Enable all minification options

\--minify-syntax

boolean

Minify syntax and inline constants

\--minify-whitespace

boolean

Minify whitespace

\--minify-identifiers

boolean

Minify variable and function identifiers

\--keep-names

boolean

Preserve original function and class names when minifying

### Development Features

\--watch

boolean

Rebuild automatically when files change

\--no-clear-screen

boolean

Don’t clear the terminal when rebuilding with `—watch`

\--react-fast-refresh

boolean

Enable React Fast Refresh transform (for development testing)

### Standalone Executables

\--compile

boolean

Generate a standalone Bun executable containing the bundle. Implies `—production`

\--compile-exec-argv

string

Prepend arguments to the standalone executable’s `execArgv`

### Windows Executable Details

\--windows-hide-console

boolean

Prevent a console window from opening when running a compiled Windows executable

\--windows-icon

string

Set an icon for the Windows executable

\--windows-title

string

Set the Windows executable product name

\--windows-publisher

string

Set the Windows executable company name

\--windows-version

string

Set the Windows executable version (e.g. `1.2.3.4`)

\--windows-description

string

Set the Windows executable description

\--windows-copyright

string

Set the Windows executable copyright notice

### Experimental & App Building

\--app

boolean

**(EXPERIMENTAL)** Build a web app for production using Bun Bake

\--server-components

boolean

**(EXPERIMENTAL)** Enable React Server Components

\--debug-dump-server-files

boolean

When `—app` is set, dump all server files to disk even for static builds

\--debug-no-minify

boolean

When `—app` is set, disable all minification
