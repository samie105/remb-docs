---
title: "Set up your environment"
source: "https://docs.deno.com/runtime/getting_started/setup_your_environment/"
canonical_url: "https://docs.deno.com/runtime/getting_started/setup_your_environment/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:24:18.140Z"
content_hash: "78289ca573400f9c191dc6bdbe32af05bd006027eb6bd135aee66cef40e4a3f1"
menu_path: ["Set up your environment"]
section_path: []
content_language: "en"
nav_prev: {"path": "../first_project/index.md", "title": "Making a Deno project"}
nav_next: {"path": "../command_line_interface/index.md", "title": "Command line interface"}
---

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

antigen bundle deno
```

### fish example

Output the completions to a `deno.fish` file into the completions directory in the fish config folder:

```shell
> deno completions fish > ~/.config/fish/completions/deno.fish
```

## Other tools

If you are writing or supporting a community integration using the Deno language server, read more about [integrating with the Deno LSP](/runtime/reference/lsp_integration/), but also feel free to join our [Discord community](https://discord.gg/deno) in the `#dev-lsp` channel.
