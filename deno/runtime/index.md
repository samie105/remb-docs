---
title: "Welcome to Deno"
source: "https://docs.deno.com/runtime/"
canonical_url: "https://docs.deno.com/runtime/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:01:51.456Z"
content_hash: "bf8b12eaf4326835a6f0a5652e43071216740394d4695b19e66859cac8887514"
menu_path: ["Welcome to Deno"]
section_path: []
content_language: "en"
---
**On this page**

-   [Why Deno?](#why-deno%3F)
-   [Quick install](#quick-install)
-   [First steps](#first-steps)

[Deno](https://deno.com) ([/ˈdiːnoʊ/](https://ipa-reader.com/?text=%CB%88di%CB%90no%CA%8A), pronounced `dee-no`) is an [open source](https://github.com/denoland/deno/blob/main/LICENSE.md) JavaScript, TypeScript, and WebAssembly runtime with secure defaults and a great developer experience. It's built on [V8](https://v8.dev/), [Rust](https://www.rust-lang.org/), and [Tokio](https://tokio.rs/).

## Why Deno?

-   Deno is **[TypeScript-ready out of the box](/runtime/fundamentals/typescript/).** Zero config or additional steps necessary.
-   Deno is **[secure by default](/runtime/fundamentals/security/).** Where other runtimes give full access every script they run, Deno allows you to enforce granular permissions.
-   Deno has a **robust built-in toolchain.** Unlike Node or browser JavaScript, Deno includes a [standard library](/runtime/reference/std/), along with a first-party [linter/formatter](/runtime/fundamentals/linting_and_formatting/), [test runner](/runtime/fundamentals/testing/), and more.
-   Deno is **fully compatible with [Node and npm](/runtime/fundamentals/node/).**
-   Deno is **fast and reliable**.
-   **[Deno is open-source](https://github.com/denoland/deno).**

## Quick install

Install the Deno runtime on your system using one of the terminal commands below:

\>\_

```sh
curl -fsSL https://deno.land/install.sh | sh
```

In Windows PowerShell:

```powershell
irm https://deno.land/install.ps1 | iex
```

\>\_

```sh
curl -fsSL https://deno.land/install.sh | sh
```

[Additional installation options can be found here](/runtime/getting_started/installation/). After installation, you should have the `deno` executable available on your system path. You can verify the installation by running:

\>\_

```sh
deno --version
```

## First steps

Deno can run JavaScript and [TypeScript](https://www.typescriptlang.org/) with no additional tools or configuration required, all in a secure, batteries-included runtime.

-   [Making a Deno project](/runtime/getting_started/first_project/)
-   [Setting up your environment](/runtime/getting_started/setup_your_environment/)
-   [Using the CLI](/runtime/getting_started/command_line_interface)
