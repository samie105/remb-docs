---
title: "HTML & static sites"
source: "https://bun.com/docs/bundler/html-static"
canonical_url: "https://bun.com/docs/bundler/html-static"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:49.965Z"
content_hash: "3f6a508c4836b1d6eef6dcc8ff649a4fc1ccbf9f4aa196268876268e89e2cd4c"
menu_path: ["HTML & static sites"]
section_path: []
nav_prev: {"path": "bun/bun/docs/bundler/hot-reloading/index.md", "title": "Hot reloading"}
nav_next: {"path": "bun/bun/docs/bundler/loaders/index.md", "title": "Loaders"}
---

# Or any npm client
bun install --dev bun-plugin-tailwind
```

Then, add the plugin to your `bunfig.toml`:

bunfig.toml

```
[serve.static]
plugins = ["bun-plugin-tailwind"]
```

Then, reference TailwindCSS in your HTML via `<link>` tag, `@import` in CSS, or import in JavaScript.

*   index.html
    
*   styles.css
    
*   app.ts
    

index.html

```
<!-- Reference TailwindCSS in your HTML -->
<link rel="stylesheet" href="tailwindcss" />
```

styles.css

```
@import "tailwindcss";
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
import "tailwindcss";
```

## Inline environment variables

Bun can replace `process.env.*` references in your JavaScript and TypeScript with their actual values at build time. This is useful for injecting configuration like API URLs or feature flags into your frontend code.

### Dev server (runtime)

To inline environment variables when using `bun ./index.html`, configure the `env` option in your `bunfig.toml`:

bunfig.toml

```
[serve.static]
env = "PUBLIC_*"  # only inline env vars starting with PUBLIC_ (recommended)
# env = "inline"  # inline all environment variables
# env = "disable" # disable env var replacement (default)
```

Then run the dev server:

terminal

```
PUBLIC_API_URL=https://api.example.com bun ./index.html
```

### Build for production

When building static HTML for production, use the `env` option to inline environment variables:

*   CLI
    
*   API
    

terminal

```
# Inline all environment variables
bun build ./index.html --outdir=dist --env=inline

# Only inline env vars with a specific prefix (recommended)
bun build ./index.html --outdir=dist --env=PUBLIC_*
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
// Inline all environment variables
await Bun.build({
  entrypoints: ["./index.html"],
  outdir: "./dist",
  env: "inline", 
});

// Only inline env vars with a specific prefix (recommended)
await Bun.build({
  entrypoints: ["./index.html"],
  outdir: "./dist",
  env: "PUBLIC_*", 
});
```

### Example

Given this source file:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)app.ts

```
const apiUrl = process.env.PUBLIC_API_URL;
console.log(`API URL: ${apiUrl}`);
```

And running with `PUBLIC_API_URL=https://api.example.com`:

terminal

```
PUBLIC_API_URL=https://api.example.com bun build ./index.html --outdir=dist --env=PUBLIC_*
```

The bundled output will contain:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/javascript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=5148f41bbc784f9828f1363dab67340f)dist/app.js

```
const apiUrl = "https://api.example.com";
console.log(`API URL: ${apiUrl}`);
```

## Echo console logs from browser to terminal

Bun’s dev server supports streaming console logs from the browser to the terminal. To enable, pass the `--console` CLI flag.

terminal

```
bun ./index.html --console
```

```
Bun v1.3.3
ready in 6.62ms
→ http://localhost:3000/
Press h + Enter to show shortcuts
```

Each call to `console.log` or `console.error` will be broadcast to the terminal that started the server. This is useful to see errors from the browser in the same place you run your server. This is also useful for AI agents that watch terminal output. Internally, this reuses the existing WebSocket connection from hot module reloading to send the logs.

## Edit files in the browser

Bun’s frontend dev server has support for Automatic Workspace Folders in Chrome DevTools, which lets you save edits to files in the browser.

## Keyboard Shortcuts

While the server is running:

*   `o + Enter` - Open in browser
*   `c + Enter` - Clear console
*   `q + Enter` (or `Ctrl+C`) - Quit server

## Build for Production

When you’re ready to deploy, use `bun build` to create optimized production bundles:

*   CLI
    
*   API
    

terminal

```
bun build ./index.html --minify --outdir=dist
```

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
await Bun.build({
  entrypoints: ["./index.html"],
  outdir: "./dist",
  minify: true,
});
```

### Watch Mode

You can run `bun build --watch` to watch for changes and rebuild automatically. This works nicely for library development.

## Plugin API

Need more control? Configure the bundler through the JavaScript API and use Bun’s builtin `HTMLRewriter` to preprocess HTML.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)build.ts

```
await Bun.build({
  entrypoints: ["./index.html"],
  outdir: "./dist",
  minify: true,

  plugins: [
    {
      // A plugin that makes every HTML tag lowercase
      name: "lowercase-html-plugin",
      setup({ onLoad }) {
        const rewriter = new HTMLRewriter().on("*", {
          element(element) {
            element.tagName = element.tagName.toLowerCase();
          },
          text(element) {
            element.replace(element.text.toLowerCase());
          },
        });

        onLoad({ filter: /\.html$/ }, async args => {
          const html = await Bun.file(args.path).text();

          return {
            // Bun's bundler will scan the HTML for <script> tags, <link rel="stylesheet"> tags, and other assets
            // and bundle them automatically
            contents: rewriter.transform(html),
            loader: "html",
          };
        });
      },
    },
  ],
});
```

## What Gets Processed?

Bun automatically handles all common web assets:

*   **Scripts** (`<script src>`) are run through Bun’s JavaScript/TypeScript/JSX bundler
*   **Stylesheets** (`<link rel="stylesheet">`) are run through Bun’s CSS parser & bundler
*   **Images** (`<img>`, `<picture>`) are copied and hashed
*   **Media** (`<video>`, `<audio>`, `<source>`) are copied and hashed
*   Any `<link>` tag with an `href` attribute pointing to a local file is rewritten to the new path, and hashed

All paths are resolved relative to your HTML file, so you can organize your project however you want.

## How this works

This is a small wrapper around Bun’s support for HTML imports in JavaScript.

## Standalone HTML

You can bundle your entire frontend into a **single self-contained `.html` file** with no external dependencies using `--compile --target=browser`. All JavaScript, CSS, and images are inlined directly into the HTML.

terminal

```
bun build --compile --target=browser ./index.html --outdir=dist
```

Learn more in the [Standalone HTML docs](bun/bun/docs/bundler/standalone-html/index.md).

## Adding a backend to your frontend

To add a backend to your frontend, you can use the “routes” option in `Bun.serve`. Learn more in the full-stack docs.
