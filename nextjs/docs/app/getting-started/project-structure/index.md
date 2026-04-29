---
title: "Project structure and organization"
source: "https://nextjs.org/docs/app/getting-started/project-structure"
canonical_url: "https://nextjs.org/docs/app/getting-started/project-structure"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:12:17.492Z"
content_hash: "dce7399ef5e4b9a846d3642d9d5f168ec4ce736f41f1c1cd29ba7bda0d8c842b"
menu_path: ["Project structure and organization"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/getting-started/installation/index.md", "title": "Installation"}
nav_next: {"path": "nextjs/docs/app/getting-started/layouts-and-pages/index.md", "title": "Layouts and Pages"}
---

# Project structure and organization

Last updated April 23, 2026

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions[](#folder-and-file-conventions)

### Top-level folders[](#top-level-folders)

Top-level folders are used to organize your application's code and static assets.

![Route segments to path segments](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/top-level-folders.png)

|  |  |
| --- | --- |
| [`app`](../../index.md) | App Router |
| [`pages`](../../../pages/building-your-application/routing/index.md) | Pages Router |
| [`public`](../../api-reference/file-conventions/public-folder/index.md) | Static assets to be served |
| [`src`](../../api-reference/file-conventions/src-folder/index.md) | Optional application source folder |

### Top-level files[](#top-level-files)

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

|  |  |
| --- | --- |
| **Next.js** |  |
| [`next.config.js`](../../api-reference/config/next-config-js/index.md) | Configuration file for Next.js |
| [`package.json`](../installation/index.md#manual-installation) | Project dependencies and scripts |
| [`instrumentation.ts`](../../guides/instrumentation/index.md) | OpenTelemetry and Instrumentation file |
| [`proxy.ts`](../../api-reference/file-conventions/proxy/index.md) | Next.js request proxy |
| [`.env`](../../guides/environment-variables/index.md) | Environment variables (should not be tracked by version control) |
| [`.env.local`](../../guides/environment-variables/index.md) | Local environment variables (should not be tracked by version control) |
| [`.env.production`](../../guides/environment-variables/index.md) | Production environment variables (should not be tracked by version control) |
| [`.env.development`](../../guides/environment-variables/index.md) | Development environment variables (should not be tracked by version control) |
| [`eslint.config.mjs`](../../api-reference/config/eslint/index.md) | Configuration file for ESLint |
| `.gitignore` | Git files and folders to ignore |
| [`next-env.d.ts`](../../api-reference/config/typescript/index.md#next-envdts) | TypeScript declaration file for Next.js (should not be tracked by version control) |
| `tsconfig.json` | Configuration file for TypeScript |
| `jsconfig.json` | Configuration file for JavaScript |

### Routing Files[](#routing-files)

Add `page` to expose a route, `layout` for shared UI such as header, nav, or footer, `loading` for skeletons, `error` for error boundaries, and `route` for APIs.

|  |  |  |
| --- | --- | --- |
| [`layout`](../../api-reference/file-conventions/layout/index.md) | `.js` `.jsx` `.tsx` | Layout |
| [`page`](../../api-reference/file-conventions/page/index.md) | `.js` `.jsx` `.tsx` | Page |
| [`loading`](../../api-reference/file-conventions/loading/index.md) | `.js` `.jsx` `.tsx` | Loading UI |
| [`not-found`](../../api-reference/file-conventions/not-found/index.md) | `.js` `.jsx` `.tsx` | Not found UI |
| [`error`](../../api-reference/file-conventions/error/index.md) | `.js` `.jsx` `.tsx` | Error UI |
| [`global-error`](../../api-reference/file-conventions/error/index.md#global-error) | `.js` `.jsx` `.tsx` | Global error UI |
| [`route`](../../api-reference/file-conventions/route/index.md) | `.js` `.ts` | API endpoint |
| [`template`](../../api-reference/file-conventions/template/index.md) | `.js` `.jsx` `.tsx` | Re-rendered layout |
| [`default`](../../api-reference/file-conventions/default/index.md) | `.js` `.jsx` `.tsx` | Parallel route fallback page |

### Nested routes[](#nested-routes)

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a `page` or `route` file exists.

| Path | URL pattern | Notes |
| --- | --- | --- |
| `app/layout.tsx` | — | Root layout wraps all routes |
| `app/blog/layout.tsx` | — | Wraps `/blog` and descendants |
| `app/page.tsx` | `/` | Public route |
| `app/blog/page.tsx` | `/blog` | Public route |
| `app/blog/authors/page.tsx` | `/blog/authors` | Public route |

### Dynamic routes[](#dynamic-routes)

Parameterize segments with square brackets. Use `[segment]` for a single param, `[...segment]` for catch‑all, and `[[...segment]]` for optional catch‑all. Access values via the [`params`](../../api-reference/file-conventions/page/index.md#params-optional) prop.

| Path | URL pattern |
| --- | --- |
| `app/blog/[slug]/page.tsx` | `/blog/my-first-post` |
| `app/shop/[...slug]/page.tsx` | `/shop/clothing`, `/shop/clothing/shirts` |
| `app/docs/[[...slug]]/page.tsx` | `/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router` |

### Route groups and private folders[](#route-groups-and-private-folders)

Organize code without changing URLs with route groups [`(group)`](../../api-reference/file-conventions/route-groups/index.md#convention), and colocate non-routable files with private folders [`_folder`](#private-folders).

| Path | URL pattern | Notes |
| --- | --- | --- |
| `app/(marketing)/page.tsx` | `/` | Group omitted from URL |
| `app/(shop)/cart/page.tsx` | `/cart` | Share layouts within `(shop)` |
| `app/blog/_components/Post.tsx` | — | Not routable; safe place for UI utilities |
| `app/blog/_lib/data.ts` | — | Not routable; safe place for utils |

### Parallel and Intercepted Routes[](#parallel-and-intercepted-routes)

These features fit specific UI patterns, such as slot-based layouts or modal routing.

Use `@slot` for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.

| Pattern (docs) | Meaning | Typical use case |
| --- | --- | --- |
| [`@folder`](../../api-reference/file-conventions/parallel-routes/index.md#slots) | Named slot | Sidebar + main content |
| [`(.)folder`](../../api-reference/file-conventions/intercepting-routes/index.md#convention) | Intercept same level | Preview sibling route in a modal |
| [`(..)folder`](../../api-reference/file-conventions/intercepting-routes/index.md#convention) | Intercept parent | Open a child of the parent as an overlay |
| [`(..)(..)folder`](../../api-reference/file-conventions/intercepting-routes/index.md#convention) | Intercept two levels | Deeply nested overlay |
| [`(...)folder`](../../api-reference/file-conventions/intercepting-routes/index.md#convention) | Intercept from root | Show arbitrary route in current view |

### Metadata file conventions[](#metadata-file-conventions)

#### App icons[](#app-icons)

|  |  |  |
| --- | --- | --- |
| [`favicon`](../../api-reference/file-conventions/metadata/app-icons/index.md#favicon) | `.ico` | Favicon file |
| [`icon`](../../api-reference/file-conventions/metadata/app-icons/index.md#icon) | `.ico` `.jpg` `.jpeg` `.png` `.svg` | App Icon file |
| [`icon`](../../api-reference/file-conventions/metadata/app-icons/index.md#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated App Icon |
| [`apple-icon`](../../api-reference/file-conventions/metadata/app-icons/index.md#apple-icon) | `.jpg` `.jpeg`, `.png` | Apple App Icon file |
| [`apple-icon`](../../api-reference/file-conventions/metadata/app-icons/index.md#generate-icons-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Apple App Icon |

#### Open Graph and Twitter images[](#open-graph-and-twitter-images)

|  |  |  |
| --- | --- | --- |
| [`opengraph-image`](../../api-reference/file-conventions/metadata/opengraph-image/index.md#opengraph-image) | `.jpg` `.jpeg` `.png` `.gif` | Open Graph image file |
| [`opengraph-image`](../../api-reference/file-conventions/metadata/opengraph-image/index.md#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Open Graph image |
| [`twitter-image`](../../api-reference/file-conventions/metadata/opengraph-image/index.md#twitter-image) | `.jpg` `.jpeg` `.png` `.gif` | Twitter image file |
| [`twitter-image`](../../api-reference/file-conventions/metadata/opengraph-image/index.md#generate-images-using-code-js-ts-tsx) | `.js` `.ts` `.tsx` | Generated Twitter image |

#### SEO[](#seo)

|  |  |  |
| --- | --- | --- |
| [`sitemap`](../../api-reference/file-conventions/metadata/sitemap/index.md#sitemap-files-xml) | `.xml` | Sitemap file |
| [`sitemap`](../../api-reference/file-conventions/metadata/sitemap/index.md#generating-a-sitemap-using-code-js-ts) | `.js` `.ts` | Generated Sitemap |
| [`robots`](../../api-reference/file-conventions/metadata/robots/index.md#static-robotstxt) | `.txt` | Robots file |
| [`robots`](../../api-reference/file-conventions/metadata/robots/index.md#generate-a-robots-file) | `.js` `.ts` | Generated Robots file |

## Organizing your project[](#organizing-your-project)

Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### Component hierarchy[](#component-hierarchy)

The components defined in special files are rendered in a specific hierarchy:

-   `layout.js`
-   `template.js`
-   `error.js` (React error boundary)
-   `loading.js` (React suspense boundary)
-   `not-found.js` (React error boundary for "not found" UI)
-   `page.js` or nested `layout.js`

![Component Hierarchy for File Conventions](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/file-conventions-component-hierarchy.png)

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.

![Nested File Conventions Component Hierarchy](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/nested-file-conventions-component-hierarchy.png)

### Colocation[](#colocation)

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

![A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-not-routable.png)

And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

![A diagram showing how page.js and route.js files make routes publicly accessible.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-routable.png)

This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.

![A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-colocation.png)

> **Good to know**: While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](#store-project-files-outside-of-app).

### Private folders[](#private-folders)

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

![An example folder structure using private folders](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-private-folders.png)

Since files in the `app` directory can be [safely colocated by default](#colocation), private folders are not required for colocation. However, they can be useful for:

-   Separating UI logic from routing logic.
-   Consistently organizing internal files across a project and the Next.js ecosystem.
-   Sorting and grouping files in code editors.
-   Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
> 
> -   While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> -   You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
> -   If you don't use private folders, it would be helpful to know Next.js [special file conventions](index.md#routing-files) to prevent unexpected naming conflicts.

### Route groups[](#route-groups)

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-route-groups.png)

Route groups are useful for:

-   Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
-   Enabling nested layouts in the same route segment level:
    -   [Creating multiple nested layouts in the same segment, including multiple root layouts](#creating-multiple-root-layouts)
    -   [Adding a layout to a subset of routes in a common segment](#opting-specific-segments-into-a-layout)

### `src` folder[](#src-folder)

Next.js supports storing application code (including `app`) inside an optional [`src` folder](../../api-reference/file-conventions/src-folder/index.md). This separates application code from project configuration files which mostly live in the root of a project.

![An example folder structure with the \`src\` folder](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-src-directory.png)

## Examples[](#examples)

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

### Store project files outside of `app`[](#store-project-files-outside-of-app)

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

![An example folder structure with project files outside of app](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-project-root.png)

### Store project files in top-level folders inside of `app`[](#store-project-files-in-top-level-folders-inside-of-app)

This strategy stores all application code in shared folders in the **root of the `app` directory**.

![An example folder structure with project files inside app](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-app-root.png)

### Split project files by feature or route[](#split-project-files-by-feature-or-route)

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

![An example folder structure with project files split by feature or route](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-app-root-split.png)

### Organize routes without affecting the URL path[](#organize-routes-without-affecting-the-url-path)

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).

![Organizing Routes with Route Groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-organisation.png)

Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.

![Route Groups with Multiple Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-multiple-layouts.png)

### Opting specific segments into a layout[](#opting-specific-segments-into-a-layout)

To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).

![Route Groups with Opt-in Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-opt-in-layouts.png)

### Opting for loading skeletons on a specific route[](#opting-for-loading-skeletons-on-a-specific-route)

To apply a [loading skeleton](../../api-reference/file-conventions/loading/index.md) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.

![Folder structure showing a loading.tsx and a page.tsx inside the route group](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-loading.png)

Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.

### Creating multiple root layouts[](#creating-multiple-root-layouts)

To create multiple [root layouts](../../api-reference/file-conventions/layout/index.md#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.

![Route Groups with Multiple Root Layouts](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-group-multiple-root-layouts.png)

In the example above, both `(marketing)` and `(shop)` have their own root layout.

Was this helpful?
