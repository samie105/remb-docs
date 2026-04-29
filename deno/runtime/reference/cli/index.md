---
title: "Deno CLI Subcommands"
source: "https://docs.deno.com/runtime/reference/cli/"
canonical_url: "https://docs.deno.com/runtime/reference/cli/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:25:04.133Z"
content_hash: "5862e25c07cab47ee00488464b3e76f73d8609e8f036b6c957376568c814b221"
menu_path: ["Deno CLI Subcommands"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/web/workers/index.md", "title": "Workers - Web documentation"}
nav_next: {"path": "deno/runtime/reference/cli/env_variables/index.md", "title": "Environment variables"}
---

**On this page**

-   [Execution](#execution)
-   [Dependency management](#dependency-management)
-   [Tooling](#tooling)
-   [Other](#other)

The Deno CLI (Command Line Interface) allows you to interact with the Deno runtime environment from your terminal or command prompt. The CLI has a number of subcommands that can be used to perform different tasks, check the links below for more information on each subcommand.

## Execution

-   [deno run](run/index.md) - run a script
-   [deno serve](serve/index.md) - run a web server
-   [deno task](task/index.md) - run a task
-   [deno repl](repl/index.md) - starts a read-eval-print-loop
-   [deno eval](eval/index.md) - evaluate provided script

## Dependency management

-   [deno add](add/index.md) - add dependencies
-   [deno approve-scripts](approve_scripts/index.md) - manage lifecycle scripts of npm packages
-   [deno audit](audit/index.md) - audit dependencies
-   deno cache - _(Deprecated. Please use [deno install](install/index.md))_
-   [deno install](install/index.md) - install a dependency or a script
-   [deno uninstall](uninstall/index.md) - uninstall a dependency or a script
-   [deno remove](remove/index.md) - Remove dependencies
-   [deno outdated](outdated/index.md) - view or update outdated dependencies

## Tooling

-   [deno bench](bench/index.md) - benchmarking tool
-   [deno check](check/index.md) - type check your program without running it
-   [deno compile](compile/index.md) - compile a program into a standalone executable
-   [deno completions](completions/index.md) - generate shell completions
-   [deno coverage](coverage/index.md) - generate test coverage reports
-   [deno create](create/index.md) - scaffold a new project from a template
-   [deno doc](doc/index.md) - generate documentation for a module
-   [deno deploy](deploy/index.md) - Manage and publish your projects on the web
-   [deno fmt](fmt/index.md) - format your code
-   [deno info](info/index.md) - inspect an ES module and all of its dependencies
-   [deno init](init/index.md) - create a new project
-   [deno jupyter](jupyter/index.md) - run a Jupyter notebook
-   [deno lint](lint/index.md) - lint your code
-   [deno lsp](lsp/index.md) - language server protocol integration
-   [deno publish](publish/index.md) - publish a module to JSR
-   [deno test](test/index.md) - run your tests
-   [deno types](types/index.md) - print runtime types
-   [deno upgrade](upgrade/index.md) - upgrade Deno to the latest version
-   [deno x](x/index.md) - run an npm or JSR package

## Other

-   [Unstable feature flags](unstable_flags/index.md)
-   [Integrating the Deno LSP](../lsp_integration/index.md)
