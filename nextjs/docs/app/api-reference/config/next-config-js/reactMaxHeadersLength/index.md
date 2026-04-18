---
title: "reactMaxHeadersLength"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength"
canonical_url: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:08:18.934Z"
content_hash: "da4d75dd04b131f0cdcd8eb823f0e93dcfe0bd14982e71ec8b7257e2de2a13e1"
menu_path: ["reactMaxHeadersLength"]
section_path: []
nav_prev: {"path": "nextjs/docs/app/api-reference/config/next-config-js/reactCompiler/index.md", "title": "reactCompiler"}
nav_next: {"path": "nextjs/docs/app/api-reference/config/next-config-js/reactStrictMode/index.md", "title": "reactStrictMode"}
---

# reactMaxHeadersLength

Last updated April 15, 2026

During prerendering, React can emit headers that can be added to the response. These can be used to improve performance by allowing the browser to preload resources like fonts, scripts, and stylesheets. The default value is `6000`, but you can override this value by configuring the `reactMaxHeadersLength` option in `next.config.js`:

next.config.js

```
module.exports = {
  reactMaxHeadersLength: 1000,
}
```

> **Good to know**: This option is only available in App Router.

Depending on the type of proxy between the browser and the server, the headers can be truncated. For example, if you are using a reverse proxy that doesn't support long headers, you should set a lower value to ensure that the headers are not truncated.

[Previous

reactCompiler

](/docs/app/api-reference/config/next-config-js/reactCompiler)

[Next

reactStrictMode

](/docs/app/api-reference/config/next-config-js/reactStrictMode)

Was this helpful?

supported.

Send
