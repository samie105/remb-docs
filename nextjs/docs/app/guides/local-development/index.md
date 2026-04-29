---
title: "How to optimize your local development environment"
source: "https://nextjs.org/docs/app/guides/local-development"
canonical_url: "https://nextjs.org/docs/app/guides/local-development"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:13:59.416Z"
content_hash: "a2081c6d76d59a098e7b297665d1a9c0c113fb17e04adf81291a67f1adeddac6"
menu_path: ["How to optimize your local development environment"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun"]
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/guides/lazy-loading/index.md", "title": "How to lazy load Client Components and libraries"}
nav_next: {"path": "nextjs/docs/app/guides/mcp/index.md", "title": "Enabling Next.js MCP Server for Coding Agents"}
---

# How to optimize your local development environment

Last updated April 23, 2026

Next.js is designed to provide a great developer experience. As your application grows, you might notice slower compilation times during local development. This guide will help you identify and fix common compile-time performance issues.

## Local dev vs. production[](#local-dev-vs-production)

The development process with `next dev` is different than `next build` and `next start`.

`next dev` compiles routes in your application as you open or navigate to them. This enables you to start the dev server without waiting for every route in your application to compile, which is both faster and uses less memory. Running a production build applies other optimizations, like minifying files and creating content hashes, which are not needed for local development.

## Improving local dev performance[](#improving-local-dev-performance)

### 1\. Check your computer's antivirus[](#1-check-your-computers-antivirus)

Antivirus software can slow down file access. While this is more common on Windows machines, this can be an issue for any system with an antivirus tool installed.

On Windows, you can add your project to the [Microsoft Defender Antivirus exclusion list](https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e#bkmk_threat-protection-settings).

1.  Open the **"Windows Security"** application and then select **"Virus & threat protection"** → **"Manage settings"** → **"Add or remove exclusions"**.
2.  Add a **"Folder"** exclusion. Select your project folder.

On macOS, you can disable [Gatekeeper](https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-sec5599b66df/web) inside of your terminal.

1.  Run `sudo spctl developer-mode enable-terminal` in your terminal.
2.  Open the **"System Settings"** app and then select **"Privacy & Security"** → **"Developer Tools"**.
3.  Ensure your terminal is listed and enabled. If you're using a third-party terminal like iTerm or Ghostty, add that to the list.
4.  Restart your terminal.

![Screenshot of macOS System Settings showing the Privacy & Security pane](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/macos-gatekeeper-privacy-and-security.png)

![Screenshot of macOS System Settings showing the Developer Tools options](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/macos-gatekeeper-developer-tools.png)

If you or your employer have configured any other Antivirus solutions on your system, you should inspect the relevant settings for those products.

### 2\. Update Next.js and use Turbopack[](#2-update-nextjs-and-use-turbopack)

Make sure you're using the latest version of Next.js. Each new version often includes performance improvements.

Turbopack is now the default bundler for Next.js development and provides significant performance improvements over webpack.

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
pnpm add next@latest
pnpm dev  # Turbopack is used by default
```

If you need to use Webpack instead of Turbopack, you can opt-in:

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
pnpm dev --webpack
```

[Learn more about Turbopack](/blog/turbopack-for-development-stable). See our [upgrade guides](../upgrading/index.md) and codemods for more information.

### 3\. Check your imports[](#3-check-your-imports)

The way you import code can greatly affect compilation and bundling time. Learn more about [optimizing package bundling](../package-bundling/index.md) and explore tools like [Dependency Cruiser](https://github.com/sverweij/dependency-cruiser) or [Madge](https://github.com/pahen/madge).

#### Icon libraries[](#icon-libraries)

Libraries like `@material-ui/icons`, `@phosphor-icons/react`, or `react-icons` can import thousands of icons, even if you only use a few. Try to import only the icons you need:

```
// Instead of this:
import { TriangleIcon } from '@phosphor-icons/react'
 
// Do this:
import { TriangleIcon } from '@phosphor-icons/react/dist/csr/Triangle'
```

You can often find what import pattern to use in the documentation for the icon library you're using. This example follows [`@phosphor-icons/react`](https://www.npmjs.com/package/@phosphor-icons/react#import-performance-optimization) recommendation.

Libraries like `react-icons` includes many different icon sets. Choose one set and stick with that set.

For example, if your application uses `react-icons` and imports all of these:

-   `pi` (Phosphor Icons)
-   `md` (Material Design Icons)
-   `tb` (tabler-icons)
-   `cg` (cssgg)

Combined they will be tens of thousands of modules that the compiler has to handle, even if you only use a single import from each.

#### Barrel files[](#barrel-files)

"Barrel files" are files that export many items from other files. They can slow down builds because the compiler has to parse them to find if there are side-effects in the module scope by using the import.

Try to import directly from specific files when possible. [Learn more about barrel files](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js) and the built-in optimizations in Next.js.

#### Optimize package imports[](#optimize-package-imports)

Next.js can automatically optimize imports for certain packages. If you are using packages that utilize barrel files, add them to your `next.config.js`:

```
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

Turbopack automatically analyzes imports and optimizes them. It does not require this configuration.

### 4\. Check your Tailwind CSS setup[](#4-check-your-tailwind-css-setup)

If you're using Tailwind CSS, make sure it's set up correctly.

A common mistake is configuring your `content` array in a way which includes `node_modules` or other large directories of files that should not be scanned.

Tailwind CSS version 3.4.8 or newer will warn you about settings that might slow down your build.

1.  In your `tailwind.config.js`, be specific about which files to scan:
    
    ```
    module.exports = {
      content: [
        './src/**/*.{js,ts,jsx,tsx}', // Good
        // This might be too broad
        // It will match `packages/**/node_modules` too
        // '../../packages/**/*.{js,ts,jsx,tsx}',
      ],
    }
    ```
    
2.  Avoid scanning unnecessary files:
    
    ```
    module.exports = {
      content: [
        // Better - only scans the 'src' folder
        '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
      ],
    }
    ```
    

### 5\. Check custom webpack settings[](#5-check-custom-webpack-settings)

If you've added custom webpack settings, they might be slowing down compilation.

Consider if you really need them for local development. You can optionally only include certain tools for production builds, or explore using the default Turbopack bundler and configuring [loaders](../../api-reference/config/next-config-js/turbopack/index.md#configuring-webpack-loaders) instead.

### 6\. Optimize memory usage[](#6-optimize-memory-usage)

If your app is very large, it might need more memory.

[Learn more about optimizing memory usage](../memory-usage/index.md).

### 7\. Server Components and data fetching[](#7-server-components-and-data-fetching)

Changes to Server Components cause the entire page to re-render locally in order to show the new changes, which includes fetching new data for the component.

The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

[Learn more about the experimental option](../../api-reference/config/next-config-js/serverComponentsHmrCache/index.md).

### 8\. Consider local development over Docker[](#8-consider-local-development-over-docker)

If you're using Docker for development on Mac or Windows, you may experience significantly slower performance compared to running Next.js locally.

Docker's filesystem access on Mac and Windows can cause Hot Module Replacement (HMR) to take seconds or even minutes, while the same application runs with fast HMR when developed locally.

This performance difference is due to how Docker handles filesystem operations outside of Linux environments. For the best development experience:

-   Use local development (`npm run dev` or `pnpm dev`) instead of Docker during development
-   Reserve Docker for production deployments and testing production builds
-   If you must use Docker for development, consider using Docker on a Linux machine or VM

[Learn more about Docker deployment](../../getting-started/deploying/index.md#docker) for production use.

## Tools for finding problems[](#tools-for-finding-problems)

### Detailed fetch logging[](#detailed-fetch-logging)

Use the `logging.fetches` option in your `next.config.js` file, to see more detailed information about what's happening during development:

```
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

[Learn more about fetch logging](../../api-reference/config/next-config-js/logging/index.md).

### Turbopack tracing[](#turbopack-tracing)

Turbopack tracing is a tool that helps you understand the performance of your application during local development. It provides detailed information about the time taken for each module to compile and how they are related.

1.  Make sure you have the latest version of Next.js installed.
    
2.  Generate a Turbopack trace file:
    
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
    NEXT_TURBOPACK_TRACING=1 pnpm dev
    ```
    
3.  Navigate around your application or make edits to files to reproduce the problem.
    
4.  Stop the Next.js development server.
    
5.  A file called `trace-turbopack` will be available in the `.next/dev` folder.
    
6.  You can interpret the file using `npx next internal trace [path-to-file]`:
    
    ```
    npx next internal trace .next/dev/trace-turbopack
    ```
    
    On versions where `trace` is not available, the command was named `turbo-trace-server`:
    
    ```
    npx next internal turbo-trace-server .next/dev/trace-turbopack
    ```
    
7.  Once the trace server is running you can view the trace at [https://trace.nextjs.org/](https://trace.nextjs.org/).
    
8.  By default the trace viewer will aggregate timings, in order to see each individual time you can switch from "Aggregated in order" to "Spans in order" at the top right of the viewer.
    

> **Good to know**: The trace file is placed under the development server directory, which defaults to `.next/dev`.

### Still having problems?[](#still-having-problems)

Share the trace file generated in the [Turbopack Tracing](#turbopack-tracing) section and share it on [GitHub Discussions](https://github.com/vercel/next.js/discussions) or [Discord](https://nextjs.org/discord).

Was this helpful?
