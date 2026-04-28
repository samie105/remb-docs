---
title: "deno remove"
source: "https://docs.deno.com/runtime/reference/cli/remove/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/remove/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:31:53.802Z"
content_hash: "2381346d5b24fe1ca909b8181e19dcd54e33cd7f1588ece4a3e16c90c949909a"
menu_path: ["deno remove"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/cli/lsp/index.md", "title": "deno lsp"}
nav_next: {"path": "deno/runtime/reference/cli/repl/index.md", "title": "deno repl"}
---

**On this page**

-   [Basic usage](#basic-usage)
-   [Where dependencies are removed from](#where-dependencies-are-removed-from)
-   [Dependency management options](#dependency-management-options)
-   [Options](#options)

`deno remove` removes dependencies from your project's configuration file. It is the inverse of [`deno add`](/runtime/reference/cli/add/).

## Basic usage

Remove a package:

\>\_

```sh
deno remove @std/path
```

Remove multiple packages at once:

\>\_

```sh
deno remove @std/path @std/assert npm:express
```

## Where dependencies are removed from

`deno remove` will look at both [`deno.json`](/runtime/fundamentals/configuration/) and `package.json` (if present) and remove the matching dependency from whichever file it is found in.

Command line usage:

```
deno remove [OPTIONS] [packages]...
```

Remove dependencies from the configuration file.

```
deno remove @std/path
```

You can remove multiple dependencies at once:

```
deno remove @std/path @std/assert
```

## Dependency management options

`--frozen`<BOOLEAN>optional

Error out if lockfile is out of date.

`--lock`<FILE>optional

Check the specified lock file. (If value is not provided, defaults to "./deno.lock").

`--no-lock`

Disable auto discovery of the lock file.

## Options

`--lockfile-only`

Install only updating the lockfile.
