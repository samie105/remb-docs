---
title: "Route Groups"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-groups"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-groups"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:10:42.865Z"
content_hash: "ab7c4c203a3f097d4e685e8ac86b40d7541d90b84b311d8cfbdf0bf79db3d608"
menu_path: ["Route Groups"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/runtime/index.md", "title": "runtime"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/src-folder/index.md", "title": "src Folder"}
---

# Route Groups

Last updated April 15, 2026

Route Groups are a folder convention that let you organize routes by category or team.

## Convention[](#convention)

A route group can be created by wrapping a folder's name in parenthesis: `(folderName)`.

This convention indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-route-groups.png&w=3840&q=75)![An example folder structure using route groups](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-route-groups.png&w=3840&q=75)

## Use cases[](#use-cases)

*   Organizing routes by team, concern, or feature.
*   Defining multiple [root layouts](/docs/app/api-reference/file-conventions/layout#root-layout).
*   Opting specific route segments into sharing a layout, while keeping others out.

## Caveats[](#caveats)

*   **Full page load**: If you navigate between routes that use different root layouts, it'll trigger a full page reload. For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js`. This **only** applies to multiple root layouts.
*   **Conflicting paths**: Routes in different groups should not resolve to the same URL path. For example, `(marketing)/about/page.js` and `(shop)/about/page.js` would both resolve to `/about` and cause an error.
*   **Top-level root layout**: If you use multiple root layouts without a top-level `layout.js` file, make sure your home route (/) is defined within one of the route groups, e.g. app/(marketing)/page.js.

[Previous

route.js

](/docs/app/api-reference/file-conventions/route)

[Next

src

](/docs/app/api-reference/file-conventions/src-folder)

Was this helpful?

supported.

Send




