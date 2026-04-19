# Bun Developer Docs Skill Guide

## Overview

Bun is a modern JavaScript runtime, package manager, and bundler designed for high performance and developer productivity. It aims to accelerate workflows for building, testing, and deploying JavaScript/TypeScript applications, with features like native bundling, hot reloading, and fast npm package installs.

---

## Key Concepts

- **Bundler**: Transpiles, bundles, and optimizes JavaScript/TypeScript/code and assets. Supports standalone executables, modern CSS features, and plugins.
- **Bytecode caching**: Compiles scripts to bytecode for faster startup and execution.
- **Hot reloading**: Enables hot module replacement (HMR) for rapid development feedback.
- **Standalone executables**: Compile entrypoints into single-file binaries for distribution.
- **Plugins**: Extend bundler and runtime with custom logic for loading/importing assets.
- **Module resolution**: Advanced resolving system for node modules, conditions, and environments.
- **Testing**: Built-in test runner with snapshot testing, coverage, and Jest compatibility.
- **Package management**: Fast npm-compatible CLI (bun install, bun outdated, etc.).
- **Deployment guides**: Step-by-step guides for deploying Bun apps on platforms like Render and Vercel.
- **TypeScript integration**: Native support and type definitions for Bun APIs.

---

## Navigation Guide

- **Getting Started / Installation**:
  - See [Install Bun](bun/bun/docs/installation/index.md) for setup instructions.
- **Bundling, Output, and Executables**:
  - For bundling options and standalone output see [Bundler](bun/bun/docs/bundler/index.md), [Single-file executable](bun/bun/docs/bundler/executables/index.md), and related bundler pages.
- **Fast development / HMR**:
  - [Hot reloading](bun/bun/docs/bundler/hot-reloading/index.md)
- **Plugins and Asset Handling**:
  - [Plugins](bun/bun/docs/bundler/plugins/index.md), [Loaders](bun/bun/docs/bundler/loaders/index.md), [CSS](bun/bun/docs/bundler/css/index.md)
- **Testing and Test Runner**:
  - [Writing tests](bun/bun/docs/test/writing-tests/index.md), [Snapshots](bun/bun/docs/test/snapshots/index.md), [Runtime behavior](bun/bun/docs/test/runtime-behavior/index.md)
- **TypeScript Usage**:
  - [TypeScript](bun/bun/docs/typescript/index.md)
- **Deployment & Ecosystem**:
  - Guides for Render, Vercel, Vite, etc. in [Deploy a Bun application on Render](bun/bun/docs/guides/deployment/render/index.md), [Build a frontend using Vite and Bun](bun/bun/docs/guides/ecosystem/vite/index.md)
- **Utilities & Advanced Features**:
  - [Get absolute path to current entrypoint](bun/bun/docs/guides/util/main/index.md), [Module Resolution](bun/bun/docs/runtime/module-resolution/index.md), [C Compiler](bun/bun/docs/runtime/c-compiler/index.md)
- **Package Management**:
  - [bun outdated](bun/bun/docs/pm/cli/outdated/index.md), [Install a package under a different name](bun/bun/docs/guides/install/npm-alias/index.md)

---

## Top Docs Pages

- [Install Bun](bun/bun/docs/installation/index.md): Step-by-step installation guide for Bun CLI and runtime
- [Bundler](bun/bun/docs/bundler/index.md): Overview and usage of Bun's bundling and compilation features
- [Single-file executable](bun/bun/docs/bundler/executables/index.md): Compile apps into standalone binaries
- [Bytecode Caching](bun/bun/docs/bundler/bytecode/index.md): Enhance performance via bytecode compilation
- [Hot reloading](bun/bun/docs/bundler/hot-reloading/index.md): Enable HMR for fast development cycles
- [Plugins](bun/bun/docs/bundler/plugins/index.md): Extend Bun's capabilities with custom plugins
- [CSS](bun/bun/docs/bundler/css/index.md): Handling and optimizing CSS, including modules and Tailwind
- [Loaders](bun/bun/docs/bundler/loaders/index.md): Handling non-js assets and import resolution
- [Minifier](bun/bun/docs/bundler/minifier/index.md): Code minification and advanced output options
- [Module Resolution](bun/bun/docs/runtime/module-resolution/index.md): Specify custom module loading/conditions
- [Writing tests](bun/bun/docs/test/writing-tests/index.md): Bun’s test runner API & usage patterns
- [Snapshots](bun/bun/docs/test/snapshots/index.md): Snapshot testing workflow and best practices
- [bun outdated](bun/bun/docs/pm/cli/outdated/index.md): Check for stale dependencies in your project
- [TypeScript](bun/bun/docs/typescript/index.md): Type definitions and configuration for Bun development
- [Deploy a Bun application on Render](bun/bun/docs/guides/deployment/render/index.md): Real-world deployment example guide

---

## Gotchas & Structure Quirks

- Many advanced features (plugins, custom loaders, bytecode, standalone executables) are in the `bun/bun/docs/bundler/` section.
- Deployment and ecosystem guides live under `bun/bun/docs/guides/`, not in the main API or bundler docs.
- Asset handling and plugin customization are tightly coupled but separated across `plugins`, `loaders`, and CSS pages.
- Test runner API and advanced test management are found under `bun/bun/docs/test/` – not under runtime.
- TypeScript compatibility is handled in its own page (not covered in guides).
- The package manager CLI docs (`bun outdated`, etc.) are found in `bun/bun/docs/pm/cli/`, not general guides.

---