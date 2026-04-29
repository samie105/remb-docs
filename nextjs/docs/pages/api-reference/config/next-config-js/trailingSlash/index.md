---
title: "trailingSlash"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash"
canonical_url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:20:50.775Z"
content_hash: "5087c665c5db0944830e3c4a84814915aa86c63679fedf38d34ac0c42f7af8c9"
menu_path: ["trailingSlash"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "../serverExternalPackages/index.md", "title": "serverExternalPackages"}
nav_next: {"path": "../transpilePackages/index.md", "title": "transpilePackages"}
---

# trailingSlash

Last updated April 23, 2026

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

-   Static file URLs, such as files with extensions.
-   Any paths under `.well-known/`.

For example, the following URLs will remain unchanged: `/file.txt`, `images/photos/picture.png`, and `.well-known/subfolder/config.json`.

When used with [`output: "export"`](/docs/app/guides/static-exports) configuration, the `/about` page will output `/about/index.html` (instead of the default `/about.html`).

## Version History[](#version-history)

| Version | Changes |
| --- | --- |
| `v9.5.0` | `trailingSlash` added. |

Was this helpful?
