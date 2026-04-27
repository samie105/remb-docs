---
title: "Installation"
source: "https://nextjs.org/docs/app/getting-started/installation"
canonical_url: "https://nextjs.org/docs/app/getting-started/installation"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:12:04.627Z"
content_hash: "38fc9fd01b448ac52bf0c9849d7cbefbbc985b6e2f79d4e99a1825e608b09a27"
menu_path: ["Installation"]
section_path: []
version: "latest"
tab_variants: ["pnpm","npm","yarn","bun","pnpm","npm","yarn","bun","pnpm","npm","yarn","bun"]
content_language: "en"
---
[App Router](/docs/app)[Getting Started](/docs/app/getting-started)Installation

# Installation

Last updated April 23, 2026

Create a new Next.js app and run it locally.

## Quick start[](#quick-start)

1.  Create a new Next.js app named `my-app`
2.  `cd my-app` and start the dev server.
3.  Visit `http://localhost:3000`.

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
pnpm create next-app@latest my-app --yes
cd my-app
pnpm dev
```

-   `--yes` skips prompts using saved preferences or defaults. The default setup enables TypeScript, Tailwind CSS, ESLint, App Router, and Turbopack, with import alias `@/*`, and includes `AGENTS.md` (with a `CLAUDE.md` that references it) to guide coding agents to write up-to-date Next.js code.

## System requirements[](#system-requirements)

Before you begin, make sure your development environment meets the following requirements:

-   Minimum Node.js version: [20.9](https://nodejs.org/)
-   Operating systems: macOS, Windows (including WSL), and Linux.

## Supported browsers[](#supported-browsers)

Next.js supports modern browsers with zero configuration.

-   Chrome 111+
-   Edge 111+
-   Firefox 111+
-   Safari 16.4+

Learn more about [browser support](/docs/architecture/supported-browsers), including how to configure polyfills and target specific browsers.

## Create with the CLI[](#create-with-the-cli)

The quickest way to create a new Next.js app is using [`create-next-app`](/docs/app/api-reference/cli/create-next-app), which sets up everything automatically for you. To create a project, run:

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
pnpm create next-app
```

On installation, you'll see the following prompts:

Terminal

```
What is your project named? my-app
Would you like to use the recommended Next.js defaults?
    Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, AGENTS.md
    No, reuse previous settings
    No, customize settings - Choose your own preferences
```

If you choose to `customize settings`, you'll see the following prompts:

Terminal

```
Would you like to use TypeScript? No / Yes
Which linter would you like to use? ESLint / Biome / None
Would you like to use React Compiler? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
Would you like to include AGENTS.md to guide coding agents to write up-to-date Next.js code? No / Yes
```

After the prompts, [`create-next-app`](/docs/app/api-reference/cli/create-next-app) will create a folder with your project name and install the required dependencies.

## Manual installation[](#manual-installation)

To manually create a new Next.js app, install the required packages:

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
pnpm i next@latest react@latest react-dom@latest
```

> **Good to know**:
> 
> -   The `App Router` uses [React canary releases](https://react.dev/blog/2023/05/03/react-canaries) built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks, but you should still declare react and react-dom in package.json for tooling and ecosystem compatibility.
> -   The `Pages Router` uses the React version from your `package.json`.

Then, add the following scripts to your `package.json` file:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

These scripts refer to the different stages of developing an application:

-   `next dev`: Starts the development server using Turbopack (default bundler).
-   `next build`: Builds the application for production.
-   `next start`: Starts the production server.
-   `eslint`: Runs ESLint.

Turbopack is now the default bundler. To use Webpack run `next dev --webpack` or `next build --webpack`. See the [Turbopack docs](/docs/app/api-reference/turbopack) for configuration details.

### Create the `app` directory[](#create-the-app-directory)

Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.

Create an `app` folder. Then, inside `app`, create a `layout.tsx` file. This file is the [root layout](/docs/app/api-reference/file-conventions/layout#root-layout). It's required and must contain the `<html>` and `<body>` tags.

app/layout.tsx

JavaScriptTypeScript

```
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

Create a home page `app/page.tsx` with some initial content:

app/page.tsx

JavaScriptTypeScript

```
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

Both `layout.tsx` and `page.tsx` will be rendered when the user visits the root of your application (`/`).

![App Folder Structure](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/app-getting-started.png)

> **Good to know**:
> 
> -   If you forget to create the root layout, Next.js will automatically create this file when running the development server with `next dev`.
> -   You can optionally use a [`src` folder](/docs/app/api-reference/file-conventions/src-folder) in the root of your project to separate your application's code from configuration files.

### Create the `public` folder (optional)[](#create-the-public-folder-optional)

Create a [`public` folder](/docs/app/api-reference/file-conventions/public-folder) at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

You can then reference these assets using the root path (`/`). For example, `public/profile.png` can be referenced as `/profile.png`:

app/page.tsx

JavaScriptTypeScript

```
import Image from 'next/image'
 
export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

## Run the development server[](#run-the-development-server)

1.  Run `npm run dev` to start the development server.
2.  Visit `http://localhost:3000` to view your application.
3.  Edit the `app/page.tsx` file and save it to see the updated result in your browser.

## Set up TypeScript[](#set-up-typescript)

> Minimum TypeScript version: `v5.1.0`

Next.js comes with built-in TypeScript support. To add TypeScript to your project, rename a file to `.ts` / `.tsx` and run `next dev`. Next.js will automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

### IDE Plugin[](#ide-plugin)

Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.

You can enable the plugin in VS Code by:

1.  Opening the command palette (`Ctrl/⌘` + `Shift` + `P`)
2.  Searching for "TypeScript: Select TypeScript Version"
3.  Selecting "Use Workspace Version"

![TypeScript Command Palette](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/typescript-command-palette.png)

See the [TypeScript reference](/docs/app/api-reference/config/typescript) page for more information.

## Set up linting[](#set-up-linting)

Next.js supports linting with either ESLint or Biome. Choose a linter and run it directly via `package.json` scripts.

-   Use **ESLint** (comprehensive rules):

package.json

```
{
  "scripts": {
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

-   Or use **Biome** (fast linter + formatter):

package.json

```
{
  "scripts": {
    "lint": "biome check",
    "format": "biome format --write"
  }
}
```

If your project previously used `next lint`, migrate your scripts to the ESLint CLI with the codemod:

Terminal

```
npx @next/codemod@canary next-lint-to-eslint-cli .
```

If you use ESLint, create an explicit config (recommended `eslint.config.mjs`). ESLint supports both [the legacy `.eslintrc.*` and the newer `eslint.config.mjs` formats](https://eslint.org/docs/latest/use/configure/configuration-files#configuring-eslint). See the [ESLint API reference](/docs/app/api-reference/config/eslint#with-core-web-vitals) for a recommended setup.

> **Good to know**: Starting with Next.js 16, `next build` no longer runs the linter automatically. Instead, you can run your linter through NPM scripts.

See the [ESLint Plugin](/docs/app/api-reference/config/eslint) page for more information.

## Set up Absolute Imports and Module Path Aliases[](#set-up-absolute-imports-and-module-path-aliases)

Next.js has in-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files.

These options allow you to alias project directories to absolute paths, making it easier and cleaner to import modules. For example:

```
// Before
import { Button } from '../../../components/button'
 
// After
import { Button } from '@/components/button'
```

To configure absolute imports, add the `baseUrl` configuration option to your `tsconfig.json` or `jsconfig.json` file. For example:

tsconfig.json or jsconfig.json

```
{
  "compilerOptions": {
    "baseUrl": "src/"
  }
}
```

In addition to configuring the `baseUrl` path, you can use the `"paths"` option to `"alias"` module paths.

For example, the following configuration maps `@/components/*` to `components/*`:

tsconfig.json or jsconfig.json

```
{
  "compilerOptions": {
    "baseUrl": "src/",
    "paths": {
      "@/styles/*": ["styles/*"],
      "@/components/*": ["components/*"]
    }
  }
}
```

Each of the `"paths"` are relative to the `baseUrl` location.

Was this helpful?
