---
title: "Next.js Glossary"
source: "https://nextjs.org/docs/app/glossary"
canonical_url: "https://nextjs.org/docs/app/glossary"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:12:39.759Z"
content_hash: "0b0f2b9a1cab62658afdf3c03eb8277503823eb4e7c6292d18624ccd65d1f687"
menu_path: ["Next.js Glossary"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/turbopack/index.md", "title": "Turbopack"}
nav_next: {"path": "nextjs/docs/pages/getting-started/index.md", "title": "Getting Started - Pages Router"}
---

# Next.js Glossary

Last updated April 23, 2026

# A[](#a)

## App Router[](#app-router)

The Next.js router introduced in version 13, built on top of React Server Components. It uses file-system based routing and supports layouts, nested routing, loading states, error handling, and more. Learn more in the [App Router documentation](../index.md).

# B[](#b)

## Build time[](#build-time)

The stage when your application is being compiled. During build time, Next.js transforms your code into optimized files for production, generates static pages, and prepares assets for deployment. See the [`next build` CLI reference](../api-reference/cli/next/index.md#next-build-options).

# C[](#c)

## Cache Components[](#cache-components)

A feature that enables component and function-level caching using the [`"use cache"` directive](../api-reference/directives/use-cache/index.md). Cache Components allows you to mix static, cached, and dynamic content within a single route by prerendering a static HTML shell that's served immediately, while dynamic content streams in when ready. Configure cache duration with [`cacheLife()`](../api-reference/functions/cacheLife/index.md), tag cached data with [`cacheTag()`](../api-reference/functions/cacheTag/index.md), and invalidate on-demand with [`updateTag()`](../api-reference/functions/updateTag/index.md). Learn more in the [Cache Components guide](../getting-started/caching/index.md).

## Catch-all Segments[](#catch-all-segments)

Dynamic route segments that can match multiple URL parts using the `[...folder]/page.js` syntax. These segments capture all remaining URL segments and are useful for implementing features like documentation sites or file browsers. Learn more in [Dynamic Route Segments](../api-reference/file-conventions/dynamic-routes/index.md#catch-all-segments).

## Client Bundles[](#client-bundles)

JavaScript bundles sent to the browser. Next.js splits these automatically based on the [module graph](#module-graph) to reduce initial payload size and load only the necessary code for each page.

## Client Component[](#client-component)

A React component that runs in the browser. In Next.js, Client Components can also be rendered on the server during initial page generation. They can use state, effects, event handlers, and browser APIs, and are marked with the [`"use client"` directive](#use-client-directive) at the top of a file. Learn more in [Server and Client Components](../getting-started/server-and-client-components/index.md).

A navigation technique where the page content updates dynamically without a full page reload. Next.js uses client-side navigation with the [`<Link>` component](../api-reference/components/link/index.md), keeping shared layouts interactive and preserving browser state. Learn more in [Linking and Navigating](../getting-started/linking-and-navigating/index.md#client-side-transitions).

## Client Cache[](#client-cache)

An in-memory cache in the browser that stores [RSC Payload](#rsc-payload) for visited and prefetched routes. During [client-side navigation](#client-side-navigation), Next.js serves cached [layouts](#layout) and [loading states](#loading-ui) instantly without a server request. Pages are not cached by default but are reused during browser back/forward navigation.

The client cache is cleared on page refresh. It can be invalidated programmatically with [`revalidateTag`](../api-reference/functions/revalidateTag/index.md), [`revalidatePath`](../api-reference/functions/revalidatePath/index.md), [`updateTag`](../api-reference/functions/updateTag/index.md), [`router.refresh`](../api-reference/functions/use-router/index.md), [`cookies.set`](../api-reference/functions/cookies/index.md), or [`cookies.delete`](../api-reference/functions/cookies/index.md).

You can configure the client cache duration with [`staleTimes`](../api-reference/config/next-config-js/staleTimes/index.md) globally, or per-route via the `stale` property in [`cacheLife`](../api-reference/functions/cacheLife/index.md#client-cache-behavior) (recommended).

## Code Splitting[](#code-splitting)

The process of dividing your application into smaller JavaScript chunks based on routes. Instead of loading all code upfront, only the code needed for the current route is loaded, reducing initial load time. Next.js automatically performs code splitting based on routes. Learn more in the [Package Bundling guide](../guides/package-bundling/index.md).

# D[](#d)

## Dynamic rendering[](#dynamic-rendering)

When a component is rendered at request time rather than [build time](#build-time). A component becomes dynamic when it uses [Request-time APIs](#request-time-apis).

## Dynamic route segments[](#dynamic-route-segments)

[Route segments](#route-segment) that are generated from data at request time. Created by wrapping a folder name in square brackets (e.g., `[slug]`), they allow you to create routes from dynamic data like blog posts or product pages. Learn more in [Dynamic Route Segments](../api-reference/file-conventions/dynamic-routes/index.md).

# E[](#e)

## Environment Variables[](#environment-variables)

Configuration values accessible at build time or request time. In Next.js, variables prefixed with `NEXT_PUBLIC_` are exposed to the browser, while others are only available server-side. Learn more in [Environment Variables](../guides/environment-variables/index.md).

## Error Boundary[](#error-boundary)

A React component that catches JavaScript errors in its child component tree and displays a fallback UI. In Next.js, create an [`error.js` file](../api-reference/file-conventions/error/index.md) to automatically wrap a route segment in an error boundary. Learn more in [Error Handling](../getting-started/error-handling/index.md).

# F[](#f)

## Font Optimization[](#font-optimization)

Automatic font optimization using [`next/font`](../api-reference/components/font/index.md). Next.js self-hosts fonts, eliminates layout shift, and applies best practices for performance. Works with Google Fonts and local font files. Learn more in [Fonts](../getting-started/fonts/index.md).

## File-system caching[](#file-system-caching)

A Turbopack feature that stores compiler artifacts on disk between runs, reducing work across `next dev` or `next build` commands for significantly faster compile times. Learn more in [Turbopack FileSystem Caching](../api-reference/config/next-config-js/turbopackFileSystemCache/index.md).

# H[](#h)

## Hydration[](#hydration)

React's process of attaching event handlers to the DOM to make server-rendered static HTML interactive. During hydration, React reconciles the server-rendered markup with the client-side JavaScript. Learn more in [Server and Client Components](../getting-started/server-and-client-components/index.md#how-do-server-and-client-components-work-in-nextjs).

# I[](#i)

## Import Aliases[](#import-aliases)

Custom path mappings that provide shorthand references for frequently used directories. Import aliases reduce the complexity of relative imports and make code more readable and maintainable. Learn more in [Absolute Imports and Module Path Aliases](../getting-started/installation/index.md#set-up-absolute-imports-and-module-path-aliases).

## Incremental Static Regeneration (ISR)[](#incremental-static-regeneration-isr)

A technique that allows you to update static content without rebuilding the entire site. ISR enables you to use static generation on a per-page basis while revalidating pages in the background as traffic comes in. Learn more in the [ISR guide](../guides/incremental-static-regeneration/index.md).

> **Good to know**: In Next.js, ISR is also known as [Revalidation](#revalidation).

## Intercepting Routes[](#intercepting-routes)

A routing pattern that allows loading a route from another part of your application within the current layout. Useful for displaying content (like modals) without the user switching context, while keeping the URL shareable. Learn more in [Intercepting Routes](../api-reference/file-conventions/intercepting-routes/index.md).

## Image Optimization[](#image-optimization)

Automatic image optimization using the [`<Image>` component](../api-reference/components/image/index.md). Next.js optimizes images on-demand, serves them in modern formats like WebP, and automatically handles lazy loading and responsive sizing. Learn more in [Images](../getting-started/images/index.md).

# L[](#l)

## Layout[](#layout)

UI that is shared between multiple pages. Layouts preserve state, remain interactive, and do not re-render on navigation. Defined by exporting a React component from a [`layout.js` file](../api-reference/file-conventions/layout/index.md). Learn more in [Layouts and Pages](../getting-started/layouts-and-pages/index.md).

## Loading UI[](#loading-ui)

Fallback UI shown while a [route segment](#route-segment) is loading. Created by adding a [`loading.js` file](../api-reference/file-conventions/loading/index.md) to a folder, which automatically wraps the page in a [Suspense boundary](#suspense-boundary). Learn more in [Loading UI](../api-reference/file-conventions/loading/index.md).

# M[](#m)

## Module Graph[](#module-graph)

A graph of file dependencies in your app. Each file (module) is a node, and import/export relationships form the edges. Next.js analyzes this graph to determine optimal bundling and code-splitting strategies. Learn more in [Server and Client Components](../getting-started/server-and-client-components/index.md#reducing-js-bundle-size).

## Metadata[](#metadata)

Information about a page used by browsers and search engines, such as title, description, and Open Graph images. In Next.js, define metadata using the [`metadata` export](../api-reference/functions/generate-metadata/index.md) or [`generateMetadata` function](../api-reference/functions/generate-metadata/index.md) in layout or page files. Learn more in [Metadata and OG Images](../getting-started/metadata-and-og-images/index.md).

## Memoization[](#memoization)

Caching the return value of a function so that calling the same function multiple times during a render pass (request) only executes it once. In Next.js, `fetch` `GET` requests with the same URL and options are automatically memoized across Server Components, layouts, pages, and `generateMetadata`/`generateStaticParams` (but not [Route Handlers](../api-reference/file-conventions/route/index.md) since they are not part of the React component tree).

For non-`fetch` operations, use the React [`cache`](https://react.dev/reference/react/cache) function. Learn more in the [`fetch` API reference](../api-reference/functions/fetch/index.md).

## Middleware[](#middleware)

See [Proxy](#proxy).

# N[](#n)

## Not Found[](#not-found)

A special component shown when a route doesn't exist or when the [`notFound()` function](../api-reference/functions/not-found/index.md) is called. Created by adding a [`not-found.js` file](../api-reference/file-conventions/not-found/index.md) to your app directory. Learn more in [Error Handling](../getting-started/error-handling/index.md#not-found).

# P[](#p)

## Private Folders[](#private-folders)

Folders prefixed with an underscore (e.g., `_components`) that are excluded from the routing system. These folders are used for code organization and shared utilities without creating accessible routes. Learn more in [Private Folders](../getting-started/project-structure/index.md#private-folders).

## Page[](#page)

UI that is unique to a route. Defined by exporting a React component from a [`page.js` file](../api-reference/file-conventions/page/index.md) within the `app` directory. Learn more in [Layouts and Pages](../getting-started/layouts-and-pages/index.md).

## Parallel Routes[](#parallel-routes)

A pattern that allows simultaneously or conditionally rendering multiple pages within the same layout. Created using named slots with the `@folder` convention, useful for dashboards, modals, and complex layouts. Learn more in [Parallel Routes](../api-reference/file-conventions/parallel-routes/index.md).

## Partial Prerendering (PPR)[](#partial-prerendering-ppr)

A rendering optimization that combines prerendering and dynamic rendering in a single route. The static shell is served immediately while dynamic content streams in when ready, providing the best of both rendering strategies. Learn more in [Cache Components](../getting-started/caching/index.md).

## Prefetching[](#prefetching)

Loading a route in the background before the user navigates to it. Next.js automatically prefetches routes linked with the [`<Link>` component](../api-reference/components/link/index.md) when they enter the viewport, making navigation feel instant. Learn more in the [Prefetching guide](../guides/prefetching/index.md).

## Prerendering[](#prerendering)

When a component is rendered at [build time](#build-time) or in the background during [revalidation](#revalidation). The result is HTML and [RSC Payload](#rsc-payload), which can be cached and served from a CDN. Prerendering is the default for components that don't use [Request-time APIs](#request-time-apis).

## Proxy[](#proxy)

A file ([`proxy.js`](../api-reference/file-conventions/proxy/index.md)) that runs code on the server before request is completed. Used to implement server-side logic like logging, redirects, and rewrites. Formerly known as Middleware. Learn more in the [Proxy guide](../getting-started/proxy/index.md).

# R[](#r)

## Redirect[](#redirect)

Sending users from one URL to another. In Next.js, redirects can be configured in [`next.config.js`](../api-reference/config/next-config-js/redirects/index.md), returned from [Proxy](../api-reference/file-conventions/proxy/index.md), or triggered programmatically with the [`redirect()` function](../api-reference/functions/redirect/index.md). Learn more in [Redirecting](../guides/redirecting/index.md).

## Request-time APIs[](#request-time-apis)

Functions that access request-specific data, causing a component to opt into [dynamic rendering](#dynamic-rendering). These include:

-   [`cookies()`](../api-reference/functions/cookies/index.md) - Access request cookies
-   [`headers()`](../api-reference/functions/headers/index.md) - Access request headers
-   [`searchParams`](../api-reference/file-conventions/page/index.md#searchparams-optional) - Access URL query parameters
-   [`draftMode()`](../api-reference/functions/draft-mode/index.md) - Enable or check draft mode

## Runtime rendering[](#runtime-rendering)

See [Dynamic rendering](#dynamic-rendering).

## Revalidation[](#revalidation)

The process of updating cached data. Can be time-based (using [`cacheLife()`](../api-reference/functions/cacheLife/index.md) to set cache duration) or on-demand (using [`cacheTag()`](../api-reference/functions/cacheTag/index.md) to tag data, then [`updateTag()`](../api-reference/functions/updateTag/index.md) to invalidate). Learn more in [Caching and Revalidating](../getting-started/caching/index.md).

## Rewrite[](#rewrite)

Mapping an incoming request path to a different destination path without changing the URL in the browser. Configured in [`next.config.js`](../api-reference/config/next-config-js/rewrites/index.md) or returned from [Proxy](../api-reference/file-conventions/proxy/index.md). Useful for proxying to external services or legacy URLs.

## Route Groups[](#route-groups)

A way to organize routes without affecting the URL structure. Created by wrapping a folder name in parentheses (e.g., `(marketing)`), route groups help organize related routes and enable per-group [layouts](#layout). Learn more in [Route Groups](../api-reference/file-conventions/route-groups/index.md).

## Route Handler[](#route-handler)

A function that handles HTTP requests for a specific route, defined in a [`route.js` file](../api-reference/file-conventions/route/index.md). Route Handlers use the Web Request and Response APIs and can handle `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS` methods. Learn more in [Route Handlers](../getting-started/route-handlers/index.md).

## Route Segment[](#route-segment)

A part of the URL path (between two slashes) defined by a folder in the `app` directory. Each folder represents a segment in the URL structure. Learn more in [Project Structure](../getting-started/project-structure/index.md).

## RSC Payload[](#rsc-payload)

The React Server Component Payload—a compact binary representation of the rendered React Server Components tree. Contains the rendered result of Server Components, placeholders for Client Components, and props passed between them. Learn more in [Server and Client Components](../getting-started/server-and-client-components/index.md#how-do-server-and-client-components-work-in-nextjs).

# S[](#s)

## Server Component[](#server-component)

The default component type in the App Router. Server Components render on the server, can fetch data directly, and don't add to the client JavaScript bundle. They cannot use state or browser APIs. Learn more in [Server and Client Components](../getting-started/server-and-client-components/index.md).

## Server Action[](#server-action)

A [Server Function](#server-function) that is passed to a Client Component as a prop or bound to a form action. Server Actions are commonly used for form submissions and data mutations. Learn more in [Server Actions and Mutations](../getting-started/mutating-data/index.md).

## Server Function[](#server-function)

An asynchronous function that runs on the server, marked with the [`"use server"` directive](../api-reference/directives/use-server/index.md). Server Functions can be invoked from Client Components. When passed as a prop to a Client Component or bound to a form action, they are called [Server Actions](#server-action). Learn more in [React Server Functions](https://react.dev/reference/rsc/server-functions).

## Static Export[](#static-export)

A deployment mode that generates a fully static site with HTML, CSS, and JavaScript files. Enabled by setting `output: 'export'` in `next.config.js`. Static exports can be hosted on any static file server without a Node.js server. Learn more in [Static Exports](../guides/static-exports/index.md).

## Static rendering[](#static-rendering)

See [Prerendering](#prerendering).

## Static Assets[](#static-assets)

Files such as images, fonts, videos, and other media that are served directly without processing. Static assets are typically stored in the `public` directory and referenced by their relative paths. Learn more in [Static Assets](../api-reference/file-conventions/public-folder/index.md).

## Static Shell[](#static-shell)

The prerendered HTML structure of a page that's served immediately to the browser. With [Partial Prerendering](#partial-prerendering-ppr), the static shell includes all statically renderable content plus [Suspense boundary](#suspense-boundary) fallbacks for dynamic content that streams in later.

## Streaming[](#streaming)

A technique that allows the server to send parts of a page to the client as they become ready, rather than waiting for the entire page to render. Enabled automatically with [`loading.js`](../api-reference/file-conventions/loading/index.md) or manual `<Suspense>` boundaries. Learn more in the [Streaming guide](../guides/streaming/index.md).

## Suspense boundary[](#suspense-boundary)

A React [`<Suspense>`](https://react.dev/reference/react/Suspense) component that wraps async content and displays fallback UI while it loads. In Next.js, Suspense boundaries define where the [static shell](#static-shell) ends and [streaming](#streaming) begins, enabling [Partial Prerendering](#partial-prerendering-ppr).

# T[](#t)

## Turbopack[](#turbopack)

A fast, Rust-based bundler built for Next.js. Turbopack is the default bundler for `next dev` and available for `next build`. It provides significantly faster compilation times compared to Webpack. Learn more in [Turbopack](../api-reference/turbopack/index.md).

## Tree Shaking[](#tree-shaking)

The process of removing unused code from your JavaScript bundles during the build process. Next.js automatically tree-shakes your code to reduce bundle sizes. Learn more in the [Package Bundling guide](../guides/package-bundling/index.md).

# U[](#u)

## `"use cache"` Directive[](#use-cache-directive)

A directive that marks a component or function as cacheable. It can be placed at the top of a file to indicate that all exports in the file are cacheable, or inline at the top of a function or component to mark that specific scope as cacheable. Learn more in the [`"use cache"` reference](../api-reference/directives/use-cache/index.md).

## `"use client"` Directive[](#use-client-directive)

A special React directive that marks the boundary between server and client code. It must be placed at the top of a file, before any imports or other code. It indicates that React Components, helper functions, variable declarations, and all imported dependencies should be included in the [client bundle](#client-bundles). Learn more in the [`"use client"` reference](../api-reference/directives/use-client/index.md).

## `"use server"` Directive[](#use-server-directive)

A directive that marks a function as a [Server Function](#server-function) that can be called from client-side code. It can be placed at the top of a file to indicate that all exports in the file are Server Functions, or inline at the top of a function to mark that specific function. Learn more in the [`"use server"` reference](../api-reference/directives/use-server/index.md).

# V[](#v)

## Version skew[](#version-skew)

After a new version of your application is deployed, clients that are still active may reference JavaScript, CSS, or data from an older build. This mismatch between client and server versions is called version skew, and it can cause missing assets, Server Action errors, and navigation failures. Next.js uses [`deploymentId`](../api-reference/config/next-config-js/deploymentId/index.md) to detect and handle version skew. Learn more in [Self-Hosting - Version Skew](../guides/self-hosting/index.md#version-skew).

Was this helpful?
