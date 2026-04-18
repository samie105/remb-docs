---
title: "trailingSlash"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-18T13:21:27.316Z"
content_hash: "df273a2c44c4d44b11c429dcc9b9fe1f5530476d1b92eebcc9ec4fa81e3e6620"
menu_path: ["trailingSlash"]
section_path: []
nav_prev: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/serverExternalPackages/index.md", "title": "serverExternalPackages"}
nav_next: {"path": "nextjs/docs/pages/api-reference/config/next-config-js/transpilePackages/index.md", "title": "transpilePackages"}
---

# trailingSlash

Last updated April 15, 2026

By default Next.js will redirect URLs with trailing slashes to their counterpart without a trailing slash. For example `/about/` will redirect to `/about`. You can configure this behavior to act the opposite way, where URLs without trailing slashes are redirected to their counterparts with trailing slashes.

Open `next.config.js` and add the `trailingSlash` config:

next.config.js

```
module.exports = {
  trailingSlash: true,
}
```

With this option set, URLs like `/about` will redirect to `/about/`.

When using `trailingSlash: true`, certain URLs are exceptions and will not have a trailing slash appended:

*   Static file URLs, such as files with extensions.
*   Any paths under `.well-known/`.

For example, the following URLs will remain unchanged: `/file.txt`, `images/photos/picture.png`, and `.well-known/subfolder/config.json`.

When used with [`output: "export"`](/docs/app/guides/static-exports) configuration, the `/about` page will output `/about/index.html` (instead of the default `/about.html`).

## Version History[](#version-history)

Version

Changes

`v9.5.0`

`trailingSlash` added.

Was this helpful?

supported.

Send
