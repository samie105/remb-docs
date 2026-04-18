---
title: "template.js"
source: "https://nextjs.org/docs/app/api-reference/file-conventions/template"
canonical_url: "https://nextjs.org/docs/app/api-reference/file-conventions/template"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:11:01.108Z"
content_hash: "b82e3fd27e4dada3d344d14c72866e36416d7a12e465b2e8131c86c6679340ad"
menu_path: ["template.js"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/file-conventions/src-folder/index.md", "title": "src Folder"}
nav_next: {"path": "nextjs/docs/app/api-reference/file-conventions/unauthorized/index.md", "title": "unauthorized.js"}
---

# template.js

Last updated April 15, 2026

A **template** file is similar to a [layout](/docs/app/getting-started/layouts-and-pages#creating-a-layout) in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.

They are useful when you need to:

*   Resynchronize `useEffect` on navigation.
*   Reset the state of a child Client Components on navigation. For example, an input field.
*   To change default framework behavior. For example, Suspense boundaries inside layouts only show a fallback on first load, while templates show it on every navigation.

## Convention[](#convention)

A template can be defined by exporting a default React component from a `template.js` file. The component should accept a `children` prop.

![template.js special file](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftemplate-special-file.png&w=3840&q=75)![template.js special file](/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftemplate-special-file.png&w=3840&q=75)

app/template.tsx

TypeScript

JavaScriptTypeScript

```
export default function Template({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

In terms of nesting, `template.js` is rendered between a layout and its children. Here's a simplified output:

Output

```
<Layout>
  {/* Note that the template is given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

In the [component hierarchy](/docs/app/getting-started/project-structure#component-hierarchy), `template.js` renders between `layout.js` and `error.js`. It wraps `error.js`, `loading.js`, `not-found.js`, and `page.js`, but does **not** wrap the `layout.js` in the same segment.

## Props[](#props)

### `children` (required)[](#children-required)

Template accepts a `children` prop.

Output

```
<Layout>
  {/* Note that the template is automatically given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

## Behavior[](#behavior)

*   **Server Components**: By default, templates are Server Components.
*   **With navigation**: Templates receive a unique key for their own segment level. They remount when that segment (including its dynamic params) changes. Navigations within deeper segments do not remount higher-level templates. Search params do not trigger remounts.
*   **State reset**: Any Client Component inside the template will reset its state on navigation.
*   **Effect re-run**: Effects like `useEffect` will re-synchronize as the component remounts.
*   **DOM reset**: DOM elements inside the template are fully recreated.

### Templates during navigation and remounting[](#templates-during-navigation-and-remounting)

This section illustrates how templates behave during navigation. It shows, step by step, which templates remount on each route change and why.

Using this project tree:

```
app
├── about
│   ├── page.tsx
├── blog
│   ├── [slug]
│   │   └── page.tsx
│   ├── page.tsx
│   └── template.tsx
├── layout.tsx
├── page.tsx
└── template.tsx
```

Starting at `/`, the React tree looks roughly like this.

> Note: The `key` values shown in the examples are illustrative, the values in your application may differ.

Output

```
<RootLayout>
  {/* app/template.tsx */}
  <Template key="/">
    <Page />
  </Template>
</RootLayout>
```

Navigating to `/about` (first segment changes), the root template key changes, it remounts:

Output

```
<RootLayout>
  {/* app/template.tsx */}
  <Template key="/about">
    <AboutPage />
  </Template>
</RootLayout>
```

Navigating to `/blog` (first segment changes), the root template key changes, it remounts and the blog-level template mounts:

Output

```
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    <Template key="/blog">
      <BlogIndexPage />
    </Template>
  </Template>
</RootLayout>
```

Navigating within the same first segment to `/blog/first-post` (child segment changes), the root template key doesn't change, but the blog-level template key changes, it remounts:

Output

```
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    {/* remounts because the child segment at this level changed */}
    <Template key="/blog/first-post">
      <BlogPostPage slug="first-post" />
    </Template>
  </Template>
</RootLayout>
```

Navigating to `/blog/second-post` (same first segment, different child segment), the root template key doesn't change, but the blog-level template key changes, it remounts again:

Output

```
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    {/* remounts again due to changed child segment */}
    <Template key="/blog/second-post">
      <BlogPostPage slug="second-post" />
    </Template>
  </Template>
</RootLayout>
```

## Version History[](#version-history)

Version

Changes

`v13.0.0`

`template` introduced.

[Previous

src

](/docs/app/api-reference/file-conventions/src-folder)

[Next

unauthorized.js

](/docs/app/api-reference/file-conventions/unauthorized)

Was this helpful?

supported.

Send




