---
title: "deno types"
source: "https://docs.deno.com/runtime/reference/cli/types/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/types/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:56:37.605Z"
content_hash: "08d4a60bd6457d51b3ccfbf39a9fd549761a3d6225b227c95c174f6729efeaa7"
menu_path: ["deno types"]
section_path: []
nav_prev: {"path": "deno/deno/runtime/reference/cli/test/index.md", "title": "deno test"}
nav_next: {"path": "deno/deno/runtime/reference/cli/uninstall/index.md", "title": "deno uninstall"}
---

On this page

*   [Basic usage](#basic-usage)
*   [When to use this](#when-to-use-this)

`deno types` prints the TypeScript type declarations for all Deno-specific APIs. This is useful for editors and tools that need Deno's type information.

## Basic usage

Print type declarations to stdout:

\>\_

```sh
deno types
```

Save to a file for use with an editor or type checker:

\>\_

```sh
deno types > deno.d.ts
```

## When to use this

Most editors with the [Deno extension](/runtime/reference/vscode/) handle types automatically. You may need `deno types` if you are:

*   Using an editor without Deno LSP support
*   Generating type declarations for a build pipeline
*   Inspecting which APIs are available at your current Deno version

Command line usage:

```
deno types [OPTIONS]
```

Print runtime TypeScript declarations.

```
deno types > lib.deno.d.ts
```

The declaration file could be saved and used for typing information.

