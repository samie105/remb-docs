---
title: "src Directory"
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder"
canonical_url: "https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:22:07.167Z"
content_hash: "4d6b68fc557315aa5f479084c4e4cb1e2e773b99c6fa50411efc042d654e933c"
menu_path: ["src Directory"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/file-conventions/public-folder/index.md", "title": "public Folder"}
nav_next: {"path": "nextjs/docs/pages/api-reference/functions/index.md", "title": "Functions"}
---

# src Directory

Last updated April 15, 2026

As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` folder.

This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.

To use the `src` folder, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.

![An example folder structure with the \`src\` folder](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![An example folder structure with the \`src\` folder](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)

> **Good to know**:
> 
> *   The `/public` directory should remain in the root of your project.
> *   Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
> *   `.env.*` files should remain in the root of your project.
> *   `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
> *   If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
> *   If you're using Proxy, ensure it is placed inside the `src` folder.
> *   If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the [content section](https://tailwindcss.com/docs/content-configuration).
> *   If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.

Was this helpful?

supported.

Send


