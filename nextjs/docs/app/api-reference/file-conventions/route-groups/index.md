---
title: "Route Groups"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-groups"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/route-groups"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:09:25.220Z"
content_hash: "33fa7e2a0bdb8d45ce61fc490bc52d45764b14cfbc4609dd977a631cb8e1c5d6"
menu_path: ["Route Groups"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/route-segment-config/runtime/index.md", "title": "runtime"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/src-folder/index.md", "title": "src Folder"}
---

# Route Groups

Last updated April 23, 2026

Route Groups are a folder convention that let you organize routes by category or team.

## Convention[](#convention)

A route group can be created by wrapping a folder's name in parenthesis: `(folderName)`.

This convention indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-route-groups.png)

## Use cases[](#use-cases)

-   Organizing routes by team, concern, or feature.
-   Defining multiple [root layouts](../layout/index.md#root-layout).
-   Opting specific route segments into sharing a layout, while keeping others out.

## Caveats[](#caveats)

-   **Full page load**: If you navigate between routes that use different root layouts, it'll trigger a full page reload. For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js`. This **only** applies to multiple root layouts.
-   **Conflicting paths**: Routes in different groups should not resolve to the same URL path. For example, `(marketing)/about/page.js` and `(shop)/about/page.js` would both resolve to `/about` and cause an error.
-   **Top-level root layout**: If you use multiple root layouts without a top-level `layout.js` file, make sure your home route (/) is defined within one of the route groups, e.g. app/(marketing)/page.js.

Was this helpful?
