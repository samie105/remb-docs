---
title: "Project structure and organization"
source: "https://nextjs.org/docs/app/getting-started/project-structure"
canonical_url: "https://nextjs.org/docs/app/getting-started/project-structure"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:13:37.213Z"
content_hash: "7d6e857093b122e1d6d69c66216edd9acf606bff5cb1413c2ea8418c60787594"
menu_path: ["Project structure and organization"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/getting-started/installation/index.md", "title": "Installation"}
nav_next: {"path": "nextjs/docs/app/getting-started/layouts-and-pages/index.md", "title": "Layouts and Pages"}
---

# Project structure and organization

Last updated April 15, 2026

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions[](#folder-and-file-conventions)

### Top-level folders[](#top-level-folders)

Top-level folders are used to organize your application's code and static assets.

![Route segments to path segments](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftop-level-folders.png&w=3840&q=75)![Route segments to path segments](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftop-level-folders.png&w=3840&q=75)

[`app`](/docs/app)

App Router

[`pages`](/docs/pages/building-your-application/routing)

Pages Router

[`public`](/docs/app/api-reference/file-conventions/public-folder)

Static assets to be served

[`src`](/docs/app/api-reference/file-conventions/src-folder)

Optional application source folder

### Top-level files[](#top-level-files)

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

**Next.js**

[`next.config.js`](/docs/app/api-reference/config/next-config-js)

Configuration file for Next.js

[`package.json`](/docs/app/getting-started/installation#manual-installation)

Project dependencies and scripts

[`instrumentation.ts`](/docs/app/guides/instrumentation)

OpenTelemetry and Instrumentation file

[`proxy.ts`](/docs/app/api-reference/file-conventions/proxy)

Next.js request proxy

[`.env`](/docs/app/guides/environment-variables)

Environment variables (should not be tracked by version control)

[`.env.local`](/docs/app/guides/environment-variables)

Local environment variables (should not be tracked by version control)

[`.env.production`](/docs/app/guides/environment-variables)

Production environment variables (should not be tracked by version control)

[`.env.development`](/docs/app/guides/environment-variables)

Development environment variables (should not be tracked by version control)

[`eslint.config.mjs`](/docs/app/api-reference/config/eslint)

Configuration file for ESLint

`.gitignore`

Git files and folders to ignore

[`next-env.d.ts`](/docs/app/api-reference/config/typescript#next-envdts)

TypeScript declaration file for Next.js (should not be tracked by version control)

`tsconfig.json`

Configuration file for TypeScript

`jsconfig.json`

Configuration file for JavaScript

### Routing Files[](#routing-files)

Add `page` to expose a route, `layout` for shared UI such as header, nav, or footer, `loading` for skeletons, `error` for error boundaries, and `route` for APIs.

[`layout`](/docs/app/api-reference/file-conventions/layout)

`.js` `.jsx` `.tsx`

Layout

[`page`](/docs/app/api-reference/file-conventions/page)

`.js` `.jsx` `.tsx`

Page

[`loading`](/docs/app/api-reference/file-conventions/loading)

`.js` `.jsx` `.tsx`

Loading UI

[`not-found`](/docs/app/api-reference/file-conventions/not-found)

`.js` `.jsx` `.tsx`

Not found UI

[`error`](/docs/app/api-reference/file-conventions/error)

`.js` `.jsx` `.tsx`

Error UI

[`global-error`](/docs/app/api-reference/file-conventions/error#global-error)

`.js` `.jsx` `.tsx`

Global error UI

[`route`](/docs/app/api-reference/file-conventions/route)

`.js` `.ts`

API endpoint

[`template`](/docs/app/api-reference/file-conventions/template)

`.js` `.jsx` `.tsx`

Re-rendered layout

[`default`](/docs/app/api-reference/file-conventions/default)

`.js` `.jsx` `.tsx`

Parallel route fallback page

### Nested routes[](#nested-routes)

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a `page` or `route` file exists.

Path

URL pattern

Notes

`app/layout.tsx`

—

Root layout wraps all routes

`app/blog/layout.tsx`

—

Wraps `/blog` and descendants

`app/page.tsx`

`/`

Public route

`app/blog/page.tsx`

`/blog`

Public route

`app/blog/authors/page.tsx`

`/blog/authors`

Public route

### Dynamic routes[](#dynamic-routes)

Parameterize segments with square brackets. Use `[segment]` for a single param, `[...segment]` for catch‑all, and `[[...segment]]` for optional catch‑all. Access values via the [`params`](/docs/app/api-reference/file-conventions/page#params-optional) prop.

Path

URL pattern

`app/blog/[slug]/page.tsx`

`/blog/my-first-post`

`app/shop/[...slug]/page.tsx`

`/shop/clothing`, `/shop/clothing/shirts`

`app/docs/[[...slug]]/page.tsx`

`/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router`

### Route groups and private folders[](#route-groups-and-private-folders)

Organize code without changing URLs with route groups [`(group)`](/docs/app/api-reference/file-conventions/route-groups#convention), and colocate non-routable files with private folders [`_folder`](#private-folders).

Path

URL pattern

Notes

`app/(marketing)/page.tsx`

`/`

Group omitted from URL

`app/(shop)/cart/page.tsx`

`/cart`

Share layouts within `(shop)`

`app/blog/_components/Post.tsx`

—

Not routable; safe place for UI utilities

`app/blog/_lib/data.ts`

—

Not routable; safe place for utils

### Parallel and Intercepted Routes[](#parallel-and-intercepted-routes)

These features fit specific UI patterns, such as slot-based layouts or modal routing.

Use `@slot` for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.

Pattern (docs)

Meaning

Typical use case

[`@folder`](/docs/app/api-reference/file-conventions/parallel-routes#slots)

Named slot

Sidebar + main content

[`(.)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)

Intercept same level

Preview sibling route in a modal

[`(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)

Intercept parent

Open a child of the parent as an overlay

[`(..)(..)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)

Intercept two levels

Deeply nested overlay

[`(...)folder`](/docs/app/api-reference/file-conventions/intercepting-routes#convention)

Intercept from root

Show arbitrary route in current view

### Metadata file conventions[](#metadata-file-conventions)

#### App icons[](#app-icons)

[`favicon`](/docs/app/api-reference/file-conventions/metadata/app-icons#favicon)

`.ico`

Favicon file

[`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#icon)

`.ico` `.jpg` `.jpeg` `.png` `.svg`

App Icon file

[`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)

`.js` `.ts` `.tsx`

Generated App Icon

[`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon)

`.jpg` `.jpeg`, `.png`

Apple App Icon file

[`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx)

`.js` `.ts` `.tsx`

Generated Apple App Icon

#### Open Graph and Twitter images[](#open-graph-and-twitter-images)

[`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image)

`.jpg` `.jpeg` `.png` `.gif`

Open Graph image file

[`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)

`.js` `.ts` `.tsx`

Generated Open Graph image

[`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image)

`.jpg` `.jpeg` `.png` `.gif`

Twitter image file

[`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx)

`.js` `.ts` `.tsx`

Generated Twitter image

#### SEO[](#seo)

[`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml)

`.xml`

Sitemap file

[`sitemap`](/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts)

`.js` `.ts`

Generated Sitemap

[`robots`](/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt)

`.txt`

Robots file

[`robots`](/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file)

`.js` `.ts`

Generated Robots file

## Organizing your project[](#organizing-your-project)

Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### Component hierarchy[](#component-hierarchy)

The components defined in special files are rendered in a specific hierarchy:

*   `layout.js`
*   `template.js`
*   `error.js` (React error boundary)
*   `loading.js` (React suspense boundary)
*   `not-found.js` (React error boundary for "not found" UI)
*   `page.js` or nested `layout.js`

![Component Hierarchy for File Conventions](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)![Component Hierarchy for File Conventions](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.

![Nested File Conventions Component Hierarchy](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)![Nested File Conventions Component Hierarchy](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)

### Colocation[](#colocation)

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-not-routable.png&w=3840&q=75)![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-not-routable.png&w=3840&q=75)

And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

![A diagram showing how page.js and route.js files make routes publicly accessible.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-routable.png&w=3840&q=75)![A diagram showing how page.js and route.js files make routes publicly accessible.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-routable.png&w=3840&q=75)

This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.

![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-colocation.png&w=3840&q=75)![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-colocation.png&w=3840&q=75)

> **Good to know**: While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](#store-project-files-outside-of-app).

### Private folders[](#private-folders)

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

![An example folder structure using private folders](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-private-folders.png&w=3840&q=75)![An example folder structure using private folders](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-private-folders.png&w=3840&q=75)

Since files in the `app` directory can be [safely colocated by default](#colocation), private folders are not required for colocation. However, they can be useful for:

*   Separating UI logic from routing logic.
*   Consistently organizing internal files across a project and the Next.js ecosystem.
*   Sorting and grouping files in code editors.
*   Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
> 
> *   While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> *   You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
> *   If you don't use private folders, it would be helpful to know Next.js [special file conventions](/docs/app/getting-started/project-structure#routing-files) to prevent unexpected naming conflicts.

### Route groups[](#route-groups)

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-route-groups.png&w=3840&q=75)![An example folder structure using route groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-route-groups.png&w=3840&q=75)

Route groups are useful for:

*   Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
*   Enabling nested layouts in the same route segment level:
    *   [Creating multiple nested layouts in the same segment, including multiple root layouts](#creating-multiple-root-layouts)
    *   [Adding a layout to a subset of routes in a common segment](#opting-specific-segments-into-a-layout)

### `src` folder[](#src-folder)

Next.js supports storing application code (including `app`) inside an optional [`src` folder](/docs/app/api-reference/file-conventions/src-folder). This separates application code from project configuration files which mostly live in the root of a project.

![An example folder structure with the \`src\` folder](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![An example folder structure with the \`src\` folder](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)

## Examples[](#examples)

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

### Store project files outside of `app`[](#store-project-files-outside-of-app)

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

![An example folder structure with project files outside of app](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-project-root.png&w=3840&q=75)![An example folder structure with project files outside of app](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-project-root.png&w=3840&q=75)

### Store project files in top-level folders inside of `app`[](#store-project-files-in-top-level-folders-inside-of-app)

This strategy stores all application code in shared folders in the **root of the `app` directory**.

![An example folder structure with project files inside app](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root.png&w=3840&q=75)![An example folder structure with project files inside app](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root.png&w=3840&q=75)

### Split project files by feature or route[](#split-project-files-by-feature-or-route)

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

![An example folder structure with project files split by feature or route](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root-split.png&w=3840&q=75)![An example folder structure with project files split by feature or route](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root-split.png&w=3840&q=75)

### Organize routes without affecting the URL path[](#organize-routes-without-affecting-the-url-path)

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).

![Organizing Routes with Route Groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-organisation.png&w=3840&q=75)![Organizing Routes with Route Groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-organisation.png&w=3840&q=75)

Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.

![Route Groups with Multiple Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-layouts.png&w=3840&q=75)![Route Groups with Multiple Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-layouts.png&w=3840&q=75)

### Opting specific segments into a layout[](#opting-specific-segments-into-a-layout)

To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).

![Route Groups with Opt-in Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-opt-in-layouts.png&w=3840&q=75)![Route Groups with Opt-in Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-opt-in-layouts.png&w=3840&q=75)

### Opting for loading skeletons on a specific route[](#opting-for-loading-skeletons-on-a-specific-route)

To apply a [loading skeleton](/docs/app/api-reference/file-conventions/loading) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.

![Folder structure showing a loading.tsx and a page.tsx inside the route group](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-loading.png&w=3840&q=75)![Folder structure showing a loading.tsx and a page.tsx inside the route group](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-loading.png&w=3840&q=75)

Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.

### Creating multiple root layouts[](#creating-multiple-root-layouts)

To create multiple [root layouts](/docs/app/api-reference/file-conventions/layout#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.

![Route Groups with Multiple Root Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-root-layouts.png&w=3840&q=75)![Route Groups with Multiple Root Layouts](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-root-layouts.png&w=3840&q=75)

In the example above, both `(marketing)` and `(shop)` have their own root layout.

[Previous

Installation

](/docs/app/getting-started/installation)

[Next

Layouts and Pages

](/docs/app/getting-started/layouts-and-pages)

Was this helpful?

supported.

Send
