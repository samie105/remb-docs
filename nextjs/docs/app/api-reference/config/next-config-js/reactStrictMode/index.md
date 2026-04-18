---
title: "reactStrictMode"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:19.927Z"
content_hash: "ce956c826750b2732860b5cd3648534c596e9f9c9d6c40e08698e32dc7f2307c"
menu_path: ["reactStrictMode"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength/index.md", "title": "reactMaxHeadersLength"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/redirects/index.md", "title": "redirects"}
---

# reactStrictMode

Last updated April 15, 2026

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

[Previous

reactMaxHeadersLength

](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)

[Next

redirects

](/docs/app/api-reference/config/next-config-js/redirects)

Was this helpful?

supported.

Send
