---
title: "@astrojs/\n\t\t\t\t\treact"
source: "https://docs.astro.build/en/guides/integrations-guide/react/"
canonical_url: "https://docs.astro.build/en/guides/integrations-guide/react/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:37.000Z"
content_hash: "5c1a89f9d81b1935b4999d72054f6a88de877c41fe8385504986ac6b4876b688"
menu_path: ["@astrojs/\n\t\t\t\t\treact"]
section_path: []
nav_prev: {"path": "astro/en/guides/integrations-guide/preact/index.md", "title": "@astrojs/\n\t\t\t\t\tpreact"}
nav_next: {"path": "astro/en/guides/integrations-guide/solid-js/index.md", "title": "@astrojs/\n\t\t\t\t\tsolid-js"}
---

# @astrojs/ react

v5.0.3 [GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/react/) [npm](https://www.npmjs.com/package/@astrojs/react) [Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/react/CHANGELOG.md)

This **[Astro integration](../../integrations/index.md)** enables rendering and client-side hydration for your [React](https://react.dev/) components.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/react`, run the following from your project directory and follow the prompts:

*   [npm](#tab-panel-1721)
*   [pnpm](#tab-panel-1722)
*   [Yarn](#tab-panel-1723)

```
npx astro add react
```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/react` package:

*   [npm](#tab-panel-1724)
*   [pnpm](#tab-panel-1725)
*   [Yarn](#tab-panel-1726)

```
npm install @astrojs/react
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'react'` (or similar) warning when you start up Astro, you’ll need to install `react` and `react-dom` with its type definitions:

*   [npm](#tab-panel-1727)
*   [pnpm](#tab-panel-1728)
*   [Yarn](#tab-panel-1729)

```
npm install react react-dom @types/react @types/react-dom
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

```
import { defineConfig } from 'astro/config';import react from '@astrojs/react';
export default defineConfig({  // ...  integrations: [react()],});
```

And add the following code to the `tsconfig.json` file.

```
{  "extends": "astro/tsconfigs/strict",  "include": [".astro/types.d.ts", "**/*"],  "exclude": ["dist"],  "compilerOptions": {    "jsx": "react-jsx",    "jsxImportSource": "react"  }}
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first React component in Astro, head to our [UI framework documentation](../../framework-components/index.md#using-framework-components). You’ll explore:

*   📦 how framework components are loaded,
*   💧 client-side hydration options, and
*   🤝 opportunities to mix and nest frameworks together

## Integrate Actions with `useActionState()`

[Section titled “Integrate Actions with useActionState()”](#integrate-actions-with-useactionstate)

The `@astrojs/react` integration provides two functions for use with [Astro Actions](../../actions/index.md): `withState()` and `getActionState()`.

These are used with [React’s useActionState() hook](https://react.dev/reference/react/useActionState) to read and update client-side state when triggering actions during form submission.

### `withState()`

[Section titled “withState()”](#withstate)

**Type:** `(action: FormFn<T>) => (state: T, formData: FormData) => FormFn<T>`  

**Added in:** `@astrojs/react@4.4.0`

You can pass `withState()` and the action you want to trigger to React’s `useActionState()` hook as the form action function. The example below passes a `like` action to increase a counter along with an initial state of `0` likes.

```
import { actions } from 'astro:actions';import { withState } from '@astrojs/react/actions';import { useActionState } from "react";
export function Like({ postId }: { postId: string }) {  const [state, action, pending] = useActionState(    withState(actions.like),    { data: 0, error: undefined }, // initial likes and errors  );
  return (    <form action={action}>      <input type="hidden" name="postId" value={postId} />      <button disabled={pending}>{state.data} ❤️</button>    </form>  );}
```

The `withState()` function will match the action’s types with React’s expectations and preserve metadata used for progressive enhancement, allowing it to work even when JavaScript is disabled on the user’s device.

### `getActionState()`

[Section titled “getActionState()”](#getactionstate)

**Type:** `(context: ActionAPIContext) => Promise<T>`  

**Added in:** `@astrojs/react@4.4.0`

You can access the state stored by `useActionState()` on the server in your action `handler` with `getActionState()`. It accepts the [Astro API context](../../../reference/api-reference/index.md#the-context-object), and optionally, you can apply a type to the result.

The example below gets the current value of likes from a counter, typed as a number, in order to create an incrementing `like` action:

```
import { defineAction, type SafeResult } from 'astro:actions';import { z } from 'astro/zod';import { getActionState } from '@astrojs/react/actions';
export const server = {  like: defineAction({    input: z.object({      postId: z.string(),    }),    handler: async ({ postId }, ctx) => {      const { data: currentLikes = 0, error } = await getActionState<SafeResult<any, number>>(ctx);
      // handle errors      if (error) throw error;
      // write to database      return currentLikes + 1;    },  })};
```

## Options

[Section titled “Options”](#options)

### Combining multiple JSX frameworks

[Section titled “Combining multiple JSX frameworks”](#combining-multiple-jsx-frameworks)

When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

```
import { defineConfig } from 'astro/config';import preact from '@astrojs/preact';import react from '@astrojs/react';import svelte from '@astrojs/svelte';import vue from '@astrojs/vue';import solid from '@astrojs/solid-js';
export default defineConfig({  // Enable many frameworks to support all different kinds of components.  // No `include` is needed if you are only using a single JSX framework!  integrations: [    preact({      include: ['**/preact/*'],    }),    react({      include: ['**/react/*'],    }),    solid({      include: ['**/solid/*'],    }),  ],});
```

### Children parsing

[Section titled “Children parsing”](#children-parsing)

Children passed into a React component from an Astro component are parsed as plain strings, not React nodes.

For example, the `<ReactComponent />` below will only receive a single child element:

```
---import ReactComponent from './ReactComponent';---
<ReactComponent>  <div>one</div>  <div>two</div></ReactComponent>
```

If you are using a library that _expects_ more than one child element to be passed, for example so that it can slot certain elements in different places, you might find this to be a blocker.

You can set the experimental flag `experimentalReactChildren` to tell Astro to always pass children to React as React virtual DOM nodes. There is some runtime cost to this, but it can help with compatibility.

You can enable this option in the configuration for the React integration:

```
import { defineConfig } from 'astro/config';import react from '@astrojs/react';
export default defineConfig({  // ...  integrations: [    react({      experimentalReactChildren: true,    }),  ],});
```

### Disable streaming (experimental)

[Section titled “Disable streaming (experimental)”](#disable-streaming-experimental)

Astro streams the output of React components by default. However, you can disable this behavior by enabling the `experimentalDisableStreaming` option. This is particularly helpful for supporting libraries that don’t work well with streaming, like some CSS-in-JS solutions.

To disable streaming for all React components in your project, configure `@astrojs/react` with `experimentalDisableStreaming: true`:

```
import { defineConfig } from 'astro/config';import react from '@astrojs/react';
export default defineConfig({  // ...  integrations: [    react({      experimentalDisableStreaming: true,    })  ]});
```

## More integrations

### Front-end frameworks

*   ![](/logos/alpine-js.svg)
    
    ### [@astrojs/alpinejs](../alpinejs/index.md)
    
*   ![](/logos/preact.svg)
    
    ### [@astrojs/preact](../preact/index.md)
    
*   ![](/logos/react.svg)
    
    ### [@astrojs/react](index.md)
    
*   ![](/logos/solid.svg)
    
    ### [@astrojs/solid⁠-⁠js](../solid-js/index.md)
    
*   ![](/logos/svelte.svg)
    
    ### [@astrojs/svelte](../svelte/index.md)
    
*   ![](/logos/vue.svg)
    
    ### [@astrojs/vue](../vue/index.md)
    

### Adapters

*   ![](/logos/cloudflare-pages.svg)
    
    ### [@astrojs/cloudflare](../cloudflare/index.md)
    
*   ![](/logos/netlify.svg)
    
    ### [@astrojs/netlify](/en/guides/integrations-guide/netlify/)
    
*   ![](/logos/node.svg)
    
    ### [@astrojs/node](../node/index.md)
    
*   ![](/logos/vercel.svg)
    
    ### [@astrojs/vercel](../vercel/index.md)
    

### Other integrations

*   ![](/logos/db.svg)
    
    ### [@astrojs/db](../db/index.md)
    
*   ![](/logos/markdoc.svg)
    
    ### [@astrojs/markdoc](../markdoc/index.md)
    
*   ![](/logos/mdx.svg)
    
    ### [@astrojs/mdx](../mdx/index.md)
    
*   ![](/logos/partytown.svg)
    
    ### [@astrojs/partytown](../partytown/index.md)
    
*   ![](/logos/sitemap.svg)
    
    ### [@astrojs/sitemap](../sitemap/index.md)
    

[Contribute](../../../contribute/index.md) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
