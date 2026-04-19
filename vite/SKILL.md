# Vite Documentation SKILL.md

## Overview

Vite is a modern front-end build tool that significantly improves web development workflow by offering lightning-fast development server start, hot module replacement (HMR), and optimized production builds. It leverages native ES modules and a plugin-extendable architecture to deliver a lean, high-performance developer experience.

---

## Key Concepts

- **Development Server:** Vite serves your source files over native ES modules, enabling instant server start and almost instant hot updates.
- **Pre-Bundling:** Dependencies are pre-bundled using esbuild to enable faster page loads and efficient import resolution.
- **Plugins:** Vite's plugin system is Rollup-compatible with extra Vite-specific capabilities, allowing powerful customizations.
- **Production Build:** Uses Rollup for highly optimized output and supports a range of advanced features out-of-the-box.
- **Asset Handling:** Handles static assets, CSS preprocessors, and patterns familiar from modern tooling.
- **Environment Variables:** Exposes `import.meta.env` for environment- and mode-specific variables.
- **SSR & Integration:** Supports server-side rendering and integration with backends.
- **Configuration:** Extensive configuration via `vite.config.js/ts` or direct API interfaces.

---

## Navigation Guide

**For Common Tasks:**

- **Getting Started & Philosophy:** Start with [Getting Started](vite/guide/index.md), [Philosophy](vite/guide/philosophy/index.md), and [Why Vite](vite/guide/why/index.md) for project context.
- **Features & CLI:** See [Features](vite/guide/features/index.md) for supported capabilities, [CLI](vite/guide/cli/index.md) for command usage.
- **Plugins:** For extending Vite, use [Using Plugins](vite/guide/using-plugins/index.md) and [Plugin API](vite/guide/api-plugin/index.md).
- **Assets & Build:** [Static Asset Handling](vite/guide/assets/index.md) and [Building for Production](vite/guide/build/index.md) for static resources and production deployment.
- **Environment & Modes:** Use [Env Variables and Modes](vite/guide/env-and-mode/index.md) for config differences across environments.
- **Advanced APIs:** Find [JavaScript API](vite/guide/api-javascript/index.md), [HMR API](vite/guide/api-hmr/index.md), and [Config Reference](vite/config/index.md) for programmatic/custom usage.
- **SSR & Backend:** [Server-Side Rendering (SSR)](vite/guide/ssr/index.md) and [Backend Integration](vite/guide/backend-integration/index.md) for full-stack and non-SPA cases.
- **Troubleshooting & Performance:** [Troubleshooting](vite/guide/troubleshooting/index.md) and [Performance](vite/guide/performance/index.md) for optimization and issue resolution.
- **Migration:** [Migration from v7](vite/guide/migration/index.md) for upgrade help.
- **Environment API:** [Environment API](vite/guide/api-environment/index.md) and related pages under `api-environment-*` for advanced/experimental uses.

---

## Most Important Pages

1. [Getting Started](vite/guide/index.md)  
   Quick setup and project bootstrap.
2. [Philosophy](vite/guide/philosophy/index.md)  
   Background on Vite's design and goals.
3. [Why Vite](vite/guide/why/index.md)  
   Problems Vite solves over previous generation tools.
4. [Features](vite/guide/features/index.md)  
   Highlights of what Vite supports out of the box.
5. [Command Line Interface](vite/guide/cli/index.md)  
   CLI commands and options.
6. [Using Plugins](vite/guide/using-plugins/index.md)  
   How to add and configure plugins.
7. [Dependency Pre-Bundling](vite/guide/dep-pre-bundling/index.md)  
   How Vite optimizes dependencies.
8. [Static Asset Handling](vite/guide/assets/index.md)  
   Working with images, fonts, CSS, and more.
9. [Building for Production](vite/guide/build/index.md)  
   How to create optimized production builds.
10. [Deploying a Static Site](vite/guide/static-deploy/index.md)  
    Steps for deploying Vite-built apps.
11. [Env Variables and Modes](vite/guide/env-and-mode/index.md)  
    Using environment variables and different modes.
12. [Server-Side Rendering (SSR)](vite/guide/ssr/index.md)  
    Guide to SSR setup in Vite-powered projects.
13. [Backend Integration](vite/guide/backend-integration/index.md)  
    Using Vite alongside, or integrated with, backend servers.
14. [Configuring Vite](vite/config/index.md)  
    Complete config file reference and structure.
15. [Plugin API](vite/guide/api-plugin/index.md)  
    Authoring plugins for Vite (dev and build phases).
16. [Performance](vite/guide/performance/index.md)  
    Diagnose and fix performance bottlenecks.
17. [Troubleshooting](vite/guide/troubleshooting/index.md)  
    Common issues and solutions.

---

## Notable Gotchas & Doc Structure Notes

- **Plugin Development:** Vite plugins should start with the [Plugin API](vite/guide/api-plugin/index.md) but may need Rollup API references as Vite's system extends Rollup.
- **Config Reference:** The main configuration details live under [Configuring Vite](vite/config/index.md). Some assets/static options are only referenced from feature guides ([Static Asset Handling](vite/guide/assets/index.md)), not directly in the config docs.
- **Environment API:** Advanced environment manipulation exists under `vite/guide/api-environment*`. These are in release-candidate phase and may be less stable.
- **Migration:** If updating from v7 or earlier, consult the [Migration from v7](vite/guide/migration/index.md) as core internals and defaults may have changed.
- **Backend Integration:** For non-SPA or traditional server projects, see [Backend Integration](vite/guide/backend-integration/index.md) early—Vite has patterns that differ from classic build tools.
- **Performance:** If you encounter slowness, [Performance](vite/guide/performance/index.md) offers targeted advice tailored for Vite (not generic JS optimizations).

---

Use these guides and references to answer developer questions, troubleshoot issues, and suggest best-practices for Vite-based web applications. For tasks outside the above shortlist, refer to the next-closest section according to the navigation guide.