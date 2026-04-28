---
title: "reactStrictMode"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:39.290Z"
content_hash: "c4f30c45d5ba0f798b22859e759113e8bee5251ee9194e933c29b2d7f270a26e"
menu_path: ["reactStrictMode"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize/index.md", "title": "experimental.proxyClientMaxBodySize"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/redirects/index.md", "title": "redirects"}
---

# reactStrictMode

Last updated April 23, 2026

> **Good to know**: Since Next.js 13.5.1, Strict Mode is `true` by default with `app` router, so the above configuration is only necessary for `pages`. You can still disable Strict Mode by setting `reactStrictMode: false`.

> **Suggested**: We strongly suggest you enable Strict Mode in your Next.js application to better prepare your application for the future of React.

React's [Strict Mode](https://react.dev/reference/react/StrictMode) is a development mode only feature for highlighting potential problems in an application. It helps to identify unsafe lifecycles, legacy API usage, and a number of other features.

The Next.js runtime is Strict Mode-compliant. To opt-in to Strict Mode, configure the following option in your `next.config.js`:

next.config.js

```
module.exports = {
  reactStrictMode: true,
}
```

If you or your team are not ready to use Strict Mode in your entire application, that's OK! You can incrementally migrate on a page-by-page basis using `<React.StrictMode>`.

Was this helpful?
