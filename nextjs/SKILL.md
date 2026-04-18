# Next.js SKILL

## 1. What is Next.js and What Problems Does It Solve

Next.js is a React-based framework designed for building performant, scalable web applications. It streamlines server-side rendering (SSR), static site generation (SSG), and client-side rendering, enabling developers to create fast, SEO-friendly, and user-centric apps. It solves key problems such as:

- Automatic routing and filesystem-based conventions
- Hybrid rendering strategies (SSR, SSG, ISR)
- Data fetching and caching optimizations
- Image, font, and asset optimization
- Seamless deployment integrations
- Support for edge functions and serverless architecture
- Developer productivity with fast refresh, debugging, and testing tools

## 2. Documentation Structure Overview

The Next.js docs are organized roughly into these main parts:

- **Getting Started** (`nextjs/docs/app/getting-started/`): Basic setup and core concepts for beginners, including installation, project structure, routing, data fetching, caching, deployment, and error handling.
- **Guides** (`nextjs/docs/app/guides/`): In-depth tutorials and best practices on specific topics such as authentication, caching strategies, debugging, deployment, internationalization, testing, migration, performance, and security.
- **API Reference** (`nextjs/docs/app/api-reference/`): Comprehensive reference for Next.js core APIs including components (e.g., Image, Link), directives (e.g., `use client`), file-system conventions (routing, layouts, dynamic segments), configuration options (`next.config.js`), and low-level functions for routing, caching, and metadata.
- **Messages & Errors** (`nextjs/docs/messages/`): Error and warning explanations to help diagnose common issues.
- **Version & Upgrade Guides** (`nextjs/docs/app/guides/upgrading/`): Guides on transitioning between Next.js versions and applying codemods.

## 3. Navigation Strategy for Common Developer Questions

- **Getting Started questions** (setup, routing basics, data fetching, SSR/SSG): Start under [Getting Started](nextjs/docs/app/getting-started/index.md) and its subpages like [Installation](nextjs/docs/app/getting-started/installation/index.md), [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md), or [Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md).
- **How to implement a specific feature or follow best practices**: Search under [Guides](nextjs/docs/app/guides/index.md), where targeted topics like [Authentication](nextjs/docs/app/guides/authentication/index.md) or [Caching](nextjs/docs/app/guides/cdn-caching/index.md) live.
- **API details or usage**: Go to [API Reference](nextjs/docs/app/api-reference/index.md) for specifics. Use:
  - Components: `components/`
  - Directives (e.g., `use client`): `directives/`
  - File conventions (routing files, layouts): `file-conventions/`
  - Configuration modules: `config/next-config-js/`
  - Functions (fetch, redirect, cookies): `functions/`
- **Error messages and diagnostics**: Check the messages directory (`docs/messages/`) for detailed explanations.
- **Upgrading and migration**: Use [Upgrading](nextjs/docs/app/guides/upgrading/index.md) and related version-specific upgrade guides.

## 4. Most Important Pages and Concepts

### Core Concepts and Getting Started

- [Getting Started](nextjs/docs/app/getting-started/index.md) – overview and starting point
- [Project Structure](nextjs/docs/app/getting-started/project-structure/index.md) – explains the file/folder layout
- [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md) – routing and page design
- [Server and Client Components](nextjs/docs/app/getting-started/server-and-client-components/index.md) – critical React concepts in Next.js
- [Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md) and [Mutating Data](nextjs/docs/app/getting-started/mutating-data/index.md)
- [Caching](nextjs/docs/app/getting-started/caching/index.md) and [Revalidating](nextjs/docs/app/getting-started/revalidating/index.md)
- [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md)
- [Deploying](nextjs/docs/app/getting-started/deploying/index.md)

### Key Guides

- [Authentication](nextjs/docs/app/guides/authentication/index.md)
- [Debugging](nextjs/docs/app/guides/debugging/index.md)
- [Environment Variables](nextjs/docs/app/guides/environment-variables/index.md)
- [Incremental Static Regeneration (ISR)](nextjs/docs/app/guides/incremental-static-regeneration/index.md)
- [Rendering Philosophy](nextjs/docs/app/guides/rendering-philosophy/index.md)
- [Testing](nextjs/docs/app/guides/testing/index.md) with subpages on Jest, Playwright, Cypress etc.
- [Migrating](nextjs/docs/app/guides/migrating/index.md) and sub-guides for specific migrations

### API Reference Essentials

- [File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md) (routing, layouts, error handling files)
- [Components](nextjs/docs/app/api-reference/components/index.md) (Image, Link, Script, Font)
- [Directives](nextjs/docs/app/api-reference/directives/index.md) (e.g. `use client`, `use server`)
- [Functions](nextjs/docs/app/api-reference/functions/index.md) (redirect, notFound, cookies, revalidatePath)
- [Configuration](nextjs/docs/app/api-reference/config/index.md), especially [`next.config.js`](nextjs/docs/app/api-reference/config/next-config-js/index.md) and its options

## 5. Gotchas and Non-Obvious Documentation Structure Details

- **File-system conventions are key** for understanding routing, layouts, loading states, error handling, and metadata; these live under `api-reference/file-conventions`. This is fundamental to Next.js app structure but may require piecing together from multiple files (e.g., `page.js`, `layout.js`, `loading.js`, `error.js`).
- **Directives control rendering behavior** (`use client`, `use server`) and are documented separately under `api-reference/directives`, crucial for React Server Components compatibility.
- **Incremental Static Regeneration and caching are covered in both `getting-started` and `guides`**, but the detailed mechanics (like revalidation) live under [How Revalidation Works](nextjs/docs/app/guides/how-revalidation-works/index.md) and related guides.
- **API Reference is highly granular and splits logically by feature** (components, functions, config) instead of monolithic docs, so knowing where to look is important.
- **Migration guides are subdivided by source (e.g., from Create React App, Vite) and by feature (App Router migration, Cache Components migration)** to ease incremental adoption rather than all-in-one listings.
- **Some error explanations and "messages" are separate from main docs**, so for troubleshooting specific runtime or build errors, check `docs/messages/` early.
- **The docs expect familiarity with React basics and concepts such as Server Components**, so assimilate "Getting Started" pages on Server and Client Components early for context.
- **Metadata and SEO specifics have their own files under file conventions and guides**, important for rich previews and site indexing.

---

This SKILL file should help an AI agent orient itself efficiently in the Next.js docs, enabling targeted lookups based on typical developer intents and issues.