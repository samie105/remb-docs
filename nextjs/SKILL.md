# Next.js Documentation Skill File

## Overview
Next.js is a React framework for building robust, optimized full-stack web applications. It solves complexity around routing, server/client rendering, data fetching, caching, and deployment, letting developers focus on building user interfaces rather than low-level tooling and configuration.

---

## Key Concepts

- **File-System Routing:** Pages and layouts are mapped directly to folders/files, making navigation and structure simple.
- **Server & Client Components:** Next.js distinguishes between components rendered server-side ("Server Components") and those running client-side ("Client Components"), optimizing for performance and code-splitting.
- **Data Fetching & Mutations:** Unified APIs allow fetching and mutating data from both server and client contexts, supporting static, dynamic, and hybrid approaches.
- **Caching & Revalidation:** Built-in caching primitives and revalidation strategies ensure performance and freshness for both SSR and SSG.
- **Optimizations:** Automatic handling for CSS, images, fonts, metadata, and OG images.
- **API Routes & Route Handlers:** Easily add backend endpoints within your frontend project.
- **Project Structure:** Convention-over-configuration, with strict file/folder rules for layouts, pages, API, and assets.

---

## Navigation Guide

- **Project Setup & Basics:** Start with [Getting Started](nextjs/docs/app/getting-started/index.md), [Installation](nextjs/docs/app/getting-started/installation/index.md), and [Project Structure](nextjs/docs/app/getting-started/project-structure/index.md).
- **UI & Routing:** Use [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md), [Linking and Navigating](nextjs/docs/app/getting-started/linking-and-navigating/index.md), and file convention docs under `app/api-reference/file-conventions/`.
- **Data Handling:** Check [Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md), [Mutating Data](nextjs/docs/app/getting-started/mutating-data/index.md), and API references for functions and directives.
- **Performance & Caching:** Refer to [Caching](nextjs/docs/app/getting-started/caching/index.md), [Revalidating](nextjs/docs/app/getting-started/revalidating/index.md), and corresponding guides.
- **Styling & Optimization:** See [CSS](nextjs/docs/app/getting-started/css/index.md), [Image Optimization](nextjs/docs/app/getting-started/images/index.md), and [Font Optimization](nextjs/docs/app/getting-started/fonts/index.md).
- **Error Handling & Utilities:** Use [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md) and check component/guides for best practices.
- **Deployment:** Visit [Deploying](nextjs/docs/app/getting-started/deploying/index.md) and platform-specific guides.

---

## Top 15 Essential Pages

1. [Next.js Docs](nextjs/docs/index.md)  
   General landing page and summary of what Next.js provides.

2. [Getting Started](nextjs/docs/app/getting-started/index.md)  
   Key entry point for new users; links to all core features.

3. [Installation](nextjs/docs/app/getting-started/installation/index.md)  
   Walkthrough on initializing and running a Next.js app locally.

4. [Project Structure](nextjs/docs/app/getting-started/project-structure/index.md)  
   Guidelines for folders, files, and conventions in Next.js apps.

5. [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md)  
   Details about routing, layouts, pages, and their relationship in the file system.

6. [Server and Client Components](nextjs/docs/app/getting-started/server-and-client-components/index.md)  
   How to split logic between server and client, and why it matters.

7. [Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md)  
   Approaches to fetching data on both server and client.

8. [Mutating Data](nextjs/docs/app/getting-started/mutating-data/index.md)  
   How to mutate state and data, including APIs and components.

9. [Caching](nextjs/docs/app/getting-started/caching/index.md)  
   Core caching strategies, including component-level and CDN.

10. [Revalidating](nextjs/docs/app/getting-started/revalidating/index.md)  
    Methods to revalidate cache and update content.

11. [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md)  
    Patterns for catching and displaying errors in Next.js.

12. [Route Handlers](nextjs/docs/app/getting-started/route-handlers/index.md)  
    How to define backend API endpoints in your Next.js app.

13. [API Reference](nextjs/docs/app/api-reference/index.md)  
    Detailed docs for all core components, directives, file conventions, and functions (see subpages).

14. [File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md)  
    Rules, patterns, and special files for routing, layouts, metadata, errors, etc.

15. [Deploying](nextjs/docs/app/getting-started/deploying/index.md)  
    Step-by-step process for deploying your application.

---

## Notable Gotchas & Structure Quirks

- **File Conventions Are Critical:** Many Next.js features are activated by naming files/folders in set ways. Route groups, segments, layouts, templates, and error boundaries must follow these conventions ([File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md)).
- **API Reference Is Split:** API docs are separated by "Directives", "Components", "File-system conventions", and "Functions". Always check the relevant subfolder for full details.
- **Guide vs. Getting Started:** The "Getting Started" section is best for learning basics and core app features. The "Guides" directory covers deep dives, platform integrations, security, testing, and migration topics.
- **Cache Components:** Caching strategies may differ depending on the version and whether "cacheComponents" is enabled. Refer to both [Caching](nextjs/docs/app/getting-started/caching/index.md) and [Caching (Previous Model)](nextjs/docs/app/guides/caching-without-cache-components/index.md) if relevant.
- **Migration Information:** If upgrading/migrating, consult the dedicated guides in [Migrating](nextjs/docs/app/guides/migrating/index.md) and [Upgrading](nextjs/docs/app/guides/upgrading/index.md), including versioned pages.

---