---
title: "How to install Tailwind CSS v3 in your Next.js application"
source: "https://nextjs.org/docs/app/guides/tailwind-v3-css"
canonical_url: "https://nextjs.org/docs/app/guides/tailwind-v3-css"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:29.133Z"
content_hash: "3daa6fd65b0927b60d51c4cd402b3d6d71921afcc0fda7047d4011254df4c2a8"
menu_path: ["How to install Tailwind CSS v3 in your Next.js application"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/streaming/index.md", "title": "Streaming"}
nav_next: {"path": "nextjs/docs/app/guides/testing/index.md", "title": "Testing"}
---

# How to install Tailwind CSS v3 in your Next.js application

Last updated April 15, 2026

This guide will walk you through how to install [Tailwind CSS v3](https://v3.tailwindcss.com/) in your Next.js application.

> **Good to know:** For the latest Tailwind 4 setup, see the [Tailwind CSS setup instructions](/docs/app/getting-started/css#tailwind-css).

## Installing Tailwind v3[](#installing-tailwind-v3)

Install Tailwind CSS and its peer dependencies, then run the `init` command to generate both `tailwind.config.js` and `postcss.config.js` files:

pnpmnpmyarnbun

Terminal

```
pnpm add -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p
```

## Configuring Tailwind v3[](#configuring-tailwind-v3)

Configure your template paths in your `tailwind.config.js` file:

tailwind.config.js

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Add the Tailwind directives to your global CSS file:

app/globals.css

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Import the CSS file in your root layout:

app/layout.tsx

TypeScript

JavaScriptTypeScript

```
import './globals.css'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

## Using classes[](#using-classes)

After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.

app/page.tsx

TypeScript

JavaScriptTypeScript

```
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

## Usage with Turbopack[](#usage-with-turbopack)

As of Next.js 13.1, Tailwind CSS and PostCSS are supported with [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css).

[Previous

Streaming

](/docs/app/guides/streaming)

[Next

Testing

](/docs/app/guides/testing)

Was this helpful?

supported.

Send
