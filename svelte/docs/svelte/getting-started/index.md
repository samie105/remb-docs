---
title: "Getting started"
source: "https://svelte.dev/docs/svelte/getting-started"
canonical_url: "https://svelte.dev/docs/svelte/getting-started"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:48.327Z"
content_hash: "c03eb144df1891cad8d1b1e97f722a6fbdb42c09bd6f57f247e79c2b133a4edd"
menu_path: ["Getting started"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/overview/index.md", "title": "Overview"}
nav_next: {"path": "svelte/docs/svelte/svelte-files/index.md", "title": ".svelte files"}
---

We recommend using [SvelteKit](../kit), which lets you [build almost anything](../kit/project-types). It's the official application framework from the Svelte team and powered by [Vite](https://vite.dev/). Create a new project with:

```
npx sv create myapp
cd myapp
npm install
npm run dev
```

Don't worry if you don't know Svelte yet! You can ignore all the nice features SvelteKit brings on top for now and dive into it later.

## Alternatives to SvelteKit[](#Alternatives-to-SvelteKit)

You can also use Svelte directly with Vite via [vite-plugin-svelte](https://github.com/sveltejs/vite-plugin-svelte) by running `npm create vite@latest` and selecting the `svelte` option (or, if working with an existing project, adding the plugin to your `vite.config.js` file). With this, `npm run build` will generate HTML, JS, and CSS files inside the `dist` directory. In most cases, you will probably need to [choose a routing library](/packages#routing) as well.

> Vite is often used in standalone mode to build [single page apps (SPAs)](../kit/glossary#SPA), which you can also [build with SvelteKit](../kit/single-page-apps).

There are also [plugins for other bundlers](/packages#bundler-plugins), but we recommend Vite.

## Editor tooling[](#Editor-tooling)

The Svelte team maintains a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode), and there are integrations with various other [editors](https://sveltesociety.dev/collection/editor-support-c85c080efc292a34) and tools as well.

You can also check your code from the command line using [`npx sv check`](https://svelte.dev/docs/cli/sv-check).

## Getting help[](#Getting-help)

Don't be shy about asking for help in the [Discord chatroom](/chat)! You can also find answers on [Stack Overflow](https://stackoverflow.com/questions/tagged/svelte).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/01-introduction/02-getting-started.md) [llms.txt](/docs/svelte/getting-started/llms.txt)

previous next

[Overview](/docs/svelte/overview) [.svelte files](/docs/svelte/svelte-files)


