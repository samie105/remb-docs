---
title: "deno lint"
source: "https://docs.deno.com/runtime/reference/cli/lint/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/lint/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:30:48.993Z"
content_hash: "c8021e7345668825d10b63f80584a050d9082f2ccd9141d11ea7af60194551f0"
menu_path: ["deno lint"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/jupyter/index.md", "title": "Jupyter Kernel for Deno"}
nav_next: {"path": "deno/runtime/reference/cli/outdated/index.md", "title": "deno outdated"}
---

**On this page**

-   [Basic usage](#basic-usage)
-   [Watch mode](#watch-mode)
-   [Using in CI](#using-in-ci)
-   [Available rules](#available-rules)
-   [Configuring rules in deno.json](#configuring-rules-in-deno.json)
-   [Including and excluding files](#including-and-excluding-files)
-   [Lint plugins](#lint-plugins)
-   [Ignore directives](#ignore-directives)
    -   [File level](#file-level)
    -   [Line level](#line-level)
-   [Ignore ban-unused-ignore itself](#ignore-ban-unused-ignore-itself)
-   [Linting options](#linting-options)
-   [Options](#options)
-   [File watching options](#file-watching-options)

Deno ships with a built-in linter that analyzes your code for potential errors, bugs, and stylistic issues. For a broader overview, see [Linting and Formatting](../../../fundamentals/linting_and_formatting/index.md).

## Basic usage

Lint all TypeScript and JavaScript files in the current directory:

\>\_

```sh
deno lint
```

Lint specific files or directories:

\>\_

```sh
deno lint src/ main.ts
```

## Watch mode

Automatically re-lint files when they change:

\>\_

```sh
deno lint --watch
```

## Using in CI

`deno lint` exits with a non-zero status code when it finds violations, making it suitable for CI pipelines:

\>\_

```sh
deno lint
deno fmt --check
deno test
```

## Available rules

Deno's linter includes over 100 rules. View all available rules:

\>\_

```sh
deno lint --rules
```

For a full list with documentation, visit the [lint rules](/lint/) reference.

## Configuring rules in `deno.json`

Customize which rules are active in your `deno.json`:

deno.json

```json
{
  "lint": {
    "rules": {
      "tags": ["recommended"],
      "include": ["ban-untagged-todo"],
      "exclude": ["no-unused-vars"]
    }
  }
}
```

-   **`tags`** — rule sets to enable. Available tags: `recommended`, `fresh`
-   **`include`** — additional individual rules to enable
-   **`exclude`** — rules to disable even if included by a tag

See the [Configuration](../../../fundamentals/configuration/index.md#linting) page for all available options.

## Including and excluding files

Specify which files to lint in `deno.json`:

deno.json

```json
{
  "lint": {
    "include": ["src/"],
    "exclude": ["src/testdata/", "src/generated/**/*.ts"]
  }
}
```

You can also exclude files from the command line:

\>\_

```sh
deno lint --ignore=dist/,build/
```

## Lint plugins

You can extend the linter with custom rules using [lint plugins](../../lint_plugins/index.md).

## Ignore directives

### File level

To ignore a whole file use `// deno-lint-ignore-file` at the top of the file:

```ts
// deno-lint-ignore-file

function foo(): any {
  // ...
}
```

You can also specify the reason for ignoring the file:

```ts
// deno-lint-ignore-file -- reason for ignoring

function foo(): any {
  // ...
}
```

The ignore directive must be placed before the first statement or declaration:

```ts
// Copyright 2018-2024 the Deno authors. All rights reserved. MIT license.

/**
 * Some JS doc
 */

// deno-lint-ignore-file

import { bar } from "./bar.js";

function foo(): any {
  // ...
}
```

You can also ignore certain diagnostics in the whole file:

```ts
// deno-lint-ignore-file no-explicit-any no-empty

function foo(): any {
  // ...
}
```

If there are multiple `// deno-lint-ignore-file` directives, all but the first one are ignored:

```ts
// This is effective
// deno-lint-ignore-file no-explicit-any no-empty

// But this is NOT effective
// deno-lint-ignore-file no-debugger

function foo(): any {
  debugger; // not ignored!
}
```

### Line level

To ignore specific diagnostics use `// deno-lint-ignore <codes...>` on the preceding line of the offending line.

```ts
// deno-lint-ignore no-explicit-any
function foo(): any {
  // ...
}

// deno-lint-ignore no-explicit-any explicit-function-return-type
function bar(a: any) {
  // ...
}
```

You must specify the names of the rules to be ignored.

You can also specify the reason for ignoring the diagnostic:

```ts
// deno-lint-ignore no-explicit-any -- reason for ignoring
function foo(): any {
  // ...
}
```

## Ignore `ban-unused-ignore` itself

`deno lint` provides [`ban-unused-ignore` rule](/lint/rules/ban-unused-ignore/), which will detect ignore directives that don't ever suppress certain diagnostics. This is useful when you want to discover ignore directives that are no longer necessary after refactoring the code.

In a few cases, however, you might want to ignore `ban-unused-ignore` rule itself. One of the typical cases would be when working with auto-generated files; it makes sense to add file-level ignore directives for some rules, and there's almost no need for detecting unused directives via `ban-unused-ignore` in this case.

You can use `// deno-lint-ignore-file ban-unused-ignore` as always if you want to suppress the rule for a whole file:

```ts
// deno-lint-ignore-file ban-unused-ignore no-explicit-any

// `no-explicit-any` isn't used but you'll get no diagnostics because of ignoring
// `ban-unused-ignore`
console.log(42);
```

Do note that ignoring `ban-unused-ignore` itself only works via file-level ignore directives. This means that per line directives, like `// deno-lint-ignore ban-unused-ignore`, don't work at all. If you want to ignore `ban-unused-ignore` for some special reasons, make sure to add it as a file-level ignore directive.

Command line usage:

```
deno lint [OPTIONS] [files]...
```

Lint JavaScript/TypeScript source code.

```
deno lint
```

```
deno lint myfile1.ts myfile2.js
```

Print result as JSON:

```
deno lint --json
```

Read from stdin:

```
cat file.ts | deno lint -
```

```
cat file.ts | deno lint --json -
```

List available rules:

```
deno lint --rules
```

To ignore specific diagnostics, you can write an ignore comment on the preceding line with a rule name (or multiple):

```
// deno-lint-ignore no-explicit-any
```

```
// deno-lint-ignore require-await no-empty
```

To ignore linting on an entire file, you can add an ignore comment at the top of the file:

```
// deno-lint-ignore-file
```

## Linting options

`--compact`

Output lint result in compact format.

`--fix`

Fix any linting errors for rules that support it.

`--ignore`<ignore>

Ignore linting particular source files.

`--json`

Output lint result in JSON format.

`--rules`

List available rules.

`--rules-exclude`<rules-exclude>

Exclude lint rules.

`--rules-include`<rules-include>

Include lint rules.

`--rules-tags`<rules-tags>

Use set of rules with a tag.

## Options

`--allow-import, -I`<IP\_OR\_HOSTNAME>optional

Allow importing from remote hosts. Optionally specify allowed IP addresses and host names, with ports as necessary. Default value: deno.land:443,[jsr.io:443](http://jsr.io:443),[esm.sh:443](http://esm.sh:443),[raw.esm.sh:443](http://raw.esm.sh:443),[cdn.jsdelivr.net:443](http://cdn.jsdelivr.net:443),[raw.githubusercontent.com:443](http://raw.githubusercontent.com:443),[gist.githubusercontent.com:443](http://gist.githubusercontent.com:443).

`[--config, -c](< https://docs.deno.com/go/config>)`<FILE>

Configure different aspects of deno including TypeScript, linting, and code formatting. Typically the configuration file will be called `deno.json` or `deno.jsonc` and automatically detected; in that case this flag is not necessary.

`--deny-import`<IP\_OR\_HOSTNAME>optional

Deny importing from remote hosts. Optionally specify denied IP addresses and host names, with ports as necessary.

`--ext`<EXT>

Specify the file extension to lint when reading from stdin.For example, use `jsx` to lint JSX files or `tsx` for TSX files.This argument is necessary because stdin input does not automatically infer the file type.Example usage: `cat file.jsx | deno lint -` --ext=jsx`.`

`--no-config`

Disable automatic loading of the configuration file.

`--permit-no-files`

Don't return an error code if no files were found.

## File watching options

`--no-clear-screen`

Do not clear terminal screen when under watch mode.

`--watch`

Watch for file changes and restart process automatically. Only local files from entry point module graph are watched.

`--watch-exclude`<FILES>optional

Exclude provided files/patterns from watch mode.
