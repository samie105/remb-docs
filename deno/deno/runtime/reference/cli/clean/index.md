---
title: "deno clean"
source: "https://docs.deno.com/runtime/reference/cli/clean/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/clean/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:51:25.499Z"
content_hash: "77e8e031a10b5d59bd172da364cfb8c62bbd2b21b836d053c3c04785451d4fdf"
menu_path: ["deno clean"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/check/index.md", "title": "deno check"}
nav_next: {"path": "deno/deno/runtime/reference/cli/compile/index.md", "title": "deno compile"}
---

On this page

*   [Basic usage](#basic-usage)
*   [Dry run](#dry-run)
*   [Keeping specific caches](#keeping-specific-caches)
*   [When to use this](#when-to-use-this)
*   [Options](#options)
*   [Dependency management options](#dependency-management-options)

`deno clean` removes Deno's global module cache directory. See [Modules](/runtime/fundamentals/modules/) for more information about how Deno caches dependencies.

## Basic usage

\>\_

```sh
deno clean
```

## Dry run

Preview what would be deleted without actually removing anything:

\>\_

```sh
deno clean --dry-run
```

## Keeping specific caches

Use `--except` to preserve certain cache types while cleaning the rest:

\>\_

```sh
deno clean --except=npm,jsr
```

## When to use this

Use `deno clean` when you need to:

*   Resolve issues caused by corrupted or stale cached modules
*   Free disk space used by cached dependencies

Command line usage:

```
deno clean [OPTIONS] [except-paths]...
```

Remove the cache directory (`$DENO_DIR`)

## Options

`--dry-run`

Show what would be removed without performing any actions.

`--except, -e`

Retain cache data needed by the given files.

## Dependency management options

`--node-modules-dir`<MODE>optional

Sets the node modules management mode for npm packages.

`--vendor`<vendor>optional

Toggles local vendor folder usage for remote modules and a node\_modules folder for npm packages.
