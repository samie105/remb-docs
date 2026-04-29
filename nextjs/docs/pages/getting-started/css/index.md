---
title: "How to use CSS in your application"
source: "https://nextjs.org/docs/pages/getting-started/css"
canonical_url: "https://nextjs.org/docs/pages/getting-started/css"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:22:59.806Z"
content_hash: "b8a5400fdf490032c5b4606cc6438cdcaf2f39c04b87f512a8a8e392abaf84ba"
menu_path: ["How to use CSS in your application"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/getting-started/fonts/index.md", "title": "How to use fonts"}
nav_next: {"path": "nextjs/docs/pages/getting-started/deploying/index.md", "title": "How to deploy your Next.js application"}
---

# How to use CSS in your application

Last updated April 23, 2026

Next.js provides several ways to style your application using CSS, including:

-   [Tailwind CSS](#tailwind-css)
-   [CSS Modules](#css-modules)
-   [Global CSS](#global-css)
-   [External Stylesheets](#external-stylesheets)
-   [Sass](../../../app/guides/sass/index.md)
-   [CSS-in-JS](../../../app/guides/css-in-js/index.md)

## Tailwind CSS[](#tailwind-css)

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that provides low-level utility classes to build custom designs.

Install Tailwind CSS:

#### pnpm

pnpm

#### npm

npm

#### yarn

yarn

#### bun

bun

Terminal

```
pnpm add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:

postcss.config.mjs

```
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:

styles/globals.css

```
@import 'tailwindcss';
```

Import the CSS file in your `pages/_app.js` file:

pages/\_app.js

```
import '@/styles/globals.css'
 
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Now you can start using Tailwind's utility classes in your application:

pages/index.tsx

JavaScriptTypeScript

```
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](../../../app/guides/tailwind-v3-css/index.md).

## CSS Modules[](#css-modules)

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `pages` directory:

/styles/blog.module.css

```
.blog {
  padding: 24px;
}
```

pages/blog/index.tsx

JavaScriptTypeScript

```
import styles from './blog.module.css'
 
export default function Page() {
  return <main className={styles.blog}></main>
}
```

## Global CSS[](#global-css)

You can use global CSS to apply styles across your application.

Import the stylesheet in the `pages/_app.js` file to apply the styles to **every route** in your application:

pages/\_app.js

```
import '@/styles/global.css'
 
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Due to the global nature of stylesheets, and to avoid conflicts, you should import them inside [`pages/_app.js`](../../building-your-application/routing/custom-app/index.md).

## External stylesheets[](#external-stylesheets)

Next.js allows you to import CSS files from a JavaScript file. This is possible because Next.js extends the concept of [`import`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import) beyond JavaScript.

### Import styles from `node_modules`[](#import-styles-from-node_modules)

Since Next.js **9.5.4**, importing a CSS file from `node_modules` is permitted anywhere in your application.

For global stylesheets, like `bootstrap` or `nprogress`, you should import the file inside `pages/_app.js`. For example:

pages/\_app.js

```
import 'bootstrap/dist/css/bootstrap.css'
 
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

To import CSS required by a third-party component, you can do so in your component. For example:

components/example-dialog.js

```
import { useState } from 'react'
import { Dialog } from '@reach/dialog'
import VisuallyHidden from '@reach/visually-hidden'
import '@reach/dialog/styles.css'
 
function ExampleDialog(props) {
  const [showDialog, setShowDialog] = useState(false)
  const open = () => setShowDialog(true)
  const close = () => setShowDialog(false)
 
  return (
    <div>
      <button onClick={open}>Open Dialog</button>
      <Dialog isOpen={showDialog} onDismiss={close}>
        <button className="close-button" onClick={close}>
          <VisuallyHidden>Close</VisuallyHidden>
          <span aria-hidden>×</span>
        </button>
        <p>Hello there. I am a dialog</p>
      </Dialog>
    </div>
  )
}
```

## Ordering and Merging[](#ordering-and-merging)

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.

For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:

page.tsx

JavaScriptTypeScript

```
import { BaseButton } from './base-button'
import styles from './page.module.css'
 
export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

base-button.tsx

JavaScriptTypeScript

```
import styles from './base-button.module.css'
 
export function BaseButton() {
  return <button className={styles.primary} />
}
```

### Recommendations[](#recommendations)

To keep CSS ordering predictable:

-   Try to contain CSS imports to a single JavaScript or TypeScript entry file
-   Import global styles and Tailwind stylesheets in the root of your application.
-   **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
-   Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
-   Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
-   Extract shared styles into shared components to avoid duplicate imports.
-   Turn off linters or formatters that auto-sort imports like ESLint’s [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports).
-   You can use the [`cssChunking`](../../../app/api-reference/config/next-config-js/cssChunking/index.md) option in `next.config.js` to control how CSS is chunked.

## Development vs Production[](#development-vs-production)

-   In development (`next dev`), CSS updates apply instantly with [Fast Refresh](../../../architecture/fast-refresh/index.md).
-   In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
-   CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
-   CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.

## Next Steps

Learn more about the features mentioned in this page.

[

### Tailwind CSS

Style your Next.js Application using Tailwind CSS.

](/docs/pages/guides/tailwind-v3-css)[

### Sass

Learn how to use Sass in your Next.js application.

](/docs/pages/guides/sass)[

### CSS-in-JS

Use CSS-in-JS libraries with Next.js

](/docs/pages/guides/css-in-js)

Was this helpful?
