---
title: "deno lsp"
source: "https://docs.deno.com/runtime/reference/cli/lsp/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/lsp/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:54:20.879Z"
content_hash: "d9939de159c6125811e71ae00f94a88ce5190a5177a47123984dcca13cc2dffd"
menu_path: ["deno lsp"]
section_path: []
---
On this page

*   [Usage](#usage)
*   [Editor setup](#editor-setup)

Info

Usually humans do not use this subcommand directly. The 'deno lsp' can provide IDEs with go-to-definition support and automatic code formatting.

Starts the Deno language server. The language server is used by editors to provide features like IntelliSense, code formatting, and more.

## Usage

\>\_

```sh
deno lsp
```

The language server communicates over stdin/stdout using the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/). You typically don't run this directly — your editor starts it automatically.

## Editor setup

For instructions on configuring your editor to use the Deno language server, see:

*   [Deno & VS Code](/runtime/reference/vscode/)
*   [LSP integration](/runtime/reference/lsp_integration/) for other editors
