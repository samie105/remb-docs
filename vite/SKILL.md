## Overview

Vite is a modern frontend build tool that provides an extremely fast ESM-based development server and optimized production builds powered by Rollup. It offers a lean, extensible core designed to push modern web standards while remaining framework-agnostic. An agent needs to know Vite to scaffold projects, configure builds, manage assets, and extend functionality through its plugin and environment APIs.

## Mental Model

Vite separates development and production concerns while unifying them through a plugin-driven Environment API. Development leverages native ES modules with dependency pre-bundling and Hot Module Replacement; production uses aggressively optimized Rollup chunking. The architecture is intentionally lean, pushing framework-specific logic into plugins and custom environment instances. Canonical pages: `vite/guide/philosophy/index.md`, `vite/guide/why/index.md`, `vite/guide/api-environment/index.md`, `vite/guide/api-plugin/index.md`.

## Learning Paths

### Getting Started
1. `vite/guide/why/index.md`
2. `vite/guide/features/index.md`
3. `vite/config/shared-options/index.md`
4. `vite/guide/using-plugins/index.md`

### Production Ready
1. `vite/guide/build/index.md`
2. `vite/config/build-options/index.md`
3. `vite/guide/assets/index.md`
4. `vite/guide/dep-pre-bundling/index.md`
5. `vite/config/dep-optimization-options/index.md`

### Reference Deep-Dive
1. `vite/config/index.md`
2. `vite/guide/api-environment/index.md`
3. `vite/guide/api-plugin/index.md`
4. `vite/guide/api-hmr/index.md`
5. `vite/guide/api-environment-plugins/index.md`

## Concept Map

- Philosophy & Motivation
  - Why Vite: `vite/guide/why/index.md`
  - Project Philosophy: `vite/guide/philosophy/index.md`
- Configuration
  - Configuring Vite: `vite/config/index.md`
  - Shared Options: `vite/config/shared-options/index.md`
  - Server Options: `vite/config/server-options/index.md`
  - Preview Options: `vite/config/preview-options/index.md`
  - Build Options: `vite/config/build-options/index.md`
  - Dep Optimization Options: `vite/config/dep-optimization-options/index.md`
- Development
  - Features: `vite/guide/features/index.md`
  - HMR API: `vite/guide/api-hmr/index.md`
  - Dependency Pre-Bundling: `vite/guide/dep-pre-bundling/index.md`
- Production & Assets
  - Building for Production: `vite/guide/build/index.md`
  - Static Asset Handling: `vite/guide/assets/index.md`
- Extending Vite
  - Using Plugins: `vite/guide/using-plugins/index.md`
  - Plugin API: `vite/guide/api-plugin/index.md`
  - Environment API for Plugins: `vite/guide/api-environment-plugins/index.md`
- Advanced Environments
  - Environment API: `vite/guide/api-environment/index.md`
  - SSR: `vite/guide/ssr/index.md`
  - Env Variables and Modes: `vite/guide/env-and-mode/index.md`
  - Backend Integration: `vite/guide/backend-integration/index.md`

## If You Need To...

| If you need to... | Read |
|---|---|
| Configure the dev server | `vite/config/server-options/index.md` |
| Configure build output | `vite/config/build-options/index.md` |
| Optimize dependencies | `vite/config/dep-optimization-options/index.md` |
| Handle static assets | `vite/guide/assets/index.md` |
| Set up a production build | `vite/guide/build/index.md` |
| Add or author plugins | `vite/guide/using-plugins/index.md`, `vite/guide/api-plugin/index.md` |
| Use environment variables | `vite/guide/env-and-mode/index.md` |
| Implement SSR | `vite/guide/ssr/index.md` |
| Understand the Environment API | `vite/guide/api-environment/index.md` |
| Set up HMR in custom code | `vite/guide/api-hmr/index.md` |
| Integrate with a backend | `vite/guide/backend-integration/index.md` |

## Top Must-Know Pages

1. `vite/config/index.md` — Entry point for configuration patterns including intellisense, conditional config, and async config.
2. `vite/config/shared-options/index.md` — Defines root, base, mode, define, and plugins used across all projects.
3. `vite/config/build-options/index.md` — Controls production output via build.target, build.outDir, build.assetsDir, and module preloading.
4. `vite/config/server-options/index.md` — Configures the development server host, port, HTTPS, and strictPort behavior.
5. `vite/guide/build/index.md` — Explains browser compatibility, public base paths, chunking strategy, and production customization.
6. `vite/guide/api-plugin/index.md` — Core reference for plugin conventions, hooks, transforming custom files, and virtual modules.
7. `vite/guide/api-environment/index.md` — Formalizes environments and unifies dev/build behavior through the Environment API.
8. `vite/guide/dep-pre-bundling/index.md` — Describes why and how Vite pre-bundles dependencies for fast ESM development.
9. `vite/guide/assets/index.md` — Covers importing assets as URLs, strings, workers, and explicit inline handling.
10. `vite/guide/features/index.md` — Surveys supported features like CSS preprocessors, Lightning CSS, and client types.