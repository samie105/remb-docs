---
title: "viewTransition"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:09:06.895Z"
content_hash: "c719aa34879c4ff27ef654fd94a73580b474a801c2d972b5e402f1bed82991f1"
menu_path: ["viewTransition"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/useLightningcss/index.md", "title": "useLightningcss"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/webpack/index.md", "title": "Custom Webpack Config"}
---

# viewTransition

This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on [GitHub](https://github.com/vercel/next.js/issues).

Last updated April 15, 2026

`viewTransition` enables React's [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) integration in Next.js. This lets you animate navigations, loading states, and content changes using the native browser View Transitions API.

To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
}
 
module.exports = nextConfig
```

The [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition) component is provided by React. The `experimental.viewTransition` flag enables Next.js integration, such as triggering transitions during route navigations.

## Usage[](#usage)

You can import the [`<ViewTransition>` Component](https://react.dev/reference/react/ViewTransition) from React in your application:

```
import { ViewTransition } from 'react'
```

### Live Demo[](#live-demo)

Check out the [View Transitions Demo](https://react-view-transitions-demo.labs.vercel.dev) to see this feature in action, or read the [designing view transitions guide](/docs/app/guides/view-transitions) for a step-by-step walkthrough.

The View Transitions API is a baseline web standard, and browser support continues to expand. As React's [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition) component evolves, more transition patterns and use cases will become available.

[Previous

useLightningcss

](/docs/app/api-reference/config/next-config-js/useLightningcss)

[Next

webpack

](/docs/app/api-reference/config/next-config-js/webpack)

Was this helpful?

supported.

Send
