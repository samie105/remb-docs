---
title: "deno create"
source: "https://docs.deno.com/runtime/reference/cli/create/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/create/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:28:03.815Z"
content_hash: "6a2a02a89bd53c54097186d70477616eef86ee48646bf7c4e2a2149cb1e86e49"
menu_path: ["deno create"]
section_path: []
content_language: "en"
nav_prev: {"path": "../compile/index.md", "title": "deno compile"}
nav_next: {"path": "../completions/index.md", "title": "deno completions"}
---

**On this page**

-   [Usage](#usage)
-   [How it works](#how-it-works)
-   [Examples](#examples)
-   [Flags](#flags)
-   [Options](#options)

The `deno create` command scaffolds a new project from a template package. It works with both [JSR](https://jsr.io/) and [npm](https://www.npmjs.com/) packages that provide project templates.

## Usage

\>\_

```sh
deno create [OPTIONS] [PACKAGE] [-- [ARGS]...]
```

By default, unprefixed package names are resolved from JSR. You can use the `npm:` or `jsr:` prefix to be explicit, or use the `--npm` / `--jsr` flags.

## How it works

Package resolution differs between npm and JSR:

-   **npm packages** use the `create-` naming convention. Running `deno create npm:vite` resolves to the `create-vite` package on npm and executes its main entry point.
-   **JSR packages** use the `./create` export. Any JSR package can act as a template by defining a `./create` entry point in its [`deno.json`](/runtime/fundamentals/configuration/):

deno.json

```json
{
  "name": "@my-scope/my-template",
  "version": "1.0.0",
  "exports": {
    ".": "./mod.ts",
    "./create": "./create.ts"
  }
}
```

When you run `deno create @my-scope/my-template`, Deno looks for the `./create` export and runs it as the scaffolding script.

## Examples

Create a project from a JSR package:

\>\_

```sh
deno create @fresh/init
```

Create a project from an npm package:

\>\_

```sh
deno create npm:vite my-app
```

Using the `--npm` flag to treat unprefixed names as npm packages:

\>\_

```sh
deno create --npm create-vite my-app
```

Pass arguments to the template package:

\>\_

```sh
deno create @fresh/init -- --force
```

## Flags

-   `--npm` - Treat unprefixed package names as npm packages
-   `--jsr` - Treat unprefixed package names as JSR packages (default)
-   `-y, --yes` - Bypass the prompt and run with full permissions

Command line usage:

```
deno create [OPTIONS] [PACKAGE] [-- [ARGS]...]
```

scaffolds a project from a package

## Options

`--jsr`

Treat unprefixed package names as JSR packages.

`--npm`

Treat unprefixed package names as npm packages.

`--yes, -y`

Bypass the prompt and run with full permissions.
