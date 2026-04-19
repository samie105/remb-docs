# Deno Documentation Skill File

## Overview
Deno is a modern, secure JavaScript, TypeScript, and WebAssembly runtime, designed as an improved alternative to Node.js. It focuses on simplicity, out-of-the-box TypeScript support, explicit permissions, and portable modern tooling for web and server-side development.

---

## Key Concepts

- **TypeScript First:** Native TypeScript execution and tooling.
- **Security:** Explicit permissions required for file, network, and environment access.
- **Module System:** Supports ES Modules from URLs, npm compatibility, and JS standard library modules.
- **CLI Tooling:** Robust built-in tools for formatting, linting, testing, bundling, and more.
- **Configuration:** Uses `deno.json` for project/config, integrates with `package.json` for npm-like workflows.
- **Node Compatibility:** Runs many npm ecosystem packages and provides Node APIs.
- **WebAssembly/FFI:** Supports Wasm and foreign function interfaces.
- **Web Standard APIs:** Adopts browser APIs for cross-platform code.
- **Workspaces:** Supports monorepos and project grouping.
- **Publishing:** Easily publish packages via `deno publish` and JSR.

---

## Navigation Guide

- **Getting Started:** 
  - Basics, installation, and initial project steps: `deno/deno/runtime/getting_started/*`
- **Core Concepts:** 
  - Language features, security, modules, configuration: `deno/deno/runtime/fundamentals/*`
- **CLI Reference:** 
  - Details for each CLI command: `deno/deno/runtime/reference/cli/*`
- **Standard Library APIs:** 
  - For utilities and helpers: `deno/deno/runtime/reference/std/*`
- **Advanced Topics:** 
  - Web development, OpenTelemetry, FFI, Docker, LSP/VSCode integration: `deno/deno/runtime/reference/*`
- **Contributing & Internal:** 
  - Docs, architecture, profiling, release details: `deno/deno/runtime/contributing/*`
- **Help/FAQ:** 
  - Tips, troubleshooting: `deno/deno/runtime/help/index.md`

---

## Top Pages & Tasks

| Page                                                | Description                                                    |
|-----------------------------------------------------|----------------------------------------------------------------|
| [Welcome to Deno](deno/deno/runtime/index.md)       | Introduction to Deno, motivation, and first steps              |
| [Installation](deno/deno/runtime/getting_started/installation/index.md) | How to install Deno on your system                  |
| [First project](deno/deno/runtime/getting_started/first_project/index.md) | Creating your first project: init, run, test         |
| [Setup your environment](deno/deno/runtime/getting_started/setup_your_environment/index.md) | Configure shells/IDEs for Deno                    |
| [Command line interface](deno/deno/runtime/getting_started/command_line_interface/index.md) | Overview of CLI commands and permission flags        |
| [TypeScript](deno/deno/runtime/fundamentals/typescript/index.md) | TypeScript support, checking, compiling                |
| [Node](deno/deno/runtime/fundamentals/node/index.md) | Node/npm compatibility, using Node APIs                 |
| [Security](deno/deno/runtime/fundamentals/security/index.md) | Permissions model and secure execution                 |
| [Modules and dependencies](deno/deno/runtime/fundamentals/modules/index.md) | Import sources, dependency management, JSR/npm         |
| [Configuration](deno/deno/runtime/fundamentals/configuration/index.md) | Using `deno.json` and `package.json`                   |
| [Web development](deno/deno/runtime/fundamentals/web_dev/index.md) | Using Deno with web frameworks (React, Oak, etc.)      |
| [Testing](deno/deno/runtime/fundamentals/testing/index.md) | Built-in testing and coverage tools                    |
| [deno run](deno/deno/runtime/reference/cli/run/index.md) | Details for running scripts and granting permissions   |
| [deno test](deno/deno/runtime/reference/cli/test/index.md) | Running tests, test options, coverage                  |
| [deno publish](deno/deno/runtime/reference/cli/publish/index.md) | Publishing packages to JSR                             |
| [deno deploy](deno/deno/runtime/reference/cli/deploy/index.md) | Deploying projects with environment variables          |
| [HTTP Server](deno/deno/runtime/fundamentals/http_server/index.md) | Creating and managing HTTP servers                     |
| [Standard Library Overview](deno/deno/runtime/reference/std/index.md) | Entry point to utilities and standard APIs             |
| [Help](deno/deno/runtime/help/index.md)             | Troubleshooting, FAQ, links to additional assistance   |

---

## Gotchas & Doc Structure Quirks

- **CLI Commands:** Each CLI tool has its own reference page under `deno/deno/runtime/reference/cli/*`. Look here for specific command flags, usage, and advanced options.
- **Standard Library:** Modules are grouped under `deno/deno/runtime/reference/std/`. Each has its own page, e.g. `deno/deno/runtime/reference/std/fs/index.md` for filesystem utilities.
- **TypeScript Configuration:** Custom TypeScript options/tsconfig details are found in `deno/deno/runtime/reference/ts_config_migration/index.md`.
- **Node Compatibility:** Mixing Node/npm in Deno can have nuanced limitations; always check `fundamentals/node` and `reference/migration_guide`.
- **Web Frameworks:** The "Web development" page aggregates links to framework-specific guides; start there for React, Oak, Fresh, etc.
- **Publishing & Deploy:** `JSR` (Deno's package registry) publishing is in `deno publish`, deploy options are in `deno deploy`.
- **Permissions:** Deno's default security model restricts everything; see `fundamentals/security` and CLI command docs for correct flag usage.
- **Workspaces & Monorepos:** Managed in `fundamentals/workspaces`.

---

## Rapid Index by Task

- Install, update Deno: `getting_started/installation`, `reference/cli/update`
- Run scripts: `reference/cli/run`
- Work with npm: `fundamentals/node`, `reference/cli/add`
- Check/typecheck: `fundamentals/typescript`, `reference/cli/check`
- Manage dependencies: `fundamentals/modules`, `reference/cli/add`
- Set up project config: `fundamentals/configuration`
- Test and coverage: `fundamentals/testing`, `reference/cli/test`, `reference/cli/coverage`
- Format/lint: `fundamentals/linting_and_formatting`, `reference/cli/fmt`, `reference/cli/lint`
- Web servers/APIs: `fundamentals/http_server`, `fundamentals/web_dev`
- Publish/deploy: `reference/cli/publish`, `reference/cli/deploy`
- Troubleshooting: `help/index.md`