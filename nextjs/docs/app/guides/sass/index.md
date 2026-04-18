---
title: "How to use Sass"
source: "https://nextjs.org/docs/app/guides/sass"
canonical_url: "https://nextjs.org/docs/app/guides/sass"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:16:11.112Z"
content_hash: "af2f1931c98bccff48c282f5de73532af5cb81b0488a4524408819130e85de22"
menu_path: ["How to use Sass"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/guides/rendering-philosophy/index.md", "title": "Next.js Rendering Philosophy"}
nav_next: {"path": "nextjs/docs/app/guides/scripts/index.md", "title": "How to load and optimize scripts"}
---

# How to use Sass

Last updated April 15, 2026

Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.

First, install [`sass`](https://github.com/sass/sass):

pnpmnpmyarnbun

Terminal

```
pnpm add -D sass
```

> **Good to know**:
> 
> Sass supports [two different syntaxes](https://sass-lang.com/documentation/syntax), each with their own extension. The `.scss` extension requires you use the [SCSS syntax](https://sass-lang.com/documentation/syntax#scss), while the `.sass` extension requires you use the [Indented Syntax ("Sass")](https://sass-lang.com/documentation/syntax#the-indented-syntax).
> 
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").

### Customizing Sass Options[](#customizing-sass-options)

If you want to configure your Sass options, use `sassOptions` in `next.config`.

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}
 
export default nextConfig
```

#### Implementation[](#implementation)

You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the [`sass`](https://www.npmjs.com/package/sass) package.

next.config.ts

TypeScript

JavaScriptTypeScript

```
import type { NextConfig } from 'next'
 
const nextConfig: NextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}
 
export default nextConfig
```

### Sass Variables[](#sass-variables)

Next.js supports Sass variables exported from CSS Module files.

For example, using the exported `primaryColor` Sass variable:

app/variables.module.scss

```
$primary-color: #64ff00;
 
:export {
  primaryColor: $primary-color;
}
```

app/page.js

```
// maps to root `/` URL
 
import variables from './variables.module.scss'
 
export default function Page() {
  return <h1 style={{ color: variables.primaryColor }}>Hello, Next.js!</h1>
}
```

[Previous

Rendering Philosophy

](/docs/app/guides/rendering-philosophy)

[Next

Scripts

](/docs/app/guides/scripts)

Was this helpful?

supported.

Send


