# Next.js Developer Skill Guide

## Overview

Next.js is a React framework for building full-stack web applications. It enables developers to create performant, scalable apps with features like server-side rendering, routing, API routes, data fetching, and robust optimizations—all with minimal configuration. The documentation provides thorough guidance from basic setup to advanced concepts, covering both the App Router and legacy models.

---

## Key Concepts

- **File-System Routing**: Routes are defined by folder and file structure in the `app` directory, making navigation and component organization straightforward.
- **Server and Client Components**: Next.js distinguishes between components rendered on the server vs. client for optimal performance and flexibility.
- **Data Fetching and Mutating**: Multiple patterns for getting and updating data on both server and client, supporting static, dynamic, and incremental approaches.
- **Caching & Revalidation**: Built-in mechanisms to cache responses and revalidate content, with support for granular control and CDN integration.
- **Layouts & Pages**: Nest reusable layouts and create pages via convention (`layout.js`, `page.js`) for predictable UI structures.
- **Error Handling**: Standardized error boundaries, error-specific files, and custom logic for robust UX.
- **Optimization**: Native support for image, font, and metadata optimization; efficient bundling and streaming.
- **API Reference**: Comprehensive documentation on directives, components, file conventions, and route configurations.
- **Migration & Upgrading**: Guides for moving from older architectures or other frameworks (Vite, CRA), and version-specific upgrade paths.

---

## Navigation Guide

- **Setup, Basics, App Structure**:  
  See [Getting Started](nextjs/docs/app/getting-started/index.md) and its child pages for installation, project structure, and basic routing.

- **Data Handling (Fetching, Mutating, Caching, Revalidation)**:  
  Use the "Getting Started" subpages ([Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md), [Mutating Data](nextjs/docs/app/getting-started/mutating-data/index.md), [Caching](nextjs/docs/app/getting-started/caching/index.md), [Revalidating](nextjs/docs/app/getting-started/revalidating/index.md)) and relevant API reference entries.

- **Routing & Navigation**:  
  Refer to [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md), [Linking and Navigating](nextjs/docs/app/getting-started/linking-and-navigating/index.md), and [API Reference > File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md) for file-based routing and route groups.

- **Optimizations & UI**:  
  [Image Optimization](nextjs/docs/app/getting-started/images/index.md), [Font Optimization](nextjs/docs/app/getting-started/fonts/index.md), [CSS](nextjs/docs/app/getting-started/css/index.md), and component guides.

- **Error Handling**:  
  [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md) and API Reference files like [`error.js`](nextjs/docs/app/api-reference/file-conventions/error/index.md).

- **API Usage & Advanced Configuration**:  
  Visit [API Reference](nextjs/docs/app/api-reference/index.md), with detailed docs on directives, components, file conventions, and route segment config.

- **Guides**:  
  [Guides](nextjs/docs/app/guides/index.md) cover analytics, authentication, security, migration, deployment, dev tooling, advanced caching, and various integrations.

---

## Top 15 Most Important Pages

1. [Getting Started](nextjs/docs/app/getting-started/index.md)  
   Entry point to foundational concepts, first project setup.
2. [Installation](nextjs/docs/app/getting-started/installation/index.md)  
   Step-by-step guide to starting a Next.js app.
3. [Project Structure](nextjs/docs/app/getting-started/project-structure/index.md)  
   Explains file/folder conventions and app organization.
4. [Layouts and Pages](nextjs/docs/app/getting-started/layouts-and-pages/index.md)  
   How routing and UI structure work; page and layout conventions.
5. [Linking and Navigating](nextjs/docs/app/getting-started/linking-and-navigating/index.md)  
   Client-side navigation, Link component, route renders.
6. [Server and Client Components](nextjs/docs/app/getting-started/server-and-client-components/index.md)  
   Component types, boundaries, usage patterns.
7. [Fetching Data](nextjs/docs/app/getting-started/fetching-data/index.md)  
   Data fetching techniques in both server/client contexts.
8. [Mutating Data](nextjs/docs/app/getting-started/mutating-data/index.md)  
   Patterns for updating/submitting data in Next.js.
9. [Caching](nextjs/docs/app/getting-started/caching/index.md)  
   Covers cache components, cache control, and configuration.
10. [Revalidating](nextjs/docs/app/getting-started/revalidating/index.md)  
    How stale data gets refreshed—manual and automatic approaches.
11. [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md)  
    Error boundaries, custom error pages/files.
12. [API Reference](nextjs/docs/app/api-reference/index.md)  
    Main entry to all directives, components, and supported file conventions.
13. [Functions > fetch](nextjs/docs/app/api-reference/functions/fetch/index.md)  
    Core API for server-side and client-side data requests.
14. [Components > Link Component](nextjs/docs/app/api-reference/components/link/index.md)  
    Detailed usage and props for client navigation.
15. [File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md)  
    List and explanation of special files for routing, errors, layouts, etc.

---

## Notable Gotchas and Structural Quirks

- Many key concepts are split between "Getting Started" pages and the deeper "API Reference" and "Guides" sections; always check both if looking for detail vs. overview.
- **File conventions** are critical: specific filenames (e.g., `layout.js`, `error.js`, `page.js`, etc.) trigger special routing or behavior. See [File-system conventions](nextjs/docs/app/api-reference/file-conventions/index.md).
- Migration/upgrade guides live in [Guides > Migrating](nextjs/docs/app/guides/migrating/index.md) and [Guides > Upgrading](nextjs/docs/app/guides/upgrading/index.md) subfolders, including step-by-step migration paths from Vite, Create React App, and across major Next.js versions.
- Advanced caching differs between "Cache Components" (current model) and [Caching (Previous Model)](nextjs/docs/app/guides/caching-without-cache-components/index.md); use the correct page per your app config.
- Some optimizations and integrations (e.g., analytics, CDN, OpenTelemetry, external platforms) are only in the Guides section, not surfaced in Getting Started.
- When troubleshooting, reference [Debugging](nextjs/docs/app/guides/debugging/index.md), [Error Handling](nextjs/docs/app/getting-started/error-handling/index.md), and [API Reference > error.js](nextjs/docs/app/api-reference/file-conventions/error/index.md).

---